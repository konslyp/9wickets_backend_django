// JavaScript Document

function Borrar(valor)
{
	if(document.getElementById("busqueda").value==valor)
		document.getElementById("busqueda").value="";		
}


function Escribir(valor)
{
	if(document.getElementById("busqueda").value=="")
		document.getElementById("busqueda").value=valor;
}

function Borrar2(valor)
{
	if(document.getElementById("busqueda2").value==valor)
		document.getElementById("busqueda2").value="";		
}


function Escribir2(valor)
{
	if(document.getElementById("busqueda2").value=="")
		document.getElementById("busqueda2").value=valor;
}