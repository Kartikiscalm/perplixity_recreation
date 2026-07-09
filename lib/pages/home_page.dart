import 'package:flutter/material.dart';
import '../wigets/side_bar.dart';
import '../wigets/search_section.dart';
import 'package:perplixity_recreation/theme/colours.dart';

class Homepage extends StatelessWidget {
  const Homepage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: [
          SideBar(),
          Expanded(
            child: Column(
              children: [
                Expanded(child: SearchSection()), // search section
                // footer
                Container(
                  padding: EdgeInsets.symmetric(vertical: 16),
                  child: Wrap(
                    alignment: WrapAlignment.center,
                    children: [
                      Padding(
                        padding: EdgeInsets.symmetric(horizontal: 12),
                        child: Text(
                          "llm used is gemini 2.5 flash",
                          style: TextStyle(
                            fontSize: 14,
                            color: AppColors.footerGrey,
                          ),
                        ),
                      ),
                      Padding(
                        padding: EdgeInsets.symmetric(horizontal: 12),
                        child: Text(
                          "github username: Kartikiscalm",
                          style: TextStyle(
                            fontSize: 14,
                            color: AppColors.footerGrey,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
