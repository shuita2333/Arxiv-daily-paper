# 📦 其他研究 | 2026年08月28日

> 本类共 **171** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-171](./part-04.md)

---

### 101. [Frequency-aware forecasting for short-term typhoon gust prediction](https://arxiv.org/abs/2608.25604)

**<font color=#1a73e8>作者：</font>** Xuefei Wang, Tingyi Liu, Heng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate gust forecasting under typhoon conditions remains challenging due to the highly non-stationary and multi-scale characteristics of extreme wind fluctuations. Existing deep learning models often struggle to simultaneously capture long-term trends and rapid local variations, resulting in degraded performance during extreme events. We propose WDANet, a frequency-aware forecasting framework that integrates stationary wavelet decomposition, a Feature-wise Linear Modulation (FiLM) strategy, and a dual-branch encoder-decoder architecture, enabling separate modeling of trend and fluctuation components. Taking the offshore regions of the Western Pacific in China as an example, we conduct fine-grid wind gust prediction research. The results demonstrate that WDANet shows advantages for short lead times under the experimental setting across a 24-h forecasting horizon and achieves higher prediction accuracy than ECMWF-HRES within the first 6 h. During extreme wind events, WDANet more accurately captures gust peaks and attains the best RMSE and MAE performance. These results highlight its potential for offshore wind power operation, disaster warning, and risk mitigation.

---


### 102. [When Should a Network Emit Geometry, and When Should It Detect It? Readout, Reconciliation, and Representation in Floorplan Vectorization](https://arxiv.org/abs/2608.25608)

**<font color=#1a73e8>作者：</font>** He Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A network trained to recover the walls, openings, and rooms of a rasterized floorplan can produce its output in two ways: by emitting the geometry as an autoregressive coordinate sequence, or by detecting it on dense junction and centerline heatmaps and assembling a graph. We compare the two readouts on the same trained network. On real scans (CubiCasa5K) detection is better on every wall measure (+2.7 wall F1 at tolerance 0.05, +5.1 at 0.015; paired bootstrap intervals exclude zero), and reading an opening heatmap the decoder never used raises opening F1 by 2.6x without retraining. Within real scans the readout's advantage grows with plan size and reverses on small plans; on clean vector renders sequence decoding is better by 5 to 8 points where its training covered the render style, while under full domain shift the readout, given calibrated thresholds, stays ahead; neither ink density nor plan size explains the reversal. With matched data and recipe, a room-centric system with a reconciliation step and a wall-first sequence model reach comparable wall quality, so the output representation matters less than is usually assumed. A prior from the other family helps at the output but not at the input: deterministic fusion of the two outputs raises wall F1 by 7 points, whereas conditioning one model on the other's output gives no gain in three forms, including two ground-truth-content controls. We also provide an edit-cost metric that scores a draft by the human work needed to correct it, corrected CubiCasa5K annotations, and ResPlan-FP, a CC BY 4.0 benchmark of 16,998 plans with frozen splits and three baseline tracks. Code, the benchmark, and the corrected annotations are available at this https URL

---


### 103. [On the Separation of Human and AI-Generated Images in CLIP Embedding Space](https://arxiv.org/abs/2608.25609)

**<font color=#1a73e8>作者：</font>** Andrea Asperti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We identify a previously unreported phenomenon in CLIP representations: human and AI-generated paintings spontaneously separate along the dominant principal directions of their joint embedding distribution, without any supervised objective designed to distinguish the two classes. Rather than exploiting this phenomenon for detection, our objective is to interpret it: we seek to identify the visual information underlying the separation and to trace it back from the embedding space to the image domain. We pursue this objective through a progressive investigation combining interpretable image representations with gradient-based inversion, used systematically as an experimental probe of the relationships identified in feature space. Robustness experiments and increasingly expressive statistical descriptors progressively rule out several intuitive explanations based on global image properties and simple local statistics, and point instead to distributed multiscale image structure. Multiscale scattering provides the most informative interpretable representation considered, but offers only a partial account of the phenomenon.
Direct inversion provides a complementary and striking observation: substantial displacements along the dominant CLIP directions can be induced by image perturbations that remain nearly imperceptible to human observers, showing that the directions involved in the separation are highly sensitive to image variations with very low perceptual salience for humans. Taken together, these results reveal a significant difference between the visual evidence reflected in CLIP representations and that readily accessible to human perception, raising broader questions about the relationship between artificial and human vision and, ultimately, between artificial and human aesthetic judgment.

---


### 104. [Using profiles of cognitive capability to assess AI suitability for workplace tasks](https://arxiv.org/abs/2608.25623)

**<font color=#1a73e8>作者：</font>** Jonathan Prunty, Marko Tešić, Patrick Quinn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organisations deploying AI face a scoping problem: which tasks can be automated, which should remain with humans, and which are best shared between the two. Aggregate benchmark scores provide little insight into where systems will succeed or fail in practice, while human judgements of model capabilities quickly become outdated. We introduce a pipeline that profiles agents and tasks using a shared set of core cognitive capabilities. Cognitive capability profiling infers an agent's capabilities from performance on a benchmark battery annotated for the cognitive demands of each item. Task requirements weighting elicits from domain experts the relative importance of these same capabilities for their work. As both use a common set of cognitive dimensions, they can be updated independently as models and roles change, and combined to estimate AI suitability at the level of a domain, organisation, role, or individual duty. We validate capability recovery on synthetic agents, profile six AI systems, and elicit task requirements from 410 employees across six occupational domains. AI systems differed more across cognitive dimensions than across model families, while workplace activities converged on a shared cognitive core. The resulting scores provide a comparative scoping tool for identifying promising candidates for piloting and areas where current systems are unlikely to be well suited. We discuss extending the framework to profile human workers alongside AI systems, moving from AI suitability towards human-machine task allocation.

---


### 105. [SeVeR: Selective Visual Exposure and Retrieval for 3D Medical Image Question Answering](https://arxiv.org/abs/2608.25630)

**<font color=#1a73e8>作者：</font>** Yaojun Hu, Danyang Tu, Yang Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Volumetric medical VQA requires reasoning over long and redundant 3D visual token sequences, especially in multi-sequence MRI where complementary modalities provide diverse diagnostic cues but expose the decoder to many repeated anatomical regions. To investigate reasoning under multi-sequence visual redundancy, we first introduce BreMRIs-VQA, a clinically curated breast MRI benchmark with 1.19M QA pairs from 71.0K sequences and 12.9K patients, covering both free-text and multiple-choice questions. We further propose SeVeR, a selective visual exposure framework that compresses dense volumes into modality-wise prototypes and retrieves complementary multi-level evidence with change-aware gated attention during decoding, trained with a marginal-utility self-consistency objective that suppresses unhelpful retrieval. Experiments on BreMRIs-VQA and public benchmarks show that SeVeR improves both discriminative and generative performance while exposing substantially fewer visual tokens.

---


### 106. [DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search](https://arxiv.org/abs/2608.25635)

**<font color=#1a73e8>作者：</font>** Junzhao Zhang, Tao Zhang, Liren Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial e-commerce search systems ultimately aim to optimize the user-level long-term objective, such as n-day cumulative purchases or gross merchandise value (GMV) per user. However, such objectives are defined at the user level, whereas search ranking is based on item-level scores within each request. Existing methods typically bridge this granularity gap through manually designed multi-objective fusion, where predictions of multiple item-level objectives, such as clicks, carts, purchases, and transaction value, are combined into a ranking score that serves as a proxy for the ultimate objective. Such hand-crafted fusion schemes rely on a small set of manually tuned weights, limiting fine-grained personalization and leading to suboptimal alignment with the ultimate objective. In this paper, we propose DCEO (Direct Causal Effect Optimization), a data-driven framework for learning item-level proxy scores that are better aligned with the ultimate objective. We first aggregate the item-level proxy scores into a user-level proxy metric and quantify its alignment with the ultimate objective using a relative causal effect. We then develop an actor-critic framework, where the critic estimates the ultimate objective for a given user-level proxy metric, and the actor dynamically generates context-dependent fusion weights over multiple objectives to construct the item-level proxy scores and is trained to directly optimize the relative causal effect. Extensive offline experiments and analyses demonstrate the effectiveness and interpretability of DCEO. In addition, DCEO has been deployed in a large-scale industrial e-commerce search system, outperforming the conventional GMV proxy by 0.36% in GMV in a 41-day online A/B test.

---


### 107. [LDAC-Net: A Learnable Multi-Lag Differencing Attention-Convolution Network for Drift-Robust Recognition with Low-Cost MOX Gas Sensors](https://arxiv.org/abs/2608.25646)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Liangxiu Han, Yue Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Portable electronic-nose systems based on low-cost metal-oxide (MOX) gas sensors offer a practical solution for gas and odour recognition, but their signals are affected by slow chemical transients, drifting sensor offsets, scale variation, and cross-channel correlations. Existing pipelines commonly use fixed first-order temporal differencing (FOTD), which requires a manually selected lag and may discard useful response information. We propose LDAC-Net, an end-to-end learnable multi-lag differencing attention-convolution network that operates directly on multi-channel MOX signals. Its learnable differential feature enhancement front-end combines window-conditioned statistical affine normalisation, which compensates for window-specific offset and scale variation, with learnable multi-lag differencing, which weights and combines temporal differences across multiple lags. A compact attention-convolution backbone subsequently models local transients and longer-range temporal dependencies. On the 50-class SmellNet-Base task, LDAC-Net achieves 68.2% top-1 accuracy, exceeding the best FOTD-preprocessed comparison model by approximately 14 percentage points and the raw-input Transformer by more than 30 points. Ablation studies confirm the contributions of both proposed components. The representation also transfers to SmellNet-Mixtures, improving accuracy from 45.4% to 50.5%, and generalises to the 62-channel eNose-Drift benchmark under strong long-term drift, achieving 70.6% top-1 accuracy and 69.6% macro-F1. These results outperform the best comparison model with dataset-retuned FOTD preprocessing by 8.0 and 3.0 points, respectively, demonstrating that learnable, sensor-aware preprocessing is more effective than fixed handcrafted differencing for low-cost MOX gas-sensor recognition.

---


### 108. [MAMA-FLUX.2: Image-to-Image Synthesis of Post-Contrast Breast DCE-MRI for the MAMA-SYNTH Challenge](https://arxiv.org/abs/2608.25648)

**<font color=#1a73e8>作者：</font>** Kamil Kwarciak, Marek Wodzinski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic contrast-enhanced breast MRI is central to cancer diagnosis and monitoring, but requires gadolinium-based contrast agents. In this work, we address pre-to-post contrast breast MRI synthesis for the MAMA-SYNTH challenge. We propose MAMA-FLUX.2, a conditional latent flow-matching approach based on FLUX.2-Klein-4B. The pre-contrast image is encoded as spatial conditioning, while the model predicts the flow field associated with the post-contrast target latent. To adapt the pretrained model efficiently, we use LoRA fine-tuning and introduce a regional training objective combining global flow matching, tumor-region supervision, and stable foreground regularization. We further investigate LoRA rank, intensity windowing, and regional loss weights on axial slices, prioritizing clinically relevant tumor-focused metrics. Our ablation study shows that moderate tumor and stable-foreground weighting improves the trade-off between image fidelity and tumor-region accuracy. The final model achieves the best overall balance with LoRA rank/$\alpha=64/64$, $\mathrm{MHA}_{\max}=25$, $\lambda_{\mathrm{tumor}}=0.25$, and $\lambda_{\mathrm{stable}}=0.1$. These results demonstrate that compact pretrained rectified-flow transformers can be adapted for contrast-enhanced MRI synthesis using parameter-efficient fine-tuning and task-aware regional losses.

---


### 109. [Diffusion Transformers for Roof Graph Synthesis and Reconstruction](https://arxiv.org/abs/2608.25652)

**<font color=#1a73e8>作者：</font>** Daniel Panangian, Ksenia Bittner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present RoofDiT, a generative framework for 2D roof graph synthesis and reconstruction. Roofs are compactly described as planar graphs of junctions and structural edges, but existing methods often rely on fixed geometric rules or direct reconstruction objectives. RoofDiT instead models roof structures directly as vertex-edge graphs and learns a conditional generative prior over their geometry and connectivity. Our framework follows a two-stage design: a diffusion transformer generates roof vertices, and an edge prediction module infers the corresponding graph topology. To improve geometric fidelity, RoofDiT combines relative geometry-aware attention with footprint and aerial-image conditioning, while using an alignment regularizer to encourage common horizontal, vertical, and diagonal roof patterns. The same model supports unconditional generation, footprint-conditioned synthesis, and image-guided reconstruction by changing the conditioning signal. Experiments show improved graph generation quality over a diffusion baseline, favorable performance against a straight-skeleton prior in the footprint-conditioned setting, and the highest edge F1 among compared methods for image-guided reconstruction.

---


### 110. [Unmatched Does Not Mean False: Incomplete Reference Sets Can Reverse Calibration Rankings in Open-Ended Theory-of-Mind Tracking](https://arxiv.org/abs/2608.25654)

**<font color=#1a73e8>作者：</font>** Zhexi Feng, Wuxi Chen, Bingrui Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-ended Theory-of-Mind (ToM) trackers emit valid beliefs absent from finite references. A finite-reference-plus-matcher pipeline marks unmatched outputs false, creating proxy labels that can reverse proper-score model selection on fixed outputs. Holding 259 beliefs and paired scores fixed, reference recoding lowers weighted prevalence from 0.783 to 0.295 and reverses strictly proper Brier risk: a frozen source-prior rule leads native confidence by 0.227 under reference labels and trails by 0.152 under blinded adjudication, in all six authored scenarios. A reference-only Platt recalibrator reverses further. An ICE-specific reversal appears in a released 301-question NQ-open DPR-BERT pipeline: its average-confidence baseline improves instance-level calibration error by 0.045 under exact match but worsens it by 0.074 under human correctness, with both intervals excluding zero. On independently authored OpenToM narratives, 90-96% of audited unmatched beliefs are literally true and the paired direction again reverses. An exact decomposition attributes the distortion to omitted truths, and a closed-form criterion correctly classifies comparisons from twelve released systems. Frozen-audit retrospective replay shows 50 attempted annotations recover ranking direction with probability at least 0.996. TriSource-Restore anchors full-frame reference labels and frozen automatic judgments to a probability-sampled human pilot, maintains at least nominal coverage, narrows intervals, and repairs confidence subject to a base-rate deployment gate.

---


### 111. [AffectSim: A Controllable Interactive 3D Simulation Benchmark for Embodied Affective Perception](https://arxiv.org/abs/2608.25664)

**<font color=#1a73e8>作者：</font>** Ke Xing, Zhilong Wang, Zheng Lian 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Existing affective benchmarks largely consist of fixed recordings whose observation conditions are determined before inference, making it difficult to systematically study how embodied sensing influences affective perception. We introduce AffectSim, a controllable interactive 3D simulation benchmark for embodied affective perception. Rather than treating affective samples as fixed recordings, AffectSim instantiates emotion-expressive human motions as replayable 3D episodes in which distance, orientation, occlusion, scene geometry, and agent viewpoint can be systematically varied while preserving the underlying behavior and emotion label. AffectSim contains 27{,}647 episodes across five emotion categories and 57 scenes. Its factorized design separates affective behavior from observation conditions, supporting controlled re-observation of the same behavior as well as agent-controlled sensing in an executable 3D environment. To demonstrate this capability, we instantiate embodied emotion perception under matched initial (P-Init), reference (P-Ref), and actively acquired (A-Obs) observations. Across 24 frozen perception-model configurations, P-Ref substantially outperforms P-Init, while a simple two-stage active-observation baseline improves 21 of 24 configurations. Mean Macro-F1 increases from 9.89% to 11.70% for open-source models and from 22.61% to 24.26% for closed-source models, recovering 32.0% and 20.1% of their respective P-Ref--P-Init gaps. Episode-level recovery and path-aware evaluation further characterize the current baseline beyond aggregate recognition performance. These results demonstrate the value of making affective observation controllable and establish AffectSim as an initial platform for studying embodied affective perception through interactive 3D simulation.

---


### 112. [An Analysis of the Impact of Psychological Factors and Techniques Across Different Types of Social Engineering](https://arxiv.org/abs/2608.25670)

**<font color=#1a73e8>作者：</font>** Helin Omer, Daniela Pöhn  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing is a well-known social engineering (SE) type used to trick individuals into revealing personal information or performing desired actions, like downloading and installing malware. Other SE types, like vishing and smishing, have emerged and are increasingly being used. As SE continues to successfully persuade victims into actions, the questions arise of which SE attack types are most effective for specific psychological factors (PFs) and, conversely, which PFs are most effective for particular attack types. To answer these questions, we conducted a laboratory study with n=12 participants, in which each participant was shown all 25 stimuli (five PFs and five SE types). The results of this exploratory study show that the most effective SE attack type for authority, trust, and greed was spear-phishing. The most successful combination of PF and attack type was spear-phishing using greed. The least successful combinations were pop-ups using authority, smishing using authority, and vishing using curiosity, each having had no success at all.

---


### 113. [Deep Learning Segmentation of Diffusion-Weighted MRI Acute Ischaemic Stroke: A Pragmatic Evaluation Across Three Datasets](https://arxiv.org/abs/2608.25675)

**<font color=#1a73e8>作者：</font>** Atle Bjørnerud, Till Schellhorn, Thor H. Skattør 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective: Diffusion-weighted MRI (DWI-MRI) is the gold standard for visualizing and quantifying acute ischaemic stroke (AIS). Although deep learning methods can accurately segment AIS lesions, the optimal image inputs and model architecture remain uncertain. We evaluated whether accurate AIS lesion segmentation can be achieved using a pragmatic deep learning approach with minimal preprocessing and clinically feasible inference times.
Materials and Methods: Self-configured nnU-Net models were trained on 1,744 DWI cases from local, national, and open-access datasets and tested on 436 cases. Four experimental conditions were evaluated using five-fold cross-validation: with or without brain extraction and using either DWI alone or DWI plus apparent diffusion coefficient (ADC) images as inputs. Two architectures were compared: the baseline nnU-Net (base) and a residual encoder nnU-Net (ResEnc). Performance was benchmarked against the DeepISLES ensemble model from the 2022 ISLES challenge.
Results: In the test set (n=436), the base model achieved a median (IQR) Dice similarity coefficient (DSC) of 0.84 (0.19). For the base model, only two of six pairwise comparisons between input configurations showed significant differences. ResEnc produced small but significant improvements in DSC compared with the base model for DWI, DWI+brain extraction, and DWI+ADC inputs (all p<0.02), but not for DWI+ADC+brain extraction (p>0.50). The base model significantly outperformed DeepISLES, particularly in patients with smaller infarct volumes (signed-rank test, p<0.01).
Conclusions: A baseline nnU-Net trained on DWI alone, without preprocessing, enabled fast and accurate AIS lesion segmentation. This streamlined approach may facilitate clinical research and support acute stroke imaging workflows

---


### 114. [Adversarial Training of Linear Models under Stealthy Attacks](https://arxiv.org/abs/2608.25681)

**<font color=#1a73e8>作者：</font>** Lovisa Eriksson, Dave Zachariah, André M. H. Teixeira  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive models are widely used in many fields, but are vulnerable to false data injection attacks. To address this, detection schemes and adversarial training have been proposed, but such approaches lack guarantees against stealthy attacks. We therefore propose a detector-based switched model, in which optimal attack strategies are stealthy. For linear prediction models, we derive a convex formulation of the resulting adversarial risk. The model incorporates protected features and introduces a hyperparameter modelling attack probability, enabling an explicit performance trade-off between clean and attacked data regimes. Numerical simulations on real and synthetic data show improved performance on partially attacked data, even for misspecified attack probabilities.

---


### 115. [Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems](https://arxiv.org/abs/2608.25690)

**<font color=#1a73e8>作者：</font>** Roee M. Francos, Daniel Garces, Orhan Eren Akgün 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Sequential decision-making in multi-robot systems typically assumes that planning information is reliable and that agents execute the actions anticipated by the planner. Compromised agents can violate both assumptions, creating a mismatch between the planning model and physical execution. We study this problem in online multi-robot routing under localization spoofing. We introduce a distance-constrained spoofing model for monitor-aware adversaries, together with a tiered bipartite matching strategy that maximizes assignment influence while limiting spoofing magnitude. To mitigate such attacks, we develop a trust-aware monitor that combines probabilistic localization trust, calibrated using real GPS spoofing data, with behavioral evidence from task execution to classify agents and remove detected adversaries from subsequent planning. We further show that undetected adversaries can cause rollout to lose its expected cost-improvement behavior by violating planner-execution consistency. Trust-aware removal restores this consistency after detection, enabling stable routing and recovery of rollout's empirical advantage over the base policy. Experiments using real GPS spoofing datasets and San Francisco taxicab demand demonstrate effective detection and resilient routing across varying spoofing capabilities, adversarial fleet sizes, adaptive attacks, monitoring configurations, and rollout horizons.

---


### 116. [CloSeR: Unified Relational Distillation from Closed-Set Teachers for Category Discovery](https://arxiv.org/abs/2608.25692)

**<font color=#1a73e8>作者：</font>** Yuanpei Liu, Zhenqi He, Jialu Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized Category Discovery (GCD) is an intriguing open-world problem that has garnered increasing attention: given partially labelled data, the goal is to correctly recognize known classes while discovering coherent novel categories from unlabelled samples. Recent GCD methods typically adapt foundation models by jointly optimizing supervised classification and unsupervised discovery objectives on mixed labelled and unlabelled data. While effective, this coupled training can entangle closed-set recognition and open-set discovery, leading to objective conflict and biased predictions, and may disturb the semantic geometry of pretrained representations under limited labels and noisy pseudo-labels. We propose CloSeR, a simple plug-and-play framework that injects Closed-Set Relational knowledge into GCD training. CloSeR first builds a domain-adapted closed-set teacher by tuning lightweight block-wise adapters on labelled known-class data while keeping the foundation model backbone frozen, thereby preserving pretrained priors at low training cost. It then transfers the teacher's knowledge to downstream GCD via Unified Relational Distillation (URD), which distills complementary global sample-to-prototype relations to anchor known-class semantics and local sample-to-sample relations to preserve neighborhood structure, using separate feature pathways to reduce optimization interference. CloSeR is head-agnostic and readily integrates with both parametric and non-parametric GCD methods. Extensive experiments with DINO and DINOv2 backbones on six benchmarks (CIFAR-10/100, ImageNet-100, CUB, Stanford-Cars, and FGVC-Aircraft) show consistent gains over GCD baselines, achieving state-of-the-art performance. Project page: this https URL

---


### 117. [Unsupervised Anatomical Feature Learning via Diffusion Models: Enhanced Medical Image Segmentation with Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2608.25693)

**<font color=#1a73e8>作者：</font>** Akshat G, Divyansh Gupta, Shaleen Bhatnagar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Acquiring pixel-level annotations for medical image segmentation is a severe bottleneck. Traditional U-Net architectures, while effective, learn local texture patterns and lack awareness of global anatomical structures, leading to boundary delineation failures in low-data regimes. This research paper proposes utilizing unsupervised Denoising Diffusion Probabilistic Models (DDPMs) to extract anatomical features. We train a DDPM on 21 unlabeled abdominal CT scans to learn structural representations, transferring the encoder weights to a downstream segmentation task evaluated on the BTCV multi-organ dataset. Diffusion pretraining significantly improved liver segmentation: Dice increased from $0.75\pm0.36$ to $0.93\pm0.16$ ($p < 5.33\times10^{-26}$, 0.529 Cohen's d), Average Surface Distance (ASD) decreased by 66%, and 95th-percentile Hausdorff Distance (HD95) reduced by 45%. For kidney segmentation, Dice improved from $0.90\pm0.19$ to $0.95\pm0.10$ ($p < 4.01\times10^{-11}$). Multi-organ pooled performance showed a 68% variance reduction and a 74% improvement in boundary precision (Dice $0.95\pm0.07$). Crucially, frozen encoder models retained > 80% of fine-tuned performance without exposure to segmentation labels, proving the existence of learned anatomical priors. In low-data scenarios, diffusion-pretrained models maintained robust performance with only 50% (Dice: 0.92 liver, 0.94 kidney), 25%, and even 10% (Dice: 0.89 liver, 0.71 kidney) of labeled data. Using unlabeled images for diffusion-based pretraining successfully embeds robust anatomical features prior to human supervision, transforming U-Nets into anatomy-aware systems.

---


### 118. [Modeling spatio-temporal locality in multi-step forecasting of geo-referenced time series](https://arxiv.org/abs/2608.25698)

**<font color=#1a73e8>作者：</font>** Annunziata D'Aversa, Gianvito Pio, Michelangelo Ceci  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting future measurements from geographically distributed sensors is essential across many domains. However, the spatial distribution of these sensors raises multiple challenges, primarily due to spatial autocorrelation phenomena, that introduce inter-dependencies among nearby locations, that cannot therefore be treated independently. While some existing approaches can capture such phenomena, they generally model the spatial dimension globally across all locations. On the other hand, the method we propose in this paper, called SPALT, focuses on capturing spatial relationships among time series with similar trends, even if they occur at different times, thus modeling the spatio-temporal locality. SPALT leverages linear model trees, which allow us to consider the spatial autocorrelation locally: during the tree-building process, the adopted heuristics group time series exhibiting similar trends into the same node, on which additional features considering the spatial dimension are selectively injected. Additionally, we propose a new pruning strategy, based on Reduced Error Pruning, that also considers the spatio-temporal locality during the tree simplification. Designed for a multi-step setting, SPALT provides forecasts for multiple future time steps across multiple sensors simultaneously. The characteristics exhibited by SPALT can provide significant benefits in different domains, where measurements come from distributed sensors. In this paper, we focus on data produced by sensors located in multiple renewable power plants measuring their energy production at regular, short intervals. Experiments on 3 real-world datasets demonstrate the effectiveness of SPALT in forecasting the production of energy at different time horizons, and its superior performance in comparison with tree-based models and state-of-the-art neural networks that incorporate both temporal and spatial dimensions.

---


### 119. [Tropospheric temperature and humidity profile retrieval from Meteosat Flexible Combined Imager based on deep learning](https://arxiv.org/abs/2608.25700)

**<font color=#1a73e8>作者：</font>** Alejandro Salgueiro, Johannes Rausch, Julie Thérèse Villinger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Meteosat Third Generation (MTG) Flexible Combined Imager (FCI) offers new opportunities for tropospheric temperature and humidity profiling, at higher spatio-temporal resolutions and expanded spectral coverage relative to its predecessor. Vertically resolved retrievals from broadband imagers are inherently challenging, and operational retrieval algorithms typically rely on numerical weather prediction (NWP) background fields to compensate for limited infrared spectral resolution, reducing the retrievals' independence. We develop a spatially aware deep learning framework to retrieve all-sky tropospheric temperature and humidity profiles from FCI, without forecast profiles as input. A Residual U-Net that exploits spatial context across all 16 FCI channels was trained on 14 months of collocated FCI observations and CERRA reanalysis targets over Europe. Validated against independent radiosondes, retrieved temperatures show biases below 0.4 K and standard deviations of 1.5-1.9 K. Retrieved relative humidity standard deviations range from 12-20 %, compared to 9-19 % for CERRA. Performance degrades modestly under clouds, with standard deviation increases below 0.4 K and 3 % RH beneath cloud tops despite limited direct radiative information. Ablation experiments show that spatial context improves retrievals, with the largest gains below cloud tops. Feature sensitivity analysis indicates broad consistency with FCI bands' established radiative transfer characteristics. Visible and near-infrared channels contribute despite not being commonly used in physics-based profile inversions. These results demonstrate that spatially aware deep learning models can extract statistically reliable tropospheric profiles from geostationary imager observations, independent of NWP forecast fields, enabling more rapid autonomous monitoring of the atmosphere.

---


### 120. [Skeleton-based Zero-Shot Spatio-Temporal Action Localization via Weakly-Supervised Pretraining](https://arxiv.org/abs/2608.25701)

**<font color=#1a73e8>作者：</font>** Koshiro Nagano, Fumiaki Sato, Ryo Hachiuma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a novel pretraining strategy for skeleton-based zero-shot spatio-temporal action localization to estimate unseen actions for person instances while overcoming high annotation costs for training via new target actions and pretraining using large-scale action scenery datasets. Specifically, our approach, termed Skeleton-Language feature Pooling Switching, introduces a weakly-supervised vision-language pretraining mechanism. This mechanism transitions pooling kernels from pretraining, which aggregates skeleton features at the video level and aligns them with each video's known action text embeddings, to the inference phase that computes instance-level features without training via target actions. Furthermore, we propose Scene-Mixed Discriminative Contrastive Learning to distinguish actions at the instance level within the combined scene through the MIL framework. Our experiments on four public spatio-temporal action localization and classification datasets demonstrate that the proposed method effectively addresses annotation limitations.

---


### 121. [Difficulty-Aware Sample Allocation for Adaptive Data Augmentation in Semantic Segmentation](https://arxiv.org/abs/2608.25710)

**<font color=#1a73e8>作者：</font>** Olasimbo Ayodeji Arigbabu, Abimbola Ismail Arigbabu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data augmentation is a standard component of modern semantic segmentation pipelines, but most augmentation techniques allocate transformations uniformly across training samples or adapt to a single difficulty signal such as loss. This ignores the fact that segmentation difficulty is multi-factorial, since ambiguous predictions, persistent optimization errors, rare classes, and complex object boundaries can each make a sample informative in different ways. This paper introduces Difficulty-Aware Sample Allocation (DASA), an architecture-agnostic framework that assigns stronger augmentation to samples estimated to be more difficult. DASA combines prediction ambiguity, training loss, class rarity, and boundary complexity into a normalized difficulty score, then maps that score to sample-specific augmentation strength during iterative training. Experiments on Oxford-IIIT Pet and binary Pascal VOC segmentation with U-Net, DeepLabV3, and SegFormer-B0 show that DASA improves over standard training and is competitive with or stronger than single-signal adaptive baselines. On Oxford-IIIT Pet, DASA improves DeepLabV3 from 0.633 to 0.740 mIoU. On binary Pascal VOC, DASA obtains the best foreground IoU for all three evaluated architectures. These results attest to the value of multi-factor difficulty estimation as a practical mechanism for directing augmentation where it is most useful.

---


### 122. [It's a matter of timescale: non-linear utility in successor features and multi-objective planning and learning](https://arxiv.org/abs/2608.25723)

**<font color=#1a73e8>作者：</font>** Liam P.H. Mertens, Lucas N. Alegre, Florent Delgrange 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time is of the essence when dealing with multiple reward signals and non-linear utility. In this paper we argue that the current main approaches in multi-objectiveRL (SER and ESR), and successor features, are insufficient. While each approach deals with non-linear effects on user utility on different timescales, none of them take into account that different effects happening on different timescales can happen within the same decision problem. We motivate that this can indeed be the case by an example, both intuitively and numerically, leading to a new perspective, and a significant and non-trivial gap in the literature.

---


### 123. [MIMONet: Multi-scale Input and Multi-scale Output Network for Salient Object Detection](https://arxiv.org/abs/2608.25733)

**<font color=#1a73e8>作者：</font>** Zhaojian Yao, Wei Gao, Tiesong Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The existing methods for saliency detection task focus on the application of multi-level features, aiming to take advantage of the respective strengths of high- and low-level features. However, because the inputs of these models are single-size images, their multi-level features have difficulty in learning the knowledge of size variations of salient objects. Object-scale variation learning has great potential for detecting multi-scale objects, which has not been fully explored by existing methods. To improve the recognition ability of a model for objects with different sizes, we are inspired by the image pyramid to propose a Multi-scale Input and Multi-scale Output Network (MIMONet). In MIMONet, we extract multi-level features for three images with different resolutions to form three encoder branches, and information will be exchanged between the branches. The advantage of this approach is that the features of one branch can learn the knowledge of target size variation from the features of the other two branches. In addition, we design a Multi-scale Perception (MSP) module, in which the input feature layer is divided into several sub-layers with different resolutions. Capturing the multi-level structure information of the objects in these sub-layers can make the objects more fully perceived. For network training, we propose a Joint Saliency Loss (JSL), which can constrain multiple saliency maps output by the network to identify the same foreground objects, and induce their boundaries to be preserved clearly. Experimental results show that MIMONet has stronger detection capabilities and harvests better evaluation scores on multiple datasets compared to existing models. The code of our model will be released.

---


### 124. [InteractGesture: Progressive Chunk Guidance for Continuous Streaming Co-Speech Gesture Control](https://arxiv.org/abs/2608.25734)

**<font color=#1a73e8>作者：</font>** Ekkasit Pinyoanuntapong, Ajinkya Deogade, Paul Streli 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-speech gesture generation has made significant progress toward realistic full-body motion from speaker audio, yet existing models lack fine-grained spatial controllability of individual joints. To address this, we introduce \emph{InteractGesture}, a model-agnostic, inference-time method for spatially controllable gesture generation. \emph{InteractGesture} guides target latent estimates of a diffusion sampler through a differentiable RVQ-VAE decoder, backpropagating spatial control gradients to adjust motion latents during sampling. A primary challenge in streaming co-speech generation is chunk-wise dependency: standard sequential inference freezes prior chunks, preventing spatial constraints in future chunks from adjusting preceding trajectories and causing boundary inconsistencies. To overcome this limitation, we propose \emph{Progressive Chunk Guidance}, a chunk-window strategy that maintains an active set of editable chunk latents with staggered delays, enabling spatial constraints to propagate gradients backward across chunk boundaries during streaming generation. Experiments on the BEAT2 dataset show that \emph{InteractGesture} improves multi-joint spatial control while preserving overall gesture quality. Furthermore, our approach supports diverse applications, including sparse joint positioning, dense joint trajectory control, and directional pointing. Our project page is available at this https URL .

---


### 125. [Moving Beyond More Views: Redundancy-Aware Ego-Exo Fusion for Proficiency Estimation](https://arxiv.org/abs/2608.25736)

**<font color=#1a73e8>作者：</font>** Xu Dong, Wanqing Li, Anthony Adeyemi-Ejeye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> EgoExo proficiency estimation aims to assess action quality by integrating fine-grained motion cues from egocentric (1st-person) views with spatial context from multiple exocentric (3rd-person) views. Simply adding more exocentric views degrades EgoExo performance, as redundant or noisy perspectives dilute useful motion cues. Our analysis identifies two key causes: (1) Multiview redundancy - From the data perspective, certain views provide limited or noisy information, diluting discriminative cues; (2) Overfitting - From the feature perspective, conventional fusion increases representational complexity, causing the model to memorise view-specific patterns rather than learn generalisable representations. To address these issues, we propose two complementary modules: AdaMVS, which adaptively identifies and fuses the most informative view tokens under weak supervision from the data perspective, and VIB-GB, which combines Gradient Blending and Variational Information Bottleneck regularisation from the feature perspective to compress redundant signals and suppress overfitting during training. Experiments on EgoExo-4D and EgoExo-Fitness demonstrate that our method learns both which view to look at and how to fuse them, achieving new state-of-the-art results. Our source code is available at this https URL

---


### 126. [MeMark: Membrane-Space Watermarking for Spiking Neural Networks](https://arxiv.org/abs/2608.25738)

**<font color=#1a73e8>作者：</font>** Roberto Riaño, Gorka Abad, Stjepan Picek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) are increasingly distributed as pretrained checkpoints and reused as backbones for new tasks. However, current SNN watermarks are mainly verified against the model output. Thus, a user who replaces the output head can keep most of the original network while removing the evidence used for verification. We present MeMark, a watermark designed for the checkpoint-reuse setting. Instead of storing the watermark in the output head, MeMark embeds a multi-bit identifier in the internal membrane state of selected Leaky Integrate-and-Fire (LIF) neurons. A secret input drives each selected neuron to the chosen side of its own firing threshold, and the same threshold is later used to recover the secret bit, so the verifier does not need a learned decoder. We evaluate MeMark across recurrent, convolutional, residual, and transformer SNNs. On a 215.4M-parameter SpikeGPT checkpoint, all 20 independent 64-bit keys pass the fixed 51/64 verification rule, while none of the $30\,000$ fresh random keys pass when tested against all 20 protected checkpoints and the clean model. All 20 genuine keys also remain above the threshold after fine-tuning, 90\% pruning, int8 quantization, and output-head replacement. Under our stated threat model, adaptive attacks can weaken the watermark but do not remove the ownership evidence in the settings we test. Additionally, we study false ownership claims, key-aware and key-agnostic removal, partial key disclosure, rollback, and extraction into a student. The results show that MeMark can provide evidence of checkpoint derivatives, while being resistant to the adversary's attacks and complete head replacement.

---


### 127. [A Constitutive Markov Physics-Informed Neural Operator (MPNO) for Autoregressive Stability in Transient Dynamics](https://arxiv.org/abs/2608.25744)

**<font color=#1a73e8>作者：</font>** Wenpu Du, Peng Zhou, Yunlong Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators applied to transient-dynamics PDEs with strong discontinuities exhibit autoregressive instability: in concrete-penetration stress-field prediction, the wavelet neural operator (WNO) diverges in autoregressive rollout, while MeshGraphNets collapse to zero predictions. WNO's instability stems from the lack of a structural constraint on the spectral radius of its propagation operator; the Fourier neural operator (FNO) is stable in these measurements but only emergently, not by construction. We propose a constitutive Markov physics-informed neural operator (MPNO) modeling one-step evolution as a Markov (row-stochastic) propagation operator. Physics-coupled edge weights (acoustic-impedance harmonic mean, contact area, and traction amplitude) encode material-interface constitutive information into a nonnegative symmetric adjacency matrix W; after normalizing the graph Laplacian L = D - W by lambda_max, the propagator P = I - alpha*L~ is constructively constrained to spectral radius rho(P) <= 1, suppressing exponential amplification of autoregressive errors. Stability is thus a designable architectural property, not an optimized loss objective. On three PDEs (Burgers and two-dimensional transverse-section concrete penetration), MPNO rolls out stably with bounded error on all test seeds at 100/135/165 m/s; the single-step relative L2 error is 0.7304 +/- 0.0008, better than WNO and comparable to FNO at about one quarter of FNO's parameters. The edge-weight formula transfers across scenarios by replacing material-property variables. With about 20K parameters, MPNO delivers roughly 10^5x inference speedup over LS-DYNA.

---


### 128. [Comparing Corrupted Constrained Learning Problems](https://arxiv.org/abs/2608.25745)

**<font color=#1a73e8>作者：</font>** Laura Iacovissi, Rabanus Derr, Robert C. Williamson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A key result in statistics is the data processing inequality, originally proved by Blackwell (1951) and later refined by DeGroot (1962) in terms of statistical uncertainty. It states that the Bayes risk of a statistical experiment obtained by stochastically modifying another experiment cannot be lower than the Bayes risk of the original experiment, regardless of the loss function or prior chosen. In machine learning, this result underlies applications such as the information bottleneck principle and some feature learning techniques. However, machine learning problems are constrained learning problems: the model class used does not include all measurable functions. We present a simple counterexample showing that the classical data processing inequality fails to hold in such a setting. Hence, we formulate a generalized data processing inequality, requiring the constrained Bayes risk of a joint distribution (with respect to a loss function and a constrained hypothesis class) to lower bound the constrained Bayes risk on the stochastically modified distribution, regardless of the choice of distribution. We show this inequality to be equivalent to a set containment condition on a specific function set induced by the loss and model class, called the superprediction set. Finally, we derive sufficient conditions for this containment.

---


### 129. [Toward Interpretable Privacy Guarantees in Face-Swapping Anonymization](https://arxiv.org/abs/2608.25750)

**<font color=#1a73e8>作者：</font>** Vishnu Bondalakunta, Arman Zareian Jahromi, Shuangqing Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Face-swapping has emerged as a promising approach to facial privacy protection, replacing a target individual's appearance with that of a donor while preserving non-facial context. The resulting images visually resemble the donor, and face recognition systems tend to suppress the target's match scores -- ostensibly satisfying privacy requirements. Empirical evaluation across a range of face-swapping models, however, reveals that significant target identity leakage still occurs. This raises a deeper question: why does leakage occur, and can it be predicted? We propose a linear stochastic model that treats face-swappers as transformations on the space of identity embeddings, providing an interpretable account of the leakage mechanism. The model is fit to empirical observations and used to derive testable predictions. The aim is to ground privacy assessments in principled, interpretable analysis, thus making formal privacy guarantees explainable -- and perfectible -- rather than purely observational.

---


### 130. [Learning from waste: Machine Learning for health risk prediction and computer vision-based sorting in Ghana](https://arxiv.org/abs/2608.25759)

**<font color=#1a73e8>作者：</font>** Hilda Adwubi Osei, Catherine Tenewaa Osei, Desdemona Yaa Asobayire  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The inappropriate disposal of solid waste remains a significant public health and environmental concern worldwide, including in Ghana. Poor sanitation and improper waste management practices contribute to substantial economic costs and avoidable deaths annually. In 2022, a field study in Atonsu, Kumasi, Ghana, reported a community-perceived relationship between household waste disposal and illness patterns, but only through descriptive analysis without quantitative validation. This study extends that investigation using two data-driven approaches. First, a Random Forest classifier was developed to predict illness categories using waste disposal practices and demographic survey data. On a held-out group of respondents who reported illness (N=69), the model obtained a macro F1 score of 0.63, with disposal method emerging as the most important substantive predictor of illness type. Second, a MobileNetV2 image classification model enabled automated waste sorting via visual recognition, achieving 88.2% accuracy and a macro F1 score of 0.87 on the test set (N=415). The vision-based approach offers an affordable, camera-driven alternative to complex multi-sensor systems, making it highly suitable for resource-constrained settings. Taken together, the findings provide quantitative evidence for a community health relationship previously documented only qualitatively. They demonstrate the potential for automated waste-sorting in low-resource environments. Importantly, the results illustrate that technological performance alone does not guarantee public health improvements; effective institutional support and implementation are equally necessary.

---


### 131. [Cooperative Multi-Agent Reinforcement Learning for Adaptive Aggregation in Semi-Supervised Federated Learning with non-IID Data](https://arxiv.org/abs/2608.25794)

**<font color=#1a73e8>作者：</font>** Rene Glitza, Luca Becker, Rainer Martin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables distributed training of machine learning models while preserving data privacy. However, FL struggles with heterogeneous, non-IID client data distributions, resulting in sub-optimal and biased global models. In this paper, we propose pFedMARL, a novel approach leveraging Multi-Agent Reinforcement Learning (MARL) with Twin Delayed Deep Deterministic Policy Gradient (TD3) to dynamically adapt aggregation strategies in FL settings. Our method employs a server-side agent adjusting client contributions to optimize global model robustness and client-side agents balancing global and local updates to personalize models effectively without pre-training. We demonstrate superior performance of pFedMARL for training a semi-supervised audio spectrogram transformer, matching or outperforming FedAvg, Ditto, and local training approaches across multiple non-IID scenarios and in the presence of adversarial clients. Our results indicate that pFedMARL actively improves accuracy, robustness, and fairness, making it suitable for real-world deployments.

---


### 132. [Geometry-Constrained Kolmogorov-Arnold Networks: Learning Edge Geometry via Banach Duality](https://arxiv.org/abs/2608.25807)

**<font color=#1a73e8>作者：</font>** K S Sesh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold Networks (KANs) replace fixed activations in deep architectures with learnable univariate edge functions, making the choice of edge parametrisation central. Existing variants rely on fixed bases such as splines, polynomials, or Fourier features, which impose a function-space geometry before data are observed. We introduce geometry-constrained KANs, a family of edge activations derived from Banach duality maps in which the geometry itself is learned through a scalar exponent $p > 1$ per edge. This exponent controls the qualitative response: sub-Euclidean values produce sharp, threshold-like behaviour reminiscent of the $\ell_1$ (LASSO) geometry, $p = 2$ recovers the linear regime, and larger values produce flatter responses near the origin. Across 50 symbolic-regression targets ($40$ from the AI Feynman benchmark plus $10$ synthetic stress tests), geometry-constrained KANs match or beat every fixed-basis baseline on median NRMSE (Banach-KAN $0.030$, tying Chebyshev and improving on splines); on average rank Banach-KAN is best on the $18$-equation core ($2.00$) and statistically tied with the strongest spline on the full benchmark ($2.32$ vs. $2.34$). The clearest gains appear under measurement noise: as $\sigma$ grows from $0$ to $1$, $\ell^p$-KAN degrades only $3.7\times$ -- below even a cross-validated spline ($\approx 11\times$) -- while an unregularised spline degrades $21.6\times$; Banach-KAN degrades $8.8\times$, comparable to a tuned spline but far more stable than the unregularised one. Banach-KAN also takes the most per-equation wins in the small-sample regime, with fixed-basis models catching up only as the training set grows. Learned exponents provide an interpretable, relative signal: at a fixed initialisation they reveal a consistent, target-dependent geometric ordering across equation families and input dimensions.

---


### 133. [TDFNet: Tri-projection Deformable Fusion Network for Panoramic Salient Object Detection](https://arxiv.org/abs/2608.25808)

**<font color=#1a73e8>作者：</font>** Qiangqiang Zhou, Jiacong Yu, Jiawei Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed the growing potential of panoramic salient object detection in robotic vision, virtual reality, and related applications. However, projecting spherical scenes onto 2D planes inevitably introduces geometric distortions, which fundamentally limit the effectiveness of existing projection-based methods. Specifically, Equirectangular Projection (ERP) suffers from severe polar stretching distortions, while cube map projection introduces discontinuities across cube-face boundaries, resulting in degraded feature discriminability and compromised geometric consistency. To address these limitations, we propose TDFNet, the first Tri-projection Deformable Fusion Network for panoramic salient object detection, exploiting complementary projection representations to alleviate geometric distortions and improve detection this http URL, we design a cross-projection deformable attention (CDA) module that leverages spatial correspondences between different projections to construct geometry-aware sampling locations, guiding deformable attention for cross-projection contextual aggregation and enhancing robustness against projection-induced deformations. Furthermore, we introduce a latitude-guided fusion module, which utilizes spherical latitude priors to construct geometric confidence weights for adaptively balancing ERP and CMP features. Meanwhile, LGF incorporates distortion-reduced semantic references from Tangent Projection to achieve cross-projection feature refinement and spatial this http URL constructing a three-branch encoding architecture based on ERP, CMP, and Tangent Projection, TDFNet simultaneously preserves global spatial continuity, local geometric details, and fine-grained boundary information.

---


### 134. [Canalization Before Generalization: Grokking as a Dynamical Probe](https://arxiv.org/abs/2608.25813)

**<font color=#1a73e8>作者：</font>** Yiming Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For overparameterized neural networks, many solutions can fit the training data equally well while behaving very differently on unseen samples. Grokking separates training fit from visible generalization, providing a window for studying how this selection develops during training. We sweep short, fixed-duration weight-decay (WD) pulses across this plateau and measure how they shift later generalization time. Across three grokking tasks, these shifts are unordered early in the plateau but later form a stable dose ordering, with stronger WD increases leading to earlier generalization and stronger WD decreases leading to later generalization. This ordering emerges before visible generalization in all three tasks. Meanwhile, test-loss barriers between perturbed and baseline generalization checkpoints collapse toward zero while the ordered timing effects persist. We call this combination of increasingly constrained solution selection and persistent dose-ordered timing sensitivity the canalization of function selection.

---


### 135. [Steer the Sampling, Not the Kernel Grid: Geometry-Guided Sampling Operator for Volumetric Segmentation](https://arxiv.org/abs/2608.25819)

**<font color=#1a73e8>作者：</font>** Sizhe Wang, Himashi Peiris, Zhaolin Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D segmentation is central to quantitative lesion assessment and anatomy mapping for clinical planning and follow-up. Thin, elongated, and fine anatomical/pathological structures (e.g., vessels) are a particularly challenging case: a one-voxel boundary error can disconnect a branch and change clinically relevant topology. In encoder-decoder networks (e.g., U-Net), repeated downsampling and fixed-grid convolution blur or alias fine structures and weaken orientation cues, so early mistakes propagate across scales. We propose a geometry-guided local operator that steers where features are sampled, rather than deforming convolutional kernels, under a single formulation for both feature refinement (stride 1) and resolution reduction (stride > 1). At each voxel, it predicts a local orientation and bounded step sizes, samples symmetrically along these directions, and transforms paired samples into compact geometric and boundary cues with lightweight mixing; a cross-scale consensus aligns encoder and decoder features at skip connections to reduce geometric mismatch. Replacing all stride 1 and stride 2 operators in a 3D U-Net yields consistent improvements on BraTS, MSD Hepatic Vessel, and TDSC-ABUS, with notably better boundary metrics (e.g., BraTS Dice 86.1 to 88.9, HD95 7.1 to 6.2; TDSC-ABUS HD95 39.1 to 27.8) while reducing parameters from 2.3M to 0.8M. We further demonstrate that the operator can be integrated into other backbones (e.g., nnU-Net, Swin-UNETR, and MedNeXt) without changing their macro-architectures while providing consistent performance gains.

---


### 136. [Learning Continuous Regional Temperature Fields with Lead-Time and Resolution Queries](https://arxiv.org/abs/2608.25823)

**<font color=#1a73e8>作者：</font>** Chunlei Shi, Jiong Wang, Yi-Lin Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate regional near-surface temperature forecasting is fundamental to short-range weather services and downstream risk assessment. Existing deep learning-based regional forecasters commonly produce a fixed set of future frames on a prescribed grid, limiting their use when forecast products must be evaluated at query-dependent lead times or display resolutions. To overcome these fixed-output constraints, we formulate regional T2M forecasting as query-conditioned continuous spatiotemporal temperature field evaluation and propose the Continuous Spatiotemporal Temperature Forecaster (CSTF), a neural field that turns forecast lead time and output resolution into explicit queries when evaluating 2-m temperature (T2M). Specifically, CSTF first encodes multivariable ERA5 histories into latent meteorological states and then decodes T2M as a coordinate-based field. Accordingly, spatial location, forecast lead time, and output resolution are introduced as queries, enabling standard hourly forecasts, intermediate lead-time diagnostics, and resolution-controllable outputs within a unified field-evaluation framework. Furthermore, to maintain coherence across flexible field queries, we design spatial-gradient, temporal-difference, and scale-consistency objectives that regularize regional thermal structures, lead-wise evolution, and cross-resolution agreement. Experiments on the Southeast China 0-6 h ERA5-Land benchmark demonstrate that CSTF achieves the best aggregate deterministic skill, including a 17.0 percent reduction in Bias, with global-scope diagnostics further illustrating flexible lead-time and resolution-controllable inference.

---


### 137. [Unfolding Scientific Papers into Multi-Turn Generation Trajectories for Continued Pre-Training](https://arxiv.org/abs/2608.25826)

**<font color=#1a73e8>作者：</font>** Qiankai Xu, Qiguang Chen, Zixin Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A recent line of synthetic-data work reconstructs the thinking behind existing text rather than rewriting the text itself, but it operates on short web passages, recovers only local thoughts, and leaves the structure of whole documents untouched. Scientific papers are written to a clear and largely uniform structure and make a natural substrate for lifting this paradigm to the document level. We present a pipeline that unfolds each paper into a multi-turn generation trajectory in which a teacher model reconstructs the writing process of the whole paper: a writing request, a global plan, and pre-writing deliberation for each section. All section texts and the abstract are kept verbatim from the source paper. We apply the pipeline to quality-filtered arXiv papers and obtain a corpus for continued pre-training (CPT) that is roughly twice the size of the source text. The same reverse construction extends to instruction data and evaluation. Treating real paper text as the answer yields an SFT dataset. Anchoring tasks in held-out papers yields PAW-Bench, an academic-writing benchmark whose tasks carry their own rubrics and checklists. In controlled experiments CPT on our corpus followed by supervised fine-tuning on public datasets improves writing benchmarks broadly while preserving general reasoning and improving long-document reading. The writing gain persists even when every model is fine-tuned on a dedicated writing SFT dataset. Mixing our SFT data into that recipe lifts academic writing further.

---


### 138. [FlowMoDL: Model-Based Deep Learning with Conjugate-Gradient Data Consistency for Highly Accelerated 4D Flow MRI Reconstruction](https://arxiv.org/abs/2608.25828)

**<font color=#1a73e8>作者：</font>** Tristan Gottwald, Michelle Bruch, Mubashir-Ul Hassan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FlowMoDL, an unrolled neural network for highly accelerated 4D flow MRI reconstruction that directly optimizes for both anatomical magnitude and phase-derived velocity accuracy. Building on the MoDL framework, FlowMoDL alternates a learned (3+1)D spatiotemporal denoiser with conjugate-gradient data-consistency updates based on the SENSE forward model. A novel dual-pathway conditioning scheme adapts the denoiser features and data-consistency weighting, enabling a single model to handle varying acceleration factors ($10\times$ to $50\times$). To ensure physiological accuracy, the network is trained using a deep-supervision composite loss that explicitly penalizes velocity magnitude and angular errors, stabilized by a curriculum schedule. We evaluate FlowMoDL on the multi-center CMRx4DFlow dataset against classical and deep-learning baselines (CG-SENSE, MoDL, FlowVN, and FlowMRI-Net). A key advantage of FlowMoDL is its superior gradient step efficiency. When evaluated under an equivalent, limited budget of gradient steps, competing flow-specific networks degrade significantly. In contrast, FlowMoDL robustly converges and strictly outperforms all competitors across all acceleration factors in magnitude SSIM, nRMSE, relative velocity error, and angular error, successfully recovering sharp structural details and temporally coherent velocity fields.

---


### 139. [Socialized Detector Learning: Trajectory-Guided and Reciprocal Distillation for Heterogeneous Object Detectors](https://arxiv.org/abs/2608.25836)

**<font color=#1a73e8>作者：</font>** Weihao Li, Yunqi Zhu, Zhihe Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection knowledge is fragmented across independently trained, heterogeneous detectors with complementary category supports. In socialized learning, this knowledge resides in a society, and learning aims to evolve the society collectively through exchange. However, aggregation-based socialization does not explicitly plan transfer order, whereas progressive multi-teacher distillation considers order but remains a one-way student enhancement in a shared category space. Building on Socialized Learning, we formulate Socialized Detector Learning (SDL) for heterogeneous, category-specialized object detectors and propose Trajectory-Guided and Reciprocal Distillation (TGRD).TGRD estimates directed operational Inter-Detector Transfer Difficulty (IDTD) from held-out feature-alignment residuals, precomputes a fixed score table, and greedily constructs a carrier trajectory. Along the trajectory, knowledge is progressively consolidated into a union-category carrier and then returned to experts through reciprocal transfer. A conditional proxy-certificate analysis shows that, under stated assumptions, the progressive certificate is no larger than an aggregated-target counterpart. On MS COCO with four heterogeneous experts and two carrier initializations, final carriers outperform epoch-matched simultaneous aggregation controls by 2.6 AP in both settings. Reciprocal detectors attain 20.8--28.4 AP on previously unsupported categories while remaining within 1.3 AP of original expert-specific performance. These results support order-aware progressive consolidation followed by reciprocal transfer as a viable mechanism for detector-society evolution.

---


### 140. [VINCENT: Validated Interaction Network for Cross-drug Explanation of Therapeutics](https://arxiv.org/abs/2608.25841)

**<font color=#1a73e8>作者：</font>** Fan-Sheng Chuang, Xuchen Li, Yujing Bian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug synergy prediction estimates whether two drugs produce a stronger joint effect than expected from their individual activities. For drug combination discovery, a single synergy score is often not enough: researchers also need to know which molecular regions jointly drive the prediction. We study motif-pair synergy explanation, which identifies pairs of chemically coherent regions, one from each drug, that jointly contribute to predicted synergy. Existing interpretable synergy models expose atom- or substructure-level signals, but their explanations are built into the predictor architecture, and none validates cross-drug region scores under repeated perturbations or feeds that evidence back to refine the explanation. A reliable motif-pair explanation should instead be chemically coherent, perturbation-stable, and aligned with predictor behavior. We introduce VINCENT (Validated Interaction Network for Cross-drug Explanation of Therapeutics), a post-training framework for a fixed interaction-aware synergy predictor. VINCENT extracts atom-pair evidence from attention and gradient signals, groups atoms into chemically coherent motifs, and validates candidate motif pairs through repeated local perturbations. The validated evidence is fed back to refine motif assignments, yielding explanations that satisfy these three criteria. On a 25-pair literature-annotated subset, VINCENT achieves a mean motif recall of 0.826 (95% CI: 0.78-0.87), compared with 0.49-0.66 for baselines. Across all 71 test pairs, its validated interaction scores yield a TP/TN separation of 3.36. These results show that closed-loop perturbation validation recovers literature-supported molecular regions more accurately than existing alternatives while producing cross-drug interaction scores that better reflect predictor behavior.

---


### 141. [DEFUSE: Generalizable Backdoor Defense for Self-Supervised Encoders with Generative Priors](https://arxiv.org/abs/2608.25851)

**<font color=#1a73e8>作者：</font>** Tuo Chen, Jie Gui, Minjing Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) encoders are vulnerable to backdoor attacks, posing threats to both visual SSL encoders and vision-language encoders. Existing defenses are typically designed for only one of these paradigms and rely on restrictive assumptions such as access to uninfected in-distribution data or precomputed pseudo-labels, which are difficult to satisfy in practice. To address these limitations, we propose DEFUSE, a generalizable backdoor detection framework for SSL encoders. Inspired by Bayesian posterior inference, we reformulate backdoor detection as a representation-conditioned image likelihood estimation problem parameterized by a conditional diffusion generative model. Uninfected representations tend to yield semantically consistent reconstructions, whereas backdoored ones are more likely to be mapped to the attacker's target class or semantically meaningless images, deviating from the original semantics and thereby exposing the backdoor. However, we find that the exact likelihood is intractable, because highly abstracted representations discard the low-level information necessary for pixel-faithful reconstruction. We therefore relax the objective to semantic reconstruction and evaluate it in a well-separated representation space provided by a reference encoder. Rather than training from scratch, we fine-tune a pretrained diffusion model, leveraging its generative prior to map data onto the natural image manifold while preserving semantic content. Extensive experiments demonstrate that DEFUSE substantially outperforms existing detectors across diverse attack settings, generalizing to both visual SSL and vision-language encoders. Notably, our method greatly reduces the reliance on prior knowledge about the victim encoder or the attack strategy. The source code is available at this https URL .

---


### 142. [Learning Late, Guiding Early: Timestep-Decoupled Semantic Guidance for Fair Face Generation](https://arxiv.org/abs/2608.25862)

**<font color=#1a73e8>作者：</font>** Subir Kumar Parida, Rajbabu Velmurugan, Ketan Kotwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Demographic imbalance in synthetic face generation can propagate to downstream face recognition systems, making fairness an important consideration when diffusion models are used for data generation. Existing fairness-aware generation approaches often require model retraining, architectural modifications, or repeated guidance throughout the reverse diffusion process. In this work, we introduce Semantic Boundary Predictor (SBP), an inference-time framework that performs demographic guidance through a one-shot intervention during reverse denoising. Our approach is motivated by the observation that latent representations at different diffusion timesteps play distinct semantic roles: late-stage latents provide stronger demographic separability, whereas early-stage latents offer greater flexibility for semantic intervention. SBP leverages this timestep decoupling by learning linear semantic boundaries from late-stage latent representations while applying them only once at the initial noisy latent, allowing the remainder of the reverse denoising process to proceed unchanged. The method requires neither retraining nor fine-tuning of the underlying Latent Diffusion Model and operates without external balanced datasets. Experiments on CelebA-HQ demonstrate substantial improvements in demographic fairness, reducing fairness disparity by 98% for gender, 95% for binary race, and 15% for four-class race, while maintaining perceptual image quality across demographic groups. Owing to its one-shot inference strategy and model-agnostic design, SBP introduces only a small computational overhead and can be readily integrated with existing pre-trained latent diffusion models.

---


### 143. [How Edge of Stability Hinders SCAFFOLD in Federated Optimization](https://arxiv.org/abs/2608.25873)

**<font color=#1a73e8>作者：</font>** Anant Khandelwal, Michael Crawshaw, Mingrui Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In federated learning, it is well known that heterogeneous data can (in theory) slow down optimization, and much effort has been directed at designing optimization algorithms that are unaffected by data heterogeneity, such as the SCAFFOLD algorithm. Yet, despite strong theoretical guarantees, SCAFFOLD does not usually outperform the much simpler FedAvg in practice. In this work, we propose that this gap is due to the presence of Edge of Stability (EoS) and progressive sharpening in federated optimization, supported by extensive empirical probing. First, we find that EoS-like dynamics occur with both FedAvg and SCAFFOLD under a variety of architectures and hyperparameters. We observe that the equilibrium value of the sharpness is inversely proportional to the learning rate (as in GD), and interestingly, the degree of data heterogeneity (but not the number of local steps) also affects the equilibrium value. Most importantly, we observe that SCAFFOLD's ability to estimate the gradient of the global objective is severely degraded at the EoS, as measured by the correlation between sharpness and SCAFFOLD's error in estimating the global gradient along the optimization trajectory. This suggests a mechanism for SCAFFOLD's lackluster performance in deep learning: with high sharpness at the EoS, SCAFFOLD cannot reliably estimate the global gradient.

---


### 144. [A Hybrid Security Framework for Mini-Programs: Visual UI Compliance and Network Risk Assessment](https://arxiv.org/abs/2608.25877)

**<font color=#1a73e8>作者：</font>** Panpan Shen, Lei Xie, Xiaoqi Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the continuous development of the WeChat ecosystem, WeChat Mini Programs, due to their advantages of not requiring installation, using little memory, and being ready to use instantly, have seen a surge in user numbers and have now become an indispensable service carrier in mobile internet. However, as Mini Programs rapidly became popular, issues regarding the compliance of their interface interaction design and the safety of operational behavior have become increasingly apparent. Many Mini Programs have problems such as clickable buttons and icons not being standard in size, or ad pop-ups and payment entrances being placed in a way that is easy to misclick. The close or cancel buttons are often too small or hidden, making it easy to accidentally click on ads or payment content, and difficult to accurately click the cancel button. This can result in involuntary payments or being redirected to illegal pages, causing unnecessary financial losses and seriously harming users' property security and legal rights. To address the above issues, this article develops a detection program to check the position and size of various icons and buttons in Mini Programs, and analyze whether redirected links fall within a safe range. YOLOv8 is used to identify various buttons in images, displaying the corresponding icon and its data based on the mouse click position. Violations are flagged and recorded. At the same time, mitmproxy is used to capture relevant data requests generated during clicks, analyzing the safety of redirections, and presenting key information for user observation.

---


### 145. [Loss-Based Active Learning for Neural Abstractive Summarization](https://arxiv.org/abs/2608.25881)

**<font color=#1a73e8>作者：</font>** Michail Ioannou, Tatiana Passali, George Michalopoulos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning abstractive summarization models requires high-quality annotated data. However, obtaining such corpora is expensive and time-consuming, as it requires human annotators to read and comprehend long documents to create accurate summaries. Active learning mitigates this issue by selecting only the most informative instances for annotation, allowing models to achieve competitive results with significantly fewer labels. However, the application of active learning to summarization remains under-explored, and existing studies often suffer from instability and significant computational bottlenecks. To overcome these challenges, we propose LOBSTER (LOss-BaSed acTivE leaRning), a novel active learning framework designed specifically for abstractive summarization. LOBSTER improves performance by prioritizing unlabeled instances semantically similar to the model's current high-loss training examples, enabling the model to explicitly correct its specific weaknesses. Our empirical evaluation across three benchmark datasets and two summarization backbone models demonstrates that LOBSTER consistently matches or outperforms current state-of-the-art approaches while achieving a query selection speedup of up to 665x.

---


### 146. [Embedding NDRE Trajectories into Contrastive Learning for Label-Free, Physiology-Aware Crop-Stress Staging and DSS Outputs](https://arxiv.org/abs/2608.25888)

**<font color=#1a73e8>作者：</font>** Shafqaat Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Timely detection of crop stress is critical for sustaining yields under increasing drought frequency, yet conventional vegetation index thresholds or image-based clustering often fail to capture stress progression, limiting their value for farm decision-making. To address this gap, we present EigenCL, a physiology-guided contrastive learning framework that stages crop stress from Sentinel-2 NDRE trajectories, with the goal of providing interpretable and transferable stress diagnostics for decision support systems (DSS). EigenCL was trained on 10,000 maize NDRE patches from drought-affected Iowa fields in 2020 and tested on Nebraska fields in 2023 without retraining, with validation incorporating soil-moisture records, U.S. Drought Monitor maps, and county-level yield statistics. The model produced four physiologically coherent stress clusters (Healthy, Mild, Moderate, Severe), significantly outperforming baselines including K-Means, SimCLR, ProtoCLR, and an ablation model (Silhouette = 0.748, DBI = 0.35, CHI = 49,624). Clusters aligned with maize growth stages, with severe stress peaking around tasseling-silking (VT-R1), a stage known to drive yield loss; moreover, EigenCL clusters correlated with soil moisture at 0-14-day lags (rho up to 0.72) and matched yield anomalies in drought-affected counties. By embedding NDRE trajectory dynamics into contrastive learning, EigenCL enables early stress alerts and interpretable DSS outputs (e.g., heatmaps, scouting priorities, regional risk indices), extending beyond single-date NDRE thresholds and supporting scalable monitoring for climate-smart agronomy.

---


### 147. [Towards A Unified Information Bottleneck Framework for Time Series Explanations](https://arxiv.org/abs/2608.25897)

**<font color=#1a73e8>作者：</font>** Xu Zheng, Zichuan Liu, Zhuomin Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explaining deep learning models operating on time series data is crucial in various applications that require transparent and interpretable insights into model behavior. {Existing explanation methods generally fall into two categories: attribution-based explanations, which identify the temporal regions most responsible for a prediction, and counterfactual explanations, which reveal how an input should be modified to alter the model's decision.} {Despite valuable insights, these two fields are largely studied independently. This disconnect leaves attribution methods lacking causal validation, while counterfactual methods suffer from severe instability, producing adversarial-like noise instead of meaningful explanations.} In this work, we revisit time-series explainability from an information-theoretic perspective and show that existing explainers are vulnerable to trivial solutions and distributional shifts. To address these limitations, we propose a unified objective function for explainable time series learning that bridges attribution and counterfactual reasoning within a single framework. Building upon the Information Bottleneck principle, our formulation explicitly prevents trivial explanations and out-of-distribution counterfactuals. {Based on this objective function, we introduce {\modelname}, a novel explanation framework that learns a parametric transformation network to construct explanation-embedded instances, where preserved information yields attribution explanations and controlled information removal produces stable counterfactual explanations.} We evaluate {\modelname} on synthetic and real-world benchmarks against state-of-the-art baselines. Extensive quantitative and qualitative results show that {\modelname} consistently outperforms competing methods, yielding faithful attributions and stable counterfactual explanations.

---


### 148. [Forecasting Multiple Observables with SCROLL: Score-Trained Uncertainty for Stochastic Dynamics](https://arxiv.org/abs/2608.25898)

**<font color=#1a73e8>作者：</font>** Pavel Prochazka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting a stochastic dynamical system rarely means a single number: one wants several observables---future state, threshold event, regime label---each with its own likelihood. Standard multi-task recipes balance per-task losses, tuned or learned. We instead compose the observables' likelihoods in per-task free-routed last-layer beliefs on a shared backbone; this absorbs unit-dependent loss scaling into likelihood parameters learned in the same gradient pass. Stochastic dynamics supply what static benchmarks cannot: computable ground truth for the predictive variance. Results land where theory puts them: on the well-specified, homoscedastic Ornstein--Uhlenbeck process the learned predictive law recovers the analytic kernel and correctly specified baselines tie. On heteroscedastic systems (stochastic Lorenz-63, real air-quality data) the belief's input-dependent variance separates: best single-run NLL on the state and regime tasks, calibration matched only by arms whose NLL it beats, at a fraction of the tuned grids' cost. On the real series the state margin holds across five rolling origins.

---


### 149. [Quantum-Inspired Modeling of Driving Behavior](https://arxiv.org/abs/2608.25907)

**<font color=#1a73e8>作者：</font>** Mohammad Elayan, Omid Armantalab, Wissam Kontar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Driver behavior is heterogeneous, context-dependent, and changes over time, and these properties shape the traffic phenomena we observe. Most models, however, fix in advance which behavioral variables interact and how. Behavior outside that form is absorbed as noise, while models flexible enough to capture it tend to lose interpretability. We introduce a quantum-inspired representation of driver behavior that combines properties usually treated separately or in part: it is continuous, probabilistic, context-dependent, history-dependent, and represents interactions among behavioral variables as learned from data. Each driver is encoded as an evolving density matrix, providing a unified representation of behavioral uncertainty, temporal evolution, and context-dependent behavioral variation. Trained without supervision on the I-24 MOTION dataset, the framework recovers three interpretable driving profiles representing three regimes: free flow, transition, and congestion. The profiles capture the behavioral range of the data and the smooth transitions drivers make between regimes as conditions change. The same representation also reproduces known macroscopic phenomena, aligning with the fundamental diagram and reproducing hysteresis loops. We also show how the representation supports practical use: it supplies context-dependent parameters to classical car-following models, and gives an autonomous vehicle a live behavioral read of the surrounding drivers with a short-horizon forecast of their motion. The framework points toward models of traffic that are interpretable and trustworthy by construction. We release an open-source toolkit on GitHub (this https URL) spanning data processing, training, inference, and analysis.

---


### 150. [SAMpLE: A SystemC-AMS Machine LEarning-based Framework for Virtual Prototyping](https://arxiv.org/abs/2608.25910)

**<font color=#1a73e8>作者：</font>** Andrei Mihai Albu, Sara Vinco  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine Learning (ML) is increasingly used in virtual prototypes of embedded systems to model behaviors that are difficult to capture analytically. However, integrating ML models into virtual platform simulation is still typically done through ad hoc solutions, which limits reuse, comparability, and reproducibility. This paper presents \textbf{\textit{SAMpLE}}, an open-source SystemC-AMS-based framework that integrates ML models as first-class Timed Dataflow (TDF) components through a standardized plug-and-play interface. SAMpLE provides two execution backends: a native C++ backend for online training of lightweight models, and an offline backend for executing externally developed models without requiring re-implementation in C++ or manual integration steps. The framework uses ONNX as a standard model exchange format to enable integration of externally trained ML models into SystemC-AMS simulations, and allows the evaluation of different ML-based solutions within the same testbench, dataset, and simulation workflow. The modular design and unified and reproducible environment will allow future extensions of SAMpLE to new models, without modifying the SystemC-AMS structure.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-171](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
