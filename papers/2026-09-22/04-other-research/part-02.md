# 📦 其他研究 | 2026年09月22日

> 本类共 **179** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-179](./part-04.md)

---

### 51. [Beyond Reference-Based Evaluation: Reward Models for Meta-Evaluation of Grammatical Error Correction](https://arxiv.org/abs/2609.21231)

**<font color=#1a73e8>作者：</font>** Ruotian Wu, Bill E. Johnson, Gene Saunders 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reference-based metrics for Grammatical Error Correction (GEC) such as M$^2$ and ERRANT assume that the reference set enumerates all valid edits, and therefore often penalize corrections that are grammatical and meaning-preserving but phrased differently. We introduce RM-EVAL, a reward model trained on human preference data from SEEDA, as a reference-free meta-evaluator that predicts human-like quality judgments at both full-sequence and partial-sequence levels. Beyond evaluation, we show that the same reward model can be used as a learning signal to improve GEC generation via Reward-Guided Text Generation (RGTG), which keeps a base GEC model frozen and performs online, reward-driven decoding. Across SEEDA, RM-EVAL achieves strong agreement with human rankings, and RGTG yields consistent gains in reward and external validation, demonstrating a unified framework for both assessing and enhancing GEC systems without relying on gold references.

---


### 52. [Self-Care and Mental Health: Mapping Over A Decade of HCI Interventions](https://arxiv.org/abs/2609.21239)

**<font color=#1a73e8>作者：</font>** Anna Fang, Tony Wang, Jenny Fu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Technology increasingly supports self-care for understanding and improving one's own mental health. HCI is at the center of the turn towards self-care technology, yet we lack an account of who these interventions serve, what practices they support, how technology mediates those practices, and assumptions underlying design for self-care. In order to characterize the current landscape and inform future research, we analyzed 91 SIGCHI papers that contribute HCI interventions for mental health self-care from the ACM Digital Library from 2015 through June 2026. Then, we conducted an interpretive synthesis to surface six orientations of self-care, which describe how HCI self-care interventions constitute care through shared assumptions regarding self, care, and technology. Overall, our work provides an interconnected vocabulary for positioning HCI mental health self-care, highlights changing responsibilities of care towards users, and discusses implications for providing a more situated account of HCI self-care technology in addressing the 'general' user.

---


### 53. [Multiclass Semantic Segmentation of Wildland Fire Images Using Context-Aware Centralized Copy-Paste Data Augmentation](https://arxiv.org/abs/2609.21241)

**<font color=#1a73e8>作者：</font>** Joon Tai Kim, Nishanth Kunchala, Vishv Patel 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Producing accurate annotations for deep learning based image segmentation is both costly and labor intensive. This challenge is especially evident in wildland fire applications, where accurately labeled datasets are scarce due to the difficulty of collecting and annotating dynamic fire scenes. To address this problem, our previous work introduced the Centralized Copy-Paste Data Augmentation (CCPDA) method for semantic segmentation of wildland fire imagery, which generates artificial training samples by randomly pasting fire clusters from source images onto target images. However, random placement can produce contextually unrealistic scenes, such as fire burning on asphalt. In this paper, we present a context-aware strategy designed specifically to improve data quality and realism in small multiclass wildland fire datasets, ensuring that augmented samples remain contextually meaningful. The proposed method restricts fire placement to semantically valid target regions and selects the location whose Ash-Vegetation composition most closely matches the source context. This approach preserves existing fire regions in the target image, prevents unrealistic placements, and maintains contextual accuracy by generating images that resemble real wildland fire scenes. We evaluate the Context-Aware CCPDA strategy through numerical analysis and comparisons with other augmentation methods by a weighted sum-based multi-objective optimization (MOO) approach. The results confirm that the context-aware data augmentation strategy leads to improved segmentation performance and contextual realism, outperforming other augmentation procedures.

---


### 54. [SafeStyle: Calibrated Style Residual Injection for Controllable Style-Leakage Trade-off in Diffusion Stylization](https://arxiv.org/abs/2609.21242)

**<font color=#1a73e8>作者：</font>** Zhangping Yang, Min Li, Song Yan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-guided diffusion stylization aims to transfer visual style from a reference image while preserving the semantics specified by a text prompt. However, image conditioning often entangles transferable style cues with reference-specific content, leading to an inherent trade-off: stronger conditioning improves style fidelity but increases content leakage, whereas aggressive suppression reduces leakage at the cost of style expression. This challenge is further complicated by the distinct spatial organization of texture- and geometry-dominant styles. To address these issues, we propose SafeStyle, a training-free framework for calibrated style residual injection in frozen diffusion models. SafeStyle first estimates style-supported and content-associated subspaces from compact calibration sets, preserving their informative overlap while suppressing useless content variations. It then transports the purified style evidence over adaptive spatial granularity and constrains its effective influence through an explicit residual-norm budget. Experiments across texture- and geometry-dominant styles show that SafeStyle achieves a DINO style similarity of 0.432 while maintaining competitive text alignment. On a semantically disjoint leakage-stress benchmark, it further achieves a DINO style similarity of 0.474 with only 0.8\% semantic leakage, demonstrating an effective balance between style fidelity and reference-content suppression.

---


### 55. [Geometry-Aware Diffusion Guidance via Curvature-Adaptive Tubular Correction](https://arxiv.org/abs/2609.21251)

**<font color=#1a73e8>作者：</font>** Enze Jiang, Jinwei He, Zheng Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gradient-guided diffusion samplers provide flexible priors for inverse problems and conditional generation, but strong guidance can move the sampling trajectory into regions where the learned score is poorly supported. Existing tangent-projection strategies limit first-order departure from an iso-density surface, yet discard potentially useful normal motion and overlook the second-order departure induced by tangent motion on a curved surface. We introduce curvature-adaptive tubular correction (CAT), a training-free plugin that regulates both effects within a shared, noise-dependent geometric budget. CAT decomposes the guidance gradient into normal and tangent components, charges normal displacement at first order and tangent displacement according to directional curvature, and obtains their jointly optimal magnitudes from a one-dimensional dual equation. Armijo backtracking calibrates the resulting finite step against the actual guidance objective, while matrix-free directional derivatives avoid constructing the full score Jacobian. We establish local guarantees for the tubular approximation, uniqueness of the correction, and sufficient objective decrease. Across seven inverse problems on FFHQ and ImageNet, CAT improves the evaluated pixel- and latent-space host samplers, with particularly consistent gains in perceptual metrics. It also improves black hole reconstruction on InverseBench and yields the lowest FID among the compared methods at every tested classifier-free guidance scale, while maintaining stable saturation and contrast. These results support curvature-aware tubular control as a reusable mechanism for stabilizing diffusion guidance.

---


### 56. [Two's a Crowd: Human and AI-Based Copresence for Developers with ADHD](https://arxiv.org/abs/2609.21254)

**<font color=#1a73e8>作者：</font>** Veronica Pimenova, Seth Bernstein, Shalini Madan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Effective collaboration and communication are vital to developer productivity and well-being, yet remain constrained by human factors such as attention, intrinsic motivation, and interpersonal accountability. These constraints are particularly vital for developers identifying with Attention Deficit Hyperactivity Disorder (ADHD), who navigate persistent environmental barriers in modern hybrid workplace settings. While developers with ADHD frequently rely on collaborative copresence practices (such as body doubling or pair programming) to support executive function, the recent emergence of agentic AI coding assistants has begun reshaping these collaborative dynamics. To investigate how developers with ADHD engage in human and AI-based copresence practices, we conducted semi-structured interviews with 14 software engineers with ADHD. Our findings reveal that while traditional human-human copresence provides critical social support and onboarding structure, it forces developers to constantly manage professional reputation and sacrifice personal privacy. Conversely, developers leverage emerging human-AI copresence to maintain accountability and cognitive flow without the social anxiety, performance judgment, or surveillance associated with human observation. Based on these empirical insights, we map developer copresence practices onto core dimensions of Goffman's copresence theory and Forsgren et al.'s SPACE framework of developer productivity, and provide design recommendations for AI-based tools that promote inclusive collaboration for developers with ADHD.

---


### 57. [Edit-VAR: Taming Visual Autoregressive Model for Precise Video Editing](https://arxiv.org/abs/2609.21268)

**<font color=#1a73e8>作者：</font>** Chongbo Zhao, Jiangming Wang, Xilai Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided video editing modifies target content while preserving the appearance and temporal coherence of unedited regions. Training-based approaches provide strong control but demand substantial data and computation. Training-free methods fall into inversion-free and inversion-based paradigms. Inversion-free approaches avoid trajectory recovery, but their source-preserving guidance can limit editing strength and leave semantic changes incomplete. Inversion-based approaches recover a latent trajectory before regeneration, where approximation errors can accumulate and cause source-content drift and temporal inconsistency. We introduce Edit-VAR, the first training-free and inversion-free framework for text-guided video editing with a pretrained visual autoregressive video model. Edit-VAR directly encodes the source video into multi-scale discrete tokens and performs probability-guided conditional token replacement for source preservation. Attention-guided token-wise and scale-aware modulation selectively relaxes source constraints over edit-relevant positions and generation stages. Scale-Decoupled Generation, implemented as late-scale constraint release, regenerates motion-consistent details and reduces texture fragmentation. Residual-guided token pruning further exploits redundancy at the final two high-resolution scales to reduce inference cost. Extensive experiments and a blind user study demonstrate that Edit-VAR outperforms existing training-free video editing methods overall in editing fidelity, source preservation, temporal coherence, and inference efficiency.

---


### 58. [Transcript-Bound Combiners for Downgrade-Resilient Hybrid Post-Quantum Key Establishment: Definition, Proof, and Embedded-Device Cost](https://arxiv.org/abs/2609.21273)

**<font color=#1a73e8>作者：</font>** Bhanwar Gupta, Sanjeev Rana  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hybrid key establishment runs a post-quantum key-encapsulation mechanism (KEM) alongside a classical Diffie-Hellman primitive, so that the session key stays secure while either component resists attack. This design is now standardized in the Transport Layer Security protocol, Secure Shell, and the Internet Key Exchange, with the standardized module-lattice KEM (ML-KEM) as the post-quantum component. A hybrid KEM secures the derived key, but not the integrity of the negotiation that selects which primitives are used. Full protocols authenticate that negotiation through a handshake transcript; a hybrid KEM deployed as a standalone drop-in primitive, or inside a minimal handshake without transcript authentication, inherits no such guarantee, and an active attacker can strip the post-quantum option. We ask what the key schedule alone must contain to make downgrade resilience a local property of the combiner. We give a game-based definition at the combiner layer and prove a two-sided separation: a combiner that ignores the transcript is downgraded with certainty, whereas one that binds the session key and the confirmation tag to a hash of the transcript blocks every such attempt, up to a term negligible for a 256-bit transcript hash. We also give an explicit strongest-link security bound. Using a calibrated cost model composed from published Cortex-M4 measurements, transcript binding adds one hash per party - about 11.8% of handshake computation but only 1.5% of radio-inclusive energy - and adds no messages or bytes on the wire. Every reported number is produced by a released harness that passes a 30-check validation gate.

---


### 59. [MIRCID: Inferred Hub-miRNAs Drive Cross-Task Improvements in Drug Mechanistic Modeling](https://arxiv.org/abs/2609.21280)

**<font color=#1a73e8>作者：</font>** Xin Cao, Yigang Chen, Jiatong Xu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug mechanism-of-action (MoA) modeling commonly relies on perturbational transcriptomes, but matched microRNA (miRNA) measurements are often unavailable. Inferred regulatory features offer a scalable way to reuse these data. Here, we present MIRCID, a framework comparing gene expression with inferred transcription factor (TF) activity and miRNA expression across pathway classification and similarity-based MoA retrieval. HubmiRNet infers 414 pan-cancer hub miRNAs (HubmiRs) from 977 L1000 landmark genes, achieving a Pearson correlation coefficient of 87.72\%; its 1,298-output variant also outperformed SiCmiR on the full-miRNA task (71.21\% versus 67.30\%). In the evaluated comparisons, miRNA augmentation provided more consistent gains than TF activity. Generic embedding controls showed model-dependent utility, while complementarity analyses identified a distinct, partially linearly recoverable representation that retained gene-derived structure. Illustrative rescue cases linked improved classification to biologically plausible miRNA patterns in samples with weak transcriptional signatures. These findings support inferred HubmiRs as a biologically informed recoding of transcriptomic data for perturbational drug modeling, while leaving recovery of measured perturbational miRNA responses to further validation.

---


### 60. [Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding](https://arxiv.org/abs/2609.21288)

**<font color=#1a73e8>作者：</font>** Chenqian Le, Beatrice Fumagalli, Yasamin Esmaeili 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surface electromyography (sEMG)-based silent speech interfaces are limited by cross-user variability and calibration burden. We study a limited-data setting in which each of 27 speech-typical participants contributed less than 0.5 h of data (21.3 min on average) across Aloud and Mimed speech. Within a closed 50-sentence corpus, we used leave-one-subject-out evaluation, initializing from a released single-subject checkpoint, pretraining on non-held-out participants, and fine-tuning on the target participant. This pipeline achieved 21.7% character error rate (CER) and 31.9% word error rate (WER), compared with 49.3% CER without target-subject calibration and 68.0% CER for direct checkpoint fine-tuning. Multi-subject pretraining from random initialization followed by fine-tuning reached 44.9% CER and did not converge under the fixed schedule in 5 of 27 folds, indicating substantial optimization and accuracy benefits from checkpoint initialization. Macro-averaged CER declined from 74.4% with one pretraining participant to 21.7% with 26. Three minutes of target-subject calibration achieved 20.5% CER and 31.7% WER, with no statistically significant difference from the full approximately 13-min pool (21.7% CER and 31.9% WER). A subject-specific adapter provided no detectable benefit. Excluding the five evaluation sentences from all sEMG model-training data increased CER and WER to 78.6% and 99.9%. These results support short-calibration personalization in a standardized-montage, closed-corpus setting.

---


### 61. [Identifying Security Platform Product Abuse with Machine Learning](https://arxiv.org/abs/2609.21303)

**<font color=#1a73e8>作者：</font>** Shaefer Drew, Michael Brautbar, Paul Knight 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Product abuse is an individually rare, but growing, problem across the SaaS industry. Highly sophisticated threat actors can misuse security platforms within customer environments or conduct bypass experiments on the product itself. Threat actors can leverage living-off-the-land (LOTL) attacks to avoid using cumbersome, frequently detected malware. Remediating this threat requires collecting multiple data modalities across different types of databases, addressing a cold-start problem in the intrinsic rarity of such sophisticated but dangerous events, and designing within the constraints of real-world deployment (e.g., cost, user behavior, performance, etc). To wit, we provide the first study of such a whole-system defense, especially with respect to a deployed and operational capability. Our results show an increase in product abuse coverage by 35\%, a 30\% reduction in monthly alerts, and adaptability to changes in malicious actors' behavior. We review both the constraints we considered in designing the system to meet operational requirements and a retrospective evaluation of the value of explainable features and counterfactual performance on previously identified attacks.

---


### 62. [Combining Object Detection with Geometry-Aware Clustering to Distinguish Overlapping Plants in UAV Imagery](https://arxiv.org/abs/2609.21304)

**<font color=#1a73e8>作者：</font>** Ik Jae Lee, Hieu D. Nguyen, Mahbubur Meenar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable plant-level information from unmanned aerial vehicle (UAV) imagery is important for automated crop monitoring. However, in dense crop canopies, adjacent plants frequently overlap and are detected as a single object, reducing the reliability of plant-level measurements. This study presents a geometry-aware post-detection framework for resolving overlapping plant instances using standard RGB UAV imagery.
The framework combines object detection with geometric clustering of plant components. Leaves or branches detected within each bush-level region are represented using two complementary geometric features: component centroids and radial intersection points (RIPs) derived from detected plant structures. K-means and Gaussian mixture models determine whether a detected region contains a single plant or two overlapping plants. Density filtering suppresses spurious radial intersections, and a post-pipeline ensemble combines spatial and directional geometric information.
The framework was evaluated using UAV imagery of eggplant and tomato crops under field conditions. Centroid-based clustering achieved an F1-score of 0.89 for eggplant, while the combined centroid-RIP approach achieved the best tomato performance, with an accuracy of 0.80, precision of 1.00, and F1-score of 0.75 using K-means. Density filtering substantially improved RIP-based clustering for tomato.
The proposed approach provides a lightweight, modular engineering solution that can be integrated with existing RGB UAV monitoring pipelines without additional depth sensors, pixel-level segmentation, three-dimensional reconstruction, or retraining of the primary bush detector. The results demonstrate that geometric reasoning applied to existing detector outputs can complement deep-learning-based object detection and improve plant-level interpretation in dense agricultural canopies.

---


### 63. [Fast And Accurate Text Content File Type Identification](https://arxiv.org/abs/2609.21306)

**<font color=#1a73e8>作者：</font>** Manu Nandan, Michael Brautbar, Edward Raff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A common requirement across organizations is to have a tool that can identify file types based on their contents, particularly in the cybersecurity domain where magic numbers and file extensions can not be trusted. While existing tools work well in practice, there is plenty of room for improvement either in terms of computational load and time for detection in the case of model based tools like Magika or in terms of accuracy of detection in the case of file parsing tools that use programming language constructs. In this study, we propose a neural network model for identification of types of text content files, especially source code, that is more accurate and faster than other available tools. Our experiments on open-source files indicate that it is not only more accurate on average for text-content file-type identification, but also approximately four times faster than Magika, while being 28% smaller in size.

---


### 64. [An Introduction to Compression-Based Machine Learning](https://arxiv.org/abs/2609.21309)

**<font color=#1a73e8>作者：</font>** John Hurwitz, Edward Raff, Charles K. Nicholas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Any lossless compression algorithm (like gzip) may be converted into a machine learning method, via either Normalized Compression Distance or the Minimum Description Length principle. Any auto-regressive model may be converted into a lossless compression method via entropy coding. This seemingly circular dependence has unrealized potential in modern artificial intelligence and machine learning, and we survey and formalize the various strategies that have been used to leverage compression for machine learning. We introduce and empirically validate a design framework for compression-based ML, finding compression-based methods competitive with conventional baselines and decisively stronger on malware. We find that varying these design choices yields accuracy gains of up to 0.62.

---


### 65. [S3VD: Semantic-Guidance Spatio-Temporal Scanning for Video Deraining](https://arxiv.org/abs/2609.21322)

**<font color=#1a73e8>作者：</font>** Kui Jiang, Yiang Chen, Yan Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Heavy rainfall severely degrades outdoor videos by corrupting high-frequency details and introducing motion blur, critically undermining the reliability of visual tasks. Recently, State Space Models (SSMs), particularly Mamba, have emerged as efficient alternatives for vision tasks with their linear complexity and ability to model long-range dependencies. However, when confronted with the poor visual representations in rainy videos, Mamba still faces difficulties in preserving the integrity of 2D spatial semantics and modeling 3D spatio-temporal correlations. To break these limitations, we introduce S3VD, a Semantic-Guidance Spatio-Temporal Scanning framework for video deraining, featuring two key innovations: Multi-Scale Semantic Fusion (MSSF) Module and Spatio-Temporal Scanning Fusion (STSF) Module. The former integrates temporal semantic priors from DINOv2 to guide precise feature representation and counteract the loss of local semantic context inherent to Mamba's 1D flatten operation, enhancing robustness against extreme degradation. The latter introduces a spatio-temporal scanning mechanism and devises a Decoupled-Gating Mamba (DG-Mamba) layer, which employs two independent gates to adaptively control preceding and subsequent contextual information within the input clip, optimizing intra-frame and inter-frame correlation modeling. Experiments on video deraining benchmarks demonstrate the superiority of S3VD, achieving state-of-the-art performance with an average 0.84 dB PSNR improvement over Mamba-based baselines.

---


### 66. [LEGIT: Credentialing Protocol for Trustworthy AI Agent Marketplaces](https://arxiv.org/abs/2609.21325)

**<font color=#1a73e8>作者：</font>** Steve Drew, Jiayu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic marketplaces are emerging where AI agents with varying capabilities autonomously complete specialized tasks for buyers. A major challenge of such marketplaces is that buyers cannot easily determine which agent will perform best on their tasks. Reported benchmark scores may be difficult to verify or compare across tasks, software, and budgets. We introduce LEGIT, a credentialing protocol connecting certification, reputation, and proposed marketplace allocation. Certification binds measured quality and cost per solved task to an agent configuration, task domain, evaluation budget, and evidence through a signed record. Reputation links records of past task outcomes to the same identity, subject to the reliability of the reported feedback. Buyers and agents can verify credential records and inspect optional visual profiles. Evaluations reveal cost differences between agent configurations with similar observed task success, and show that comparisons depend on the evaluation budget. These results support binding performance measurements to the tested configuration and resource limits. A complementary analysis quantifies the deposits and fees required for reputation manipulation under a stated Sybil attack model.

---


### 67. [Deep Reinforcement Learning with Buffered Quantile Objectives](https://arxiv.org/abs/2609.21327)

**<font color=#1a73e8>作者：</font>** Mohammad Alipour-vaezi, Sajad Khodadadian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantile-based reinforcement learning provides an interpretable approach to risk-sensitive decision-making by optimizing a prescribed quantile of the cumulative-return distribution. Despite this appeal, learning under a point quantile objective is challenging: quantiles can change abruptly under small perturbations of the return distribution, and exact quantile-sensitive planning requires computationally demanding distributional optimization. Lower-buffered quantiles alleviate the former difficulty by averaging neighboring quantiles immediately below the target level, providing a smoother surrogate while preserving the underlying point-quantile objective. Existing methods based on this principle, however, remain model-based and rely on explicit return-law planning, limiting their applicability beyond small tabular problems. We develop Deep-BQRL, a model-free distributional reinforcement-learning framework that extends buffered-quantile learning to neural function approximation. The method learns conditional return quantiles directly from sampled transitions, constructs buffered action scores from the relevant region of the learned quantile function, and uses ensemble disagreement to guide exploration. An augmented input representation allows the learned policy to respond to trajectory information without explicitly reproducing the quantile-state recursion required by exact planning. Experiments on an asset-selling optimal-stopping problem and slippery FrozenLake compare Deep-BQRL with model-based UCB-BQRL and tabular PPO and TRPO implementations. In asset selling, Deep-BQRL attains smaller mean cumulative point-quantile policy gaps than PPO and TRPO at the reported target levels, while UCB-BQRL retains the smallest gaps. The learned stopping decisions also vary with the target quantile, providing an interpretable illustration of the method's risk-sensitive behavior.

---


### 68. [Routine Blood Tests Outperform CRP for Distinguishing Bacterial From Viral Infection in Children](https://arxiv.org/abs/2609.21332)

**<font color=#1a73e8>作者：</font>** Mihaela Demireva, Zhecho Mitev, Djuna Chinareva-Klimentova 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Acute infectious diseases are among the leading causes of medical consultations and hospitalizations in children worldwide. These infections are predominantly caused by viruses or bacteria, yet differentiating between the two remains a common clinical challenge. As a result, pediatricians often default to the safer option of prescribing antibiotics contributing to the growing problem of antimicrobial resistance. The objective is to assess the additional predictive value of CBC towards determining the current infection. This retrospective study used data from 906 pediatric patients aged between 2 and 14 years who were tested positive either for viral or bacterial infection between 2022 and 2026. Inclusion criteria further required availability of CBC results and CRP level measurements. These laboratory parameters as well as age were used as input features for several supervised classification models. Model performance was evaluated using AUC, sensitivity and specificity. The best performing model is XGBoost, which included all features, achieving out of-sample performance of AUC of 81.7% and sensitivity of 70.8%, specificity of 79.2%. All trained models outperform a CRP-based only decision-rule model in terms of AUC. We suggest that the decision to prescribe antibiotics should be based on a number of factors, including but not limited to CBC, some of which are not currently incorporated into routine practice.

---


### 69. [Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization](https://arxiv.org/abs/2609.21347)

**<font color=#1a73e8>作者：</font>** Xiangfei Guo, Hao Shi, Yufan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in 3D Gaussian Splatting (3DGS) has enabled dense visual SLAM with pinhole cameras, yet most pipelines are not designed for panoramic imagery. We present Cube-Splat, the first panoramic GS-SLAM framework that factorizes each 360° frame into a cubemap of four fixed-orientation virtual pinhole views sharing a single optical center. By designating the front face as the primary pose state, we accumulate gradients from all faces via an adjoint mapping, thereby enabling multi-face observations to coherently update a single state while strictly preserving cross-view geometric consistency. Concurrently, our mapping module densifies and optimizes anisotropic Gaussians using aggregated cubemap rays for high-fidelity, dense reconstruction. Furthermore, to rigorously evaluate panoramic SLAM under diverse and challenging conditions, we introduce SynPano, a highly scalable, photorealistic synthetic dataset featuring parameterized complex trajectories and multi-modal ground truth. Extensive evaluations on two public benchmarks (PALVIO and OmniBlender) and our SynPano dataset, collectively encompassing both indoor and outdoor scenes, demonstrate that Cube-Splat achieves state-of-the-art (SOTA) performance in tracking accuracy and reconstruction fidelity. Both the source code and the SynPano dataset are available at this https URL.

---


### 70. [Field Tracking of Insects Using a Stereoscopic Event-Based Camera Setup](https://arxiv.org/abs/2609.21354)

**<font color=#1a73e8>作者：</font>** Pratham G. Shenwai, Martin J. Lankheet, John T. Hrynuk 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-speed tracking of small, fast-moving organisms in their natural environments is important to better understand their behavior and ecology. Traditional frame-based imaging suffers from motion blur due to low temporal resolution, and data storage limitations, propelling a search for more adaptive solutions. Event cameras, which capture changes in brightness at pixel level instead of entire frames, have emerged as a promising solution by increasing temporal resolution and data efficiency. Here, we demonstrate the use of event-based imaging with standard video-based processing methods by converting the asynchronous events into conventional video formats, allowing us to leverage the event camera's enhanced temporal detail to capture intricate insect flight movements and apply established image analysis techniques. Coupling this conversion process with a stereoscopic configuration provides continuous, low-latency, three-dimensional tracking of fast-moving subjects in field conditions. As a result, we substantially mitigate motion artifacts and achieve more accurate representations of animal movements. By making event-based imaging more readily applicable in natural field settings, our method support broader applications across animal behavior and ecological research, agricultural management, and other fields requiring high-fidelity object tracking in the wild.

---


### 71. [Batched Paillier-Based Hamming-Distance Computation over Binary Embeddings](https://arxiv.org/abs/2609.21364)

**<font color=#1a73e8>作者：</font>** Yavor Litchev, Liwen Ouyang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Additively homomorphic encryption supports outsourced computation on encrypted binary embeddings, but large-integer arithmetic and data movement can limit throughput. We describe a Paillier-based client that combines a carry-separated binary encoding, table-based encryption, reduced-exponent decryption, CUDA/CGBN arithmetic, persistent device state, and batched retrieval integration. We establish the encoding's correctness and characterize four CPU and GPU client configurations. The lookup configuration uses a 280-bit exponent-size parameter. Across 3 warm-state trials on batches of 10,000 random 512-bit embeddings, the lookup GPU configuration achieved median-batch throughputs of 43,091 encryptions/s and 28,983 Hamming- distance decodes/s. Its amortized costs were 0.0232 ms and 0.0345 ms per vector, corresponding to factors of 453.8 and 200.9 relative to the measured CPU baseline. These implementation- specific results demonstrate the throughput benefits of combining cryptographic precomputation, batched accelerator execution, and persistent runtime state. The study distinguishes warm-batch performance from isolated-request latency and identifies the remaining costs of initialization, transport, and retrieval integration.

---


### 72. [RobotEQ-Video: A Video-Centric Benchmark for Social Proactive Intelligence with World-State Taxonomy](https://arxiv.org/abs/2609.21371)

**<font color=#1a73e8>作者：</font>** Xinyi Che, Zheng Lian, Kuofei Fang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Social Proactive Intelligence (SPI) extends proactive assistance beyond task completeness to consider social appropriateness in diverse embodied scenarios. However, prior SPI research faces two key limitations. First, existing work focuses on static images, whereas dynamic videos provide crucial cues for inferring human states and needs, offering richer information than isolated images. Second, prior work often relies on free-form data collection pipelines, which fail to guarantee comprehensive coverage of diverse scenarios. To address these gaps, we introduce RobotEQ-Video, shifting the focus from image-centric to video-centric analysis. To ensure comprehensive video coverage, we construct a hierarchical world-state taxonomy organized into a four-level coarse-to-fine structure, comprising 6 domains, 20 dimensions, 142 level-1 attributes, and 816 level-2 attributes. The resulting benchmark comprises 2K+ videos with 100K+ human annotations and 16K+ labels for assessing behavior properness. Benchmark evaluation reveals that current systems remain unreliable and fall short of human performance. We further explore how world models can help tackle this task. This work advances SPI research from static images to dynamic videos and ensures more comprehensive scenario coverage during benchmarking.

---


### 73. [JEPA Guided Diffusion: Predictive Vision-Language Conditioning for Generative Traffic Forecasting](https://arxiv.org/abs/2609.21379)

**<font color=#1a73e8>作者：</font>** Trinh Tra Giang Nguyen, Thanh Nguyen Vo, Nguyen Hoai Thuong Bui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate traffic forecasting requires both understanding scene dynamics and synthesizing realistic future observations. Recent diffusion-based video generation models produce visually plausible predictions but require expensive end-to-end training and often entangle scene understanding with image synthesis. In this work, we propose a decoupled forecasting framework that separates future representation learning from video generation. A frozen V-JEPA encoder first extracts predictive latent representations from the observed traffic videos, capturing the underlying scene dynamics in a semantic latent space. A lightweight latent alignment module then projects these representations into the conditioning space of a frozen Cosmos diffusion module, enabling future video synthesis without retraining the large generative model. By freezing all foundation models and training only the lightweight alignment module, the proposed framework substantially reduces optimization complexity while preserving forecasting capability. Experimental results on the AI City Challenge 2026 Track 5 benchmark demonstrate that the proposed method achieved a score of 75.1297, ranking third in the competition. These results suggest that predictive world representations learned by V-JEPA can effectively guide downstream video generation, providing a practical and efficient alternative to end-to-end diffusion-based forecasting.

---


### 74. [Knowledge-Graph-Augmented Chronos-2 for HEC-RAS Surrogate Forecasting](https://arxiv.org/abs/2609.21381)

**<font color=#1a73e8>作者：</font>** Edward Holmberg, Elias Ioup, Mahdi Abdelguerfi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether coupling a time-series foundation model to hydraulic project knowledge improves surrogate forecasting of HEC-RAS water-surface elevation (WSE). We present KG-Chronos-2, which combines a frozen Chronos-2 predictor with exact-state residual decoding, graph-conditioned historical retrieval, and input-aligned correction. We compare the method with persistence, a residual LSTM, project-conditioned recurrent GeoFNO, a hydraulic DCRNN-style model, and frozen Chronos-2. Task-specific fitting uses the 2008 simulation. Evaluation covers 64 fixed 24-hour windows from the 2011 and 2002 simulations at 4,675 cross sections in 71 reaches on a shared geometry. KG-Chronos-2 achieves event-balanced root-mean-square error 0.246970 in native WSE units. It reduces RMSE by 14.13% relative to frozen Chronos-2, 29.38% relative to the hydraulic DCRNN-style model, and 39.54% relative to recurrent GeoFNO. The 95% hierarchical-bootstrap interval for its event-balanced RMSE difference from frozen Chronos-2 is [-0.075177, -0.016317]. KG-Chronos-2 also achieves the lowest active-window and final-lead RMSE among the six completed systems. These results support coupling a frozen temporal predictor to project knowledge for warm-start HEC-RAS forecasting on the fixed benchmark.

---


### 75. [Probabilistic Forecasting of Business Process Executions with Neural Temporal Point Processes](https://arxiv.org/abs/2609.21382)

**<font color=#1a73e8>作者：</font>** Jiaxin Yuan, Daniela Grigori, Han van der Aa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operators of service-based systems act on forecasts of how a running execution will continue, and such a forecast is actionable only if its reliability is known. Mainstream deep-learning models for this task are discriminative and deterministic: they emit a single next activity and a single remaining-time estimate, without a distribution to reason over. We instead cast the problem as generative sequence modelling with marked temporal point processes, which define a joint density over the next mark and its inter-event time and therefore deliver predictive distributions by construction. Real event logs violate the simple-point-process assumption these models rest on, since consecutive events frequently carry identical timestamps; we handle such ties explicitly and combine a transformer encoder with a mixture decoder over inter-event times, trained by exact log-likelihood. On ten public logs, the resulting model matches discriminative baselines on point accuracy, dominates them on the calibration and sharpness of remaining-time distributions, and is the cheapest at inference, since a full predictive distribution is obtained in a single forward pass without sampling.

---


### 76. [SIRA: Reasoning-Aware Surgical Instrument Segmentation via Query-Anchored Alignment](https://arxiv.org/abs/2609.21402)

**<font color=#1a73e8>作者：</font>** Zhibo Zhang, Qijie Wang, Zengqiang Yan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical instrument segmentation (SIS) plays a critical role in robotic assistance and surgical workflow analysis. However, most existing SIS methods formulate segmentation as a category-driven localization problem, limiting their ability to capture procedural context and task-dependent semantics in surgical workflows. We introduce Reasoning-Aware Surgical Instrument Segmentation (RA-SIS), a task formulation that frames segmentation as query-conditioned inference under surgical context. To benchmark this setting, we construct SurgRS, a surgical reasoning segmentation dataset consisting of 41,000 image-text pairs, which aligns instance-level masks with structured query-answer supervision to enable semantic grounding at the pixel level. Based on SurgRS, we propose Surgical Instrument Reasoning and Segmentation Assistant (SIRA), a multimodal framework that disentangles target-level and query-level semantics and integrates them with visual features through query-anchored dual alignment. By aligning query semantics with spatial features and segmentation prompts, SIRA enhances semantic-visual consistency in mask prediction. Extensive experiments on SurgRS demonstrate improvements over existing reasoning-aware baselines. Code is available at this https URL.

---


### 77. [Quantization-Aware Kalman Estimation for Diffusion Sampling](https://arxiv.org/abs/2609.21407)

**<font color=#1a73e8>作者：</font>** Qitan Shi, Cheng Jin, Jiawei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantization offers a practical path to deploying diffusion models with reduced memory and computation, but aggressive compression can cause quantized outputs to deviate substantially from their full-precision counterparts. Sampling-stage correction methods seek to compensate for such deviations during sampling, but existing approaches rely primarily on local information and underexploit trajectory history, limiting their ability to correct errors that propagate across timesteps. In this work, we formulate sampling with a quantized denoiser as an online estimation problem, using the history of quantized denoiser outputs to recover the underlying full-precision outputs required by the sampler. We propose QuAKE, a Quantization-Aware Kalman Estimator that combines a smooth trajectory prior with a conditional Gaussian observation model. At each sampling step, QuAKE recursively updates the posterior over the output window in closed form and feeds its posterior mean to the sampler. QuAKE is a lightweight plug-and-play corrector that requires no modification to the quantized network and naturally supports arbitrary high-order multistep ODE samplers. Experiments across W4A4-quantized text-to-image diffusion models show that QuAKE consistently outperforms existing methods in reducing the distributional discrepancy from full-precision sampling.

---


### 78. [When Online Adaptation Hurts: Parameter-Frozen Test-Time Ensembling for Continual Medical Image Segmentation](https://arxiv.org/abs/2609.21412)

**<font color=#1a73e8>作者：</font>** Ruijie Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmenters often get worse when sites, scanner vendors, or protocols change. Continual test-time adaptation (CTTA) addresses this problem without target labels, but it can be impossible to update a model on a non-stationary stream and can lead to a lot of errors. We examine a more reasonable and meaningful alternative: parameter-frozen inference enhancement(PIE). We use a source-trained segmenter that learns about anatomy-preserving scale and flip views, maps their predictions back to the native location, and averages the probabilities. We do not modify the weights of the model or the normalization statistics. On a cardiac MRI stream from M\&Ms, which is trained on vendor A and evaluated sequentially on vendors B, C, and D, PIE has 0.7786 mean Dice, compared to 0.7680 for source-only inference and 0.7388--0.7416 for five other online-adaptation baselines. The controlled ablations show that performance saturates at 28 views, and confidence weighting, class-prior correction, connected-component filtering, morphological refinement, and inter-slice smoothing have no effect or cause negative transfer. Qualitative results on cardiac MRI and fundus images are also consistent with the frozen ensemble keeping thinner and nested anatomical structures. These results provide a strong, stable baseline for medical CTTA and expose an important failure mode: adaptation and handcrafted refinement can be less reliable than carefully designed inference.

---


### 79. [TrustBOM: A Scalable Architecture for Confidentiality-Preserving SBOMs Across Organizations](https://arxiv.org/abs/2609.21419)

**<font color=#1a73e8>作者：</font>** Van Thang Nguyen, Frederic Rupprecht, Tom Lawrence 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software Bills of Materials (SBOMs) have emerged as a key mechanism for software supply chain governance in enterprise architectures. However, their adoption across organizations remains limited due to concerns about exposing sensitive dependency information. To address this limitation, we propose TrustBOM, a scalable architecture for confidentiality-preserving SBOMs integrated into enterprise CI/CD workflows. TrustBOM enables software providers to attest that specific vulnerabilities or restricted licenses are absent from their software without revealing the underlying dependency graph. This is achieved using zero-knowledge non-membership proofs, which are applied selectively based on consumer-defined policy constraints. The architecture ensures that proof generation scales linearly with the number of asserted constraints rather than with the size of the SBOM, enabling efficient operation in large-scale enterprise environments. Empirical evaluation demonstrates linear performance, with an average proof generation time of 0.9 seconds per constraint on commodity hardware, indicating the feasibility of deployment in enterprise platform ecosystems.

---


### 80. [P$^3$-SAM: SAM with Perceptual Parallel Prompt for Few-Shot Strip Steel Surface Defect Segmentation](https://arxiv.org/abs/2609.21424)

**<font color=#1a73e8>作者：</font>** Qian Xu, Hang Xiong, Anpeng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot semantic segmentation (FSS) of strip steel surface defects (S$^3$D) has posed significant challenges distinct from natural scenes. Unlike natural images, S$^3$D task exhibits unique characteristics including low local contrast, uneven illumination, and complex fine-grained texture patterns. Although recent methods based on Segment Anything Model (SAM) have shown promise in FSS on natural images by leveraging SAM's powerful pre-trained representations, these unique industrial characteristics of S$^3$D images lead to performance drop when directly applying SAM to industrial defect scenarios. In this paper, we propose a novel Perceptual Parallel Prompt (P$^3$) framework that empowers SAM, creating the P$^3$-SAM model to address these challenges through two core strategies. First, we develop a Perceptual-Optimized Encoding (POE) strategy that enhances local contrast and preserves critical texture details for S$^3$D segmentation. Second, we introduce the Parallel Prompt Generator (PPG) strategy that simultaneously generates both semantic and spatial prompts, enabling comprehensive guidance for SAM's decoder across varying images. Extensive experiments on three few-shot S$^3$D benchmarks demonstrate that P$^3$-SAM achieves state-of-the-art performance, with particularly notable improvements of 12.00% in mIoU on Surface Defects-4i dataset.

---


### 81. [DEFEAT: Stitching Fragmented File I/O Contexts for Early Ransomware Detection](https://arxiv.org/abs/2609.21426)

**<font color=#1a73e8>作者：</font>** Muhammad Ejaz Ahmed, Hyoungshick Kim, Mohsen Ali Alawami 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ransomware increasingly fragments its file operations across temporary and intermediate files, scattering the semantic context that links individual I/O events to an overarching encryption campaign. This fragmentation defeats existing detectors that reason over isolated file streams -- whether pattern-based methods that match rigid event sequences or learning-based methods that require accumulating statistical evidence across many files. We present DEFEAT, a framework that reconstructs this fragmented, scattered context by grouping causally related file events into File Event Gadgets (FEGs), semantically coherent units that capture the full intent behind sequences of file operations spanning multiple dynamically created files. Unlike provenance graphs (system-wide causal graphs that record relationships among all OS entities, such as processes, files, sockets, and registry keys, across the entire system), FEGs are scoped to the file-operation context of a single user asset, enabling lightweight, targeted analysis without whole-system instrumentation. Each FEG is modelled as an attributed control flow graph (ACFG) and embedded via a graph neural network for unsupervised clustering, enabling analysts to label entire behavioural clusters rather than individual samples, reducing annotation effort by 94%. Evaluated on a corpus of 97,816,471 file I/O events spanning 67 ransomware families, DEFEAT achieves 99.2% detection accuracy and outperforms state-of-the-art methods including UNVEIL, RWGuard, and Peeler by 6.57 to 7.56%. The framework operates at the granularity of a single file encryption: because each ACFG represents exactly one FEG (one user asset context), a cluster label can be assigned as soon as the first file operation completes, enabling detection at the first encrypted file.

---


### 82. [Decision-Focused Learning for Mean-Variance Portfolio Optimization via KKT-Based Reformulation](https://arxiv.org/abs/2609.21427)

**<font color=#1a73e8>作者：</font>** Kensei Nosaka, Shunnosuke Ikeda, Yuichi Takano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mean-variance portfolio optimization (MVO) is a central framework in data-driven asset management. A widely adopted approach is a two-stage framework that first predicts expected returns and then solves the optimization problem based on these predictions, with the predictive models trained by minimizing prediction errors. However, this objective of prediction is not aligned with the quality of the downstream portfolio decision. Decision-focused learning (DFL), which directly minimizes the downstream decision loss within the learning process, has thus emerged as a promising direction. However, existing DFL approaches to MVO rely on surrogate losses or constraint relaxations for tractability, creating a structural mismatch between predictive model training and the constrained MVO solved at evaluation. We propose a single-level optimization formulation that incorporates the Karush-Kuhn-Tucker (KKT) optimality conditions of the lower-level MVO into the upper-level learning problem. This formulation explicitly preserves the budget and short-sale constraints while remaining tractable for standard nonlinear optimization solvers. Rolling-window experiments on real-world ETF (Exchange Traded Funds) data across two asset universes with different correlation structures show that our method achieved the best performance on multiple investment metrics and also demonstrated performance improvement due to the proposed regularization.

---


### 83. [AESSI: An Around-Ear Silent Speech Interface for Cross-Day Online Reuse without Test-Day Calibration](https://arxiv.org/abs/2609.21436)

**<font color=#1a73e8>作者：</font>** Xiran Xu, Mochu Dong, Yujie Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Silent speech interfaces (SSIs) enable private communication without audible speech and may support people with post-stroke dysarthria. Everyday reuse requires articulation-related representations that generalize across days despite sensor repositioning and physiological changes. We present AESSI, an around-ear SSI using masked-context representation pretraining (MCRP): a student predicts teacher representations from masked time-frequency inputs to encourage robustness to recording variability. We collected 44 electrophysiological recordings from 24 participants for 25 everyday Mandarin sentences. With six participants' complete final recordings held out, AESSI achieved 92.24 percent mean accuracy without test-day calibration. AESSI exceeded the best adapted baseline by 50.57 percentage points. At least 21 days after each participant's last recording, five participants each completed 50 independently randomized online tests without calibration, achieving 98.0 percent overall accuracy. Median preprocessing and inference time in CPU replay was 31.70 ms. These results demonstrate end-to-end system operation and support online reuse without test-day calibration. Demo is included with the paper.

---


### 84. [Think Locally, Refine Globally for Memory-Efficient 3D Reconstruction](https://arxiv.org/abs/2609.21437)

**<font color=#1a73e8>作者：</font>** Jingke Zhou, Chenhang Ma, Zhizhou Zhong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose LoG-VGGT, a memory-efficient framework for long-sequence 3D reconstruction that balances local temporal modeling with global camera consistency. Instead of relying on full global attention, our method introduces cross-window attention at a small subset of transformer blocks, enabling effective information propagation across adjacent temporal windows while keeping memory usage bounded. To mitigate long-term pose drift, we further design a global camera consistency refinement module, where camera tokens interact with compact register tokens via cross-attention to enforce scene-level constraints across the entire sequence. This design enables joint optimization of camera representations and significantly improves long-horizon pose stability without incurring the high cost of sequence-wide attention. Extensive experiments demonstrate that LoG-VGGT achieves improved depth accuracy and robust camera pose estimation across multiple long-sequence benchmarks, while delivering competitive streaming reconstruction performance.

---


### 85. [People escalate against a competitor labelled human and hold back against one labelled an optimising machine](https://arxiv.org/abs/2609.21439)

**<font color=#1a73e8>作者：</font>** Vinicius Ferraz, Leon Houf  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People increasingly compete against AI agents rather than other human opponents. We distinguish two channels: an opponent effect and an information effect. These are different elements with different consequences: the opponent effect is specific to a given computational system, the information effect a property of the information environment that an organisation or policymaker can control. We separate them in a preregistered experiment (N = 1,395) using a dynamic all-pay auction, a repeated contest in which escalation of commitment arises from the incentives. What participants are told about the opponent (human, an AI trained to imitate people, or an AI trained to compete well) is varied and crossed with who they actually face, in a deception-free design. What people are told influences escalation: the median price rises by 6.7 points when a human might be the opponent and falls by 8.8 when an optimising machine might be, a spread of about 15% of the prize value of the competition, produced by information alone. Competing against the AI agents lowers prices, yet reduces the chance that both sides finish with positive earnings, showing distinct effects of the opponent channel. The information effect is not explained by articulated strategy, or individual differences, and is consistent with a competitive response engaged when a human is a live possibility. This shows that describing an AI competitor is not behaviourally neutral.

---


### 86. [Optimal Randomized Proper Online Learning](https://arxiv.org/abs/2609.21445)

**<font color=#1a73e8>作者：</font>** Zachary Chase, Idan Mehalel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove that the optimal expected mistake bound of online learning a function class $\mathcal{H}$ by a randomized proper learning algorithm is $O(\mathtt{L}(\mathcal{H}) \log T)$, where $\mathtt{L}(\mathcal{H})$ is the Littlestone dimension of $\mathcal{H}$ and $T$ is the time horizon. Our result improves upon the previously best known bound of $O(\mathtt{L}(\mathcal{H}) \log^6 T)$ given by Daskalakis and Golowich (STOC 2022), and is optimal up to a universal constant for worst-case classes.

---


### 87. [ME-Dex 1.0: Bringing Heterogeneous Tactile Sensing into World Action Modeling](https://arxiv.org/abs/2609.21449)

**<font color=#1a73e8>作者：</font>** Xuancheng Zhang, Xuetao Liu, Qianying Tang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models bring the predictive capabilities of video models into robot action generation, providing a rich foundation for modeling future visual states. Tactile sensing complements this foundation with direct measurements of physical interaction. Some existing methods use tactile features as conditioning inputs without jointly predicting future tactile states, visual observations, and actions. Our key insight is that tactile signals, like video, provide observations of the evolving world state and should be modeled as future observations alongside video. We present ME-Dex-1.0 (MachEmbodied-Dex-1.0), a unified World Action Tactile Model for joint visual, tactile, and action learning. ME-Dex-1.0 adopts a Mixture-of-Transformers architecture comprising a Video Expert, a Tactile Expert, and an Action Expert, all trained with flow matching. We use shared attention connects the experts in intermediate layers, allowing action generation to draw on learned representations of visual and tactile dynamics during joint denoising. To support multi-source heterogeneous tactile inputs, a Canonical Hand Model and a Unified Tactile Autoencoder map tactile observations from different embodiments and sensing layouts into shared spatial and latent spaces. To address the limited availability of paired visual, tactile, and action data, we develop the Agentic Tactile Data Engine, an agent-based data production platform. It supplements RoboTwin and DexJoCo with tactile data recorded directly from force sensors during trajectory replay in simulation. Experiments on the RoboTwin, DexJoCo, and ManiFeel simulation platforms, together with real robot evaluations, demonstrate improved manipulation performance using both grippers and dexterous hands equipped with tactile sensing.

---


### 88. [CompAdapt: Adaptable Composite Motion Modeling for Physics-Consistent Text-to-Video Generation](https://arxiv.org/abs/2609.21455)

**<font color=#1a73e8>作者：</font>** Haoran Qin, Renlong Wu, Tianyu Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While diffusion-based text-to-video (T2V) models have demonstrated impressive capability in generating realistic and temporally coherent videos, they often fail to respect fundamental physical dynamics. Although recent physics-constrained methods incorporate explicit dynamics priors to improve physical plausibility, they remain limited to simple single-type motions, depend on manually specified parameters, and struggle to generalize to unseen physical laws. In this work, we propose CompAdapt, a physics-consistent T2V framework for adaptable generation across complex real-world scenarios. It extends neural dynamics modeling beyond single-type motions to encompass composite physical behaviors, including coupled motions, multi-stage transitions, and multi-object collisions. Furthermore, CompAdapt translates natural language prompts into structured physical semantics, enabling end-to-end specification of motion types, temporal relations, and initial physical parameters. To generalize to novel physical environments, CompAdapt introduces dynamics-aware prior matching, achieving one-shot adaptation without retraining the core dynamics module. In addition, a physics-aware latent feature fusion module improves visual fidelity under fast and complex motion. Experiments on physics-focused T2V benchmarks demonstrate that CompAdapt improves physical consistency over both general T2V models and physics-constrained baselines, while preserving high visual quality and adaptability to unseen dynamics. The project page is available at this https URL .

---


### 89. [Efficient Architecture Search under Leave-One-Subject-Out Evaluation](https://arxiv.org/abs/2609.21457)

**<font color=#1a73e8>作者：</font>** Heinke Hihn, Friedhelm Schwenker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural architectures are widely used for signal processing in automated pain assessment systems. However, architecture design has remained largely a manual task despite the potential efficiency benefits of Neural Architecture Search (NAS). Embedding NAS in a Leave-One-Subject-Out (LOSO) evaluation is computationally demanding because a fully nested implementation requires $N$ independent architecture searches and, assuming approximately linear training cost, scales as $\mathcal{O}(N^2)$. We propose a block-based, leakage-controlled approach that shares NAS runs between subjects, reducing the number of searches from $N$ to $B$, where $B \ll N$, dubbed PainNAS. On the BioVid Heat Pain dataset, PainNAS yields comparable subject-level accuracy with substantially fewer parameters and FLOPs.

---


### 90. [PSEE: Progressive Sensor Event Expansion for Point-Supervised Temporal Action Localization](https://arxiv.org/abs/2609.21462)

**<font color=#1a73e8>作者：</font>** Jiaxi Yin, Ge Wang, Han Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal action localization (TAL) in wearable sensor streams identifies action classes and temporal boundaries, enabling finer-grained activity understanding than conventional action recognition. However, training typically requires costly start--end annotations for every action instance. To reduce this burden, we study point-supervised TAL, where each instance is labeled with only one timestamp and its class. We propose Progressive Sensor Event Expansion (PSEE), which combines semantic activations, sensor-specific transition evidence, and adaptive temporal ownership to recover point-supervised pseudo segments. These segments supervise standard TAL detectors without modifying their inference procedures. Cross-subject experiments on four inertial-sensing benchmarks demonstrate improved pseudo-boundary quality over adapted point-supervised baselines, compatibility with different TAL detectors, and robustness to point sampling. Code is available at this https URL.

---


### 91. [SkillIR: Evolving Scene-Aware Skills for Agentic Image Restoration](https://arxiv.org/abs/2609.21468)

**<font color=#1a73e8>作者：</font>** Jie Shao, Shengkai Hu, Xu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies agentic image restoration, in which multimodal agents coordinate specialized restoration tools to recover images affected by complex degradations. Existing restoration agents often derive complete tool-use plans from the original degraded image or retrieve previously successful trajectories, providing limited support for adapting individual actions to evolving intermediate restoration states. We find that accepted tool executions can change the residual degradation state and, consequently, the applicability of subsequent tools. To address this issue, we propose SkillIR, a skill-guided framework that represents restoration experience as degradation-centered action evidence rather than complete tool-use trajectories. SkillIR consolidates context-dependent action outcomes into scene-aware restoration skills that characterize applicable conditions, expected effects, and attributable failure cases. Instead of prescribing a complete restoration plan, the retrieved skills guide one bounded action at a time within a verified residual-state loop: each tool output is treated as a candidate, committed only after transition verification, and followed by reassessment of the active residual degradations. After each rollout, the resulting evidence is used to create, refine, or patch dynamic skills, enabling accumulated restoration experience to improve decision-making for subsequent inputs. Experiments on synthetic and real-world multi-degradation datasets demonstrate that SkillIR improves restoration quality and enables more reliable and effective tool use.

---


### 92. [Risk-Aware Occupancy for Safety-Oriented End-to-End Autonomous Driving](https://arxiv.org/abs/2609.21470)

**<font color=#1a73e8>作者：</font>** Jiaxing Chen, Hengduo Zou, Yiren Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse representation formulates the environment perception for the end-to-end driving system as a set of discrete elements like objects and lane lines. This formulation meets safety risks in crowded, occluded scenes dealing with unstructured obstacles, uncertain regions, and intricate interactions. In this paper, we propose a dense representation, risk-aware occupancy, to characterize planning-relevant risks in an explicit and uniform manner. It jointly encodes global scene occupancy, map-derived traffic constraints, and future dynamic agent occupancy into a unified BEV map. The unified BEV map captures the risk evidence for trajectory planning in both spatial and temporal dimensions. We design an E2E network, ROIDrive, to realize risk-aware occupancy. It predicts risk-aware occupancy with an independent branch and injects it into planning queries for safety-oriented trajectory generation. In addition, to quantify the safety problem, we introduce RiskOcc4D-nuScenes built upon nuscenes and occ3d-nuscenes. Our risk-aware occupancy yields relative open-loop collision reductions of 52.9% under the UniAD metric and 35.0% under the ST-P3 metric on nuScenes.

---


### 93. [MT-WAM: Reorienting the One-Pass Predictive Representation Toward Action Generation](https://arxiv.org/abs/2609.21474)

**<font color=#1a73e8>作者：</font>** Yiguang Yang, Jiankun Peng, Xiaoming Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fast-WAM shows that video-action co-training improves control without generating future video at inference, making the representation from a single video diffusion Transformer forward central to action generation. However, future-observation prediction does not explicitly prioritize the future dynamics and visual structure needed for control. We present MT-WAM, which retains the original training objectives and adds complementary supervision for future two-dimensional point trajectories and visual features. A lightweight dual-stream branch copied from the video backbone's final blocks provides target-specific processing, while a structured attention mask prevents cross-stream attention. Motion-stream tokens supply additional dynamics conditions to the action expert. Future visual-feature prediction provides supervision in a feature space that captures object and spatial structure. This supervision trains the video backbone to provide more informative visual context for action generation under changing visual conditions, without adding visual-feature-stream tokens to action conditioning. At inference, MT-WAM uses video and motion caches computed once per replan and skips future-video prediction. Without additional embodied policy pretraining, MT-WAM achieves 98.2% success on LIBERO and 73.7% on LIBERO-Plus, exceeding Fast-WAM by 23.8 percentage points on the latter. On RoboTwin 2.0 Clean2Rand, Random success increases from 6.30% to 19.40%; across four real-world tasks, average success increases from 67.0% to 77.8%.

---


### 94. [OpenSAL360: Open-Source Crowdsourcing Platform for Omnidirectional Video Saliency Collection](https://arxiv.org/abs/2609.21480)

**<font color=#1a73e8>作者：</font>** Alexey Bryncev, Andrey Moskalenko, Kira Shilovskaya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnidirectional video saliency prediction plays an important role in many immersive multimedia applications, including viewport-adaptive streaming and compression, foveated rendering, mesh simplification, perceptual quality assessment. Yet progress in this area remains constrained by the cost and complexity of collecting eye-tracking data with VR headsets, which makes large-scale dataset creation difficult to extend. We present OpenSAL360, the first open-source platform for scalable, low-cost 360° video saliency collection. Unlike conventional VR-based protocols, it requires only a standard screen, mouse, and internet connection, enabling parallel saliency data collection from common crowdsourcing assessors without specialized hardware. We validate our collection protocol against seven well-established VR eye-tracking datasets and conduct ablation studies on key interface, pre-, and post-processing parameters. To demonstrate the effectiveness and scalability of the proposed methodology, we collect and publicly release a saliency dataset covering 500 omnidirectional videos annotated by 2,000+ crowdsourcing assessors, making it, to the best of our knowledge, the largest dataset in this field. We make OpenSAL360 publicly available at this https URL.

---


### 95. [Driving on Registers, Reasoning on Risk: Risk-Aware Occupancy for Register-Based End-to-End Autonomous Driving](https://arxiv.org/abs/2609.21486)

**<font color=#1a73e8>作者：</font>** Jiaxing Chen, Hengduo Zou, YuKai Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal trajectory prediction improves behavioral coverage in end-to-end autonomous driving, but existing methods remain limited by sparse scene representations. Incomplete evidence leads to low-quality candidate generation and unreliable ranking among geometrically similar trajectories. On a register-based baseline, bad and poor candidates constitute 19.74% of the candidate set, while the oracle-best candidate ranks only 33.9th on average. We propose RRDrive, which introduces risk-aware occupancy as a dense, temporally aligned, and trajectory-queryable representation. Its global structure guides high-quality multimodal generation, while candidate-conditioned risk queries support fine-grained selection. We further construct RiskOcc4D-NAVSIM with automatic risk annotations. RRDrive achieves a selected-trajectory PDMS of 0.951, representing a 1.5% relative improvement over the baseline (0.937), and improves the average candidate PDMS by 7.7%. In challenging scenes, it improves candidate PDMS by 30.2% and increases the Spearman correlation among good candidates by 0.41, from 0.26 to 0.67. To move beyond this oracle setting, we further develop an external RiskOcc predictor, a perception module that estimates risk-aware occupancy directly from sensor inputs. The competitive performance validates the representation's feasibility.

---


### 96. [Benchmarking Gender Bias in Machine Translation Evaluation Metrics across Occupations](https://arxiv.org/abs/2609.21490)

**<font color=#1a73e8>作者：</font>** Orfeas Menis Mastromichalakis, Giorgos Filandrianos, Wafaa Mohammed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gender bias remains a persistent concern in machine translation (MT), affecting both generated translations and their automatic evaluation. When a source text leaves a person's gender unspecified, translations may realize that person using masculine or feminine forms, and both MT systems and evaluation metrics may exhibit systematic preferences between these alternatives despite the source providing no basis for such a distinction. We study this behavior in the WMT 2026 Automated Translation Quality Evaluation Systems Shared Task using an occupation-balanced subset of GAMBIT+. We consider seven English-source language pairs, six from the original dataset, targeting Arabic, Czech, Greek, Icelandic, Russian, and Ukrainian, and extend the original resource with German. The subset contains 1,308 masculine/feminine translation pairs per target language, with three examples for each of the 436 ISCO-08 occupational groups. We evaluate shared-task submissions and baselines for score prediction and error annotation, examining the direction, magnitude, and frequency of gender-related differences. We find an overall tendency for masculine translations to receive higher scores, as well as differences per occupation following stereotypical gender representations, although the strength and consistency of this preference vary considerably across evaluators and languages. Our results show that gender bias remains present in MT evaluation, but that capturing its extent requires looking beyond a single aggregate measure to complementary dimensions of evaluator behavior.

---


### 97. [VoxelTTO: Voxel-Aligned Feed-Forward 3D Gaussian Splatting with Test-Time Optimization](https://arxiv.org/abs/2609.21498)

**<font color=#1a73e8>作者：</font>** Yibin Zhao, Yihan Pan, Yangwen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent feed-forward 3D Gaussian Splatting (3DGS) methods typically regress pixel-aligned Gaussian primitives, often causing excessive overlap and artifacts, while inaccuracies in predicted camera poses can lead to misalignment in novel-view synthesis (NVS). We present VoxelTTO, a feed-forward framework for reconstructing geometrically accurate 3DGS scenes from an arbitrary number of images and optional camera parameters. VoxelTTO aggregates dense image features into a global voxel representation and decodes Gaussians from voxel features, breaking the pixel-to-Gaussian correspondence. To exploit known camera parameters while keeping the pretrained visual foundation model (VFM) parameters frozen, we introduce test-time optimization (TTO) that adapts lightweight LoRA modules using pose supervision. We further replace vanilla 3DGS rasterization with stochastic solid volume rendering during training and inference, improving geometric fidelity. Training updates only the voxel-aligned Gaussian reconstruction modules, requiring 80 GPU hours. Experiments on Replica, Tanks and Temples, and DTU demonstrate improved RGB-D NVS and camera-pose estimation relative to prior methods.

---


### 98. [2D GauSS-MI: Efficient Active Scene Reconstruction with Balanced Visual and Geometric Quality](https://arxiv.org/abs/2609.21516)

**<font color=#1a73e8>作者：</font>** Yuhan Xie, Jia Pan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active reconstruction requires efficient active view selection to achieve high-quality reconstruction within limited onboard computational resources. Existing methods face challenges in adequately balancing visual and geometric quality with the computational efficiency required for real-time operation. In this work, we present an active reconstruction framework based on 2D Gaussian Splatting (2DGS). We develop an efficient online 2DGS mapping pipeline for incremental RGB-D observations and introduce a probabilistic reliability model that characterizes the view-dependent reconstruction quality of individual 2D Gaussian splats. Building on this model, we formulate 2D Gaussian Splatting Shannon Mutual Information (2D GauSS-MI), a mutual-information-based metric that exploits the explicit surface orientation of 2DGS to evaluate the expected information gain of candidate views. The proposed metric enables active view selection to account for both visual and geometric reconstruction quality. We evaluate the proposed system against three state-of-the-art baselines on eight Replica scenes. Experimental results demonstrate that our method achieves a favorable balance between visual and geometric reconstruction quality with substantially lower computational cost and competitive model storage.

---


### 99. [Learning-to-Optimize as the Missing Architectural Layer of AI-Native Networks](https://arxiv.org/abs/2609.21519)

**<font color=#1a73e8>作者：</font>** Giambattista Amati, Federica Mangiatordi, Pierpaolo Salvo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) is becoming a fundamental design principle of future AI-native communication networks, enabling autonomous resource management, adaptive control, and zero-touch network operation. While current AI-native architectures increasingly embed intelligence across network functions, they provide little guidance on how optimisation knowledge should be systematically generated, transferred, and exploited by AI models. This paper argues that the Learning-to-Optimize (L2O) represents the missing architectural layer between optimisation and AI-native intelligence. Rather than viewing optimisation merely as an online decision engine, the proposed paradigm redefines optimisation algorithms as offline knowledge generators that produce high-quality supervisory information for neural surrogate models. The resulting models inherit optimisation expertise while enabling low-latency runtime inference suitable for dynamic network environments. A generic four-stage L2O workflow is introduced, comprising optimisation, knowledge generation, surrogate learning, and runtime inference. Unlike existing Learning-to-Optimize approaches, which primarily focus on algorithm acceleration, the proposed framework establishes L2O as an architectural abstraction applicable across heterogeneous communication and computing systems. The proposed paradigm is illustrated by an NR-V2X relay-selection problem, in which optimisation-generated solutions from a Mixed-Integer Linear Programming (MILP) solver are used to train a Graph Neural Network that can reproduce near-optimal decisions in real time. The presented perspective positions Learning-to-Optimize as a key architectural enabler for future AI-native networks.

---


### 100. [Refine Then Fusion: Training-Free 3D Point Cloud Adaptation with Priority Refinement and Multi-Modal Knowledge Fusion](https://arxiv.org/abs/2609.21522)

**<font color=#1a73e8>作者：</font>** Hang Cheng, Yan Chen, Mingyu Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent pre-trained foundation models provide rich multi-modal priors for downstream 3D vision tasks. However, the effectiveness of these representations in few-shot scenarios is limited by two fundamental challenges: High-dimensional features often contain substantial channel redundancy and task-irrelevant noise, while the reliability of different modalities varies across samples. Consequently, direct aggregation of heterogeneous representations overlooks sample-dependent modality reliability and may obscure the discriminative cues essential. To address these limitations, we propose Refine Then Fusion(RTF), a training-free framework for few-shot 3D recognition. RTF first identifies discriminative feature channels by jointly modeling inter-class similarity and intra-class stability, thereby decoupling domain-specific knowledge refinement from the cached representations of pre-trained models. It then introduces a reliability-aware fusion mechanism that estimates sample-wise modality reliability from the distribution shifts induced by feature refinement, enabling adaptive aggregation of multi-modal representations. Furthermore, RTF constructs a memory cache that integrates instance-level support features with class-level prototypes to infer query labels. Extensive experiments on five benchmarks demonstrate that RTF consistently outperforms single-modal baselines, partial-fusion variants, and existing lightweight adaptation methods, achieving state-of-the-art few-shot 3D recognition performance without gradient optimization, additional training data, auxiliary training, or parameter updates.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-179](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
