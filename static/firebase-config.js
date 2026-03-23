import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-storage.js";

const firebaseConfig = {
    apiKey: "VOTRE_API_KEY",
    authDomain: "meshora-benin.firebaseapp.com",
    projectId: "meshora-benin",
    storageBucket: "meshora-benin.appspot.com",
    messagingSenderId: "VOTRE_ID",
    appId: "VOTRE_APP_ID"
};

const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
export const storage = getStorage(app);
