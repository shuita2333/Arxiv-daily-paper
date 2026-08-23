# 📦 其他研究 | 2026年08月24日

> 本类共 **155** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-155](./part-04.md)

---

### 51. [SAGE-XGBoost: Spatially Augmented Graph Embeddings--Machine Learning Framework for Natural Hazards Susceptibility Mapping under Data Scarcity](https://arxiv.org/abs/2608.19672)

**<font color=#1a73e8>作者：</font>** Mohammad H. Vahidnia, Ali Pourkarimi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural hazard susceptibility mapping is often constrained by limited labeled data, reducing the generalizability of conventional machine learning and limiting the applicability of complex deep learning models. This study proposes SAGE (Spatially Augmented Graph Embeddings), a structurally informed feature-engineering framework that combines controlled noise-based data augmentation with neighborhood-based graph embeddings to improve prediction under data-scarce conditions. A K-nearest neighbor graph is constructed to derive local spatial statistics, which are reduced using principal component analysis and integrated with environmental covariates and spatial coordinates. The resulting features are used with XGBoost to develop the SAGE-XGBoost model. The framework was evaluated for landslide and wildfire susceptibility mapping. SAGE-XGBoost consistently outperformed conventional and spatially explicit machine learning models. Compared with Spatial XGBoost, it achieved an absolute improvement of above 33 percentage points across the two case studies. The model reached AUC values of approximately 0.97 for landslide susceptibility and 0.95 for wildfire susceptibility. Feature importance analysis confirmed the contribution of graph embeddings to prediction, while their integration improved spatial coherence and reduced local noise amplification. Overall, SAGE-XGBoost provides an efficient and transferable alternative to deep representation learning for environmental hazard assessment and other geospatial prediction tasks under limited supervision.

---


### 52. [Grounding Mindfulness in Embodied Tangibles: A Scoping Review & Theoretical Framework for HCI Design](https://arxiv.org/abs/2608.19673)

**<font color=#1a73e8>作者：</font>** Tharaka Sachintha Ratnayake, Samangi Wadinambiarachchi, Sarah Schömbs 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Embodied and tangible devices are increasingly used to support mindfulness practices across meditation, yoga, and everyday routines. However, existing HCI research lacks a coherent theoretical foundation for explaining how such systems support distinct mindfulness processes and outcomes. First, we report findings from a scoping review of tangible devices (n=65) for mindfulness in HCI based on the mechanisms of action of mindfulness. The review found that most systems primarily target attentional regulation and body awareness, while emotion regulation and change in perspective on the self remain comparatively underexplored. Also, the evaluation methods used to assess the effectiveness of tangible systems for mindfulness-related outcomes were found to be fragmented and weakly grounded in theory. Building on these findings, a theoretical framework grounded in the Self-Awareness, Self-Regulation, and Self-Transcendence (S-ART) framework is proposed to explain how tangible systems support different forms of mindfulness practice. Within the framework, we present two complementary models: (1) Embodied Sensory Expansion (ESE) for focused-attention meditation (FAM) and (2) Embodied Sensory Anchoring (ESA) for open-monitoring meditation (OMM). Together, we show how this framework can provide a principled basis for explaining designs, generating hypotheses, and evaluating tangible mindfulness technologies in HCI, while highlighting key gaps for future research.

---


### 53. [Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcement Learning](https://arxiv.org/abs/2608.19684)

**<font color=#1a73e8>作者：</font>** Tanachai Anakewat, Takayuki Osa, Tatsuya Harada  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent studies investigate how to leverage pre-collected datasets to improve the policy performance and sample efficiency of RL. One promising approach to achieve this goal is to employ a two-stage strategy: In the first stage, diverse skills are extracted as a low-level policy from a given dataset, and a high-level policy is trained to solve a specific task in the second stage. Typically, extraction of the low-level policy is performed based on unsupervised learning such as trajectory VAE. However, a limitation of this approach is that the quality of the low-level policy highly depends on the quality of the dataset. To address this issue, we introduce QDOS (Quality-Diversity Offline Skill learning), a unified pipeline for robust offline-to-online learning. Our approach incorporates an Advantage-Weighted Quality-Diversity pretraining objective, which weights the skill extraction and diversity objectives by the estimated advantage of each trajectory segment. This approach allows the model to extract diverse and high-value skills. By providing robust and task-relevant skill representations, QDOS significantly improves the quality of the embedded skill space used by the low-level policy. We further integrate this with a dual dataset reuse strategy, where offline data is used both for skill pretraining and for populating the online replay buffer via pseudo-labeling. Experiments demonstrate that QDOS significantly outperforms strong baselines in structured manipulation tasks and unstructured locomotion tasks, confirming its ability to accelerate exploration and improve final returns in challenging sparse-reward domains.

---


### 54. [RIPE++: Reinforced Keypoint Learning from Positive Pairs Only](https://arxiv.org/abs/2608.19693)

**<font color=#1a73e8>作者：</font>** Johannes Künzel, Peter Eisert, Anna Hilsmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse keypoint extraction and matching underpin core tasks in geometric computer vision, including structure-from-motion, visual SLAM, augmented reality, and medical image registration. Learning robust local feature representations, however, typically requires accurate camera poses or depth supervision, which are often unavailable in real-world settings. Reinforcement learning (RL) has recently emerged as a promising alternative, requiring only the information if two images show the same scene or not. However, existing RL formulations such as RIPE rely on coarse binary rewards and carefully constructed negative training pairs, limiting training stability and descriptor discriminability. In this paper, we revisit RL-based keypoint learning and propose a reward that fully exploits the geometric consistency signal, deriving both reward and penalty from a single positive pair without contrasting against negatives. This richer signal provides sufficient supervisory contrast to learn discriminative detectors and descriptors from positive image pairs alone, enabling representation learning under extremely limited supervision. Furthermore, we show that the same RL objective can be extended to the matching stage by adapting LightGlue, raising AUC@5 on MegaDepth1500 from 56.58 to 59.65 and enabling weakly-supervised training of the full sparse matching pipeline from image pairs with partial visual overlap. We validate our approach on established benchmarks, demonstrating competitive results compared to fully-supervised methods. We further show that the method can be even trained on low texture medical video sequences, where camera poses are usually unavailable and standard SfM pipelines often fail. Code and data are available at this https URL .

---


### 55. [Scale-Separated Conditioning for Style-Encoder-Free Diffusion Stylization](https://arxiv.org/abs/2608.19719)

**<font color=#1a73e8>作者：</font>** Jingtao Zhang, Haorui Gao, Youqing Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-based diffusion stylization requires separating target geometry from transferable appearance. Existing tuning-based methods often rely on aligned content-style-target triplets or auxiliary visual encoders, which increases data cost and can transfer unintended scene structure from the style reference. We propose SEFS (Style-Encoder-Free Stylization), a style-encoder-free conditioning framework for diffusion transformers. SEFS forms style tokens from stochastic low-resolution crops of single training images. This crop bottleneck preserves local appearance statistics such as palette, stroke, texture, and material, while reducing access to global layout cues. Target content is encoded by edge and segmentation cues and fused with the noisy latent through parameter-efficient trainable projections. We add style-to-denoising re-normalization for token-statistic alignment and cross-block skip fusion for spatial detail. SEFS trains on unpaired single images; the frozen diffusion VAE is used only to place image conditions in the latent space. On artistic stylization benchmarks, SEFS improves content consistency and leakage diagnostics while retaining reference-style affinity, and ablations support the crop-resolution, re-normalization, and skip-fusion choices. The code of SEFS will be made publicly available.

---


### 56. [A Locally Tokenized Generative Model for Robust Time-Series Watermarking](https://arxiv.org/abs/2608.19727)

**<font color=#1a73e8>作者：</font>** Dongbin Kim, Geonwoo Shin, Yujin Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Watermarking is a central tool for provenance in generative models, yet its application to multivariate time series remains hindered by reliability failures under post-editing attacks. We show that existing detectors, which rely on globally coupled re-encoding, suffer from bidirectional drift of the null distribution: post-editing attacks can shift the z-score of non-watermarked samples in either direction, invalidating clean-calibrated thresholds. We argue that this instability is a property of the re-encoding, and that reliable detection requires each recovered unit to depend only on a bounded temporal neighborhood. Guided by this principle, we propose L-VQVAE, a generative model in which each discrete token is produced from a short contiguous window, and LVQMark, a watermarking method over this token space that combines logit-bias injection with robust re-encoding for attack-time detection. Experiments on four benchmarks spanning finance, energy, and neuroimaging show that our approach preserves generation quality while stabilizing both detection power and false-positive behavior under post-editing attacks.

---


### 57. [Learning to Beat: Phenotype-Guided Latent Flow with Regional Motion Priors for Biventricular Motion Synthesis](https://arxiv.org/abs/2608.19738)

**<font color=#1a73e8>作者：</font>** Xuan Yang, Xiaohan Yuan, Hao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Full-cycle biventricular geometry is essential for characterizing cardiac function. However, dense and temporally consistent 3D+t biventricular meshes are not routinely available, whereas end-diastolic (ED) anatomy can often be obtained reliably. We therefore investigate full-cycle biventricular motion synthesis from a single ED mesh. This task is challenging because cardiac deformation is spatially heterogeneous and phenotype dependent, while conventional global generative models often obscure localized motion patterns. In this study, we propose a region-specific and phenotype-adaptive framework that integrates motion-informed functional parcellation with conditional latent flow. A functional partition learned from reconstructed motion organizes the ventricular surface into regions with coherent dynamics and enables topology-aware regional feature exchange. A phenotype-conditioned rectified-flow model subsequently maps the ED anatomy to full-cycle motion latents through fine-grained conditioning and prototype-routed motion adapters. An optional control branch further incorporates available motion descriptors for controllable synthesis. Experiments on ACDC, M\&Ms, and M\&Ms-2 demonstrate consistent improvements in geometric accuracy and functional fidelity. Under ED-only synthesis, our method achieves biventricular ASSD, HD95, and vRMSE of \(1.49\pm0.34\)~mm, \(3.77\pm1.06\)~mm, and \(3.31\pm1.03\)~mm, respectively, outperforming all competing methods. Complementary functional and robustness evaluations further demonstrate that the synthesized sequences preserve physiologically plausible ventricular dynamics and generalize across cohorts and disease phenotypes. The code will be released publicly upon acceptance of the manuscript for publication.

---


### 58. [One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows](https://arxiv.org/abs/2608.19741)

**<font color=#1a73e8>作者：</font>** Zhuochun Li, Youngmin Ko, Ali Keramati 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent agent benchmarks increasingly ground evaluation in executable environments, from code repair to web navigation, app APIs, and function calling. Yet completing consequential work beyond code requires more than producing a plausible response or valid tool call: agents must gather missing information over multiple turns, follow domain policies, coordinate dependent tools, and realize the correct persistent state transition without collateral effects. In this paper, we introduce Thinkingbox, a sandbox for tool-agent-user interaction that provides isolated MCP-compatible tool sessions, complete execution traces, and outcome evaluation over terminal backend state. Built on this sandbox, Thinkingbox-bench contains 507 policy-conditioned workflows across numerous scenarios, including retail, hospitality, auto insurance, neobank internal IT, and consulting IT/HR support. Each attempt is evaluated by task-specific executable checks that accept valid trajectories while rejecting wrong, missing, or extra effects; designated tasks additionally check required properties of the final response. Across proprietary and open-weight models, the strongest achieves 65.36% pass@1, but only 25.25% pass^20. Moreover, many failed trials show clean termination and valid state-changing actions, showing that response or tool-call-level signals are not clear proxies for end-to-end task completion. Thinkingbox-bench reveals a large gap between occasionally finding a successful trajectory and reliably completing stateful business tasks. We release both Thinkingbox and Thinkingbox-Bench: this https URL

---


### 59. [Gallileo-4D: Frozen Backbone Ensemble for Dynamic 4D Reconstruction](https://arxiv.org/abs/2608.19743)

**<font color=#1a73e8>作者：</font>** Nicolò Savioli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe our entry to the PhysAI Dynamic 4D Reconstruction Challenge, which placed third of 27 teams at 0.58356 APD on the final leaderboard, without a single gradient update. This was not the plan: of thirteen fine-tuning configurations of a pre-trained 4D backbone, twelve degraded the challenge score, and eleven of those twelve improved local validation at the same time. We trace this inversion to the structure of the benchmark: only 25% of the evaluation set belongs to the data variant released for training, so updates that fit the available data damage the pre-trained features the remaining 75% relies on. Our system therefore freezes the backbone and spends its budget at inference time, fusing three decoding configurations -- temporal stride-3, horizontal-flip test-time augmentation, and dense stride-1 -- under a convex weighting. The ensemble recovers +0.041 APD over the frozen baseline, more than any training run achieved, at zero training cost.

---


### 60. [Truncate Bad, Upweight Good: BoN-Style Distillation via Rank-Based Classification](https://arxiv.org/abs/2608.19748)

**<font color=#1a73e8>作者：</font>** Yarin Bar, Yaniv Romano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time selection methods, such as Best-of-N, improve generation by sampling a pool of candidates and selecting the top-ranked completion according to a reward model. Distillation seeks to amortize this procedure into a single policy by replacing raw rewards with in-pool ranks and learning a policy that upweights higher-ranked completions. However, existing rank-based policies typically use smooth full-support reweighting, so low-ranked completions receive less mass but remain in the target support. Although a sharper reweighting reduces lower-tail mass, it also increases reliance on brittle ranking at the top made by a single reward model. We propose TUP: a Truncate-bad, Upweight-good Policy that removes low-ranked completions from the support and reweights only the retained upper tail with a tunable sharpness. TUP admits a closed-form, prompt-independent normalization and can be trained fully offline via binary cross-entropy, using shifted-truncated win-rates as soft labels and distilled-to-reference log-likelihood ratios as logits. Theoretically, under certain assumptions, we show that for any unknown oracle reward, the best monotone rank-reweighting can be matched by a lower-tail truncation rule, providing formal support for removing the lower tail rather than merely downweighting it. Empirically, we show that TUP is competitive with strong offline alignment baselines.

---


### 61. [TGL-APT: Temporal Graph Learning with Graph Distillation for Efficient APT Investigation](https://arxiv.org/abs/2608.19750)

**<font color=#1a73e8>作者：</font>** Jing Chen, Ayong Ye, Yuanhuang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advanced Persistent Threat (APT) attacks pose a critical challenge to modern systems, as their stealthy, multi-stage nature renders conventional detection methods ineffective. While provenance graphs provide rich behavioral context for attack investigation, attack-relevant evidence is often sparse and embedded in large volumes of routine system activity, making full-graph learning both computationally expensive and difficult to correlate over long attack sequences. We present TGL-APT, an adaptive investigation framework built on the observation that attack-relevant information is non-uniformly distributed and often mediated by structurally influential or behaviorally distinctive entities, which we characterize as information-bottleneck nodes. TGL-APT combines three complementary components: (1) information-bottleneck-guided graph distillation that suppresses provenance redundancy while bounding structural distortion and preserving causal reachability; (2) adaptive temporal graph learning that continuously refines the core node set as node relevance evolves; and (3) cross-spatiotemporal attack fingerprint alignment that associates fragmented suspicious activities across different entities and time windows. Finally, causal expansion and stage characterization reconstruct coherent attack processes for investigation. Experiments on three DARPA E3 datasets show F1-scores of 95.7%, 90.9%, and 88.9%, while reducing training time, detection latency, and memory usage by approximately 39%, 33%, and 22%, respectively, compared with KAIROS. These results demonstrate that TGL-APT effectively balances detection performance, computational efficiency, and investigation capability for provenance-based APT analysis.

---


### 62. [GenMatch: An End-to-End Generative Matching Framework for Micro-View Order-Dispatching in Ride-Hailing](https://arxiv.org/abs/2608.19751)

**<font color=#1a73e8>作者：</font>** Chuang Liu, Yuxueqing Zhang, Tengfei Lyu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Micro-View Order-Dispatching assigns available drivers to passenger orders within each dispatch batch and is critical to the service quality and operational efficiency of ride-hailing platforms. Mainstream industrial solutions follow a multi-stage paradigm of model prediction, value calculation, and dispatch matching. Although dispatch quality is determined by the final batch-level assignment, these stages optimize different intermediate objectives. This cross-stage objective inconsistency means that improving a single stage does not necessarily improve the overall dispatch result. We therefore formulate Micro-View Order-Dispatching as a generative matching problem and propose GenMatch, an end-to-end Generative Matching framework and the first such framework deployed in a real-world production environment. Applying generative modeling to this problem introduces three challenges. First, each dispatch batch forms a dynamic sparse bipartite graph, requiring efficient structured batch-level encoding. Second, replacing the hand-crafted value function requires learning unified business utility from heterogeneous feedback. Third, directly generating an assignment requires tracking the evolving matching state because each selected order-driver pair changes the remaining feasible candidates. GenMatch addresses these challenges with a Context-Aware Bipartite Encoder, a Business-Aware Utility Learner, and a State-Aware Pointer Decoder. Extensive offline evaluations and online A/B tests in five cities across DiDi's international ride-hailing markets show consistent improvements over competitive baselines, confirming the effectiveness and practicality of GenMatch for industrial order-dispatching.

---


### 63. [Finite-Horizon Input-Output Dynamics of Minibatch Perturbations in AdamW](https://arxiv.org/abs/2608.19762)

**<font color=#1a73e8>作者：</font>** Kang Liu, Suyan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A minibatch can influence training beyond the update at which it is observed because AdamW stores past gradient information in its optimizer states. We study this delayed effect through paired trajectories that differ only in one gradient update and share the same subsequent training sequence. We formulate AdamW as a finite-horizon input--state--output (ISO) system whose state contains the model parameters and first- and second-moment estimates. Linearizing the joint dynamics yields a signed response operator that maps a localized gradient perturbation to its future loss effects, revealing how optimizer memory shapes their magnitude, timing, and sign. We further derive an exact multistep error decomposition and establish first-order finite-horizon accuracy under local smoothness and controlled activation switching. Experiments validate the response mechanism and optimizer-state effects, while repeated-future analyses reveal substantial prospective structure in delayed influence that can be partially recovered from ISO approximations. Code is available at this https URL.

---


### 64. [Far from the Crowd: Scalable Self-Supervised Learning via Geographic Isolation](https://arxiv.org/abs/2608.19766)

**<font color=#1a73e8>作者：</font>** Daniele Rege Cambrin, Francesco Rossi, Mattia Varile  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised pretraining on remote sensing imagery typically treats all samples as equally informative, despite large variability in geographic and visual structure. We propose a curriculum learning strategy for self-supervised Earth observation that ranks samples by geographic isolation, a label-free proxy derived entirely from geolocation metadata already present in geospatial datasets, requiring no image decoding, no model feedback, and no manual annotation. Unlike visual complexity proxies, it scales as O(D log D) with dataset size D and is well-defined for both contrastive and reconstructive objectives. We integrate the proposed measure into MoCoV2 and MAE pretraining and evaluate across three downstream tasks from CopernicusBench (BigEarthNet, DFC-2020, LCZ). Our curriculum reaches baseline final-epoch performance using as few as 20% of the training budget (MAE) and at most 40% (MoCo) of the training budget, and improves final downstream performance by up to +5 mAP on BigEarthNet, with gains of 1-5 points across benchmarks, matching visual-complexity curricula while reducing pre-computation cost by more than 140x (4 s vs. 568 s on SSL4EO). A CKA and effective-rank analysis further reveals that curriculum-trained encoders develop higher-dimensional, more uniformly utilized embedding spaces throughout training.

---


### 65. [Coupled Optimal Transport with Landmark Constraints](https://arxiv.org/abs/2608.19783)

**<font color=#1a73e8>作者：</font>** Xiang Gu, Jian Sun, Zongben Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing optimal transport (OT) models primarily seek an OT map or plan between distributions by minimizing a prescribed transport cost or distortion. However, minimizing transport cost or distortion alone may fail to identify a geometrically meaningful transformation between the two distributions. To address this limitation, this paper proposes a novel coupled OT framework that leverages a small number of annotated landmarks to guide the recovery of an underlying deformation governing the distribution transformation. The coupled OT framework integrates the optimization of the transport plan and the deformation field into a unified model, where the landmark-guided deformation field and the cost-driven transport plan are coupled through a mutual-consistency constraint. As a result, the deformation is jointly determined by the annotated landmarks and cost-driven distribution matching. The proposed framework provides a principled connection between landmark-based registration and transport-based distribution matching, enabling the recovery of transport maps from sparse geometric supervision. We establish the well-definedness of the proposed model in a general variational setting and develop a finite-element-based numerical algorithm for computation whose convergence properties are systematically analyzed. The practical effectiveness of the proposed approach is verified in shape matching.

---


### 66. [TT-net: Quantum Inspired Tensor Network Denoising in Conditional GANs](https://arxiv.org/abs/2608.19789)

**<font color=#1a73e8>作者：</font>** Michal A. Sterzel, Marko J. Rančić  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developed as a workhorse for classical simulations of quantum algorithms and quantum many-body systems, Tensor Network methods have entered the scientific mainstream in quantum physics. Among various types of tensor networks, Tensor Trains (commonly know as Matrix Product States in the quantum computing community) have already found applications in machine learning. These methods often rely on a powerful linear algebra tool called the Singular Value Decomposition (SVD). Several conditional GAN architectures for image denoising incorporate SVD as a single-cut decomposition step applied to generator feature maps. In this work we introduce TT-Net, which replaces the per-channel SVD denoising block with a two-cut tensor-train decomposition capable of accessing cross-channel information directly, a capability absent from contemporary alternatives. In a controlled comparison differing only in this decomposition mechanism, TT-Net outperforms SVD-Net on PSNR and SSIM across all three noise types tested (Gaussian, motion blur, and salt-and-pepper), supporting the hypothesis that cross-channel access improves denoising quality. Training-dynamics analysis further shows that TT-Net's adversarial loss term consistently saturates to a stagnant state across all three noise types, more so than SVD-Net's, while reconstruction quality continues to improve regardless, raising an open question about the adversarial component's contribution that this work identifies but does not resolve. Furthermore, for Gaussian noise our method outperforms both the EigenGAN and the state of the art Pix2pix method which does not assume any linear algebra decompositions and does not retain any linear algebra information. Our manuscript shows how quantum inspired tools can be used as practical real world feature filters for deep learning applications.

---


### 67. [LoRA-GA$^2$: Low Rank Adaptation with Multi-step Gradient Adaptive Alignment](https://arxiv.org/abs/2608.19800)

**<font color=#1a73e8>作者：</font>** Haonan He, Xinyue Fan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) is a prominent fine-tuning method for large models, achieving competitive performance with reduced memory overhead. However, a persistent performance gap remains between LoRA and full fine-tuning. Recent studies have sought to narrow this gap by employing one-step gradient approximations of pretrained weights to align LoRA updates with the principal directions or intrinsic dimensionalities of full fine-tuning updates. Nevertheless, these approaches fail to capture the full dynamics of the gradients. In this paper, we propose LoRA-GA$^2$, an effective fine-tuning algorithm that fully leverages multi-step gradient information. Specifically, we introduce a lightweight probe for multi-step gradients of pretrained weights that incurs no additional GPU memory cost and only marginal time overhead. We further employ a spectrum-aware, importance-based rank allocation and optimal initialization derived from multi-step gradients. Extensive experimental results demonstrate that LoRA-GA$^2$ consistently outperforms existing LoRA variants while preserving the efficiency advantages of vanilla LoRA. For instance, LoRA-GA$^2$ surpasses the leading baseline by an average of 0.66 points on the GLUE benchmark, and outperforms the strongest baseline by 1.03 points on GSM8K and 0.87 points on HumanEval, respectively.

---


### 68. [Unsupervised Anomaly Detection Using Flow Matching on Tabular Data](https://arxiv.org/abs/2608.19801)

**<font color=#1a73e8>作者：</font>** Philip Konz, Tejaswini Medi, Margret Keuper  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial anomaly detection often relies on large unlabeled transaction logs, where anomalous samples may already be present during training. Such training-set contamination violates the clean-normal data assumption underlying many anomaly detection methods. Although flow matching has demonstrated strong performance in generative modeling, its robustness in unsupervised tabular anomaly detection remains underexplored. In this work, we study flow-matching-based anomaly detection under contaminated training data by comparing Time-Conditioned Contraction Matching (TCCM) with Forest-Flow and evaluating multiple anomaly scoring functions. Our results show that the choice of anomaly score is critical. The original single-step Decision score used by TCCM is sensitive to contamination, whereas trajectory-based Deviation and Reconstruction scores provide more stable anomaly signals. With these scores, Forest-Flow becomes competitive with, and in some cases outperforms, TCCM. These findings highlight the importance of anomaly scoring for flow-matching methods in financial anomaly detection under severe class imbalance.

---


### 69. [ADAPT: Physics-Aware Diffusion-based World Models for Adaptive Predictive Transferable HVAC Control](https://arxiv.org/abs/2608.19804)

**<font color=#1a73e8>作者：</font>** Xu Yang, Kailai Sun, Dianyu Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Buildings account for roughly one-third of global energy consumption and CO$_2$ emissions. Optimizing indoor climate systems plays a critical role for urban climate mitigation aligned with UN Sustainable Development Goals 11 and 13. However, indoor delayed thermodynamic responses and partial observability severely hinder existing methods, which are primarily limited by implicit thermal inertia, occupancy dynamic prediction, and cumulative prediction errors, especially for out-of-distribution environments. In practice, these challenges are further exacerbated by the high cost and privacy burden of dense indoor sensing, forcing operators to collect only limited data in a single operating regime while expecting controllers to generalize reliably across unseen seasons and climate regions. To address this problem, we propose ADAPT, a physics-aware conditional diffusion indoor environmental world model for HVAC control. The model predicts a short-horizon held-action thermal baseline to capture the latent thermal inertia of the buildings. The diffusion backbone utilizes the robustness of generative models, while a learnable multi-zone heat-balance regularizer constrains generated trajectories to satisfy transferable building thermodynamics without requiring known building geometry or manually calibrated thermal parameters. A credit assignment is then design for the downstream reinforcement learning. Extensive experiments on SemibuildingSim and Sinergym demonstrate that ADAPT reduces HVAC energy consumption by 7.3\% and occupant discomfort by 30.2\% compared with state-of-the-art baselines under IID control. Under OOD control scenarios spanning unseen seasons and climate regions, ADAPT maintains robust performance with only marginal degradation relative to its IID performance, substantially outperforming existing methods in transfer robustness.

---


### 70. [FAR-DPO: Feasibility-Aware and Robust Direct Preference Optimization for Cyclic Peptide Design](https://arxiv.org/abs/2608.19808)

**<font color=#1a73e8>作者：</font>** Guofeng Zhang, Rong Han, Xiaoyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cyclic peptides are emerging as promising molecular scaffolds in drug discovery due to their high binding affinity and structural stability. However, extending generative models from linear to cyclic peptide design remains challenging, as cyclization sharply restricts the feasible design space through coupled geometric and biophysical constraints. Moreover, limited training data has led existing approaches to rely largely on zero-shot generation or post hoc filtering, resulting in low yields of feasible designs and limited control over multi-objective trade-offs. To address these limitations, we propose FAR-DPO (Feasibility-Aware and Robust Direct Preference Optimization), an architecture-agnostic framework that steers generative models toward structurally and biophysically feasible cyclic peptide designs, particularly for challenging targets. FAR-DPO integrates feasibility-aware preference construction with difficulty-aware group-robust optimization. Specifically, it constructs within-target preference pairs through feasibility-gated multi-objective dominance and adaptively reweights predefined difficulty groups according to their current preference losses. On the CPSea LNR benchmark, under a fixed generation budget, FAR-DPO increases overall success rate from 46.89% to 57.79% on PepGLAD and from 47.96% to 49.57% on PepFlow. These gains also extend to the hardest target quartile and are accompanied by more favorable best-per-target binding scores. Together, these results demonstrate FAR-DPO's effectiveness in improving feasibility and target-wise robustness.

---


### 71. [Core-KAN: Continuous Vision Kernels with Kolmogorov-Arnold Networks](https://arxiv.org/abs/2608.19817)

**<font color=#1a73e8>作者：</font>** Lan Guo, Mengling Li, Haoran Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional convolutional kernels are typically defined on fixed discrete grids, limiting their ability to accommodate heterogeneous local structures. Existing adaptive operators improve flexibility but often couple geometric scale variation with content-dependent filtering, while incurring high computational cost from per-location kernel generation. To decouple geometric scale adaptation from content-dependent filtering while avoiding expensive per-location kernel generation, we propose Continuous Relative-scale KAN (Core-KAN), a relative-scale-conditioned continuous convolution operator. Core-KAN maps input features into a compact latent basis space and uses a lightweight scale controller to predict local scales relative to an exponential moving average reference. A KAN-based generator represents depth-wise kernel bases as continuous coordinate functions, allowing the operator to synthesize spatial filters at arbitrary resolutions rather than being confined to a fixed lattice. Instead of synthesizing independent kernels at every location, it constructs a compact bank of scale-conditioned kernel responses and interpolates them according to the predicted local scale map. An independent mixing controller further combines the interpolated basis responses based on local content, explicitly decoupling geometric scale adaptation from content-dependent filtering. Together with lightweight pointwise projections, this design forms a low-rank dynamic convolution that scales efficiently with kernel size and integrates readily into hierarchical vision backbones. Experiments across three representative vision tasks show Core-KAN consistently outperforms strong convolutional and dynamic-kernel baselines with only marginal parameter and computational overhead, offering an efficient, general framework for continuous, scale-adaptive convolution.

---


### 72. [Survival of~the~Stealthiest: Evolving Low-Entropy Ransomware via~Genetic Algorithms](https://arxiv.org/abs/2608.19821)

**<font color=#1a73e8>作者：</font>** Efrat Levenberg, Kristina Sviazhina, Ayelet Butman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional ransomware deployment often relies on massive encryption procedure, triggering immediate detection by modern defense systems. This work introduces a paradigm shift in cryptographic attacks by framing ransomware execution as a Search-Based Software Engineering (SBSE) optimization problem. This approach addresses the persistence gap observed in modern threats, where attacks aim to remain undercover for hours rather than minutes. Using a Genetic Algorithm (GA), we optimize data encryption under a hard constraint on the statistical deviation from baseline system activity. We demonstrate that our evolved attack patterns can evade behavioral monitors under fingerprinting techniques. Our results suggest that search-based methods provide a powerful framework for generating evasive malware, highlighting an emerging challenge for automated software defense.

---


### 73. [Calming Robot Pitches? Exploring the Influence of Robot Voice Pitch on Children's Stress Levels](https://arxiv.org/abs/2608.19826)

**<font color=#1a73e8>作者：</font>** Nina G. M. van Roij, Emilia I. Barakova, Briana Isaila 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examined whether variations in robot speech pitch influence children's stress levels during a robot-guided game. Although lower-pitched voices have been shown to facilitate stress regulation in human communication, it remains unclear whether this effect generalizes to synthetic voices in child-robot interactions. Twenty-seven Dutch children aged 8-12 years were randomly assigned to interact with a Zenbo Junior II robot using either a lower-pitched or a higher-pitched voice. The interaction consisted of an introduction followed by a timed LEGO-building game. Stress levels, measured with an adapted version of CAM-S, increased during the game, confirming the stress-inducing nature of the task. No differences emerged between pitch conditions. These findings suggest that the benefits of lower pitch in reducing stress may not directly translate to child-robot interactions. Possible explanations include children's developing sensitivity to emotional tone, mismatches between the robot's voice and appearance, or the use of fixed pitch changes that sound unnatural, since real speech varies dynamically across multiple dimensions. Future research examining combinations of prosodic cues (beyond pitch alone) could provide further insights and help inform robot voice design for effective stress regulation support for children.

---


### 74. [Dancing Through Soundscapes: Designing a Low-Cost, Sound-Based Device for Sensing and Interpreting Movement and Dance](https://arxiv.org/abs/2608.19827)

**<font color=#1a73e8>作者：</font>** Swen E. Gaudl, Silvia Carderelli-Gronau  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When we move through space, we often rely on multiple senses beyond vision to perceive and act in that environment: we ``feel'' the presence of others; we build internal representations and models and recall them to navigate the environment. We also leave traces and impressions that others pick up on. The traces include echoes, heat, the displacement of objects such as furniture or footprints, air movement close to the face of another, smells such as perfume, but also the immediate sounds we make when we move and breathe. Movement is a spatial and temporal activity, and dance as a form of movement practice requires coordination of oneself in relation to others, the space and a potential score. When rehearsing dance, dancers have to relate to others often not just by looking but more often by feeling and imagining or remembering where others are based on experience and shared practice. So how can we approach technology-mediated movement and dance? Why should we explore it? How can we support spatial and temporal practice meaningfully and joyfully? In this work, we focus on sound traces; we present the design and rationale for a sound-based artefact that translates movement-based sound into layered, explorable, generative soundscapes. The work contributes a novel artefact for exploring movement-based activities with a audio-first approach, with a focus on the spatial performative experience. The paper further reflects on observations from workshops and public sharings, including how participants used repetition, stillness, environmental sound, and call-and-response to understand and improvise with the soundscape.

---


### 75. [Causal Reasoning with Bipartite Graphical Causal Models](https://arxiv.org/abs/2608.19831)

**<font color=#1a73e8>作者：</font>** Joris M. Mooij  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Causal Bayesian networks (CBNs) and structural causal models (SCMs) are the dominant frameworks for graphical causal reasoning, but they cannot adequately represent all real-world causal systems. In particular, systems at equilibrium---where feedback mechanisms create cyclic causal dependencies---can exhibit causal semantics that are fundamentally incompatible with these frameworks: different interventions that enforce the same variable value may have different effects, rendering the standard ``perfect intervention'' do($X = x$) ambiguous. We propose bipartite graphical causal models (BGCMs), in which the structure of a system of equations is encoded by a bipartite graph with variable and equation nodes. In this framework, a hard intervention do($f_j : X_v = \xi_v$) specifies which equation is replaced, which variable is targeted, and at what value---resolving the ambiguity of the standard notion. We demonstrate, through a detailed case study of a physical system, that this representation naturally corresponds to distinct real-world interventions. We formulate a Markov property in terms of a new graphical separation criterion (B-separation) that exploits the functional determinism inherent in the equations, and we extend it to settings with non-random inputs. We show how this gives rise to a do-calculus for reasoning about domain invariances. BGCMs strictly generalize CBNs and SCMs while retaining the ability to perform graphical causal reasoning.

---


### 76. [Adaptive Probabilistic Shielding by Learning MDPs for Safe Reinforcement Learning](https://arxiv.org/abs/2608.19836)

**<font color=#1a73e8>作者：</font>** Astrid Horn Brorholt, Maris F. L. Galesloot, Nils Jansen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic shielding is a technique for safe reinforcement learning (RL). Typically, a static observer -- called the shield -- constrains the learning agent's actions to those for which acting safely remains feasible. Traditionally, the shield is computed from the transition probabilities of the underlying Markov decision process (MDP). Thus, this technique is not applicable when the MDP model is not given a priori, which, unfortunately, is the case in typical RL applications. In this paper, we study the problem of computing a shield in the setting where the transition graph of the MDP is known, but the transition probabilities are unknown. Our approach integrates probabilistic shielding with online model learning: as the RL agent explores the environment, we estimate the transition probabilities. From this estimate, we compute a shield. While the shield may be conservative initially, it adapts as the model estimate becomes more precise. Thus, the shield improves in tandem with the RL agent. This paradigm of adaptive probabilistic shielding raises a number of challenges, such as when to recompute the shield and how to balance between exploration and safety during learning. We empirically evaluate multiple variants of this paradigm across several environments.

---


### 77. [Specification-delta-driven data governance: an empirical study of the «spec-delta» as the unit of change in lakehouse data platforms](https://arxiv.org/abs/2608.19838)

**<font color=#1a73e8>作者：</font>** Pablo Ramirez Amador  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spec Driven Development SDD has consolidated the idea that the specification rather than the code should be the primary artefact governing AI assisted work. Tools such as GitHub Spec Kit, and proposals such as Constitutional SDD, have formalised this principle in the software domain, while the executable data-contracts literature has extended it to schema and quality enforcement at run time. Nevertheless, the treatment of the specification delta OpenSpec's core idea that every change should produce a reviewable increment of requirements as the unit of change in data platforms remains empirically unexplored, even though many data-platform changes are contractual (new datasets, service-level agreements, metric semantics, access policies) rather than purely code changes. This work formalises the spec-delta concept, proposes a taxonomy of data platform changes according to their suitability for incremental specification, and defines a controlled experiment comparing a spec-delta-driven workflow against a conventional code pull-request workflow without a delta. The response variables are discovery to deployment time, the density of defects reaching the Silver and Gold lakehouse layers, cross-tool metric divergence, and reviewer cognitive load measured with NASA TLX. The paper explicitly reserves a demonstration-and-laboratory section for instantiation on a real lakehouse environment. The contribution is not a tool but reproducible evidence and an applicability guide that helps to avoid the up front over specification antipattern.

---


### 78. [Online Test-Time Adaptation for Generalizable Dynamic Graph Anomaly Detection](https://arxiv.org/abs/2608.19858)

**<font color=#1a73e8>作者：</font>** Jialun Zheng, Hanchen Yang, Jiannong Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalizable dynamic graph anomaly detection (DGAD) enables pretrained detectors to identify anomalies in unseen target domains without costly retraining. However, existing methods often fail for two reasons. First, they mainly rely on domain-agnostic patterns and miss domain-specific patterns that keep evolving. Second, they assume access to the full target domain data, whereas in more practical online test-time adaptation settings, target data arrive sequentially in unlabeled chunks. To address these limitations, we formulate online test-time adaptation for generalizable DGAD and propose OTTA-DGAD. OTTA-DGAD first extracts dynamic prototypes, i.e., evolving representations of normal and anomalous patterns, from temporal ego-graphs and stores them in a memory buffer. The buffer selectively retains general patterns shared across the source domains used for pretraining while incorporating new patterns from the target domain. An anomaly scorer then compares incoming edge representations against these prototypes to identify both general and domain-specific anomalies. During adaptation, OTTA-DGAD updates the memory buffer using reliable pseudo-labels identified through confidence-based detection. It further enriches each target chunk with relevant representations retained from previous chunks, compensating for information loss resulting from the sequential arrival of data. Extensive experiments under strict test-then-adapt OTTA settings demonstrate state-of-the-art performance on ten real-world datasets from diverse domains.

---


### 79. [AutoLumNet: Monotone Optimal Transport for Single-Shot Exposure Correction](https://arxiv.org/abs/2608.19860)

**<font color=#1a73e8>作者：</font>** Airin Akter Tania, Md Raihan Khan, Mohiuddin Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-shot exposure correction aims to map an arbitrarily degraded image---whether under-exposed, over-exposed, or a spatial mixture of both---to a well-exposed output from a single capture. We present AutoLumNet, a framework that decomposes this task into a global monotone tone curve and a bounded local residual, making the global component the locus of formal guarantees. The tone curve is parameterized as the normalized cumulative integral of a strictly positive density, ensuring strict monotonicity by construction rather than by penalty. We prove that this parameterization (i)~preserves the pairwise luminance ordering of all pixels and all spatial extrema unconditionally, and (ii)~is dense in the space of valid tone corrections, containing the one-dimensional optimal-transport map from the input to any target luminance distribution. A differentiable sorted-sample Wasserstein-2 objective drives the learned curve toward the OT optimum during training. Spatially varying effects that the global map provably cannot address---local shading, chrominance shifts, and clipped-region restoration---are handled by a bounded residual decoder with dual-branch convex fusion, for which we provide an explicit sufficient condition for local order preservation. Experiments on five benchmarks (MSEC, SICE, LCDP, LOL-v1, LOL-v2-real) show that AutoLumNet achieves state-of-the-art PSNR and SSIM across both under- and over-exposure regimes at 11.2\,ms per frame, and generalizes zero-shot to pure low-light benchmarks without retraining. To our knowledge, AutoLumNet is the first exposure-correction method to unite structural monotonicity, optimal-transport optimality, and bounded local adaptivity within a single trainable architecture. Code is available at this https URL.

---


### 80. [A 360-Degree Vision Dataset for Learning Yaw Control on GPS-Denied Micro-UAVs in Disaster-Response-Relevant Environments](https://arxiv.org/abs/2608.19866)

**<font color=#1a73e8>作者：</font>** Niklas Voigt, Hartmut Surmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel data-driven approach to camera-based autonomy for micro-drones in GPS-denied, radio-challenging indoor environments. The target application is disaster and emergency response, where micro-UAVs can provide rapid situational awareness in hazardous settings such as firefighting and chemical, biological, radiological, and nuclear (CBRN) incidents while reducing risk for human responders. When the communication link is lost, the micro-drone uses a learned yaw controller to autonomously navigate toward open space, preserving onboard sensor data that would otherwise be lost with the vehicle. A custom micro-drone equipped with a 360-degree camera was used to record diverse industrial, underground, and training scenarios representative of communication-denied field operations. We introduce a preprocessing pipeline that converts equirectangular 360-degree footage into planar front views and dynamically generates image-label pairs for AI training. We then train and compare multiple convolutional neural network variants that predict a continuous yaw command from a single monocular view. Evaluation on a held-out test set confirms the feasibility of the learned yaw-prediction approach. A semi-autonomous real-world test further demonstrates the practicality of the method while revealing key failure modes, particularly reflections and glare.

---


### 81. [Evaluating Smart Home Device User Responses to their (Un)Confirmed Privacy Expectations](https://arxiv.org/abs/2608.19873)

**<font color=#1a73e8>作者：</font>** Tania Khatun, Mahdieh Sheikh Rezaei, Danny Yuxing Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Users of smart home devices are often unaware of how their devices handle personal data. We examine how revealing these data practices influences user trust, satisfaction, and coping behaviors, including decisions to block device communications. Using Expectation-Confirmation Theory, we conducted two complementary studies to balance ecological validity with experimental control. An in-situ field study used network monitoring to reveal actual device traffic, and an online experiment presented simulated reports with manipulated levels of advertising-related communications. Across both studies, when data practices aligned with user expectations, satisfaction increased, strengthening intentions to continue using the device. Defensive responses, however, followed different pathways: satisfaction predicted willingness to block in the in-situ field study, whereas collection concerns were the primary predictor of blocking in the experiment. Together, these findings show how transparency reshapes attitudes and behaviors among existing smart-home users, underscoring the role of expectation confirmation in real-world, continued-use contexts.

---


### 82. [TESTNAV: Pareto-Guided Search for Compositional Robustness Testing](https://arxiv.org/abs/2608.19882)

**<font color=#1a73e8>作者：</font>** Arooj Arif, Tobias Hartung, Elena Botoeva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning models remain vulnerable to real-world input perturbations, especially when multiple corruptions co-occur in the same input (e.g., brightness shifts and motion blur). Compositional testing reveals these interaction effects but introduces two challenges: combinatorial growth of the perturbation space as dimensions and severity levels increase, and uneven diagnostic value-many combinations yield unrealistically degraded inputs with limited practical relevance.
We present TESTNAV, 1 a Pareto-guided robustness testing framework for efficiently exploring discrete, compositional perturbation spaces when only a limited number of perturbation configurations can be evaluated. TESTNAV prioritises severe yet realistic failures by formulating robustness testing as bi-objective optimisation: maximise performance degradation while preserving input fidelity measured by modality-specific metrics (e.g., SSIM and KID for vision; chrF and BERT-F1 for language and code). It uses NSGA-II to approximate the bi-objective Pareto front. Across four benchmarks spanning vision, natural language, and code generation, TESTNAV recovers Pareto fronts up to 2.15x faster than search-based baselines, using 35.8%-89.3% of the discrete perturbation space defined by four perturbation dimensions with six levels each.

---


### 83. [Separating Covariate Shift from Mechanism Change with Two Discriminators: CJSD, a Conditional Discrepancy with an Exact Covariate-Concept Decomposition](https://arxiv.org/abs/2608.19885)

**<font color=#1a73e8>作者：</font>** Kentaro Oda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Streaming systems that maintain a pool of expert models must repeatedly decide whether to reuse an existing expert for arriving data, spawn a new one, or defer. We present a decision layer that makes all three outcomes statistically meaningful. Reuse and spawn are posed as one-sided sequential hypotheses on a conditional (mechanism-level) discrepancy, separated by an indifference zone; defer is exactly the state in which neither betting e-process has accumulated sufficient evidence. We prove finite-time anytime validity for the observable surrogate discrepancy of a predictable discriminator sequence, and an unconditional one-sided transfer to the population quantity in which each side's slack is the excess risk of a single discriminator; an empirically observed downward-bias regularity makes the spawn side exactly conservative. Recency without sacrificing the guarantee is obtained by a restarted e-detector: a bank of unwindowed betting supermartingales at geometrically spaced restart times (O(log t) memory), with the error budget spent over restart instances, which preserves lifetime anytime validity; spending over expert-creation order likewise controls multiplicity for unboundedly many experts. On synthetic multi-concept streams, Electricity, Covertype, and the recurrence-heavy INSECTS benchmark, the instance-accounted restarted bank achieves zero false spawns and zero false reuses after switches and matches or exceeds the retired windowed heuristic (INSECTS-reoccurring accuracy 0.675), making the deployed algorithm and the guaranteed algorithm one and the same.

---


### 84. [Evidence Before Expansion: Reuse, Spawn, or Defer in Lifelong Expert Pools](https://arxiv.org/abs/2608.19888)

**<font color=#1a73e8>作者：</font>** Kentaro Oda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Streaming systems that maintain a pool of expert models must repeatedly decide whether to reuse an existing expert for arriving data, spawn a new one, or defer. We present a decision layer that makes all three outcomes statistically meaningful. Reuse and spawn are posed as one-sided sequential hypotheses on a conditional (mechanism-level) discrepancy, separated by an indifference zone; defer is exactly the state in which neither betting e-process has accumulated sufficient evidence. We prove finite-time anytime validity for the observable surrogate discrepancy of a predictable discriminator sequence, and an unconditional one-sided transfer to the population quantity in which each side's slack is the excess risk of a single discriminator; an empirically observed downward-bias regularity makes the spawn side exactly conservative. Recency without sacrificing the guarantee is obtained by a restarted e-detector: a bank of unwindowed betting supermartingales at geometrically spaced restart times (O(log t) memory), with the error budget spent over restart instances, which preserves lifetime anytime validity; spending over expert-creation order likewise controls multiplicity for unboundedly many experts. On synthetic multi-concept streams, Electricity, Covertype, and the recurrence-heavy INSECTS benchmark, the instance-accounted restarted bank achieves zero false spawns and zero false reuses after switches and matches or exceeds the retired windowed heuristic (INSECTS-reoccurring accuracy 0.675), making the deployed algorithm and the guaranteed algorithm one and the same.

---


### 85. [Reliable Neural Collapse Approximation for Open-World Test-Time Adaptation](https://arxiv.org/abs/2608.19890)

**<font color=#1a73e8>作者：</font>** Jia-Qi Lin, Yuangang Pan, Chang-Dong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-Time Adaptation (TTA) methods aim to bridge the domain gap between the source and target domains. However, traditional TTA methods become ineffective when the label distribution shift occurs, a challenge commonly referred to as an open-world scenario. In this paper, we introduce a new method named Reliable Neural Collapse approximation (ReNC) for Open-World Test-Time Adaptation (OWTTA). Specifically, we leverage neural collapse as a structural prior for reliable target-domain adaptation. Guided by this prior, we justify that the pre-trained classifier weights can serve as the prototypes of the source domain. By measuring the similarity between samples and prototypes, we filter out the Out-Of-Distribution~(OOD) samples for reliable updates. Furthermore, we propose a neural collapse approximation mechanism to refine these prototypes, ensuring they can gradually adapt to the target domain while maintaining the neural collapse structure. Extensive experiments on several open-world benchmarks demonstrate the superiority of the proposed method. Our empirical analysis suggests that ReNC better preserves NC-related properties in the target domain, providing useful evidence for explaining reliable OWTTA and offering new insights for model design. Code is available at this https URL.

---


### 86. [Unified and Efficient Point-Line Local Features](https://arxiv.org/abs/2608.19894)

**<font color=#1a73e8>作者：</font>** François Costa, Raphael Kreft, Eckhard Goedeke 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view computer vision pipelines typically rely on accurate sparse keypoints and robust descriptors. While incorporating line features has shown clear benefits for matching and pose estimation, existing point-line approaches remain inefficient: they detect points and lines separately, use increasingly heavy networks, and depend on CPU-bound heuristics that hinder real-time performance. We introduce a Unified Efficient Points and Lines (UPAL) feature extractor that jointly extracts keypoints, line segments, and feature descriptors within a single lightweight architecture. A shared backbone provides common representations that feed different branches for point and line features. Line segments are recovered through an accelerated post-processing stage, an enhanced and highly efficient variant of the LSD algorithm. UPAL matches or exceeds state-ofthe-art performance in both point and line applications while significantly reducing computational cost, achieving, for instance, a 4x speedup and 10x smaller memory footprint over the ALIKED + DeepLSD pipeline. Code is publicly available at this https URL.

---


### 87. [AvatarDynamizer: From Static to Dynamic Human Avatars via Generative Dynamic Textures](https://arxiv.org/abs/2608.19900)

**<font color=#1a73e8>作者：</font>** Guoxing Sun, Heming Zhu, Linjie Lyu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For full-body avatars, modeling surface dynamics is crucial for overcoming the uncanny valley and achieving perceptual realism. Person-agnostic methods recover static 3D avatars from monocular images, videos, or text prompts, but their skeleton-driven animations lack realistic surface dynamics such as clothing wrinkles. In contrast, person-specific methods achieve high-quality rendering and realistic dynamics, but require expensive multi-view captures for each individual. Recent generalizable dynamic avatar methods struggle to embed surface dynamics, leading to either limited multi-view consistency or dynamic expressiveness. To this end, we propose AvatarDynamizer, a generative method that transforms an off-the-shelf static 3D avatar into a controllable, realistic, and multi-view-consistent 4D avatar. We introduce a novel texture-space surface-dynamics embedding and formulate avatar dynamics modeling as conditional texture generation. Our encoder--decoder representation embeds pose-dependent dynamics into dynamic texture maps, enabling compatibility with pre-trained video diffusion models while decoding them into 3D Gaussians for multi-view consistent rendering. Since existing datasets are limited in scale, sequence length, or motion diversity, we collect a large-scale multi-view dataset with long sequences covering diverse skeletal motions and surface dynamics. Experiments show that our method effectively animates static avatars with faithful surface dynamics and outperforms competing generalizable methods in visual fidelity, especially under limited dynamic training data.

---


### 88. [Bringing analytic rigor to agentic AI for science: The Brain Researcher platform for neuroimaging data analysis](https://arxiv.org/abs/2608.19902)

**<font color=#1a73e8>作者：</font>** Zijiao Chen, Nicholas Lu, Xinhui Li 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can execute scientific analyses, but an analytic output becomes a defensible claim only after alternatives are weighed and the claim is limited to what the evidence supports. Agents may reproduce failures including selective analysis, premature declarations of success and optimization of imperfect criteria. We present Brain Researcher, an agentic research harness operating in a neuroimaging researcher's computational environment under rules for admissible analyses, required checks and claim scope. In benchmarks, Brain Researcher increased first-choice tool-selection accuracy across seven models by 70.2 percentage points (23.3% without it versus 93.6% with it) and verifiable grounding from 4.6% to 22.0%. In collaborator-led and self-evolving studies, multiverse analyses exposed analytic-choice sensitivity, and scientific review classified claims as accepted, qualified, revised, blocked, rejected or deferred. By linking decisions to evidence and provenance, Brain Researcher embeds methodological judgment within the workflow, not after it.

---


### 89. [PETA:Parameter-Efficient Test-Time Adaptation for Virtual Screening](https://arxiv.org/abs/2608.19906)

**<font color=#1a73e8>作者：</font>** Jia-Qi Lin, Yinghua Yao, Chang-Dong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurately ranking active ligands for a target protein pocket from massive chemical libraries remains a central challenge in virtual screening. DrugCLIP and its recent extensions substantially accelerate this process by encoding protein pockets and molecules into a shared embedding space. Despite this progress, further performance improvements typically require retraining the entire model, incurring substantial computational overhead and making target-specific customization inefficient. In this work, we formulate the specialization of pretrained virtual screening models to individual pockets as a test-time adaptation problem and propose PETA, a parameter-efficient framework that directly adapts pretrained model at test time. Given a target pocket, PETA constructs pocket-specific negatives through molecular diffusion and chemical validity filtering, and further moves them toward the reference ligand retrieved from structural databases via embedding-space mixup to create more challenging ranking tasks. A ranking objective then places greater emphasis on suppressing high-scoring invalid candidates that could contaminate the top-ranked screening results, providing structured supervision for lightweight adaptation. Experiments across diverse benchmarks demonstrate that this lightweight, pocket-specific adaptation outperforms both pretrained and fully retrained baselines while updating only the LayerNorm parameters, which account for approximately $0.03\%$ of the full model.

---


### 90. [Spike-based Belief Propagation in Nonlinear Dynamical Systems](https://arxiv.org/abs/2608.19907)

**<font color=#1a73e8>作者：</font>** Sepideh Adamiat, Hongye Wang, Wouter M. Kouw 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a Bayesian control framework that integrates spike-based dynamics with probabilistic inference for adaptive control. Bayesian inference is widely regarded as a core computational principle of brain function, providing a normative framework for perception, decision-making, and learning under uncertainty. By combining a biologically inspired spiking neural model with Bayesian inference principles, we propose a brain-like control algorithm capable of operating in uncertain environments. We use the mountain car parking problem as a benchmark with non-linear dynamics. Our results demonstrate that the proposed controller can successfully update states in real time and generate goal-directed action plans through spike-driven dynamics. The results highlight the proposed model's potential as a bridge between computational neuroscience and probabilistic control theory.

---


### 91. [Multi-Source Wasserstein Distributionally Robust Graph Learning](https://arxiv.org/abs/2608.19914)

**<font color=#1a73e8>作者：</font>** Chuansen Peng, Yifan Xia, Jinshan Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Network topology inference from graph signals is central to graph signal processing with applications in neuroscience, sensor, and social networks. In practice, target-domain samples are scarce while heterogeneous source-domain data are abundant. Fusing these sources is challenging: Euclidean averaging works for homogeneous sources but degrades sharply as inter-source divergence grows, collapsing distinct geometries into an inflated, biased consensus. We exploit the Wasserstein metric's distribution-preserving properties to counter heterogeneity while preserving each source's intrinsic geometry. We propose MS-WDRO, a multi-source Wasserstein distributionally robust graph learning framework that fuses heterogeneous sources via their weighted Wasserstein barycenter, a geometrically principled nominal distribution, then builds an ambiguity ball around it to hedge residual uncertainty. Minimizing worst-case risk yields a tractable regularized Laplacian estimator solved efficiently via a provably convergent ADMM scheme. We establish non-asymptotic guarantees: a finite-sample concentration bound for the empirical barycenter, a pooling bias lower bound proving naive aggregation is suboptimal, and an out-of-sample excess risk bound decaying at a parametric rate with only logarithmic dependence on source count. To calibrate hyperparameters governing robustness, sparsity, and source fusion, we unroll the solver into a differentiable architecture trained end-to-end, achieving data-adaptive calibration beyond cross-validation while retaining interpretability. Experiments on synthetic benchmarks and the multi-site ABIDE~I neuroimaging dataset show MS-WDRO consistently outperforms seven baselines in graph recovery, sample efficiency, and downstream diagnostic utility, with the largest gains in the sample-scarce regime.

---


### 92. [Auditing Recorded Predictive Lead Service-Line Classifications Against Physical Verification: A Statewide Study of New York](https://arxiv.org/abs/2608.19922)

**<font color=#1a73e8>作者：</font>** Muhammad Sarmad Sohail  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Under the US Lead and Copper Rule Revisions, a utility may determine a service line's material with a predictive model instead of inspecting it. New York State publishes, per address, which method was used. Almost no address carries both a model classification and a physical verification, so the check is between populations within a utility rather than paired addresses. We screen all 153 New York localities that classified at least 100 addresses this way. Seventy-five (49%), covering 125,990 addresses or 57% of those screened, record one value. Zero variance alone is not misconduct: 68 of the 75 match their own verification or have too little to test. Seven are contradicted by their own crews, six beyond any sampling explanation. Five are boroughs of New York City, which file as one system; one is East Rochester, 550 km away. New York City is the largest case: a predictive model is the recorded basis for 43,215 addresses, and on all of them the recorded material is "Known Other". The city records "Unknown" on 121,779 addresses, 1,880 already excavated, and lead on 120,692. In the model bucket both counts are zero, and the 95% upper bound on the rate is 0.0085%. Across the rest of New York the same method records lead or the hedge "Unknown but could be lead" on 12.21% of 176,888 addresses, a comparison whose weaknesses we report. The model-cleared population is newer, median year built 1984 against 1930, and construction era accounts for about a third of the gap and not the rest: holding era fixed, records-based classification finds lead at 4.3-31.9%, physical verification at 1.5-14.5%, the model in no era. Six era-aware estimators place the expected lead lines among them at 1,150-1,450. Two findings need no comparison: 7,782 of these addresses are in pre-1940 buildings, and the archived 2025 snapshot shows the public-side determination was copied from a customer-side model output.

---


### 93. [Securing Filesystems for Confidential Computing](https://arxiv.org/abs/2608.19924)

**<font color=#1a73e8>作者：</font>** Dimitra Giantsidi, Antoine Delignat-Lavaud, Cédric Fournet 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Confidential computing protects applications inside Trusted Execution Environments (TEEs), but it leaves storage vulnerable. Even with disk encryption, a malicious cloud provider can roll back, replay, fork, or tamper with disk state, breaking the integrity and freshness guarantees required by stateful applications. Existing solutions either assume trusted storage, incur high overheads, or push integrity logic into applications. We present ShieldFS, a POSIX-compliant filesystem that provides end-to-end integrity and freshness for persistent storage in the confidential-computing threat model without requiring application changes. ShieldFS represents permissible filesystem states using succinct cryptographic commitments, maintained inside TEEs and replicated in a lightweight trusted registry. On-disk data structures, including a write-ahead log and a storage pool, are authenticated using hash chains and an embedded Merkle tree. ShieldFS utilizes transactions and copy-on-write to update persistent filesystem state and commitments atomically. The commitments are verified during reads, ensuring that rollback, replay, and equivocation attacks are detected even when the entire I/O stack is untrusted. We implement the design by extending ZFS, yielding ShieldZFS. Evaluation with standard filesystem benchmarks and real-world workloads shows that ShieldZFS provides strong integrity and freshness guarantees with performance comparable to state-of-the-art filesystems.

---


### 94. [A Strong Linear Baseline for Whole-Heart Cardiac Shape Completion on CT, with an Open Eleven-Structure Statistical Shape Model](https://arxiv.org/abs/2608.19932)

**<font color=#1a73e8>作者：</font>** Matej Gazda, Jakub Gazda, Juraj Gazda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public cardiac cohorts annotate different subsets of the heart, so shapes from separate sources cannot be pooled without shared correspondence. Among released cardiac shape resources, none we identified carries the atrial appendage, pulmonary veins, and caval stumps as separate blocks in one mesh. Completion benchmarks also compare deep models against a least-squares projection onto shape modes, not the conditional estimator the same fitted model implies. We release an eleven- structure cardiac computed-tomography (CT) statistical shape model, built from 383 automatically labelled cases in 11 571-vertex correspondence, and compare completion estimators under one frozen internal split and endpoint. On a 76-case internal list held out from fitting, a closed-form conditional-Gaussian estimator reconstructed the missing non-chamber structures at 3.717 mm mean per-vertex error, averaged equally over one, three, five, and nine observed structures. A five-refit mask-conditioned graph variational autoencoder reached 5.248 mm and nearest-neighbour retrieval 8.931 mm. The paired difference was 1.531 mm (95% confidence interval 1.384 to 1.711), and the ordering held in a raw-coordinate sensitivity arm. Expert manual labels exist for 58 external CT cases, but our registered reference is close enough to score only five structures. There the closed-form estimator again had lower average surface distance, 95th-percentile Hausdorff distance, and Chamfer error for both completed atria. On a second public benchmark of 20 cases the reference was close enough for three of four completed structures, and the same ordering held there. Four structures have no expert reference. The released model and its completion operator support cohort-unification research on aligned CT, not clinical use.

---


### 95. [ShadowPath: Lookup-Private Credential Status Verification over Authenticated State](https://arxiv.org/abs/2608.19937)

**<font color=#1a73e8>作者：</font>** Patrick Herbke, Wolf Rieder, Christian René Sechting 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Verifiable credentials let holders present digitally signed claims without requiring the issuer to participate in every presentation. Revocation complicates this privacy model because a verifier must determine whether a credential remains valid. Existing status checks may expose recurring identifiers, registry positions, or request metadata. Such information can serve as stable handles to link separate presentations. ShadowPath moves the credential status lookup to the holder. For each presentation, the holder proves, in zero-knowledge, that the credential has not been revoked under the verifier-selected registry root. The verifier learns the status result but not observable metadata. To the best of our knowledge, we provide the first evaluation of Verkle trees for credential revocation and compare them with sparse Merkle trees to assess their applicability in real world applications. The comparison tests whether reducing path depth with Verkle trees offsets the higher cost of KZG-based authentication. Across 30 desktop trials, median Groth16 proving took 371.6ms with sparse Merkle and 2.11s with Verkle. Verification took 3.70ms and 7.55ms, respectively. Groth16 Verkle proving took about 3s on both primary mobile devices. The results show that shorter authenticated paths do not necessarily yield cheaper zero-knowledge proofs. With fresh session randomness, verifier-visible status data do not reveal whether two presentations use the same credential under the stated assumption of session-value independence. This guarantee excludes issuer-verifier collusion and synchronization traffic.

---


### 96. [Dynamic Gated Cross-Modal Fusion with Sarcastic-aware Contrastive Regularization for Multimodal Sarcasm Detection](https://arxiv.org/abs/2608.19942)

**<font color=#1a73e8>作者：</font>** Hao Guo, Subin Huang, Junjie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal sarcasm detection aims to identify sarcastic intent from multimodal content, where inconsistencies between literal meaning and contextual cues often signal irony. This task has attracted increasing research attention. However, accurate detection remains challenging due to instance-dependent modality contributions and misleading semantic consistency, where surface-level alignment masks underlying contradictory intent. Existing methods often rely on fixed fusion strategies and treat sarcasm as generic cross-modal mismatch, limiting their ability to capture subtle sarcasm cues and instance-specific modality interactions. To address these challenges, we propose a novel MSD framework that integrates Dynamic Gated Cross-Modal Fusion with Sarcastic-aware Contrastive Regularization (SaCR). Specifically, a bidirectional gated interaction module performs cross-modal feature filtering and adaptively calibrates textual and visual contributions at the instance level. A dynamic fusion gate further balances modality importance to generate more robust multimodal representations. Furthermore, SaCR is introduced as a label-aware contrastive regularization objective that encourages semantic consistency for non-sarcastic samples while suppressing misleading consistency in sarcastic cases. The proposed framework is trained end-to-end with a multi-objective learning strategy that jointly optimizes multimodal classification and auxiliary unimodal supervision. Extensive experiments on MMSD and MMSD2.0 demonstrate that the proposed method consistently outperforms strong baselines.

---


### 97. [Designing Human-mediated AI Guidance: Ready Together for Personalized Family Emergency Preparedness](https://arxiv.org/abs/2608.19950)

**<font color=#1a73e8>作者：</font>** Nini Kurashvili, Yana Ivanchenko, Greta Schiavo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) systems are increasingly used across domains to provide personalized information, recommendations, and decision support. However, in some contexts, AI-generated information may not be suitable for direct delivery to the final recipient. Instead, it may need to be interpreted, adapted, and communicated by a human who understands the recipient's needs, emotional state, and situational context. Human-AI interaction research has given less attention to situations in which a more knowledgeable human acts as an intermediary between an AI system and a less experienced or less informed recipient. We introduce the human-mediated AI guidance framework and explore it through Ready Together, an AI-supported family emergency preparedness system in which parents mediate AI-generated content for their children. The system is designed to provide personalized guidance and support parents in making emergency preparedness more interactive and understandable through guided activities and family-centered learning. The system design was informed by a qualitative, design-oriented research process involving semi-structured interviews and co-design activities. Findings identified challenges in family emergency preparedness, including difficulty discussing emergencies with children, uncertainty about providing appropriate explanations, and a preference for interactive learning activities. These findings informed the design of an interactive prototype, subsequently evaluated through a pilot study and a heuristic evaluation. Participants responded positively to the personalized recommendations and practical activities. Preliminary findings suggest that human-mediated AI guidance may support context-sensitive family preparedness while preserving parents' responsibility for interpreting, adapting, and communicating AI-generated information.

---


### 98. [Learning Early-to-Final Solution Consistency for MILP Acceleration](https://arxiv.org/abs/2608.19953)

**<font color=#1a73e8>作者：</font>** Guanlin Li, Chengrui Gao, Chenguang Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixed-Integer Linear Programming (MILP) is a fundamental problem class in operations research and combinatorial optimization, with broad applications to industrial decision-making. Owing to their NP-hardness, however, modern solvers may struggle to find high-quality solutions for challenging MILP instances within practical time limits. Recent learning-based approaches seek to accelerate MILP solving by directly predicting high-quality solutions from static instance-level features, such as variable-constraint bipartite graphs. Yet accurate solution prediction from instance features alone is difficult, and these methods largely overlook the information revealed during the solver's search process. In this paper, we find that solutions produced at the early search stage of MILP solvers, which are computationally cheap to obtain, are often structurally close to the solutions found after full-budget search. Motivated by this observation, we propose a new solver-informed paradigm that shifts the learning target from variable assignment to early-to-final consistency: for each variable, we predict whether its early-stage assignment should persist in full-budget solutions. The predicted consistency naturally guides downstream search, for instance by fixing the assignments deemed consistent. At inference time, we further ensemble consistency predictions across multiple early-stage solutions to improve robustness. Experiments across four MILP benchmarks show our method improves prediction-guided search across diverse downstream pipelines. With Gurobi, our proposed method reduces the primal gap by 56.9% on average and closes it completely on combinatorial auction instances. Besides, we transferred the Gurobi-trained model zero-shot to SCIP without adaptation, achieving a 36.4% average gap reduction across benchmarks.

---


### 99. [Tracking the Trend in How Speech Synthesizers Deceive People](https://arxiv.org/abs/2608.19959)

**<font color=#1a73e8>作者：</font>** Milan Šalko, Anton Firc, Kamil Malinka 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advances in speech synthesis have made deepfake audio highly realistic. Earlier studies reported 70-80% human detection accuracy, but relied primarily on older synthesizers. We compare human detection for three selected voice synthesis tools released in 2019, 2022, and 2024 with 82 IT professionals, and benchmark humans against six pretrained detectors on the same material. For fully synthetic speech (full spoofs), the F1 score drops from about 90% for RTVC and YourTTS to 48% for ElevenLabs, although listeners were explicitly warned that deepfakes were present. For partial spoofing, where only one sentence of an utterance is altered, strict accuracy falls to 9%, and listeners classify the synthetic sentence as bona fide 77% of the time. Humans and detectors fail in complementary ways, and neither reliably localizes short manipulations. Additionally, listeners increasingly mislabel bona fide speech as fake, eroding trust in unmanipulated audio. These findings show that human perception alone is unreliable for the selected modern and partial-spoof conditions and motivate procedural verification, provenance, watermarking, and segment-level detection.

---


### 100. [G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs](https://arxiv.org/abs/2608.19964)

**<font color=#1a73e8>作者：</font>** Bhavya Gupta, Onat Gungor, Tajana Rosing  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous driving systems must operate under partial observability, where safety-critical objects may be occluded or visible only to neighboring connected vehicles. Vehicle-to-vehicle cooperation can reduce this uncertainty, but existing cooperative driving methods often compress multi-agent evidence into latent features or hidden multimodal states. As a result, they obscure which agent observed each object, whether the object is visible to the ego vehicle, and how conflicting evidence affects downstream decisions. We propose G-MARK, a grounded multi-agent reasoning framework that converts cooperative object-centric observations into explicit provenance-aware knowledge graphs (KGs). The resulting KGs preserve object hypotheses together with their source attribution, ego-versus-partner visibility, uncertainty, conflicts, spatial relations, and planning-relevant context. G-MARK then derives a shared feature representation from these KGs, enabling lightweight task heads to support object reasoning, motion prediction, control selection, and trajectory forecasting. Compared with the state-of-the-art baseline, GMARK improves occlusion reasoning accuracy by 42.2%, reduces control-selection error by 13.1%, and achieves comparable trajectory-planning accuracy with a 25.6x smaller structured communication payload. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-155](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
