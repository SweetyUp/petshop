using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
using System.Collections;

public class SendRequestOnClick : MonoBehaviour
{
    public Button yourButton;
    public GameObject itemObject; // 场景中的物体

    void Start()
    {
        Button btn = yourButton.GetComponent<Button>();
        btn.onClick.AddListener(TaskOnClick);
    }

    void TaskOnClick()
    {
        string itemName = itemObject.name;
        StartCoroutine(SendRequest(itemName));
    }

    IEnumerator SendRequest(string itemName)
    {
        string jsonData = "{\"message\":\"" + itemName + "\"}";
        string url = "http://127.0.0.1:8001/get_evaluate/"; // 替换为你的API接口

        UnityWebRequest request = new UnityWebRequest(url, "POST");
        byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(jsonData);
        request.uploadHandler = (UploadHandler)new UploadHandlerRaw(bodyRaw);
        request.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        yield return request.SendWebRequest();

        if (request.result != UnityWebRequest.Result.Success)
        {
            Debug.Log("Error: " + request.error);
        }
        else
        {
            Debug.Log("Response: " + request.downloadHandler.text);
        }
    }
}
