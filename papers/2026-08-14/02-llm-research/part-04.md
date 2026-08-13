# 🧠 大模型相关研究 | 2026年08月14日

> 本类共 **164** 篇论文：已确认 **147** 篇，待复核 **17** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-164**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-164**

---

### 151. [Repurposing RGB-based Foundation Model for Depth Estimation on Thermal Images Using Hierarchical Supervision](https://arxiv.org/abs/2608.11564)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jie Hong, Tingtian Li, Xuesong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth estimation from thermal images is highly valuable for robotic applications in adverse conditions, such as nighttime and rainy weather. Recent studies have sought to transfer knowledge from RGB-based foundation models to thermal modalities, yet the rich hierarchical representations these models encode remain underutilized. To address this limitation, we propose RGB-HS, a novel framework for thermal-image depth estimation that leverages hierarchical supervision from an RGB-based foundation model. Specifically, we first replace the baseline thermal encoder with a foundational model and introduce a parallel RGB branch that also employs a foundational model as an encoder of the same architecture, taking RGB images as input. The alignment is then performed across multiple levels between the tokens of the two encoders, allowing the thermal student branch to capture both structural precision and semantic abstraction from the RGB teacher branch. Furthermore, we introduce verification to refine the alignment process by weighting tokens from the RGB branch based on RGB image quality. Extensive experiments on the popular benchmark demonstrate that RGB-HS achieves competitive performance and more effectively exploits the representational capacity of RGB-based foundation models for depth estimation on thermal images.

---


### 152. [Zero-OVCD: Bridging Training-Free Foundation Models and Pseudo-Label Learning for Open-Vocabulary Change Detection](https://arxiv.org/abs/2608.11663)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Daifeng Peng, Yuanke Peng, Haiyan Guan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary change detection (OVCD) enables the identification of user-specified land-cover changes in bitemporal remote sensing images, but existing training-free pipelines remain vulnerable to inaccurate candidate masks, ambiguous semantic assignments, and accumulated inference errors. To address these issues, we propose Zero-OVCD, a two-stage framework that requires no pixel-level annotations from the target domain. In the first stage, high-quality change pseudo-labels are generated through complementary candidate-mask refinement, multiscale semantic similarity fusion with margin-based reliability filtering, and response-guided mask correction and completion. These components jointly suppress noisy candidates, enhance mask-level semantic discrimination, and recover missed change regions. In the second stage, a change detector is trained using the generated pseudo-labels, while checkpoint voting and high-agreement sample selection are introduced to mitigate residual pseudo-label noise. On LEVIR-CD, WHU-CD, and S2Looking, Stage I achieves F1 scores of 86.25%, 85.82%, and 50.48%, while Stage II further improves them to 88.65%, 88.85%, and 57.96%, respectively. On SECOND, the macro-average F1 across six category-wise one-vs-rest tasks increases from 47.91% to 50.92%. These results demonstrate that bridging training-free foundation-model inference with noise-aware pseudo-label learning provides an effective solution for open-vocabulary change detection without target-domain pixel-level annotations. Code will be available at this https URL.

---


### 153. [LEMUR: Latent Entropy-aware Multimodal Unlearning via Visual-anchored Reasoning Redirection](https://arxiv.org/abs/2608.11691)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xinhao Zhong, Yuxia Qiao, Junhao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement-learning (RL) post-training equips multimodal large reasoning models (MLRMs) with exploratory chains of thought (CoT), substantially improving visual reasoning. However, we find that this capability introduces a distinct privacy vulnerability: even when a sensitive fact is successfully unlearned from the final answer, the model may still reproduce it in its reasoning trace. This leakage is substantially more pronounced in natively RL-trained MLRMs than in their non -reasoning base models, revealing a privacy risk that existing unlearning methods are not designed to address. We show that RL-induced exploration leaves sensitive content with a distinctive token-level entropy signature that is largely absent from base models. Based on this observation, we propose LEMUR, a fully training-free, inference-time unlearning framework for natively RL-trained multimodal models. LEMUR uses entropy dynamics as a control signal to identify when sensitive reasoning begins and when sanitization should stop. During this interval, it redirects the reasoning trajectory through entropy-modulated visual-anchor latent injection, replacing committed tokens with sanitized, probability-weighted embeddings re-grounded in the input image. Across diverse MLRMs, LEMUR consistently outperforms existing unlearning met hods in suppressing both reasoning-trace and answer leakage, while better preserving non-sensitive utility and output fluency. These results demonstrate that RL-induced entropy dynamics provide a distinctive signal for privacy leakage and that exploiting this signal enables effective training-free unlearning for reasoning-capable multimodal models.

---


### 154. [STAR: A Spatial-Topology Aware Routing Framework for Generalizable 3D Scene Understanding](https://arxiv.org/abs/2608.11699)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mingwei Xing, Xinliang Wang, Yifeng Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Constructing a unified 3D scene understanding model has long been hindered by the topological discrepancies across sensor modalities. While applying the Mixture-of-Experts (MoE) architecture is a flexible approach for multi-domain 3D understanding, we observe that conventional feature-only MoE routers may underrepresent local sampling topology under semantic supervision, making expert allocation difficult when semantic consistency coexists with geometric heterogeneity. To overcome this challenge, we propose STAR (Spatial-Topology Aware Routing Framework). Specifically, we introduce a multi-attribute self-supervised pre-training branch, covering topological and textural variations, to anchor cross-domain structural priors. Building upon this, we design a domain-aware expert branch with two mechanisms: Domain-Spatial-Guided Routing (DSR), which captures local topological variations from spatial context, and Entropy-controlled Dynamic Allocation (EDA), which adjusts the number of activated experts according to routing uncertainty. Together, these branches combine stable cross-domain representation learning with adaptive expert allocation. Extensive experiments across various tasks, encompassing both indoor and outdoor scenes, demonstrate the effectiveness of STAR. It achieves 80.1% mIoU on the ScanNet validation set and 77.2% mIoU on S3DIS, consistently improving over strong baselines. Code is available at our project page (this https URL).

---


### 155. [Consolidator: Learning Persistent Routed Memory Across Context Boundaries](https://arxiv.org/abs/2608.11701)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Copying short-term memory (STM) into a slower store can preserve state across a context boundary, but persistence alone does not ensure that the retained state influences subsequent memory access. We test this distinction in a Phasor Memory Network (PMNet) using Consolidator, a shared slot-local operator that transforms routed STM before accumulating it into long-term memory (LTM), without replaying the source tokens. After each consolidation, the KV cache and STM are cleared. The retained LTM can still be read and is also fed into the hierarchical router, thereby conditioning which explicit-memory slots subsequent inputs access. We evaluate this mechanism on a two-segment modulo-10 mapping task in which the second segment updates the mapping at the same memory address. Following a second consolidation and reset, a held-out query must recover the updated mapping from LTM. The backbone and memory interface are frozen, leaving only 12.35K Consolidator parameters trainable (0.041\% of a 29.95M model). Across five paired runs from the same STM-pretraining checkpoint, direct LTM routing raises updated-mapping recall from $44.38\pm1.94\%$ to $87.02\pm1.76\%$ ($+42.64\pm1.10$ percentage points), while immediate STM recall remains 89.90\% in both conditions; both train separate Consolidators and retain the same LTM read paths. Learned consolidation outperforms forced identity accumulation by $21.40\pm1.91$ percentage points without routing and $68.70\pm1.76$ with routing. Thus, on this task, consolidated LTM serves as both retrievable content and an access state that shapes subsequent slot selection.

---


### 156. [LiveAnimate: Stable Long-Form Streaming Human Animation in Real-Time](https://arxiv.org/abs/2608.11745)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuxuan Zhang, Haozhong Xiong, Yubo Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose-driven human animation synthesizes a video of a target person from a single reference image and a driving pose stream. Real-time generation is essential for interactive applications such as live streaming, telepresence, and virtual avatars, yet diffusion-based systems require minutes to hours per clip, precluding responsive interaction. We present LiveAnimate, to our knowledge the first animation system to combine real-time streaming with stable long-form generation at billion scale, built on a 14B-parameter video Diffusion Transformer (DiT). A two-stage training pipeline first adapts a pretrained bidirectional DiT into a block-causal autoregressive generator through Reference-Anchored Teacher-Forcing Adaptation, and then reduces the sampling budget to three steps through Block-wise Self-Forcing Distillation. To preserve appearance over extended streams, we introduce Pose-Retrieval Sink Attention (PR-Sink), a bounded KV-cache mechanism combining a Static Sink that permanently anchors the first generated block, a Dynamic Sink that holds a pose-retrieved historical block, and a three-slot Rolling Window. When a pose recurs, PR-Sink restores the relevant appearance context without retaining the entire sequence, so memory and per-block latency remain constant regardless of stream duration. Together with Ulysses sequence parallelism and operator fusion, these designs enable 19.63\,FPS streaming inference on two NVIDIA H100 GPUs. On a three-minute benchmark, LiveAnimate maintains nearly constant perceptual quality and identity from the first 30 seconds to the final minute (IQA 4.047 vs.\ 4.026), while prior systems degrade substantially or require hours of offline computation for the same rollout. These results establish a new operating point in quality, latency, and duration for interactive full-body animation.

---


### 157. [HarmoniDPO: Video-guided Audio Generation via Preference-Optimized Diffusion](https://arxiv.org/abs/2608.11913)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wenshuo Peng, Kaipeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-to-audio (V2A) generation faces significant challenges in achieving precise temporal synchronization and high perceptual quality due to the complex, ambiguous relationship between visual and auditory cues. Existing methods typically compress video inputs into single feature representations, leading to significant loss of temporal dynamics and fine-grained visual information. These approaches also rely on reconstruction-based training objectives that poorly correlate with human perceptual judgments of audio quality and appropriateness. We propose HarmoniDPO, a novel framework that integrates preference-based optimization into diffusion-based V2A generation to address these limitations. (1) Our approach leverages a dual video representation: combining global context with frame-wise features to preserve temporal dynamics and semantic detail. (2) Inspired by reinforcement learning from human feedback (RLHF), HarmoniDPO employs online Direct Preference Optimization (online-DPO) to fine-tune a diffusion-based V2A model from preference judgments, enhancing perceptual quality and alignment. (3) Additionally, we introduce Dual-scale Diffusion Search (DDS), a test time scaling algorithm that adaptively optimizes output fidelity during inference. Experiments demonstrate that HarmoniDPO outperforms state-of-the-art methods in audio-video synchronization and subjective audio quality, offering a robust solution for generating realistic, human-preferred audio from video.

---


### 158. [Distillation of Foundation Models for Time-dependent PDEs](https://arxiv.org/abs/2608.11937)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Daniel Musekamp, Boshra Ariguib, Andrei Manolache 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models for time-dependent partial differential equations (PDEs) are trained on large and diverse collections of physical systems and can generalize effectively to new downstream tasks. After fine-tuning on only a few trajectories from a target domain, they can achieve strong accuracy in low-data regimes. However, these models are typically large and computationally intensive, limiting their usefulness as fast surrogates for numerical solvers. We propose Teacher Rollout Extension (TREX), a knowledge distillation framework that transfers the predictive capability of a pretrained foundation model into a compact and efficient student. Starting from a fine-tuned teacher, TREX augments limited downstream data by generating long synthetic trajectories through teacher rollouts, optionally with periodic noise injection. This procedure samples from the teacher-induced rollout distribution without requiring explicit knowledge of the initial-condition distribution, while exposing the student to long-horizon states and local recovery behavior around states encountered during autoregressive prediction. The student can further incorporate task-specific inductive biases, such as equivariance, that the teacher does not necessarily enforce. We evaluate TREX on multiple PDE benchmarks. The resulting students can match or surpass the teacher's accuracy while reducing the number of parameters by several orders of magnitude and achieving more than an order-of-magnitude speedup in inference.

---


### 159. [Understanding Why Foundation Models Work for Diffusion-Generated Image Detection](https://arxiv.org/abs/2608.12155)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Davide Cozzolino, Giovanni Poggi, Luisa Verdoliva  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models have recently emerged as powerful feature extractors for detecting AI-generated images, achieving strong generalization across generators and robustness to common image degradations. However, the reason behind their effectiveness is poorly understood. In this work, we investigate what cues are exploited by foundation-model-based detectors to distinguish real images from diffusion-generated ones. To this end, we design an ad hoc analysis protocol based on DDIM inversion. Given a real image we generate a sequence of synthetic copies by changing the depth of DDIM inversion. Even though most copies are semantically identical to the real reference, the detector score varies significantly across them due to subtle traces introduced by the diffusion synthesis, showing that its decision is not primarily driven by semantic failures. Through a frequency-swapping analysis, we further reveal that the discriminative cues exploited by the detectors are mainly localized in the low-to-mid frequency range, rather than only in the high-frequency range, as is the case for artifacts commonly associated with generative models. Finally, a latent-space analysis shows that regenerated images exhibit reduced variance and effective dimensionality, indicating that diffusion models do not fully reproduce the variability of real data. Overall, our results suggest that foundation-model-based detectors succeed by capturing non-semantic low-to-mid frequency distributional discrepancies between real and diffusion-generated images. These findings provide new insight into the robustness and generalization of such detectors and suggest directions for more interpretable forensic methods.

---


### 160. [Rethinking Agent Security as a Networking Problem](https://arxiv.org/abs/2608.12172)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Van Tran, Taveesh Sharma, Tajveer Singh Dhesi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> AI agents are rapidly becoming more capable and widely deployed, promising substantial gains in productivity and enabling new classes of applications. However, their growing autonomy also introduces significant privacy and security risks. Existing defenses are predominantly agent-centric, relying on the agent itself to detect threats and enforce privacy and security policies. This approach is fundamentally limited because it entrusts policy enforcement to AI agents whose LLM-driven behavior is inherently nondeterministic and vulnerable to manipulation through attacks such as prompt injection. As a result, current defenses cannot reliably prevent privacy and security threats, highlighting a critical need for a new solution to securing AI agent systems.
The networking community has long grappled with similar challenges and offers insightful principles we can borrow to design a more secure AI agent system. These include centralized control with distributed enforcement, capability-based access for mediating requests to sensitive resources, and least privilege through zero-trust enforcement. Historically, these principles have provided strong deterministic guarantees for networked systems. However, these principles alone are insufficient for AI agents because the safety and appropriateness of an agent's actions often depend on semantic context beyond the expressiveness of static rules.
Building on these principles, we advocate for a systematic approach to AI agent security that combines deterministic enforcement mechanisms, which provide strong security guarantees, with semantic, context-aware policies that enable nuanced decision-making. We then present a reference architecture and identify key research questions and future directions to guide the design of secure and privacy-preserving AI agent systems.

---


### 161. [ScreenShot: A Foundation Model for Few-Shot Combination Drug Screening](https://arxiv.org/abs/2608.12219)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Antoine de Mathelin, Christopher Tosh, Wesley Tansey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Treating patients with combinations of drugs reduces the risk of resistance to any individual drug. Finding effective combinations is difficult because the large search space makes combinatorial screens prohibitively expensive, time consuming, and often technically infeasible. Predictive models can fill this gap, yet existing methods typically require molecular profiling of each sample and per-cohort training, limiting their applicability when time and tissue are scarce. To address this challenge, we introduce ScreenShot, a hierarchical transformer pretrained on 40 drug screening datasets covering 3,700 drugs and 6,000 biological samples, whose architecture mirrors the nested structure of screening data. Given a few-shot context of observations from a new patient, ScreenShot predicts the response of the sample to combination therapies through in-context learning, operating directly on functional measurements with no fine-tuning and no molecular profiling. On four held-out datasets, ScreenShot outperforms all baselines in both prediction accuracy and identification of selectively effective treatments. ScreenShot's internal representations are directly useful for experimental design: we use them to drive a weighted k-means++ active learning strategy that selects which experiments to run, achieving the same hit detection as uniform screening with a third of the budget. Source code and interactive dashboard: this https URL.

---


### 162. [VICBench: A Multi-Language Benchmark for Code Vulnerability Detection](https://arxiv.org/abs/2608.12246)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jin Lu, Xuening Han, Yang Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Evaluating security vulnerability detection tools requires benchmark datasets with vulnerability-inducing commits (VICs) - the commits that first introduce vulnerabilities into codebases. VICs are essential for determining the full range of vulnerable software versions. Existing vulnerability datasets suffer from limited programming language coverage, restricted patch complexity, and narrow project scope. Through our dual annotation by human experts and an agentic workflow, we create a benchmark - VICBench - of 100 verified VICs for 100 CVEs across 88 projects in Python, Java, and C++, covering 48 CWE types. VICBench features complex real-world vulnerability fixes averaging 38.6 lines and corresponding VICs of 252.5 lines - significantly larger than prior work. Our evaluation shows that state-of-the-art algorithms V-SZZ and LLM4SZZ achieve only 33.3%-40.1% F1, confirming that using existing approaches still entails significant manual effort. VICBench enables robust evaluation of vulnerability detection approaches.

---


### 163. [Class Activation Mapping in Explainable Computer Vision: A Method-Centered Review of CNN, Transformer, and Foundation-Model-Era Visual Explanations](https://arxiv.org/abs/2608.12299)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** AmirHossein Eshghi, Hamid Saadatfar, Seyyed Ali Hoseini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class activation mapping (CAM) is one of the most widely used visual explanation families in explainable artificial intelligence. Its purpose is intuitive: it converts internal model evidence into a heatmap that highlights the image regions, convolutional channels, tokens, or patches that support a target class or concept. Since the first CAM formulation in 2016, the field has moved far beyond global-average-pooled CNN classifiers. CAM-style methods now include gradient-based post-hoc explanations, gradient-free score and ablation methods, high-resolution upscaling, weakly supervised localization and segmentation, transformer token attribution, causal and debiasing methods, and foundation-model-era approaches that use CLIP, DINO, SAM, or feature-distribution comparisons. This review synthesizes a strict corpus of 57 method-centered papers published from 2016 onward. The paper develops a taxonomy that separates methods by attribution mechanism, architectural dependence, and evaluation objective. It then reviews gradient-based CAMs, recent and hybrid CAM-style methods, and model-based or architecture-aware methods. Across the corpus, the main trend is clear: the field is shifting from explaining one class score in one low-resolution CNN layer toward comparative, multi-layer, probabilistic, token-aware, and foundation-model-aware explanations. At the same time, evaluation remains fragmented. Faithfulness, localization, robustness, computational cost, and human trust are often measured with different protocols. The review therefore emphasizes not only what each method contributes, but also which gap it leaves open and which later methods attempt to close that gap.

---


### 164. [AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses](https://arxiv.org/abs/2608.12307)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Cheng Qian, Wenting Zhao, Liangwei Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work on distillation transfers the capabilities of large models to smaller ones often by updating the latter's parameters, through teacher forcing, on-policy distillation, and related training-time methods. In this paper, we ask whether such transfer can instead occur at test time. We study strong-to-weak scaffolding: whether a stronger builder model can construct inference-time harnesses that help a weaker target model solve tasks more reliably without any parameter updates. Using four representative Theory-of-Mind benchmarks, each builder model uses 5% of the data as a validation set to iteratively refine its harness over multiple rounds, after which the finalized harness is evaluated on the full test set. Empirically, this form of test-time capability transfer is highly effective, nearly doubling average target-model performance from 0.49 to 0.91. Our analysis shows that the gains come primarily from offloading unstable model reasoning into deterministic code, benchmark-specific routing, and strict answer-format enforcement, rather than from encouraging the target model to reason more extensively or sample more broadly. We further find that builder-model reasoning effort improves harness quality monotonically, platform effects are modest relative to the builder model's own capability, and weaker target models receive the largest gains. These results suggest that inference-time harness design is an important complement to conventional training-time distillation, enabling strong models to transfer cognitive structure to weaker models without retraining.

---


> [!TIP]
> 当前位于：**151-164**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-164**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
