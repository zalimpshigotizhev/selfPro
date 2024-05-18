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

const form = reactive({
  state: "reg"
})


function setState (val){
    form.state = val
}
// todo: Доделать состояние form (Войти/Рег) через useRootStore
function sendDataServer(){

}


</script>
<template>
    <div class="root">
        <div :style="`background-image: url(${imgUrl})`" class="img"></div>
        <!-- <img src="../../assets/img/neuron.png" alt=""> -->
        <div class="main" v-if="form.state == 'reg'">
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
                        <el-input v-model="formLabelAlign.password" type="password" autocomplete="off" />
                    </el-form-item>
                    <el-form-item label="Repeat Password">
                        <el-input v-model="formLabelAlign.repeat_password" type="password" autocomplete="off"  />
                    </el-form-item>
                </el-form>
            </div>
            <div class="btns">
                <el-button type="success" round class="btn-main">Зарегистрироваться</el-button>
                <p>или</p>
                <el-button type="success" round class="btn-second" @click="setState('join')">Войти</el-button>
            </div>
        </div>
        <div class="main" v-if="form.state == 'join'">
            <h1>Вход</h1>
            <div class="form">
                <el-form
                label-position="top"
                label-width="auto"
                :model="formLabelAlign"
                style="max-width: 600px"
                class="join"
                >
                    <el-form-item label="Email">
                        <el-input v-model="formLabelAlign.email" />
                    </el-form-item>

                    <el-form-item label="Password">
                        <el-input v-model="formLabelAlign.password" type="password" autocomplete="off" />
                    </el-form-item>
                    <a class="forge-password">Забыли пароль?</a>
                </el-form>
            </div>
            <div class="btns">
                <el-button type="success" round class="btn-main">Войти</el-button>
                <p>или</p>
                <el-button type="success" round class="btn-second" @click="setState('reg')">Зарегистрироваться</el-button>
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
    @media (min-width: $min-mobile) and (max-width: $max-mobile)
        display: none

.main
    position: relative
    width: 50%
    padding: 32px 40px
    @media (min-width: $min-mobile) and (max-width: $max-mobile)
        width: 100%

.form
    max-width: 450px
    min-width: 200px
    height: 350px
    min-height: 300px

h1
    font-family: "JetBrains ExtraBold", sans-serif
    font-size: 45px

.btns
    display: flex
    align-items: center
    font-family: "JetBrains ExtraLight", sans-serif

    button
        font-family: "JetBrains ExtraLight", sans-serif
        

    .btn-main
        margin: 10px
        background-color: $pretty-green
        border: none
        padding: 20px

    
    .btn-second
        margin: 10px
        background-color: $pretty-purple
        border: none
        padding: 10px

.join
    padding-top: 5em

.forge-password
    padding-left: 20em

    

        
</style>