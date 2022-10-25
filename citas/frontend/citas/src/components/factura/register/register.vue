<template>
    <Form :factura="factura" :submit-data="submitData" />
</template>

<script lang="ts">
import { IFactura } from '../../../models/interfaces/facturainterfaces';
import Form from '../../UI/form.vue';
import { store } from "../../../context/store";

const factura: IFactura = {
    fact_nombre: '',
    fact_precio: '',
    tiposervicio: '',
};
export default {
    data() {
        return {
            factura: factura
        }
    },
    methods: {
        submitData(factura: IFactura) {
            store.commit('postfactura', { ...this.$data.factura, ...factura });
        }
    },
    components: {
        Form
    }
}
</script>

<style scoped >
</style>