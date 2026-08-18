# 📦 其他研究 | 2026年08月19日

> 本类共 **435** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

---

### 201. [From Contexts to Values: Context-Dependent Defeat in Abstract Argumentation](https://arxiv.org/abs/2608.15536)

**<font color=#1a73e8>作者：</font>** Albert Sadowski, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In value-based argumentation, an audience's ordering of values decides which attacks succeed as defeats. In many settings the deciding factor is not the audience but the circumstances: the same attack may succeed at one procedural stage, or under one regulation, and fail at another. Context-dependent argumentation frameworks (CDAFs), a model we recently introduced, capture this directly: one set of arguments, one attack relation, and a defeat function that switches each attack on or off per context, so every context induces an ordinary Dung framework. This raises a reduction question: is context genuinely new, or can one value assignment with per-context orderings reproduce the defeat function, collapsing the CDAF into a VAF? We present a polynomial-time decision procedure for this question and map the harder neighbouring problems, with upper bounds from NP to $\Sigma^p_3$. We also present a validated reference implementation and a measurement: representability is rare and falls fast with the number of contexts.

---


### 202. [EA-LiteUNet: An Edge-Adaptive and Resource-Efficient U-Net for Boundary-Sensitive Dermoscopic Image Segmentation](https://arxiv.org/abs/2608.15537)

**<font color=#1a73e8>作者：</font>** Wang Jiangtao, Nur Intan Raihana Ruhaiyem, Fu Panpan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate boundary delineation remains a persistent challenge in dermoscopic image segmentation because of blurred lesion margins, heterogeneous textures, and complex background artifacts. From a signal-processing perspective, lesion boundaries represent high-frequency components that are highly susceptible to aliasing, noise amplification, and information loss. Consequently, repeated downsampling and feature transformations in conventional convolutional architectures often lead to severely degraded boundary representations. To address these limitations, we propose EA-LiteUNet, an edge-adaptive and computationally efficient U-Net variant specifically designed for boundary-sensitive medical image segmentation. The architecture integrates three core mechanisms: (1) boundary-aware representation learning to suppress aliasing and preserve high-frequency structural details; (2) attention-guided feature modulation to selectively enhance boundary-relevant responses across multi-scale features; and (3) a resource-adaptive inference strategy to dynamically balance segmentation accuracy and computational efficiency. Extensive evaluations across three public dermoscopic datasets demonstrate that EA-LiteUNet consistently achieves superior boundary precision. Specifically, on the ISIC 2018 dataset, the method significantly reduces the 95% Hausdorff Distance (HD95) to 12.89 pixels while maintaining a robust Dice score of 92.08%. Notably, this strong performance is achieved with an ultralightweight configuration of merely 0.29M parameters and 1.17 GFLOPs. Ablation studies further validate the complementary effects of these components, confirming their contribution to enhanced boundary fidelity and stable optimization.

---


### 203. [Spectral Saliency for Machine Unlearning](https://arxiv.org/abs/2608.15548)

**<font color=#1a73e8>作者：</font>** Cedar Site Bai, Amber Yijia Zheng, Raymond A. Yeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning (MU) aims to remove the influence of specific training data while preserving model utility. As the name suggests, MU can be viewed as the inverse of learning, using gradient-based updates to reduce the influence of a forget-set by counteracting the previously learned behavior. Recently, Muon, a gradient descent variant, has been introduced. Muon applies spectral magnitude normalization to encourage exploration of rare directions and demonstrates promising performance. Inspired by Muon, we adopt the spectral view for unlearning and propose Spectral Saliency Unlearning (SSU). SSU thresholds weak singular components and updates only those directions supported by a confident unlearning signal. We further provide theoretical justification for this thresholding approach from the perspective of the forgetting-retention trade-off. Experiments across image classifiers, diffusion models, and LLMs demonstrate SSU's effectiveness.

---


### 204. [RigidBench: Evaluating Rigid-Body Physics in Video Generation Models](https://arxiv.org/abs/2608.15555)

**<font color=#1a73e8>作者：</font>** Swarnim Jain, Shangzhe Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video models are increasingly used to predict what happens next in a scene, yet the metrics commonly used to compare their outputs say little about whether the predicted objects move correctly. Motion, geometry, identity, background stability, and visual similarity can fail independently, but whole-frame scores often mix these errors together. We introduce RigidBench, a simulator-grounded benchmark that compares a generated continuation with a reference rollout from the same initial frame and motion description. Its five rigid-body tasks vary objects, materials, viewpoints, and indoor and outdoor scenes, with per-frame masks, depth, 6-DoF trajectories, and contacts available for scoring. We evaluate eight models on the same 100 examples with ten measurements that keep these aspects separate. The resulting rankings depend strongly on what is measured: no model leads on all ten, and across model means, higher SSIM accompanies larger 3D trajectory error (r = 0.89). RigidBench also includes 5,000 training videos with exact simulator state, which we use to fine-tune and analyze Wan 2.2 TI2V-5B. Full fine-tuning reduces 3D trajectory error by about 20% with almost no change in SSIM, while teacher-forced probes and targeted interventions show that object position is represented throughout Wan's diffusion transformer and used by its denoising computation.

---


### 205. [Amortised Post-Hoc Explanation with Exact Preservation for Dynamic Graph Anomaly Detectors](https://arxiv.org/abs/2608.15559)

**<font color=#1a73e8>作者：</font>** Iyad Assaad Nekka, Hamida Seba, Walid Khaled Hidouci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection in dynamic graphs underpins financial fraud analysis, intrusion detection, and platform integrity, where automated decisions require human-interpretable justifications. StrGNN, the strongest performer in recent benchmarks, produces no explanation: when an edge is flagged, the analyst receives only a score. Explanation metrics are undefined for StrGNN because no attribution vector exists. This paper closes that gap. We present X-StrGNN, a post-hoc explanation layer that wraps a trained, frozen StrGNN and emits, for every flagged edge, dual attributions: a structural attribution identifying which contextual interactions in the enclosing subgraph drove the decision, and a temporal attribution identifying which historical snapshot carried the signal. Both attributions are multiplicative masks identically one in the unexplained pass, so the layer is an exact pass-through: detection is preserved to machine precision, verified rather than asserted (Delta AUC = 0.0000, Delta AP = 0.0000, Delta P@100 = 0.0000). Attribution costs 0.66 ms per edge, making explanation of an entire alarm list feasible. We conduct the first controlled design study of attribution strategies for this architecture, comparing gradient attribution, per-instance mask optimisation, and amortised parameterisation under one protocol, one budget, and three seeds. X-StrGNN attains the highest stability (0.913) at 268x lower cost than per-instance optimisation, and its temporal attribution (1.601 against a measured random floor of 0.973) is separably better than its ablated control, while per-instance optimisation - the most expensive strategy - falls below that floor. Code, protocol, and per-seed measurements are released.

---


### 206. [PoseAdapter: Dual-Stream 2.5D Controllable Image Generation for Complex Multi-Object Scenes](https://arxiv.org/abs/2608.15583)

**<font color=#1a73e8>作者：</font>** Yufeng Chi, Huimin Ma, Fan Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Text-to-Image (T2I) diffusion models have achieved remarkable success, precise spatial and orientational control in multi-object scenes remains a persistent challenge. Existing methods either rely on computationally expensive dense 3D maps or suffer from severe attribute leakage and "cut-and-paste" artifacts. To address these limitations, we propose PoseAdapter, a lightweight framework for high-fidelity 2.5D controllable image generation. Instead of dense spatial maps, it establishes precise spatial-angular anchors using an efficient condition layout: individual object captions, 2D bounding boxes, and 3D angles. To resolve the generative trade-off between strict instance isolation and global coherence, we introduce a Context-Aware Dual-Stream Representation. By injecting local object tokens and relation-enriched scene tokens into the visual stream of modern MM-DiT architectures via parallel masked and unmasked pathways, PoseAdapter eliminates attribute leakage while preserving natural inter-object relationships and scene-level coherence. To support this paradigm, we construct OrientLayout, a high-quality dataset featuring standardized 2.5D annotations and instance-level decoupled semantics. Extensive experiments demonstrate that PoseAdapter outperforms state-of-the-art baselines in spatial accuracy, orientational precision, and multi-object visual fidelity. Code and dataset will be available at this https URL.

---


### 207. [Quantum Models with Multi-Stage Training for Compositional Concept Generalization](https://arxiv.org/abs/2608.15601)

**<font color=#1a73e8>作者：</font>** Mina Abbaszadeh, Matilda Karabina Moore, Mehrnoosh Sadrzadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compositional Concept Generalization (CoCoGen), the ability to systematically recombine learned primitives in novel contexts, is a key challenge for multimodal learning. In this work, we provide a solution using a compositional model of meaning that separates nouns from relations and uses tensors and variational quantum circuits to train them on data. This model enables us to employ a multi stage training paradigm, one that first learns object representations from single-object image-caption pairs, then subsequently transfers these to the relational stage where object parameters are frozen and optimisation is only applied to relational components. This design explicitly enforces compositional factorisation at the circuit, ensuring that relations are learned as transformations over stable primitives. The training paradigm is tested on the CLEVR dataset developed specificially for CoCoGen. For text, we work with vector representations of nouns and higher order tensor representations of relations using a set of different ansatz. For images, we work with quantum encodings of image embeddings dervied from Open AI's Vision Language tool CLIP and contrast amplitude encoding, which preserves the original embedding geometry, with angle encoding, which introduces nonlinear feature transformations. Our results show that multi-staged training combined with structured encodings significantly improves out of distribution relational generalisation, while using orders of magnitude fewer trainable parameters than classical baselines. We find that performance gains arise from the interaction between representation and encoding, with nonlinear quantum encodings enhancing the separability of compositional structure. These findings demonstrate that structured quantum representations and staged learning provide an effective framework for compositional generalisation in multimodal quantum machine learning.

---


### 208. [Benchmarking Quantum Machine Learning for Power-System Attack Detection: Evaluation Choices Decide the Outcome Before the Models Do](https://arxiv.org/abs/2608.15617)

**<font color=#1a73e8>作者：</font>** Md Rezwanul Islam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning detectors for power-system cyberattacks are themselves attack surfaces, and quantum machine learning has been proposed for them. We benchmark fidelity-kernel SVMs and variational classifiers against six tuned classical models on public power-system attack data (Mississippi State/ORNL), across white-box, transfer, decision-based black-box, and poisoning attacks. Our headline finding is methodological: the benchmark's answers are set by the evaluator's choices before the models. Eight choices -- six in the evaluation protocol, two in the tuning the benchmark itself runs -- each reversed or moved a conclusion at fixed models. The largest is the split: the row-level protocol scores 0.905 macro-F1 where holding whole source files out leaves 0.594, and in the capped matched-dimensionality regime the quantum arm sits within noise of chance with the classical arm 0.024 above it. A fidelity kernel looks most robust until attacked directly (retention 0.886 to 0.064); a mis-fitted surrogate manufactures a 10x asymmetry; an unseeded black-box attack moves 75% between restarts. A positive control explains the accuracy null: the labels, not the pipeline. We give the control that catches each choice and release the seeded benchmark.

---


### 209. [Bias-Corrected Ceilings of Emotion Predictability from Human Label Variation Based on Instance-Level Fano Bounds](https://arxiv.org/abs/2608.15619)

**<font color=#1a73e8>作者：</font>** Keito Inoshita  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotion recognition from text keeps improving on benchmarks, yet whether an accuracy ceiling has been reached is seldom asked with discipline. Our aim is not to pin this ceiling to a single number, but to quantify how far it depends on finite annotation, estimator choice, annotation noise, and the evaluation protocol, and thereby to discipline how confidently saturation can be claimed. We propose Bias-corrected Affective Ceiling Estimation (BACE), an analysis framework that estimates a bias-corrected ceiling, separates irreducible from reducible error, and disciplines the resulting claims. An anchored Dirichlet-mixture empirical Bayes estimator, bracketed between plug-in and NSB, recovers the human-consensus distribution; an annotator split, a noise deconvolution, and a fixed claim gate then attribute error without circularity. Methodologically, unconstrained point estimates place reachability anywhere from 0.38 to 1.03, so saturation cannot be decided by any single estimator. Substantively, the only assertion passing the claim gate is that at least about 33% of a representative classifier's error on GoEmotions is irreducible, with the same pattern recurring on offensiveness and irony.

---


### 210. [Rotation-Invariant Multi-IMU Activity Recognition under Independent Per-Location Orientation Shifts](https://arxiv.org/abs/2608.15621)

**<font color=#1a73e8>作者：</font>** Seungyeol Baek, Yoonbyung Chai, Yonghyeon Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human Activity Recognition (HAR) with self-administered wearables, such as at-home rehabilitation and exercise monitoring, often requires reattaching inertial measurement units (IMUs) across sessions. In multi-IMU settings, this can induce independent orientation offsets across body locations, a deployment shift that conventional scalar HAR models do not structurally handle. Existing remedies rely on rotation augmentation, whose robustness depends on sampled transformations, or calibration and orientationnormalization pipelines requiring additional reference-frame assumptions or explicit procedures. We present Truly Rotation-Invariant HAR (TRI-HAR), a rotation-invariant framework that makes robustness to independent per-location IMU orientation offsets a structural model property. TRI-HAR reshapes accelerometer and gyroscope streams into triaxial vectors, applies a shared SO(3)-equivariant backbone and invariant projection to each IMU location, and fuses the resulting invariant features for activity classification. Across four multi-IMU benchmarks, TRI-HAR preserves macro-F1 under fixed independent per-location SO(3) rotations and outperforms rotation-augmented baselines under this target shift without requiring rotational augmentation.

---


### 211. [In Defense of OCTA: The Reconstruction-Utility Gap in OCT-to-OCTA Synthesis](https://arxiv.org/abs/2608.15626)

**<font color=#1a73e8>作者：</font>** Michael Chertok, Alon Tiosano, Orly Gal-Or 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optical coherence tomography angiography (OCTA) images retinal blood flow, giving capillary-perfusion and foveal-avascular-zone biomarkers that grade diabetic-retinopathy ischemia. Because OCTA hardware is less common than structural OCT, recent work synthesizes it from OCT, reporting strong reconstruction (3D PSNR > 31 dB, SSIM > 0.9). We ask not whether the synthetic image looks similar, but whether it supports the measurements OCTA is acquired for. A frozen real-OCTA segmenter, applied as a probe to two synthesizers (XOCT, TransPro), shows downstream Dice falling with structural fineness: large vessels survive (0.862 -> 0.831) while the fine capillary network collapses (0.798 -> 0.635, five times the large-vessel loss; paired Wilcoxon p < 1e-3), TransPro worse throughout. A matched-blur control shows this detail is fabricated, not blurred. Retrained on a private Spectralis dataset, neither synthesizer reproduces the neovascular lesion (qualitative, n=3). Reconstruction fidelity is not clinical utility; we establish downstream-task fidelity as the evaluation OCT-to-OCTA synthesis needs.

---


### 212. [Sparse Prototype Code Underlies Classification and Prediction Across Modalities](https://arxiv.org/abs/2608.15632)

**<font color=#1a73e8>作者：</font>** Yehonatan Avidan, Daniel D. Lee, Haim Sompolinsky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural representations have become a central tool for studying the internal mechanisms of modern AI models, yet their complex high-dimensional structure makes them difficult to interpret. We show that classification tasks give rise to a universal representational geometry, shared across state-of-the-art models in vision, audio, and language processing. The key structure is that within-class variability is not random in representation space. Instead, its classifier-relevant component has strong and structured correlations with the class's own centroid and with the centroids of its competing classes. Building on this observation, we derive an analytical mean-field theory governed mainly by the variability along true-class and rival-class centroid coordinates, together with a global renormalization of the class radius that compensates for the non-Gaussian statistics of real representations. The theory accurately predicts classification accuracy across architectures and modalities. The relevant geometric quantities improve systematically with model scale, mirroring the observed gains in accuracy. A striking feature of the theory is its sparsity: accurate prediction requires only a small set of centroid coordinates associated with the true class and its strongest rivals - connecting our framework to sparse-feature extraction approaches such as sparse autoencoders. Together, these results provide a parsimonious predictive theory of neural representations and suggest that classification in deep networks is governed by a sparse, centroid-aligned structure embedded within the full high-dimensional representation space.

---


### 213. [A contribution to the critique of blockchain censorship](https://arxiv.org/abs/2608.15640)

**<font color=#1a73e8>作者：</font>** Ruichao Jiang, Michelle Yeo, Long Wen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study the blockchain censorship attack introduced in [21], which shows that joining the attack is a dominant strategy. We show that, by introducing certain detectability threshold, joining the attack can lead to strictly less reward for whales, which are defined to be a small number of validators that hold significantly more voting power than the rest (henceforth known as minnows). This leads to a change of the equilibrium: With whales unwilling to participate in the attack, it is difficult for minnows alone to launch the attack. We also perform Monte Carlo simulation to show the existence of reduction for whales' reward in Ethereum and Solana.

---


### 214. [Wiktionary as a Crowdsourced Lexicon for English Dialects](https://arxiv.org/abs/2608.15641)

**<font color=#1a73e8>作者：</font>** Sidney Wong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper evaluates Wiktionary as an ethically crowdsourced lexicon for English dialects. We took a two-phase approach, providing an in-depth descriptive analysis of the crowdsourced lexicon for 12 national varieties of English before applying the lexicon to geo-referenced, country-level social media language data to examine the real-world performance of this crowdsourced dialect lexicon. We demonstrate that Wiktionary matches or exceeds the coverage of traditional dictionaries, such as the Oxford English Dictionary (OED), for regional and Outer-Circle varieties. Our dialect-specific case study on New Zealand English found high alignment between Wiktionary and the OED based on word-formation patterns (R = 0.883). Similarly, we observed high alignment between the dialect lexicon and geo-referenced social media language. While this paper found that Wiktionary has broad coverage of lexical properties, it also highlighted some of the macro-challenges involved in evaluating dialect-responsive language resources and tools, such as the role of language contact in dialects and register effects in web-based corpora.

---


### 215. [When Time Meets Space: Entropy Integration and Dynamic Threshold for Adaptive DDoS Detection in SDN](https://arxiv.org/abs/2608.15642)

**<font color=#1a73e8>作者：</font>** Zhaoyang Zhang, Shen Wang, Ahmad Taha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Entropy-based Distributed Denial of Service (DDoS) detection in Software-Defined Networking (SDN) commonly relies on spatial traffic distributions and static or loosely adaptive thresholds, making it vulnerable to legitimate traffic fluctuations in Internet of Things (IoT) environments. This paper proposes a lightweight spatiotemporal entropy-based detector for DDoS attacks. Spatial entropy is computed from dynamically selected traffic attribute pairs, while temporal entropy captures the randomness of packet inter-arrival times. The two normalized entropy measures are fused into a unified indicator and evaluated using a constrained second-order Exponentially Weighted Moving Average threshold that jointly tracks entropy trend and volatility. To prevent attack-contaminated observations from biasing threshold adaptation, threshold updates are performed only for windows classified as normal. Testbed results show 99.26% recall, a 0.9737 F1-score, and a 3.2% false positive rate (41.74% below that of spatial entropy alone). On CICDDoS2019, the method achieves an FPR of 0 and remains competitive with machine-learning-based methods. It requires 3.95 ms of core processing per window and 11.65% system-wide CPU utilization, supporting resource-constrained edge and IoT deployment.

---


### 216. [Generalised Transportability via Causal Abstractions](https://arxiv.org/abs/2608.15645)

**<font color=#1a73e8>作者：</font>** Yorgos Felekis, Paris Giampouras, Fabio Massimo Zennaro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transporting a causal conclusion from a source study population to a target one is a fundamental problem in causal inference. The theory of transportability provides a criterion for when this is possible: given experimental data from the source and observational data from the target, it determines whether a target query is identifiable and does so completely; i.e. if the query can be transported, the criterion finds the exact formula. However, it works one query at a time and returns an expression rather than the value itself. It is also silent in two practically important regimes: when the query is not transportable and when no target data exist at all. To tackle both, we take a model-level perspective grounded in Causal Abstraction theory. Source and target share variables, graph, and interventions, differing only at a known set of mechanisms, which makes transportability a special case of same-level abstraction. Thus, instead of asking whether one query transports, we ask whether a single map aligns the source and target across their interventional behaviour. We characterise when such a map exists in both the Markovian and semi-Markovian settings; when it does, every target query transports at once. Our main contribution lies in the approximate case. When no exact map exists, the best approximate one still yields certified query intervals, recasting abstraction error as a quantitative notion of approximate transportability. We formulate model-level transport as distributionally robust optimisation over mechanism and environment perturbations of the unseen target and derive certificates for both challenging regimes: bounds for non-transportable queries, and guarantees under target-agnostic settings. We evaluate our framework on synthetic Markovian and semi-Markovian benchmarks and a real ecological dataset, and we show that the certified intervals bracket the true interventional query.

---


### 217. [Situated Practice Systems: A Computational System for Supporting the Coaching and Practice of Regulation Skills for Innovation Work](https://arxiv.org/abs/2608.15646)

**<font color=#1a73e8>作者：</font>** Kapil Garg, Darren Gergle, Haoqi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Students are increasingly expected to prepare for open-ended innovation work, which requires well-developed cognitive, metacognitive, and emotional regulation skills. College learning environments offer opportunities to work on real-world problems--such as in design and engineering--but students often remain unaware of their ineffective work practices and recurring regulation challenges, and may struggle to improve. Coaching from experts can help, but students' practices and regulation behaviors are largely invisible from work artifacts alone and are difficult to diagnose and track without computational support. We introduce Situated Practice Systems (SPS), which provide: (1) an Interactive Context-Assessment-Plan (CAP) Notes tool to support coaches' understanding and modeling students' regulation-informed practices, and (2) Practice Agents that help students develop more effective practices. SPS uses Practice Objects to represent practices and regulation behaviors computationally, and Practice Scripts to automatically present suggested practices to students in relevant situations. In a formative 3-week field study, SPS helped coaches identify recurring regulation gaps and provide tailored practices. SPS also guided students in adopting more effective ways of working on their own and with others. We demonstrate how CSCW systems and learning environments can be designed to support the development of students' work practices and regulation skills, enabling them to lead innovation work.

---


### 218. [Hierarchical Adaptive Feature Refinement Network for VHR Remote Sensing Image Segmentation](https://arxiv.org/abs/2608.15647)

**<font color=#1a73e8>作者：</font>** Shuaishuai Cao, Meng Tang, Shuwei Peng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation of very-high-resolution (VHR) remote sensing imagery increasingly benefits from strong pretrained hierarchical encoders, yet exploiting their multi-stage representations remains difficult. Nearby regions demand different balances between fine detail and semantic context, aggressive task-specific transformations perturb useful pretrained features, and conventional semantic supervision provides limited structural guidance. We present HAFR-Net, a progressive refinement framework that adaptively organizes and conservatively refines hierarchical representations instead of replacing them with a monolithic decoder transformation. Heterogeneity-Guided Stage-Adaptive Fusion (HG-SAF) predicts dense stage weights conditioned on local feature variation. A Frequency-Residual Adapter (FRA) then injects frequency information through a bounded, zero-initialized residual branch that keeps the fused representation as its reference. A Confusion-Aware Tri-Prior Decoder (CATP) finally regularizes the prediction with boundary, objectness, and training-derived class-relation cues. Under a matched Swin-B training and single-scale inference protocol, HAFR-Net attains 84.12%, 87.86%, 55.17%, and 67.70% mIoU on ISPRS Vaihingen, ISPRS Potsdam, LoveDA, and OpenEarthMap, improving the matched UPerNet baseline by 0.55, 0.95, 1.55, and 1.84 percentage points, respectively. Controlled analyses further show consistent spatial reweighting beyond content-only routing, improved boundary and thin-structure accuracy over matched spatial and spectral alternatives, and reduced confusion on pre-declared class pairs.

---


### 219. [Gaussian-JEPA: Joint-Embedding Predictive Learning for 3D Gaussian Splats](https://arxiv.org/abs/2608.15651)

**<font color=#1a73e8>作者：</font>** Bin Ren, Qi Ma, Yue Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) represents 3D content with anisotropic primitives that jointly encode geometry and appearance. Fixed-budget encoders consume sampled observations of Gaussian assets, so the same object may be observed through different primitive realizations. Existing self-supervised methods mainly reconstruct masked Gaussian attributes, tying supervision to one sampled realization and requiring an input-space decoder. Latent prediction offers an alternative, but its application to Gaussian tokens requires targets that accommodate coupled attributes and heterogeneous spatial support. We introduce Gaussian-JEPA, which predicts representations of held-out Gaussian token blocks from visible context. An online encoder processes the context, while a shared exponential-moving-average encoder supplies stop-gradient features for multi-scale targets. Complementary target projections and feature-space grounding provide latent supervision without reconstructing Gaussian attributes. We evaluate the features under Gaussian resampling, partial observations, and renderable shape completion, together with transfer to part segmentation and object classification. Compared with matched reconstruction pretraining, Gaussian-JEPA is more consistent across resampled inputs, retains more instance information under partial observations, and provides stronger frozen features for Gaussian completion. These results support latent prediction as an effective objective for reusable 3D Gaussian representations. Code is on the project page (this https URL).

---


### 220. [Scalable Black-Box Model Attribution for Images](https://arxiv.org/abs/2608.15652)

**<font color=#1a73e8>作者：</font>** Asaf Livne, Amir Jevnisek, Shai Avidan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of generative models raises the model attribution problem: given only an image, can we determine which model produced it? Existing methods have grown as elaborate as the generators they target, on the as- sumption that a more sophisticated model demands a more sophisticated attributor. We show it does not. RPA (Raw- Patch Attribution) attributes images in the strictest black- box setting with a lightweight CNN. Despite its simplicity, it attributes more models at higher accuracy than prior work, reaching 98.0% on 25-class DRAGON and 92.9% on 27- class OpenFake; it is data-efficient and runs at a cost inde- pendent of the number of candidate models; and it stays ro- bust to the compression, blur, and resizing images undergo in the wild. Training for closed-set attribution yields a ver- satile feature extractor: the same representation recovers model lineage without supervision, flags and groups unseen generators, and admits new models through few-shot adap- tation rather than retraining.

---


### 221. [A Responsible Artificial Intelligence Framework for Groundwater Modeling](https://arxiv.org/abs/2608.15657)

**<font color=#1a73e8>作者：</font>** Chong Chen, Yulu Zhang, Qingxi Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid development and widespread application of artificial intelligence (AI) have sparked intense discussions on how to deploy responsible AI systems in a manner aligned with human values and ethical standards. Compared to fields like healthcare, energy, or finance, the application of AI in groundwater is relatively limited, and research on responsible AI is even more scarce. Taking the middle reaches of the Heihe River Basin as the study area, this paper proposes six Responsible AI principles: transparency, technical robustness, privacy governance, fairness, accountability, and sustainability. LSTM and Transformer time-series models are developed using multi-source hydrometeorological data, and validated via post-hoc interpretability, Monte Carlo simulation, and scenario analysis. The results show that Transformer outperforms LSTM in accuracy, robustness, and interpretability, demonstrating the operability and practical value of Responsible AI principles in groundwater prediction to support sustainable water management under climate change and human activities.

---


### 222. [WorldRover: A Scalable Synthetic Video Data Engine for World Exploration with Rich Annotations](https://arxiv.org/abs/2608.15659)

**<font color=#1a73e8>作者：</font>** Xiaojie Xu, Zhengyuan Lin, Runyi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning to generate or reconstruct explorable worlds requires video paired with more than RGB: camera motion, scene geometry, temporal correspondence and, for interactive models, control signals. Real capture can provide some of these signals, but dense geometry and long-range correspondence usually rely on estimation or specialised instrumentation. Rendering provides these quantities directly, yet existing synthetic resources rarely combine them on the same frames while also supporting controlled changes of viewpoint and appearance. We introduce WorldRover, a data engine for generating richly annotated, long-range explorations of artist-built environments. At its core, WorldRover-Engine is an Unreal Engine pipeline that executes and offline-renders minute-scale routes while preserving their full trajectories and scene geometry. The same exploration can be replayed from first-person, third-person, and 360 panoramic cameras under different environmental states. Using WorldRover-Engine, we construct WorldRover-10M, whose sequences pair RGB with metric depth, camera trajectories, and trajectory-derived action signals throughout each exploration. Third-person subsets additionally provide dense optical flow, long-range 2D/3D point tracks with visibility, and a character trajectory distinct from the camera trajectory. The engine can render a traversal from first-person, third-person and 360 panoramic viewpoints, under different environmental states or with a neutral white material, while preserving the route and scene geometry. WorldRover therefore turns long-horizon world exploration into a scalable data-generation problem, providing supervision for models that must build, maintain, and revisit coherent representations of an explorable world.

---


### 223. [Sequential Multimodal Evidence Optimization for Product Media Ranking in E-Commerce](https://arxiv.org/abs/2608.15662)

**<font color=#1a73e8>作者：</font>** Prasenjit Dey, Frank McIntyre, Arnab Sinha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On modern e-commerce stores, customers consume ordered slates of heterogeneous product media, such as images, videos, and 3D renders, before making purchase decisions. Existing media-ranking systems often optimize myopic engagement proxies such as clicks or dwell time, even though product media assets are cooperative informational components of the same item that together help customers find the information they need through sequential interaction. We present Sequential Multimodal Evidence Optimization (SMEO), a two-stage utility-guided framework for customer-oriented media sequencing. SMEO first learns a trajectory utility model from consumed media prefixes to estimate how ordered evidence helps customers reach a purchase decision, while mitigating position-bias and variable-depth imbalance in logged data. Recognizing that customer attention is a limited resource, it then trains an autoregressive ranking policy with survival-weighted reward-to-go that prioritizes the most decision-relevant information early, so customers can find what they need with less effort. By decoupling utility learning from policy optimization, SMEO enables stable offline learning from biased logs and post-hoc media attribution without explicit media-level labels. Evaluated offline on large-scale e-commerce sessions using doubly robust off-policy estimation, SMEO improves estimated conversion by 5.5% and helps customers reach a purchase decision with 15% fewer swipes than existing baselines.

---


### 224. [BASeg: Boundary-Aware Remote Sensing Segmentation with Structural Penalties](https://arxiv.org/abs/2608.15683)

**<font color=#1a73e8>作者：</font>** Yuexi Song, Kailai Sun, Zhuoyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation is a core computer vision task in the remote sensing field, accelerating advancements in ur- ban development, agriculture, ecology, water resources, and environmental monitoring. However, recent methods usually struggle to capture fine-grained object features and bound- ary details. Besides, current widely used datasets often lack city morphology diversity and segmentation on generative im- ages remains largely unexplored. To address these issues, we propose a Mahalanobis-Angle Boundary Loss (MABL) that explicitly enhances boundary and shape consistency. MABL jointly models structural importance and boundary orientation through Mahalanobis distance-based weighting and angle- aware penalty. It can be readily integrated into diverse seg- mentation architectures and consistently improves their accu- racy. Built upon MABL, we introduce BASeg, a boundary- aware remote sensing segmentation framework with Struc- tural Penalties. BASeg integrates a Global Visual State Space module (GSM) with a Cross-Feature Fusion module (CFM) to capture both long-range contextual dependencies and fine- grained local details. Additionally, we establish a global 10- city benchmark dataset (GCD-25k) to facilitate accurate build- ing and road segmentation. Extensive experiments on four remote-sensing benchmarks demonstrate that BASeg consis- tently outperforms existing methods, achieving up to a 2.8% improvement in mIoU while producing more accurate object boundary segmentation across diverse scenes. Moreover, integrating MABL into multiple existing segmentation archi- tectures consistently improves performance across datasets, demonstrating its robustness and broad applicability.

---


### 225. [Counterfactual Sensitivity Is Not Repairability: Auditing Replay Probes for Video Evidence](https://arxiv.org/abs/2608.15685)

**<font color=#1a73e8>作者：</font>** Rama AlHamidi, Rasul Khanbayov, Erchin Serpedin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tool-using video agents retrieve visual evidence before answering, but the final answer is not forced to depend on what was retrieved. The natural black box test is counterfactual: destroy the semantic content of the frames the agent retrieved and check whether the answer changes, against a matched sham that re-executes the identical pipeline on those same frames. We introduce CARVE, a black-box counterfactual probe that compares answer changes under matched SHAM and DESTROY replays. Across three independent k=3 runs on a frozen VideoExplorer-style agent, DESTROY changes the answer 29.3 percentage points more often than SHAM, yielding a large and reproducible aggregate effect. Question-level scores are less stable, and increasing the replay budget from k=3 to k=10 reduces ties but weakens the original zero-threshold routing policy. At k=3, CARVE selects 538 of 1,258 LVBench questions and improves accuracy by 3.26 points, with higher fallback yield than most matched random subsets. The score shows only a weak association with annotated temporal coverage, so CARVE is best understood as a routing signal rather than a direct grounding classifier. Our implementation is available at this https URL.

---


### 226. [Training-Free Long-Term Multi-Object Tracking for Sports Video Analytics](https://arxiv.org/abs/2608.15688)

**<font color=#1a73e8>作者：</font>** Tomasz Stanczyk, Seongro Yoon, Francois Bremond  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term multi-object tracking in sports remains challenging due to frequent occlusions, rapid camera motion, and repeated player reappearances. We introduce McByte++, a training-free tracking-by-detection framework that integrates lightweight mask propagation, conditional camera motion compensation, and online re-identification within a unified pipeline. Compared to its predecessor, McByte++ substantially improves runtime efficiency while enhancing identity preservation. On SoccerNet-tracking and SportsMOT benchmarks, McByte++ achieves up to +3.0 HOTA and +6.1 IDF1 improvements over the original McByte in the online setting, with further gains when combined with offline global association. Replacing heavy segmentation components and optimizing motion modeling yields up to an order-of-magnitude speed increase. All results are obtained without detector retraining or dataset-specific tuning. Code will be made available at this https URL.

---


### 227. [BERTopic-Virality Prioritisation: A Scalable Framework for Thematic and Comparative Analysis of COVID-19 and Monkeypox Misinformation on Twitter](https://arxiv.org/abs/2608.15691)

**<font color=#1a73e8>作者：</font>** Mkululi Sikosana, Sean Maudsley-Barton, Oluwaseun Ajao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Health misinformation circulating during pandemics can gain traction rapidly, creating harmful narratives that compete with public health guidance. Most topic-modelling pipelines treat engagement as an external outcome, limiting their ability to prioritise semantically coherent topics that are also rapidly diffusing. We introduce BERTopic-VP, a virality-prioritised topic-modelling framework that combines contextual embedding-based clustering (BERTopic) with a post hoc Virality Prioritisation (VP) layer. The pipeline is complemented by a two-stage hybrid misinformation detection module that fuses a supervised content-based classifier with an external verification signal derived from public-health knowledge bases. Applied to three benchmark datasets, COVID-19_FNIR, Monkeypox, and Constraint, the framework achieves strong classification performance, with F1 up to 0.950 and ROC-AUC up to 0.989, while identifying high-impact clusters under top 1%, 5%, and 10% VP thresholds. For datasets without native engagement metadata, prioritisation is based on a logistic propensity-to-spread score, used as an ordinal proxy for diffusion potential rather than a direct measure of engagement. The results show that integrating semantic structure, virality-aware ranking, and affective-linguistic profiling enables scalable and interpretable comparative analysis of misinformation across pandemics. The proposed framework supports monitoring-oriented early warning by surfacing low-volume but high-risk narratives for analyst review.

---


### 228. [Automated Fetal Brain MRI Biometry in Healthy and Pathological Cases](https://arxiv.org/abs/2608.15692)

**<font color=#1a73e8>作者：</font>** Ema Masterl, Tina Vipotnik Vesnaver, Nejc Šubič 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated biometric analysis of fetal brain MRI enables reproducible, observer-independent quantitative assessment, yet existing methods are often restricted to few measurements or evaluated only on healthy cases. We assemble and evaluate an automated biometric analysis pipeline that localizes 22 anatomical landmarks on NeSVoR-reconstructed 3D volumes and derives 11 clinically relevant measurements spanning supratentorial, ventricular, cerebellar, and midline structures. We compare two landmark localization models, H3DE-Net and SCN, on a heterogeneous cohort of 122 acquisitions (both healthy controls and range pathologies). Localization accuracy was assessed with a linear mixed-effects model, agreement with normative growth trajectories with calibrated centile charts, and diagnostic utility with a decision tree classifying VM severity. H3DE-Net achieved significantly lower localization error than SCN across all landmarks (mean 1.36 mm vs. 3.58 mm in HC and 1.90 mm vs. 4.13 mm in PC; p < 0.001), and outperformed a GA-based regression baseline in 7 of 11 measurements. H3DE-Net measurements yielded higher classification AUC in every diagnostic group, with the clearest advantage in separating healthy controls from VM. Decision tree thresholds for ventricular width fell near the clinical 10 mm and 15 mm cut-offs used to define and grade VM.

---


### 229. [RRFC: Recursive Refinement via Feedback Conditioning for Iterative Image-to-Image Generation](https://arxiv.org/abs/2608.15694)

**<font color=#1a73e8>作者：</font>** Kareem Hassani, Chaymaa Abbas, Hadi Al Mubasher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conditional image-to-image generators are single-shot: they map input features to an output in one forward pass and treat it as final, with no opportunity to improve on it. Although trained to produce the best possible result in one step, such a model leaves room for improvement if it can adaptively revise its own output over iterations. We propose Recursive Refinement via Feedback Conditioning (RRFC), a novel feedback-conditioning framework for iterative output refinement that teaches a model to adaptively revise its output by conditioning on a new signal, namely its most recent previous prediction, which is fed back as an auxiliary set of channels alongside the original input. This preserves the generator's core architecture while modifying its conditioning interface and, depending on the model family, its training or inference procedure, so RRFC can be attached to existing generators without redesign. We evaluate RRFC across six baselines spanning adversarial, equilibrium, and diffusion-based models and three paired image-to-image translation tasks. Across 18 architecture-task settings, RRFC yields seven Holm-corrected improvements, seven degradations, and four non-significant changes. The gains concentrate on reconstruction-fidelity and identity settings, while five of the seven degradations fall on the single semantic-layout task, where every model declines. These results indicate that feedback-based refinement helps when its objective overlaps with the evaluated property, and that its gains concentrate on the tasks where that overlap holds.

---


### 230. [Bitstream Action Recognition is Byte Modeling](https://arxiv.org/abs/2608.15695)

**<font color=#1a73e8>作者：</font>** Fangcheng Li, Chaoran Huang, Tianyi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional action recognition typically relies on successful pixel decoding of the bitstream. However, bitstream corruption during storage or transmission may cause severe visual artifacts or even decoding failure, posing a significant challenge to reliable action recognition. Bitstream Action Recognition (BAR) aims to overcome the dependency on decoding and the vulnerability to corruption. In this paper, we propose a novel BAR framework, Bitstream Recognition via Anchoring Corrupted Embeddings (BRACE). BRACE is a dual-branch byte-modeling architecture that treats a corrupted bitstream and its intact counterpart as two byte realizations of the same action. This guides the generation of rich and stable representations for robustness to corruption through Intact-Anchored Representation Alignment (IARA). The intact representation serves as a stable anchor, and the corrupted one is aligned to it at the embedding and decision levels under Unreliable-Anchor Suppression (UAS), entirely in representation space and without repairing the bitstream. To address the scarcity of corrupted bitstreams in practice, we introduce the Real-world Bitstream Corruption Simulator (RBCS), a four-parameter simulator that reproduces bit-flip and byte-loss errors arising in transmission and storage. Building on RBCS, we construct the first large-scale BAR dataset (BAR-D), which comprises the BAR-Stanford40 and BAR-PPMI subsets and spans diverse corruption types and severity levels. Finally, we build a large benchmark on BAR-D involving 14 action recognition methods from the pixel, compressed, and bitstream domains. Extensive experiments demonstrate that BRACE has superior robustness to bitstream corruption than all comparison methods. Ablation studies further validate the effectiveness of the proposed RBCS augmentation and IARA.

---


### 231. [Adaptive Mixing of Policies from Searching and Policies from Learning](https://arxiv.org/abs/2608.15700)

**<font color=#1a73e8>作者：</font>** Gavin B. Rens  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: Distillation of training targets generated thru search/planning has proven useful in reinforcement learning, but search can take exceedingly long. Objectives: Rather than perform search to the same depth every time (typically at a fixed period of steps), reduce the search depth proportionally to the quality of the policy network priors. Methods: We describe Flexer, an architecture that, for each step, mixes the policy from a neural network and the policy from Monte Carlo tree search. The mixing factor favors the MCTS policy as the policy imitation error of the network and the environment models' variance increases. Results: Flexer outperforms a version of AlphaZero (and DQN and ADP) for some experiments on three toy symbolic problems.

---


### 232. [PixelControl: Fine-Grained Condition Fidelity in Text-to-Image Diffusion](https://arxiv.org/abs/2608.15705)

**<font color=#1a73e8>作者：</font>** Xin Lin, Haodong Li, Zhifei Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable text-to-image diffusion models can often follow the global layout of spatial conditions, yet still violate fine-grained structures such as object boundaries, thin contours, and medium/small conditioned regions. This limitation is especially problematic for VAE-based latent diffusion, where spatial compression can weaken high-frequency and low-area condition signals. We propose PixelControl, a pixel-space controllable diffusion framework for fine-grained condition fidelity. Built on a PixelDiT-style backbone, PixelControl avoids the latent bottleneck and introduces two complementary designs. First, Structure-Aware Control Injection derives a condition structure map and uses it to strengthen injected control residuals around spatially sensitive regions. Second, Multi-Scale Pyramid Cycle Loss verifies generated images against condition-derived structures across multiple resolutions, balancing global layout consistency with local boundary and detail accuracy. PixelControl supports depth, segmentation, edge, and their combinations through modality-specific control branches with lightweight gated fusion. Experiments across depth, segmentation, and edge control show that PixelControl improves structural fidelity and visual quality over existing controllable generation methods, with especially strong gains on boundaries and medium/small conditioned regions. The project page can be found at: this https URL

---


### 233. [What You Ask is What You Ground: Bridging Question Intent to Temporal Evidence for Grounded VideoQA](https://arxiv.org/abs/2608.15708)

**<font color=#1a73e8>作者：</font>** Jinhwan Seo, Kyubeom Han, Jumin Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study a critical yet overlooked failure mode in Grounded Video Question Answering: question-invariant grounding, where models predict nearly identical temporal segments for different questions about the same video. We trace this behavior to two structural limitations in prior common designs: (i) modality isolation that fixes video representations before they receive question semantics, and (ii) weak question injection inside the grounding module. To address this, we propose GroundFormer, which conditions video features on question intent before localization via learnable communication tokens that mediate directed visuo-lingual interaction. On top of the question-conditioned features, a factorized MIL cross-attention couples answer selection with temporal evidence under candidate-level supervision, while Gaussian smoothing converts peaked attention into temporally coherent segments. We further introduce a hierarchical multi-modal contrastive loss that aligns video, question, and answer embeddings across a two-pass training pipeline. GroundFormer achieves state-of-the-art grounded VideoQA performance on NExT-GQA and STAR, substantially improving question-discriminative temporal grounding.

---


### 234. [YOLO26-RD: An End-to-End Road Damage Detection Network With Learnable Contrast Enhancement and Edge-Guided Downsampling](https://arxiv.org/abs/2608.15713)

**<font color=#1a73e8>作者：</font>** Sompote Youwai, Pawarotorn Chaipetch, Hathairat Samaikul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated pavement-distress detection is commonly framed as a small-object problem, motivating high-resolution P2/4 detection heads and lossless downsampling. We present YOLO26-RD, an end-to-end (NMS-free) detector built on YOLO26 with two lightweight novel modules (LearnableContrast, a 494-parameter differentiable analogue of CLAHE that adapts contrast per tile inside the network, and EdgeSPD, a Sobel-gated space-to-depth downsampler adding only 2 parameters over SPD-Conv), and we subject the design to a data-first audit on a 7,618-image road-survey dataset (alligator crack, linear crack, patching). The audit falsifies the small-object premise: 92% of instances are COCO-large, and linear cracks are extreme-aspect structures (median 10:1) whose difficulty is sensitivity, not localization. Guided by this analysis, we remove the P2 detection level while retaining P2 features in the fusion path, which improves mAP50 by 2.8 points over the full YOLO26-RD model and reduces epoch time by 8%. Trained from scratch at 640x640, our best screening configuration reaches 0.787 mAP50 on the validation split versus a 0.771 project baseline (a stock YOLO26-s of uncontrolled recipe), with the largest per-class gain on the rarest class (patching, 2.6 points over baseline; 9.4 over the unmodified YOLO26-RD control under an identical recipe). A failure-mode decomposition further attributes the residual error of the bottleneck class (crack, approximately 0.74 across all architectures tested) to train/validation distribution shift on crack orientation and length, sub-pixel crack width at 640x640, and label incompleteness, factors no architecture change can address. We argue that for pavement imagery, measurement-driven subtraction outperforms module accretion, and we release our audit protocol alongside the model.

---


### 235. [PLeDO: Pain Level Detection for Osteoarthritis from EMR Data](https://arxiv.org/abs/2608.15719)

**<font color=#1a73e8>作者：</font>** Yuhao Chen, Jiahao Cai, Nafiz Sadman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Osteoarthritis (OA) is a progressive chronic joint disease resulting in a breakdown of articular cartilage and bone when damaged joint tissues are not able to normally repair themselves. The aim of this pilot research study is to understand the pain severity for OA from patients' primary care Electronic Medical Records (EMR), both from the structured medical data and the unstructured chart note data using information extraction, natural language processing and machine learning techniques. We propose SPaDe, a Synonym-based Pain level Detection tool to categorize patients into having mild or moderate-to-severe pain to understand diagnosis and treatment methods based on only the pain related expressions in the unstructured chart note. Expressions are subjective, objective, and influenced by cultural background and demography which poses a difficult challenge. Therefore, we improve the model by incorporating the medication information from the structured EMR data and pain scale related information from the chart note to propose an integrated pain level detection tool for OA called PLeDO. With the help of human labeled gold standard data, we demonstrate that both SPaDe and PLeDO can detect mild and moderate-to-severe pain from the EMR data to analyze and potentially improve the quality of care in primary care setting.

---


### 236. [Anatomical and Physical Supervision for CT-less PET Attenuation Correction: BIC-MAC 2026 Challenge](https://arxiv.org/abs/2608.15721)

**<font color=#1a73e8>作者：</font>** Petros Chatzitoulousis, George K. Matsopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report describes our submission to the Big Cross-Modal Attenuation Correction (BIC-MAC) 2026 Challenge for CT-less PET attenuation correction through multimodal pseudo-CT synthesis. We build upon a standard nnU-Net architecture and combine anatomical and physical supervision to improve both pseudo-CT quality and downstream PET reconstruction. Anatomical supervision is introduced through a frozen TotalSegmentator feature extractor, anatomy-guided structural constraints and patch sampling, while physical supervision is achieved using a differentiable attenuation correction factor projection loss based on multi-angle attenuation projections. Furthermore, the network is initialized with pretrained weights obtained from training on the SynthRAD Challenge MR-to-CT dataset. Minimal architectural modifications are applied, while performance improvements are pursued across the nnU-Net pipeline, including preprocessing, plans, and supervision design, among other components. Our final submission demonstrates the effectiveness of combining anatomical supervision, attenuation physics, and efficient nnU-Net scaling for CT-less PET attenuation correction.

---


### 237. [Learning Auditable Classifier Models: Source-Disjoint Tree Ensembles](https://arxiv.org/abs/2608.15725)

**<font color=#1a73e8>作者：</font>** Srikumar Krishnamoorthy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive models in clinical and regulated settings must be accurate and fully auditable. Tree ensembles deliver strong accuracy on tabular data, but their sequential boosting couples structure discovery with coefficient estimation, making compact per-prediction auditing difficult. Interpretable alternatives impose structural constraints that limit expressiveness: generalized additive models typically restrict interactions to pairwise terms and post-hoc rule extractors produce overlapping rules that hinder compact interpretation. We introduce Residual Pattern Tree Ensemble (RPTE), a three-stage learning approach, that is built on three key principles: bounded feature budget, source disjointness, and separate coefficient estimation. Stage~1 builds a supervised symbolic feature vocabulary. Stage~2 grows shallow trees under a source-disjointness constraint, where each raw variable is allocated to at most one tree, and retains only the discovered tree structures. Stage~3 solves a single $\ell_1$-regularized logistic regression over leaf-region indicators, yielding jointly optimal sparse coefficients. This learning approach ensures that every prediction decomposes into an algebraic sum of named, non-overlapping rule contributions, enabling full auditability by design. Empirical evaluation on twelve clinical-domain binary classification benchmarks using repeated stratified 5-fold cross-validation shows that RPTE performs competitively against tuned opaque ensembles and interpretable baselines. RPTE reduces model inspection units by 9$\times$ to 87$\times$ relative to XGBoost and maintains lower audit complexity than EBM on all 12 datasets. RuleFit requires comparable or fewer inspection units on three datasets where its rule count is small, but without source-disjointness guarantees. The source code is available at \href{this https URL}{this https URL}.

---


### 238. [FirstDiff: One-Step Diffusion-Based Anomaly Detection for Multivariate Time Series via Initial Noise Prediction](https://arxiv.org/abs/2608.15727)

**<font color=#1a73e8>作者：</font>** Ali Boudaghi, Alireza Nemati, Hadi Zare  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently shown strong potential for multivariate time-series anomaly detection by learning the distribution of normal data through iterative denoising. Existing diffusion-based approaches, however, typically perform anomaly detection after completing the reverse diffusion process, relying primarily on the final reconstructed signal and overlooking informative representations produced during denoising. This design incurs substantial computational cost and limits the use of intermediate diffusion information for anomaly detection.
In this paper, we propose FirstDiff, a diffusion-based anomaly detection framework based on the observation that the predicted diffusion noise at the initial reverse-diffusion evaluation already contains sufficient information for accurate anomaly detection. FirstDiff models the statistical distribution of predicted diffusion noise under normal behavior using validation data, enabling anomaly inference from a single denoising-network evaluation rather than completing the reverse diffusion trajectory.
To model complex temporal and inter-sensor dependencies, FirstDiff employs a Diffusion Transformer as the denoising backbone. Extensive experiments on five public benchmark datasets demonstrate that FirstDiff achieves state-of-the-art performance while reducing diffusion inference from the full reverse trajectory to a single denoising-network evaluation.

---


### 239. [Identifying Confusion Trends in Concept-based XAI for Multi-Label Classification](https://arxiv.org/abs/2608.15731)

**<font color=#1a73e8>作者：</font>** Haadia Amjad, Ronald Tetzlaff  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep Neural Networks (DNNs) deployed in high-risk domains, such as healthcare and autonomous driving, must be not only accurate but also understandable to ensure user trust. In real-world computer vision tasks, these models often operate on complex images containing background noise and are heavily annotated. To make such models explainable, Concept-based Explainable AI (CXAI) methods need to be assessed for their applicability and problem-solving capacity. In this work, we explore CXAI use cases in multi-label classification by training two DNNs, VGG16 and ResNet50, on the 20 most annotated labels in the MS-COCO dataset (Microsoft Common Objects in Context). We apply two CXAI methods, CRP (Concept Relevance Propagation) and CRAFT (Concept Recursive Activation FacTorization), to generate concept-level explanations and investigate the overall evaluations. Our analysis reveals three key findings: (1) CXAI highlights learning weaknesses in DNNs, (2) higher concept distinctiveness reduces label and concept confusion, and (3) environmental concepts expose dataset-induced biases. Our results demonstrate the potential of CXAI to enhance the understanding of model generalizability and to diagnose bias instigated by the dataset.

---


### 240. [ES3D: Embedding Semantics into 3D Space for Component-Aware Editing](https://arxiv.org/abs/2608.15749)

**<font color=#1a73e8>作者：</font>** Xuancheng Jin, Rengan Xie, Jiayuan Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D editing methods have made notable progress in controllability, yet they remain limited in several important ways. Most approaches rely on text-driven editing, which struggles to express fine-grained visual changes intended by the user. Moreover, many methods require manually supplied 3D masks or introduce unintended changes to regions that should remain untouched. These limitations largely arise from the absence of fine-grained semantic understanding, making it difficult for existing models to retrieve or modify specific 3D components.
We introduce ES3D, a framework that embeds semantics directly into 3D space, enabling component-aware retrieval and editing of a 3D asset conditioned on multiple local reference images and optional text queries. We first construct a 3D semantic embedding by projecting multi-view semantic features into the voxelized space of the asset. We then perform 3D component retrieval by computing feature similarity between the 3D semantic embedding and the semantic embeddings of image or text queries. For editing, we employ a pretrained 3D generative model with an inpainting mechanism to modify the retrieved components guided by user-provided images while preserving the rest of the asset. Overall, ES3D is a 3D editing framework that retrieves editable regions based on semantic cues and uses multiple images as conditions. Extensive experiments demonstrate that ES3D produces geometrically consistent and semantically coherent edits, enabling robust image-based and text-assisted control for 3D editing.

---


### 241. [Beyond Independence: Learning Correlated Views for Variational Incomplete Multi-View Clustering](https://arxiv.org/abs/2608.15757)

**<font color=#1a73e8>作者：</font>** Zheming Xu, Aiyue Tang, Shidi Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incomplete multi-view clustering (IMVC) aims to uncover shared cluster structures from data with partially observed views. Although recent imputation-free methods based on variational inference demonstrate robustness to missing views, they commonly rely on a conditional independence assumption across views in the posterior aggregation stage, which fails to capture the inherently structured and potentially correlated nature of multi-view data. In this paper, we propose a variational framework that explicitly goes beyond this assumption by introducing a learnable cross-view correlation structure. Specifically, we explicitly model and learn correlations between views by utilizing the covariance structure of posterior estimation errors during aggregation. To facilitate robust and efficient learning, the correlation matrix is parameterized through a normalized Cholesky decomposition, ensuring positive definiteness and enabling the entire model to be trained jointly through a unified variational objective. Extensive experiments on multiple IMVC benchmarks demonstrate that our method consistently outperforms state-of-the-art approaches across diverse missing-view settings while introducing only a negligible number of learnable parameters. These results highlight the effectiveness of adaptive correlation modeling in variational IMVC, demonstrating the need to go beyond the independence assumption in IMVC. The code is available at this https URL.

---


### 242. [Provenance, Not Behaviour: A Serialisation Artifact in Edge-IIoTset and a Leakage-Free Benchmark for Precision-Agriculture Intrusion Detection](https://arxiv.org/abs/2608.15761)

**<font color=#1a73e8>作者：</font>** Mostafa M. Galal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Edge-IIoTset is the reference benchmark for machine-learning intrusion detection in the industrial Internet of Things, and results reported on it cluster above 99%. We show that much of that performance is not intrusion detection. The preprocessing recipe distributed with the dataset instructs researchers to one-hot encode seven categorical columns. Four of them separate attack from normal traffic with an accuracy of 1.0000 on their own, through the spelling of the placeholder written for an absent protocol field: the string "0" in the normal-traffic branch of the dataset build against "0.0" in the attack branch. The label is recoverable from a serialisation artifact encoding file provenance, with no network behaviour modelled, and separates every row of both curated subsets. Under 5-fold x 3-repeat cross-validation, five of six standard classifiers attain exactly 1.0000 +/- 0.0000 accuracy and the sixth attains 0.99998. Under a corrected protocol, naive Bayes falls by 0.3005 macro-F1 and the strongest model settles at 0.9503 +/- 0.0011. Label, ordinal and frequency encoding leak identically. Because the curated subsets also lack Modbus and per-device identity, we rebuild the benchmark from the raw captures under uniform parsing, producing AgriEdge: 1,276,122 rows, five devices with full attribution, and no column separating the classes above 0.0288. A leave-one-device-out sweep locates the generalisation boundary at the perception/actuation layer, where random forest falls from 0.9988 to 0.5083 balanced accuracy. Non-IID federated partitioning costs at most 0.0037 macro-F1, but a 20-round LoRaWAN training run costs 4.6 hours of uplink.

---


### 243. [TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity](https://arxiv.org/abs/2608.15767)

**<font color=#1a73e8>作者：</font>** Armin Steinhauser  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce TinyCast, an attention-free zero-shot forecaster that emits a predictive distribution from 146,505 parameters, on the premise that at this size the periodic structure of a context is worth computing rather than learning. A zero-parameter spectral detector supplies the dominant periods, the context is folded on their phase, and a dilated convolutional encoder and a block-autoregressive quantile decoder model the rest. It is smaller than every zero-shot entry on the GIFT-Eval board whose parameter count can be established. On probabilistic accuracy it defines the size-accuracy frontier. Among zero-shot entries declaring no test-data leakage it is the only one below 1.4M parameters that emits a predictive distribution, and every entry scoring better carries at least that budget. On Chronos-ZS and fev-bench every neural model ahead of it carries at least 28 times its parameters. Because the mixing path is convolutions and matrix multiplications only, it exports to static INT8 and forecasts end to end on an embedded device without per-signal fitting.

---


### 244. [Temporal Graph Prototype-conditioned Conformal Prediction for Fraud Detection](https://arxiv.org/abs/2608.15768)

**<font color=#1a73e8>作者：</font>** Xudong Chen, Shengbo Gong, Lu Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction (CP) provides distribution-free coverage guarantees and has emerged as a principled tool for uncertainty quantification. In edge-level fraud detection on temporal interaction graphs, where false positives and false negatives both carry substantial cost, such coverage guarantees are particularly appealing for risk-aware decision making. However, directly applying existing graph conformal predictors yields inefficient prediction sets due to two recurring properties of fraud data. Fraudulent interactions are often embedded in benign-dominated neighborhoods that dilute calibration signals, while extreme class imbalance leaves scarce labeled-fraud support in the calibration split and leads to overly conservative class-conditional thresholds. To address these issues, we propose ProtoCP, a conformal prediction framework for edge-level fraud detection on temporal graphs. ProtoCP improves calibration efficiency by focusing calibration on fraud-relevant subgraph context and producing more stable nonconformity scores under class imbalance and temporal drift. Specifically, it leverages learned prototypes to suppress benign-dominated noise in the calibration context and introduces a neighborhood-relative scoring mechanism with temporal score diffusion for stable class-conditional calibration. Experiments on four fraud benchmarks (YelpChi, S-FFSD, FTFD, and BankSim) show that ProtoCP achieves the target coverage with consistently smaller prediction sets than state-of-the-art baselines. Our codes are available at this https URL

---


### 245. [Learning Stock Trading Policies via Barycenter-Based Adversarial Inverse Reinforcement Learning](https://arxiv.org/abs/2608.15770)

**<font color=#1a73e8>作者：</font>** Arishi Orra, Himanshu Choudhary, Manoj Thakur  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing effective trading strategies using reinforcement learning remains challenging due to delayed and noisy rewards, poor exploration, and the difficulty of enforcing explicit risk constraints. In this work, we propose BRaG, a barycenter-based adversarial inverse reinforcement learning framework for stock trading that learns trading behavior from multiple heterogeneous expert strategies. BRaG aggregates expert demonstrations using a performance-weighted Wasserstein barycenter, yielding a stable pseudo-expert representation that captures shared structure across diverse trading styles. This representation is used to pretrain a trading policy via adversarial imitation learning, which alleviates unstable exploration during reinforcement learning. The pretrained policy is subsequently refined using reinforcement learning with true market rewards. To ensure risk-aware decision-making, BRaG incorporates control barrier functions that constrain action execution and regularize policy learning to satisfy drawdown limits. We evaluate the proposed approach on four major global equity markets, including the US, UK, Indian, and Taiwanese indices. Across all the markets, the proposed approach achieves stronger performance than both classical trading rules and recent deep reinforcement learning methods, while exhibiting more stable risk characteristics.

---


### 246. [Fast Simulation Algorithms for OLH using Binomial Modeling](https://arxiv.org/abs/2608.15778)

**<font color=#1a73e8>作者：</font>** Berkay Kemal Balioglu, Alireza Khodaie, M. Emre Gursoy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Optimized Local Hashing (OLH) is a widely used hash-based Local Differential Privacy (LDP) protocol, and simulation-based experimentation is the standard approach for evaluating OLH and OLH-based applications in research. However, the existing OLH simulations have $O(nd)$ computational complexity, where $n$ is the user population size and $d$ is the domain size, and can lead to significant execution times as $n$ and $d$ grow. In this paper, we propose two fast simulation algorithms for OLH (2-Binom and 3-Binom) grounded in Binomial modeling. Our key insight is that, for any domain value $v$, the total number of users whose perturbed reports support $v$ can be decomposed into a sum of two or three Binomial random variables. Using this insight, our algorithms reduce the simulation complexity to $O(n + d)$ without hurting statistical equivalence. In particular, we theoretically prove that both algorithms yield unbiased frequency estimations with variances identical to those of the original OLH simulations. Experiments on real-world datasets confirm that both approaches reduce execution times from several minutes to milliseconds, yielding significant speedups with no change in utility.

---


### 247. [RoofGS: Roofline-Guided End-to-End Acceleration of 3D Gaussian Splatting](https://arxiv.org/abs/2608.15785)

**<font color=#1a73e8>作者：</font>** Yang Luo, Yan Gong, Yongsheng Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables real-time novel-view synthesis but remains limited on GPUs at high resolutions. Through a stage-wise Roofline characterization, we identify two distinct hardware bottlenecks: global memory traffic dominates the front end, whereas instruction throughput limits rasterization. Guided by this analysis, we develop RoofGS, a rendering framework that applies bottleneck-specific optimizations rather than generic kernel acceleration. For the memory-bound front end, we design a resolution-adaptive quantized depth sorting key that compresses each key to 32 bits. For the compute-bound rasterizer, we introduce a range-aware bit-level fast exponential approximation tailored to the bounded exponent range after opacity culling, with a derived per-pixel error bound. These two core techniques are complemented by additional optimizations (kernel fusion, compact attribute storage, culling, dual-pixel evaluation) that additionally reduce memory traffic and improve instruction-level parallelism. Experiments show that RoofGS achieves a 10.1$\times$ end-to-end speedup over 3DGS at 4K on an RTX 4090, increasing throughput from 61 to 616 FPS, with only a 0.028 dB PSNR loss.

---


### 248. [ChainSpace: A Chained-Reasoning Paradigm for Spatial Intelligence](https://arxiv.org/abs/2608.15788)

**<font color=#1a73e8>作者：</font>** Xiaohan Zhang, Feng Gu, Xudong Rao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence requires foundation models to maintain coherent spatial state across interactions with the physical world. However, existing data-centric approaches typically treat spatial reasoning as independent question-answer instances, enabling shortcut-based answering and providing limited supervision for persistent spatial understanding. To address this, we introduce ChainSpace, a chained-reasoning paradigm that structures spatial reasoning as a state-preserving multi-round process. In this paradigm, spatial questions are organized into logically constrained and jointly consistent chains, where later questions depend on spatial constraints established in earlier rounds. Following this principle, we instantiate ChainSpace-Bench, a manually annotated real-world multi-round benchmark with a Chain-Aware Metric, and ChainSpace-Pipeline, a simulator-based chain-structured supervision generation framework for spatial intelligence training. Experiments show that ChainSpace-Bench exposes chain-level failures that are not captured by isolated question accuracy. Additionally, with a relatively small amount of simulator-generated chained data, models trained by ChainSpace-Pipeline achieve the best performance among open-source models on ChainSpace-Bench and transfer competitively to multiple external spatial intelligence benchmarks. These results establish ChainSpace as an effective paradigm for more faithful evaluation and more data-efficient learning of spatial intelligence.

---


### 249. [CrevasseSeg: A Label-Efficient UAV Crevasse Segmentation Framework](https://arxiv.org/abs/2608.15790)

**<font color=#1a73e8>作者：</font>** Steven Wallace, William D Harcourt, Richard Hann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Crevasse mapping from uncrewed aerial vehicle (UAV) imagery matters for glaciological research and for field safety in glaciated terrain. Yet, pixel-level annotation of glacier surfaces is costly and requires domain experts. We introduce CrevasseSeg, a framework for binary segmentation over the terminus of Borebreen, Svalbard, comprising 1,938 unlabelled UAV orthomosaic tiles for self-supervised/unsupervised fine-tuning, 24 labelled tiles for validation and 176 labelled tiles for testing. Using CrevasseSeg, we benchmark five self-supervised objectives -- BYOL, a Jensen-Shannon Divergence (JSD) objective, Barlow-Twins, VICReg, and a combined BYOL-JSD objective -- across three architectures: O-Net, O-Net++, and a DINOv3-initialised O-Net. Each configuration is evaluated under two frozen-feature readouts that differ only in the form of their decision boundary: a linear probe and a non-linear XGBoost classifier fit only on the 24 labelled validation images. Our central finding is a consistent inversion between the two readouts: DINOv3 features are the weakest under linear probing but the strongest under a non-linear readout. A UMAP analysis of the learned feature space shows that DINOv3 fragments pixels into many small clusters in which the classes are locally interleaved, whereas the convolutional architectures (O-Net and O-Net++) embed them onto a single class-sorted manifold. Satellite-pretrained DINOv3 improves over natural-image initialisation across objectives, and our label-efficient DINOv3-ViT-L-Sat-O-Net-BYOL-JSD pipeline reaches 75.33 mDSC / 61.28 mIoU, outperforming standard machine learning baselines fit on the same 24 labelled images with the RGB pixel values used as features. We release CrevasseSeg to support label-efficient segmentation research in remote sensing.

---


### 250. [Emergent 3D Instance Segmentation from Self-Supervised Point Transformers](https://arxiv.org/abs/2608.15796)

**<font color=#1a73e8>作者：</font>** Ted Lentsch, Santiago Montiel-Marín, Holger Caesar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised 3D instance segmentation of outdoor LiDAR scans has traditionally relied on handcrafted geometric priors such as density-based clustering, motion cues, or projected 2D detections. In this work, we investigate whether a frozen, self-supervised point transformer already contains the structural information required to isolate object instances without any handcrafted geometric prior. Using this transformer purely as a feature extractor, we probe its internal representations across the SemanticKITTI, nuScenes, and Waymo Perception datasets. Our analysis yields four core insights: (1) the instance signal concentrates in the attention queries and keys rather than in the values or final output features; (2) output features semantically collapse, merging adjacent same-class objects that the queries and keys keep distinct; (3) this instance signal is bimodal in depth, strongest at the shallowest and deepest encoder stages; and (4) this signal is driven predominantly by the rotary position encoding (RoPE), whose removal collapses its advantage. We put these findings into our method TokenGraph3D, a training-free segmenter that groups points via connected components on a key-similarity graph, using neither density-based clustering nor proximity priors. Under identical prior-free conditions, we substantially outperform output-feature baselines, making the emergent 3D instance structure visible.

---


> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
