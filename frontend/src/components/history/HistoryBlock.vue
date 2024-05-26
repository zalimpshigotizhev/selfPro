<script setup>
import { normalizeColor, getText } from '../../scripts/main.js'

const props = defineProps({
    history:{
        type: Object,
        required: true
    }
})


function normalizeDate(timestamp){
    const date = new Date(timestamp);
    const year = date.getFullYear();
    const month = date.getMonth() + 1;
    const day = date.getDate();
    return `${year}.${month}.${day}`
}

function normalizeTime(timestamp){
    const date = new Date(timestamp);
    const hours = date.getHours();
    const minutes = date.getMinutes();
    return `${hours}:${minutes}`;
}


const normalizeData = {
    "name": getText(props.history.name, 9),
    "color": normalizeColor(props.history.color),
    "time_intensive": props.history.time_intensive,
    "date": normalizeDate(props.history.datetime),
    "time": normalizeTime(props.history.datetime),

}

console.log(normalizeData.time_intensive);
</script>
<template>
    <div class="block-history" :style="`background-color: ${normalizeData.color};`">
        <div class="decoration">
            <div class="wrapper">
                <div class="name">
                    <VTooltip>
                        <p >{{ normalizeData.name }}</p>
                        <template #popper>
                            <div class="tip">
                                {{ history.name }} 
                            </div>
                        </template>
                    </VTooltip>
                </div>
                <div class="information">
                    <div class="left">
                        <div class="added">
                            added
                        </div>
                        <div class="time-intensive">
                            <p>{{ normalizeData.time_intensive }} min.</p>
                        </div>
                    </div>
                    
                    <div class="datetime">
                        <div class="date">
                            <p>{{ normalizeData.date }}</p>
                        </div>
                        <div class="time">
                            <p>{{ normalizeData.time }}</p>
                        </div>
                    </div>
    
                </div>
            </div>
            <div class="right">
                <div class="delete">
    
                </div>
            </div>
        </div>

    </div>
</template>
<style lang="sass" scoped>
@import '../../assets/style/main'

.block-history
    display: flex
    width: 80%
    height: 172px
    background-color: red
    border-radius: 25px
    padding-left: 2em
    border: solid #E1E1E1
    margin-bottom: 30px

    @include respond-to(sm)
        font-size: 15px
        height: 132px


    .decoration
        display: flex
        width: 100%
        padding: 0 40px

        @include respond-to(lg)
            padding: 0 

        .wrapper
            display: flex
            flex-direction: column
            width: 85%

            .name
                font-family: "JetBrains Medium"
                font-size: 40px
                width: 80%
                padding: 17px 0

                @include respond-to(lg)
                    font-size: 35px
                    width: 70%

                @include respond-to(md)
                    font-size: 30px
                    width: 60%

                @include respond-to(xs)
                    font-size: 25px
                    width: 60%
    

            
            .information
                display: flex
                align-items: center
                justify-content: space-between
                font-family: "JetBrains Light",sans-serif
                font-size: 25px

                @include respond-to(sm)
                    font-size: 15px

                .left
                    display: flex
                    align-items: center
                    .added
                        display: flex
                        align-items: center
                        justify-content: center
                        color: #51BF55
                        font-family: "JetBrains Thin", sans-serif
                        font-size: 32px
                        width: 140px
                        height: 50px
                        background-color: #E9E9E9
                        border: 1px solid 
                        border-radius: 37px
                        margin-right: 30px 

                        @include respond-to(sm)
                            width: 70px
                            height: 25px
                            font-size: 13px


                .datetime
                    display: flex
                    font-size: 16px
                    color: #A5A5A5

                    @include respond-to(sm)
                        flex-direction: column
                        align-items: center
                        font-size: 12px

                    .date
                        padding-right: 15px 

                
                
                    
        

        .right
            display: flex
            justify-content: center
            align-items: center
            width: 20%
            .delete
                cursor: pointer
                width: 51px
                height: 51px
                border-radius: 50px 
                background: url("../../assets/img/delete.png")
                background-size: 65%
                background-position: center center
                background-repeat: no-repeat
                background-color: #591C1C
                
                @include respond-to(sm)
                    background-size: 50%

                &:hover,
                &:active
                    background-color: #773A3A
                
                @include respond-to(sm)
                    width: 25.5px
                    height: 25.5px

    
                



</style>