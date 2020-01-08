$ie = New-Object -com internetexplorer.application
$ie.Navigate2("http://blog.msdn.com/powershell")
$ie.visible = $true
# $ie.Quit()
