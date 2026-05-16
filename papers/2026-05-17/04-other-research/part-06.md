# 📦 其他研究 | 2026年05月17日

> 本类共 **337** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-337](./part-07.md)

---

### 251. [Holistic Evaluation and Failure Diagnosis of AI Agents](https://arxiv.org/abs/2605.14865)

**<font color=#1a73e8>作者：</font>** Netta Madvil, Gilad Dym, Alon Mecilati 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents execute complex multi-step processes, but current evaluation falls short: outcome metrics report success or failure without explaining why, and process-level approaches struggle to connect failure types to their precise locations within long, structured traces. We present a holistic agent evaluation framework that pairs top-down agent-level diagnosis with bottom-up span-level evaluation, decomposing analysis into independent per-span assessments. This decomposition scales to traces of arbitrary length and produces span-level rationales for each verdict. On the TRAIL benchmark, our framework achieves state-of-the-art results across all metrics on both GAIA and SWE-Bench, with relative gains over the strongest prior baselines of up to 38% on category F1, up to 3.5x on localization accuracy, and up to 12.5x on joint localization-categorization accuracy. Per-category analysis shows our framework leading in more error categories than any other evaluator. Notably, the same frontier model achieves several times higher localization accuracy when used inside our framework than as a monolithic judge over the full trace, showing that evaluation methodology, not model capability, is the bottleneck.

---


### 252. [REALM: Retrospective Encoder Alignment for LFP Modeling](https://arxiv.org/abs/2605.14867)

**<font color=#1a73e8>作者：</font>** Peicheng Wu, Zhenyu Bu, Runze Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spike activity has been the dominant neural signal for behavior decoding due to its high spatial and temporal resolution. However, as brain-computer interfaces (BCIs) move toward high channel counts and wireless operation, the high sampling frequency of spike signals becomes a bottleneck due to high power and bandwidth requirements. Local field potentials (LFPs) represent a different spatial-temporal scale of brain activity compared to spikes, offering key advantages including improved long-term stability, reduced energy consumption, and lower bandwidth requirement. Despite these benefits, LFP-based decoding models typically show reduced accuracy and often rely on non-causal architectures that are unsuitable for real-time deployment. To address these challenges, we propose REALM: a retrospective distillation framework that enables causal LFP decoding. Inspired by offline-to-online distillation strategies in speech recognition, REALM transfers representational knowledge from a pretrained multi-session bidirectional LFP model to a causal version for real-time deployment. We first pretrain a bidirectional Mamba-2 teacher model using a masked autoencoding objective. We then distill this teacher model into a compact student model via a combined objective of representation alignment and task supervision. REALM consistently outperforms both causal and non-causal LFP-based SOTA methods for behavior decoding. Notably, our REALM improves decoding performance while achieving a $2\times$ reduction in parameter count and a $10\times$ reduction in training time. These results demonstrate that retrospective distillation effectively bridges the gap between offline and real-time neural decoding. REALM shows that LFP-only models can achieve competitive decoding performance without reliance on spike signals, offering a practical and scalable alternative for next-generation wireless implantable BCIs.

---


### 253. [Fast Adversarial Attacks with Gradient Prediction](https://arxiv.org/abs/2605.14868)

**<font color=#1a73e8>作者：</font>** Kamil Ciosek, Aleksandr V. Petrov, Nicolò Felicioni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating adversarial examples at scale is a core primitive for robustness evaluation, adversarial training, and red-teaming, yet even "fast" attacks such as FGSM remain throughput-limited by the cost of a backward pass. We introduce a family of attacks that eliminates the backward pass by predicting the input gradient from forward-pass hidden states via a lightweight linear regression. The approach is motivated by a kernel view of neural networks and is exact in the Neural Tangent Kernel regime, while remaining effective for practical finite-width models. Empirically, our methods recover much of FGSM's attack performance while using only a small fraction of the time, corresponding to a $532\%$ increase in throughput. These results suggest gradient prediction as a simple and general route to significantly faster adversarial generation under realistic wall-clock constraints.

---


### 254. [LPH-VTON: Resolving the Structure-Texture Dilemma of Virtual Try-On via Latent Process Handover](https://arxiv.org/abs/2605.14874)

**<font color=#1a73e8>作者：</font>** Yixin Liu, Baihong Qian, Jinglin Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual Try-On (VTON) aims to synthesize photorealistic images of garments precisely aligned with a person's body and pose. Current diffusion-based methods, however, face a fundamental trade-off between structural integrity and textural fidelity. In this paper, we formalize this challenge as a consequence of complementary inductive biases inherent in prevailing architectures: models heavily reliant on spatial constraints naturally favor geometric alignment but often suppress textures, whereas models dominated by unconstrained generative priors excel at vibrant detail rendering but are prone to structural drift. Based on this diagnosis, we propose LPH-VTON, a new synergistic framework that resolves this tension within a single, continuous denoising process. LPH-VTON strategically decomposes the generation, leveraging a structure-biased model to establish a geometrically consistent latent scaffold in the early stages, before handing over control to a texture-biased model for high-fidelity detail rendering. Extensive experiments validate our approach. Our model achieves a superior Pareto-optimal balance, establishing new benchmarks in perceptual faithfulness while maintaining highly competitive structural alignment across the standard dataset VITON-HD, proving the efficacy of temporal architectural decoupling.

---


### 255. [Unlocking Complex Visual Generation via Closed-Loop Verified Reasoning](https://arxiv.org/abs/2605.14876)

**<font color=#1a73e8>作者：</font>** Hanbo Cheng, Limin Lin, Ruo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid advancements, current text-to-image (T2I) models predominantly rely on a single-step generation paradigm, which struggles with complex semantics and faces diminishing returns from parameter scaling.
While recent multi-step reasoning approaches show promise, they are hindered by ungrounded planning hallucinations lacking verification, monolithic post-hoc reflection, long-context optimization instabilities, and prohibitive inference latency. To overcome these bottlenecks, we propose the Closed-Loop Visual Reasoning (CLVR) framework, a comprehensive system that deeply couples visual-language logical planning with pixel-level diffusion generation. CLVR introduces an automated data engine with step-level visual verification to synthesize reliable reasoning trajectories, and proposes Proxy Prompt Reinforcement Learning (PPRL) to resolve long-context optimization instabilities by distilling interleaved multimodal histories into explicit reward signals for accurate causal attribution. Furthermore, to mitigate the severe latency bottleneck caused by iterative denoising, we propose $\Delta$-Space Weight Merge (DSWM), a theoretically grounded method that fuses alignment weights with off-the-shelf distillation priors, reducing the per-step inference cost to just 4 NFEs without requiring expensive re-distillation. Extensive experiments demonstrate that CLVR outperforms existing open-source baselines across multiple benchmarks and approaches the performance of proprietary commercial models, unlocking general test-time scaling capabilities for complex visual generation.

---


### 256. [HeatKV: Head-tuned KV-cache Compression for Visual Autoregressive Modeling](https://arxiv.org/abs/2605.14877)

**<font color=#1a73e8>作者：</font>** Jonathan Cederlund, Axel Berg, Durmus Alp Emre Acar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Autoregressive (VAR) models have recently demonstrated impressive image generation quality while maintaining low latency. However, they suffer from severe KV-cache memory constraints, often requiring gigabytes of memory per generated image. We introduce HeatKV, a novel compression method that adapts cache allocation in each head based on its attention to previously generated scales. Using a small offline calibration set, the attention heads are ranked according to their attention scores over prior scales. Based on this ranking, we construct a static pruning schedule tailored to a given memory budget. Applied to the Infinity-2B model, HeatKV achieves $2 \times$ higher compression ratio in memory allocation for KV cache compared to existing methods, while maintaining similar or better image fidelity, prompt alignment and human perception score. Our method achieves a new state-of-the-art (SOTA) for VAR model KV-cache compression, showcasing the effectiveness of fine-grained, head-specific cache allocation.

---


### 257. [Decision-Level Fusion for Robust Wearable Affect Recognition](https://arxiv.org/abs/2605.14878)

**<font color=#1a73e8>作者：</font>** Lokesh Singh, Athina Georgara, Jayati Deshmukh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Automatic recognition of affective state from wearable physiology has clear societal impact for public health, preventive care, and stress-aware interventions, but real deployments require robustness to non-stationary dynamics, artefacts, and missing sensors. We study this problem on WESAD, using baseline, stress, and amusement conditions, where common fixed-basis spectral features such as FFT bandpower and Welch PSD can oversmooth short-lived discriminative patterns. We propose a non-stationary pipeline that combines Fourier-Bessel Series Expansion (FBSE) with EWT data-driven spectral segmentation to extract mode-wise transient descriptors. For multimodal integration, we adopt decision-level aggregation over per-modality predictors and weight each modality by predictive uncertainty and modality reliability. Results on WESAD, using 15 subjects and ECG, EDA, BVP, EMG, and ACC signals across three classes, indicate that decision-level aggregation is approximately 84 percent of the time at least as good as feature-level aggregation, and approximately 48 percent of the time strictly better, suggesting improved robustness under heterogeneous and partially reliable sensing.

---


### 258. [Temporal Fair Division in Multi-Agent Systems: From Precise Alternation Metrics to Scalable Coordination Proxies](https://arxiv.org/abs/2605.14879)

**<font color=#1a73e8>作者：</font>** Nikolaos Al. Papadopoulos  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A plethora real-world environments require agents to compete repeatedly for the same limited resource, calling for a temporal notion of fairness judged across entire interaction histories. This paper advances the theory of temporal fair division by introducing Rotational Periodicity (RP), a family of lightweight metrics, alongside the ALT family of sliding-window measures, within a unified framework for repeated multi-agent resource competition.
We formalise the Multi-Agent Battle of the Exes (MBoE) as a repeated fair division instance and establish Perfect Alternation (PA) as its canonical temporally fair solution, drawing connections to proportionality, envy-freeness, and n-periodic round-robin allocation. RP decomposes temporal fairness into two complementary sub-measures: Rotational Score (RS) and Waiting Periods Evaluation (WPE), achieving O(nu+n) time complexity versus the O(nu*n) of ALT, where nu is the episode count and n the agent count.
Empirical evaluation across n in {2,3,5,8,10} reveals three findings. First, both RP and ALT expose a coordination failure invisible to traditional metrics: Q-learning agents perform worse than random policies by 10-73% on RP and 7-35% on CALT, while Reward Fairness remains misleadingly high (above 0.92 for n>=3). Second, RP achieves 12-25x computational speedup over ALT, growing with n. Third, the two families are complementary: ALT provides richer discrimination for small populations; RP scales reliably where ALT becomes intractable. Together they form a diagnostic toolkit for temporal fair division.

---


### 259. [Denoising-GS: Gaussian Splatting with Spatial-aware Denoising](https://arxiv.org/abs/2605.14880)

**<font color=#1a73e8>作者：</font>** Qingyuan Zhou, Xinyi Liu, Weidong Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D Gaussian Splatting (3DGS) have achieved remarkable success in high-fidelity Novel View Synthesis (NVS), yet the optimization process inevitably introduces noisy Gaussian primitives due to the sparse and incomplete initialization from Structure-from-Motion (SfM) point clouds. Most existing methods focus solely on adjusting the positions of primitives during optimization, while neglecting the underlying spatial structure. To this end, we introduce a new perspective by formulating the optimization of 3DGS as a primitive denoising process and propose Denoising-GS, a spatial-aware denoising framework for Gaussian primitives by taking both the positions and spatial structure into consideration. Specifically, we design an optimizer that preserves the spatial optimization flow of primitives, facilitating coherent and directed denoising rather than random perturbations. Building upon this, the Spatial Gradient-based Denoising strategy jointly considers the spatial supports of primitives to ensure gradient-consistent updates. Furthermore, the Uncertainty-based Denoising module estimates primitive-wise uncertainty to prune redundant or noisy primitives, while the Spatial Coherence Refinement strategy selectively splits primitives in sparse regions to maintain structural completeness. Experiments conducted on three benchmark datasets demonstrate that Denoising-GS consistently enhances NVS fidelity while maintaining representation compactness, achieving state-of-the-art performance across all benchmarks. Source code and models will be made publicly available.

---


### 260. [AIMing for Standardised Explainability Evaluation in GNNs: A Framework and Case Study on Graph Kernel Networks](https://arxiv.org/abs/2605.14884)

**<font color=#1a73e8>作者：</font>** Magdalena Proszewska, N. Siddharth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have advanced significantly in handling graph-structured data, but a comprehensive framework for evaluating explainability remains lacking. Existing evaluation frameworks primarily involve post-hoc explanations, and operate in the setting where multiple methods generate a suite of explanations for a single model. This makes comparison of explanations across models difficult. Evaluation of inherently interpretable models often targets a specific aspect of interpretability relevant to the model, but remains underdeveloped in terms of generating insight across a suite of measures. We introduce AIM, a comprehensive framework that addresses these limitations by measuring Accuracy, Instance-level explanations, and Model-level explanations. AIM is formulated with minimal constraints to enhance flexibility and facilitate broad applicability. Here, we use AIM in a pipeline, extracting explanations from inherently interpretable GNNs such as graph kernel networks (GKNs) and prototype networks (PNs), evaluating these explanations with AIM, identifying their limitations and obtaining insights to their characteristics. Taking GKNs as a case study, we show how the insights obtained from AIM can be used to develop an updated model, xGKN, that maintains high accuracy while demonstrating improved explainability. Our approach aims to advance the field of Explainable AI (XAI) for GNNs, providing more robust and practical solutions for understanding and improving complex models.

---


### 261. [Masked Next-Scale Prediction for Self-supervised Scene Text Recognition](https://arxiv.org/abs/2605.14885)

**<font color=#1a73e8>作者：</font>** Zhuohao Chen, Zeng Li, Yifei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene Text Recognition requires modeling visual structures that evolve from coarse layouts to fine-grained character strokes. Training such models relies on large amounts of annotated data. Recent self-supervised approaches, such as Masked Image Modeling (MIM), alleviate this dependency by leveraging large-scale unlabeled data. Yet most existing MIM methods operate at a single spatial scale and fail to capture the hierarchical nature of scene text. In this work, we introduce Masked Next-Scale Prediction (MNSP), a unified self-supervised framework designed to explicitly model cross-scale structural evolution. The framework incorporates Next-Scale Prediction (NSP), which learns hierarchical representations by predicting higher-resolution features from lower-resolution contexts. Naive scale prediction, however, tends to produce spatially diffuse attention, directing the model toward background regions rather than textual structures. MNSP resolves this limitation by jointly learning cross-scale prediction and masked image reconstruction. NSP captures global layout priors across resolutions, while masked reconstruction imposes strong local constraints that guide attention toward informative text regions. A Multi-scale Linguistic Alignment module further maintains semantic consistency across different resolutions. Extensive experiments demonstrate that MNSP achieves state-of-the-art performance, reaching 86.2\% average accuracy on the challenging Union14M benchmark and 96.7\% across six standard datasets. Additional analyses show that our method improves robustness under extreme scale and layout variations. Code is available at this https URL

---


### 262. [BiFedKD: Bidirectional Federated Knowledge Distillation Framework for Non-IID and Long-Tailed ECG Monitoring](https://arxiv.org/abs/2605.14886)

**<font color=#1a73e8>作者：</font>** Zixuan Shu, Tiancheng Cao, Hen-Wei Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) monitoring in Internet of Medical Things (IoMT) networks is constrained by strict data-sharing regulations and privacy concerns. Federated learning (FL) enables collaborative learning by keeping raw ECG data on devices, but frequent transmissions of high-dimensional model updates incur heavy per-round traffic over bandwidth-limited links. To alleviate this bottleneck, federated distillation (FD) replaces parameter exchange with logit-based knowledge transfer. However, the performance of FD often degrades under the non-independent and identically distributed (non-IID) and long-tailed label distributions in ECG deployments. To address these challenges, we propose a bidirectional federated knowledge distillation (BiFedKD) framework that employs an aggregation-by-distillation pipeline with temperature scaling to produce a stable global distillation signal for cross-client alignment. Experiments on the MIT-BIH Arrhythmia dataset show that BiFedKD improves accuracy and Macro-F1 over the baseline by $3.52\%$ and $9.93\%$, respectively. Moreover, to reach the same Macro-F1, BiFedKD reduces communication overhead by $40\%$ and computation cost by $71.7\%$ compared with the baseline.

---


### 263. [SurgicalMamba: Dual-Path SSD with State Regramming for Online Surgical Phase Recognition](https://arxiv.org/abs/2605.14889)

**<font color=#1a73e8>作者：</font>** Sukju Oh, Sukkyu Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online surgical phase recognition (SPR) underpins context-aware operating-room systems and requires committing to a prediction at every frame from past context alone. Surgical video poses three demands that natural-video recognizers do not jointly address: procedures span tens of thousands of frames, time flows non-uniformly as long routine stretches are punctuated by brief phase-defining transitions, and the visual domain is narrow so backbone features are strongly correlated across channels. Existing recognizers either let per-frame cost grow with elapsed length, or hold cost bounded but advance state at a uniform rate with channel-independent dynamics, leaving the latter two demands unaddressed. We present SurgicalMamba, a causal SPR model built on Mamba2's structured state-space duality (SSD) that holds per-frame cost at O(d). It introduces three SSD-compatible components, each targeting one demand: a dual-path SSD block that separates long- and short-term regimes at the level of recurrent state; intensity-modulated stepping, a continuous-time time-warp that adapts the slow path's effective rate to phase-relevant information; and state regramming, a per-chunk Cayley rotation that opens cross-channel mixing in the otherwise axis-aligned SSM recurrence. The learned rotation planes inherit a phase-aligned structure without any direct supervision, offering an interpretable internal signature of surgical workflow. Across seven public SPR benchmarks, SurgicalMamba reaches state-of-the-art accuracy and phase-level Jaccard under strict online evaluation: 94.6%/82.7% on Cholec80 (+0.7 pp/+2.2 pp over the strongest prior) and 89.5%/68.9% on AutoLaparo (+1.7 pp/+2.0 pp), at 119 fps on a single GPU. Ablations isolate the contribution of each component. The code is publicly available at this https URL.

---


### 264. [Hierarchical Image Tokenization for Multi-Scale Image Super Resolution](https://arxiv.org/abs/2605.14891)

**<font color=#1a73e8>作者：</font>** Isma Hadji, Enrique Sanchez, Adrian Bulat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a multi-scale Image Super Resolution (ISR) method building on recent advances in Visual Auto-Regressive (VAR) modeling. VAR models break image tokenization into additive, gradually increasing scales, using Residual Quantization (RQ), an approach that aligns perfectly with our target ISR task. Previous works taking advantage of this synergy suffer from two main shortcomings. First, due to the limitations in RQ, they only generate images at a predefined fixed scale, failing to map intermediate outputs to the corresponding image scales. They also rely on large backbones or a large corpus of annotated data to achieve better performance. To address both shortcomings, we introduce two novel components to the VAR training for ISR, aiming at increasing its flexibility and reducing its complexity. In particular, we introduce a) a \textbf{Hierarchical Image Tokenization (HIT)} approach that progressively represents images at different scales while enforcing token overlap across scales, and b) a \textbf{Direct Preference Optimization (DPO) regularization term} that, relying solely on the (LR,HR) pair, encourages the transformer to produce the latter over the former. Our proposed HIT acts as a strong inductive bias for the VAR training, resulting in a small model (300M params vs 1B params of VARSR), that achieves state-of-the-art results without external training data, and that delivers multi-scale outputs with a single forward pass.

---


### 265. [Your CLIP has 164 dimensions of noise: Exploring the embeddings covariance eigenspectrum of contrastively pretrained vision-language transformers](https://arxiv.org/abs/2605.14893)

**<font color=#1a73e8>作者：</font>** Jakub Grzywaczewski, Dawid Płudowski, Przemysław Biecek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastively pre-trained Vision-Language Models (VLMs) serve as powerful feature extractors. Yet, their shared latent spaces are prone to structural anomalies and act as repositories for non-semantic, multi-modal noise. To address this phenomenon, we employ spectral decomposition of covariance matrices to decompose the VLM latent space into a multi-modal semantic signal component and a shared noise subspace. We observe that this noise geometry exhibits strong subgroup invariance across distinct data subsets. Crucially, pruning these shared noise dimensions is mainly harmless, preserving or actively improving downstream task performance. By isolating true semantic signals from artifactual noise, this work provides new mechanistic insights into the representational structure of modern VLMs, suggesting that a substantial fraction of their latent geometry is governed by shared, architecture-level noise rather than task-relevant semantics alone.

---


### 266. [SEDiT: Mask-Free Video Subtitle Erasure via One-step Diffusion Transformer](https://arxiv.org/abs/2605.14894)

**<font color=#1a73e8>作者：</font>** Zheng Hui, Yunlong Bai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent breakthroughs in video diffusion models have significantly accelerated the development of video editing techniques. However, existing methods often rely on inpainting video frames based on masked input, which requires extracting the target video mask in advance, and the precision of the segmentation directly affects the quality of the completion. In this paper, we present SEDiT, a novel one-stage video Subtitle Erasure approach via One-step Diffusion Transformer. We introduce a mask-free inference approach that enables direct erasure of the targeted subtitle. The proposed one-stage framework mitigates the sub-optimality inherent in the two-stage processing of prior models. Since subtitle removal is a localized editing task in which most pixels remain unchanged, the underlying distribution shift is minimal, making it well-suited to one-step generation under rectified flow. We empirically validate the reliability of one-step denoising and further provide a formal theoretical justification. Under the localized-editing structure of subtitle removal, the conditional optimal transport (OT) map and its induced rectified flow velocity field are Lipschitz continuous with respect to the latent variable, which underpins the theoretical feasibility of one-step sampling. To address the challenge of long-term temporal consistency, we adopt a hybrid training strategy by occasionally conditioning the model with a clean first-frame latent. This facilitates temporal continuity, allowing each segment during inference to leverage the output of its predecessor. To avoid visible seams caused by cropping and reinserting processed targets, particularly in scenarios involving substantial motion, we feed the original video directly into SEDiT. Thanks to one-step and chunk-wise streaming inference, our method can efficiently handle native 1440p video with infinite length.

---


### 267. [Critic-Driven Voronoi-Quantization for Distilling Deep RL Policies to Explainable Models](https://arxiv.org/abs/2605.14897)

**<font color=#1a73e8>作者：</font>** Senne Deproost, Denis Steckelmacher, Ann Nowé  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite many successful attempts at explaining Deep Reinforcement Learning policies using distillation, it remains difficult to balance the performance-interpretability trade-off and select a fitting surrogate model. In addition to this, traditional distillation only minimizes the distance between the behavior of the original and the surrogate policy while other RL-specific components such as action value are disregarded. To solve this, we introduce a new model-agnostic method called Critic-Driven Voronoi State Partitioning, which partitions a black box control policy into regions where a simple class of model can be optimized using gradient descent. By exploiting the critic value network of the original policy, we iteratively introduce new subpolicies in regions with insufficient value, standing in for a measure of policy complexity. The partitioning, a Voronoi quantizer, uses nearest neighbor lookups to assign a linear function to each point in the state space resulting in a cell-like diagram. We validate our approach on several well known benchmarks and proof that this distillation approaches the original policy using a reasonable sized set of linear functions.

---


### 268. [COREKG: Coreset-Guided Personalized Summarization of Knowledge Graphs](https://arxiv.org/abs/2605.14900)

**<font color=#1a73e8>作者：</font>** Sohel Aman Khan, Raghava Mutharaju, Supratim Shit  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Graphs (KGs) are extensively used across different domains and in several applications. Often, these KGs are very large in size. Such KGs become unwieldy for tasks such as question answering and visualization. Summarization of KGs offers a viable alternative in such cases. Furthermore, personalized KG summarization is crucial in the current data-driven world as it captures the specific requirements of users based on their query patterns. Since it only maintains relevant information, the personalized summaries of KG are small, resulting in significantly smaller storage requirements and query runtime. In this work, we adapt the coreset theory to create personalized KG summaries. For a given dataset and a user-specific query workload, we present an approach that samples a relevant subset of triples using sensitivity-based importance sampling. We ensure that the subset approximates the characteristics of the full dataset with bounded approximation error. We define sensitivity scores that measure the importance of a triple with respect to a user's query workload, which are then used by our coreset construction algorithm. We explicitly focus on personalized knowledge graph summarization by constructing summaries independently for each user based on their query behaviour.
Our evaluation on Freebase, WikiData, and DBpedia shows that COREKG delivers higher query-answering accuracy and structural coverage than the state-of-the-art methods, such as GLIMPSE, PPR, iSummary, PEGASUS and APEX$^2$ while requiring only a tiny fraction of the original graph.

---


### 269. [Representative Attention For Vision Transformers](https://arxiv.org/abs/2605.14913)

**<font color=#1a73e8>作者：</font>** Yuntong Li, Hainuo Wang, Hengxing Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Linear attention has emerged as a promising direction for scaling Vision Transformers beyond the quadratic cost of dense self-attention. A prevalent strategy is to compress spatial tokens into a compact set of intermediate proxies that mediate global information exchange. However, existing methods typically derive these proxy tokens from predefined spatial layouts, causing token compression to remain anchored to image coordinates rather than the semantic organization of visual content. To overcome this limitation, we propose Representative Attention (RPAttention), a linear global attention mechanism that performs token compression directly in representation space. Instead of constructing intermediate tokens from fixed spatial partitions, it dynamically forms a compact set of learned representative tokens to enable semantically related regions to communicate regardless of their spatial distance, by following a lightweight Gather-Interact-Distribute paradigm. Spatial tokens are first softly gathered into representative tokens through competitive similarity-based routing. The representatives then perform global interaction within a compact latent space, before broadcasting the refined information back to all spatial tokens via query-driven cross-attention. Via replacing coordinate-driven aggregation with representation-driven compression, RPAttention preserves global receptive fields while adaptively aligning token communication with the content structure of each this http URL reduces the dominant token interaction complexity from quadratic to linear scaling with respect to the number of spatial tokens, while maintaining expressive global context modeling. Extensive experiments across diverse vision transformer backbones on image classification, object detection, and semantic segmentation demonstrate the effectiveness of our design.

---


### 270. [TILBench: A Systematic Benchmark for Tabular Imbalanced Learning Across Data Regimes](https://arxiv.org/abs/2605.14915)

**<font color=#1a73e8>作者：</font>** Ruizhe Liu, Jiaqi Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imbalanced learning remains a fundamental challenge in tabular data applications. Despite decades of research and numerous proposed algorithms, a systematic empirical understanding of how different imbalanced learning methods behave across diverse data characteristics is still lacking. In particular, it remains unclear how different method families compare in predictive performance, robustness under varying data characteristics, and computational scalability. In this work, we present Tabular Imbalanced Learning Benchmark (TILBench), a large-scale empirical benchmark for tabular imbalanced learning. TILBench evaluates more than 40 representative algorithms across 57 diverse tabular datasets, resulting in over 200000 controlled experiments across a wide range of data characteristics. Our findings show that no single method consistently dominates across all settings; instead, the effectiveness of imbalanced learning methods depends strongly on dataset characteristics and computational constraints. Based on these findings, we provide practical recommendations for selecting appropriate methods in real-world applications.

---


### 271. [SceneParser: Hierarchical Scene Parsing for Visual Semantics Understanding](https://arxiv.org/abs/2605.14923)

**<font color=#1a73e8>作者：</font>** Pengxin Xu, Xincheng Lin, Luping Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General scene perception has progressed from object recognition toward open-vocabulary grounding, part localization, and affordance prediction. Yet these capabilities are often realized as isolated predictions that localize objects, parts, or interaction points without capturing the structured dependencies needed for interaction-oriented scene understanding. To address this gap, we introduce Hierarchical Scene Parsing, an interaction-oriented parsing task that represents physical scenes as explicit scene -> object -> part -> affordance hierarchies with cross-level bindings. We instantiate this task with SceneParser, a VLM-based parser trained for unified hierarchical generation with structural-completion pseudo labels and curriculum learning. To support training and evaluation, we construct SceneParser-Bench, a large-scale benchmark built with a scalable hierarchical data engine, containing 110K training images, a 5K validation split, 777K objects, 1.14M parts, 1.74M affordance annotations, and 1.74M valid object-part-affordance chain instances. We further introduce Level-1 to Level-3 conditional metrics and ParseRate to evaluate localization, cross-level binding, and hierarchical completeness. Experiments show that existing MLLMs and perception-stitching pipelines struggle with hierarchical parsing on our SceneParser-Bench, while SceneParser achieves stronger structure-aware performance. Besides, ablations, evaluations on COCO and AGD20K, and a downstream planning probe demonstrate that our SceneParser is compatible with conventional tasks and provides an actionable representation for visual understanding.

---


### 272. [Road Maps as Free Geometric Priors: Weather-Invariant Drone Geo-Localization with GeoFuse](https://arxiv.org/abs/2605.14925)

**<font color=#1a73e8>作者：</font>** Yunsong Fang, Tingyu Wang, Zhedong Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Drone-view geo-localization aims to match a query drone image, often captured under adverse weather conditions (e.g., rain, snow, fog), against a gallery of geo-tagged satellite images. Weather-induced degradations in the drone view, such as noise, reduced visibility, and partial occlusions, severely exacerbate the intrinsic cross-view domain gap. While prior methods predominantly rely on weather-specific architectures or data augmentations, they have largely overlooked road map data, a readily available modality that provides strong, inherently weather-invariant geometric layout cues (e.g., road networks and building footprints) at negligible additional cost. We introduce GeoFuse, a cross-modal fusion framework that integrates precisely aligned road map tiles with satellite imagery to yield more discriminative and weather-resilient representations. We first augment the existing University-1652 and DenseUAV benchmarks with geo-aligned road maps, supplying structural priors robust to meteorological variations. Building on this, we propose a flexible fusion module that combines satellite and road map features via token-level and channel-level interactions, with a lightweight dynamic gating mechanism that adaptively weights modality contributions per instance. Finally, we employ class-level cross-view contrastive learning to promote robust alignment between weather-degraded drone features and the fused satellite-roadmap representations. Extensive experiments under diverse weather conditions show that GeoFuse consistently outperforms state-of-the-art methods, achieving +3.46% and +23.18% Recall@1 accuracy on the University-1652 and DenseUAV benchmarks, respectively.

---


### 273. [SCRWKV: Ultra-Compact Structure-Calibrated Vision-RWKV for Topological Crack Segmentation](https://arxiv.org/abs/2605.14926)

**<font color=#1a73e8>作者：</font>** Hanxu Zhang, Chen Jia, Hui Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving pixel-level accurate segmentation of structural cracks across diverse scenarios remains a formidable challenge. Existing methods face significant bottlenecks in balancing crack topology modeling with computational efficiency, often failing to reconcile high segmentation quality with low resource demands. To address these limitations, we propose the Ultra-Compact Structure-Calibrated Vision RWKV (SCRWKV), a network that achieves high-precision modeling via a novel Structure-Field Encoder (SFE) backbone while maintaining linear complexity. The SFE integrates the Adaptive Multi-scale Cascaded Modulator (AMCM) to enhance texture representation and utilizes the Structure-Calibrated Insight Unit (SCIU) as its core engine. Specifically, the SCIU employs the Geometry-guided Bidirectional Structure Transformation (GBST) to capture topological correlations and integrates the Dynamic Self-Calibrating Decay (DSCD) into Dy-WKV to suppress noise propagation. Furthermore, we introduce a lightweight Cross-Scale Harmonic Fusion (CSHF) decoder to achieve precise feature aggregation. Systematic evaluations on multiple benchmarks characterized by complex textures and severe interference demonstrate that SCRWKV, with only 1.22M parameters, significantly outperforms SOTA methods. Achieving an F1 score of 0.8428 and mIoU of 0.8512 on the TUT dataset, the model confirms its robust potential for efficient real-world deployment. The code is available at this https URL.

---


### 274. [Learning with Shallow Neural Networks on Cluster-Structured Features](https://arxiv.org/abs/2605.14927)

**<font color=#1a73e8>作者：</font>** Elisabetta Cornacchia, Laurent Massoulié  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of deep learning in high-dimensional settings is often attributed to the presence of low-dimensional structure in real-world data. While standard theoretical models typically assume that this structure lies in the target function, projecting unstructured inputs onto a low-dimensional subspace, data such as images, text or genomic sequences exhibit strong spatial correlations within the input space itself. In this paper, we propose a tractable model to study how these correlations affect the sample complexity of learning with gradient descent on shallow neural networks. Specifically, we consider targets that depend on a small number of latent Boolean variables, and input features grouped into clusters and correlated with the latent variables. Under an identifiability assumption, we show that for a layerwise gradient-descent variant, the sample complexity scales with the number of hidden variables and, when the signal-to-noise ratio is sufficiently high, is independent of the input dimension, up to logarithmic terms. We empirically test our theoretical findings on both synthetic and real data.

---


### 275. [Multi-scale Coarse-to-fine Modeling for Test-time Human Motion Control](https://arxiv.org/abs/2605.14935)

**<font color=#1a73e8>作者：</font>** Nhat Le, Daochang Liu, Anh Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MSCoT, a multi-scale, coarse-to-fine model for test-time human motion synthesis and control. Unlike recent approaches that rely on multiple iterative denoising/token-prediction steps, or modules tailored for specific control signals, MSCoT discretizes motion into a multi-scale hierarchical representation and predicts the entire token sequence at each temporal scale in a coarse-to-fine fashion. Building on this coarse-to-fine paradigm, we propose an efficient multi-scale token guidance strategy that overcomes the challenge of discrete sampling and steers the token distribution towards the control goals, allowing for fast and flexible control. To address the limitations of a discrete codebook, a lightweight token refiner further adds continuous residuals to the discrete token embeddings and allows differentiable test-time refinement optimization to ensure precise alignment with the control objectives. MSCoT is able to produce quality motions, consistent with the control constraints, while offering substantially faster sampling than diffusion-based approaches. Experiments on popular benchmarks demonstrate state-of-the-art controllable text-to-motion generation performance of MSCoT over existing baselines, with better motion quality (48% FID improvement), higher control accuracy (-61% avg error), and $10 \times$ faster inference speed on HumanML3D.

---


### 276. [Slot-MPC: Goal-Conditioned Model Predictive Control with Object-Centric Representations](https://arxiv.org/abs/2605.14937)

**<font color=#1a73e8>作者：</font>** Jonathan Spieler, Angel Villar-Corrales, Sven Behnke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive world models enable agents to model scene dynamics and reason about the consequences of their actions. Inspired by human perception, object-centric world models capture scene dynamics using object-level representations, which can be used for downstream applications such as action planning. However, most object-centric world models and reinforcement learning (RL) approaches learn reactive policies that are fixed at inference time, limiting generalization to novel situations. We propose Slot-MPC, an object-centric world modeling framework that enables planning through Model Predictive Control (MPC). Slot-MPC leverages vision encoders to learn slot-based representations, which encode individual objects in the scene, and uses these structured representations to learn an action-conditioned object-centric dynamics model. At inference time, the learned dynamics model enables action planning via MPC, allowing agents to adapt to previously unseen situations. Since the learned world model is differentiable, we can use gradient-based MPC to directly optimize actions, which is computationally more efficient than relying on gradient-free, sampling-based MPC methods. Experiments on simulated robotic manipulation tasks show that Slot-MPC improves both task performance and planning efficiency compared to non-object-centric world model baselines. In the considered offline setting with limited state-action coverage, we find that gradient-based MPC performs better than gradient-free, sampling-based MPC. Our results demonstrate that explicitly structured, object-centric representations provide a strong inductive bias for controllable and generalizable decision-making. Code and additional results are available at this https URL.

---


### 277. [Not All Symbols Are Equal: Importance-Aware Constellation Design for Semantic Communication](https://arxiv.org/abs/2605.14940)

**<font color=#1a73e8>作者：</font>** Albert Shaju, Christo Kurisummoottil Thomas, Mayukh Roy Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semantic communication systems for goal-oriented transmission must protect task-relevant information not only through source compression but also via physical layer mapping. Existing approaches decouple constellation design and semantic encoding, exposing critical symbols to channel errors at the same rate as irrelevant ones. Contrary to this, in this paper, a joint semantic-physical layer framework is proposed, which is composed of a vector quantized-variational autoencoder that extracts discrete latent concepts, a semantic criticality indicator (SCI) that scores each concept by task relevance, and a deep reinforcement learning agent that dynamically selects the transmission subset based on instantaneous channel conditions. At the physical layer, a learned semantic-aware M -QAM constellation assigns symbol positions according to joint co-occurrence statistics and SCI scores, departing from the uniform spacing and Gray coding of standard M -QAM which minimizes average BER without regard for semantic content. We introduce a novel semantic symbol vulnerability (SSV) metric and a semantic protection probability (SPP) to quantify the exposure of task-critical symbols to decoding errors, and prove that any Gray-coded constellation is strictly suboptimal in SCI-Weighted SSV whenever the source exhibits non-uniform semantic importance and co-occurrence statistics. Simulation results demonstrate that the proposed constellation achieves near 100% SPP across modulation orders from 4-QAM to 1024-QAM versus 50% for standard constellations at high spectral efficiency, a 21:1 compression ratio with semantic quality above 0.9, generalizing across MNIST, Fashion-MNIST, and FSDD without modification.

---


### 278. [ACE-LoRA: Adaptive Orthogonal Decoupling for Continual Image Editing](https://arxiv.org/abs/2605.14948)

**<font color=#1a73e8>作者：</font>** Yuehao Liu, Weijia Zhang, Xuanming Shang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art diffusion models often rely on parameter-efficient fine-tuning to perform specialized image editing tasks. However, real-world applications require continual adaptation to new tasks while preserving previously learned knowledge. Despite the practical necessity, continual learning for image editing remains largely underexplored. We propose ACE-LoRA, a dynamic regularization framework for continual image editing that effectively mitigates catastrophic forgetting. ACE-LoRA leverages Adaptive Orthogonal Decoupling to identify and orthogonalize task interference, and introduces a Rank-Invariant Historical Information Compression strategy to address scalability issues in continual updates. To facilitate continual learning in image editing and provide a standardized evaluation protocol, we introduce CIE-Bench, the first comprehensive benchmark in this domain. CIE-Bench encompasses diverse and practically relevant image editing scenarios with a balanced level of difficulty to effectively expose limitations of existing models while remaining compatible with parameter-efficient fine-tuning. Extensive experiments demonstrate that our method consistently outperforms existing baselines in terms of instruction fidelity, visual realism, and robustness to forgetting, establishing a strong foundation for continual learning in image editing.

---


### 279. [A CUBS-Compatible Ultrasound Morphology and Uncertainty-Aware Baseline for Carotid Intima-Media Segmentation and Preliminary Risk Prediction](https://arxiv.org/abs/2605.14949)

**<font color=#1a73e8>作者：</font>** Aueaphum Aueawatthanaphisut  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Carotid atherosclerosis is a major contributor to ischemic stroke and transient ischemic attack. Conventional ultrasound assessment is commonly based on intima-media thickness, plaque appearance, stenosis degree, and peak systolic velocity, but these morphology- and velocity-based indicators may not fully capture patient-specific vascular risk. This study presents AtheroFlow-XNet, a CUBS-compatible ultrasound morphology and uncertainty-aware learning baseline for carotid intima-media segmentation and preliminary risk prediction. Using the Carotid Ultrasound Boundary Study dataset, manual lumen-intima and media-adventitia boundary annotations were converted into dense intima-media masks for supervised segmentation. Clinical variables were incorporated into an auxiliary risk-prediction branch, and Monte Carlo dropout was used for uncertainty-aware inference. The model was evaluated using a patient-level train-validation-test split with 1,522 training images, 326 validation images, and 328 testing images. The proposed model achieved a Dice coefficient of 0.7930 for LI-MA mask segmentation, a segmentation loss of 0.2359, and an area under the receiver operating characteristic curve of 0.6910 for preliminary risk prediction. Qualitative results showed that predicted masks were generally aligned with manual annotations, while uncertainty maps highlighted ambiguous wall-boundary regions. These results suggest that ultrasound-derived carotid morphology can support automated wall analysis and uncertainty-aware interpretation. Since CUBS does not provide Doppler waveforms or CFD-derived hemodynamic biomarkers, this work should be interpreted as a reproducible morphology-driven baseline. Future work will incorporate Doppler-derived flow profiles, patient-specific vascular reconstruction, and CFD-based wall shear biomarkers.

---


### 280. [Evo-Depth: A Lightweight Depth-Enhanced Vision-Language-Action Model](https://arxiv.org/abs/2605.14950)

**<font color=#1a73e8>作者：</font>** Tao Lin, Yuxin Du, Jiting Liu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action models have emerged as a promising paradigm for robotic manipulation by unifying perception, language grounding, and action generation. However, they often struggle in scenarios requiring precise spatial understanding, as current VLA models primarily rely on 2D visual representations that lack depth information and detailed spatial relationships. While recent approaches incorporate explicit 3D inputs such as depth maps or point clouds to address this issue, they often increase system complexity, require additional sensors, and remain vulnerable to sensing noise and reconstruction errors. Another line of work explores implicit 3D-aware spatial modeling directly from RGB observations without extra sensors, but it often relies on large geometry foundation models, resulting in higher training and deployment costs. To address these challenges, we propose Evo-Depth, a lightweight depth-enhanced VLA framework that enhances spatially grounded manipulation without relying on additional sensing hardware or compromising deployment efficiency. Evo-Depth employs a lightweight Implicit Depth Encoding Module to extract compact depth features from multi-view RGB images. These features are incorporated into vision-language representations through a Spatial Enhancement Module via depth-aware modulation, enabling efficient spatial-semantic enhancement. A Progressive Alignment Training strategy is further introduced to align the resulting depth-enhanced representations with downstream action learning. With only 0.9B parameters, Evo-Depth achieves superior performance across four simulation benchmarks. In real-world experiments, Evo-Depth attains the highest average success rate while also exhibiting the smallest model size, lowest GPU memory usage, and highest inference frequency among compared methods.

---


### 281. [Efficient Online Conformal Selection with Limited Feedback](https://arxiv.org/abs/2605.14953)

**<font color=#1a73e8>作者：</font>** Sreenivas Gollapudi, Kostas Kollias, Kamesh Munagala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the problem of conformal selection, where an agent must select a minimal subset of options to ensure that at least one ``success'' is identified with a pre-specified target probability $\phi$. While traditional online conformal prediction focuses on maintaining validity for the observed sequence, minimizing the resource cost (efficiency) of such selections, especially under limited feedback, remains a significant challenge. In this work, we consider settings with the most limited ``bandit'' feedback, and demonstrate that the simple Adaptive Conformal Inference (ACI) update rule, when applied to the appropriate control parameter or dual variable, is both adversarially valid, ensuring the success target is met on average for any input sequence (and hence under distribution shifts), and stochastically efficient, achieving sublinear efficiency regret for $i.i.d.$ inputs against an appropriate stochastic benchmark. We show such guarantees under canonical models capturing bandit and semi-bandit feedback to the agent via a unifying algorithmic technique, and analytic framework involving Lyapunov functions. Our approach handles more complex settings than prior work, while requiring significantly less feedback, and our results provide a new theoretical bridge between efficient online learning with limited feedback and distribution-free uncertainty quantification.

---


### 282. [H-OmniStereo: Zero-Shot Omnidirectional Stereo Matching with Heading-Aligned Normal Priors](https://arxiv.org/abs/2605.14963)

**<font color=#1a73e8>作者：</font>** Chenxing Jiang, Zhe Tong, Pusen Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereo matching on top-bottom equirectangular images provides an effective framework for full-surround perception, as vertically aligned epipolar lines enable the use of advanced perspective stereo architectures that are largely driven by large-scale datasets and monocular priors. However, the performance of such adaptations is severely limited by the scarcity of omnidirectional stereo datasets and the degradation of perspective monocular priors under spherical this http URL address these challenges, we propose H-OmniStereo, a zero-shot omnidirectional stereo matching framework. First, we construct high-quality synthetic dataset comprising over 2.8 million top-bottom equirectangular stereo pairs to scale up training. Second, we introduce an equirectangular monocular normal estimator, specifically operating in a heading-aligned coordinate system. Beyond providing distortion-robust and cross-view-consistent geometric priors for establishing reliable correspondences in stereo matching, this design boosts training efficiency and accommodates train-test FoV this http URL experiments show that our approach achieves higher accuracy than existing methods on out-of-domain datasets and successfully generalizes to real-world consumer camera setups using a single model. Both the model and the dataset will be open-sourced.

---


### 283. [Performance-Driven Policy Optimization for Speculative Decoding with Adaptive Windowing](https://arxiv.org/abs/2605.14978)

**<font color=#1a73e8>作者：</font>** Jie Jiang, Xing Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates LLM inference by having a lightweight draft model propose speculative windows of candidate tokens for parallel verification by a larger target model. In practice, speculative efficiency is often bottlenecked by hard-to-draft positions, where an early mismatch truncates the accepted prefix and invalidates the rest of the speculative window. Most learning-based drafters are still optimized with token-level supervised objectives, even though speculative utility is inherently window-level and prefix-sensitive. We propose PPOW (Performance-Driven Policy Optimization with Adaptive Windowing), a reinforcement learning framework that shifts drafter optimization from token-level imitation to window-level optimization. PPOW combines a Cost-Aware Speedup Reward, a Distribution-Based Proximity Reward, and Adaptive Divergence-Aware Windowing, which prioritizes informative windows with high confidence-weighted draft-target divergence. PPOW achieves average acceptance lengths of 6.29-6.52 and speedups of 3.39-4.36$\times$ across multiple model families and benchmarks under a unified decoding protocol. These results show that performance-driven window-level optimization is a practical approach to improving speculative decoding efficiency.

---


### 284. [MicroscopyMatching: Towards a Ready-to-use Framework for Microscopy Image Analysis in Diverse Conditions](https://arxiv.org/abs/2605.14980)

**<font color=#1a73e8>作者：</font>** Xiaofei Hui, Haoxuan Qu, Hossein Rahmani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analyzing microscopy images to extract biological object properties (e.g., their morphological organization, temporal dynamics, and population density) is fundamental to various biomedical research. Yet conducting this manually is costly and time-consuming. Though deep learning-based approaches have been explored to automate this process, the substantial diversity of microscopy analysis settings in practice (including variations of biological object types, sample processing protocols, imaging equipment, and analysis tasks, etc.) often renders them ineffective. As a result, these approaches typically require extensive adaptation for different settings, which, however, can impose burdens that are often practically unsustainable for laboratories, forcing biomedical researchers to still commonly rely on manual analysis, thereby severely bottlenecking the pace of biomedical research progress. This situation has created a pressing and long-standing need for a reliable and broadly applicable microscopy image analysis tool, yet such a tool is still missing. To address this gap, we present the first ready-to-use microscopy image analysis framework, MicroscopyMatching, that can reliably perform key analysis tasks (including segmentation, tracking, and counting) across diverse microscopy analysis settings. From a fundamentally different perspective, MicroscopyMatching reformulates diverse microscopy image analysis tasks as a unified matching problem, effectively handling this problem by exploiting the robust matching capability from pre-trained latent diffusion models.

---


### 285. [Distance-Matrix Wasserstein Statistics for Scalable Gromov--Wasserstein Learning](https://arxiv.org/abs/2605.14981)

**<font color=#1a73e8>作者：</font>** Ao Xu, Tieru Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gromov--Wasserstein (GW) distances compare graphs, shapes, and point clouds through internal distances, without requiring a common coordinate system. This invariance is powerful, but discrete GW is a nonconvex quadratic optimal transport problem and is difficult to estimate at scale. We propose \emph{Distance-Matrix Wasserstein} (DMW), a hierarchy of Wasserstein statistics comparing laws of random finite distance matrices. Rather than optimizing a global point-level alignment, DMW samples $n$ points from each space, records their pairwise distances, and transports the resulting matrix laws. We prove that DMW is a relaxation and lower bound of GW, and establish a reverse approximation inequality: the GW--DMW gap is controlled by the Wasserstein error of approximating each original measure with $n$ samples. Hence population DMW converges to GW as sampled subspaces become dense. We further give finite-sample bounds, including intrinsic-dimensional rates that depend on the data manifold rather than the ambient matrix dimension $\binom n2$. For scalable computation, we introduce sliced and multi-scale DMW; for $p=1$, the sliced multi-scale dissimilarity yields positive-definite exponential kernels. Experiments on synthetic metric spaces, scalability benchmarks, graph classification, and two-sample testing validate the theory and demonstrate an interpretable GW-style proxy for structural comparison.

---


### 286. [Second-Order Actor-Critic Methods for Discounted MDPs via Policy Hessian Decomposition](https://arxiv.org/abs/2605.14982)

**<font color=#1a73e8>作者：</font>** Sanjeev Manivannan, Shuban V  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the discounted reward setting in reinforcement learning (RL). To mitigate the value approximation challenges in policy gradient methods, actor-critic approaches have been developed and are known to converge to stationary points under suitable assumptions. However, these methods rely on first-order updates. In contrast, second-order optimization provides principled curvature-aware updates that are proven to accelerate convergence, but its application in RL is limited by the computational complexity of Hessian estimation. In this work, we analyze second-order approximations for the actor update that leverage the full curvature information of the objective as much as possible. A stable approximation requires treating the action-value function as locally constant with respect to policy parameters, which does not generally hold in policy gradient methods. We show that this approximation becomes well-justified under a two-timescale actor-critic framework, where the critic evolves on a faster timescale and can be treated as quasi-stationary during actor updates. Building on this insight, we formulate a second-order actor-critic method for the discounted reward setting that leverages Hessian-vector product (HVP) computations, resulting in a computationally efficient and stable second-order update.

---


### 287. [Sat3DGen: Comprehensive Street-Level 3D Scene Generation from Single Satellite Image](https://arxiv.org/abs/2605.14984)

**<font color=#1a73e8>作者：</font>** Ming Qian, Zimin Xia, Changkun Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating a street-level 3D scene from a single satellite image is a crucial yet challenging task. Current methods present a stark trade-off: geometry-colorization models achieve high geometric fidelity but are typically building-focused and lack semantic diversity. In contrast, proxy-based models use feed-forward image-to-3D frameworks to generate holistic scenes by jointly learning geometry and texture, a process that yields rich content but coarse and unstable geometry. We attribute these geometric failures to the extreme viewpoint gap and sparse, inconsistent supervision inherent in satellite-to-street data. We introduce Sat3DGen to address these fundamental challenges, which embodies a geometry-first methodology. This methodology enhances the feed-forward paradigm by integrating novel geometric constraints with a perspective-view training strategy, explicitly countering the primary sources of geometric error. This geometry-centric strategy yields a dramatic leap in both 3D accuracy and photorealism. For validation, we first constructed a new benchmark by pairing the VIGOR-OOD test set with high-resolution DSM data. On this benchmark, our method improves geometric RMSE from 6.76m to 5.20m. Crucially, this geometric leap also boosts photorealism, reducing the Fréchet Inception Distance (FID) from $\sim$40 to 19 against the leading method, Sat2Density++, despite using no extra tailored image-quality modules. We demonstrate the versatility of our high-quality 3D assets through diverse downstream applications, including semantic-map-to-3D synthesis, multi-camera video generation, large-scale meshing, and unsupervised single-image Digital Surface Model (DSM) estimation. The code has been released on this https URL.

---


### 288. [Compositional Video Generation via Inference-Time Guidance](https://arxiv.org/abs/2605.14988)

**<font color=#1a73e8>作者：</font>** Ariel Shaulov, Eitan Shaar, Amit Edenzon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video diffusion models generate realistic videos, but often fail on prompts requiring fine-grained compositional understanding, such as relations between entities, attributes, actions, and motion directions. We hypothesize that these failures need not be addressed by retraining the generator, but can instead be mitigated by steering the denoising process using the model's own internal grounding signals. We propose \textbf{CVG}, an inference-time guidance method for improving compositional faithfulness in frozen text-to-video models. Our key observation is that cross-attention maps already encode how prompt concepts are grounded across space and time. We train a lightweight compositional classifier on these attention features and use its gradients during early denoising steps to steer the latent trajectory toward the desired composition. Built on a frozen VLM backbone, the classifier transfers across semantically related composition labels rather than relying only on narrow category-specific features. CVG improves compositional generation without modifying the model architecture, fine-tuning the generator, or requiring layouts, boxes, or other user-supplied controls. Experiments on compositional text-to-video benchmarks show improved prompt faithfulness while preserving the visual quality of the underlying generator.

---


### 289. [Characterizing the visual representation of objects from the child's view](https://arxiv.org/abs/2605.14990)

**<font color=#1a73e8>作者：</font>** Jane Yang, Tarun Sepuri, Alvin Wei Ming Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Children acquire object category representations from their everyday experiences in the first few years of life. What do the inputs to this learning process look like? We analyzed first-person videos of young children's visual experience at home from the BabyView dataset ($N$ = 31 participants, 868 hours, ages 5--36 months), using a supervised object detection model to extract common object categories from more than 3 million frames. We found that children's object category exposure was highly skewed: a few categories (e.g., cups, chairs) dominated children's visual experiences while most categories appeared rarely, replicating previous findings from a more restricted set of contexts. Category exemplars were highly variable: children encountered objects from unusual angles, in highly cluttered scenes, and partially occluded views; many categories (especially animals) were most frequently viewed as depictions. Surprisingly, despite this variability, detected categories (e.g., giraffes, apples) showed stronger groupings within superordinate categories (e.g., animals, food) relative to groupings derived from canonical photographs of these categories. We found this same pattern when using high-dimensional embeddings from both self-supervised visual and multimodal models; this effect was also recapitulated in densely sampled data from individual children. Understanding the robustness and efficiency of visual category learning will require the development of models that can exploit strong superordinate structure and learn from non-canonical, sparse, and variable exemplars.

---


### 290. [Predicting Response to Neoadjuvant Chemotherapy in Ovarian Cancer from CT Baseline Using Multi-Loss Deep Learning](https://arxiv.org/abs/2605.14991)

**<font color=#1a73e8>作者：</font>** Francesco Pastori, Francesca Fati, Marina Rosanu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ovarian cancer is the most lethal gynecologic malignancy: around 60% of patients are diagnosed at an advanced stage, with an associated 5-year survival rate of about 30%. Early identification of non-responders to neoadjuvant chemotherapy remains a key unmet need, as it could prevent ineffective therapy and avoid delays in optimal surgical management. This work proposes a non-invasive deep learning framework to predict neoadjuvant chemotherapy response from pre-treatment contrast-enhanced CT by leveraging automatically derived 3D lesion masks. The approach encodes axial slices with a partially fine-tuned pretrained image encoder and aggregates slice-level representations into a volumetric embedding through an attention-based module. Training combines classification loss with supervised contrastive regularization and hard-negative mining to improve separation between ambiguous responders and non-responders. The method was developed on a retrospective single-center cohort from the European Institute of Oncology (Milan, IT), including 280 eligible patients (147 responder, 133 non-responder). On the test cohort, the model achieved a ROC-AUC of 0.73 (95% CI: 0.58-0.86) and an F1-score of 0.70 (95% CI: 0.56-0.82). Overall, these results suggest that the proposed architecture learns clinically relevant predictive patterns and provides a robust foundation for an imaging-based stratification tool.

---


### 291. [Learning Developmental Scaffoldings to Guide Self-Organisation](https://arxiv.org/abs/2605.14998)

**<font color=#1a73e8>作者：</font>** Milton L. Montero, Elias Najarro, Jakob Schauser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> From subcellular structures to entire organisms, many natural systems generate complex organisation through self-organisation: local interactions that collectively give rise to global structure without any blueprint of the outcome. Yet a significant portion of the information driving such processes is not produced by self-organisation itself, instead, it is often offloaded to initial conditions of the system. Biological development is a prime example, where maternal pre-patterns encode positional and symmetry-breaking information that scaffolds the self-organising process. From maternal morphogen gradients in early embryogenesis to tissue-level morphogenetic pre-patterns guiding organ formation, this transfer of information to initial conditions, analogous to a memory-compute trade-off in computational systems, is a fundamental part of developmental processes. In this work, we study this offloading phenomenon by introducing a model that jointly learns both the self-organisation rules and the pre-patterns, allowing their interplay to be varied and measured under controlled conditions: a Neural Cellular Automaton (NCA) paired with a learned coordinate-based pattern generator (SIREN), both trained simultaneously to generate a set of patterns. We provide information-theoretic analyses of how information is distributed between pre-patterns and the self-organising process, and show that jointly learning both components yields improvements in robustness, encoding capacity, and symmetry breaking over purely self-organising alternatives. Our analysis further suggests that effective pre-patterns do not simply approximate their targets; rather, they bias the developmental dynamics in ways that facilitate convergence, pointing to a non-trivial relationship between the structure of initial conditions and the dynamics of self-organisation.

---


### 292. [Towards Gaze-Informed AI Disclosure Interfaces: Eye-Tracking Attentional and Cognitive Load While Reading AI-Assisted News](https://arxiv.org/abs/2605.14999)

**<font color=#1a73e8>作者：</font>** Pooja Prajod, Hannes Cools, Thomas Röggla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative AI becomes increasingly integrated into journalism, designing effective AI-use disclosures that inform readers without imposing unnecessary burden is a key challenge. While prior research has primarily focused on trust and credibility, the impact of disclosures on readers' attentional and cognitive load remains underexplored. To address this gap, we conducted a $3\times2\times2$ mixed factorial study manipulating the level of AI-use disclosure detail (none, one-line, detailed), news type (politics, lifestyle), and role of AI (editing, partial content generation), measuring load via NASA-TLX and eye-tracking. Our results reveal a significant attentional cost: one-line disclosures resulted in significantly higher fixation durations and saccade counts, particularly for AI-edited content. Detailed disclosures did not impose additional burden. Drawing on Information-Gap Theory, we argue that brief labels may trigger increased visual scrutiny by alerting readers to AI use without providing enough information. NASA-TLX scores and pupil diameter showed no significant differences across conditions, suggesting that AI-use disclosures do not impose cognitive burden regardless of the detail level. Interview insights contextualize these findings and reveal a strong preference for detailed or ``detail-on-demand'' designs. Our findings inform the design of gaze-informed adaptive disclosure interfaces that dynamically adjust transparency levels based on readers' attentional patterns and news context.

---


### 293. [DeepTokenEEG Enhancing Mild Cognitive Impairment and Alzheimers Classification via Tokenized EEG Features](https://arxiv.org/abs/2605.15009)

**<font color=#1a73e8>作者：</font>** Thinh Nguyen-Quang, Minh Long Ngo, Ngoc-Son Nguyen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The detection of Alzheimers disease (AD) is considered crucial, as timely intervention can improve patient outcomes. Electroencephalogram (EEG)-based diagnosis has been recognized as a non-invasive, accessible, and cost-effective approach for AD detection; however, it faces challenges related to data availability, accuracy of modern deep learning methods, and the time-consuming nature of expert-based interpretation. In this study, a novel lightweight and high-performance model, DeepTokenEEG, was designed for the diagnosis of AD and the classification of EEG signals from AD patients, individuals with other neurological conditions, and healthy subjects. Unlike traditional heavy-weight models, DeepTokenEEG ultilizes spatial and temporal tokenizer that effectively captures AD-related biomarkers in both temporal and frequency domain with only 0.29 million paramaters. Trained in a combined dataset of 274 subjects, including 180 AD cases, and 94 healthy controls, the proposed method achieves a maximum recorded accuracy of 100% on specific frequency bands, representing an improvement of 1.41-15.35% over state-of-the-art methods on the same dataset. These results indicate the potential of DeepTokenEEG for early detection and screening of AD, with promising applicability for deployment due to its compact size.

---


### 294. [3D Skew-Normal Splatting](https://arxiv.org/abs/2605.15010)

**<font color=#1a73e8>作者：</font>** Xiangru Wu, Ke Fan, Yanwei Fu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has emerged as a leading representation for real-time novel view synthesis and been widely adopted in various downstream applications. The core strength of 3DGS lies in its efficient kernel-based scene representation, where Gaussian primitives provide favorable mathematical and computational properties. However, under a finite primitive budget, the symmetric shape of each primitive directly affects representation compactness, especially near asymmetric structures such as object boundaries and one-sided surfaces. Recent works have explored more complex kernel distributions, yet they either remain within the elliptical family or rely on hard truncation, which limits continuous shape control and introduces distributional discontinuities. In this paper, we propose Skew-Normal Splatting (SNS), which adopts the Azzalini Skew-Normal distribution as the fundamental primitive. By introducing a learnable and bounded skewness parameter, SNS can continuously interpolate between symmetric Gaussians and Half-Gaussian-like shapes, enabling flexible modeling of both sharp boundaries and interior regions. Moremover, SNS preserves analytical tractability under affine transformations and marginalization. This property allows seamless integration into existing Gaussian Splatting rasterization this http URL, to address the strong coupling between scale, rotation, and skewness parameters, we introduce a decoupled parameterization and a block-wise optimization strategy to enhance training stability and accuracy. Extensive experiments on standard novel-view synthesis benchmarks show that SNS consistently improves reconstruction quality over Gaussian and recent non-Gaussian kernels, with clearer benefits on sharp boundaries and thin or one-sided structures.

---


### 295. [The Scientific Contribution Graph: Automated Literature-based Technological Roadmapping at Scale](https://arxiv.org/abs/2605.15011)

**<font color=#1a73e8>作者：</font>** Peter A. Jansen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific contributions rarely develop in isolation, but instead build upon prior discoveries. We formulate the task of automated technological roadmapping as extracting scientific contributions from scholarly articles and linking them to their prerequisites. We present the Scientific Contribution Graph, a large-scale AI/NLP-domain resource containing 2 million detailed scientific contributions extracted from 230k open-access papers and connected by 12.5 million prerequisite edges. We further introduce scientific prerequisite prediction, a scientific discovery task in which models predict which existing technologies can enable future discoveries, and show that contemporary models are rapidly improving on this task, reaching 0.48 MAP when evaluated using temporally filtered backtesting. We anticipate technological roadmapping resources such as this will support scientific impact assessment and automated scientific discovery.

---


### 296. [COTCAgent: Preventive Consultation via Probabilistic Chain-of-Thought Completion](https://arxiv.org/abs/2605.15016)

**<font color=#1a73e8>作者：</font>** Zihan Deng, Xiaozhen Zhong, Chuanzhi Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models empower healthcare, intelligent clinical decision support has developed rapidly. Longitudinal electronic health records (EHR) provide essential temporal evidence for accurate clinical diagnosis and analysis. However, current large language models have critical flaws in longitudinal EHR reasoning. First, lacking fine-grained statistical reasoning, they often hallucinate clinical trends and metrics when quantitative evidence is textually implied, biasing diagnostic inference. Second, non-uniform time series and scarce labels in longitudinal EHR hinder models from capturing long-range temporal dependencies, limiting reliable clinical reasoning. To address the above limitations, this work presents the Probabilistic Chain-of-Thought Completion Agent (COTCAgent), a hierarchical reasoning framework for longitudinal electronic health records. It consists of three core modules. The Temporal-Statistics Adapter (TSA) converts analytical plans into executable code for standardized trend output. The Chain-of-Thought Completion (COTC) layer leverages a symptom-trend-disease knowledge base with weighted scoring to evaluate disease risk, while the bounded completion module acquires structured evidence through standardized inquiries and iterative scoring constraints to ensure rigorous reasoning. By decoupling statistical computation, feature matching, and language generation, the framework eliminates reliance on complex multi-modal inputs and enables efficient longitudinal record analysis with lower computational overhead. Experimental results show that COTCAgent powered by Baichuan-M2 achieves 90.47% Top-1 accuracy on the self-built dataset and 70.41% on HealthBench, outperforming existing medical agents and mainstream large language models. The code is available at this https URL.

---


### 297. [Generalized Priority-Aware Shapley Value](https://arxiv.org/abs/2605.15018)

**<font color=#1a73e8>作者：</font>** Kiljae Lee, Ziqi Liu, Weijing Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shapley value and its priority-aware extensions are widely used for valuation in machine learning, but existing methods require pairwise priority to be binary and acyclic, a restriction spectacularly violated in real-data examples such as aggregated human preferences and multi-criterion comparisons. We introduce the generalized priority-aware Shapley value (GPASV), a random order value defined on arbitrary directed weighted priority graphs, in which pairwise edges penalize rather than forbid order violations. GPASV covers a range of classical models as boundary cases. We establish GPASV through an axiomatic characterization, develop the associated computational methods, and introduce a priority sweeping diagnostic extending PASV's. We apply GPASV to LLM ensemble valuation on the cyclic Chatbot Arena preference graph, illustrating that priority-aware valuation is not a one-button operation: different balances of pairwise graph priority versus individual soft priority produce substantively different valuations of the same data.

---


### 298. [HiSem: Hierarchical Semantic Disentangling for Remote Sensing Image Change Captioning](https://arxiv.org/abs/2605.15024)

**<font color=#1a73e8>作者：</font>** Man Wang, Chenyang Liu, Wenjun Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing image change captioning (RSICC) aims to achieve high-level semantic understanding of genuine changes occurring between bi-temporal images. Despite notable progress, existing methods are fundamentally limited by a shared modeling assumption: changed and unchanged image pairs, which have intrinsically different semantic granularities, are processed under a unified modeling strategy. This modeling inconsistency leads to semantic entanglement between coarse-grained change existence judgment and fine-grained semantic this http URL address the above limitation, we propose a novel hierarchical semantic disentangling network (HiSem) that explicitly disentangles semantic representations of different granularities. Specifically, we first introduce the Bidirectional Differential Attention Modulation (BDAM) module that leverages discrepancy-aware attention to enhance cross-temporal interactions, thereby amplifying true change signals while suppressing irrelevant variations. Building upon this, we design a Hierarchical Adaptive Semantic Disentanglement (HASD) module that performs adaptive routing at two hierarchical levels: a coarse-grained image-level routing mechanism distinguishes changed and unchanged image pairs, while a fine-grained token-level Mixture-of-Experts (MoE) block models diverse and heterogeneous change semantics for changed samples. Extensive experiments on two benchmark datasets demonstrate that HiSem outperfoms previous methods, achieving a significant improvement of +7.52\% BLEU-4 on the WHU-CDC dataset. More importantly, our approach provides a structured perspective for RSICC by explicitly aligning model design with the intrinsic semantic heterogeneity of bi-temporal scenes. The code will be available at this https URL

---


### 299. [WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections](https://arxiv.org/abs/2605.15030)

**<font color=#1a73e8>作者：</font>** Tri Cao, Yulin Chen, Hieu Cao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web agents can autonomously complete online tasks by interacting with websites, but their exposure to open web environments makes them vulnerable to prompt injection attacks embedded in HTML content or visual interfaces. Existing guard models still suffer from limited generalization to unseen domains and attack patterns, high false positive rates on benign content, reduced deployment efficiency due to added latency at each step, and vulnerability to adversarial attacks that evolve over time or directly target the guard itself. To address these limitations, we propose WARD (Web Agent Robust Defense against Prompt Injection), a practical guard model for secure and efficient web agents. WARD is built on WARD-Base, a large-scale dataset with around 177K samples collected from 719 high-traffic URLs and platforms, and WARD-PIG, a dedicated dataset designed for prompt injection attacks targeting the guard model. We further introduce A3T, an adaptive adversarial attack training framework that iteratively strengthens WARD through a memory-based attacker and guard co-evolution process. Extensive experiments show that WARD achieves nearly perfect recall on out-of-distribution benchmarks, maintains low false positive rates to preserve agent utility, remains robust against guard-targeted and adaptive attacks under substantial distribution shifts, and runs efficiently in parallel with the agent without introducing additional latency.

---


### 300. [TopoPrimer: The Missing Topological Context in Forecasting Models](https://arxiv.org/abs/2605.15035)

**<font color=#1a73e8>作者：</font>** Zara Zetlin, Kayhan Moharreri, Maria Safi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce TopoPrimer, a framework that makes the global topological structure of the series population an explicit input
to any forecasting model. TopoPrimer improves accuracy across diverse domains, stabilizes forecasts under seasonal demand
spikes, and closes the cold-start gap. Precomputed once per domain via persistent homology and spectral sheaf coordinates,
TopoPrimer deploys per token for fully-trained models and as a lightweight adapter for pre-trained backbones. Of these two
components, sheaf coordinates are the primary accuracy driver. Across four public benchmarks on Chronos and TimesFM,
TopoPrimer consistently improves forecasting accuracy, with gains of up to 7.3% MSE on ECL. The topology advantage persists
with near-identical magnitude across zero-shot and fine-tuned backbones, suggesting topology and per-series training
capture complementary signals. The gains are most pronounced in difficult regimes. Under peak seasonal demand, classical
and zero-shot models degrade by up to 50%, while TopoPrimer stays within 10%. At cold start with no item history,
TopoPrimer reduces MAE by 27% over a topology-free baseline.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-337](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
