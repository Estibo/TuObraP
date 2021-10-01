const botonesDelete=document.querySelectorAll('.btn-delete')

if(botonesDelete){
    const arreloBotones=Array.from(botonesDelete);
    arreloBotones.forEach((btn)=>{
        btn.addEventListener('click', (e)=>{
            if(!confirm('Are you sure, you want to delete it?')){
                e.preventDefault();
            }
        });
    });

}