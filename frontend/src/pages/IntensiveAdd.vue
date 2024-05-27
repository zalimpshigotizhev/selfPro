<script setup>

import Header from 'components/Header.vue'
import { useRouter } from 'vue-router';
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'


const imageUrl = ref('')
const name = ref('')
const color = ref('')

// const handleAvatarSuccess: UploadProps['onSuccess'] = (
//   response,
//   uploadFile
// ) => {
//   imageUrl.value = URL.createObjectURL(uploadFile.raw!)
// }

// const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
//   if (rawFile.type !== 'image/jpeg') {
//     ElMessage.error('Avatar picture must be JPG format!')
//     return false
//   } else if (rawFile.size / 1024 / 1024 > 2) {
//     ElMessage.error('Avatar picture size can not exceed 2MB!')
//     return false
//   }
//   return true
// }

const router = useRouter();


function goBack(){
    router.go(-1)
}
</script>
<template>
    <Header/>
    <div>
        <div class="block">
            <div class="title">Intensive Add</div>
            <div class="btns">
                <el-button type="danger" round class="second" @click="goBack()">back</el-button>
            </div>
        </div>
        <div class="back">
            <div class="wrapper">
                <div class="left">
                    <el-upload
                    class="avatar-uploader"
                    action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload"
                    >
                    <img v-if="imageUrl" :src="imageUrl" class="avatar" />
                    <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
                  </el-upload>
                </div>
                <div class="right">
                    <el-input
                    v-model="name"
                    class="input-name"
                    maxlength="64"
                    placeholder="Please input"
                    show-word-limit
                    type="text"
                    />
                    <div class="color-save">
                        <div class="color">
                            <span class="demonstration">Выберите цвет вашего интенсива</span>
                            <el-color-picker v-model="color" />
                        </div>
                        <el-button type="success" round class="btn" @click="moveIntensiveAdd()">Добавить</el-button>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>
<style lang="sass" scoped>
@import '../assets/style/main'




.title
    font-family: "JetBrains ExtraBold", sans-serif
    font-size: 64px

    @media (min-width: $min_mobile) and (max-width: $max_mobile)
        font-size: 44px

.block
    display: flex
    align-items: center
    margin-bottom: 40px
    @media (min-width: $min_mobile) and (max-width: $max_pad)
        margin-bottom: 20px
        flex-direction: column
        align-items: flex-start

    .btns
        display: flex

        button

            margin-left: 30px
            padding: 23px 25px
            font-family: "JetBrains ExtraLight", sans-serif
            font-size: 25px

            @media (min-width: $min_mobile) and (max-width: $max_pad)
                margin: 10px
                margin-right: 30px
                margin-left: 0
        .second
            background-color: #633A34
            border: none

            &:hover,
            &:active
                background-color: #844e46

.back
    display: flex
    flex-direction: column
    justify-content: center
    align-items: center
    padding-top: 1em
    background-color: #ffffff
    width: 100%
    height: 483px
    border-radius: 30px
    margin-bottom: 100px

    @include respond-to(lg)
        height: 70vh

    @include respond-to(md)
        height: 70vh

        
    


    .wrapper
        display: flex
        justify-content: center
        align-items: center
        flex-wrap: wrap
        width: 100vh
        height: auto
        @include respond-to(lg)
            width: 60vh
            flex-direction: column

        @include respond-to(xs)
            width: 30vh

        .left
            width: 50%


            @include respond-to(lg)
                width: 70%
                padding: 0
                padding-top: 30px

            @include respond-to(xs)
                width: 100%
                

            .avatar-uploader
                display: flex
                justify-content: center
                border: 1px dashed #000080
                border-radius: 6px
                position: relative
                overflow: hidden
                transition: var(--el-transition-duration-fast)

                &:hover
                    border-color: var(--el-color-primary)
    
                    
                .avatar
                    width: 178px
                    height: 178px
                    display: block
                
                
                .avatar-uploader-icon
                    font-size: 28px
                    color: #8c939d
                    width: 370px
                    height: 178px
                    text-align: center

                    &:hover
                        color: var(--el-color-primary)


        
        .right
            display: flex
            flex-direction: column
            align-items: center
            align-items: center

            width: 50%
            padding-left: 30px 
            @include respond-to(lg)
                width: 100%
                padding: 0
                padding-top: 30px


            .input-name
                width: 100%

                @include respond-to(lg)
                    max-width: 370px
                    width: 100%
                    height: 40px


            .color-save
                display: flex
                align-items: center
                justify-content: space-between
                padding-top: 30px
                .color
                    width: 70%
                    font-family: "JetBrains Regular", sans-serif
                    font-size: 15px
                    display: flex
                    flex-direction: column
                    padding-right: 30px
                    
                    @include respond-to(lg)
                        font-size: 15px

                        .el-color-picker__trigger
                            width: 30px
                            height: 30px

                .btn
                    font-family: "JetBrains Regular", sans-serif
                    font-size: 20px
                    background-color: #37ad5f
                    padding: 20px 30px

                    &:hover
                        background-color: #50c878
</style>    