<template>
    <div class="card" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">Nombre: {{i?.fact_nombre}}</h5>
        </div>
        <ul class="list-group list-group-flush">
          <th class="list-group-item">Precio: {{i?.fact_precio}}</th>
          <th class="list-group-item">Tipo de servicio: {{i?.tiposervicio}}</th>
        </ul>
    </div>
</template>

<script lang="ts">
import { IFactura } from "../../models/interfaces/facturainterfaces";
export default {
    props: {
        i: {
            type: Object as () => IFactura
        }
    },
}
</script>

<style lang="scss">
</style>