﻿using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using log4net;
//using MouseKeyboardActivityMonitor;
//using MouseKeyboardActivityMonitor.WinApi;
using Win.Api;

namespace Tracking.Core
{
    public class Monitor
    {
        private static readonly ILog _log = LogManager.GetLogger(System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);

        //private readonly KeyboardHookListener keyboardHookManager;
        //private readonly MouseHookListener mouseHookManager;

        private object _syncRoot = new object();

        private readonly TimeSpan ActivityThreshold = TimeSpan.FromMinutes(1);
        private DateTime _lastActivity = DateTime.Now;
        private WinApi _winApi = new WinApi();

        public Monitor()
        {
            //keyboardHookManager = new KeyboardHookListener(new GlobalHooker());
            //keyboardHookManager.Enabled = true;
            //keyboardHookManager.KeyDown += KeyDown;
            //mouseHookManager = new MouseHookListener(new GlobalHooker());
            //mouseHookManager.Enabled = true;
            //mouseHookManager.MouseMove += MouseMove;
            //mouseHookManager.MouseDown += MouseDown;
        }

        public void Start()
        {
            var timer = new System.Threading.Timer((Object stateInfo) => { RecordActivity(); }, 
                null, TimeSpan.Zero, ActivityThreshold);
        }

        public void RecordActivity()
        {
            try
            {
                lock (_syncRoot)
                {
                    // Skip if there's been no activity.
                    if (DateTime.Now > _lastActivity + ActivityThreshold)
                    {
                        return;
                    }
                }

                using (Bitmap image = _winApi.CaptureDesktop())
                {
                    var fileTime = DateTime.Now.ToString("yyyy.MM.dd__HH.mm.ss.ffff");
                    var filePath = Path.Combine(@"P:\Temp\Tracking.Self", fileTime + ".png");
                    image.Save(filePath);
                    _log.InfoFormat("RecordActivity: Screen Shot saved to {0}", filePath);

                    /*
                    using (MemoryStream memoryStream = new MemoryStream())
                    {
                        var fields = new System.Collections.Specialized.NameValueCollection();
                        fields.Add("datetime", DateTime.UtcNow.ToString("o"));
                        image.Save(memoryStream, System.Drawing.Imaging.ImageFormat.Png);
                        memoryStream.Position = 0;
                        var password = "???";
                        Network.HttpAuthenticatedFileUpload(
                            "http://localhost:5000/api/upload",
                            "phillipwei@gmail.com",
                            password,
                            fields,
                            "file",
                            fileTime + ".png",
                            "image/png",
                            memoryStream);
                        // File.OpenRead(fileTime + ".png"));
                    }
                    */
                }
            }
            catch (Exception e)
            {
                _log.Fatal(e.Message + e.StackTrace);
            }
        }

        public void CameraCapture()
        {

        }

        private void MouseMove(object sender, MouseEventArgs e)
        {
            lock (_syncRoot)
            {
                _lastActivity = DateTime.Now;
            }
        }

        private void MouseDown(object sender, MouseEventArgs e)
        {
            lock (_syncRoot)
            {
                _lastActivity = DateTime.Now;
            }
        }

        private void KeyDown(object sender, KeyEventArgs e)
        {
            lock (_syncRoot)
            {
                _lastActivity = DateTime.Now;
            }
        }
    }
}
