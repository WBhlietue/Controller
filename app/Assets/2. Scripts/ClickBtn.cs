using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

public class ClickBtn : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler, IPointerDownHandler
{
    public string btnName;
    public bool isWork = true;
    bool isEnter = false;



    public void OnPointerEnter(PointerEventData eventData)
    {
        // SendInfo(1);
        // Vibrate();
    }

    public void OnPointerExit(PointerEventData eventData)
    {
        SendInfo(0);
    }
    public void SendInfo(int status)
    {
         if(!isWork){
            return;
        }
        MainManager.instance.SendData(btnName, status);
    }

    void Vibrate(){
        if(!isWork){
            return;
        }
        if(CheckIP.vibrate){
            Handheld.Vibrate();
        }
    }

    public void OnPointerDown(PointerEventData eventData)
    {
        SendInfo(1);
        Vibrate();
    }
}
