# 🧠 大模型相关研究 | 2026年10月08日

> 本类共 **303** 篇论文：已确认 **280** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-303**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-303**

---

### 301. [Valid for Free: Homophily-Gated Conformal Prediction for Training-Free Node Classification with Tabular Foundation Models](https://arxiv.org/abs/2610.08564)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nguyen Duy Long, Phung Minh Hien, Nguyen Trong Viet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) can classify the nodes of a graph without training on it, by reading node and neighborhood features as table rows next to labeled context rows. Work in this line reports predictive performance, not conformal coverage or prediction-set size. To our knowledge, we give the first reliability study of the setting, with TabICL as the TFM and half of each graph as labeled context. As for any predictor fixed before calibration, a frozen in-context predictor makes split conformal prediction exactly valid in finite samples, with no training, validation fold, or tuning on the target graph. An audit across ten graphs then shows that the training-free TabICL posterior has lower expected calibration error (ECE) than GCN with temperature scaling (GCN+TS) on nine of them. Its mean ECE over the ten graphs is 0.019, about 35 percent below the 0.029 of GCN+TS. We also introduce HG-DAPS, a training-free diffusion score whose homophily gate reads only the in-context labels, so the guarantee still holds. Relative to adaptive prediction sets (APS), it reduces mean set size by 5.8 to 17.1 percent on six homophilous graphs and changes it by under 1 percent on four heterophilous ones. On two binary, class-imbalanced graphs, a pre-registered trap case shows that gating on raw rather than adjusted homophily lowers coverage among low-homophily nodes by 0.27 and 0.12. Marginal coverage stays at the nominal 0.90 and masks this drop.

---


### 302. [LiDAR Resolution Recovery via Foundation-Model-Guided Diffusion](https://arxiv.org/abs/2610.08620)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Samed Doğan, Nico Leuze, Alfred Schöttl  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-beam-count LiDAR sensors are costly, yet many perception pipelines require dense angular sampling. Using a pretrained Stable Diffusion model as the backbone, we fine-tune a LiDAR-conditioned depth model with pseudo-depth targets from a 2D foundation model. During training, the LiDAR conditioning is randomly decimated at different beam budgets. We then investigate how much of a LiDAR scan can be recovered from heavily decimated input and characterize performance across the input beam budget. We evaluate against physically held-out real beams on nuScenes and report recovery separately from fit accuracy. Our model yields its largest advantage in very sparse regimes, achieving a $\delta_{1.25}$ accuracy of $66.8$% from $4$-beam input where scattered interpolation reaches only $45.1$%. A class-stratified error breakdown further reveals that planar surfaces recover first while objects introducing depth discontinuities degrade earliest. Together, these results quantify the recovery/resolution trade-off for foundation-model-guided LiDAR enhancement.

---


### 303. [GeneICL: A Tabular Foundation Model for Bulk Transcriptomics](https://arxiv.org/abs/2610.08694)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Michael Bohl, Alexander Theus, David Wissel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gene expression is widely measured in biomedicine, yet clinical outcome prediction remains challenging due to high dimensionality, strong feature correlations, and limited labeled data. Large self-supervised transcriptomic foundation models often fail to outperform simple supervised baselines. Tabular foundation models offer an alternative through in-context learning, but are typically pretrained on generic synthetic data rather than transcriptomic structure. We ask whether transcriptomics-aware pretraining, rather than scale, is the missing ingredient. Towards this end, we introduce GeneICL, a 4.2M-parameter tabular foundation model combining a semi-synthetic pretraining prior built from measured bulk expression profiles with a parameter-efficient recurrent architecture. We further enable right-censored survival prediction via a training-free reduction to regression using Cox partial-likelihood residuals. We evaluate GeneICL on 80 clinical outcome-prediction tasks spanning classification, regression, and survival. Tabular foundation models consistently outperform self-supervised transcriptomic models, while GeneICL achieves the best overall rank among evaluated foundation models and tuned baselines. GeneICL does so with up to 387$\times$ fewer parameters, no gradient updates at inference, and predictions within seconds on a laptop CPU.

---


> [!TIP]
> 当前位于：**301-303**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-303**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
