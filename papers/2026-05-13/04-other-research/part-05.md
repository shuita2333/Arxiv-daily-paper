# 📦 其他研究 | 2026年05月13日

> 本类共 **396** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-396](./part-08.md)

---

### 201. [Deanonymizable Scoped Linkable Ring Signatures](https://arxiv.org/abs/2605.11715)

**<font color=#1a73e8>作者：</font>** Montassar Naghmouchi, Maryline Laurent  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Although ring signatures offer highly desirable privacy requirements like anonymity and ad-hoc group formation with signer autonomy, they partially lack trust requirements like linkability and accountability that are required for strict use-cases, such as consent management in healthcare. Existing signature schemes fail to natively integrate scoped linkability with decentralized accountability (on-demand deanonymization) in a single scheme without relying on separate commitments or a centralized opener. We therefore introduce Deanonymizable Scoped Linkable Ring Signatures (DSLRS). The originality of the DSLRS is manifold. DSLRS uses scopes (context identifiers) and dynamic key images to provide scoped linkability and unlinkability across different scopes. Decentralized accountability is provided thanks to two ELGamal components deeply embedded in the signature, and a decentralized deanonymization network of k-of-N nodes that can collaboratively extract the signer's public key. DSLRS scheme is defined and proved under the ECDLP and DDH hardness assumptions in the Random Oracle Model (ROM). Formal security definitions and formal reduction proofs are provided before introducing a blockchain-based instantiation for a consent management application using DSLRS.

---


### 202. [EPIC: Efficient Predicate-Guided Inference-Time Control for Compositional Text-to-Image Generation](https://arxiv.org/abs/2605.11722)

**<font color=#1a73e8>作者：</font>** Sunung Mun, Sunghyun Cho, Jungseul Ok  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-image (T2I) generators can synthesize realistic images, but still struggle with compositional prompts involving multiple objects, counts, attributes, and relations. We introduce EPIC (Efficient Predicate-Guided Inference-Time Control), a training-free inference-time refinement framework for compositional T2I generation. EPIC casts refinement as predicate-guided search: it parses the original prompt once into a fixed visual program of object variables and typed predicates, covering checkable conditions such as object presence, counts, attributes, and relations. Each generated or edited image is verified against this program using visual evidence extracted from that image. An image is judged to satisfy the prompt only when all predicates are satisfied; otherwise, failed predicates decide the next step, routing local failures to targeted editing and global failures to resampling while the fixed visual program remains unchanged. On GenEval2, EPIC improves prompt-level accuracy from 34.16% for single-pass generation with the base generator to 71.46%. Under the same generator/editor setting and maximum image-model execution budget, EPIC outperforms the strongest prior refinement baseline by 19.23 points while reducing realized cost by 31% in image-model executions, 72% in MLLM calls, and 81% in MLLM tokens per prompt.

---


### 203. [CaC: Advancing Video Reward Models via Hierarchical Spatiotemporal Concentrating](https://arxiv.org/abs/2605.11723)

**<font color=#1a73e8>作者：</font>** Jiyuan Wang, Huan Ouyang, Jiuzhou Lin 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose Concentrate and Concentrate (CaC), a coarse-to-fine anomaly reward model based on Vision-Language Models. During inference, it first conducts a global temporal scan to anchor anomalous time windows, then performs fine-grained spatial grounding within the localized interval, and finally derives robust judgments via structured spatiotemporal Chain-of-Thought reasoning. To equip the model with these capabilities, we construct the first large-scale generated video anomaly dataset with per-frame bounding-box annotations, temporal anomaly windows, and fine-grained attribution labels. Building on this dataset, we design a three-stage progressive training paradigm. The model initially learns spatial and temporal anchoring through single- and multi-frame supervised fine-tuning, and then is optimized by a reinforcement learning strategy based on two-turn Group Relative Policy Optimization (GRPO). Beyond conventional accuracy rewards, we introduce Temporal and Spatial IoU rewards to supervise the intermediate localization process, effectively guiding the model toward more grounded and interpretable spatiotemporal reasoning. Extensive experiments demonstrate that CaC can stably concentrate on subtle anomalies, achieving a 25.7% accuracy improvement on fine-grained anomaly benchmarks and, when used as a reward signal, CaC reduces generated-video anomalies by 11.7% while improving overall video quality.

---


### 204. [Online Continual Learning with Dynamic Label Hierarchies](https://arxiv.org/abs/2605.11742)

**<font color=#1a73e8>作者：</font>** Xinrui Wang, Shao-Yuan Li, Bartłomiej Twardowski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online Continual Learning (OCL) aims to learn from endless non\text{-}stationary data streams, yet most existing methods assume a flat label space and overlook the hierarchical organization of real\text{-}world concepts that evolves both horizontally (sibling classes) and vertically (coarse or fine categories). To better reflect this context, we introduce a new problem setting, DHOCL (Online Continual Learning from Dynamic Hierarchies), where taxonomies evolve across granularities and each sample provides supervision at a single hierarchical level. In this setting, we find two fundamental issues: (i) partial supervision under mixed granularities provides only point-wise signals over an evolving path-wise hierarchy, which constrains plasticity and undermines cross-level semantic consistency, and (ii) the dynamically evolving hierarchies induce granularity-dependent interference, destabilizing popular replay and regularization mechanisms and thereby exacerbating catastrophic forgetting. To tackle these issues, we propose HALO (Hierarchical Adaptive Learning with Organized Prototypes), which adaptively combines complementary classification heads, regularized by organized learnable hierarchical prototypes, enabling rapid adaptation, hierarchical consistency, and structured knowledge consolidation as the taxonomy evolves. Extensive experiments on multiple benchmarks demonstrate that HALO consistently outperforms existing methods across hierarchical accuracy, mistake severity, and continual performance.

---


### 205. [WorldComp2D: Spatio-semantic Representations of Object Identity and Location from Local Views](https://arxiv.org/abs/2605.11743)

**<font color=#1a73e8>作者：</font>** SeongMin Jin, Doo Seok Jeong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning latent representations that capture both semantic and spatial information is central to efficient spatio-semantic reasoning. However, many existing approaches rely on implicit latent structures combined with dense feature maps or task-specific heads, limiting computational efficiency and flexibility. We propose WorldComp2D, a novel lightweight representation learning framework that explicitly structures latent space geometry according to object identity and spatial proximity using multiscale local receptive fields. This framework consists of (i) a proximity-dependent encoder that maps a given observation into a spatio-semantic latent space and (ii) a localizer that infers the coordinates of objects in the input from the resulting spatio-semantic representation. Using facial landmark localization as a proof-of-concept, we show that, compared to SoTA lightweight models, WorldComp2D reduces the numbers of parameters and FLOPs by up to 4.0X and 2.2X, respectively, while maintaining real-time performance on CPU. These results demonstrate that explicitly structured latent spaces provide an efficient and general foundation for spatio-semantic reasoning. This framework is open-sourced at this https URL.

---


### 206. [BronchoLumen: Analysis of recent YOLO-based architectures for real-time bronchial orifice detection in video bronchoscopy](https://arxiv.org/abs/2605.11748)

**<font color=#1a73e8>作者：</font>** Yongchao Li, Marian Himstedt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bronchoscopy is routinely conducted in pulmonary clinics and intensive care units, but navigating the complex branching of the respiratory tract remains challenging. This paper introduces BronchoLumen, a real-time YOLO-based system for detecting bronchial orifices in video bronchoscopy, aiming to assist navigation and CAD systems. The paper investigates if bronchial orifices can be robustly detected across image domains using state-of-the-art object detection and a limited set of public image data. The study includes the description and comparison of YOLOv8, a widely adopted architecture, and YOLOv12, a more recent architecture integrating attention-based modules to improve spatial reasoning. Both models are trained and tested solely on publicly available datasets comprising different image domains. A comparison of both models is conducted based on the common metrics mAP@0.5 and mAP@0.5:0.9 with the latter emphasizing localization accuracy. For YOLOv8 we obtained a mAP@0.5 of 0.91 on an in-domain and 0.68 on a cross-domain test set. YOLOv12 achieved 0.84 and 0.68 respectively with slightly better localization accuracy with mAP@0.5:0.9 of 0.48 and 0.26 compared to YOLOv8 with 0.45 and 0.25. Challenges like motion blur and low contrast occasionally entailed uncertainties but the system demonstrated overall robustness in most scenarios. BronchoLumen is an open-weight, YOLO-based solution for bronchial orifice detection offering high accuracy and efficiency across multiple image domains. While the more recent YOLOv12 achieves better localization accuracy, we observed a slightly worse precision. The models have been made publicly available to foster further research in bronchoscopy navigation.

---


### 207. [Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised Graph Anomaly Detection](https://arxiv.org/abs/2605.11749)

**<font color=#1a73e8>作者：</font>** Yingjie Zhou, Yuqin Xie, Fanxing Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weakly supervised graph anomaly detection aims to unveil unusual graph instances, e.g., nodes, whose behaviors significantly differ from normal ones, given only a limited number of annotated anomalies and abundant unlabeled samples. A major challenge is to learn a meaningful latent feature representation that reduces intra-class variance among normal data while remaining highly sensitive to anomalies. Although recent works have applied self-supervised feature learning for graph anomaly detection, their strategies are not specifically tailored to its unique requirements, motivating our exploration of a more domain-specific approach. In this paper, we introduce a weakly supervised graph anomaly detection method that leverages a feature learning strategy tailored for graph anomalies. Our approach is built upon a multi-task learning scheme that extracts robust feature representations through synthesized anomalies. We generate synthetic anomalies by perturbing the normal graph in various ways and assign a dedicated detection head to each anomaly type, ensuring that learned features are sensitive to potential deviations from normal patterns. Although synthetic anomalies may not perfectly replicate real-world patterns, they provide valuable auxiliary data for effective feature learnin, much like features learned from ImageNet classification transfer to downstream vision tasks. Additionally, we adopt a two-phase learning strategy: an initial warm-up phase using only synthetic samples, followed by a full-training phase integrating both tasks, to balance the influence of synthetic and real data. Extensive experiments on public datasets demonstrate the superior performance of our method over its competitors. Code is available at this https URL.

---


### 208. [Federated Client Selection under Partial Visibility: A POMDP Approach with Spatio-Temporal Attention](https://arxiv.org/abs/2605.11752)

**<font color=#1a73e8>作者：</font>** Qijun Hou, Yuchen Shi, Pingyi Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning relies on effective client selection to alleviate the performance degradation caused by data heterogeneity. Most existing methods assume full visibility of all clients at each communication round. However, in large-scale or edge-based deployments, the server can only access a subset of clients due to communication, mobility, or availability constraints, resulting in partial visibility where only a subset of clients is observable for aggregation in each communication round. In this paper, we formulate federated client selection under partial visibility as a Partially Observable Markov Decision Process (POMDP) and propose a Spatial-Temporal attention-based reinforcement learning framework. By integrating historical global models and client identity embeddings, the proposed method captures both the temporal contexts of training and the persistent characteristics of clients. Experimental results across multiple datasets demonstrate that our approach achieves superior performance compared to existing baselines in heterogeneous and partially visible settings, validating its effectiveness in addressing the challenges of incomplete observations in practical federated learning systems.

---


### 209. [One-Step Generative Modeling via Wasserstein Gradient Flows](https://arxiv.org/abs/2605.11755)

**<font color=#1a73e8>作者：</font>** Jiaqi Han, Puheng Li, Qiushan Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models and flow-based methods have shown impressive generative capability, especially for images, but their sampling is expensive because it requires many iterative updates. We introduce W-Flow, a framework for training a generator that transforms samples from a simple reference distribution into samples from a target data distribution in a single step. This is achieved in two steps: we first define an evolution from the reference distribution to the target distribution through a Wasserstein gradient flow that minimizes an energy functional; second, we train a static neural generator to compress this evolution into one-step generation. We instantiate the energy functional with the Sinkhorn divergence, which yields an efficient optimal-transport-based update rule that captures global distributional discrepancy and improves coverage of the target distribution. We further prove that the finite-sample training dynamics converge to the continuous-time distributional dynamics under suitable assumptions. Empirically, W-Flow sets a new state of the art for one-step ImageNet 256$\times$256 generation, achieving 1.29 FID, with improved mode coverage and domain transfer. Compared to multi-step diffusion models with similar FID scores, our method yields approximately 100$\times$ faster sampling. These results show that Wasserstein gradient flows provide a principled and effective foundation for fast and high-fidelity generative modeling.

---


### 210. [Focusable Monocular Depth Estimation](https://arxiv.org/abs/2605.11756)

**<font color=#1a73e8>作者：</font>** Yuxin Du, Tao Lin, Zile Zhong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth foundation models generalize well across scenes, yet they are typically optimized with uniform pixel-wise objectives that do not distinguish user-specified or task-relevant target regions from the surrounding context. We therefore introduce Focusable Monocular Depth Estimation (FDE), a region-aware depth estimation task in which, given a specified target region, the model is required to prioritize foreground depth accuracy, preserve sharp boundary transitions, and maintain coherent global scene geometry. To prioritize task-critical region modeling, we propose FocusDepth, a prompt-conditioned monocular relative depth estimation framework that guides depth modeling to focus on target regions via box/text prompts. The core Multi-Scale Spatial-Aligned Fusion (MSSA) in FocusDepth spatially aligns multi-scale features from Segment Anything Model 3 to the Depth Anything family and injects them through scale-specific, gated conditional fusion. This enables dense prompt cue injection without disrupting geometric representations, thereby endowing the depth estimation model with focused perception capability. To study FDE, we establish FDE-Bench, a target-centric monocular relative depth benchmark built from image-target-depth triplets across five datasets, containing 252.9K/72.5K train/val triplets and 972 categories spanning real-world and embodied simulation environments. On FDE-Bench, FocusDepth consistently improves over globally fine-tuned DA2/DA3 baselines under both box and text prompts, with the largest gains appearing in target boundary and foreground regions while preserving global scene geometry. Ablations show that MSSA's spatial alignment is the key design factor, as disrupting prompt-geometry correspondence increases AbsRel by up to 13.8%.

---


### 211. [M$^4$-SAM: Multi-Modal Mixture-of-Experts with Memory-Augmented SAM for RGB-D Video Salient Object Detection](https://arxiv.org/abs/2605.11760)

**<font color=#1a73e8>作者：</font>** Jiyuan Liu, Jia Lin, Xiaofei Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Segment Anything Model 2 (SAM2) has emerged as a foundation model for universal segmentation. Owing to its generalizable visual representations, SAM2 has been successfully applied to various downstream tasks. However, extending SAM2 to the RGB-D video salient object detection (RGB-D VSOD) task encounters three challenges including limited spatial modeling of linear LoRA, insufficient employment of SAM's multi-scale features, and dependence of initialization on explicit prompts. To address the issues, we present Multi-Modal Mixture-of-Experts with Memory-Augmented SAM (M$^4$-SAM), which equips SAM2 with modality-related PEFT, hierarchical feature fusion, and prompt-free memory initialization. Firstly, we inject Modality-Aware MoE-LORA, which employs convolutional experts to encode local spatial priors and introduces a modality dispatcher for efficient multi-modal fine-tuning, into SAM2's encoder. Secondly, we deploy Gated Multi-Level Feature Fusion, which hierarchically aggregates multi-scale encoder features with an adaptive gating mechanism, to balance spatial details and semantic context. Finally, to conduct zero-shot VSOD without manual prompts, we utilize a Pseudo-Guided Initialization, where a coarse mask is regarded as a pseudo prior and used to bootstrap the memory bank. Extensive experiments demonstrate that M$^4$-SAM achieves the state-of-the-art performance across all evaluation metrics on three public RGB-D VSOD datasets.

---


### 212. [Decomposing the Generalization Gap in PROTAC Activity Prediction: Variance Attribution and the Inter-Laboratory Ceiling](https://arxiv.org/abs/2605.11764)

**<font color=#1a73e8>作者：</font>** Thor Klamt, Wolfgang Nejdl, Ming Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning predictors of biochemical activity often exhibit large random-split-to-leave-one-target-out generalisation gaps that have been documented but not decomposed. We frame this as an evaluation-science question and use targeted protein degradation as the empirical test bed. PROTACs (proteolysis-targeting chimeras) are heterobifunctional small molecules that induce targeted protein degradation, with more than forty candidates currently in clinical trials; published predictors report AUROC of 0.85 to 0.91 under random-split cross-validation, while the leave-one-target-out (LOTO) protocol of Ribes et al. reduces performance to approximately 0.67. Random splits reward within-target interpolation, whereas LOTO measures the novel-target prediction that de-novo design depends on. We decompose this gap and identify inter-laboratory measurement variance as the dominant component, anchored by a within-target cross-laboratory cascade bounding the inter-laboratory contribution at 0.124 AUROC, well above the 0.05 contribution from binarisation-threshold choice. Across eight published architectures and ESM-2 protein language models up to 3B parameters, LOTO AUROC plateaus near 0.67, with a comparable plateau under SMILES-level deduplication; a 21-dimensional 2000-trial hyperparameter optimisation cannot break this ceiling, and the rank-1 single-seed configuration regresses by 0.161 AUROC under multi-seed validation, matching a closed-form selection-bias prediction (Bailey and Lopez de Prado, 2014). Few-shot k=5 stratified per-target retraining combined with ADMET features lifts 65-target LOTO AUROC from 0.668 to 0.7050, and post-hoc Platt scaling recovers raw output to within the 0.05 well-calibrated threshold. We release PROTAC-Bench (10,748 measurements, 173 targets, 65 LOTO folds), the variance-decomposition framework, the per-target calibration protocol, and the evaluation code.

---


### 213. [Safety-Oriented Evaluation of Language Understanding Systems for Air Traffic Control](https://arxiv.org/abs/2605.11769)

**<font color=#1a73e8>作者：</font>** Yujing Chang, Yash Guleria, Duc-Thinh Pham 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Air Traffic Control (ATC) is a safety-critical domain in which incorrect interpretation of instructions may lead to severe operational consequences. While large language models (LLMs) demonstrate strong general performance, their reliability in operational ATC environments remains unclear. Existing evaluation approaches, largely based on aggregate metrics such as F1 or macro accuracy, treat all errors uniformly and fail to account for the asymmetric consequences of high-risk semantic mistakes (e.g., incorrect runway identifiers or movement constraints). To address this gap, we propose a safety-oriented, consequence-aware evaluation framework tailored to ATC operations. Our results reveal that while current LLMs achieve reasonable aggregate accuracy, their operational reliability is severely limited. Evaluated on clean transcripts, the peak Risk Score reaches only 0.69, with most models scoring below 0.6 despite high macro-F1 performance. Further analysis shows that errors concentrate in high-impact entities despite relatively stable action-type classification, indicating structural grounding deficiencies. These findings highlight the necessity of consequence-aware evaluation protocols for the responsible deployment of AI-assisted ATC systems.

---


### 214. [Behavioral Integrity Verification for AI Agent Skills](https://arxiv.org/abs/2605.11770)

**<font color=#1a73e8>作者：</font>** Yuhao Wu, Tung-Ling Li, Hongliang Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills extend LLM agents with privileged third-party capabilities such as filesystem access, credentials, network calls, and shell execution. Existing safety work catches malicious prompts and risky runtime actions, but the skill artifact itself goes unverified. We formalize this as the behavioral integrity verification (BIV) problem: a typed set comparison between declared and actual capabilities over a shared taxonomy that bridges code, instructions, and metadata. The BIV framework instantiates this comparison by pairing deterministic code analysis with LLM-assisted capability extraction. The resulting structured evidence supports three downstream analyses: deviation taxonomy, root-cause classification, and malicious-skill detection. On 49,943 skills from the OpenClaw registry, the deviation taxonomy reveals a pervasive description-implementation gap: 80.0% of skills deviate from declared behavior, with four novel compound-threat categories surfaced. Root-cause classification finds that deviations are mostly oversight, not malice: 81.1% trace to developer oversight and 18.9% to adversarial intent, with 5.0% of skills carrying predicted multi-stage attack chains. On a 906-skill malicious-skill detection benchmark, BIV reaches an F1 of 0.946, outperforming state-of-the-art rule-based and single-pass LLM baselines. These results demonstrate behavioral integrity auditing for agent skills at scale.

---


### 215. [Revisiting Shadow Detection from a Vision-Language Perspective](https://arxiv.org/abs/2605.11771)

**<font color=#1a73e8>作者：</font>** Yonghui Wang, Wengang Zhou, Hao Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shadow detection is commonly formulated as a vision-driven dense prediction problem, where models rely primarily on pixel-wise visual supervision to distinguish shadows from non-shadow regions. However, this formulation can become unreliable in visually ambiguous cases, where similar dark regions may correspond either to cast shadows or to intrinsically dark surfaces, making visual evidence alone insufficient for establishing a stable decision rule. In this work, we revisit shadow detection from a vision--language perspective and argue that robust prediction benefits from an explicit semantic reference beyond visual cues alone. We propose SVL, a Shadow Vision--Language framework that uses language as an explicit semantic reference to disambiguate shadows from visually similar dark regions. SVL aligns the global image representation with shadow-related text embeddings through a scene-level shadow ratio regression objective, thereby providing image-level guidance on the overall extent of shadows. To transfer this global guidance to dense inference, SVL introduces a global-to-local coupling mechanism that enforces consistency between image-level guidance and patch-level predictions. In parallel, SVL applies local patch-level constraints with text embeddings to improve fine-grained discrimination under challenging appearance conditions. Built on a frozen DINOv3 image encoder, the framework learns only lightweight projection and decoding modules, yielding a parameter-efficient design with less than $1\%$ trainable parameters. Extensive experiments on multiple shadow detection benchmarks, including dedicated hard-case evaluations, suggest strong overall performance and improved robustness under visually ambiguous conditions.

---


### 216. [Is Monotonic Sampling Necessary in Diffusion Models?](https://arxiv.org/abs/2605.11773)

**<font color=#1a73e8>作者：</font>** Muhammad Haris Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models generate samples by iteratively denoising a Gaussian prior, traversing a sequence of noise levels that, in every published sampler, decreases monotonically. Six years of intensive work has refined nearly every aspect of this recipe, including the corruption operator, the training objective, the schedule shape, the architecture, and the ODE solver. Yet the assumption of monotonicity itself has never been systematically tested. Here we ask whether monotonic sampling is load-bearing or merely conventional. We design four families of structured nonmonotonic schedules and apply them to three architecturally distinct generative models, DDPM, EDM, and Flow Matching, across NFE budgets ranging from 10 to 200 function evaluations, plus a 42-cell hyperparameter ablation, on CIFAR-10. Across all 90 tested configurations, no tested nonmonotonic schedule improves on the monotonic baseline. The magnitude of the penalty, however, spans nearly three orders of magnitude: persistent and substantial in DDPM, intermediate in Flow Matching, and indistinguishable from zero in EDM. We show that this variation is not noise but a structural property of each trained denoiser, and we formalize it as the Schedule Sensitivity Coefficient, a cheap, architecture-agnostic diagnostic that provides evidence of non-convergence to the Bayes-optimal denoiser at the critical noise level. Our findings justify the field's tacit reliance on monotonic schedules and supply a new probe of diffusion model quality complementary to sample-quality metrics such as Frechet Inception Distance.

---


### 217. [Choosing features for classifying multiword expressions](https://arxiv.org/abs/2605.11779)

**<font color=#1a73e8>作者：</font>** Eric Laporte  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiword expressions (MWEs) are a heterogeneous set with a glaring need for classifications. Designing a satisfactory classification involves choosing features. In the case of MWEs, many features are a priori available. Not all features are equal in terms of how reliably MWEs can be assigned to classes. Accordingly, resulting classifications may be more or less fruitful for computational use. I outline an enhanced classification. In order to increase its suitability for many languages, I use previous works taking into account various languages.

---


### 218. [Psychological Benefits and Costs of Diversifying Algorithmic Recourse](https://arxiv.org/abs/2605.11793)

**<font color=#1a73e8>作者：</font>** Tomu Tominaga, Naomi Yamashita, Takeshi Kurashima  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Algorithmic recourse provides counterfactual action plans that help people overturn unfavorable AI decisions. While diverse recourse sets may improve transparency and motivation, they may also impose cognitive load and negative emotions by increasing counterfactual reasoning demands. To examine this trade-off, we conducted a between-subjects controlled experiment (N=750) that manipulated recourse-set diversity and size, and evaluated these effects on psychological benefits and costs. Results show that diversification enhances psychological benefits (e.g., willingness to act) for small sets without incurring additional psychological costs, whereas for large sets, it makes cognitive load more salient. These findings suggest that naively diversifying recourse can burden decision subjects, underscoring the need for new diversification methods that incorporate human cognition and psychology to mitigate such costs.

---


### 219. [SB-BEVFusion: Enhancing the Robustness against Sensor Malfunction and Corruptions](https://arxiv.org/abs/2605.11799)

**<font color=#1a73e8>作者：</font>** Markus Essl, Marta Moscati, Mubashir Noman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal sensor fusion has demonstrated remarkable performance improvements over unimodal approaches in 3D object detection for autonomous vehicles. Typically, existing methods transform multimodal data from independent sensors, such as camera and LiDAR, into a unified bird's-eye view (BEV) representation for fusion. Although effective in ideal conditions, this strategy suffers from substantial performance deterioration when camera or LiDAR data are missing, corrupted, or noisy. To address this vulnerability, we develop a framework-agnostic fusion module for camera and LiDAR data that allows for handling cases when one of the two modalities is missing or corrupted. To demonstrate the effectiveness of our module, we instantiate it in BEVFusion [1], a well-established framework to combine camera and LiDAR data for 3D object detection. By means of quantitative experiments on the MultiCorrupt dataset, we demonstrate that our module achieves favorable performance improvements under scenarios of missing and corrupted modalities, substantially outperforming existing unified representation approaches across a wide range of sensor deterioration scenarios and reaching state-of-the-art performance in scenarios of corrupted modality due to extreme weather conditions and sensor failure.

---


### 220. [Stop Marginalizing My Dreams: Model Inversion via Laplace Kernel for Continual Learning](https://arxiv.org/abs/2605.11804)

**<font color=#1a73e8>作者：</font>** Patryk Krukowski, Jacek Tabor, Przemysław Spurek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-free continual learning (DFCIL) relies on model inversion to synthesize pseudo-samples and mitigate catastrophic forgetting. However, existing inversion methods are fundamentally limited by a simplifying assumption: they model feature distributions using diagonal covariance, effectively ignoring correlations that define the geometry of learned representations. As a result, synthesized samples often lack fidelity, limiting knowledge retention. In this work, we show that modeling feature dependencies is a key ingredient for effective DFCIL. We introduce REMIX, a structured covariance modeling framework that enables scalable full-covariance modeling without the prohibitive cost of dense matrix inversion and log-determinant computation. By leveraging a Laplace kernel parameterization, REMIX captures structured feature dependencies using memory that scales linearly with the feature dimensionality, while requiring only an additional logarithmic factor in computation. Modeling these correlations produces more coherent synthetic samples and consistently improves performance across standard DFCIL benchmarks. Our results demonstrate that moving beyond diagonal assumptions is essential for effective and scalable data-free continual learning. Our code is available at https://github. com/pkrukowski1/REMIX-Model-Inversion-via-Laplace-Kernel.

---


### 221. [Beyond World-Frame Action Heads: Motion-Centric Action Frames for Vision-Language-Action Models](https://arxiv.org/abs/2605.11809)

**<font color=#1a73e8>作者：</font>** Huoren Yang, Jianchao Zhao, Hu Yusong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have advanced rapidly with stronger backbones, broader pre-training, and larger demonstration datasets, yet their action heads remain largely homogeneous: most directly predict action commands in a fixed world coordinate frame. We propose \textbf{MCF-Proto}, a lightweight action head that equips VLA policies with a Motion-Centric Action Frame (MCF) and a prototype-based action parameterization. At each step, the policy predicts a rotation $R_t \in SO(3)$, composes actions in the transformed local frame from a set of prototypes, and maps them back to the world frame for end-to-end training, using only standard demonstrations without auxiliary supervision. This simple design induces stable emergent structure. Without explicit directional labels, the learned local frames develop a stable geometric structure whose axes are strongly compatible with demonstrated end-effector motion. Meanwhile, actions in the learned representation become substantially more compact, with variation captured by fewer dominant directions and more regularly organized by shared prototypes. These structural properties translate into improved robustness, especially under geometric perturbations. Our results suggest that adding lightweight geometric and compositional structure to the action head can materially improve how VLA policies organize and generalize robotic manipulation behavior. An anonymized code repository is provided in the supplementary material.

---


### 222. [MedMemoryBench: Benchmarking Agent Memory in Personalized Healthcare](https://arxiv.org/abs/2605.11814)

**<font color=#1a73e8>作者：</font>** Yihao Wang, Haoran Xu, Renjie Gu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The large-scale deployment of personalized healthcare agents demands memory mechanisms that are exceptionally precise, safe, and capable of long-term clinical tracking. However, existing benchmarks primarily focus on daily open-domain conversations, failing to capture the high-stakes complexity of real-world medical applications. Motivated by the stringent production requirements of an industry-leading health management agent serving tens of millions of active users, we introduce MedMemoryBench. We develop a human-agent collaborative pipeline to synthesize highly realistic, long-horizon medical trajectories based on clinically grounded, synthetic patient archetypes. This process yields a massive, expertly validated dataset comprising approximately 2,000 sessions and 16,000 interaction turns. Crucially, MedMemoryBench departs from traditional static evaluations by pioneering an "evaluate-while-constructing" streaming assessment protocol, which precisely mirrors dynamic memory accumulation in production environments. Furthermore, we formalize and systematically investigate the critical phenomenon of memory saturation, where sustained information influx actively degrades retrieval and reasoning robustness. Comprehensive benchmarking reveals severe bottlenecks in mainstream architectures, particularly concerning complex medical reasoning and noise resilience. By exposing these fundamental flaws, MedMemoryBench establishes a vital foundation for developing robust, production-ready medical agents.

---


### 223. [Fed-BAC: Federated Bandit-Guided Additive Clustering in Hierarchical Federated Learning](https://arxiv.org/abs/2605.11815)

**<font color=#1a73e8>作者：</font>** Satwat Bashir, Tasos Dagiuklas, Muddesar Iqbal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical federated learning (HFL) leverages edge servers for partial aggregation in edge computing. Yet existing FL methods lack mechanisms for jointly optimizing cluster assignment and client selection under data heterogeneity. This paper proposes Fed-BAC, which integrates additive cluster personalization with a two-level bandit framework: contextual bandits at the cloud learn server-to-cluster assignments, while Thompson Sampling at each edge server identifies high-contributing clients. The additive decomposition enables the sharing of knowledge between groups through a globally aggregated network, while cluster-specific networks capture distribution variations. Across three classification benchmarks (CIFAR-10, SVHN, Fashion-MNIST) under moderate ($\alpha = 0.5$) and severe ($\alpha = 0.1$) Dirichlet non-IID partitioning, Fed-BAC achieves distributed accuracy gains of up to +35.5pp over HierFAVG and +8.4pp over IFCA, while requiring only 80% client participation, converging 1.5 to 4.8$\times$ faster depending on dataset and accuracy target, and improving cross-server fairness. These gains are further validated at 5$\times$ deployment scale on CIFAR-10. The advantage of Fed-BAC increases with heterogeneity severity, confirming that additive cluster personalization becomes increasingly valuable as data distributions diverge.

---


### 224. [Ink Spiral: Symbolic Transformation from The Thinker to the Four Gentlemen](https://arxiv.org/abs/2605.11816)

**<font color=#1a73e8>作者：</font>** Lingyu Peng, Wenbo Lu, Liying Long 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Western art has regarded The Thinker as a symbol of rational contemplation, while Eastern aesthetics has taken the Four Gentlemen, namely plum, orchid, bamboo, and chrysanthemum, as symbols of moral and spiritual cultivation. This paper presents Ink Spiral, a video installation that links these traditions through AI generated ink imagery. By transforming a rotating sculpture of The Thinker into the Four Gentlemen across thousands of frames, the work shifts between three dimensional sculpture and two dimensional ink, human introspection and natural symbolism. Ink Spiral turns fixed cultural icons into a fluid dialogue, inviting audiences to perceive cross cultural connection as a living, ambiguous, and endlessly interpretable creative state.

---


### 225. [RevealLayer: Disentangling Hidden and Visible Layers via Occlusion-Aware Image Decomposition](https://arxiv.org/abs/2605.11818)

**<font color=#1a73e8>作者：</font>** Binhao Wang, Shihao Zhao, Bo Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based approaches have made substantial progress in image layer decomposition. However, accurately decomposing complex natural images remains challenging due to difficulties in occlusion completion, robust layer disentanglement, and precise foreground boundaries. Moreover, the scarcity of high-quality multi-layer natural image datasets limits advancement. To address these challenges, we propose RevealLayer, a diffusion-based framework that decomposes an RGB image into multiple RGBA layers, enabling precise layer separation and reliable recovery of occluded content in natural images. RevealLayer incorporates three key components: (1) a Region-Aware Attention module to disentangle hidden and visible layers; (2) an Occlusion-Guided Adapter to leverage contextual information to enhance overlapping regions; and (3) a composite loss to enforce sharp alpha boundaries and suppress residual artifacts. To support training and evaluation, we introduce RevealLayer-100K, a high-quality multi-layer natural image constructed through a collaboration between automated algorithms and human annotation, and further establish RevealLayerBench for benchmarking layer decomposition in general natural scenes. Extensive experiments demonstrate that RevealLayer consistently outperforms existing approaches in layer decomposition.

---


### 226. [REFNet++: Multi-Task Efficient Fusion of Camera and Radar Sensor Data in Bird's-Eye Polar View](https://arxiv.org/abs/2605.11824)

**<font color=#1a73e8>作者：</font>** Kavin Chandrasekaran, Sorin Grigorescu, Gijs Dubbelman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A realistic view of the vehicle's surroundings is generally offered by camera sensors, which is crucial for environmental perception. Affordable radar sensors, on the other hand, are becoming invaluable due to their robustness in variable weather conditions. However, because of their noisy output and reduced classification capability, they work best when combined with other sensor data. Specifically, we address the challenge of multimodal sensor fusion by aligning radar and camera data in a unified domain, prioritizing not only accuracy, but also computational efficiency. Our work leverages the raw range-Doppler (RD) spectrum from radar and front-view camera images as inputs. To enable effective fusion, we employ a variational encoder-decoder architecture that learns the transformation of front-view camera data into the Bird's-Eye View (BEV) polar domain. Concurrently, a radar encoder-decoder learns to recover the angle information from the RD data that produce Range-Azimuth (RA) features. This alignment ensures that both modalities are represented in a compatible domain, facilitating robust and efficient sensor fusion. We evaluated our fusion strategy for vehicle detection and free space segmentation against state-of-the-art methods using the RADIal dataset.

---


### 227. [COSMIC 1001: Engaging Future Speculation on Space Exploration with Generative AI](https://arxiv.org/abs/2605.11827)

**<font color=#1a73e8>作者：</font>** Lingyu Peng, Yu Liang, Ying Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cosmic 1001 is an interactive installation that transforms space exploration history into a speculative news experience. Participants first browse a news-based archive of major space events, then pose future-oriented questions or specify conditions such as year, celestial body, or mission name. In response, AI generates a future news item including a headline, article, narration, and visual media. These outputs are accumulated in the Future Tunnel, a shared visualization where individual stories form a collective landscape of possible futures. By combining historical space events with science fiction references, the installation explores a space between documentation and imagination, treating the future not as a fixed prediction but as a visible and discussable speculation.

---


### 228. [More Edits, More Stable: Understanding the Lifelong Normalization in Sequential Model Editing](https://arxiv.org/abs/2605.11836)

**<font color=#1a73e8>作者：</font>** Xin Ma, Wei Chen, Qi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lifelong Model Editing aims to continuously update evolving facts in Large Language Models while preserving unrelated knowledge and general capabilities, yet it remains plagued by catastrophic forgetting and model collapse. Empirically, we find that recent editors resilient over long horizons share the same core strategy: Lifelong Normalization (LN), which normalizes value gradients using running statistics. Removing LN causes immediate performance collapse, and we observe a counter-intuitive positive cumulative effect where early edits can promote the success of future edits. Yet the mechanism of LN remains a "black box", leaving its precise role in lifelong stability poorly understood. In this work, we provide the first theoretical account of LN in the lifelong regime. Our analysis reveals a self-reinforcing stability loop and proves that, when combined with ridge-regularized regression, LN yields parameter updates with asymptotic orthogonality and bounded norms, directly mitigating forgetting and systemic collapse. Based on these insights, we derive StableEdit, which strengthens this stability loop via an explicit warm-up stage and full whitening, improving long-horizon stability at minimal overhead. Extensive experiments validate our theory and demonstrate competitive performance. Our code is available at this https URL.

---


### 229. [Gradient Clipping Beyond Vector Norms: A Spectral Approach for Matrix-Valued Parameters](https://arxiv.org/abs/2605.11838)

**<font color=#1a73e8>作者：</font>** Alexander Yukhimchuk, Mladen Kolar, Martin Takáč 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient clipping is a standard safeguard for training neural networks under noisy, heavy-tailed stochastic gradients; yet, most clipping rules treat all parameters as vectors and ignore the matrix structure of modern architectures. We show empirically that data outliers often amplify only a small number of leading singular values in layer-wise gradient matrices, while the rest of the spectrum remains largely unchanged. Motivated by this phenomenon, we propose spectral clipping, which stabilizes training by clamping singular values that exceed a threshold while preserving the singular directions. This framework generalizes classical gradient norm clipping and can be easily integrated into existing optimizers. We provide a convergence analysis for non-convex optimization with spectrally clipped SGD, yielding the optimal $\mathcal{O}\left(K^{\frac{2 - 2\alpha}{3\alpha - 2}}\right)$ rate for heavy-tailed noise. To minimize hyperparameter tuning, we introduce layer-wise adaptive thresholds based on moving averages or sliding-window quantiles of the top singular values. Finally, we develop efficient implementations that clip only the top $r$ singular values via randomized truncated SVD, avoiding full decompositions for large layers. We demonstrate competitive performance across synthetic heavy-tailed settings and neural network training tasks.

---


### 230. [Selection, Not Fusion: Radar-Modulated State Space Models for Radar-Camera Depth Estimation](https://arxiv.org/abs/2605.11840)

**<font color=#1a73e8>作者：</font>** Zhangcheng Hou, Tomoaki Ohtsuki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radar-camera depth estimation must turn an ultra-sparse, all-weather, metric radar signal into a dense per-pixel depth map. Existing methods -- concatenation, confidence-aware gating, sparse supervision, graph-based extraction -- combine radar and image features outside the backbone's sequence operator, and even cross-modal Mamba variants leave the selection mechanism itself unimodal. We argue that the selection mechanism is the right place for radar to enter. We introduce Radar-Modulated Selection (RMS), a minimal and principled way to inject radar into Mamba's selective scan: radar modulates the scan from within, adding zero-initialised perturbations to the step size $\Delta$ and readout $\mathbf{C}$ while leaving the input projection $\mathbf{B}$ and state dynamics $\mathbf{A}$ image-only. The construction is exactly equivalent to a pretrained image-only Mamba at initialisation, ensuring radar only influences the model where it improves accuracy. Two further properties follow that out-of-scan fusion cannot offer: linear-cost cross-modal coupling at every recurrence step, and a natural fallback to the image-only backbone when radar is absent. We deploy RMS in a Multi-View Scan Pyramid (MVSP) that matches the fusion operator to radar's spatial reach at each scale. SemoDepth achieves state-of-the-art performance on nuScenes, reducing MAE by 34.0%, 29.9%, and 29.9% over the previous best at 0--50, 0--70, and 0--80m, while attaining the lowest single-frame latency (26.8ms). A further ablation shows that out-of-scan feature blending adds no accuracy on top of RMS, providing empirical validation that in-scan selection can replace out-of-scan fusion.

---


### 231. [Martingale-Consistent Self-Supervised Learning](https://arxiv.org/abs/2605.11846)

**<font color=#1a73e8>作者：</font>** Moritz Gögl, Hanwen Xing, Christopher Yau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) is often deployed under changing information, such as shorter histories, missing features, or partially observed images. In these settings, predictions from coarse and refined views should be coherent: before refinement, the coarse-view prediction should match the average prediction expected after refinement. Martingales formalize this coherence principle, but standard SSL objectives do not enforce it. Unlike invariance objectives that pull views together, martingale consistency constrains only the expected refined prediction, allowing predictions to update as information is revealed while preventing systematic drift. We introduce a martingale-consistent SSL framework that closes this gap, with practical prediction- and latent-space variants and an unbiased two-sample Monte Carlo estimator based on stochastic refinement. We evaluate the approach on synthetic and real time-series, tabular, and image benchmarks under partial-observation regimes, in both semi-self-supervised and fully label-free settings. Across these experiments, our framework improves robustness and calibration under partial observation, yielding more stable representations as information is revealed.

---


### 232. [Improving the Performance and Learning Stability of Parallelizable RNNs Designed for Ultra-Low Power Applications](https://arxiv.org/abs/2605.11855)

**<font color=#1a73e8>作者：</font>** Julien Brandoit, Arthur Fyon, Damien Ernst 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequence learning is dominated by Transformers and parallelizable recurrent neural networks (RNNs) such as state-space models, yet learning long-term dependencies remains challenging, and state-of-the-art designs trade power consumption for performance. The Bistable Memory Recurrent Unit (BMRU) was introduced to enable hardware-software co-design of ultra-low power RNNs: quantized states with hysteresis provide persistent memory while mapping directly to analog primitives. However, BMRU performance lags behind parallelizable RNNs on complex sequential tasks. In this paper, we identify gradient blocking during state updates as a key limitation and propose a cumulative update formulation that restores gradient flow while preserving persistent memory, creating skip-connections through time. This leads to the Cumulative Memory Recurrent Unit (CMRU) and its relaxed variant, the $\alpha$CMRU. Experiments show that the cumulative formulation dramatically improves convergence stability and reduces initialization sensitivity. The CMRU and $\alpha$CMRU match or outperform Linear Recurrent Units (LRUs) and minimal Gated Recurrent Units (minGRUs) across diverse benchmarks at small model sizes, with particular advantages on tasks requiring discrete long-range retention, while the CMRU retains quantized states, persistent memory, and noise-resilient dynamics essential for analog implementation.

---


### 233. [Concordance Comparison as a Means of Assembling Local Grammars](https://arxiv.org/abs/2605.11862)

**<font color=#1a73e8>作者：</font>** Juliana Pirovani, Elias de Oliveira, Eric Laporte  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Named Entity Recognition for person names is an important but non-trivial task in information extraction. This article uses a tool that compares the concordances obtained from two local grammars (LG) and highlights the differences. We used the results as an aid to select the best of a set of LGs. By analyzing the comparisons, we observed relationships of inclusion, intersection and disjunction within each pair of LGs, which helped us to assemble those that yielded the best results. This approach was used in a case study on extraction of person names from texts written in Portuguese. We applied the enhanced grammar to the Gold Collection of the Second HAREM. The F-Measure obtained was 76.86, representing a gain of 6 points in relation to the state-of-the-art for Portuguese.

---


### 234. [GATA2Floor: Graph attention for floor counting in street-view facades](https://arxiv.org/abs/2605.11863)

**<font color=#1a73e8>作者：</font>** Ngoc Tan Le, Tzoulio Chamiti, Eirini Papagiannopoulou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated analysis of building facades from street-level imagery has great potential for urban analytics, energy assessment, and emergency planning. However, it requires reasoning over spatially arranged elements rather than solely isolated detections. In this work, we model each facade as a graph over window/door detections with a vertical prior on edges. Additionally, we introduce GATA2Floor, a multi-head Graph Attention v2 (GATv2) based model that predicts the global floor count of a building and, via learnable cross-attention queries, softly assigns elements to latent floor slots, yielding interpretable outputs and robustness to irregular designs. To mitigate the lack of labeled datasets, we demonstrate that the proposed graph-based reasoning can be applied without annotations by leveraging a lightweight label-free proposal mechanism based on self-supervised features and vision-language scoring. Our approach demonstrates the value of graph-attention-based relational reasoning for facade understanding.

---


### 235. [When Brains Disagree: Biological Ambiguity Underlies the Challenge of Amyloid PET Synthesis from Structural MRI](https://arxiv.org/abs/2605.11867)

**<font color=#1a73e8>作者：</font>** Louise E.G. Baron, Ross Callaghan, David M. Cash 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structural MRI-to-amyloid PET synthesis has been proposed as a non-invasive alternative for amyloid assessment in Alzheimer's disease (AD). However, reported performance of identical models varies widely across studies, and increasingly complex architectures have not led to consistent gains. This inconsistency is thought to be caused by a fundamental biological ambiguity: MRI captures neurodegeneration, while PET measures amyloid pathology - two processes that are often temporally decoupled in AD. As a result, similar MRI patterns may correspond to different amyloid states, creating ambiguous one-to-many mappings. MRI-to-amyloid PET synthesis may therefore be intrinsically ill-posed; however, this idea has yet to be tested scientifically. The aim of this work is to test this hypothesis through two controlled experiments. We first control the training distribution by stratifying paired MRI-PET data by amyloid and neurodegeneration status. Using two standard synthesis models under a controlled design, we show that biologically unambiguous mappings are learnable in isolation, but performance collapses when data ambiguity is introduced. This demonstrates that ambiguity in the data distribution, rather than architectural capacity, constrains performance. Second, we show that introducing orthogonal biological information in the form of plasma biomarkers resolves this ambiguity. When multimodal inputs are incorporated, performance improves and stability is restored. Together, these findings suggest that limited and inconsistent performance in MRI-to-amyloid PET synthesis is explained by intrinsic biological ambiguity, and that stable, meaningful progress requires multimodal integration rather than architectural complexity.

---


### 236. [IPI-proxy: An Intercepting Proxy for Red-Teaming Web-Browsing AI Agents Against Indirect Prompt Injection](https://arxiv.org/abs/2605.11868)

**<font color=#1a73e8>作者：</font>** Chia-Pei, Chen, Kentaroh Toyoda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web-browsing AI agents are increasingly deployed in enterprise settings under strict whitelists of approved domains, yet adversaries can still influence them by embedding hidden instructions in the HTML pages those domains serve. Existing red-teaming resources fall short of this scenario: prompt-injection benchmarks ship pre-built adversarial pages that whitelisted agents cannot reach, and generic LLM scanners probe the model API rather than its retrieved content. We present IPI-proxy, an open-source toolkit for red-teaming web-browsing agents against indirect prompt injection (IPI). At its core is an intercepting proxy that rewrites real HTTP responses from whitelisted domains in flight, embedding payloads drawn from a unified library of 820 deduplicated attack strings extracted from six published benchmarks (BIPIA, InjecAgent, AgentDojo, Tensor Trust, WASP, and LLMail-Inject). A YAML-driven test harness independently parameterizes the payload set, the embedding technique (HTML comment, invisible CSS, or LLM-generated semantic prose), and the HTML insertion point (6 locations from \icode{head\_meta} to \icode{script\_comment}), enabling parameter-sweep evaluation without mock pages or sandboxed environments. A companion exfiltration tracker logs successful callbacks. This paper describes the threat model, situates IPI-proxy among contemporary IPI benchmarks and red-teaming tools, and details its architecture, design decisions, and configuration interface. By bridging static benchmarks and live deployment, IPI-proxy gives AI security teams a reproducible substrate for measuring and hardening web-browsing agents against indirect prompt injection on the same retrieval surface attackers exploit in production.

---


### 237. [FIS-DiT: Breaking the Few-Step Video Inference Barrier via Training-Free Frame Interleaved Sparsity](https://arxiv.org/abs/2605.11869)

**<font color=#1a73e8>作者：</font>** Jian Tang, Jiawei Fan, Qingbin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While the overall inference latency of Video Diffusion Transformers (DiTs) can be substantially reduced through model distillation, per-step inference latency remains a critical bottleneck. Existing acceleration paradigms primarily exploit redundancy across the denoising trajectory; however, we identify a limitation where these step-wise strategies encounter diminishing returns in few-step regimes. In such scenarios, the scarcity of temporal states prevents effective feature reuse or predictive modeling, creating a formidable barrier to further acceleration. To overcome this, we propose Frame Interleaved Sparsity DiT (FIS-DiT), a training-free and operator-agnostic framework that shifts the optimization focus from the temporal trajectory to the latent frame dimension. Our approach is motivated by an intrinsic duality within this dimension: the existence of frame-wise sparsity that permits reduced computation, coupled with a structural consistency where each frame position remains equally vital to the global spatiotemporal context. Leveraging this insight, we implement Frame Interleaved Sparsity (FIS) as an execution strategy that manipulates frame subsets across the model hierarchy, refreshing all latent positions without requiring full-scale block computation. Empirical evaluations on Wan 2.2 and HunyuanVideo 1.5 demonstrate that FIS-DiT consistently achieves 2.11--2.41$\times$ speedup with negligible degradation across VBench-Q and CLIP metrics, providing a scalable and robust pathway toward real-time high-definition video generation.

---


### 238. [Information theoretic underpinning of self-supervised learning by clustering](https://arxiv.org/abs/2605.11870)

**<font color=#1a73e8>作者：</font>** Josef Kittler, Sara Atito, Muhammad Awais  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) is recognized as an essential tool for building foundation models for Artificial Intelligence applications. The advances in SSL have been made thanks to vigorous arguments about the principles of SSL and through extensive empirical research. The aim of this paper is to contribute to the development of the underpinning theory of SSL, focusing on the deep clustering approach. By analogy to supervised learning, we formulate SSL as K-L divergence optimization.
The mode collapse is prevented by imposing an optimisation constraint on the teacher distribution. This leads to normalization using inverse cluster priors. We show that using Jensen inequality this normalization simplifies to the popular batch centering procedure. Distillation and centering are common {heuristics-based} practices in SSL, {but our work underpins them theoretically.} The theoretical model developed not only supports specific existing successful SSL methods, but also suggests directions for future investigations.

---


### 239. [$h$-control: Training-Free Camera Control via Block-Conditional Gibbs Refinement](https://arxiv.org/abs/2605.11871)

**<font color=#1a73e8>作者：</font>** Yuzhu Wang, Xi Ye, Duo Su 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free camera control for pretrained flow-matching video generators is a partial-observation inverse problem: a depth-warped guidance video supplies noisy evidence on a subset of latent sites, which the sampler must reconcile with the pretrained prior. Existing methods struggle to balance the trade-off between trajectory adherence and visual quality and the heuristic guidance-strength tuning lacks robustness. We propose \textbf{$h$-control}, which resolves this dilemma through a structural change to the sampler: each outer hard-replacement guidance step is augmented with an inner-loop \emph{block-conditional pseudo-Gibbs refinement} on the unobserved complement at the same noise level, with provable convergence to the partial-observation conditional data law. To accelerate convergence on high-dimensional video latents, we exploit their conditional locality, partitioning the unobserved complement into 3D patches, each tracked by a custom mixing indicator that adaptively freezes converged patches. On RealEstate10K and DAVIS, \textbf{$h$-control} attains the best FVD against all seven training-free and training-based competitors, outperforming every training-free baseline on every reported metric.

---


### 240. [Adaptive TD-Lambda for Cooperative Multi-agent Reinforcement Learning](https://arxiv.org/abs/2605.11880)

**<font color=#1a73e8>作者：</font>** Yue Deng, Zirui Wang, Yin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> TD($\lambda$) in value-based MARL algorithms or the Temporal Difference critic learning in Actor-Critic-based (AC-based) algorithms synergistically integrate elements from Monte-Carlo simulation and Q function bootstrapping via dynamic programming, which effectively addresses the inherent bias-variance trade-off in value estimation. Based on that, some recent works link the adaptive $\lambda$ value to the policy distribution in the single-agent reinforcement learning area. However, because of the large joint action space from multiple number of agents, and the limited transition data in Multi-agent Reinforcement Learning, the policy distribution is infeasible to be calculated statistically. To solve the policy distribution calculation problem in MARL settings, we employ a parametric likelihood-free density ratio estimator with two replay buffers instead of calculating statistically. The two replay buffers of different sizes store the historical trajectories that represent the data distribution of the past and current policies correspondingly. Based on the estimator, we assign Adaptive TD($\lambda$), \textbf{ATD($\lambda$)}, values to state-action pairs based on their likelihood under the stationary distribution of the current policy. We apply the proposed method on two competitive baseline methods, QMIX for value-based algorithms, and MAPPO for AC-based algorithms, over SMAC benchmarks and Gfootball academy scenarios, and demonstrate consistently competitive or superior performance compared to other baseline approaches with static $\lambda$ values.

---


### 241. [Learning Subspace-Preserving Sparse Attention Graphs from Heterogeneous Multiview Data](https://arxiv.org/abs/2605.11881)

**<font color=#1a73e8>作者：</font>** Jie Chen, Yuanbiao Gou, Chuanbin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The high-dimensional features extracted from large-scale unlabeled data via various pretrained models with diverse architectures are referred to as heterogeneous multiview data. Most existing unsupervised transfer learning methods fail to faithfully recover intrinsic subspace structures when exploiting complementary information across multiple views. Therefore, a fundamental challenge involves constructing sparse similarity graphs that preserve these underlying subspace structures for achieving semantic alignment across heterogeneous views. In this paper, we propose a sparse attention graph learning (SAGL) method that learns subspace-preserving sparse attention graphs from heterogeneous multiview data. Specifically, we introduce a bilinear attention factorization scheme to capture asymmetric similarities among the high-dimensional features, which breaks the symmetry bottleneck that is inherent in the traditional representation learning techniques. A dynamic sparsity gating mechanism then predicts a feature-specific compression factor for adaptively controlling the topological contributions of neighbors. Furthermore, we employ a structured sparse projection via $\alpha$-entmax to generate subspace-preserving sparse attention graphs for individual views. SAGL leverages these view-specific graphs to conduct sparse information aggregation, yielding discriminative representations for multiview learning tasks. In addition, we provide a rigorous theoretical analysis that bridges differentiable sparse attention and probability simplex constraints. Extensive experiments conducted on multiple benchmark datasets demonstrate that SAGL consistently outperforms the state-of-the-art unsupervised transfer learning approaches.

---


### 242. [Sobolev Regularized MMD Gradient Flow](https://arxiv.org/abs/2605.11884)

**<font color=#1a73e8>作者：</font>** Chenyang Tian, Bharath K. Sriperumbudur, Arthur Gretton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Sobolev-regularized Maximum Mean Discrepancy (SrMMD) gradient flow, a regularized variant of maximum mean discrepancy (MMD) gradient flow based on a gradient penalty on the witness function. The proposed regularization mitigates the non-convexity of the MMD objective and yields provable \emph{global} convergence guarantees in MMD in both continuous and discrete time. A more surprising appeal is that our convergence analysis does not rely on isoperimetric assumptions on the target distribution. Instead, it is based on a regularity condition on the difference between kernel mean embeddings. A key highlight of the proposed flow is that it is applicable in both sampling (from an unnormalized target distribution) -- using Stein kernels -- and generative modeling settings, unlike previous works, where a gradient flow is suitable for only generative modeling or sampling but not both. The effectiveness of the proposed flow is empirically verified on a broad range of tasks in both generative modelling and sampling.

---


### 243. [From Clever Hans to Scientific Discovery: Interpreting EEG Foundational Transformers with LRP](https://arxiv.org/abs/2605.11885)

**<font color=#1a73e8>作者：</font>** Justus Meyer zu Bexten, Nico Scherf, Bogdan Franczyk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emerging foundation models (FMs) in electroencephalography (EEG) promise a path to scale deep learning in diagnostics and brain-computer interfaces despite data scarcity, yet their opaque nature remains a barrier to wider adoption. We investigate attention-aware Layer-wise relevance propagation (LRP) as a post-hoc attribution method for EEG-FMs, extending LRP's use on convolutional neural network (CNN)-based EEG models to the Transformer architectures that current FMs are based on. We find that LRP can both verify EEG-FM decisions and surface novel, biologically plausible hypotheses from them. In motor imagery, it unmasks 'Clever Hans' behavior where models prioritize task correlated ocular signals over the intended motor correlates. In a naturalistic paradigm for affect prediction, it reveals a recurring reliance on a central electrode cluster, suggesting a candidate sensorimotor signature of arousal. Though heatmap interpretation remains ambiguous in this complex domain, the results position LRP as a tool for both verification and exploration of EEG-FMs, a role that will grow in both importance and discovery potential as the underlying models mature.

---


### 244. [Incentivizing Truthfulness and Collaborative Fairness in Bayesian Learning](https://arxiv.org/abs/2605.11889)

**<font color=#1a73e8>作者：</font>** Rachael Hwee Ling Sim, Jue Fan, Xiao Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaborative machine learning involves training high-quality models using datasets from a number of sources. To incentivize sources to share data, existing data valuation methods fairly reward each source based on its data submitted as is. However, as these methods do not verify nor incentivize data truthfulness, the sources can manipulate their data (e.g., by submitting duplicated or noisy data) to artificially increase their valuations and rewards or prevent others from benefiting. This paper presents the first mechanism that provably ensures (F) collaborative fairness and incentivizes (T) truthfulness at equilibrium for Bayesian models. Our mechanism combines semivalues (e.g., Shapley value), which ensure fairness, and a truthful data valuation function (DVF) based on a validation set that is unknown to the sources. As semivalues are influenced by others' data, we introduce an additional condition to prove that a source can maximize its expected data values in coalitions and semivalues by submitting a dataset that captures its true knowledge. Additionally, we discuss the implications and suitable relaxations of (F) and (T) when the mediator has a limited budget for rewards or lacks a validation set. Our theoretical findings are validated on synthetic and real-world datasets.

---


### 245. [Proteus: A Self-Evolving Red Team for Agent Skill Ecosystems](https://arxiv.org/abs/2605.11891)

**<font color=#1a73e8>作者：</font>** Zhaojiacheng Zhou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills extend LLM agents with reusable instructions, tool interfaces, and executable code, and users increasingly install third-party skills from marketplaces, repositories, and community channels. Because a skill exposes both executable behavior and context-setting documentation, its deployment risk cannot be measured by single-shot audits or prompt-level red teams alone: a realistic attacker can use audit and runtime feedback to repeatedly rewrite the skill. We frame this risk as \emph{adaptive leakage} -- whether a budgeted attacker can iteratively revise a skill until it passes audit and produces verified runtime harm -- and present \ours{}, a grey-box self-evolving red-team framework for measuring it. Proteus searches a formalized five-axis skill-attack space. Each candidate is evaluated through a unified audit-sandbox-oracle pipeline that returns structured audit findings and runtime evidence to guide cross-round mutation. Beyond initial evasion, Proteus performs path expansion, which finds alternative implementations of successful attacks, and surface expansion, which transfers learned implementation patterns to new attack objectives beyond the original seed catalogue. Across eight phase-1 cells, Proteus reaches 40--90\% Attack Success Rate at $5$ rounds (ASR@5) with positive learning-curve slopes on both evaluated auditors. Phase-2 path/surface expansion produces 438 jointly bypassing and lethal variants, with SkillVetter bypassed at $\geq 93\%$ in every cell and AI-Infra-Guard, the strongest public auditor we evaluate, still admitting up to 41.3\% joint-success. These results show that current skill vetting substantially underestimates residual risk when evaluated against adaptive, feedback-driven attackers.

---


### 246. [Toward Modeling Player-Specific Chess Behaviors](https://arxiv.org/abs/2605.11893)

**<font color=#1a73e8>作者：</font>** Loris Sogliuzzo, Aloïs Rautureau, Eric Piette  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While artificial intelligence has achieved superhuman performance in chess, developing models that accurately emulate the individualized decision-making styles of human players remains a significant challenge. Existing human-like chess models capture general population behaviors based on skill levels but fail to reproduce the behavioral characteristics of specific historical champions. Furthermore, the standard evaluation metric, move accuracy, inherently penalizes natural human variance and ignores long-term behavioral consistency, leading to an incomplete assessment of stylistic fidelity. To address these limitations, an architecture is proposed that adapts the unified Maia-2 model to champion-specific embeddings, further enhanced by the integration of a limited Monte Carlo Tree Search (MCTS) process to enrich tactical exploration during move selection. To robustly evaluate this approach, a novel behavioral metric based on the Jensen-Shannon divergence is introduced. By compressing high-dimensional board representations into a latent space using an AutoEncoder and Uniform Manifold Approximation and Projection (UMAP), move distributions are discretized on a common grid to compare behavioral similarities. Results across 16 historical world champions indicate that while integrating MCTS decreases standard move accuracy, it improves stylistic alignment according to the proposed metric, substantially reducing the average Jensen-Shannon divergence. Ultimately, the proposed metric successfully discriminates between individual players and provides promising evidence toward more comprehensive evaluations of behavioral alignment between players and AI models.

---


### 247. [Few-Shot Synthetic Data Generation with Diffusion Models for Downstream Vision Tasks](https://arxiv.org/abs/2605.11898)

**<font color=#1a73e8>作者：</font>** Daniil Dushenev, Nazariy Karpov, Daniil Zinovjev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class imbalance is a persistent challenge in visual recognition, particularly in safety-critical domains where collecting positive examples is expensive and rare events are inherently underrepresented. We propose a lightweight synthetic data augmentation pipeline that fine-tunes a LoRA adapter on as few as 20-50 real images of a rare class and uses a pretrained diffusion model to generate synthetic samples for training.
We systematically vary the synthetic-to-real ratio and evaluate the approach across two structurally different domains: chest X-ray pathology classification (NIH ChestX-ray14) and industrial surface crack detection (Magnetic Tile Defect dataset). All evaluations are performed on held-out sets of real images only.
Across both domains, synthetic augmentation consistently improves rare-class recall and F1 compared to training with real data alone. Performance improves with moderate synthetic augmentation and shows diminishing returns as the synthetic ratio increases.
These results suggest that LoRA-adapted diffusion models provide a simple and scalable mechanism for augmenting rare classes, enabling effective learning in data-scarce scenarios across heterogeneous visual domains.

---


### 248. [Mobile Traffic Camera Calibration from Road Geometry for UAV-Based Traffic Surveillance](https://arxiv.org/abs/2605.11900)

**<font color=#1a73e8>作者：</font>** Alexey Popov, Natalia Trukhina, Vadim Vashkelis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicles (UAVs) can provide flexible traffic surveillance where fixed roadside cameras are unavailable, costly, or impractical. However, raw UAV video is difficult to use for traffic analytics because vehicle motion is observed in perspective image coordinates rather than in a stable metric road coordinate system. This paper presents a lightweight pipeline for converting monocular oblique UAV traffic video into a local metric bird's-eye-view (BEV) representation. Visible road geometry, including lane markings, road borders, and crosswalks, is used to estimate a road-plane homography from image coordinates to metric ground-plane coordinates. Vehicle observations from dataset annotations or detectors are then projected to BEV using estimated ground contact points. The resulting trajectories support estimation of vehicle direction, speed, heading, and dynamic 3D cuboids on the road plane. We evaluate the pipeline on UAVDT using ground-truth annotations to isolate calibration and geometric reconstruction from detector and tracker errors. For sequence M1401, 40 sampled frames from img000001-img000196 produce 632 metric cuboid instances across 23 tracks. Results show that road-geometry calibration can transform monocular UAV footage into interpretable traffic-camera-style analytics, including BEV tracks and synchronized 3D cuboid visualizations. They also reveal key limitations: far-field vehicles are sensitive to homography errors, manual validation is currently more reliable than fully automatic calibration, and the single-plane assumption limits performance in non-planar or ambiguous road regions. The proposed pipeline provides a practical foundation for deployable UAV traffic cameras and future real-time traffic digital-twin systems.

---


### 249. [AccLock: Unlocking Identity with Heartbeat Using In-Ear Accelerometers](https://arxiv.org/abs/2605.11901)

**<font color=#1a73e8>作者：</font>** Lei Wang, Jiangxuan Shen, Xi Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The widespread use of earphones has enabled various sensing applications, including activity recognition, health monitoring, and context-aware computing. Among these, earphone-based user authentication has become a key technique by leveraging unique biometric features. However, existing earphone-based authentication systems face key limitations: they either require explicit user interaction or active speaker output, or suffer from poor accessibility and vulnerability to environmental noise, which hinders large-scale deployment. In this paper, we propose a passive authentication system, called AccLock, which leverages distinctive features extracted from in-ear BCG signals to enable secure and unobtrusive user verification. Our system offers several advantages over previous systems, including zero-involvement for both the device and the user, ubiquitous, and resilient to environmental noise. To realize this, we first design a two-stage denoising scheme to suppress both inherent and sporadic interference. To extract user-specific features, we then propose a disentanglement-based deep learning model, HIDNet, which explicitly separates user-specific features from shared nuisance components. Lastly, we develop a scalable authentication framework based on a Siamese network that eliminates the need for per-user classifier training. We conduct extensive experiments with 33 participants, achieving an average FAR of 3.13% and FRR of 2.99%, which demonstrates the practical feasibility of AccLock.

---


### 250. [Beyond Point-wise Neural Collapse: A Topology-Aware Hierarchical Classifier for Class-Incremental Learning](https://arxiv.org/abs/2605.11904)

**<font color=#1a73e8>作者：</font>** Huiyu Yi, Zhiming Xu, Dunwei Tu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Nearest Class Mean (NCM) classifier is widely favored in Class-Incremental Learning (CIL) for its superior resistance to catastrophic forgetting compared to Fully Connected layers. While Neural Collapse (NC) theory supports NCM's optimality by assuming features collapse into single points, non-linear feature drift and insufficient training in CIL often prevent this ideal state. Consequently, classes manifest as complex manifolds rather than collapsed points, rendering the single-point NCM suboptimal. To address this, we propose Hierarchical-Cluster SOINN (HC-SOINN), a novel classifier that captures the topological structure of these manifolds via a ``local-to-global'' representation. Furthermore, we introduce Structure-Topology Alignment via Residuals (STAR) method, which employs a fine-grained pointwise trajectory tracking mechanism to actively deform the learned topology, allowing it to adapt precisely to complex non-linear feature drift. Theoretical analysis and Procrustes distance experiments validate our framework's resilience to manifold deformations. We integrated HC-SOINN into seven state-of-the-art methods by replacing their original classifiers, achieving consistent improvements that highlight the effectiveness and robustness of our approach. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-396](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
