using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using log4net;
using Tracking.Core;
using Win.Api;

namespace Tracking.App
{
    public class SystemTray : Form
    {
        private static readonly ILog _logger = LogManager.GetLogger(System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);

        internal NotifyIcon TrayIcon;
        private Dictionary<string, Icon> Icons = new Dictionary<string, Icon>();
        private ContextMenu TrayMenu;
        private Monitor desktop;
        private bool IsRunning;
        private WinApi _winApi = new WinApi();

        public SystemTray()
        {
            Initialize();
            Start();
        }

        private void Initialize()
        {
            foreach (string file in Directory.EnumerateFiles("Icons"))
            {
                FileInfo fileInfo = new FileInfo(file);
                if (fileInfo.Extension == ".ico")
                {
                    Icons.Add(fileInfo.Name.Split(new char[] { '.' })[0], new Icon(file));
                }
            }

            RefreshNotificationArea();
            InitializeTrayIcon();
            desktop = new Monitor();
        }

        private void Start()
        {
            try
            {
                desktop.Start();
                TrayIcon.Icon = Icons["green"];
            }
            catch (Exception e)
            {
                _logger.Fatal(e.Message);
            }
        }

        private void RefreshNotificationArea()
        {
            _logger.Debug("Begin refresh");
            _winApi.RefreshNotificationArea();
            _logger.Debug("End refresh");
        }

        private void InitializeTrayIcon()
        {
            _logger.Debug("Begin initializing tray icon");
            TrayMenu = new ContextMenu();
            TrayMenu.MenuItems.Add("Exit", OnExit);
            TrayMenu.MenuItems.Add("Restart", OnRefresh);
            TrayIcon = new NotifyIcon();
            TrayIcon.Text = "Agent";
            TrayIcon.ContextMenu = TrayMenu;
            TrayIcon.Visible = true;
            TrayIcon.Icon = Icons["yellow"];
            _logger.Debug("End initializing tray icon");
        }

        protected override void OnLoad(EventArgs e)
        {
            Visible = false;
            ShowInTaskbar = false;
            base.OnLoad(e);
        }

        private void OnExit(object sender, EventArgs e)
        {
            _logger.Info("Exiting.");
            Application.Exit();
            _logger.Info("Exited.");
        }

        private void OnRefresh(object ender, EventArgs e)
        {
            _logger.Info("Restarting.");
            _logger.Info("Restarted.");
        }

        protected override void Dispose(bool isDisposing)
        {
            if (isDisposing)
            {
                TrayIcon.Dispose();
            }

            base.Dispose(isDisposing);
        }
    }
}
