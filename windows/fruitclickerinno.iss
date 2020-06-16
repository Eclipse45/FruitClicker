; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Fruit Clicker"
#define MyAppVersion "0.8.alpha"
#define MyAppPublisher "SeaPuppy Studios"
#define MyAppURL "www.seapuppystudios.com"
#define MyAppExeName "Fruit Clicker.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{794F73B6-1413-4DF3-A953-D3FB7758C878}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=C:\Users\colli\Documents\GitHub\FruitClicker\LICENSE
InfoBeforeFile=C:\Users\colli\Documents\GitHub\FruitClicker\README.md
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\colli\Downloads
OutputBaseFilename=Fruit Clicker Setup
SetupIconFile=C:\Users\colli\Documents\GitHub\FruitClicker\windows\images\apple.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\colli\Documents\GitHub\FruitClicker\windows\Fruit Clicker.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\colli\Documents\GitHub\FruitClicker\windows\images\*"; DestDir: "{app}\images"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

