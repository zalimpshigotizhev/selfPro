<script setup>
import { reactive, ref } from 'vue'


const formLabelAlign = reactive({
  name: '',
  email: '',
  password: '',
  repeat_password: ''
})

const props = defineProps({
    imgUrl: {
        type: String,
        required: true
        }
})

const form = ref("reg")


function setState (val){
    form = val
}
// todo: Доделать состояние form (Войти/Рег) через useRootStore


// export default {
    
// }
</script>
<template>
    <div class="root">
        <div :style="`background-image: url(${imgUrl})`" class="img"></div>
        <!-- <img src="../../assets/img/neuron.png" alt=""> -->
        <div class="main">
            <h1>Регистрация</h1>
            <div class="form">
                <el-form
                label-position="top"
                label-width="auto"
                :model="formLabelAlign"
                style="max-width: 600px"
                >
                    <el-form-item label="Name">
                        <el-input v-model="formLabelAlign.name" />
                    </el-form-item>
                    <el-form-item label="Email">
                        <el-input v-model="formLabelAlign.email" />
                    </el-form-item>
                    <el-form-item label="Password">
                        <el-input v-model="formLabelAlign.password" />
                    </el-form-item>
                    <el-form-item label="Repeat Password">
                        <el-input v-model="formLabelAlign.repeat_password" />
                    </el-form-item>
                </el-form>
            </div>
            <div class="btns">
                <el-button type="success" round class="btn-reg">Зарегистрироваться</el-button>
                <p>или</p>
                <el-button type="success" round class="btn-join">Войти</el-button>
            </div>
        </div>
    </div>
</template>
<style lang="sass" scoped>
@import '../../assets/style/main'

.root
    display: flex
    min-height: 100vh
    background-color: $background

.img
    width: 50%
    background-repeat: no-repeat
    background-position-x: auto
    background-position: center center

.main
    position: relative
    width: 50%
    padding: 32px 40px

.form
    min-height: 350px

h1
    font-family: "JetBrains ExtraBold", sans-serif
    font-size: 45px

.btns
    display: flex
    align-items: center
    font-family: "JetBrains ExtraLight", sans-serif

    button
        font-family: "JetBrains ExtraLight", sans-serif
        

    .btn-reg
        margin: 10px
        background-color: #247531
        border: none
        padding: 20px

    
    .btn-join
        margin: 10px
        background-color: #7E2753
        border: none
        padding: 10px





    

        
</style>