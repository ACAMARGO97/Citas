<template>
    <div>
        <div class="card">
            <div class="card-body text-center">
                <h2 class="fs-2">Mis Facturas</h2>
            </div>
        </div>
    </div>
    <div class="d-flex flex-row flex-wrap justify-content-around my-5">
        <template v-for="fac in factura">
            <router-link :to="{name:'updateFac',params:{id:fac.id}}">
                <CardFactura :i={...fac} />
            </router-link>
        </template>
    </div>
</template>

<script lang="ts" >
import { store } from "../../../context/store";
import CardFactura from "../../UI/card.vue";

export default {
    components: {
        CardFactura
    },
    data() {
        return {
            factura: [...store.state.verFactura]
        }
    },
    mounted() {
        store.commit('getAllFactura', "http://127.0.0.1:8000/facturas/fall/")
    }
}
</script>

<style scoped >
</style>