<template >
    <div class="flex justify-center mt-10 py-16 bg-blue-200 mx-10 rounded-3xl shadow-xl h-96">
        <div class="grid-rows-6">
            <h1 class="row-span-1 text-3xl font-bold mb-6">註冊/登入</h1>
            <div class="row-span-5" id="buttonDiv">
            </div>
        </div>
    </div>
</template>

<script>
import { inject } from 'vue'
import jwt_decode from 'jwt-decode'

export default {
    setup() {
        const login_uri = `${process.env.VUE_APP_IP}/api/users/login/google`
        const axios = inject('axios')

        async function handleCredentialResponse(response) {
            let responsePayload = jwt_decode(response.credential)
            await axios.post(login_uri, {
                "email": responsePayload.email,
                "name": responsePayload.name,
                "picture": responsePayload.picture
                
            })
            .then(response => {
                let message = response.message
                // let token = response.token
                if (message == "success") {
                    alert('登入成功')
                } else {
                    alert('登入失敗')
                }
            })
            .then(err => {
                console.log(err)
                alert('登入失敗')
            })
        }

        window.onload = function () {
            window.google.accounts.id.initialize({
                client_id: "901685356696-alg01ludm440m6q6hsgjr0rhuomguurb.apps.googleusercontent.com",
                callback: handleCredentialResponse
            });
            window.google.accounts.id.renderButton(
                document.getElementById("buttonDiv"),
                { 
                    theme: "outline", 
                    type: "standard",
                    shape: "pill",
                    size: "large" 
                }  // customization attributes
            );
            window.google.accounts.id.prompt((notification) => {
                if (notification.isNotDisplayed() || notification.isSkippedMoment()) {
                    // try next provider if OneTap is not displayed or skipped
                }
            });
        }

        return {
            login_uri,
            handleCredentialResponse
        }
    }
}
</script>