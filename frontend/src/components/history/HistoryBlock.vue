<script setup>
import normalizeColor from '../../scripts/main.js'

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
    const time = new Date(timestamp);
    const hours = time.getHours();
    const minutes = time.getMinutes();
    return `${hours}:${minutes}`;
}

const color = normalizeColor(props.history.color)
const date = normalizeDate(props.history.datetime)
const time = normalizeTime(props.history.datetime)
console.log(time);
</script>
<template>
    <div class="block-history" :style="`background-color: ${color};`">
        <div class="decoration">
            <div class="wrapper">
                <div class="name">
                    <p>{{ history.name }}</p>
                </div>
                <div class="information">
                    <div class="left">
                        <div class="added">
                            added
                        </div>
                        <div class="time-intensive">
                            <p>{{ history.time_intensive }} min.</p>
                        </div>
                    </div>
                    
                    <div class="datetime">
                        <div class="date">
                            <p>{{ date }}</p>
                        </div>
                        <div class="time">
                            <p>{{ time }}</p>
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

            
            .information
                display: flex
                align-items: center
                justify-content: space-between
                font-family: "JetBrains Light",sans-serif
                font-size: 25px


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

                .datetime
                    display: flex
                    font-size: 16px
                    color: #A5A5A5



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

                &:hover,
                &:active
                    background-color: #773A3A
                



</style>