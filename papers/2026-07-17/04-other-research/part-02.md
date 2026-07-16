# 📦 其他研究 | 2026年07月17日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

---

### 51. [Accuracy-Preserving Stability Regularization for Large-Scale Retail Demand Forecasting](https://arxiv.org/abs/2607.13331)

**<font color=#1a73e8>作者：</font>** Jize Li, Jiani He, Dishu Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retail demand forecasts are reused across replenishment, capacity, labor, and transportation planning cycles. Point-error objectives do not constrain abrupt movement between adjacent forecasts, while post-hoc smoothing acts only after model fitting. We ask whether a training-time penalty on consecutive within-series movement can improve horizontal forecast-path stability without materially changing point accuracy. The penalty is evaluated in a temporal-structured pipeline combining recent-demand embeddings with calendar, price, hierarchy, item, and store features. On selected M5 demand series at 1000, 3000, and 4000-series scales, the stability-aware hybrid model improves Forecast Stability Score over XGBoost by 6.91%, 6.66%, and 7.68%, respectively, while RMSE changes remain within 0.72% across three random seeds. Post-hoc exponential smoothing attains lower raw movement but incurs a larger RMSE cost; training-time regularization preserves more point accuracy and performs favorably under normalized stability. These findings extend forecast evaluation from point-error minimization toward an accuracy-stability trade-off perspective for operational retail forecasting.

---


### 52. [Marker-free deformable registration and fusion for augmented reality-guided positive margin localization during tumor resection surgery](https://arxiv.org/abs/2607.13343)

**<font color=#1a73e8>作者：</font>** Yue Yang, Annie Benson, Matthieu Chabanas 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Positive margins in head and neck oncologic surgery require mapping specimen-side pathology findings to the patient resection bed. This is challenging because pathologists identify the positive margin on slices of the resected, deformed specimen, while surgeons must relocate the corresponding site on the resection bed using only verbal descriptions and no visual guidance. We present a marker-free augmented reality (AR) workflow for mapping a margin label from a three-dimensional specimen scan to the resection bed. The method combines contour-constrained deformation, residual alignment to a depth scan, surface-based fusion to a head-mounted display, and target projection onto the reconstructed bed. Bead-suture correspondences estimate specimen deformation, whereas patient-to-display fusion does not require external fiducial markers. Following formative experiments, five residents and surgeons performed cadaveric cheek and scalp re-resection tasks under verbal guidance, verbal guidance with specimen examination, and AR guidance. Deformation target errors were $7.63 \pm 3.74$ mm for the cheek and $3.72 \pm 1.02$ mm for the scalp; residual specimen-to-bed distances were $2.43 \pm 2.15$ mm and $2.19 \pm 1.06$ mm, respectively. Fusion error did not differ significantly between marker-free and marker-based methods on either cadaver; overall marker-free fusion error was $2.15 \pm 0.87$ mm. End-to-end margin localization error decreased from $21.40 \pm 3.84$ mm with verbal guidance and $16.09 \pm 4.30$ mm with specimen examination to $6.19 \pm 1.79$ mm with AR guidance ($p < 0.001$). Online fusion required $5.23 \pm 0.34$ s. These results demonstrate effective marker-free AR guidance for positive-margin localization and support more precise tumor resection.

---


### 53. [EZSMT Version 3, Matured](https://arxiv.org/abs/2607.13344)

**<font color=#1a73e8>作者：</font>** Yuliya Lierler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constraint Answer Set Programming (CASP) is a hybrid reasoning paradigm that combines Answer Set Programming (ASP) with Constraint Processing and Satisfiability Modulo Theories (SMT), enabling powerful declarative encodings of complex combinatorial search problems. This paper presents the design and implementation of EZSMTV3, an extensible SMT-based CASP framework that advances the translational approach to CASP solving. Building upon the foundation of the EZSMT+ system, EZSMTV3 introduces a more expressive input language, supports optimization via weak constraints, and offers foundations for streamlined integration of new constraint types. Rather than implementing custom search procedures, EZSMTV3 leverages state-of-the-art SMT solvers, such as CVC5, YICES, and Z3 to perform reasoning. The paper provides benchmarking results comparing EZSMTV3 with its CASP peers such as CLINGCON, CLINGO[DL], and CLINGO[LP], while showcasing its ability to handle mixed-domain constraints involving both integers and reals. The system provides a robust platform for future extensions and theoretical exploration within the CASP domain.

---


### 54. [Audio-Text Cross-Attention with Psycholinguistic Support Features for Ambivalence/Hesitancy Recognition](https://arxiv.org/abs/2607.13345)

**<font color=#1a73e8>作者：</font>** Luiz F. B. F. Martins, Rodrigo W. Pisaia, Matheus M. Girardi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present an audio-text system for the Ambivalence/Hesitancy Video Recognition Challenge of the 11th ABAW Competition. The method excludes visual frames and represents each video as overlapping 5-second windows aligned with transcript timestamps. Each window combines a 320-dimensional prosodic audio descriptor, a 768-dimensional emotion-oriented RoBERTa embedding, and 74 handcrafted features capturing uncertainty, hedging, and attitudinal conflict. Audio and text are fused via temporal cross-attention, while support features are injected prior to gated multiple-instance learning (MIL) pooling to modulate the window's importance. Predictions from five independently initialized models are averaged. On the labeled public development set, the ensemble achieved an average precision of 0.875 and a macro-F1 of 0.72. Our source code is publicly available at this https URL.

---


### 55. [Learning Latency-Aware Orchestration for Multi-Agent Systems](https://arxiv.org/abs/2607.13359)

**<font color=#1a73e8>作者：</font>** Xi Shi, Mengxin Zheng, Qian Lou  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) coordinate multiple LLM-powered agents through structured workflows, gaining reasoning power but incurring high inference latency from multi-step execution and repeated model invocations. Existing orchestration methods primarily optimize task performance and inference cost, leaving latency largely unaddressed. In MAS, end-to-end latency is governed by the critical execution path, so reducing total cost alone does not reliably reduce latency. Moreover, optimizing latency while preserving accuracy remains non-trivial: naive latency optimization can misassign operator-level credit and degrade task accuracy. To address this gap, we propose Latency-Aware Multi-agent System (LAMaS), a latency-aware orchestration framework for learning-based multi-agent systems. LAMaS addresses this challenge at two levels: at training time, it learns latency-aware execution graphs through constrained optimization with critical-path-aware credit assignment; at inference time, since a graph committed at training time cannot exploit runtime evidence, it complements graph construction with a lightweight controller that adaptively eliminates redundant future agent interactions as execution unfolds. Experiments on four benchmarks show that LAMaS achieves the best latency among evaluated learning-based MAS baselines, reducing end-to-end latency by over 50\% while maintaining competitive or better accuracy. LAMaS is also modular and transfers to other MAS with minimal changes, consistently yielding latency reductions.

---


### 56. [Detector Confidence Signals Presence Rather Than Occlusion in Cluttered Manipulation](https://arxiv.org/abs/2607.13361)

**<font color=#1a73e8>作者：</font>** Yuanzhi He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Occlude a named object until about an eighth of it remains visible, and an open-vocabulary detector's confidence that the object is present barely changes; as the clutter around it grows the confidence can even rise. On real video the detector still reports the object present in 99% of occluded frames, on another instance of the same category. This matters because that confidence is widely read as a visibility signal, used to threshold detections, evaluate open-vocabulary detectors, ground language, retrieve instances, and gate active perception. We audit whether it reflects occlusion by pairing every view with a geometry-segmentation oracle that gives detector-free ground-truth visibility. As true visibility falls from every scene to one in eight, the confidence stays nearly constant and uncorrelated with visibility, and the detector reports the target present in about nine of ten scenes, firing on same-category distractors: it signals that the category is present somewhere, not that the specific target is visible. The failure holds across three detectors (Grounding DINO, OWLv2, and Segment Anything Model 3), nine object categories, two simulators with different renderers and object sets, built and natural occlusion, and real video. Two consequences follow: a confidence-based metric understates the value of resolving occlusion by about ten times (8 against 88 points in our active-perception setting), and a confidence-based gate fires exactly when the object is hidden. No single-view signal we tried, including a realizable localization check, flags the occlusion, because the occluders sit where the target is. We connect the effect to detector miscalibration and object hallucination, release the controlled benchmark, and recommend target-grounded signals for gating and evaluation.

---


### 57. [DiffGI: Differentiable Geometry Images for High-Fidelity Thin-Shell 3D Generation](https://arxiv.org/abs/2607.13365)

**<font color=#1a73e8>作者：</font>** Eungjune Shim, Hansol Lee, Eunjung Ju  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D generative models predominantly rely on implicit volumetric representations, which enforce watertight topology and struggle to represent thin-shell and non-manifold geometries such as garments. Geometry image-based approaches offer a surface-centric alternative, but existing methods rely on discrete binary occupancy maps whose resolution-dependent boundary encoding causes staircase artifacts and information loss upon downsampling, while surface reconstruction remains a non-differentiable post-processing step disconnected from the learning pipeline. To address this, we propose Differentiable Geometry Image (DiffGI), an end-to-end 3D-to-2D mapping framework that seamlessly integrates surface representation and geometric optimization. DiffGI replaces binary maps with a continuous 2D Truncated Signed Distance Function (TSDF), which encodes boundary position at subpixel precision within a fixed grid resolution, eliminating resolution-dependent staircase artifacts even under aggressive downsampling. Building on this continuous field, we introduce a differentiable Marching Squares algorithm based on analytical linear interpolation, allowing gradients from 3D surface losses to propagate back to the 2D latent space. Leveraging this differentiable pipeline, we train a DiffGI-VAE augmented with a geometry-aware normal rendering loss to compress complex 3D surfaces into an ultra-compact 32X32 latent space, and instantiate a transformer-based latent diffusion model with a flow-matching objective on top of this space for conditional 3D generation. Extensive experiments on garment and object datasets demonstrate that our method achieves superior reconstruction fidelity and boundary precision compared to prior geometry-image and voxel-based approaches, while requiring significantly fewer computational resources.

---


### 58. [xChk: Bring Your Own Identity -- Heterogeneous Assurance with Verifier-Determined Sufficiency](https://arxiv.org/abs/2607.13369)

**<font color=#1a73e8>作者：</font>** Sean MacGuire  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present xChk, a reference identity provider for Bring Your Own Identity (BYOI): users enroll via heterogeneous proofs (government KYC, corporate SSO, WebAuthn/FIDO2, professional networks, live verification, longitudinal activity, behavioral signals) and disclose them as portfolio claims in standard OAuth 2.0 / OpenID Connect (OIDC) tokens, while each relying party applies its own sufficiency policy - the IdP transports claims and may evaluate an RP-supplied evidence policy for consent, but does not adjudicate access. Enrollment depth varies by modality (some paths are user-initiated; org KYB and officer binding are operator-assisted).
xChk also supports human-in-the-loop attestation for high-risk actions: humans can initiate attestations directly (browser UI / POST /api/attestations), and AI agents acting under those principals can trigger the same gateway via scope-gated authorize/attest - hash-chained human approvals on a shared verification graph (humans via OIDC; agents via API keys). A production deployment at this https URL ships both initiation paths with bilateral RP evaluation at consent; one documented relying party (this https URL, Appendix B) exercises Login with xChk.

---


### 59. [RoughNet: Mapping Arctic Sea Ice Roughness Using Diffusion-Based Super-Resolution of Satellite Imagery](https://arxiv.org/abs/2607.13371)

**<font color=#1a73e8>作者：</font>** Tessa Cannon, Michel Tsamados, Petru Manescu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of landfast sea ice roughness is critical for climate modeling and safe Arctic over-ice travel, yet existing approaches rely on costly airborne surveys or sparse in-situ measurements, limiting spatial coverage and operational scalability. Here we show that high-resolution sea ice topography can be reconstructed directly from optical satellite imagery using a conditional diffusion framework. Our approach, RoughNet, learns to map 10 m Sentinel-2 multispectral images to locally normalized 1 m surface elevation residual fields, enabling fine-scale roughness characterization from widely available satellite data. Trained on airborne LiDAR data from two Arctic regions and evaluated on an unseen third Arctic region, the model generalizes across diverse ice conditions and partially reproduces small-scale topographic structure. The best-performing model achieves an out-of-domain root mean squared error of 9 cm while preserving the statistical and spectral properties of the underlying roughness field. These results demonstrate that generative diffusion models can recover physically meaningful surface structure from optical imagery alone, providing a scalable pathway for high-resolution sea ice mapping and roughness estimation in data-sparse environments.

---


### 60. [A POS Tier Is the Key to Automated Annotation for Low-Resource Language Documentation: Neural Interlinear Glossing for Irabu, a Southern Ryukyuan Language](https://arxiv.org/abs/2607.13372)

**<font color=#1a73e8>作者：</font>** Michinori Shimoji  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discourse data are the primary empirical basis of grammar writing in field linguistics, but producing interlinearized text is notoriously expensive - on the order of one hour of work per minute of recording. For endangered languages, where the time remaining to verify analyses with native speakers is itself limited, automating parts of the interlinearization workflow has direct documentary value. We implement a full neural annotation pipeline (morpheme segmentation, POS tagging, glossing) for Irabu Ryukyuan using deliberately small, transparent BiLSTM-CRF models, and evaluate it under a realistic hard constraint: approximately one hour of fully annotated discourse as the entire supervised resource. Two factors of the annotation itself are manipulated: its richness (with or without a POS tier) and its quantity (training budgets from 6 to 47 minutes). Gold POS improves grammatical glossing by +4.4 (SD 0.7) points (significant in all 5 seeds), and the gain grows as data shrink (+11.6 points at a quarter of the data); a POS tier more than halves the amount of glossed data needed to reach a given accuracy. In a fully automatic pipeline this gain is not yet realized: the tagger still errs on 12% of morphemes, and an incorrect POS misleads the glossing model more than no POS at all. The value is latent rather than lost: degrading gold POS with controlled noise shows the gain returning as tagger accuracy rises, with break-even near our tagger's current 88% and +1.6 to +3.2 points recovered at 92-96%. We conclude with a concrete recommendation for documentation practice: annotate quadrilinearly - text, POS, gloss, translation.

---


### 61. [Weight Feedback Computes the Jacobian Transpose Locally in Modern Deep Networks](https://arxiv.org/abs/2607.13380)

**<font color=#1a73e8>作者：</font>** Junlong Shen, Xingyu Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive Coding (PC) offers a biologically motivated alternative to backpropagation via local weight updates, yet routing error between layers still relies on an autograd Jacobian-transpose ($J^\top$) product - the last non-local operation in PC. We show that this dependency is largely avoidable. For any layer $f(x)=\mathrm{Act}(\mathrm{Norm}(L(x)))$ with frozen normalization statistics, the exact $J^\top$ factors into three locally available terms, $J^\top v = L^\top(s \odot \sigma'(z) \odot v)$, where $\sigma'$ is the activation derivative, $z$ is the pre-activation, and $s=\gamma/\sigma_{\mathrm{run}}$ is the normalization gain. Prior weight-feedback methods omitted both corrections; restoring them closes the transport gap for this layer class. Locality here holds up to three assumptions, which we state upfront: weight symmetry ($L^\top$ mirrors the forward operator, as assumed by all PC), a soft spectral-norm control that is not synapse-local, and a nearest-neighbour approximation for MaxPool. Substituting the identity into PC yields WF-Act-PC, which removes the autograd backward pass from error transport. On CIFAR-10/100 (50 epochs, 5 seeds), WF-Act-PC is the only PC method whose accuracy improves with depth, surpassing iPC - the strongest classical PC baseline - by 2.7-22.3 pp on CIFAR-10. With both methods tuned per architecture, it matches or exceeds a comparably-tuned backpropagation baseline on the deeper CIFAR-10 architectures (VGG-9: 93.57% vs. 92.43%; ResNet-18: 92.76% vs. 91.54%) and on the harder Tiny-ImageNet benchmark, while trailing tuned BP on the deeper CIFAR-100 VGG cells. Our WF-Act-PC implementation is publicly available at this https URL

---


### 62. [Set-shifting Behavioral Test for Harnessed Agents](https://arxiv.org/abs/2607.13396)

**<font color=#1a73e8>作者：</font>** Ziwei Ye  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What happens to an LLM agent's tool choice when the reliable tool silently changes within an ongoing session? We borrow set-shifting from cognitive psychology to study how well agents adapt to hidden reliability shifts. Our benchmark mounts tool-skill libraries with redundancies, where many tools solve the same task but differ in hidden reliability. In our evaluation framework, a branched schedule shifts the reliable tool group at hidden boundaries and pairs every shift with a no-shift control. We find that agents, by default, settle on a small recurring routine within a few turns of each boundary, with call shares concentrating on a few discrete values after each reliability shift. We score the set-shifting accuracy for each agent trajectory: the joint probability of routing to the target tool group in every post-shift window. We test open-weight LLMs in an open-source agentic harness and find qualitatively distinct failure modes across the same set of routines. We also find that set framing, how the toolset presents the alternatives as competing or complementary, shifts the routing dynamics.

---


### 63. [Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations](https://arxiv.org/abs/2607.13399)

**<font color=#1a73e8>作者：</font>** Rui Wang, Hongru Wang, Yi Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has become a key paradigm in LLM post-training, yet its training dynamics remain poorly understood. We present a systematic study examining the role, pathologies, and regulations of OPD. We first clarify the role of OPD as an exploration catalyst: it steers the student toward correct reasoning paths via dense token-level guidance, without expanding capability ceiling. We confirm this by showing that prompt diversity matters more than per-problem sampling numbers, and critically, that the effectiveness of OPD hinges entirely on the quality of its guiding signal. This dependency exposes two pathologies that derail exploration. The Student-Teacher Mismatch occurs when a large teacher-student distributional gap causes the guiding signal to misalign with task correctness, steering exploration in counterproductive directions. Length Exploitation arises when the aggregated token-level objective creates length-dependent shortcuts, allowing the student to game the reward landscape through response truncation or redundant padding, exploring degenerate length modes rather than reasoning strategies. To tame these pathologies, we investigate lightweight signal regulations: advantage clipping and log-scale compression, ensuring exploration is guided by faithful signals. Experiments across seven benchmarks demonstrate that these regulations alleviate length exploitation and enable effective distillation, stably surpassing OPD variants and RLVR baselines, thereby confirming that well-regulated signal quality, rather than mere teacher scale, governs successful exploration in OPD.

---


### 64. [AnomExpert: Identifying and Selecting Anatomical Planes for Prenatal Ultrasound Anomaly Diagnosis](https://arxiv.org/abs/2607.13409)

**<font color=#1a73e8>作者：</font>** Jian Wang, Yang Yang, Ziheng Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Life-limiting congenital anomalies require accurate prenatal diagnosis for appropriate clinical decision-making. Prenatal ultrasound (US) examinations involve multiple anatomical planes, and diagnosis depends on identifying anatomical planes and selecting diagnostically relevant planes for each anomaly. Existing automated methods either rely on plane-level annotations or aggregate heterogeneous images without explicitly modeling these diagnostic capabilities. We propose AnomExpert, a prototype-driven framework for prenatal US anomaly diagnosis using only case-level supervision. AnomExpert introduces learnable plane prototypes to organize unordered images into latent representations corresponding to anatomical planes without requiring plane annotations. A disease-aware sparse selection mechanism further selects diagnostically relevant planes for each anomaly. Experiments on a multi-center dataset of 3,654 cases show that AnomExpert consistently outperforms nine representative multi-instance learning methods. Using a ViT-small backbone, it achieves 86.9% accuracy and 84.2% F1-score while maintaining parameter efficiency. These findings indicate that modeling anatomical plane identification and disease-specific plane selection improves weakly supervised multi-plane prenatal US anomaly classification. The code is available at this https URL.

---


### 65. [Evaluating Frontier AI Agents as Autonomous Clinical Security Auditors](https://arxiv.org/abs/2607.13411)

**<font color=#1a73e8>作者：</font>** Michael O. Eniolade  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Clinical AI models can expose patients to harm when adversarial vulnerabilities go undetected, yet formal security auditing requires statistical expertise, specialized tools, and significant time. We present an open evaluation task, built on METR Task Standard v0.3.0, that tests whether frontier AI agents can autonomously implement a structured clinical AI security audit. Given a pre-trained clinical prediction model, a patient dataset, and written instructions, each agent must implement four attacks from pseudocode, compute a Security Posture Score covering FGSM robustness, membership inference resistance, expected calibration error, and boundary attack resistance, and write a structured JSON report in a Docker container using only a bash interface and no scaffolding code. Six variants span the Wisconsin Diagnostic Breast Cancer and MIMIC-IV ICU mortality datasets across three model architectures with increasing defense strength, with reference scores from 55.60 to 90.41. We ran 54 evaluations across three frontier models, with three runs per variant. Claude Sonnet 4.6 and GPT-4.1 completed all 18 runs and received perfect evaluator scores. GPT-4o completed 61 percent of runs and used about five times the per-run token count of Claude, although provider tokenization differs. Total API costs were 8 US dollars for GPT-4.1, 12 US dollars for Claude Sonnet 4.6, and 27 US dollars for GPT-4o. GPT-4o failures involved premature session termination, an aggregation error, and an empty submission file. The task, scoring infrastructure, and Wisconsin Breast Cancer assets are publicly released; MIMIC-IV variants require separate PhysioNet access.

---


### 66. [Is the Statistical Advantage Worth the Cost? An Empirical Comparison of KANs and MLPs for Structured Data Classification](https://arxiv.org/abs/2607.13413)

**<font color=#1a73e8>作者：</font>** Matthew Steven P. Toledo, Justine Raphael H. Jacinto, Vivekjeet Singh Chambal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study presents an empirical benchmarking comparison between Kolmogorov-Arnold Networks (KANs) and Multi-Layer Perceptrons (MLPs) on structured tabular classification tasks. Motivated by the growing interest in KANs as an alternative function-approximating architecture, we evaluate their out-of-the-box performance on twelve publicly available datasets spanning binary, multiclass, multilabel, and ordinal problems. Both models were trained under standardized preprocessing, architecture, and fixed hyperparameter settings, with performance assessed using test accuracy and F1-Score, paired hypothesis testing, and effect size analysis. Results show that KANs statistically outperform MLPs in binary and multiclass domains and achieve a significant aggregate advantage across all datasets. However, the observed medium effect size (d = -0.46) raises an important cost-benefit consideration: while KANs offer superior generalization through adaptive spline-based mappings, this advantage comes with substantially higher parameter and computational complexity relative to the MLP baseline. These findings suggest KANs are the preferred choice for high-precision applications, while MLPs remain a robust and efficient option for resource-constrained environments. Future work should extend this analysis to additional data modalities to further refine these architectural selection criteria.

---


### 67. [MultiAnimate: A Unified Framework for Controllable Multi-Character Animation](https://arxiv.org/abs/2607.13415)

**<font color=#1a73e8>作者：</font>** Zhongyi Zhang, Guangyuan Wang, Li Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative models and technological innovations have significantly addressed the fundamental challenges of character image animation. However, existing approaches predominantly focus on character animation from a single reference image, substantially limiting their applicability in scenarios such as multiple character interaction animation. To fill this gap, this paper introduces MultiAnimate, a comprehensive framework that enables concurrent animation of multiple characters within a shared environment while preserving both identity consistency and spatial relationships. The framework achieves these objectives through multiple well-designed mechanisms. First, we incorporate an identity-specific reference net that enables appearance extraction from multiple reference images, distinguishing MultiAnimate from existing approaches constrained to single reference inputs. Second, we implement an identity-aware pose encoder to address the character-pose binding challenge, wherein an attention mechanism enables the network to accurately differentiate and process multiple pose sequences during generation. Third, we introduce an interaction guider module that enhances the framework's capability to handle complex inter-character interactions by leveraging character-specific mask information, serving as an optional component that refines the pose sequences. Extensive experiments and ablation analyses demonstrate our framework's superiority in multiple character animation, particularly in scenarios involving complex motion sequences.

---


### 68. [OrDA: Orthogonal Disentanglement of Access Habits Framework for Homepage Marketing Block Recommendations](https://arxiv.org/abs/2607.13420)

**<font color=#1a73e8>作者：</font>** Lingxiao Zhang, Xiaobo Li, Tao Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clicks on homepage marketing blocks are driven by a dual-mechanism of content interest and access habits. However, habitual clicks often create Pseudo-Positives in marketing slots, where position advantage masks mediocre content quality, leading to biased recommendation ecosystems. We propose a framework called Orthogonal Disentanglement of Access habits (OrDA) to purify interest signals. OrDA utilizes a dual-tower structure with a gated allocation layer to adaptively route features and minimize interference. To ensure rigorous separation, we employ orthogonal regularization to constrain the latent interest and habit manifolds to be geometrically perpendicular. OrDA performs causal intervention (do-calculus) during inference to rank items solely by purified interest scores. Empirical online evaluations on large-scale datasets demonstrate that OrDA effectively eliminates access-habit bias, outperforming state-of-the-art methods in predictive accuracy. Online AB test 5.64% shows user click-through rates (UCTR) improvement on the Zhima homepage marketing block, Zhima rent-floor recommendation.

---


### 69. [ScanFocus: A Coarse-to-Fine Framework for Spatio-Temporal Video Grounding](https://arxiv.org/abs/2607.13421)

**<font color=#1a73e8>作者：</font>** Kai Chen, Ming Dai, Wenxuan Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-Temporal Video Grounding (STVG) aims to retrieve the visual trajectory of a specific object from a video stream as described by a natural language expression. However, most advanced methods struggle to balance global context modeling with precise boundary localization. Due to the prohibitive computational costs of processing long videos, these approaches typically resort to low-rate temporal downsampling and implicit motion modeling. This inevitably suppresses high-frequency boundary cues and neglects the explicit inter-frame dependencies required for precise boundary delineation. To address these limitations, we present \textbf{ScanFocus}, a novel coarse-to-fine framework that decouples the STVG task into a global spatio-temporal scan and a local boundary focus. Specifically, we utilize a unified vision-language fusion encoder combined with a lightweight Deformable Semantic-Motion Fusion module to efficiently align multimodal features and generate coarse proposals. To recover the suppressed fine-grained details, we introduce the Semantic-Guided Temporal Aggregator (SGTA) in the refinement stage. By densely sampling around coarse boundaries, SGTA explicitly models short-term temporal interactions under semantic guidance, capturing rapid motion changes for precise timestamp regression. Extensive experiments on three widely used benchmarks demonstrate the performance superiority of our proposed method over previous approaches. Code will be released at this https URL.

---


### 70. [Temperature Scaling Is Not Enough: Calibration Gaps Under Human Label Distributions](https://arxiv.org/abs/2607.13423)

**<font color=#1a73e8>作者：</font>** Wisdom Dogah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temperature scaling is the dominant post-hoc calibration method in modern deep learning. Its theoretical justification rests on an assumption that is rarely stated explicitly: that ground-truth labels are one-hot and deterministic. In practice, labels are frequently soft, crowd-sourced, or genuinely distributional, reflecting real disagreement among human annotators rather than annotation noise. We study whether temperature scaling retains its calibration properties when this assumption is violated, and whether any resulting degradation depends on model scale. Using CIFAR-10H and ChaosNLI, two publicly available datasets with human-annotated soft label distributions, we evaluate three model scales per modality under both hard one-hot and soft distributional label targets. Across all nine configurations we find a positive soft-label calibration gap: temperature scaling calibrated on hard labels consistently underperforms an oracle calibrated directly on soft labels, with Brier Score gaps ranging from 0.002 to 0.134. The gap grows monotonically with model scale in the vision domain and on the SNLI-derived split of ChaosNLI, and is substantially larger in the language domain (mean gap 0.079) than in vision (mean gap 0.003). A scale-ordering reversal on the MNLI-derived split remains after matched-domain training; we treat it as inconclusive for the scale hypothesis and attribute it primarily to near-chance accuracy on that split. As a second post-hoc baseline, multiclass isotonic regression yields the same qualitative conclusion: positive soft-label gaps in all nine configurations, and larger gaps in language than in vision. These findings suggest that calibration protocols built on majority-vote labels systematically misstate model reliability wherever label ambiguity is structural, with direct consequences for deployment in safety-critical settings.

---


### 71. [PUe: Biased Positive-Unlabeled Learning Enhancement by Causal Inference](https://arxiv.org/abs/2607.13428)

**<font color=#1a73e8>作者：</font>** Xutao Wang, Hanting Chen, Tianyu Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Positive-Unlabeled (PU) learning aims to achieve high-accuracy binary classification with limited labeled positive examples and numerous unlabeled ones. Existing cost-sensitive-based methods often rely on strong assumptions that examples with an observed positive label were selected entirely at random. In fact, the uneven distribution of labels is prevalent in real-world PU problems, indicating that most actual positive and unlabeled data are subject to selection bias. Building on the SAR-PU propensity-weighted framework of Bekker et al., we study a PU learning enhancement (PUe) framework using normalized propensity scores and normalized inverse probability weighting (NIPW). PUe's main contributions are a normalized inverse-probability-weighted PU risk formulation; additional theoretical analyses of normalized sample-weight error and common PU estimators under biased labeling; regularized deep propensity-score estimation; integration with modern cost-sensitive PU methods; and support for selectively labeled negative classes. Experiments on MNIST, CIFAR-10, and ADNI demonstrate improvements over several PU baselines under non-uniform label distributions.

---


### 72. [Discrete Diffusion Models: A Unified Framework from Tokenization to Generation](https://arxiv.org/abs/2607.13431)

**<font color=#1a73e8>作者：</font>** Ye Yuan, Weien Li, Rui Song 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete denoising diffusion models (DDMs) have recently emerged as a compelling alternative to autoregressive (AR) modeling for discrete data, offering parallel generation and iterative global refinement capabilities. Unlike continuous diffusion, where the state space is fixed, DDMs are fundamentally shaped by how the discrete state space is constructed: the tokenization scheme, the vocabulary topology, and domain-specific structural alphabets. This work introduces a unified conceptual framework that views discrete diffusion models through the construction of the underlying discrete state space. Within this framework, existing formulations, including transition-matrix, masking/absorbing-state, and score/ratio-based approaches, emerge as different instantiations of a common design space. The framework further exposes common design trade-offs across training objectives, inference algorithms, scaling behavior, systems optimization, and evaluation protocols, suggesting several promising directions for future research.

---


### 73. [Local Redundancy: An Information-Theoretic Measure of Plasticity from Synthetic Memorization](https://arxiv.org/abs/2607.13432)

**<font color=#1a73e8>作者：</font>** Jiaxuan Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Plasticity -- a neural network's ability to adapt to new tasks -- is critical for continual and transfer learning. Existing measures, such as effective rank, dead neuron fraction, and weight norm, lack theoretical grounding and correlate poorly with performance on new tasks. We introduce local redundancy, an information-theoretic measure derived from universal compression theory. We define local redundancy as the worst-case redundancy of a local model family -- parameters in an infinitesimal neighborhood along gradient directions -- and show this is a principled measure of plasticity. Although local redundancy is intractable to compute exactly, we prove that the expected squared gradient norm on a synthetic memorization task provides an efficiently computable lower bound. Experiments on continual image classification and time series transfer learning demonstrate that local redundancy predicts downstream performance better than existing measures and enables pretraining checkpoint selection where validation loss plateaus.

---


### 74. [Distributionally Robust and Safe Imitation Learning](https://arxiv.org/abs/2607.13436)

**<font color=#1a73e8>作者：</font>** Ahmed Aboudonia, Naira Hovakimyan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imitation learning (IL) has achieved remarkable success in complex decision-making tasks. However, its performance is highly sensitive to distribution shifts, which can pose significant safety risks. We propose a distributionally robust and safe IL framework that explicitly addresses both policy-induced and uncertainty-induced distribution shifts. Our approach develops a unified framework leveraging Taylor Series Imitation Learning (TaSIL) to mitigate policy-induced shifts and distributionally robust adaptive control to handle uncertainty-induced shifts. This architecture enables the formulation of an IL problem that optimizes performance under distributional uncertainty while systematically accounting for safety constraints. We demonstrate the effectiveness of the proposed approach on an unmanned aerial vehicle (UAV) case study where the UAV performs a task in an uncertain environment while avoiding unsafe regions.

---


### 75. [CLIP-Guided Label-Free Discriminative Region Scoring for Fine-Grained Classification](https://arxiv.org/abs/2607.13437)

**<font color=#1a73e8>作者：</font>** Yujie Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent vision models such as CLIP and SAM enable training-free segmentation and semantic encoding for fine-grained classification. A common approach is to compare the representations of segmented image regions with the text prompt embeddings of the corresponding labels. However, it remains unclear how different local regions and CLIP-based scoring strategies affect the selection of discriminative evidence, especially when ground-truth labels are unavailable. In this paper, we propose a unified CLIP-guided label-free region scoring framework for fine-grained classification. The framework evaluates cosine similarity-based, margin-based, and entropy-based scoring strategies using both SAM-generated masks and random crops, and introduces two label-free pseudo-label variants based on global image embeddings and local region embeddings. We conduct experiments on five fine-grained classification datasets to systematically compare different region generation methods and scoring strategies. The results show that Soft Negative Margin scoring achieves the strongest performance, and pseudo-label scoring closely approximates true-label performance. Although SAM produces semantically meaningful masks, random-crop-based pseudo-label scoring consistently outperforms SAM-based scoring across all datasets, suggesting that random crops preserve surrounding information and provide more stable semantic context when pseudo-labels are noisy. In addition, SAM masks benefit from aggregating embeddings from all regions, whereas random crops tend to perform better with a smaller top-k subset. These findings provide new insights for fine-grained classification.

---


### 76. [DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2607.13439)

**<font color=#1a73e8>作者：</font>** Mingyang Sun, Guozhu Meng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly applied to vulnerability detection due to their strong code comprehension capabilities, but most existing approaches rely on isolated functions or context extracted by fixed program-analysis rules. These methods cannot adaptively explore repository-level dependencies to gather sufficient context when vulnerabilities span multiple functions or files, compromising detection reliability. We present DREA (Decoupled Reasoning and Exploration Agents), a hypothesis-driven framework for repository-level vulnerability detection. DREA decouples reasoning from exploration through two collaborating agents: a planning agent backed by an advanced LLM that forms vulnerability hypotheses and directs the investigation, and an explorer agent powered by a lightweight model that retrieves repository-level context on demand. Goal-directed context acquisition is the primary source of detection improvement in this design, while offloading token-heavy exploration to the local model keeps inference economically tractable. To support evaluation, we construct RepoPairBench, a repository-grounded benchmark of validated Python vulnerability-fix pairs from real-world projects. Beyond binary detection accuracy, we introduce a reasoning correctness evaluation to assess whether a model's rationale matches the documented vulnerability mechanism. Across three LLMs, DREA improves Pair-Correctness from 19-26% to 30-42% while offloading over 93% of tokens to the explorer, reducing estimated billable API cost by a factor of 16-48. Reasoning correctness analysis further reveals that 26-55% of true positives, for both DREA and the function-only baseline, are correct predictions supported by flawed rationales, identifying security reasoning quality as a shared bottleneck for current LLMs.

---


### 77. [ε-Indistinguishability In Moving Target Defense: Framework, Algorithms, And Cloud Case Studies](https://arxiv.org/abs/2607.13440)

**<font color=#1a73e8>作者：</font>** Sailik Sengupta, Ankur Chowdhary  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Moving Target Defense (MTD) assumes its pool of candidate configurations is safe to cycle among, i.e. latency and other observables do not trivially fingerprint the active choice, but this assumption has not been quantified at the pool level. We formalize this pool-safety problem as finding the largest $\varepsilon$-close subset of the Cartesian product of per-component implementation choices, reducing pairwise indistinguishability under an additive utility model to a densest-window query over a sum-set. We give four algorithms spanning the scalability spectrum -- full enumeration, meet-in-the-middle, FFT convolution, and Monte Carlo sampling -- covering configuration spaces from tens to $10^{38}$. We then measure the anonymity gap end-to-end on two production cloud case studies, and find that a component's latency differences do not survive deployment unchanged: a four-runtime serverless rotation, where nothing else masks the interpreter, collapses from four-way to three-way anonymity against a VPC-adjacent adversary, while a $27$-configuration three-tier stack, where the same interpreter differences are instead absorbed by a shared $8$~ms database round-trip, delivers nine-way effective anonymity. The framework and the two case studies together suggest a diagnostic for MTD design: rotating a component adds anonymity only if the latency differences among its variants are too small for the adversary to identify.

---


### 78. [ReBound: Reuse-Aware Privacy For Interactive Decision Support](https://arxiv.org/abs/2607.13441)

**<font color=#1a73e8>作者：</font>** Nada Lahjouji, Shufan Zhang, Xi He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differentially private decision support frameworks answer complex aggregate threshold queries with formal bounds on false negative and false positive rates, but treat each query independently with no memory of past results. In practice, analysts work interactively, issuing sequences of related queries that refine bounds, adjust thresholds, or derive new functions from previous ones. We propose ReBound, a framework that reuses cached results from previous queries to answer new queries at reduced or zero additional privacy cost while maintaining formal utility guarantees. ReBound introduces a reuse framework for multiple refinement types, a cache graph structure for efficient lookup of reusable results, and a negotiation mechanism for when requested bounds cannot be met within budget.

---


### 79. [DreamSat-Pose: Spacecraft Pose Estimation from Single-View 3D Reconstructions and Learned 2D-3D Feature Matching](https://arxiv.org/abs/2607.13449)

**<font color=#1a73e8>作者：</font>** Josiane Uwumukiza, Jocelyn Zhao, Giovanni Lavezzi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 6-DoF pose estimation is a critical task in autonomous rendezvous and proximity operations. In the case of an unknown target, this task becomes challenging as it shall be paired with the reconstruction of the target shape model. In this article, we propose a novel framework for single-shot shape and pose estimation of unknown spacecraft objects. Given a single image, we first reconstruct a 3D shape model of the target, then estimate the relative six-degrees-of-freedom pose by learning dense 2D-3D correspondences. The image features are extracted using a frozen DINOv3 vision transformer, while the geometric features are computed from the reconstructed point cloud using a trainable dynamic graph convolutional neural network encoder. A dual-stream transformer matcher refines descriptors through alternating self- and cross-attention, producing soft correspondences that are passed to a Perspective-$n$-Point solver for pose recovery. We evaluate the method on the SPE3R dataset and consider FoundationPose as a representative baseline for current state-of-the-art capabilities. Results show reliable pose estimates achieving 0.157 degrees mean pointing error using only a single image and reconstructed geometry, demonstrating strong generalization to unseen spacecraft.

---


### 80. [Symbiosis-Inspired Knowledge Distillation for Incremental Object Detection](https://arxiv.org/abs/2607.13452)

**<font color=#1a73e8>作者：</font>** Mingyue Zeng, De Cheng, Zhipeng Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incremental object detection (IOD) aims to extend detectors to new categories while retaining previously acquired knowledge. Existing methods often adopt a class incremental learning perspective, separating feature spaces to sharpen decision boundaries. However, this separation-oriented paradigm may overlook object symbiosis in detection, where co-occurrence and occlusion introduce spatial and semantic dependencies that benefit from shared representations. Ignoring these dependencies distorts the shared representations, exacerbates confusion between old and new classes, and accelerates catastrophic forgetting. To address this, we propose Symbiosis-Inspired Knowledge Distillation (SIKD), which explicitly leverages object symbiosis at two complementary levels. Spatial Symbiosis Distillation (SpSD) focuses on symbiotic regions where the old model responds with high overlap to objects in the new task. It preserves generalizable old class cues, suppresses class-specific bias and redundancy, and distills the refined evidence to the new model at matched spatial locations with slot-aligned supervision. Semantic Symbiosis Distillation (SeSD) maintains class level structure by forming confidence weighted prototypes for old classes and aligning their inter class soft ranks over the old class logits, which stabilizes the semantic topology during adaptation. Extensive experiments demonstrate the effectiveness and superiority of the proposed method.

---


### 81. [Adversarial Prompting Framework for AI Safety Assessment](https://arxiv.org/abs/2607.13453)

**<font color=#1a73e8>作者：</font>** Yash Bhatnagar, Kunal Banerjee, Anirban Chatterjee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI), especially Generative AI (GenAI), adoption has increased in industries significantly in recent years. However, the use of these models may also expose systems to new forms of cyberattacks by different malicious actors -- adversarial prompt attack (APA) being one of the most prominent examples of such threats. This paper presents the implementation of an Adversarial Prompting Framework (APF) for a comprehensive assessment of AI safety. The framework systematically evaluates the resilience of the AI model through the generation of structured adversarial prompts at multiple sophistication levels, from direct harmful requests to advanced encoding-based attacks. Our implementation demonstrates the practical application of this methodology in enterprise environments, providing automated testing capabilities with quantitative security assessment metrics. The results indicate significant variations in the model vulnerabilities across different attack vectors, with encoded prompts presenting the highest success rates in bypassing safety mechanisms.

---


### 82. [TreeSRNF: Square-Root Normal Fields for Generative Modelling of the Geometric and Structural Variability in Tree-like 3D Objects](https://arxiv.org/abs/2607.13456)

**<font color=#1a73e8>作者：</font>** Tahmina Khanam, Hamid Laga, Mohammed Bennamoun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a novel mathematical framework for analyzing and generating complex tree-shaped 3D objects, such as botanical trees and plants, which deform both in their 3D geometry and branching structure. Unlike previous works, which either consider only the skeletal structure of tree-like objects or approximate their 3D geometry using branch thickness, the proposed framework accurately models both the 3D geometry of the tree branches and the way they are interconnected. In this paper, we first generalize the Square Root Normal Fields (SRNF) representation, originally proposed for the statistical analysis of genus-0 surfaces, to tree-shaped 3D objects. We then treat tree-shaped 3D objects as points on a novel Riemannian tree-shape space equipped with a novel Riemannian metric that measures the amount of surface bending and stretching, and structural changes one needs to apply to one 3D tree-shape to align it with another. This way, deformations become trajectories in this novel tree-shape space. We analyze the theoretical properties of this novel tree-shape space and the corresponding metric and develop algorithms for computing point-wise and branch-wise correspondences and geodesic paths between complex 3D trees. We finally show how to use these building blocks for (1) computing statistical summaries, \ie means and modes of variation, of collections of tree-shaped 3D objects, and (2) synthesizing novel tree-shaped 3D objects by sampling from probability distributions fitted to a population of tree-shaped 3D objects. We demonstrate the performance and utility of the proposed framework on real and synthetic plants and botanical trees and show that it significantly outperforms the state-of-the-art.

---


### 83. [Live Gurbani Tracking: A Benchmark and Reference System for Captioning Sikh Kirtan](https://arxiv.org/abs/2607.13457)

**<font color=#1a73e8>作者：</font>** Karanbir Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a benchmark and reference system for live captioning of Sikh Kirtan - the continuous, sung recitation of verses from the Sri Guru Granth Sahib Ji (SGGS). Unlike open-vocabulary lyrics transcription, Kirtan captioning is a closed-vocabulary problem: every displayed line must be an exact, word-for-word line from the canonical scripture, because displaying misspelled Gurmukhi is considered religiously inappropriate. We formalize the task as predicting, at every time t, a pair (shabad_id, line_idx) or null, and organize the problem space into a 2x2 matrix along two orthogonal axes: live vs. offline (causal vs. full-audio access) and blind vs. oracle (shabad identity discovered vs. given). We release v1 of the benchmark - 4 hand-annotated Kirtan recordings x 3 cold-start offsets = 12 evaluation cases, ~57 minutes of scored audio - together with a scorer that computes frame accuracy at 1s resolution over a scored region, with a 1s collar and gap-tolerant scoring at segment boundaries. We describe a reference system (fine-tuned 120M IndicConformer -> fuzzy matcher -> state machine; INT8 ONNX; RTF ~0.05 on one Apple Silicon core) that achieves 57.9% overall frame accuracy across all 12 cases (10/12 correct shabad locks) on the hardest variant (live x blind). We compare against three trivial baselines (empty, shifted-5s, perfect) and discuss why standard ASR metrics (WER/CER) measure transcription accuracy rather than the display accuracy this task requires. The benchmark, reference system, and a live deployment are released under permissive licenses to facilitate further improvements.

---


### 84. [2D Rotary Position Embedding for Scene Text Recognition with Transformers](https://arxiv.org/abs/2607.13458)

**<font color=#1a73e8>作者：</font>** Zobeir Raisi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene Text Recognition (STR) remains challenging due to the diversity of text appearances, including curvature, rotation, and perspective distortion. Recent Transformer-based approaches perform well but usually rely on one-dimensional positional encodings that ignore the 2D spatial structure of text images. Axial 2D extensions of Rotary Position Embedding (RoPE) exist for vision Transformers, but they assume roughly square, isotropic image content and apply the rotation only within encoder self-attention. Scene text violates both assumptions: crops are markedly anisotropic, and STR models are encoder-decoder, so the decoder must relate its queries to the encoder's 2D layout through cross-attention. We introduce 2D-RoPE-STR, which adapts axial 2D-RoPE to this setting through (1) an anisotropic row/column dimension allocation matched to the aspect ratio of text, and (2) an extension of the rotary coupling into encoder-decoder cross-attention, letting autoregressive decoding steps attend to encoder tokens by their 2D layout, a setting not addressed by prior encoder-only formulations. Both changes are essentially parameter-free and require no architectural redesign beyond the positional-encoding module. We further introduce a diagnostic protocol (a controlled ablation pair isolating only the positional encoding, an image-level net-win disagreement analysis, and encoder attention visualization) that identifies where and why relative 2D position helps: curved, rotated, and perspective-distorted layouts where reading order departs from a straight horizontal line. On six standard benchmarks (IIIT5K, SVT, ICDAR 2013, ICDAR 2015, CUTE80, SVTP), gains concentrate on exactly these irregular layouts, with ablations isolating each design choice against 1D RoPE and 2D sinusoidal and learnable alternatives.

---


### 85. [LPM: Industrial-Scale Generative Video Restoration](https://arxiv.org/abs/2607.13460)

**<font color=#1a73e8>作者：</font>** Bichuan Zhu, Fulin Li, Jiachao Gong 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present the Large Processing Model (LPM), a diffusion-based generative framework for photorealistic video restoration under complex, in-the-wild degradations. To our knowledge, LPM is the first generative video restoration model deployed at industrial scale. LPM addresses the diverse degradations in user-generated content (UGC) through a unified system encompassing large-scale data engineering, foundation-model training, and efficient inference. Its enhanced architecture, progressive training strategy, and temporal-pyramid inference mechanism jointly enable high-fidelity, temporally consistent restoration of arbitrarily long videos across the broad content distribution encountered on UGC platforms. LPM has been deployed in production at Kuaishou, where videos processed by the model account for approximately 45% of total viewing time, delivering consistent improvements across key quality-of-experience metrics. Beyond perceptual enhancement, LPM delivers substantial system-level benefits: at comparable perceptual quality, it reduces bitrate by 20% relative to Kuaishou's in-house codec, yielding annual bandwidth cost savings on the order of hundreds of millions. Its low serving cost also enables integration into products such as Kling, demonstrating that generative restoration can be practical, scalable, and cost-effective for large-scale video processing.

---


### 86. [DevicesWorld: Benchmarking Cross-Device Agents in Heterogeneous Environments](https://arxiv.org/abs/2607.13465)

**<font color=#1a73e8>作者：</font>** Huatao Li, Xinwei Geng, Yuheng Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based agents have rapidly improved at operating individual digital environments such as mobile applications, desktop systems, and smart homes. However, real-world user goals often span multiple devices: information may come from a phone, be processed on a desktop, and the result may need to appear on another device. Most existing benchmarks center on a single dominant execution environment, making it difficult to evaluate whether agents can acquire and integrate information across heterogeneous devices and complete end-to-end tasks with cross-device dependencies. We introduce DevicesWorld, a large-scale executable benchmark for cross-device collaborative operation. DevicesWorld contains 6,140 tasks and integrates three classes of device environments -- mobile, desktop, and IoT -- into a unified cross-device interaction and evaluation framework. Each task defines a natural-language user goal, participating devices and initial states, executable actions, rule-based verifiers, and a cleanup procedure. A multi-stage construction and quality-control pipeline keeps tasks close to realistic user needs while allowing final outcomes to be automatically verified from device states and generated files. We evaluate five frontier LLM-agent systems on a fixed evaluation set. All methods achieve low success rates, with the best reaching only 12.5%. Among failed runs, about 28.7% satisfy at least one scoring condition yet still fail the full task. Trajectories show that agents become stuck acquiring information or manipulating interfaces, confuse source and output devices, or terminate before all conditions are jointly satisfied. DevicesWorld turns cross-device collaborative operation into an executable, reproducible, and diagnostically useful evaluation problem for research on reliable cross-device agents.

---


### 87. [HIVE-3D: Hierarchical Voxel Enhancement for High-Quality 3D Scene Generation](https://arxiv.org/abs/2607.13468)

**<font color=#1a73e8>作者：</font>** Bin Zang, Wenting Zheng, Xiaoliang Luo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, a line of works can generate impressive 3D objects from a single image, but they are limited by restricted representation resolution, making them unsuitable for 3D scene generation. In this work, we introduce HIVE-3D, a novel method for high-quality 3D scene generation based on hierarchical voxel enhancement framework. Specifically, given a single scene image as input, we first produce a coarse initial scene, then introduce image segmentation and attention-based retrieval to align 2D image components with 3D scene components. Subsequently, we organize these scene relations into a hierarchical component tree, where nodes closer to the leaves denote finer-grained components. Finally, we propose a voxel super-resolution model that generates refined voxels for the target instance while maintaining strong consistency with the coarse voxels. Equipped with this model, we perform coarse-to-fine hierarchical super-resolution on images and voxels for each component, producing a high-resolution and high-quality 3D scene. Extensive experiments demonstrate that our method significantly outperforms previous approaches, achieving state-of-the-art performance.

---


### 88. [Explainable Artificial Intelligence for Anomaly Detection in Banking Transactions: An Internal Audit Perspective](https://arxiv.org/abs/2607.13469)

**<font color=#1a73e8>作者：</font>** Anupa Lodhi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The banking sector increasingly relies on automated systems to monitor electronic transactions for signs of fraud, yet conventional rule-based approaches struggle with high false-positive rates and offer no justification for their outputs, limiting their utility for compliance teams. This paper introduces an Explainable Artificial Intelligence (XAI) framework tailored for banking transaction anomaly detection within internal audit workflows. An Isolation Forest (iForest) model performs unsupervised anomaly scoring, while a SHAP (SHapley Additive exPlanations) layer provides transaction-level, feature-attributed explanations grounded in cooperative game theory [8]. A lightweight Streamlit dashboard renders these outputs in a form accessible to audit professionals without machine learning expertise. Evaluation on a synthetic banking dataset yields 0.91 precision and 0.88 recall, outperforming three unsupervised baselines. Expert feedback confirms that feature-level explanations measurably improve auditor confidence and decision quality. The framework advances the practical deployment of accountable, transparent AI in regulated financial environments.

---


### 89. [Bring Music The Horizon: Music-Driven 360$^\circ$ Video Generation](https://arxiv.org/abs/2607.13471)

**<font color=#1a73e8>作者：</font>** Kai Hsu Tsai, Yong Wei Fu, Hung I Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Music visualization offers a powerful way to enhance listeners' understanding and experience of music by translating auditory signals into visual forms. However, most existing approaches either rely heavily on lyrics or generate flat, non-immersive videos similar to conventional music videos, which limits their ability to convey the emotional dynamics of music and provide an immersive listening experience. We propose Bring Music The Horizon, an emotion-aware pipeline for music-driven 360$^\circ$ video generation. Given an input song, our work first estimates its emotional trajectory by predicting valence-arousal values at the level of every four bars. These values are then converted into emotion-aware visual guidance using EmotiCrafter, and these guidance vectors can be manipulated by the SEGA framework, which provides fine-grained semantic control for keyframe generation. Finally, image-to-video models are applied to the generated keyframes to synthesize temporally continuous 360$^\circ$ videos for immersive music visualization. Our pipeline generates 360$^\circ$ music visualization videos that reflect the emotional progression and temporal structure of the input song. We demonstrate its capability using songs from different genres and provide qualitative comparisons with From-Sound-To-Sight, a representative audio-to-visual generation baseline, on our project page at this https URL.

---


### 90. [To Play or Not to Play: Insights and Lessons Learned from 20 Years of CTFs with ENOFLAG](https://arxiv.org/abs/2607.13480)

**<font color=#1a73e8>作者：</font>** Jörg Schneider, Sebastian Neef, Sebastian Koch  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security contests in the form of CTF (Capture The Flag) exercises are nowadays a common way to learn cyber security. 20 years ago at DIMVA 2006 the on-site CTF CIPHER II was one of the conference highlights and led to the foundation of the team ENOFLAG. In this poster, we reflect on the changes in the CTF gameplay and report on lessons learned while running an academic CTF team for 20 years.

---


### 91. [GPOcc++: Unified Sparse Gaussian Occupancy Prediction with Visual Geometry Priors](https://arxiv.org/abs/2607.13481)

**<font color=#1a73e8>作者：</font>** Changqing Zhou, Yueru Luo, Yulan Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D scene understanding is fundamental to embodied intelligence and autonomous driving, where 3D occupancy provides a unified representation of objects, structures, and free space. However, recovering such a complete volumetric representation from visual observations remains challenging, particularly in occluded and unobserved regions. Visual geometry priors offer strong and generalizable geometric cues for addressing this challenge, but their outputs are inherently surface-centric, whereas occupancy prediction requires reasoning about volumetric interiors and free space. To bridge this gap, we introduce GPOcc, which transforms visual geometry priors into occupancy-aware sparse Gaussian representations for efficient and expressive volumetric scene modeling. Building on GPOcc, GPOcc++ models multi-view observations and temporal sequences within a unified framework, allowing spatial and temporal evidence to be handled through the same representation. We further extend GPOcc++ from indoor scenes to outdoor occupancy prediction. Extensive experiments on both indoor and outdoor benchmarks demonstrate consistently strong performance across both multi-view and temporal settings, together with favorable efficiency and generalization. Code will be released at this https URL.

---


### 92. [DeepLoop: Depth Scaling for Looped Transformers](https://arxiv.org/abs/2607.13491)

**<font color=#1a73e8>作者：</font>** Shuzhen Li, Yifan Zhang, Jiacheng Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers scale sequential computation by applying a compact stack of physical blocks for multiple rounds, increasing unrolled depth without increasing stored parameters. This reuse changes the residual-scaling problem: in an untied Transformer, each residual branch receives and applies its own parameter update, whereas in a looped Transformer one shared update aggregates gradients from repeated visits and is read back by those same visits in the next linearized forward pass. We formalize this tied-depth effect through a first-order perturbation bound controlled by a visit-alignment coefficient $\kappa_R$. The bound recovers the DeepNorm exponent when visits decorrelate, but in the conservative aligned regime it requires the exponent to increase from $1/4$ to $1/2$ as loop count grows at fixed physical depth. The resulting method, \textbf{DeepLoop}, keeps the Post-LN DeepNorm architecture and sets $\alpha=(2N)^{1/2}$ and $\beta=(8N)^{-1/2}$ for unrolled depth $N$. On GPT-style looped language models at GPT-2 small and GPT-2 medium scale, DeepLoop is neutral when no physical block is revisited and improves validation loss and downstream accuracy once recurrent depth is activated. These results show that stable recurrent depth requires residual scaling rules that account for parameter visits, not only nominal layer count.

---


### 93. [CASA-SDF: Curriculum-Aware Spatial Adaptation with Curvature-Guided Density for Neural Implicit Surface Reconstruction](https://arxiv.org/abs/2607.13492)

**<font color=#1a73e8>作者：</font>** Lei Yang, Weiqing Li, Zhiyong Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural implicit representations have emerged as a powerful paradigm for 3D reconstruction. However, high-fidelity indoor surface reconstruction remains a significant challenge, primarily due to the pronounced \emph{geometric heterogeneity} of indoor scenes. Large texture-less planar regions typically require stronger regularization to suppress high-frequency artifacts, while thin structures demand sharper, more adaptive representations to mitigate the spectral bias of multi-layer perceptrons (MLPs) and prevent over-smoothing. Existing approaches often rely on spatially indiscriminate prior supervision and a scene-global SDF-to-density transformation, which constrains their ability to balance planar smoothness and detail preservation. In this paper, we propose CASA-SDF (Curriculum-Aware Spatial Adaptation for SDF), a unified framework that addresses this challenge via complementary adaptations of supervision and representation capacity. Specifically, Hybrid Spatially-Adaptive Uncertainty Annealing (SAUA) fuses semantic and photometric uncertainties to construct a pixel-wise curriculum for monocular prior supervision. This strategy maintains regularization in reliable regions while attenuating unreliable supervision early in training to enable data-driven photometric refinement. Meanwhile, Curvature-Aware Locally Adaptive Density Transformation (CALADT) progressively modulates the sharpness of the SDF-to-density mapping via a curvature proxy to enhance the representation of thin structures. Extensive experiments on benchmark indoor datasets demonstrate that CASA-SDF improves surface completeness and detail recovery on high-frequency structures, without compromising the stability of planar surfaces.

---


### 94. [A VAE-Driven Multi-Task Satellite-Aided Semantic Communication Framework for 6G-Enabled Connected Autonomous Vehicles](https://arxiv.org/abs/2607.13494)

**<font color=#1a73e8>作者：</font>** S. M. Abtahiul Alam, Niloy Das, Apurba Adhikary 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The development of smart transportation systems and the introduction of 6G wireless communication technologies have significantly changed vehicle network topologies. Future connected autonomous vehicle (CAV) networks require bandwidth-efficient, reliable, and low-latency communication for safety-critical applications such as traffic sign recognition and decision-making. Conventional communication systems transmit raw data regardless of task relevance, which is inefficient in resource-constrained satellite channels where uplink bandwidth is scarce and propagation losses are large. Semantic communication addresses this limitation by transmitting task-relevant information instead of full signal representations. It extracts and conveys essential semantic features and leverages deep learning to optimize task performance at the receiver. Therefore, we present a Variational Autoencoder (VAE)-based multi-task semantic communication framework for satellite-assisted autonomous driving. Unlike deterministic autoencoder-based methods, the proposed model uses probabilistic latent representations for more robust and efficient encoding. The learned features are transmitted over noisy wireless channels to perform traffic sign reconstruction and classification. The framework is trained end-to-end to jointly optimize both tasks. Results show that the proposed approach achieves significant bandwidth reduction of up to 87.23\% to 98.17\% while maintaining stable performance across varying signal-to-noise ratio conditions.

---


### 95. [Factorized Spectral Representations for Reinforcement Learning](https://arxiv.org/abs/2607.13498)

**<font color=#1a73e8>作者：</font>** Junyi Wu, Dan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning a compact model of the world from interaction data is central to sample-efficient deep reinforcement learning. Spectral representation methods have become the leading paradigm for representation learning in continuous control by taking a matrix view of the transition kernel, with state-action pairs on one side and next states on the other, and learning a low-rank factorization through self-supervised contrastive objectives. We take this view one step further. The transition kernel is naturally a three-mode tensor over states, actions, and next states, and a CP decomposition gives one feature map per mode. We propose FaStR, which fits this decomposition with a noise contrastive objective, producing separate state, action, and next-state encoders that together form a single spectral representation. The factored form yields a smaller hypothesis class, and the sample size needed for representation learning shrinks by a factor that scales with the smaller of the state and action dimensions. Empirically, FaStR delivers its largest gains on high-dimensional locomotion tasks whose dynamics align with the factored structure, and the learned state encoder transfers intact across actuator shift while only the action encoder is retrained.

---


### 96. [M2P-AD: Memory-to-Prototype Learning with Boundary-aware Score Refinement for 3D Anomaly Detection](https://arxiv.org/abs/2607.13499)

**<font color=#1a73e8>作者：</font>** Seyoung Jeong, Jong Pil Yun, Sang Jun Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D anomaly detection has recently emerged as an important research topic in computer vision. Although existing methods have achieved high performance, excessive anomaly responses in normal regions and false positives near object boundaries remain unresolved challenges. To address these challenges, we propose a novel 3D anomaly detection model, Memory-to-Prototype Anomaly Detection (M2P-AD), which effectively models the distribution of normal features while suppressing excessive anomaly scores in normal regions and false positives near object boundaries. Specifically, we introduce a Memory-to-Prototype (M2P) module that learns representative prototypes from normal feature embeddings to preserve important structural information of objects. In addition, a Boundary extraction (BE) module is integrated to identify object boundaries, and a Boundary-aware score refinement (BSR) strategy is applied to recalibrate anomaly scores by incorporating boundary characteristics. The proposed method is evaluated on Real3D-AD, Anomaly-ShapeNet, and MulSen-AD, achieving state-of-the-art performance. Qualitative results demonstrate that excessive anomaly scores in normal regions are reduced and false positives near object boundaries are suppressed, resulting in more accurate and stable anomaly localization. The results indicate that the proposed approach enables more reliable 3D anomaly detection and provides a robust solution applicable to real-world industrial environments.

---


### 97. [LAPO: Leave-One-Turn Attribution for Self-Generated Process Rewards in Multi-Turn Search Reasoning](https://arxiv.org/abs/2607.13501)

**<font color=#1a73e8>作者：</font>** Qiang Zhu, Jiajun Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for multi-turn search reasoning typically relies on terminal outcome rewards, which cannot distinguish useful, redundant, and harmful intermediate interactions. We propose LAPO, a self-generated process-supervision method based on backward leave-one-turn attribution. For each search turn, LAPO replaces the turn and its retrieval observation with a fixed [DELETE] placeholder and measures the resulting change in the current policy's mean log-likelihood of the gold answer. This Answer-Likelihood Gain estimates the turn's contribution while preserving all downstream interactions, allowing early evidence to be evaluated in the complete reasoning context. LAPO further applies sign-consistency gating, retaining only normalized process advantages whose directions agree with their raw attribution scores. The method requires no additional reward model, teacher, verifier, or LLM-as-a-Judge. Across seven knowledge-intensive question-answering datasets with local retrieval, LAPO achieves an average exact-match score of 0.326, outperforming the strongest step-reward baseline, IGPO, by 0.053. Ablations show complementary benefits from backward attribution and sign-consistency gating, demonstrating that policy-derived retrospective attribution can provide effective process supervision for multi-turn search agents.

---


### 98. [DP-BOA: Dirichlet-Process Birth-or-Assign for On-the-Fly Category Discovery](https://arxiv.org/abs/2607.13504)

**<font color=#1a73e8>作者：</font>** Peiyan Gu, Zixin Teng, Xuming He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-the-fly category discovery requires deciding for each incoming test sample whether to assign it to an existing category or spawn a new one. Existing methods typically implement this decision through matching-based heuristics, such as radius- or hash-based rules. While effective in practice, these methods usually treat category birth implicitly as a fallback when no existing category matches confidently, rather than as an explicit alternative supported by its own statistical evidence. To address this, we propose DP-BOA, a posterior-predictive decision framework based on an online Dirichlet-process Gaussian mixture model with a Normal-Inverse-Wishart prior. During training, we use labeled data to calibrate a shared NIW prior over category Gaussians and warm-start the known-category posteriors. At test time, for each incoming sample, DP-BOA compares the posterior predictive evidence for assignment to existing categories against the evidence for spawning a new category induced by the DP prior, and then updates category statistics online after the decision. The method captures anisotropic category geometry and naturally adapts decision confidence as evidence accumulates. Across standard OCD benchmarks, DP-BOA consistently outperforms strong baselines and delivers particularly strong novel-class discovery performance while maintaining competitive known-class accuracy.

---


### 99. [CODA: How to Mitigate ColumnDisturb for (Almost) Free?](https://arxiv.org/abs/2607.13505)

**<font color=#1a73e8>作者：</font>** Moinuddin Qureshi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> ColumnDisturb is a new data-disturbance error in which activations to an aggressor row cause bitflips in a victim row located hundreds of rows away (intra-subarray bitflips) and in victim rows in adjacent subarrays (inter-subarray bitflips). Intra-subarray ColumnDisturb can be tolerated by solutions (such as SALT and REGA) that operate at subarray granularity. However, to tolerate inter-subarray ColumnDisturb, such solutions must be extended with ColumnDisturb Protection (CDP), which performs additional {\em Adjacent-Counter Increment (ACI)} for the neighboring subarrays. The ACIs ensure that adjacent subarrays also undergo mitigation, even if they receive no demand activations. Unfortunately, because ACIs occur at a 200\% rate relative to demand activations, they effectively increase the activations perceived by the bank to 3x, which causes significant slowdowns (17\% at a TRHD of 500) and refresh overheads. The goal of our paper is to tolerate ColumnDisturb while incurring negligible overheads.
We propose CODA, a ColumnDisturb mitigation that significantly reduces the rate of ACI required to securely tolerate ColumnDisturb. We present three variants of CODA. First, CODA-E (Evade), which leverages the insight that ACI can be skipped if the neighboring subarray receives a demand activation, and reduces ACI by 2x. Second, CODA-F (Fraction), which uses the timing duration of ColumnDisturb to do only a fractional increment for ACI, thereby reducing the rate of ACI by 2x-16x. Finally, CODA-G (Gangskip), which operates at multi-subarray granularity and skips ACI for neighboring subarrays within the same gang, further reduces overall ACI by 2x-8x. Overall, CODA reduces ACI by 12x-1300x, thereby making it possible to tolerate ColumnDisturb while incurring zero performance and power overhead.

---


### 100. [TRACE-PCa: Predicting Prostate Cancer Progression from Longitudinal MRI During Active Surveillance](https://arxiv.org/abs/2607.13506)

**<font color=#1a73e8>作者：</font>** Hongye Zeng, Shreeram Athreya, Dingyuan Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active surveillance (AS) is the preferred strategy for favorable-risk prostate cancer, yet current protocols rely on scheduled repeat biopsies, most of which reveal no progression and are unnecessary. Existing risk-stratification tools operate on single time-point imaging or depend on explicit lesion segmentation, limiting their ability to capture longitudinal change and excluding patients without an MRI-visible lesion. In this study, we propose an end-to-end temporal and multimodal model for predicting pathological progression during AS without lesion segmentation. We encode each serial scan with a pretrained 3D MRI foundation model and introduce a temporal attention gate that recalibrates the multi-visit features to amplify focal imaging changes associated with progression. The gated imaging representation is then fused with clinical variables in a multimodal framework to estimate the probability of progression. Validated on a longitudinal AS cohort, our approach consistently outperforms competing baselines and performs comparably to the radiologist assessment representing current clinical practice. It maintains high negative predictive value while achieving higher positive predictive value, demonstrating its potential to safely reduce unnecessary biopsies during surveillance.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
