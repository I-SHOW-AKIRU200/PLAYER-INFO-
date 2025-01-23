import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to fetch player stats from the external API
def get_player_stats(uid, region):
    api_key = "PRINCE-PERM-KEY"  # Hardcoded API key

    url = f'https://freefireinfoapiv2lk-team.vercel.app/api/playerstats?uid={uid}&region={region}&api_key={api_key}'
    
    try:
        res = requests.get(url)
        if res.status_code != 200:
            return {"error": "Failed to fetch player stats"}
        
        player_data = res.json()

        # Extract credit at the top of the response
        credit = player_data.get("I_SHOW_AKIRU", "N/A")

        # Add your Telegram username and YouTube channel link
        telegram_username = "@I_SHOW_AKIRU"  # Replace with your actual Telegram username
        youtube_channel_link = "https://youtube.com/@ishowakiru?si=a_-y0-KOSBjHUu3a"  # Replace with your actual YouTube channel link

        # Formatting the response
        response = {
            "credit": credit,  # Credit at the top
            "telegram_username": telegram_username,
            "youtube_channel": youtube_channel_link,
            "AccountInfo": {
                "AccountAvatarId": player_data.get("AccountInfo", {}).get("AccountAvatarId", "N/A"),
                "AccountBPBadges": player_data.get("AccountInfo", {}).get("AccountBPBadges", "N/A"),
                "AccountBPID": player_data.get("AccountInfo", {}).get("AccountBPID", "N/A"),
                "AccountBannerId": player_data.get("AccountInfo", {}).get("AccountBannerId", "N/A"),
                "AccountCreateTime": player_data.get("AccountInfo", {}).get("AccountCreateTime", "N/A"),
                "AccountEXP": player_data.get("AccountInfo", {}).get("AccountEXP", "N/A"),
                "AccountLastLogin": player_data.get("AccountInfo", {}).get("AccountLastLogin", "N/A"),
                "AccountLevel": player_data.get("AccountInfo", {}).get("AccountLevel", "N/A"),
                "AccountLikes": player_data.get("AccountInfo", {}).get("AccountLikes", "N/A"),
                "AccountName": player_data.get("AccountInfo", {}).get("AccountName", "N/A"),
                "AccountRegion": player_data.get("AccountInfo", {}).get("AccountRegion", "N/A"),
                "AccountSeasonId": player_data.get("AccountInfo", {}).get("AccountSeasonId", "N/A"),
                "AccountType": player_data.get("AccountInfo", {}).get("AccountType", "N/A"),
                "BrMaxRank": player_data.get("AccountInfo", {}).get("BrMaxRank", "N/A"),
                "BrRankPoint": player_data.get("AccountInfo", {}).get("BrRankPoint", "N/A"),
                "CsMaxRank": player_data.get("AccountInfo", {}).get("CsMaxRank", "N/A"),
                "CsRankPoint": player_data.get("AccountInfo", {}).get("CsRankPoint", "N/A"),
                "EquippedWeapon": player_data.get("AccountInfo", {}).get("EquippedWeapon", "N/A"),
                "EquippedWeaponImages": player_data.get("AccountInfo", {}).get("EquippedWeaponImages", "N/A"),
                "ReleaseVersion": player_data.get("AccountInfo", {}).get("ReleaseVersion", "N/A"),
                "Role": player_data.get("AccountInfo", {}).get("Role", "N/A"),
                "ShowBrRank": player_data.get("AccountInfo", {}).get("ShowBrRank", "N/A"),
                "ShowCsRank": player_data.get("AccountInfo", {}).get("ShowCsRank", "N/A"),
                "Title": player_data.get("AccountInfo", {}).get("Title", "N/A"),
                "hasElitePass": player_data.get("AccountInfo", {}).get("hasElitePass", "N/A"),
            },
            "AccountProfileInfo": {
                "EquippedOutfit": player_data.get("AccountProfileInfo", {}).get("EquippedOutfit", "N/A"),
                "EquippedOutfitImages": player_data.get("AccountProfileInfo", {}).get("EquippedOutfitImages", "N/A"),
                "EquippedSkills": player_data.get("AccountProfileInfo", {}).get("EquippedSkills", "N/A")
            },
            "GuildInfo": {
                "GuildCapacity": player_data.get("GuildInfo", {}).get("GuildCapacity", "N/A"),
                "GuildID": player_data.get("GuildInfo", {}).get("GuildID", "N/A"),
                "GuildLevel": player_data.get("GuildInfo", {}).get("GuildLevel", "N/A"),
                "GuildMember": player_data.get("GuildInfo", {}).get("GuildMember", "N/A"),
                "GuildName": player_data.get("GuildInfo", {}).get("GuildName", "N/A"),
                "GuildOwner": player_data.get("GuildInfo", {}).get("GuildOwner", "N/A")
            },
            "captainBasicInfo": {
                "AvatarImage": player_data.get("captainBasicInfo", {}).get("AvatarImage", "N/A"),
                "BannerImage": player_data.get("captainBasicInfo", {}).get("BannerImage", "N/A"),
                "EquippedWeapon": player_data.get("captainBasicInfo", {}).get("EquippedWeapon", "N/A"),
                "accountId": player_data.get("captainBasicInfo", {}).get("accountId", "N/A"),
                "accountType": player_data.get("captainBasicInfo", {}).get("accountType", "N/A"),
                "badgeCnt": player_data.get("captainBasicInfo", {}).get("badgeCnt", "N/A"),
                "badgeId": player_data.get("captainBasicInfo", {}).get("badgeId", "N/A"),
                "bannerId": player_data.get("captainBasicInfo", {}).get("bannerId", "N/A"),
                "createAt": player_data.get("captainBasicInfo", {}).get("createAt", "N/A"),
                "csMaxRank": player_data.get("captainBasicInfo", {}).get("csMaxRank", "N/A"),
                "csRank": player_data.get("captainBasicInfo", {}).get("csRank", "N/A"),
                "csRankingPoints": player_data.get("captainBasicInfo", {}).get("csRankingPoints", "N/A"),
                "exp": player_data.get("captainBasicInfo", {}).get("exp", "N/A"),
                "headPic": player_data.get("captainBasicInfo", {}).get("headPic", "N/A"),
                "lastLoginAt": player_data.get("captainBasicInfo", {}).get("lastLoginAt", "N/A"),
                "level": player_data.get("captainBasicInfo", {}).get("level", "N/A"),
                "liked": player_data.get("captainBasicInfo", {}).get("liked", "N/A"),
                "maxRank": player_data.get("captainBasicInfo", {}).get("maxRank", "N/A"),
                "nickname": player_data.get("captainBasicInfo", {}).get("nickname", "N/A"),
                "pinId": player_data.get("captainBasicInfo", {}).get("pinId", "N/A"),
                "rank": player_data.get("captainBasicInfo", {}).get("rank", "N/A"),
                "rankingPoints": player_data.get("captainBasicInfo", {}).get("rankingPoints", "N/A"),
                "region": player_data.get("captainBasicInfo", {}).get("region", "N/A"),
                "releaseVersion": player_data.get("captainBasicInfo", {}).get("releaseVersion", "N/A"),
                "seasonId": player_data.get("captainBasicInfo", {}).get("seasonId", "N/A"),
                "showBrRank": player_data.get("captainBasicInfo", {}).get("showBrRank", "N/A"),
                "showCsRank": player_data.get("captainBasicInfo", {}).get("showCsRank", "N/A"),
                "title": player_data.get("captainBasicInfo", {}).get("title", "N/A")
            },
            "creditScoreInfo": {
                "creditScore": player_data.get("creditScoreInfo", {}).get("creditScore"),
                "periodicSummaryEndTime": player_data.get("creditScoreInfo", {}).get("periodicSummaryEndTime", "N/A"),
                "periodicSummaryStartTime": player_data.get("creditScoreInfo", {}).get("periodicSummaryStartTime", "N/A"),
                "rewardState": player_data.get("creditScoreInfo", {}).get("rewardState", "N/A")
            },
            "petInfo": {
                "exp": player_data.get("petInfo", {}).get("exp", "N/A"),
                "id": player_data.get("petInfo", {}).get("id", "N/A"),
                "isSelected": player_data.get("petInfo", {}).get("isSelected", "N/A"),
                "level": player_data.get("petInfo", {}).get("level", "N/A"),
                "name": player_data.get("petInfo", {}).get("name", "N/A"),
                "selectedSkillId": player_data.get("petInfo", {}).get("selectedSkillId", "N/A"),
                "skinId": player_data.get("petInfo", {}).get("skinId", "N/A")
            },
            "socialinfo": {
                "AccountLanguage": player_data.get("socialinfo", {}).get("AccountLanguage", "N/A"),
                "AccountPreferMode": player_data.get("socialinfo", {}).get("AccountPreferMode", "N/A"),
                "AccountSignature": player_data.get("socialinfo", {}).get("AccountSignature", "N/A")
            }
        }
        
        return response

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/AKIRU_info', methods=['GET'])
def player_info():
    player_uid = request.args.get('player_uid')
    region = request.args.get('region')

    if not player_uid or not region:
        return jsonify({"error": "Player UID and region are required"}), 400

    player_info = get_player_stats(player_uid, region)

    if "error" in player_info:
        return jsonify(player_info), 500

    return jsonify(player_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # No SSL
