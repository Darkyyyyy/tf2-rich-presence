; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "TF2 Rich Presence"
#define MyAppVersion "2.1.6"
#define MyAppPublisher "Kataiser"
#define MyAppURL "https://github.com/Kataiser/tf2-rich-presence"
#define MyAppExeName "TF2 Rich Presence.bat"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{AF2C6EA0-F807-48BC-ACE3-DBC523DC4325}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} v{#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=.
OutputBaseFilename=TF2RichPresence_v{#MyAppVersion}_setup
SetupIconFile=tf2_logo_blurple.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
WizardImageFile=tf2_logo_blurple_installer.bmp
RestartApplications=no
ExtraDiskSpaceRequired=250

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"
Name: "dutch"; MessagesFile: "compiler:Languages\Dutch.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"
Name: "polish"; MessagesFile: "compiler:Languages\Polish.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Dirs]
Name: "{userappdata}\TF2 Rich Presence"; Flags: setntfscompression
Name: "{userappdata}\TF2 Rich Presence\logs"; Flags: setntfscompression

[Files]
Source: "TF2 Rich Presence v{#MyAppVersion}\License.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "TF2 Rich Presence v{#MyAppVersion}\Readme.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "TF2 Rich Presence v{#MyAppVersion}\Changelogs.html"; DestDir: "{app}"; Flags: ignoreversion
Source: "TF2 Rich Presence v{#MyAppVersion}\TF2 Rich Presence.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "TF2 Rich Presence v{#MyAppVersion}\resources\*"; DestDir: "{app}\resources"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "TF2 Rich Presence v{#MyAppVersion}\locales\*"; DestDir: "{app}\locales"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\resources\tf2_logo_blurple.ico"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\resources\tf2_logo_blurple.ico"; Tasks: desktopicon

[InstallDelete]
Type: files; Name: "{app}\resources\*.pyd"
Type: files; Name: "{app}\resources\*.py"
Type: filesandordirs; Name: "{app}\resources\gui_images"
Type: filesandordirs; Name: "{app}\resources\packages"
Type: filesandordirs; Name: "{app}\resources\python-*-embed-win32"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
