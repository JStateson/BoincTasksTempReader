// sent by Fred Efmer, Boinctask/TThrottle creator
// used as reference for the format of the  tthrottle string in the python script
LRESULT CDlgPreference::OnDlgProgramsBoincTasksString(WPARAM wParam, LPARAM lParam) {
     char szHostName[MAX_PATH], cOutput[8];
     struct hostent *host;
     CStringA *psTxt, sAFormat;
     int        iFahrenheit;

     psTxt = (CStringA *) wParam;
     szHostName[0] = 0;
     gethostname( szHostName, MAX_PATH );
     host = gethostbyname(szHostName);

     theApp.m_sMessage = "<TThrottle><HN:";

     theApp.m_sMessage += szHostName;
     theApp.m_sMessage += ">";
     theApp.m_sMessage += *psTxt;
     theApp.m_sMessage += m_sTemperature;

     GenerateRandomString(cOutput, 7);
     theApp.m_sMessage += "<RS";
     theApp.m_sMessage += cOutput;
     theApp.m_sMessage += ">";

     int iCheck;
     if (theApp.m_pDlgPrograms->m_programDlgSettings.m_bActivive) iCheck = 1;
     else iCheck = 0;
     sAFormat.Format("<AA%d>",iCheck);
     theApp.m_sMessage += sAFormat;
     iFahrenheit =
theApp.m_pTemperature->ConvertToCelcius(theApp.m_pDlgPrograms->m_programDlgSettings.m_iSetCore);
     sAFormat.Format("<SC%d>",iFahrenheit);
     theApp.m_sMessage += sAFormat;
     iFahrenheit =
theApp.m_pTemperature->ConvertToCelcius(theApp.m_pDlgPrograms->m_programDlgSettings.m_iSetGpu[0]);
     sAFormat.Format("<SG%d>",iFahrenheit);
     theApp.m_sMessage += sAFormat;
sAFormat.Format("<XC%d>",theApp.m_pDlgPrograms->m_programDlgSettings.m_iMaxCpu);
     theApp.m_sMessage += sAFormat;
sAFormat.Format("<MC%d>",theApp.m_pDlgPrograms->m_programDlgSettings.m_iMinCpu);
     theApp.m_sMessage += sAFormat;

     theApp.m_sMessage += "<TX";
     sAFormat = theApp.m_pDlgPrograms->m_programDlgSettings.m_sTxt;
     theApp.m_sMessage += sAFormat;
     theApp.m_sMessage += ">";
     theApp.m_sMessage += "<TThrottle>";

     return 0;
}

