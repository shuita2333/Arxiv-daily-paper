# 📦 其他研究 | 2026年08月13日

> 本类共 **189** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-189](./part-04.md)

---

### 51. [Accelerated Learning of High Dimensional Functions with a Tensor-Featured Training Network](https://arxiv.org/abs/2608.10351)

**<font color=#1a73e8>作者：</font>** Karl Pierce, Yuehaw Khoo, Haizhao Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work we present a method to accelerate the optimization of learning high dimensional functions using deep neural network (DNN). This optimization procedure introduces contextual features into the first layer of a DNN. The parameters of DNN are optimized via standard gradient descent while keeping the input-feature basis fixed. After optimization of the DNN parameters, the feature layer is provided a chance to update and change before DNN optimization resumes. The feature layer has two types of functions: those that can be evaluated quickly in a matrix-free way on the domain (i.e. rank-1 features) and more complex features that must first be decomposed using tensor network (TN) decomposition strategies (tensor features). In particular, we study the effect of adding features which distill pretrained DNN into TNs using a discretize and decompose strategy. To efficiently decompose high-dimensional functions constructed from discretized DNN, we leverage a randomized tensor decomposition strategy. Using randomization, we are able to reduce the storage cost of decomposing high dimensional functions by at least 8 orders of magnitude. Using this approach, we are able to efficiently train models between 5 and 40 dimensions.

---


### 52. [MazzikaAI: A knowledge-based performance-to-prompt compiler for real-time Arabic maqam accompaniment with a streaming text-to-music model](https://arxiv.org/abs/2608.10360)

**<font color=#1a73e8>作者：</font>** Jiaxin Du, Boulbaba Abdeljaouad, Yong Zhuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Arabic maqam music microtonal, modal, and built on ornamented call and response is among the traditions most underserved by generative music models, whose training frameworks remain predominantly Western and equaltempered. Real time accompaniment sharpens this gap: an AI partner must listen, adapt dynamically, and respect idiomatic microtonal structures. Streaming text to music models provide strong generative capabilities but lack precise control interfaces. We present MazzikaAI, a knowledge based system that uses natural language as the actuator of a realtime control loop. By compiling live MIDI, gesture, and inferred harmony into continuously updated text prompts, MazzikaAI steers an unmodified streaming generator, Google Lyria RealTime, without requiring model finetuning. The system embeds expert knowledge of six core maqamat, characteristic ornaments, and ensemble dynamics, maintaining realtime responsiveness with subsecond keytoaudibleupdate latency. Empirical evaluations demonstrate that dynamic prompt compilation reliably grounds generation in microtonal scales, significantly increasing offgrid quartertone content over baseline generation. Beyond its core implementation, MazzikaAI illustrates how deterministic knowledgebased rules can effectively bridge expert, nonWestern musical traditions and unfinetuned foundation models. This architecture establishes a scalable paradigm for realtime humanAI cocreation, offering a generalizable blueprint for interactive accompaniment, adaptive music education, and culturally inclusive generative audio across diverse global idioms.

---


### 53. [Visual-to-Haptic Augmentation in XR: A Wearable Glove for Perceptual Grounding in Multimodal Interaction](https://arxiv.org/abs/2608.10368)

**<font color=#1a73e8>作者：</font>** Faisal Mohd, Hamdi Elsaddik, Erhan Baturay Onural 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extended Reality (XR) systems increasingly deliver high-fidelity visual and auditory experiences, yet tactile perception remains comparatively underutilized as a modality for enriching embodied interaction. This work presents a visual-to-haptic wearable glove and a feature-based visual-to-haptic mapping algorithm that translates spatial and temporal visual features from images and videos into distributed vibrotactile patterns. The proposed method extracts motion, edge, and brightness cues and fuses them into actuator-level intensity maps aligned with a 29-actuator glove arranged in a five-by-seven layout.
The system is implemented through a modular four-layer architecture comprising the XR environment, media content handling, visual-to-haptic processing, and embedded haptic hardware. A within-subject user study (N = 20) compared visual-only interaction with visual-plus-haptic augmentation across texture-based and dynamic video scenarios. Results indicate that tactile augmentation significantly improves perceived realism in dynamic video scenarios and enhances immersion and visual-tactile correspondence across conditions, with stronger and more consistent effects observed for dynamic visual events.
While the current implementation operates in a single-user, offline-synchronized configuration, the findings demonstrate that vision-driven tactile augmentation can function as a perceptual enhancement layer within multimodal XR systems. Such a layer may provide a foundation for future socially enriched XR environments where coherent multisensory grounding supports higher-level interaction and communication.

---


### 54. [Invertible Logits Transformation for Accuracy-Preserving Post-Hoc Uncertainty Calibration](https://arxiv.org/abs/2608.10372)

**<font color=#1a73e8>作者：</font>** Lening Zhao, Qipeng Zhan, Li Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc calibration aligns a classifier's predicted confidences with its empirical accuracy without retraining. An ideal calibrator should correct nonlinear miscalibration, scale gracefully to large label spaces, and preserve the original predictions; existing methods typically violate at least one of these properties---temperature scaling lacks expressivity, more flexible parametric alternatives introduce parameters that grow with the number of classes $C$, and other expressive methods do not preserve the rank ordering of class scores and may alter the predicted class. We propose \textbf{Invertible Logits Transformation (InvLT)}, which applies a learned scalar MLP $f:\mathbb{R}\to\mathbb{R}$ element-wise to the pre-softmax logits. Sharing $f$ across all logit dimensions makes the parameter count independent of $C$. Monotonicity of $f$---and hence preservation of the argmax prediction---is softly encouraged via a paired inverse network rather than enforced through the numerical integration required by prior monotone calibrators; this avoids their computational overhead while empirically preserving the original classification accuracy in every setting we evaluate. Across standard image classification benchmarks and a range of architectures, InvLT consistently outperforms a broad set of post-hoc baselines on standard calibration metrics.

---


### 55. [Fisher8: Stabilizing Neural Heteroscedastic Regression via Output-Layer Fisher Geometry](https://arxiv.org/abs/2608.10374)

**<font color=#1a73e8>作者：</font>** Sumedh Vemuganti, Nickvash Kani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training neural networks to jointly predict mean and uncertainty estimates from noisy observations can be unstable, prompting a series of independent stabilization efforts. We argue that these interventions highlight a common underlying issue where gradient steps are poorly aligned with the geometry of the loss landscape. To better align updates with local curvature, we derive Fisher8, an output-layer gradient correction that reorients and rescales updates using Fisher geometry rather than Euclidean geometry. Unlike past stabilizers, Fisher8 introduces no data-dependent hyperparameters beyond learning rate and admits an approximate KL trust radius between successive predictive distributions. We show that prior stabilizers converge on overlapping components of this geometric correction. Across multidimensional regression and representation-learning tasks, Fisher8 obtains superior likelihood--error tradeoffs, predicts calibrated uncertainty estimates, and learns rich uncertainty-aware feature spaces.

---


### 56. [Generator-Guided Inverse Sampling for Lévy-Driven Generative Models](https://arxiv.org/abs/2608.10384)

**<font color=#1a73e8>作者：</font>** Tianfu Qi, Jun Wang, Jun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies inverse sampling for Lévy-driven generative models from the perspective of Markov generators. Unlike conventional diffusion models, Lévy-driven dynamics involve infinite jump activities, which makes their reverse process nonlocal and difficult to characterize using score information alone. We address this challenge by analyzing the forward and reversed generators. It is derived that the reversed jump component generally becomes a state-dependent Markov jump process governed by a nonlocal density ratio. This observation motivates a structured reverse sampler that decomposes the dynamics into diffusion, small jump, and large jump components. Based on this characterization, we develop a computationally tractable sampler for a class of isotropic linear Lévy SDEs with symmetric $\alpha$-stable jump components. For the jump component, the neural network is used only to amortize the rate of large jump activities, while jump amplitudes are generated from analytically derived conditional distributions, which improves interpretability and controllability. Efficient implementation techniques are further introduced under this setting to avoid expensive high-dimensional integration and sampling. The sampler is further adapted to approximate observation-guided sampling and applied to OFDM-SISO channel estimation under mixed Gaussian and impulsive noise. Simulations show robust estimation performance with a favorable tradeoff between complexity and performance.

---


### 57. [Dreamer-SAC: Off-Policy Learning in Latent World Models for Sample-Efficient Autonomous Driving](https://arxiv.org/abs/2608.10386)

**<font color=#1a73e8>作者：</font>** Jiazhuo Li, Linjiang Cao, Qi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sample-efficient reinforcement learning for autonomous driving is often limited by the trade-off between data efficiency and model bias. While world models reduce the reliance on costly environment interactions, policy optimization over learned dynamics remains sensitive to prediction errors. This paper proposes the Dreamer-SAC framework, which integrates a recurrent state-space world model with an off-policy soft actor-critic algorithm trained directly in latent space. The framework uses a combination of real interactions and short-horizon generated trajectories with n-step target estimation and multi-objective supervision. Evaluated in autonomous driving scenarios with objectives encompassing driving efficiency and safety, the proposed framework consistently outperforms representative reinforcement learning baselines, including DreamerV3, SAC, and PPO, while achieving improved performance with substantially fewer real environment interactions. Experiments reveal an inverted-U relationship between rollout horizon and policy performance, where short-horizon latent rollouts achieve the best trade-off between additional training signals and accumulated model bias. Furthermore, n-step target estimation demonstrates more effectiveness over one-step temporal-difference targets in exploiting predicted experience for value learning.

---


### 58. [FormStruct-Bench:A Hierarchical and Diagnostic Benchmark for Table-Form Document Structure Recognition](https://arxiv.org/abs/2608.10396)

**<font color=#1a73e8>作者：</font>** Lujie Ban, Jiangtao Zhu, Yuanheng Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transforming table-form documents into machine-processable records requires recovering not only their visible content but also the multilevel structure that organizes it. However, existing benchmarks evaluate either holistic document outputs or conventional table grids, and their aggregate scores provide little insight into where structural failures occur. We introduce FormStruct-Bench, a hierarchical and diagnostic benchmark that evaluates table-form document structure recognition at both the document level and progressively finer component levels, allowing aggregate performance to be traced back to specific structural failure modes. To construct auditable ground truth at scale, we annotate 70 reusable templates and expand them into 7,000 verified instances through a provenance-preserving Director--Artist--Verifier pipeline; all 1,100 instances in the template-disjoint test set additionally receive human review. Our evaluation protocol uses five primary metrics and three structure-specific diagnostics across page, schema, and component levels, together with slices over difficulty, structural constraints, and visual degradation. Across 14 API-hosted and locally deployable systems plus two SFT variants, the best document-level score reaches 83.85%, whereas the best reported fine-grained structural score remains below 18%. These results reveal a pronounced gap between reading document content and recovering the hierarchy and regional organization required for reliable table-form understanding.

---


### 59. [ELVAE: Evidential Learning-Based Variational Autoencoder for Uncertainty-Aware Generation](https://arxiv.org/abs/2608.10398)

**<font color=#1a73e8>作者：</font>** Ge Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variational autoencoders generate samples from probabilistic latent representations but do not distinguish uncertainty about the latent location from variability around it. We formulate ELVAE, an evidential learning-based VAE in which each latent coordinate is governed by an input-dependent normal-inverse-gamma posterior. This hierarchy yields an explicit latent-location uncertainty that can be used during generation, not merely reported after inference: low-uncertainty anchors support more reliable synthetic samples, while high-uncertainty anchors can be deliberately exploited for stress testing. The objective is an exact evidence lower bound, and we show that direct regularization of the full hierarchy is required, since the marginalized latent law alone cannot identify the uncertainty decomposition. In an MNIST generation pilot with a frozen external classifier, this uncertainty clearly stratified the semantic reliability of generated digits. A zero-displacement control revealed that most of the effect reflects how reliably an anchor can be re-generated, while a smaller but distinct component is attributable to uncertainty-scaled perturbation itself. The effect holds only under within-class uncertainty ranking, and its magnitude varies across seeds. These findings support the learned latent-location uncertainty as a practical control variable for uncertainty-aware generation, separating anchor reliability from perturbation-induced failure.

---


### 60. [Do Judges Behave Like Algorithms?](https://arxiv.org/abs/2608.10400)

**<font color=#1a73e8>作者：</font>** Riya Manchanda, Eric Chen, Chloe Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What if judges already behave like algorithms? As artificial intelligence and algorithms are deployed in many settings, including the judicial system, many have debated whether judges should be allowed to rely on them. Instead, we ask whether judges follow predictable, algorithmic-like rules already. If judges already follow consistent, formula-like rules based on discrete and static factors such as criminal history, age, and charge type, then judicial behavior may be improved. However, if judges rely on individualized information that cannot be identified through court data, then standards-based decision-making may be more challenging to understand or improve. This work explores these questions by studying judicial decision-making in misdemeanor bail hearings in Harris County, Texas. Using available court data, we investigate whether magistrate judges follow what resembles an algorithm; whether they consider the same variables in their decision-making; and whether they are consistent with themselves and with each other. To do this, we train machine learning models for each judge, measure variable importance metrics to determine important variables for each judge's decision-making, and analyze outcomes of similar cases for judges. Our results reveal that these judges generally behave algorithmically: their decisions can be captured by small, interpretable formulas. However, in some cases, judges differ substantially, leading to surprising inconsistency and unequal treatment across similar defendants. Identifying cases where algorithms do not explain judicial decision-making can improve the justice system by focusing attention on decisions where individualized standards, rather than rules, better explains outcomes.

---


### 61. [Automatic Field-of-View Adjustment for a View-Expansive Microscope via LSTM-Based Gaze and Pipette Motion Interpretation](https://arxiv.org/abs/2608.10401)

**<font color=#1a73e8>作者：</font>** Kenta Yokoe, Takuya Hara, Tadayoshi Aoyama  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Intracytoplasmic sperm injection (ICSI) operators frequently adjust the field-of-view (FOV) during procedures, which interrupts workflow and increases procedure time. Conventional microscopes require manual objective lens switching and illumination adjustments to achieve different FOV sizes. We propose an AI-based automatic FOV adjustment method integrated with a view-expansive microscope. This microscope enables the simultaneous acquisition of a large FOV and high-resolution images using a single objective lens through multiview imaging with galvanometer mirrors and high-speed vision, thereby eliminating the need for physical lens exchanges. Our method utilizes a long short-term memory (LSTM) model to predict the appropriate FOV size based on real-time analysis of the pipette's position and velocity, combined with the operator's gaze position. The AI model is trained using ICSI procedure data from an expert with over five years of micromanipulation experience. Experimental evaluation with novice operators reveals that the proposed automatic FOV adjustment system significantly improves the ICSI procedure speed, reducing the average task completion time from 60.5 to 48.0 s (p < 0.001). The experiments also demonstrate that this improvement enables novice operators to achieve ICSI working speeds equivalent to those of expert operators.

---


### 62. [Threat-guided Policy-aware Scene Perturbation for Safe Autonomous Driving with Online Reinforcement Learning](https://arxiv.org/abs/2608.10403)

**<font color=#1a73e8>作者：</font>** Xincong Hu, Lei Ou, Maosen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has shown promising performance in autonomous driving, yet ensuring the safety of online RL policies remains challenging due to insufficient exposure to safety-critical driving scenes. The long-tailed nature of real-world traffic situations makes dangerous and rare interactions difficult to encounter through conventional sampling, limiting the ability of RL policies to learn robust safety behaviors. Existing methods improve training diversity by synthesizing challenging scenes or adversarial situations. However, these approaches typically optimize scene generation objectives separately from the evolving policy, without explicitly modeling how generated perturbations relate to the current policy's weaknesses and learning needs. In this paper, we propose Threat-guided Policy-aware Scene Perturbation (TPSP) for safe autonomous driving with online RL. TPSP introduces a policy-aware scene encoder to capture the interaction between policy behaviors and surrounding environments, enabling scene perturbation aligned with the current policy. Based on this representation, TPSP selectively perturbs critical objects rather than applying uniform modifications across the scene. Furthermore, we develop a threat-guided optimization strategy that evaluates perturbed scenes through threat-level differences between policy rollouts on original and perturbed scenes, guiding the generation of safety-critical scenes with higher training value. Comprehensive experiments demonstrate that TPSP improves safety learning efficiency, achieving strong safety performance on NAVSIM v2 with approximately 4 million kilometers of simulated driving data. Ablation studies verify that policy-aware targeted perturbations provide more informative safety-critical experiences than random or policy-unaware strategies, enabling safer driving under limited interaction budgets.

---


### 63. [Elbow Angle Guidance System Based on Surface Haptic Sensations Elicited by Lightweight Wearable Fabric Actuator](https://arxiv.org/abs/2608.10404)

**<font color=#1a73e8>作者：</font>** Kenta Yokoe, Tadayoshi Aoyama, Yuki Funabora 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The demand for wearable haptic devices has rapidly increased for various applications. However, many haptic devices interfere with the wearer's activities and movements. In addition, several haptic devices fail to elicit intuitive haptic sensations by adjusting to the natural posture of the wearer. To address these issues, we propose an elbow angle guidance system using a lightweight wearable fabric actuator. The proposed actuator is made of fabric and has two McKibben-type artificial muscles attached to it, rendering it extremely lightweight and facilitating the delivery of surface haptic sensations to intuitively induce elbow extension and flexion. The surface haptic sensation elicited by the fabric actuator is adjusted to natural body movements without interfering with the wearer's movements. Moreover, the proposed system measures and guides the elbow angle by changing the intensity of the surface haptic sensation delivered to users in real time. The accuracy of the proposed system is demonstrated through experiments involving human participants.

---


### 64. [A second-order theory of texture for depth from focus](https://arxiv.org/abs/2608.10411)

**<font color=#1a73e8>作者：</font>** Sreekar Ranganathan, Ioannis Gkioulekas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a theory of textured appearance of optically rough surfaces based on wave optics, emphasizing the role of texture for passive depth from focus. Our theory shows that even surfaces that traditional computer vision would consider textureless can produce textured appearance, due to subjective speckle from surface microgeometry. We analyze the properties of this second-order texture, and show that we can enhance its contrast under natural ambient lighting by simply using a narrowband spectral filter. Doing so results in dramatic improvements in passive depth reconstruction of seemingly textureless scenes, as we demonstrate through extensive theory, simulations, and real-world experiments.

---


### 65. [Reasoning Shortcuts and Value Symmetries: What Symmetry Permits, Architecture Realizes, and Optimization Selects](https://arxiv.org/abs/2608.10420)

**<font color=#1a73e8>作者：</font>** Xin Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning shortcuts are solutions of a neurosymbolic system's rules that produce correct predictions through unintended concepts. A recent framework of Takemura, Inoue, and Nishino analyzes them through an automorphism group of value relabelings and asks, as its central open question, when rules pin concepts down. We first show that the framework's key definition, one shared permutation applied at every position, does not apply as stated to any of the four heterogeneous benchmarks it was evaluated on, and that the most direct embedding, padding domains to a common size, produces confident false pathology: 90.91% of solution pairs reported unexplained on CLE4EVR, where every well-defined member of the hierarchy we introduce reports 0%, and the padded verdict's content rotates with configuration-file ordering. Re-measuring eleven rule families under fifteen pre-specified predictions (thirteen confirmed), unexplained-pair rates span 0% to 99.9999% and track provable structure: six theorems give sufficient conditions for transitivity and its failure, including a Free Slot Lemma certifying Kandinsky's pathology from syntax alone. For circuit-given rules, deciding symmetry-inertness of a coordinate is coNP-complete; nontrivial-automorphism existence is coNP-hard under randomized reductions, lies in $\Sigma_2^p$, is not $\Sigma_2^p$-complete unless PH collapses, and on monotone circuits is coNP-complete outright. In the Boolean case transitivity is classified exactly: automorphisms explain everything iff the solution set is an affine coset. Weakly supervised models place all 94 observed shortcuts at the one level the componentwise theory flags and none at the 48 it certifies transitive; twelve typed-ambiguous levels produce none, separating what symmetry permits from what optimization selects, and a dual-head control replicates the geography. All numbers trace to released artifacts.

---


### 66. [GeoSeg-OV: Bridging Geospatial Gaps with Structural Guidance for Open-Vocabulary Remote Sensing Segmentation](https://arxiv.org/abs/2608.10426)

**<font color=#1a73e8>作者：</font>** Ruizhong Liu, Tingzhang Luo, Zaiyan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary remote sensing segmentation has recently emerged as a promising paradigm that enables pixel-level recognition of arbitrary categories specified by natural language, including classes unseen during training. However, geospatial domain shifts caused by heterogeneous regions, spatial resolutions, and acquisition platforms weaken visual-text matching and limit cross-dataset generalization. Recent attempts have begun to incorporate auxiliary vision foundation models (VFMs), typically coupling their features with text embeddings as additional matching evidence. However, this strategy may introduce inconsistent matching signals while leaving the structure-sensitive representations of VFMs insufficiently exploited. We therefore propose GeoSeg-OV, which decouples auxiliary VFM features from visual-text matching and repurposes them as structural guidance for cost aggregation and decoding. GeoSeg-OV constructs an orientation-robust cost volume from multi-rotation CLIP features, while a frozen VFM extracts multi-scale structure-sensitive features in parallel. We propose Structure-Guided Aggregation (SGA), which integrates cost tokens and CLIP semantic guidance with VFM-derived pairwise structural biases for coherent spatial propagation, followed by text-conditioned class-wise reasoning. We further introduce Cost-Aware Decoding (CAD) to adaptively refine and fuse multi-scale semantic and structural guidance based on the current decoder context. On the global High-Resolution Land Cover (HRLC) benchmark spanning seven datasets across six continents, GeoSeg-OV outperforms the state-of-the-art by +2.5 and +2.7 average mIoU under two training settings. A large-scale zero-shot case study further demonstrates its generalization across geographic domains and category systems without target-domain annotations or retraining.

---


### 67. [Lesion-Aware Adaptive Fourier Neural Operator for CT-to-PSMA PET Synthesis in Prostate Cancer](https://arxiv.org/abs/2608.10429)

**<font color=#1a73e8>作者：</font>** Rashmi Bhaskara, Waleed M. Almutairi, Matthew Gopaulchan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models that synthesize PET from CT or MRI can reduce patient dose and scanner demand, but are typically optimized with global losses such as L1 or mean squared error (MSE) that treat all voxels similarly. In whole-body PSMA-PET, tumor voxels occupy only a small fraction of the volume, yet carry the clinically relevant activity signal; as a result, models can achieve high structural similarity index measure (SSIM) and peak signal-to-noise ratio (PSNR) while still underestimating lesion activity or failing to preserve tumor-specific structure. Radiomics provides biologically meaningful descriptors of tumor intensity and texture, but direct radiomics conditioning is time-consuming because it requires feature extraction from delineated lesion regions. We propose LAFNO, a Lesion-Aware Adaptive Fourier Neural Operator for CT-to-PSMA-PET synthesis that replaces high-dimensional radiomics conditioning with two efficient CT-derived proxy channels. Motivated by radiomics analysis of PSMA-avid tumor core and peritumoral regions, LAFNO uses a contrast proxy for local density variation and a disorder proxy for local texture heterogeneity, both injected into the model bottleneck. LAFNO combines whole-volume reconstruction with lesion-level total lesion activity (TLA), tumor-core contrast, and peritumoral supervision. We evaluated LAFNO against four baseline architectures on the TCIA PSMA-PET-CT-Lesions dataset. LAFNO remained competitive on whole-volume image quality, achieving SSIM of 0.960 and 0.938 for 18F- and 68Ga-PSMA, respectively, while reducing per-patient TLA error to 48.3% and 64.0% for 18F- and 68Ga-PSMA, respectively, and achieving the highest tumor-core radiomics reproducibility across all feature classes for both tracers. Peritumoral reproducibility remained tracer-dependent, indicating that biological fidelity in synthetic PSMA-PET remains challenging.

---


### 68. [What We Know about Responsible AI Practices in Industry: A Half Decade of Empirical Research](https://arxiv.org/abs/2608.10431)

**<font color=#1a73e8>作者：</font>** Wesley Hanwen Deng, Agathe Balayn, Andrew Selbst 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Responsible AI (RAI) has become a central concern for technology companies, regulators, and the public. How industry practitioners interpret, implement, and sustain RAI work directly shapes the design and deployment of AI systems. As empirical scholarship examining RAI practices in industry has rapidly expanded, findings are dispersed across studies that focus on different roles, organizational contexts, and interventions. This work synthesizes current knowledge through a literature review of 161 empirical studies spanning six years, each engaging industry practitioners via interviews, surveys, workshops, ethnographies, and other methods. Our synthesis reveals both meaningful progress and persistent challenges in industry RAI practice. Practitioner awareness has increased, RAI activities have become more professionalized, and interventions such as toolkits and guidelines are more widely adopted. At the same time, practitioners continue to face substantial barriers, including limited training, uneven organizational support, and a lack of interventions tailored to day-to-day work practices. By consolidating and organizing these findings, we provide a more complete account of industry RAI than any single study to date. We conclude by discussing implications for RAI researchers, practitioners seeking to adopt effective practices, and policymakers aiming to ground governance efforts in the realities of industry contexts.

---


### 69. [Do Time-Series Forecasters Use the Right History: Recoverability, Recovery, and Functional Use of Temporal Delays](https://arxiv.org/abs/2608.10433)

**<font color=#1a73e8>作者：</font>** Qipeng Qian, Yuntao Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecast accuracy does not tell us which past inputs produced a prediction. We separate three questions for time-series models with known delay structure: can the true delay be recovered from the observed data, does the model report it, and does the forecast actually use the same history? We first derive input-conditioned recoverability measures that separate intrinsic ambiguity from model error. We then prove that a delay report can become arbitrarily reliable while forecast risk approaches the oracle even though the predictor still uses the wrong lag. This failure also appears in finite samples on the point-delay task: among forecasts with a correct delay report and normalized excess risk within 10\% of the oracle, the reported history is functionally unused under our matched masking test in 55.4\% of N-HiTS cases and 92.7\% of TCN cases. Finally, we show that routing the prediction through the reported history removes off-report bypass paths; a hard one-hot control achieves exact fixed-report alignment. The main conclusion is simple: a good forecast, even with a correct delay report, does not show that the model used the right history.

---


### 70. [DynaPPI: A Large-scale Dynamic Protein Dataset for AI-driven Advances in Protein Interactomics](https://arxiv.org/abs/2608.10435)

**<font color=#1a73e8>作者：</font>** Jiabao Wei, Zilong Geng, Yuze Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have been widely explored in protein backbone generation due to their powerful generation this http URL, in today's AI-driven biological research, predicting the structure of unknown multi-chain protein aggregates (called "complexes" in biology) remains an unsolved this http URL is because existing static or dynamic protein datasets focus solely on static snapshots or single-entity trajectories, neglecting the dynamic process of multiple monomers forming this http URL alleviate this dilemma, we present DynaPPI, a dynamic protein dataset comprising molecular dynamics (MD) trajectories of protein complex formation from dissociated chains to the bound state, as a pivotal resource to bridge the gap between static structural biology and the inherently temporal nature of dynamic molecular this http URL from this dataset, diffusion models can explicitly learn the dynamic binding trajectories of known complexes and accurately predict the structures of unknown complexes based on their diverse generative properties, thereby further catalyzing AI-driven structural biology and protein interactomics.

---


### 71. [Stream Forcing: Constructing Unified Training Trajectory for Robust Streaming Video Generation](https://arxiv.org/abs/2608.10439)

**<font color=#1a73e8>作者：</font>** Yueting Zhu, Yuehao Song, Kaicheng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video generation holds strong potential for world modeling, where future frames must be inferred online sequentially to form a continuous video stream. However, streaming video diffusion models introduce a fundamental train-inference mismatch: inference follows a specialized denoising order, whereas advanced training strategies typically require diverse noise-level configurations. To address this trade-off between train-inference consistency and training coverage, we reformulate the video diffusion sampling as a frame-indexed stochastic process over noise levels. Within this stochastic process space, we construct a continuous training trajectory along which the sampling schedule progressively evolves from independent sampling to inference-consistent sampling. We further introduce a joint calibration algorithm and a temporal correlative sampling algorithm to ensure trajectory smoothness and cross-frame correlation. Building on these designs, we propose Stream Forcing, a unified training framework for streaming video generation that balances training sufficiency and inference efficiency. Extensive experiments demonstrate that Stream Forcing significantly improves generation quality with a 36.6% FVD improvement on the UCF-101 benchmark. Furthermore, our method facilitates robust zero-shot extrapolation to long-horizon video generation with a 27.9% FVD improvement on the UCF-101 benchmark.

---


### 72. [FUSE: Frame-Unified Stress Estimation from Facial Video](https://arxiv.org/abs/2608.10442)

**<font color=#1a73e8>作者：</font>** Stefanos Gkikas, Thomas Kassiotis, Yang Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic stress detection from facial video offers a practical path to non-intrusive affect monitoring, yet existing video-based approaches commonly decompose full recordings into short temporal windows before classification. This design introduces additional choices regarding window length, overlap, and aggregation, while limiting direct analysis of temporal information across the entire recording. In this study, we present FUSE (Frame-Unified Stress Estimation), a facial-video stress detection framework that processes complete recordings as a single input without temporal windowing or external segmentation. The name reflects the defining operation of the method: rather than dividing a recording into short clips, all frames are fused into one unified two-dimensional representation from which the stress state is estimated. This unification is realized by folding the temporal dimension into the channel dimension of the spatial representation, and the resulting high-dimensional input is processed using a unified asymmetric-attention architecture. At a temporal stride of t = 1, FUSE retains the full 120-second recording as one input, corresponding to 3,600 frames at 30 fps. Experiments on a 58-subject stress dataset using a stratified subject-level protocol evaluate seven temporal-stride configurations, ranging from full-frame input to sparse subsampling. FUSE achieves the highest test accuracy of 69.44% at t = 15, while the full-frame configuration remains competitive at 69.03%. Across the stride range, computational cost varies from 12.48 to 348.78 GFLOPs, showing the trade-off between temporal density and efficiency. These results demonstrate that temporal windowing is not required for effective facial-video stress detection in this setting, and that complete-recording inference can be achieved within a single unified architecture.

---


### 73. [Quantum Incremental Learning with Mixed State Prototypes](https://arxiv.org/abs/2608.10464)

**<font color=#1a73e8>作者：</font>** Yu Wu, Qianli Zhou, Xinyang Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Incremental learning models are required to learn new classes sequentially without catastrophic forgetting, while operating under parameter and memory constraints. In the Noisy Intermediate-Scale Quantum (NISQ) era, although quantum neural networks offer advantages in feature mapping, hardware limitations restrict circuit width. Furthermore, traditional quantum classifiers are constrained by the number of orthogonal basis states, limiting their capacity to accommodate a continually growing number of categories. Thus, we introduce a novel quantum incremental learning framework based on trainable mixed-state prototypes. Its original design incorporates new classes by adding class prototypes rather than increasing the circuit width of the shared quantum backbone. The use of mixed-state prototypes is another key contribution, since they have representation capabilities to represent information than a single pure-state prototype. And the decomposable mixed-state calculation provides lower production costs and a convenient Hilbert-Schmidt (HS) distance metric for classification. Simulation results show that our model achieves high-dimensional feature concentration using a minimal number of qubits, while demonstrating lower computational complexity and robust representation in incremental learning tasks compared with classical baselines.

---


### 74. [A Joint-Distribution Route to Fair Representations with Continuous Sensitive Attributes](https://arxiv.org/abs/2608.10470)

**<font color=#1a73e8>作者：</font>** Yijin Ni, Xiaoming Huo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fair representation learning with a continuous sensitive attribute $S$ requires a representation $Z$ that is statistically independent of $S$. Existing criteria, including generalized demographic parity, the expectation of integral probability metrics (EIPM), and mutual information, enforce this independence by averaging a per-value discrepancy between the conditional law $P_{Z \mid S=s}$ and the marginal $P_Z$ over the law of $S$. This approach requires a nonparametric surrogate for the conditional law at each sensitive value. We propose evaluating independence through a single joint discrepancy $d\left(P_{Z, S}, P_Z \otimes P_S\right)$ between the joint law and the product of its marginals. We establish a disintegration identity; on decomposable witness classes it equals the conditional-integral functional that EIPM and generalized demographic parity instantiate. By reaching the same target without the conditional law, this discrepancy can be estimated directly from samples via a dependence statistic rather than conditional smoothing. We take the Hilbert-Schmidt independence criterion (HSIC) as an instance of the joint discrepancy $d$ to investigate the statistical efficiency of replacing the conditional formulation. The HSIC estimator is a closed-form $O\left(n^2\right)$ statistic that converges at the $O\left(n^{-1 / 2}\right)$ rate, in contrast to the nonparametric $O\left(n^{-2 / 5}\right)$ rate of the conditional-route estimators. We prove this instance is equivalent to the conditional maximum mean discrepancy (MMD) integral up to an explicit spectral tail. The corresponding algorithmic implementation, i.e., FRHSIC, attains fairness-accuracy tradeoffs comparable to conditional-route basel es while reducing per-epoch training time.

---


### 75. [Critic-Free Pretraining for Efficient Online Reinforcement Learning Fine-Tuning](https://arxiv.org/abs/2608.10473)

**<font color=#1a73e8>作者：</font>** Daoyi Li, Yixian Zhang, Chao Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline-to-online (O2O) reinforcement learning aims to leverage policies pretrained on static datasets while improving them through online interaction. However, directly reusing an offline-trained critic can hinder online fine-tuning: as the policy and data distribution change rapidly, value estimates inherited from offline training may become misaligned with the online environment, leading to inaccurate policy improvement and inefficient exploration. To address this problem, we introduce \textbf{C}ritic-\textbf{F}ree \textbf{P}retraining: an efficient paradigm that completely abandons the approach of offline critic training, allowing a freshly initialized critic to adapt without inheriting biased estimates. CFP is compatible with various mainstream O2O algorithms and consistently matches or improves upon conventional O2O algorithms across a diverse set of tasks, with particularly pronounced gains on several challenging tasks.

---


### 76. [Stay or Stray - A Dynamical Systems Viewpoint of Popularity Bias](https://arxiv.org/abs/2608.10474)

**<font color=#1a73e8>作者：</font>** Sarvesh Shashidhar, Lankireddy Prabhat, Arpit Agarwal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Popularity bias in recommendation systems arises when a majority user class generates disproportionate interaction data, causing the system to increasingly favour it while degrading recommendation quality for niche users. While extensive empirical evidence of popularity bias exists, the dynamics leading to its emergence are not well understood. In this work, we study the coupled evolution of recommender model updates and user engagement through the lens of dynamical systems. We formulate a stochastic process and analyse its asymptotic behaviour through an ordinary differential equation (ODE) framework grounded in two-time-scale stochastic approximation. We characterise the equilibrium points of this dynamical system, and derive conditions under which popularity bias is provably emergent, as well as conditions under which symmetric retention of all user classes is possible. We conduct experiments on synthetic data and real-world production logs derived from a large-scale commercial music recommendation platform to validate our theoretical results.

---


### 77. [Bridging Event Streams and DiT: Event-Guided Video Frame Interpolation](https://arxiv.org/abs/2608.10479)

**<font color=#1a73e8>作者：</font>** Guixu Lin, Yuyang Yu, Xiang Ji 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models have recently advanced video frame interpolation by synthesizing intermediate frames between input images. However, handling large temporal gaps and complex motion remains challenging, often resulting in motion blur, structural distortions, and temporal inconsistencies. Event cameras provide high-temporal-resolution motion cues that are well suited for bridging these gaps and improving interpolation quality. To exploit this advantage without training an event-assisted model from scratch, we propose an adapter-based framework that incorporates event-derived cues into a pre-trained image-to-video diffusion model with minimal architectural changes. Specifically, our method leverages Image Warped Events (IWEs) and bidirectional sparse optical flow to provide spatially and temporally aligned guidance during generation. By injecting these event-guided structural and motion cues into the diffusion process, our approach reduces interpolation artifacts and improves both reconstruction fidelity and temporal coherence. Experimental results on real and synthetic benchmarks show that our method consistently outperforms existing state-of-the-art approaches. The project page is at this https URL.

---


### 78. [Exploration-Driven Personalized Federated Reinforcement Learning via Intrinsic Motivation](https://arxiv.org/abs/2608.10499)

**<font color=#1a73e8>作者：</font>** Md Rafid Islam, Rafsan Jany, Zahid Hasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized Federated Reinforcement Learning (PFRL) takes a decentralized approach to storing and accessing information based on past experiences while keeping each client's data private during the learning of each client's policy. Many current methods for PFRL rely heavily on exploiting existing reinforcement learning reward signals to derive an optimal policy for each client, thereby neglecting exploration in non-stationary or sparse-reward environments. In this work, we introduce a new exploration-driven framework, Exploration-Driven Personalized Federated Reinforcement Learning via Intrinsic Motivation (EDPFRL-IM), that leverages an inherent curiosity-driven exploration at each client to promote local exploration and protect client privacy. Furthermore, to facilitate policy discovery via exploration in previously unexplored state spaces, clients add an intrinsic random network distillation (RND) signal to their extrinsic reward. Additionally, the server does not have access to clients' raw experiences or local gradient estimates; instead, the server sends global exploration priors and collects minimal novelty summaries from each client to enable both diverse and coordinated exploration among clients. Experiments in benchmark environments show that our framework outperforms average PFRL benchmarks in policy personalization and sample efficiency, primarily in delayed and sparse reward systems. Overall, EDPFRL-IM enables the integration of a flexible exploratory learning structure into federated reinforcement learning systems while preserving client privacy.

---


### 79. [DSAR: Dual-Stream Autoregressive Modeling of Temporal Cloth Dynamics for Photorealistic Animatable Avatars](https://arxiv.org/abs/2608.10500)

**<font color=#1a73e8>作者：</font>** Haozhong Xiong, Yao Yu, Yu Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creating photorealistic and temporally coherent animatable human avatars from RGB videos remains challenging. Current methods struggle to capture realistic cloth dynamics, producing over-smoothed appearance or severe artifacts on out-of-distribution poses. This limitation stems from a fundamental oversight: existing approaches neglect the temporal causality inherent in cloth physics, where current states emerge from previous states through temporal evolution rather than instantaneous skeletal configurations alone. Without explicit modeling of this causal structure, networks learn pose-appearance correlations instead of motion evolution, leading to poor generalization. We introduce a dual-stream autoregressive framework that explicitly models both observable geometric information and implicit internal state. The geometric stream propagates surface displacement from the previous frame, while the state stream fuses current features with historical states retrieved from a memory bank. Motion-adaptive aggregation handles spatially-varying dynamics, and adaptive regularization balances smoothness with flexibility. Experiments on challenging datasets demonstrate significant improvements in rendering quality, temporal consistency, and generalization to motion patterns beyond training distributions, validating that dual-stream temporal modeling enables realistic cloth dynamics.

---


### 80. [Towards Color-Faithful Low-Light Image Enhancement via Adaptive Color Debiasing and Saturation Rectification](https://arxiv.org/abs/2608.10512)

**<font color=#1a73e8>作者：</font>** Zhichen Yang, Rui Xu, Yuzhen Niu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light imaging often introduces color bias caused by the low signal-to-noise ratio and the image formation process. Although recent low-light image enhancement methods have achieved strong brightness recovery, faithful color restoration remains challenging, manifesting as overall color bias together with local under- and over-saturation. To address this issue, we propose CAGE, a cylindrical color correction framework with adaptive color debiasing and gamut-harmonized saturation rectification for color-faithful low-light image enhancement. We first introduce AdaLAB, a cylindrical adaptive LAB color space that provides a decoupled and image-specific basis for uniform color correction. Building on this color space, we further develop AdaCCT, an adaptive cylindrical color transform with forward and inverse transforms for the conversion between RGB and AdaLAB color space, as well as necessary color debiasing and saturation rectification. The forward transform suppresses embedded color bias before backbone enhancement by reorganizing the chromatic distribution through chromatic-plane shifting and scaling, while the inverse transform achieves faithful saturation rectification through out-of-gamut lightness compensation. Extensive experiments on multiple benchmarks show that CAGE achieves more faithful color restoration, specifically reduces color bias and saturation abnormality, and delivers better overall visual quality across different low-light enhancement backbones. The code is available at this https URL.

---


### 81. [SparSTAR: Sparse Attention for SpaceTime AutoRegressive Video Synthesis](https://arxiv.org/abs/2608.10519)

**<font color=#1a73e8>作者：</font>** Jongbeom Lee, Hyunwoo Yu, Jincheol Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> InfinityStar extends visual autoregressive generation to video through a sequence of image and clip pyramids. Its changing scale and cross-clip context, however, leave late-scale attention costly and make sparse patterns reused from diffusion or image VAR models unreliable. We introduce SparSTAR, a training-free block-sparse attention method tailored to this setting. At each expensive scale and attention head, SparSTAR scores contiguous key blocks from the current query and key activations, retains required conditioning context, and executes the selected blocks through a forward-only sparse path. We analyze cross-scale consistency within a clip, pattern persistence across clip boundaries, and quality degradation as reuse spans increasingly distant scales. Across these analyses, important key blocks shift, showing that recomputing block selection at each target scale is more reliable than reusing a transferred mask. On 720p text-to-video and image-to-video generation, SparSTAR preserves every token and refinement scale while providing about a 1.6x end-to-end speedup and maintaining VBench and paired-output reconstruction fidelity close to dense InfinityStar.

---


### 82. [Synthesizing Probabilistic Saturating Counters with Differentially Private Formal Guarantees](https://arxiv.org/abs/2608.10521)

**<font color=#1a73e8>作者：</font>** Zhiming Chi, Lutan Zhao, Depeng Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Branch predictors improve instruction-level parallelism in modern processors and are commonly modeled using saturating counters. However, classical saturating counters are deterministic and thus vulnerable to side-channel attacks: an attacker can manipulate the counter state and infer the branch direction of a victim process. Probabilistic saturating counters (PSCs) have been proposed to mitigate this leakage by randomizing counter updates, but existing evaluations are mainly empirical. In this paper, we give a formal analysis based on differential privacy (DP): we model PSCs and the corresponding Prime+Probe attack strategies as probabilistic Moore machines, derive optimal attack strategies, and quantify the attacker's distinguishing power through DP. Our DP guarantee applies to the PSC primitive under the Prime+Probe observation model; end-to-end security for a full branch predictor under repeated or adaptive attacks is an important direction for future work. We then synthesize parameters for an enhanced PSC that satisfies a target pure DP guarantee. To evaluate utility, we derive the stationary misprediction rate and validate the theoretical predictions on benchmark programs. Compared to deterministic and existing probabilistic saturating counters, the synthesized PSCs provide formal security guarantees while preserving competitive prediction performance.

---


### 83. [Rethinking Text-Based Image Retrieval in Specific Domain](https://arxiv.org/abs/2608.10524)

**<font color=#1a73e8>作者：</font>** Jingyang Tan, Sheng Yang, Yuanpeng Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driven by the rapid advancement of vision-language representation learning, Text-based Image Retrieval (TBIR) has made notable progress. However, existing benchmarks are predominantly constructed on an exclusive single-match assumption between query and images. While effective in general scenarios, this assumption fails to reflect practical system performance in specific domains (e.g., surveillance), where a single query often corresponds to multiple relevant candidate images. To address this limitation, we design a Domain-Specific Multi-Match Text-based Image Retrieval (DSMM-TBIR) data engine. Leveraging this engine, we construct Security Multi-Match TBIR (SecMM-TBIR), a benchmark comprising 50k surveillance images with 200 comprehensive queries. Furthermore, we observe that vanilla contrastive learning in specific domains suffers from severe false negatives, forcing the model to push apart semantically similar pairs and thus degrading retrieval performance. We propose the Semantic-Aware Fine-Tuning (SAFT) framework to address semantic compression in specific domains, which incorporates Semantic-Aware Soft-Label Supervision (SASS) and Intra-modal Structural Distillation (ISD) to establish a promising paradigm for domain-specific TBIR tasks. Experiments across diverse CLIP-like models demonstrate that SAFT yields an average mAP@20 gain of 7.8 points on SecMM-TBIR over standard image-text contrastive (ITC) fine-tuning, while also improving general-domain performance. The entire benchmark will be released to facilitate further research.

---


### 84. [Coordinating the Unknown Lipschitz Constant in Multiplayer Bandits](https://arxiv.org/abs/2608.10526)

**<font color=#1a73e8>作者：</font>** Ricardo Parada, Chenzhang Zhao, William Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by decentralized applications, we study cooperative multi-agent bandits in continuous (Lipschitz) action spaces when the Lipschitz constant is unknown. We consider three information structures: (A)~unobserved actions with common rewards, (B)~observed actions with independent rewards, and (C)~unobserved actions with independent rewards. In each case we design and analyze an algorithm that estimates the Lipschitz constant, chooses a discretization of the joint action space, and applies a cooperative bandit method to the induced discrete problem. Players never communicate once learning starts, so the central difficulty is that they must reach the \emph{same} discretization from their own data. We prove regret guarantees showing that common rewards and observable actions each supply this agreement for free, and that in their absence agreement can still be bought, through a dithered quantization of the estimate, at no cost in the leading order of the regret.

---


### 85. [Robust Multi-Agent Bandits with Heavy-Tailed Rewards and Information Asymmetry](https://arxiv.org/abs/2608.10529)

**<font color=#1a73e8>作者：</font>** Daphne Feng, Ricardo Parada, Lily Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The multi-armed bandit problem is a central framework in sequential decision-making, extensively studied under sub-Gaussian reward assumptions. However, real-world applications often involve heavy-tailed reward distributions and decentralized, information-asymmetric interactions. We study multi-agent multi-armed bandits with heavy-tailed rewards under three information-asymmetry regimes: unobserved actions with common rewards, observed actions with independent rewards, and unobserved actions with independent rewards. We develop robust decentralized algorithms for each setting and derive regret guarantees that nearly match centralized heavy-tailed rates. Experiments on a Pareto-distributed reward environment validate our theoretical findings and illustrate the trade-offs between synchronization, coordination, and exploration across the three regimes.

---


### 86. [Flow Straight to Reality: Perceptually Consistent Flow Matching for Efficient Image Restoration](https://arxiv.org/abs/2608.10544)

**<font color=#1a73e8>作者：</font>** Sangwoo Jo, Donggeun Ko, Jayeon Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration is fundamentally constrained by the tradeoff between distortion and perception: minimizing pixel-wise error yields over-smoothed results, whereas optimizing for perceptual realism often introduces structural deviations. Recent approaches attempt to balance this tradeoff via posterior sampling or multi-stage generative pipelines, yet remain computationally expensive and architecturally complex. To overcome these limitations, we propose PCFlow (Perceptually Consistent Flow Matching), a unified framework that directly parameterizes a continuous transport from degraded observations to clean targets, jointly optimizing distortion and perceptual quality. While its latent consistency flow objective drives stable and efficient few-step inference, a Latent Consistency Perceptual Loss (LCPL) imposes semantic constraints directly on the guiding velocity field, steering the dynamics toward visually sharp data manifolds. Furthermore, recognizing the inherent conflict between structural and perceptual consistencies, we integrate a conflict-free gradient projection strategy to stabilize the multi-objective optimization landscape. Combined with lightweight, convolution-only backbone, PCFlow achieves competitive performance across diverse restoration tasks at a fraction of traditional computational costs.

---


### 87. [Reinforcement Learning-Based Laser Cutting Machine Parameter Optimization](https://arxiv.org/abs/2608.10549)

**<font color=#1a73e8>作者：</font>** Khanh Quan Pham, Majid Kundroo, Geunwoo Ban 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Achieving high accuracy in laser-based cutting of optical films requires careful tuning of parameters such as focal length and laser power beam, adjusted according to the specific properties of each film type. Trial-and-error based traditional methods are used to find the most suitable cutting parameters for various films, but they are slow and inaccurate. To address this issue, this paper presents the Reinforcement Learning for Laser Cutting (RL$^{2}$C) algorithm, which uses Q-learning with an epsilon-greedy policy to dynamically optimize cutting parameters, significantly reducing taper size and film wastage. Additionally, RL$^{2}$C incorporates a dynamic environment space adaptability mechanism to allow it to adapt to new states encountered during the learning process over multiple batches of experiments. Experimental results demonstrate that RL$^{2}$C requires fewer steps and less time to find optimal cutting parameters compared to various RL-based optimization methods. Specifically, RL$^{2}$C reduces the number of optimization steps by up to 12.5\% and processing time by up to 81.8\% compared to existing methods. This study demonstrates the potential of RL in industrial laser-cutting processes by improving cut quality, reducing time and film wastage, and minimizing manual interventions.

---


### 88. [Retrieval-Corrected Conformal Prediction for Time Series](https://arxiv.org/abs/2608.10553)

**<font color=#1a73e8>作者：</font>** Sangjin Jin, Kangmin Kim, Junhyeong Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction (CP) provides distribution-free prediction intervals for fixed forecasters, but its standard calibration procedure is often inefficient for time series data, where forecast errors are temporally dependent and change across time and operating conditions. Recent time series CP methods improve local calibration using recent, weighted, or localized residuals. Yet local calibration can remain indirect, since broad residual weighting or additional adaptation procedures may dilute the evidence most relevant to the current prediction. This motivates a simple retrieval and correction strategy that selects similar past residuals as local evidence and then corrects the coverage error left by retrieval. In this paper, we propose Retrieval--Corrected Conformal Prediction (RCCP), a retrieval-augmented calibration method for time series prediction intervals. RCCP builds an asymmetric interval from retrieved one-sided residuals and calibrates its normalized retrieval error with a scalar conformal correction. Thus, retrieval provides local residual evidence, while conformal correction determines the final scale needed for coverage. We provide a coverage-gap bound based on the stability of the normalized retrieval error distribution. Across standard benchmarks and backbone forecasters, RCCP attains the target coverage in every setting and achieves the lowest Winkler scores, with fewer severe misses. RCCP also achieves low calibration and inference overhead, showing that retrieval-corrected calibration is an effective and scalable approach to uncertainty quantification in time series forecasting. Code is available at this https URL.

---


### 89. [MARCO: Click-Intent Decomposition for Calibrated Ads Conversion Prediction](https://arxiv.org/abs/2608.10562)

**<font color=#1a73e8>作者：</font>** Shiwen Shen, Xiru Huang, Liang Luo 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Not all clicks are equal. Industrial ads ranking decouples conversion probability into click-through rate (CTR) and post-click conversion rate (CVR), yet treats every click as the same event. In reality, users provide a free, self-generated signal of intent through their physical UI interactions. Different click types on the same ad exhibit a 4-fold difference in actual conversion rates. By conflating these signals, the standard CVR model under-predicts high-intent clicks and over-predicts low-intent ones, which is a bias masked by near-perfect aggregate calibration. We propose MARCO (Multi-intent Ads Ranking Composition Optimization), a framework that resolves this bias by decomposing each click by intent. Using the logged click type as a free behavioral label, MARCO trains per-intent CVR heads on homogeneous populations, and at serving time composes their per-intent CVR estimates under a predicted distribution over intents. Theoretically, we prove that decomposition never raises population risk, give the exact headroom under squared loss and non-negativity under the deployed loss, and show through a routing-efficiency dial how much of it reaches serving. Because the population-optimal score is unchanged, any gain is a finite-capacity estimation and calibration effect that we validated both offline and online. For deployment at scale, we further cast multi-impression, multi-click attribution as credit assignment with a bias-variance tradeoff analogous to RL return estimation, showing last-impression, first-click attribution is the low-bias, low-variance, deterministic choice under production constraints, and derive three consistency conditions enforced end-to-end at scale. Deployed at binary intent granularity, MARCO corrects per-intent calibration to approximately 100%, lifts conversions per click by +2.80%, and drives +0.98% cumulative improvement in topline metrics.

---


### 90. [Agentic Instruction Data Selection: Let DataMaster Interpret Your Intent](https://arxiv.org/abs/2608.10579)

**<font color=#1a73e8>作者：</font>** Fanqi Zhou, Qiaosheng Chen, Zixian Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although existing instruction data selection methods have introduced various metrics, the inherent complexity of real-world datasets makes it impractical for any single metric to generalize across all scenarios. Developers are thus often forced to manually inspect data and craft heuristic rules for each new application---a tedious and error-prone process. In this paper, we propose a paradigm shift from manual configuration to automated orchestration via the Instruction Data Selection Agent (DataMaster), which interprets user intent and autonomously composes optimal selection strategies. By allowing users to specify data needs through natural language descriptions, DataMaster simplifies data curation and removes the burden of manual strategy design. Extensive experiments across the math, medical, and code domains show that DataMaster outperforms static baselines in most settings and surpasses full-pool training in a substantial number of cases. The implementation of DataMaster and the scripts needed to reproduce the reported pipeline are publicly available at this https URL.

---


### 91. [BREAD: Baseline-Referenced Explanations for Anomaly Diagnosis](https://arxiv.org/abs/2608.10587)

**<font color=#1a73e8>作者：</font>** Jiaqi Qiu, Rob Goedhart, Jannis Kurtz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI)-based prospective anomaly detection methods are increasingly deployed in high-dimensional and nonlinear settings. Among these approaches, AI-based statistical process monitoring (SPM) is widely used, providing a structured framework for prospective monitoring. Once an anomaly is detected, a diagnosis method is needed to identify the features driving the flagged observation away from normal behaviour. Traditional SPM diagnosis methods are typically designed for specific detection models and cannot be directly applied to AI-based methods. Model-agnostic explainable AI (XAI) offers a general framework for feature relevance explanation. However, existing methods suffer from scalability limitations or assign relevance to noise features, reducing diagnosis accuracy. We propose a scalable, baseline-referenced diagnosis method that uses both the anomalous observation and normal baseline information. We provide mathematical guarantees that under a mean-shift anomaly setting, the proposed method achieves higher faithfulness in detecting the features causing the anomaly compared to LIME. Simulation studies and a real-world case study validate the effectiveness of the proposed method and show that it generates more faithful and accurate diagnosis results for AI-based prospective anomaly detection methods.

---


### 92. [A HamNoSys-Guided Dataset and Baselines for Fine-Grained Isolated Handshape Recognition in Sign Language](https://arxiv.org/abs/2608.10588)

**<font color=#1a73e8>作者：</font>** Ushnish Sarkar, Suvajit Patra, Bhaswar Chattopadhyay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Fine-grained handshape recognition supports computational sign-language transcription, recognition, and translation, but broad, phonetically defined visual inventories with signer-aware evaluation remain limited. This work introduces a benchmark grounded in the language-independent Hamburg Notation System (HamNoSys). Methods: A balanced dataset of 144,000 RGB images was collected from 15 participants for 160 handshape classes defined by the official HamNoSys 4 Handshapes Chart. ResNet-18 and ViT-B/16 were evaluated as appearance-based models, while a graph convolutional network and XGBoost were evaluated from hand landmarks. Both a class-stratified subject-dependent split and a 15-fold leave-one-subject-out (LOSO) protocol were used. The same model families were additionally assessed on LSWH100 and ASL Fingerspelling Dataset A for external context. Results: The subject-dependent benchmarks established reproducible reference performance across all four model families, whereas LOSO evaluation exposed a substantial reduction when recognition was required to generalise to unseen participants. On ASL Fingerspelling Dataset A, mean LOSO top-1 accuracy ranged from 82.20% to 87.40%. Conclusion: The documented acquisition, curation, and complementary evaluation protocols pro-vide a reproducible resource for fine-grained isolated-handshape research and for developing more accessible sign-language technologies.

---


### 93. [$π$-SUB: A Physics-Informed Synthetic Underwater Benchmark Dataset for Underwater Image Enhancement](https://arxiv.org/abs/2608.10589)

**<font color=#1a73e8>作者：</font>** Namritha Lasyapriya Maddali, Rajini Makam, Suresh Sundaram 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents $\pi$-SUB, a physics-informed framework for generating synthetic underwater benchmark datasets that bridges the synthetic-to-real gap for Underwater Image Enhancement (UIE). The proposed framework extends the classical underwater image formation model by incorporating depth-dependent downwelling irradiance, biologically resolved absorption, and environmental scattering across all ten Jerlov water types, together with independently controllable residual phenomena. Using this framework, the $\pi$-SUB dataset consists of paired synthetic underwater-reference images spanning shallow-to-deep and coastal-to-oceanic environments. Extensive simulation studies have been carried out to evaluate $\pi$-SUB along two criteria namely hyper-realism and generalizability. For hyper-realism, $\pi$-SUB attains a global Frechet Inception Distance (FID) that is 46% lower than Syrea. For generalizability, four state-of-the-art UIE architectures (FUnIE-GAN, Pix2Pix, PUIE-Net, and Phaseformer) are used for comparative evaluation of $\pi$-SUB. These models were independently trained on six datasets including one real and five synthetic datasets and tested on six real-world benchmarks datasets. Across four UIE architectures and six real benchmark datasets, $\pi$-SUB improves UIQM by 4.18% over PHISWID (next best) and 9.46% over Syrea (next best), while reducing NIQE by 48.78% and 23.98%, respectively. These results establish $\pi$-SUB as a hyper-realistic and generalizable benchmark for developing the next generation of underwater image enhancement methods. The code and dataset are available at this https URL

---


### 94. [Rethinking Data Efficiency in Industrial Dense Prediction: Pretraining Coherence, Not Inductive Bias, Determines ViTs Low-Data Advantage](https://arxiv.org/abs/2608.10590)

**<font color=#1a73e8>作者：</font>** Haoran Sui, Yaoyuan Jia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) are widely believed to require more labeled data than CNNs for industrial dense prediction. Through controlled experiments on four industrial datasets, we show that the data-efficiency gap stems from pretraining incoherence, which refers to the statistical mismatch between ImageNet-pretrained ViT backbones and COCO-pretrained CNN necks, rather than from inherent self-attention deficits. We characterize the cross-architecture feature gap and propose a lightweight AlignBlock family for pyramid-level feature recalibration. Our core finding empirically identifies a data-efficiency frontier: for domain-proximal scenes with >= 200 samples, Swin-Graft surpasses YOLOv11x (terminal 703-shot: 0.973 vs 0.956 mAP@50); for domain-distant scenes, CNNs retain advantage (hook 141-shot: 0.900 vs 0.600 mAP@50). Grafted neck weights yield up to 2.5x the mAP of a randomly initialized neck.

---


### 95. [$β$-VAEs as Effective Theories: Tolerance-Dependent Dimension](https://arxiv.org/abs/2608.10599)

**<font color=#1a73e8>作者：</font>** Johannes Hirn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In a $\beta$-VAE, increasing the regularization strength acts as a spectral cutoff by collapsing low-utility latent coordinates.
In the linear Gaussian VAE, the collapse order matches the ranking of reconstruction utilities exactly, because both are set by the PCA spectrum. We ask which parts of this picture survive in fully connected nonlinear VAEs trained on WorldClim.
We find that nonlinear interactions shift and broaden collapse onsets, so thresholds no longer coincide exactly with utilities. However, the common ordering is preserved over the resolved ranks, so the spectral cutoff still acts as a utility cutoff and the effective-description logic carries through.
The resulting effective-dimension curves reveal a head--tail tradeoff: increasing depth concentrates utility into the first few coordinates but worsens tail fidelity.

---


### 96. [Gaussian Sculpting: End-to-End Controllable Surface Reconstruction via Field Optimization](https://arxiv.org/abs/2608.10602)

**<font color=#1a73e8>作者：</font>** Ke Jiaxin, Juncheng Liu, Yi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has recently enabled real-time novel view synthesis with impressive quality. However, it struggles to recover accurate surfaces under limited viewpoints and due to the inherent irregularity of Gaussian primitives. The resulting geometric errors are notoriously difficult to correct manually. To address these issues, we propose Gaussian Sculpting, a fully differentiable end-to-end framework for high-quality surface reconstruction. Our key insight is to anchor Gaussians onto an evolving differentiable surface, allowing them to guide signed distance field (SDF) optimization instead of extracting the surface only during post-processing. To enable stable gradient isolation during joint optimization, we design a bi-level training strategy in which the outer loop optimizes the geometry represented by the SDF, while the inner loop updates the Gaussians with the geometry fixed. We further impose constraints on Gaussian parameters to ensure consistency with the underlying surface, thereby improving both geometric and appearance fidelity during optimization. In addition, we introduce a multi-resolution subdivision scheme based on octree-like partitioning to preserve fine details while reducing memory consumption. Experiments on object-level scenes demonstrate that our method effectively removes redundant surfaces, recovers missing structures caused by limited viewpoints, and achieves strong reconstruction quality even at relatively low resolutions.

---


### 97. [Simplex Relaxation for Discrete Diffusion](https://arxiv.org/abs/2608.10615)

**<font color=#1a73e8>作者：</font>** Jinya Sakurai, Patrick Pynadath, Satoshi Hayakawa 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models for categorical generation are defined by a corruption kernel, which determines the intermediate state space and the associated reverse prediction problem. We study uniform discrete diffusion and ask whether its training objective and reverse transitions can be enriched without changing the underlying categorical corruption process. We introduce Simplax, an exact Dirichlet--categorical augmentation that couples each corrupted categorical state with an auxiliary simplex-valued variable while preserving the original uniform diffusion process as its categorical marginal. This augmentation yields a tractable Rao--Blackwellized reverse-bridge objective and a corresponding stochastic reverse sampler, while retaining the corrupted categorical state as the denoiser input. Empirically, Simplax improves the generative perplexity--entropy tradeoff on unconditional OpenWebText generation. On Sudoku, a model trained exclusively on $30$-clue puzzles achieves the highest accuracy among the compared methods across all evaluated clue densities, including the minimum uniquely solvable $17$-clue regime, and also achieves the highest validity in unconditional generation.

---


### 98. [Pair-Centric Graph Rewiring for Over-Squashing via Optimal Transport-Guided Communication Alignment](https://arxiv.org/abs/2608.10619)

**<font color=#1a73e8>作者：</font>** Yan Wang, Chuan-Xian Ren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Message-passing neural networks (MPNNs) often struggle when task-relevant information is distributed across distant regions of a graph, since local propagation must compress remote signals through limited structural interfaces. Graph rewiring provides a structural response to over-squashing. Most existing methods rely on edge-level bottleneck scores or graph-level connectivity surrogates. With a limited rewiring budget, the key question is which pairwise communications most need structural support. This paper proposes PairAlign, a pair-centric graph rewiring framework that makes this question explicit through demand-support shortage. Specifically, PairAlign combines original-graph structural demand with current-graph finite-hop propagation support; their ratio highlights interactions whose communication demand is poorly supported by topology, and our theory shows that this score provides a computable proxy for the corresponding Jacobian-based shortage with a pair-level interpretation of over-squashing. Our theory reveals a two-sided effect of edge insertion: a new edge can create useful walks and simultaneously dilute existing normalized transition mass. Guided by this observation, PairAlign optimizes shortage to favor edge additions that alleviate over-squashing. Beyond selecting useful additions, PairAlign further introduces an Optimal Transport-guided rewiring mechanism to coordinate the finite edge budget for pair-level structural compatibility and shortage-target coverage. It formulates communication alignment between the candidate edge budget and the shortage targets, and the theory shows that this allocation covers shortage targets more broadly and effectively than a greedy-local assignment. Experiments on standard graph benchmarks show PairAlign's improvement across message-passing backbones, validating pair-level repair as an effective route for alleviating over-squashing.

---


### 99. [Decomposition-Induced Context-Memory Conflict: When Fact-Checking Pipelines Contradict Their Own Source Text](https://arxiv.org/abs/2608.10627)

**<font color=#1a73e8>作者：</font>** Yu-Feng Yen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decompose-then-verify pipelines, including FActScore-style fact-checkers and long-form factuality evaluators, first split a passage into atomic claims before checking each one. Decomposition itself is treated as a neutral preprocessing step. We show it is not: a decomposer can be induced to substitute its own parametric belief for what the source passage says, producing a claim that contradicts the text it was supposed to summarize faithfully. We call this Decomposition-Induced Context-Memory Conflict (DI-CC) and show it is mechanistically the same phenomenon as classical context-memory conflict, occurring inside a different pipeline stage than prior work has examined. A linear probe trained only on classical context-memory conflict data (NQ-Swap), never exposed to any decomposition output, significantly separates decomposition positions that produce DI-CC from faithful decompositions (AUC = 0.86-0.88, permutation p < 0.0005). An existing reference-free baseline, SelfCheckGPT-style self-consistency sampling, fails to detect DI-CC at all (AUC 0.51, chance-level), because DI-CC content is stably recoverable and recurs across resamples, unlike the variability self-consistency methods rely on. Context-aware decoding, a training-free mitigation from the classical setting, transfers to decomposition and suppresses DI-CC, but at a severe cost: many decompositions under coreference-heavy conditions fail to parse, often because the decomposer fabricates a different identity. We do not consider this mitigation deployment-ready. We further characterize the mechanism's boundaries: its natural occurrence rate is too sparss not manifest on naturally-occurring hallucinatedtext, and it requires a minimum model scale to detecablish DI-CC as a real, mechanistically grounded, andpartially treatable failure mode, with a scope we chhan overstate.

---


### 100. [InSight-doc: Agentic Visual Perception for Long-Document Understanding](https://arxiv.org/abs/2608.10628)

**<font color=#1a73e8>作者：</font>** Kaican Li, Weiyan Xie, Lewei Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-document understanding often requires reasoning over many visually rich pages, making inference costly and prone to context rot. In this work, we propose InSight-doc, an agentic visual perception framework that treats visual resolution as an adaptive reasoning-time resource. InSight-doc starts from low resolution and selectively zooms into high-resolution regions for finer evidence, without relying on any external retriever. To train such an agent, we construct an active-perception corpus of 17.9K high-quality SFT examples with region-level zoom-in trajectories, accompanied by 19.2K hard RL examples. Through SFT+RL, InSight-doc-8B improves the baseline by 4.3--16.4 accuracy points over document VQA benchmarks. On long documents, it reduces hallucination by more than 40% and inference latency by 41%--68% while maintaining an accuracy lead. Our code, datasets, and model are released at this https URL .

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-189](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
