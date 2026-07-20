# 📦 其他研究 | 2026年07月21日

> 本类共 **152** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-152**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-152**

---

### 151. [FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation](https://arxiv.org/abs/2607.16190)

**<font color=#1a73e8>作者：</font>** Hao Liu, Chenghuan Huang, Ye Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Diffusion Transformers process long spatio-temporal sequences, making self-attention the main bottleneck in high-resolution video generation. Training-free sparse attention reduces this cost, but adaptive Top-$p$ routing creates uneven per-head workloads under multi-GPU sequence parallelism. The resulting workload heterogeneity turns sparse attention into a rank-level straggler problem. We present \method{}, a training-free sparse-attention system that improves the distributed execution efficiency of adaptive sparse attention under multi-GPU sequence parallelism. \method{} uses Top-$p$ routing, a Top-$k$ safety floor, and video-aware block organization as the sparse-routing frontend, then repairs the materialized mask at runtime. Runtime Load Balancing migrates a small number of heavy heads via P2P communication to shorten the current critical path. Slack-Aware Sparse Augmentation fills residual non-critical-rank slack with additional high-value blocks, while overlap hides scheduling and migration overhead behind existing computation. On step-distilled Wan2.2 I2V, \method{} reduces average load imbalance from 1.34 to 1.08 and delivers a $4.41\times$ attention speedup over FlashAttention, while achieving a $2.02$--$2.11\times$ DiT inference speedup with competitive video quality.

---


### 152. [MotionForesight: Re-purposing Video Models for Future 3D Scene-Flow Prediction](https://arxiv.org/abs/2607.16192)

**<font color=#1a73e8>作者：</font>** Homanga Bharadhwaj, Yash Jangir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans can infer how objects are likely to move from passive observation: a cup may be lifted, a drawer may slide, and a lid may rotate shut. Such predictions expose the physical consequences of interaction needed to act in the real world. We study how to learn this anticipation from ordinary monocular videos of human-object interaction. Given a short observed video context, MotionForesight predicts future 3D trajectories for points on the manipulated object. This casts interaction prediction as object-centered 3D motion forecasting without any assumptions on the object properties. Our key insight is that video prediction models already encode rich priors about how objects move during human interactions. We redirect these priors from pixel prediction toward future 3D scene flow. We start from a dense 3D tracker built on a pretrained video model, generate pseudo-ground-truth tracks from complete clips, and train the forecaster using only the observed frames. We replace future RGB and geometry with learned mask latents and train a lightweight adapter to turn the retrospective tracking representation into a forward predictor, while freezing the large video and tracking components. Using just 40k human videos and no auxiliary inputs such as language, MotionForesight generalizes across diverse out-of-distribution objects, environments, viewpoints, and interactions. It also outperforms substantially larger models that use over a million training videos. These results show that we can efficiently re-purpose video priors into explicit geometric forecasts for embodied intelligence. this https URL

---


> [!TIP]
> 当前位于：**151-152**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-152**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
