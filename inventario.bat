@echo off
 set /p ubicacion= Nombre de la persona a cargo del equipo: 
 set /p grupo= Nombre del departamento que pertenece: 
 set /p carpeta= Tiene habilitado opcion de carpetas compartidas?: 
 set /p usb= Tiene acceso a USB'S?: 

 

 MKDIR \\131.107.5.64\listado\"%grupo%"  

 echo %ubicacion%  >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"

 echo %grupo% >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
 echo %carpeta% >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
 echo %usb%  >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"

 wmic csproduct get vendor >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
 wmic csproduct get name >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
 wmic bios get serialnumber >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
 wmic nicconfig get IPAddress >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
 wmic /Output:STDOUT  CPU get Name >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
 wmic logicaldisk get size >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
 wmic MemoryChip get Capacity >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
 wmic os get Caption >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
 wmic path softwarelicensingservice get oa3xoriginalproductkey >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
 wmic computersystem get NAME, USERNAME, DOMAIN,TOTALPHYSICALMEMORY /format:list >> \\131.107.5.64\listado\"%grupo%"\"%ubicacion%.txt"
 
