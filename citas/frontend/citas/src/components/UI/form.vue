<template>
    <div class="card card-border-color card-border-color-primary w-75 mx-auto">
        <div class="card-header card-header-divider text-center fs-4">Llena el Formulario de Factura</div>
        <div class="card-body">
            <div class="form-group">
                <label for="" class="form-label">Nombre</label>
                <input type="text" v-model="factura.fact_nombre" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="" class="form-label">Precio</label>
                <input type="text" v-model="factura.fact_precio" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="tiposervicio" class="form-label">Tipo de Servicio</label>
                <input type="text" v-model="factura.tiposervicio" id="tiposervicio" class="form-control"
                    required>
            </div>
            <div class="d-flex flex-row justify-content-around">
                <button class="btn btn-success w-25" onclick="submitData(factura)">Guardar</button>
                <router-link to="/facturas/all/" class="btn btn-danger w-25">Cancelar</router-link>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { IFactura } from '../../models/interfaces/facturainterfaces';
export default {
    props: {
        factura: {
            type: Object as () => IFactura,
            required: true
        },
        submitData:{
            type: Function as ()=> any,
            
        }
    },
}
</script>

<style>
.card-header{
    background-color: cornflowerblue ;
    color:white;
}
</style>