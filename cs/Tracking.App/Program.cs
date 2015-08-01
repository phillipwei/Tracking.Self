using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using log4net;
using log4net.Config;

namespace Tracking.App
{
    static class Program
    {
        private static readonly ILog _logger = LogManager.GetLogger(System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);

        [STAThread]
        static void Main()
        {
            XmlConfigurator.Configure(new System.IO.FileInfo("log4net.xml"));
            try
            {
                Application.Run(new SystemTray());
            }
            catch (Exception e)
            {
                _logger.Fatal(e.Message + " " + e.StackTrace);
            }
        }
    }
}
