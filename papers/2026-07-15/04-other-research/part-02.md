# 📦 其他研究 | 2026年07月15日

> 本类共 **420** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-420](./part-09.md)

---

### 51. [Gauge dependence and structured-output corruption in sign-branched repetition penalties: measurements across models, inference stacks, and alternative repetition controls](https://arxiv.org/abs/2607.09791)

**<font color=#1a73e8>作者：</font>** Peter Hollows  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The multiplicative repetition penalty shipped across the LLM inference ecosystem (HuggingFace, vLLM, this http URL, and a dozen further engines) branches on the sign of each raw logit (divide positives by theta, multiply negatives). But the softmax is unchanged by adding a constant to every logit, so a model's logit zero-point is arbitrary, and the sign-branch reads that arbitrary point. The sign-branch is itself the accepted fix for an earlier bug, so the accepted fix branches on a quantity the training objective leaves unconstrained. Two measurable consequences follow. (1) The penalty is not well-defined: re-centring a model's logits by a constant is a provable no-op at theta=1, yet at a routine theta=1.3 it changes 58-96% of greedy tokens, where subtractive and normalized penalties change none; real checkpoints sit at widely different zero-points, so a fixed repetition_penalty is a different operation on every model. (2) It corrupts structured output: on 200 real-world JSON schemas, theta=1.3 drops the rate of valid, schema-conformant output from 97% to 23%. In our measurements, applying the penalty to normalized log-probabilities instead of raw logits removes both effects. HuggingFace already ships that operator (LogitNormalization); today it is off by default and applied after the penalty. This note gives the mechanism, the measurements (five models up to 7B, base and RLHF, on WikiText-103 prefixes; two code models on HumanEval and JSONSchemaBench; both effects replicated inside vLLM and this http URL through their own samplers on the same inputs), and the normalized variant.

---


### 52. [JEPA for AI-Native 6G: Predictive Representations and Open Challenges](https://arxiv.org/abs/2607.09798)

**<font color=#1a73e8>作者：</font>** Sheikh Salman Hassan, Irshad A. Meer, Almoatssimbillah Saifaldawla 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sixth-generation (6G) networks are moving toward AI-native operation, where learning modules are embedded across the radio access network (RAN), edge, and core. This transition requires learning from limited labels, heterogeneous wireless and network data, partial observations, non-stationary propagation, and latency-constrained control loops. Joint-embedding predictive architecture (JEPA) is a promising self-supervised paradigm for this setting because it predicts missing or future representations in latent space instead of reconstructing raw measurements or using contrastive negative samples. This article presents a wireless-oriented tutorial on JEPA for 6G intelligence. We define the JEPA training mechanism, describe how CSI, beam measurements, KPIs, topology graphs, and sensing observations can be tokenized and masked, and position the learned encoder as a predictive representation layer for RAN, O-RAN, edge, and core functions, with task-specific heads or controllers producing final decisions. Then we present an illustrative, beam-management case study suggesting that a wireless-aware target, specifically an auxiliary future beam-energy target during self-supervised pretraining, can improve label efficiency and robustness across shifted deployment conditions relative to a supervised source domain. Finally, we outline open challenges in multi-timescale prediction, action-conditioned modeling, distributed training, trustworthiness, efficient deployment, benchmarking, and standardization.

---


### 53. [The Silent Freeze: Predicting When Low-Precision Training Stops Learning](https://arxiv.org/abs/2607.09800)

**<font color=#1a73e8>作者：</font>** Zekai Shang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training in reduced floating-point precision can silently halt learning: when a gradient-descent weight update falls below half the unit in the last place (ULP) of the weight, it rounds away and that coordinate freezes while its gradient is still nonzero. The freeze is deterministic, governed by a per-coordinate half-ULP condition, and predictable from a high-precision trajectory and the target mantissa length alone, without low-precision data. In a small GPT trained under the standard AdamW-plus-cosine recipe with bf16-equivalent stored weights, training proceeds normally and then permanently freezes just past mid-run, within four steps of the a-priori prediction. In a $124$-million-parameter GPT-2 transformer whose weights are constrained to the $8$-bit floating-point grid after every optimizer step, with no master weights, the dense weights freeze at initialization in both fp8 formats -- predicted \emph{a priori} from an fp32 reference -- and validation loss plateaus while full precision keeps improving. Stochastic rounding removes the persistent freeze, and the same reference predicts that too. The condition transfers across frozen-feature regression, a mantissa-truncation emulator spanning $128\times$ in precision, small networks, and a CNN on MNIST: a computable axis of low-precision training, not diffuse noise.

---


### 54. [Discovering Latent Response Laws in Forced Physical Systems](https://arxiv.org/abs/2607.09801)

**<font color=#1a73e8>作者：</font>** Yi Zhu, Su Chen, Xiaojun Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Governing equations provide compact descriptions of physical systems, yet the variables in which they are simple are often hidden in high-dimensional measurements. This challenge is sharper for forced systems, whose responses depend on both intrinsic dynamics and time-dependent inputs. Here we introduce FLARE, a forced latent autoencoder for response equations that learns compact response coordinates, identifies sparse input-dependent latent dynamics and decodes equation rollouts to full responses. By estimating latent dimension from data and separating state estimation from external forcing, FLARE enables forecasts to be initialized from past responses and driven by prescribed future inputs. Across known dynamical systems, application-scale forced responses and visual observations, FLARE recovers compact forced dynamics and predicts long-horizon high-dimensional responses under inputs not used for training. By turning learned coordinates into a dynamical interface, FLARE extends equation discovery to systems whose effective states are hidden within complex observations, providing a route for interpretable modelling and prediction of high-dimensional responses in forced dynamical systems.

---


### 55. [Quota Marketplace: Dynamic Pricing for Efficient Allocation of ML Training Resources](https://arxiv.org/abs/2607.09802)

**<font color=#1a73e8>作者：</font>** Balasubramanian Sivan, Renato Paes Leme, Mihai Tiuca 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The escalating demand for Machine Learning (ML) training resources in recent years has resulted in a substantial gap between the high demand and the available supply. Efficient allocation of these scarce and expensive resources is crucial for organizations to maximize their return on investment. Existing resource allocation mechanisms, like Karma [OSDI'23], are designed to guarantee Pareto efficiency and max-min fairness in settings with dynamic (time-varying) user demands, but fail to preserve these key properties in the presence of demands with heterogeneous values. Given the ubiquity and inevitability of heterogeneity in organizational values of different workloads, effective resource allocation policies must accommodate these variations.
In this paper, we describe the design, implementation, deployment, and theoretical analysis of Quota Marketplace, a market-based mechanism to efficiently allocate ML training chips (like GPUs), explicitly addressing scenarios with demands of heterogeneous value. We detail the implementation of this mechanism within Google and present metrics that demonstrate its impact. We also discuss many business-critical requirements that the Quota Marketplace handles quite effectively, and document the gains and opportunities it has unlocked. We establish theoretically how this market-based approach achieves the essential properties of Pareto efficiency and max-min fairness by allowing the users to express the value of their workloads and enabling dynamic resource pricing based on supply and demand fluctuations. Ultimately, the market facilitates resource allocation that aligns with organizational priorities.

---


### 56. [Spectral Origins of the Self-Correction Blind Spot in Autoregressive Generation](https://arxiv.org/abs/2607.09803)

**<font color=#1a73e8>作者：</font>** Ingrid Petrova, Luan Vejsiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large autoregressive language models exhibit a self-correction blind spot: they reliably fix identical errors when attributed to an external source yet fail to fix the same errors in their own outputs. Prior work has documented this phenomenon empirically, through controlled error injection, error-depth decompositions, RL-based verifier-corrector training, and intrinsic self-verification, but offers no formal model of why generating a token suppresses the ability to detect its error, no quantitative activation condition for correction markers, and no convergence guarantee for reinforcement-learning-based self-correction. We close these gaps with SPARC, a spectral-algebraic theory of self-correction in autoregressive generation. We define the error-propagation operator as the product of per-step attention Jacobians on the residual stream and prove that the blind spot arises if and only if the spectral radius of this operator is at least one. We derive a sharp activation threshold, given as a function of the spectral radius, that a correction marker must exceed, recovering the 89.3\% blind-spot reduction observed with a simple ``Wait'' marker. We further prove that RL-based verifier-corrector training converges at a rate proportional to the squared coupling strength over the square root of the number of samples if and only if the verifier-corrector coupling matrix has spectral norm below one, and that this criterion is invariant across residual-stream autoregressive modalities, unifying text LLMs and autoregressive image and video generation. Experiments across four backbones and a visual autoregressive probe validate every theorem, with spectral predictions matching measured blind-spot rates within 3.2\% RMSE.

---


### 57. [Trivial Prompt Reframing Bypasses Safety Guardrails in Googleś MedGemma-4B](https://arxiv.org/abs/2607.09804)

**<font color=#1a73e8>作者：</font>** Avi-ad Avraam Buskila  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight medical language models are increasingly used as the base of patient-facing and clinician-support applications. Their model cards prohibit specific behaviors -- recommending exact drug dosages, issuing definitive diagnoses, prescribing treatments, adjudicating drug-drug interactions, and advising that emergency care can be skipped -- yet a model card describes intended behavior, not robust behavior. We quantify that gap for MedGemma-4B-it under attacks that require no technical sophistication. We build a fully factorial benchmark of 5 guarded-behavior concepts x 50 deterministically templated questions x 6 lay-accessible attack manners x 3 repetitions (4,500 generations), serve the model locally through Ollama under default sampling, and code every response refuse/hedge/comply with three independent judges (an LLM judge, a transparent regex judge, and an NLI-entailment judge). Under the primary LLM judge the overall Attack Success Rate (ASR, the fraction coded comply) is 38.0%. The two framings that reinterpret the request as legitimate dominate: recasting a question as a "medical board exam" item raises ASR from a 29.0% baseline to 53.1% (+24.0 points), and an appeal to an alleged doctor's authority raises it to 43.7% (+14.7); crude instruction-override prefixes have no significant effect. Robustness is dominated by topic: the drug-interaction guardrail is nearly absent (83.2% ASR) while the emergency-deferral guardrail is strong (4.7%) -- and the authority framing is the only attack that breaches it. We report Wilson confidence intervals, cluster-bootstrap effect sizes, a cluster-robust logistic regression, Cochran's Q, per-manner McNemar tests, and inter-judge reliability (Fleiss' kappa = 0.26); absolute ASR is judge-dependent while the ordering of attacks and topics is not. Our findings motivate stronger deployment-time guardrails for open medical models.

---


### 58. [Detangled: A Framework for Creating, Editing, and Inferencing Feature Rich Hair Strands](https://arxiv.org/abs/2607.09811)

**<font color=#1a73e8>作者：</font>** Sarah Jobalia, Yitong Deng, Carolyn Smith 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a framework for understanding and generating feature rich hair strands. Drawing upon both scientific and cultural expertise, we define strand texture as the various distinctive patterns (curling, switchbacks, twist, etc.) that are formed by forces internal to a hair strand. We begin by proposing a novel five-dimensional parameter space, intended to be a bijection with naturally occurring hair strand textures. This encoding is both qualitatively accessible, allowing users to readily locate their own hair in the parameter space, and quantitatively precise, allowing the generation of individual strands from texture inputs. Importantly, strand texture should be independent from the overall strand direction. In order to disentangle strand texture from the overall strand direction, we identify centerline geometry and use it to map strands into a canonical space (a strand texture space). We construct centerlines using a novel method that cleanly distills complex hair grooms, separating the strand texture from the overall style (parameterized by style guides). We enable the creation of new strands conforming to our parametric description of texture via a generative artificial intelligence approach supervised by a separate neural network trained to label candidate strands according to our five-parameter description. The ability to create new strands conforming to any desired texture enables groom editing using either texture transfer or user-provided inputs. We demonstrate results on a variety of hair types.

---


### 59. [A Guess and Determine Attack on the Elliptic Curve Discrete Logarithm Problem](https://arxiv.org/abs/2607.09814)

**<font color=#1a73e8>作者：</font>** Ayan Mahalanobis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper is a continuation of our earlier work, in which, we described a Las Vegas algorithm to solve the elliptic curve discrete logarithm problem. The Las Vegas algorithm reduces the elliptic curve discrete logarithm problem to finding a zero minor in a matrix. Using intersection poset of a hyperplane arrangement, we develop an algorithm to find a zero minor in a rectangular matrix. Our methods are elementary. We discuss the complexity of our algorithm, success probability and provide implementation details. We also provide simulation details. Finding a zero minor in a matrix is also of independent interest.

---


### 60. [RUBRIC: Realism--Utility Balanced Ranking for Imbalanced Classification](https://arxiv.org/abs/2607.09816)

**<font color=#1a73e8>作者：</font>** Yanxuan Yu, Dong liu, Renata Borovica-Gajic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class imbalance poses a fundamental challenge in risk-sensitive applications such as fraud detection and medical diagnosis, where minority-class samples are scarce yet critical for accurate classification. Existing oversampling methods generate synthetic samples to rebalance class distributions; however, they often produce large numbers of low-quality candidates that distort decision boundaries or introduce artifacts, leading to overfitting and degraded generalization.
In this work, we introduce RUBRIC, a generator-agnostic filtering framework that formulates synthetic sample selection as a quality-over-quantity optimization problem. RUBRIC ranks candidates using a realism-utility trade-off: realism is quantified by a learned discriminator that distinguishes real samples from synthetic samples, while utility captures proximity to the decision boundary through a concave margin-based scoring function. We show that, under mild regularity conditions, the proposed filtering strategy monotonically tightens the generalization bound for margin-based classifiers by jointly reducing distribution shift and suppressing near-negative tail contributions.
Through extensive experiments on credit-card fraud detection and other imbalanced benchmarks, we demonstrate that RUBRIC improves F1-macro and recall while maintaining comparable ROC-AUC across several generators. We also provide explicit lambda-sensitivity analysis to show how users can recover AUPRC when ranking quality is prioritized.

---


### 61. [Estimation, Prediction, and Assortment Optimization for Markov Chain Choice Models with Panel Data](https://arxiv.org/abs/2607.09817)

**<font color=#1a73e8>作者：</font>** Yalcin Akcay, Gerardo Berbeglia, Young-San Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a framework for the Markov chain (MC) choice model with panel data, including parameter estimation, personalized choice prediction, and personalized assortment optimization. In contrast to the traditional setting, which assumes that each transaction is independently drawn from a random utility model, our framework accounts for dependencies among transactions for the same customer in historical data, captured by partial-ordering preference information. To the best of our knowledge, our framework initiates the study of choice modeling with panel data under MC. As our primary result, we propose novel expectation-maximization (EM) algorithms for MC parameter estimation by incorporating partial-ordering-based customer preference information. On synthetic datasets and the sushi dataset, our EM algorithms outperform the traditional EM algorithm of Simsek and Topaloglu (Operations Research, 66, 2018) and multinomial-logit-based partial-order benchmarks adapted from Jagabathula and Vulcano (Management Science, 64, 2018). As our secondary contribution, we present hardness and computational results for conditional choice prediction and assortment optimization problems. These results complement our estimation framework and clarify the computational landscape of conditional choice and assortment optimization, which may be of independent interest.

---


### 62. [Learning Predictive Ambiguity Sets for Decision-Focused Distributionally Robust Optimization](https://arxiv.org/abs/2607.09820)

**<font color=#1a73e8>作者：</font>** Junjie Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predict-then-optimize systems usually compress uncertainty into a point forecast and then solve a downstream optimization problem as if the forecast were reliable. Distributionally robust optimization (DRO) offers protection against misspecification, but the ambiguity set is often centered at historical samples and uses a fixed radius. We propose \emph{learned predictive ambiguity sets} (LPAS): a deep contextual model outputs a finite nominal scenario distribution, a state-dependent Wasserstein radius, and optionally an anisotropic ground metric. These outputs define a contextual ambiguity set that feeds a DRO decision layer. The radius is trained by a combination of conditional quantile calibration, size regularization, and downstream decision loss, so that robustness is adaptive rather than globally fixed. We derive the finite dual form used by the decision layer, present a staged training algorithm, and evaluate the method on distributionally robust portfolio optimization with 20 S&P 500 constituents from 2018--2026. The proposed method substantially improves over equal-weight, predict-then-optimize, and historical Wasserstein DRO baselines, achieving 26.28% annualized return, Sharpe ratio 1.30, final wealth 1.61, and lower tail loss than a deep fixed-radius DRO baseline while using a smaller average radius. The results show that learned ambiguity radii can recover most of the performance of strong fixed-radius DRO while reducing unnecessary conservatism and improving regime adaptivity.

---


### 63. [Towards Objective Dysgraphia Detection: A Multi-Branch Deep Learning Approach for Online Handwriting Analysis](https://arxiv.org/abs/2607.09826)

**<font color=#1a73e8>作者：</font>** Lydia Ouhib, Yassine Ouzar, Zoé Pinseel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dysgraphia is a specific learning disability that is prevalent among school-age children. It affects handwriting coherence, quality, fluency, and legibility, often hindering academic achievement and early learning development. This motor coordination disorder is typically diagnosed through subjective assessments based on clinician observation, which can be timeconsuming and prone to variability. In this paper, we introduce a deep learning-based framework for objective dysgraphia detection using online handwriting data captured via digitizing tablets. The proposed framework relies on two complementary branches: the first pipeline extracts both handcrafted and embedding-based kinematic features directly from raw temporal signals, while the second leverages image-based representations of the temporal signals generated using continuous wavelet transforms (CWT) and Gramian Angular Fields (GAF). The resulting features are then fused to leverage the complementary strengths of both representations. The four representations were evaluated separately and jointly using the publicly available DiaGraMo dataset, showing that the fusion of GAF, MOMENT, and hand-crafted kinematic features outperforms each individual representation, as well as other fusion schemes. These findings highlight the potential of the complementarity of image and signal based representations for more objective dysgraphia detection.

---


### 64. [TDSal: Task-Based Top-Down Saliency Prediction Model](https://arxiv.org/abs/2607.09827)

**<font color=#1a73e8>作者：</font>** Can Mizrakli, Tolga K. Capin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual saliency aims to predict the regions of an image most likely to attract human visual attention. While most saliency models assume free-viewing conditions, human attention is often shaped by explicit task goals. In this work, we address task-driven saliency prediction by proposing a model that conditions visual attention on natural-language task descriptions. The model produces task-dependent saliency maps that reflect how attention shifts under different viewing intents. Through quantitative and qualitative analysis, we show that incorporating explicit task semantics enables more faithful modeling of goal-directed visual attention.

---


### 65. [A Strong Balanced-Softmax Classifier-Retraining Baseline for Long-Tailed Recognition](https://arxiv.org/abs/2607.09832)

**<font color=#1a73e8>作者：</font>** Juan Terven, Diana Margarita Córdova Esparza, Julio Alejandro Romero Gonzalez 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-tailed recognition methods often modify losses, margins, or representations to reduce the dominance of frequent classes. We ask whether, after Balanced Softmax training, the remaining tail error can be reduced by retraining only the classifier. We evaluate BS-cRT, a two-stage procedure that trains a backbone and cosine classifier with Balanced Softmax, freezes the backbone, and updates only the classifier on balanced episodic batches. The second stage keeps the empirical-prior Balanced Softmax objective and uses raw cosine logits at inference. Across CIFAR-100-LT, CIFAR-10-LT, ImageNet-LT, and Places-LT, this classifier-only step consistently improves Few-shot accuracy over the matched Balanced Softmax checkpoint. At imbalance factor 100, Few-shot gains are +5.15 points on CIFAR-100-LT and +5.83 on CIFAR-10-LT; on ImageNet-LT and Places-LT, gains are +6.92 and +9.78 points, respectively, with a Top-1/Few-shot trade-off on ImageNet-LT. We also analyze Counterfactual Boundary Risk Minimization (CBRM), a boundary-probe extension using prototype-based features near decision boundaries. CBRM identifies two failure modes: scaled-logit cosine margins destabilize training, and corrected hardest-negative probes remain head-class anchored. The results support BS-cRT as a practical classifier-side baseline and indicate that boundary supervision must account for class frequency.

---


### 66. [Generative Testing of Automated Speech Recognition Systems](https://arxiv.org/abs/2607.09833)

**<font color=#1a73e8>作者：</font>** Yanis Xabier Wilbrand Peña, Oliver Weißl, Andrea Stocco  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems have achieved high accuracy with transformer-based models, enabling deployment in critical applications. However, they remain vulnerable to adversarial manipulation, particularly in black-box settings where attacks must preserve perceptual naturalness. This work introduces GATAS, a black-box testing approach that generates failure inducing inputs by operating in the phoneme-level latent space of a text- to-speech model. Instead of perturbing waveforms directly, the approach interpolates latent representations to induce transcription errors while remaining within the manifold of natural speech. The attack is formulated as a multi-objective optimization problem balancing semantic divergence and perceptual quality. Our empirical evaluation against both white-box and black-box baselines shows that GATAS achieves a 98% success rate while producing lower distortion and higher perceptual quality, as confirmed by human studies. Despite operating without gradient access, GATAS remains competitive against white-box methods, highlighting that representation and perceptual alignment are more critical than access to model internals. Overall, our results demonstrate that untargeted latent-space optimization enables the efficient generation of realistic and effective test cases for ASR systems.

---


### 67. [Does YOLO26 Truly Offer Advantages Over Its Predecessors for Edge Deployment? A Benchmark Study in Aquaculture](https://arxiv.org/abs/2607.09835)

**<font color=#1a73e8>作者：</font>** Rakesh Ranjan, Gajanan S. Kothawade, Kata Sharrer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The recently introduced YOLO26 architecture incorporates NMS-free end-to-end inference and is optimized for deployment on resource-constrained CPU-based devices, making it well-suited for edge-based aquaculture applications. However, its performance, operational efficiency, and deployment suitability have not been systematically validated in aquaculture-specific scenarios. This study presents a comprehensive benchmark of YOLO26 against three Ultralytics predecessors (YOLOv5u, YOLOv8, and YOLO11) across nano, small, and medium model scales for fish mortality detection, a critical indicator of fish population health and welfare. Twelve model variants were evaluated for detection accuracy, training efficiency across seven dataset sizes, and inference performance on high-performance NVIDIA A100 GPUs and a CPU-only Raspberry Pi 5 edge platform. All models achieved comparable performance on the full dataset, with mAP50 differing by only 1.04 percentage points, indicating that architectural generation has little influence on final detection accuracy when sufficient training data are available. However, clear trade-offs emerged in data efficiency and deployment performance. YOLOv8 achieved 90% mAP50 with only 400 training images, whereas the YOLO26 nano and small variants required 1,000 images to reach comparable accuracy. Conversely, YOLO26n achieved the highest inference speed on the Raspberry Pi 5 (7.51 FPS), while YOLOv5mu outperformed all contemporary medium-scale architectures on CPU-based hardware. These results show that architectural novelty alone is insufficient for model selection and that training data availability, target hardware, and inference requirements should be considered jointly when selecting object detection models for practical edge AI deployment in aquaculture.

---


### 68. [Reliability-Aware Ensemble Classification Under Class Imbalance: A Calibration Study on Liquid-Based Cervical Cytology](https://arxiv.org/abs/2607.09837)

**<font color=#1a73e8>作者：</font>** Nisreen Albzour, Sarah S. Lam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cervical cytology classification models are typically evaluated on curated, class-balanced benchmarks, but real-world liquid-based cytology (LBC) collections are often small and class-imbalanced. This paper presents a class-imbalance-aware and calibration-aware ensemble classification study on the Mendeley LBC dataset, using its native four-class Bethesda taxonomy (NILM, LSIL, HSIL, SCC) rather than a collapsed binary formulation. Three lightweight architectures (Swin-Tiny, TinyViT-5M, DenseNet121) are trained directly on Mendeley LBC using weighted random sampling to counteract class imbalance, and compared against two soft-voting ensembles (Hybrid-2, Hybrid-3). Post-hoc temperature scaling is fit on a held-out calibration subset carved out of the training portion of each cross-validation fold, distinct from both the training data used to fit model weights and the evaluation fold used for final metrics, avoiding the optimistic calibration estimates that result when the same data is used for both purposes. Calibration substantially reduces expected calibration error, Brier score, and negative log-likelihood for every model and ensemble configuration tested, while discrimination metrics (accuracy, macro-F1, macro-AUROC) remain essentially unchanged. Ensemble size shows no consistent additional reliability benefit over the best individual model once all configurations are properly calibrated. Confusion matrices show that all classification errors, across every configuration, are confined to the boundary between high-grade lesions (HSIL) and carcinoma (SCC); no errors involve the negative (NILM) or low-grade (LSIL) categories. These results suggest that, for this dataset, calibration is the dominant lever for reliability, not ensemble size, though this conclusion should be read in light of the dataset's modest size.

---


### 69. [Nonlinear Axiomatic Attribution for Cooperative Games](https://arxiv.org/abs/2607.09869)

**<font color=#1a73e8>作者：</font>** Weida Li, Zhuanghua Liu, Yaoliang Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Shapley value is a widely used concept in attribution problems, as it uniquely satisfies the axioms of linearity, consistency, equal treatment, and efficiency. Often, the inclusion AUC metric is used to evaluate the quality of player rankings, in order to identify positively participating players. However, it can be established that the Shapley value is not always reliable for this purpose. The core issue lies in its linearity: the Shapley value acts as a linear operator with an excessively large null space, which is likely to contain non-negligible perturbations that remain indistinguishable to the operator. To address this limitation, we explore the design of nonlinear axiomatic attribution methods. Inspired by the least core, which is a popular nonlinear substitute for the Shapley value, we introduce a class of nonlinear attribution methods that retain the remaining necessary axioms. Each method yields a contribution vector that is the unique optimal solution to a minimization problem, which aims to approximate utility functions as faithfully as possible. In terms of the inclusion AUC metric, our experiments demonstrate the potential effectiveness of these methods compared to Shapley value variants that relax only the efficiency axiom. Our code is available at this https URL.

---


### 70. [Prompting-MammAlps: Fine-Grained Text-to-Video Retrieval for Camera-Trap Data](https://arxiv.org/abs/2607.09876)

**<font color=#1a73e8>作者：</font>** Valentin Gabeff, Baptiste Maquignaz, Jennifer Shan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatically retrieving videos from large camera-trap datasets remains challenging. Text-to-Video retrieval (TVR) methods based on large video-language models (VLMs) have potential to retrieve events of interest by describing them with simple text queries. However, current methods often lack spatiotemporal understanding and do not generalize well to ecological data. In this work, we introduce Prompting-MammAlps, the first camera-trap TVR benchmark, and propose a fine-grained and interpretable TVR method. Specifically, we trained a vision transformer to perform spatiotemporal action localization, and convert its output to structured text, describing each video. Independently, ethology-inspired queries are processed by a Large-Language Model (LLM) based coding agent to parse the structured text per video and retrieve videos accordingly. We harnessed the LLM to use functions from a custom parsing library to minimize the risk of LLM hallucinations and to improve method interpretability. This retrieval approach applied on the Prompting-MammAlps benchmark achieved a set-based F1-score of 34\% on a test set of 135 ecologically-relevant queries and 775 candidate videos. In comparison the best zero-shot VLM achieved a F1-score of 18\%, while also lacking interpretability. Project page: this https URL

---


### 71. [A Dual-Stream Challenge-Response Protocol for Ocular Liveness Verification](https://arxiv.org/abs/2607.09883)

**<font color=#1a73e8>作者：</font>** Ismail Kably  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ocular biometric systems face sophisticated presentation attacks, including high-resolution video replays and real-time generative deepfakes, which easily bypass static liveness checks. Current Presentation Attack Detection (PAD) frameworks typically rely on isolated physiological metrics, such as gaze tracking or the Pupillary Light Reflex (PLR), which can be spoofed independently. This paper proposes a Spatio-Luminance Sensor Fusion protocol, which introduces a dual-stream challenge-response framework for ocular liveness verification by uniting these metrics into a simultaneous authentication challenge. By generating a randomized, time-varying visual stimulus that fluctuates in both spatial trajectory and luminance intensity, we construct a mathematically coupled state-space likelihood model, termed the Synchronization Matrix, to evaluate the continuous cross-correlation between the expected biological latencies of smooth pursuit tracking and pupillary constriction. Using Monte Carlo simulation grounded in literature-derived latency distributions, we demonstrate theoretical separability between genuine and simulated attack conditions, and show that a multi-round challenge design improves the detection of generative deepfakes when a non-zero rendering-latency gap exists. This work provides a simulation-supported theoretical framework for next-generation dynamic spoofing defense in ocular and iris biometrics; human-subject validation is identified as necessary future work before deployment claims can be made.

---


### 72. [Nonparametric Bayesian Inverse Reinforcement Learning with Data-Parallel Gibbs Sampling](https://arxiv.org/abs/2607.09886)

**<font color=#1a73e8>作者：</font>** Sai Anirudh Katupilla, Shreeya Dasa Lakshminath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse Reinforcement Learning recovers reward functions from expert demonstrations, but standard formulations assume that all demonstrations come from a single expert. When demonstrations are pooled from multiple experts with distinct preferences, parametric methods recover an averaged reward that fits no individual expert well. We implement Nonparametric Bayesian Inverse Reinforcement Learning with a Dirichlet Process prior over reward functions, allowing the number of latent reward types to be inferred jointly with the rewards themselves. Inference uses a collapsed Gibbs sampler combining a Chinese Restaurant Process update for cluster assignments with a Metropolis-Hastings update for reward weights, and soft value iteration as the inner planning routine. We evaluate on a 10x10 ObjectWorld grid with two and three ground-truth reward types. The serial sampler recovers K=2 with Adjusted Rand Index of 1.000, substantially outperforming a Maximum Entropy IRL baseline (ARI=0.000). Extension to K=3 shows that the sampler correctly identifies the number of clusters in all runs; assignment ARI of 0.48-0.58 reflects behavioral overlap between expert types that persists across grid instantiations, revealing that reliable K=3 evaluation on ObjectWorld requires controlled object placement rather than random seeding. We further parallelize the sampler across CPU cores using Ray on HPC hardware, achieving a peak speedup of 4.79x at 8 workers, and characterize a throughput-versus-accuracy tradeoff arising from the consensus merge heuristic used during state aggregation. Code and a containerized environment are available at this https URL.

---


### 73. [Bridging the Catalog-to-Real Gap: Scalable Product Recognition via Multi-Stage Contrastive Learning](https://arxiv.org/abs/2607.09888)

**<font color=#1a73e8>作者：</font>** Anyi Zhang, Joy Mazumder, Kiril Lomakin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated product recognition is a cornerstone of modern retail intelligence; however, accurately matching real-world, in-store images against extensive corporate catalogs remains a major scalability bottleneck for large-scale applications. In this work, we address this challenge by reformulating the task as an embedding-based cross-domain retrieval problem rather than a standard closed-set classification task. Specifically, we define the objective as retrieving the most corresponding catalog reference image for a given real-world product query crop from an expansive inventory. To bridge the severe domain gap between pristine studio packshots and noisy in-store queries, we introduce a novel catalog-to-real multi-stage contrastive learning paradigm (Cat2Real). This framework fine-tunes a vision backbone by systematically exploiting both item-level and image-level similarities to drive targeted hard negative mining. Extensive empirical evaluations demonstrate that our paradigm scales seamlessly to unseen products and categories, yielding outstanding zero-shot generalization performance even in the complete absence of real-world training images for novel inventory.

---


### 74. [Remembering Distinct Items, Not Tokens: A Learnable Dirichlet-Process Cache Between State-Space Models and Attention](https://arxiv.org/abs/2607.09889)

**<font color=#1a73e8>作者：</font>** Siddharth Pal, Viktoria Rojkova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fixed-state sequence models compress an unbounded past into a bounded state, which caps their associative recall at roughly the state dimension; attention escapes the cap by keeping a key-value entry for every token, at quadratic compute and a cache that grows with the sequence. We study the middle ground: a sparse cache that allocates a slot only when an input is novel, so its size tracks the number of distinct items rather than the number of tokens. The allocation rule is the DP-means clustering rule, the small-variance limit of a Dirichlet-process mixture, used not as latent-variable inference but as the key-value memory operator for a deep recurrent backbone. We develop it in two forms, a static cache with a fixed concentration and a surprise-adaptive variant whose concentration follows the recent novelty rate. On a controlled associative-recall benchmark with redundancy we show that the cache matches full-attention recall while storing only the distinct items, that it dominates a fixed-budget eviction cache on the recall-versus-size frontier, and that on a state-space backbone it answers both a recall query and a long-range aggregate at the lowest memory of any model tested. The allocation is learnable end to end: a two-parameter novelty-threshold gate trained on the task loss alone recovers the rule exactly, whereas an over-parameterized gate fails, so the operative ingredient is the inductive bias rather than capacity. The evidence is a family of controlled mechanism studies at modest scale, with the distinct-items property confirmed on four real streams (recommendation, systems logs, clinical events, and insurance claims); a real-backbone, real-corpus language validation is pursued in a companion study.

---


### 75. [Do Transformer Temporal Heads and Post-Pooling Motion Gates Help CorrNet-based CSLR? An Empirical Study](https://arxiv.org/abs/2607.09890)

**<font color=#1a73e8>作者：</font>** Lisi Wang, Zhidong Xiao, Jianjun Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CorrNet is a strong baseline for continuous sign language recognition (CSLR) because it models inter-frame correlations inside the visual encoding stage. In this paper, we study two natural extensions of a reproduced CorrNet system: replacing the BiLSTM temporal head with a Transformer encoder, and injecting motion cues after temporal pooling. We find that the Transformer head does not outperform the BiLSTM baseline, even with a training strategy adjusted for the Transformer, and the two heads have almost the same computational and runtime cost. For the second extension, we design a lightweight module called MotionGate. In our experiments, MotionGate consistently collapses to an identity-like mapping: the gate loses motion selectivity, and the injected residual becomes a weak, non-selective perturbation of the pooled features. These results suggest that explicit motion injection after CorrNet's correlation-based encoding is largely redundant, and that natural-looking architectural extensions in CSLR should be tested carefully instead of being assumed to help.

---


### 76. [RouteRec: Strict Evaluation of Recommender-Agent Selection and Aggregation](https://arxiv.org/abs/2607.09908)

**<font color=#1a73e8>作者：</font>** Kaiji Zhou, Vladimir Kalmykov, Yue Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recommender systems increasingly face a choice among heterogeneous agents -- collaborative filters, sequential models, content-based retrievers, and LLM-based rerankers -- yet no single agent is uniformly best. We study this choice as task-aware agent ranking under cost constraints using RouteRec, a framework that compares request-level hard selection with item-level learned aggregation over four traditional recommender agents and one LLM reranker agent. On MovieLens-1M, the full quality oracle has substantial headroom (HR@10 = 0.584), confirming that useful cross-agent signal exists. Under a leakage-free 5-fold out-of-fold protocol, however, hard selection remains below BM25 (0.223 vs. 0.254), and selective LLM escalation does not improve it. The same protocol yields a different outcome for learned aggregation: its cheap-only variant matches BM25 in HR and has a higher NDCG point estimate (0.123 vs. 0.114), while gated all-agent aggregation reaches HR@10 = 0.295 with 70.2\% LLM calls. The resulting lesson is not that routing is solved, but that request-level selection of one complete agent list is too coarse for this sparse fixed-candidate setting; item-level aggregation is the more promising action space.

---


### 77. [A Hybrid Quantum-Chaos Theory Approach to Image Encryption Using Reservoir Computing](https://arxiv.org/abs/2607.09923)

**<font color=#1a73e8>作者：</font>** Naheen Mohd. Kadir  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This research presents a novel hybrid image encryption system that combines quantum cryptography, chaos theory and reservoir computing to address the limitations of conventional encryption methods. With the rapid advancements in quantum computing, traditional systems like RSA, DHKE (related to prime number factorization) are vulnerable to quantum attacks i.e. Shor's algorithm, Grover's algorithm. In response, this study proposes a hybrid solution that uses quantum cryptographic protocols, particularly the E91 protocol, to generate secure, eavesdrop-proof keys through quantum entanglement. The integration of chaos theory, specifically the Lorenz hyper-chaotic system, enhances the encryption system by adding unpredictability and sensitivity to initial conditions, making it more resistant to both classical and quantum-based attacks. Reservoir computing is used to improve computational efficiency, enabling faster and more effective encryption and decryption processes. The system achieved encryption times as low as 0.0296s and decryption times as low as 0.0164s for 128x128 images, with MAE reduced for 300-600 node networks, and NPCR and UACI above 99.6% and 0.49, respectively, across various image sizes and configurations. By combining quantum cryptography, chaos theory and reservoir computing, this approach offers both enhanced security and practical feasibility for image encryption in the age of quantum computing.

---


### 78. [Banshee: Target Switch Attacks on Gimbal-Stabilized Visual Tracking Systems via Acoustic Injection](https://arxiv.org/abs/2607.09930)

**<font color=#1a73e8>作者：</font>** Jiarui Li, Joseph Brewington, Qingzhao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gimbal-stabilized visual tracking is critical for modern autonomous systems such as Unmanned Aerial Vehicles (UAVs). While prior work shows acoustic signals can disturb gimbal internals, the impact of such attacks on real-world applications like UAV tracking and following remains underexplored. Existing demonstrations largely overlook practical challenges for real-world attacks, such as object-motion uncertainty and runtime latency. To bridge this gap, we present Banshee, the first physically realizable attack that induces target switching in UAV visual tracking systems by exploiting acoustic vulnerabilities in gimbal-camera systems. Banshee generates carefully crafted acoustic waveforms that induce optimized adversarial gimbal oscillations, causing directionally biased camera-view drifts that break inter-frame target associations. Consequently, the onboard tracker is driven to switch from the original target to an attacker-selected object with high probability, with occasional target loss. Banshee achieves a 93.6% success rate in simulation across two commercial gimbal systems and five trackers. Real-world benchtop and in-flight black-box attacks against a commercial drone across varied scenarios show an overall 95.5% attack success rate. Our results reveal a practical cross-domain vulnerability between acoustics and vision, highlighting the need for robust designs of gimbal systems and applications. Our code is available at: this https URL.

---


### 79. ["Code Is Cheap. Show Me the Talk.": Lessons from Teaching and Managing AI Coding Tool Usage in a Visualization Course](https://arxiv.org/abs/2607.09938)

**<font color=#1a73e8>作者：</font>** Zhongzheng Xu, Taehyun Yang, Fumeng Yang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative Artificial Intelligence (GenAI) coding tools are transforming visualization education. They can assist with implementation and design, but they can also let students bypass intended learning trajectories. In this paper, we share our retrospective experience managing and teaching AI use in an upper-level visualization course. We implemented prompt injections, asked oral checkout questions, and taught two AI coding labs. Prior to our coding labs, at least half of the students had already used AI tools in their assignments. In both AI coding labs, refinement accounted for about half of students' prompting logs, and explanation was almost absent. In the lab where AI coding was optional, 44 of 78 (56.4%) submissions preferred the scaffolded instructions over designing their own prompts. Students' final projects were more polished than in our previous offering, but also more visually homogeneous. Our reflections point to the need for clearer AI use boundaries and instruction on prompting, and for teaching students to question generic AI designs and adapt them to their data and story.

---


### 80. [Optimizing ARDL Models for Retail Sales Forecasting and Fair Pricing](https://arxiv.org/abs/2607.09956)

**<font color=#1a73e8>作者：</font>** Sujay Uday Rittikar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pricing food products to balance profitability with consumer welfare is a central challenge for retailers. Dynamic pricing is widely used to maximize revenue, yet most pricing models optimize business objectives while overlooking consumer fairness. This paper studies the risk of consumer exploitation under dynamic food pricing in Canada and proposes a methodology that embeds fairness constraints directly into retail sales forecasting. We model total retail trade sales with a log--log Autoregressive Distributed Lag (ARDL) specification, in which the coefficient on a product price is a sales elasticity, and pose the pricing problem as maximizing forecast sales subject to price bounds anchored to the Consumer Price Index (CPI). We solve this problem with both Linear Programming (LP) and Simulated Annealing (SA), under single-product and multi-product configurations. A key finding is that the fitted nominal elasticities are positive. As a result, an unconstrained sales-maximizer would push every price to its upper bound, and the CPI ceiling is the safeguard that prevents this. Simulated Annealing instead settles on conservative, interior prices that lower consumer cost while still meeting the sales target. We benchmark forecast accuracy against naive, seasonal-naive, ARIMA, and SARIMA baselines, and a CPI-deflated re-specification shows that the positive nominal elasticities are largely an inflation-driven artifact. The result is a transparent, fairness-aware pricing framework.

---


### 81. [Workload-Driven Optimization for On-Device Real-Time Subtitle Translation](https://arxiv.org/abs/2607.09957)

**<font color=#1a73e8>作者：</font>** Tsz-To Wong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This report studies on-device English-to-Traditional-Chinese subtitle translation for Taiwan under short inputs, short outputs, batch-size-one inference, low latency, and privacy constraints. These conditions limit the value of optimizations designed for long-context or high-throughput language-model serving.
Starting from LMT-60-0.6B, preliminary profiling suggests that vocabulary projection becomes a more important decode-time cost after GGUF quantization reduces the relative cost of Transformer blocks. We replace the original 151k-token vocabulary with a 64k-token subtitle-domain tokenizer, migrate the embedding space, and adapt the model through embedding calibration followed by full supervised fine-tuning.
On a fixed 500-example subset of the OpenSubtitles2024 test set, the LocalSubs achieves a 59.2% tie-excluded win rate against Google Translate under GPT-4o pairwise judging. Performance is strongest on short cues and declines as cue length increases. Preliminary Apple M2 Metal measurements on a 64k-vocabulary model show a 1.63$\times$ speedup over a 151k-vocabulary profiling baseline. The raw benchmark configuration is incomplete, so the latency result is treated as preliminary.

---


### 82. [Learning in Curved Weight Space:Exponential-Linear Weight Reparameterization for Improved Optimization](https://arxiv.org/abs/2607.09967)

**<font color=#1a73e8>作者：</font>** Ethan Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many neural networks operations have a multiplicative nature rather than additive: halving or doubling a norm are analogous relatively but require unequal optimization distances when taking linear steps. Adaptive optimizers such as Adam normalize updates per coordinate, but update steps remain additive; weights with very different magnitudes receive similarly sized absolute changes, producing very different relative perturbations. We introduce \textbf{\method} (\textbf{\methodshort}), a weight reparameterization for neural networks that combines a sign-aware symmetric-exponential pathway with an identity-like linear pathway. The symmetric-exponential pathway is near-linear for small raw weights but increasingly curved at larger magnitudes. Additive updates in logarithmic space map to magnitude-proportional changes in effective weight space. The linear pathway provides a direct route through the transform that we hypothesize stabilizes optimization, while learnable scale, curvature, and offset parameters control balance between pathways and the curvature of the exponential pathway. These components create a curved parameter-space geometry that empirically improves speed of loss descent over standard linear parameterization. We also identify a useful \emph{mismatched initialization}: raw weights are chosen so a symmetric version of the transform matches Xavier statistics, but training uses an asymmetric forward transform that leaves positive weights at full strength while making negative weights smaller in magnitude; in small-model ablations, this improves early optimization and may act as a form of symmetry breaking. We train transformers on OpenWebText over nine width$\times$depth configurations, \methodshort reaches matched validation loss in 1.32--1.49$\times$ fewer training steps, with the largest widths seeing the biggest gains.

---


### 83. [TopoExplore: Topological Discrimination for Archive-Based Exploration](https://arxiv.org/abs/2607.09971)

**<font color=#1a73e8>作者：</font>** Jason Carlson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Archive-based exploration methods such as Go-Explore select which visited state to return to using visitation rarity, and frontier methods return to the boundary of the unknown; neither asks whether the unexplored region behind a boundary is enterable at all. Exploration is not just about finding reward - it is about collecting a structurally complete experience for downstream learning and planning. We introduce TopoExplore, which augments Go-Explore cell selection with a periodic topological pass: enclosed unexplored regions (voids) of the visited-set occupancy grid are detected by flood fill (the H1 classes of its cubical complex), and a decaying selection bonus is placed only on their strict entrances (gap or door cells), so sealed regions are never targeted and entered regions retire. On a controlled 18-environment MiniGrid suite (15 seeds, frozen hyperparameters) TopoExplore attains a 1.52x geometric-mean speedup in median steps-to-first-entry over its exact Go-Explore ablation, versus 1.37x for a frontier baseline; frontier exploration degrades when sealed decoy structure appears (0.83-1.48x on decoy environments vs. 1.65-2.11x for TopoExplore), while TopoExplore holds its largest win on hard multi-interaction doors (10.9x). We report an honest negative on Montezuma's Revenge - without wall knowledge, unreachable occupancy artifacts capture the bonus and performance degrades as it grows, isolating the wall-aware entrance test as the load-bearing component - and a preliminary positive on HM3D scanned buildings, where the speedup over Go-Explore tracks scene difficulty (r=0.69) even as frontier selection dominates blanket coverage. The evidence supports a deliberately scoped claim: topology-aware selection pays off where enclosed structure must be discriminated, and remains competitive at open coverage, where frontier methods are strongest, despite not being tuned for that regime.

---


### 84. [UniPose9D: Universal Category-Agnostic Object Pose Estimation](https://arxiv.org/abs/2607.09985)

**<font color=#1a73e8>作者：</font>** Yang You, Yi Du, Cole Harrison 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object pose estimation is a fundamental problem in 3D vision. Although recent state-of-the-art approaches achieve strong performance, they often overfit to existing benchmarks and exhibit limited generalization to novel categories and unseen scenes. We propose UniPose9D, a category-agnostic foundation model for 9D object pose estimation: given an instance mask/ROI and either an RGB-D observation or an RGB image with predicted depth, the model estimates rotation, translation, and metric size without category labels, CAD models, mean-shape priors, or reference views. Specifically, UniPose9D samples point pairs from the observed object geometry and uses DINOv2 and PointNet features to predict NOCS coordinates for each pair. To improve accuracy, we introduce a point-pair-based RANSAC N-hop Kabsch--Umeyama algorithm with an adaptive threshold. We further employ flow matching to address symmetric ambiguities and construct a large-scale training set by curating and aligning pose annotations from existing public datasets. Experiments across six datasets show that a single unified model can match or surpass specialist methods while generalizing to unseen objects and in-the-wild scenarios. Our code and model are available on this https URL.

---


### 85. [Robust, Scalable Detection of Text Containment in Large Web-Crawled Corpora](https://arxiv.org/abs/2607.10020)

**<font color=#1a73e8>作者：</font>** Lars Henry Berge Olsen, Pierre Lison, Martin Jullum 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present FindMyText, an open-source Python package designed to efficiently assess whether a given text appears, in part or in full, within a text corpus. The tool builds on prior techniques for document fingerprinting, but extends them with a novel mechanism to explicitly capture sequences of matching fingerprints. By identifying such chains, the tool can more reliably detect near-verbatim copies of a given text rather than mere textual similarities. This makes FindMyText particularly suited for verifying the presence of copyrighted material in a corpus. Leveraging a distributed, disk-based indexing framework, the system scales to large web-crawled datasets. Using a new benchmark for evaluating text containment methods, we show that FindMyText outperforms alternative approaches across three datasets (ArXiv papers, Wikipedia, and generic web content).

---


### 86. [A Symbolic Neural CPU for Quantization-Simulated Writeback and Interpretable Program Execution](https://arxiv.org/abs/2607.10021)

**<font color=#1a73e8>作者：</font>** Jose Luis Lima de Jesus Silva  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural networks can learn algorithmic input-output mappings, but trusting a learned executor requires more than a correct final answer because the state transitions that produce it are usually hidden. To make those transitions visible, we introduce a trace-supervised symbolic neural CPU, a factorized learned execution architecture that combines recurrent control, an explicit operation router over a fixed differentiable arithmetic-logic unit bank, destination-masked register writeback, complete trajectory supervision and matched fixed-point replay. The model exposes the selected operation, source and destination registers, register trajectory, memory signals and writeback semantics at every step. On the principal 16-wide benchmark, the non-quantized executor reproduces reference execution exactly, while the eight-bit quantization-simulated executor preserves the symbolic operation path through programs of 1,000 instructions. When the same execution is evaluated against a matched fixed-point replay, the residual numerical drift disappears, showing that it comes from a mismatch between continuous and low-precision reference semantics rather than from execution failure. We compare recurrent, Transformer, temporal-convolution, temporal graph-inspired and state-space controllers, and the ablations show that operation-gate supervision is necessary for an inspectable execution path. Hidden-opcode memory-pressure tasks expose the remaining limits in delayed state use and temporal binding. We also extend the interface with ValueMemory, hybrid adaptive leaky integrate-and-fire controllers, candidate-constrained symbolic control trained through behaviour cloning and actor-critic reinforcement learning, and an RV32I base-integer semantic bridge. Together, these results establish a trace-verifiable framework for interpretable, low-precision and controllable neural execution.

---


### 87. [SafeGuard: A Lightweight Client-Server Architecture for Real-Time Endpoint Threat Detection and Response](https://arxiv.org/abs/2607.10027)

**<font color=#1a73e8>作者：</font>** Gideon Francis Oghie, DivineDavid Shittu Abolanle  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Endpoint devices remain a primary target for cyberattacks, yet commercial Endpoint Detection and Response (EDR) platforms are often too costly and operationally complex for small and resource-constrained organizations. This paper presents SafeGuard, a lightweight three-tier client-server architecture for real-time endpoint monitoring, threat reporting, and administrative response. The system comprises a Flutter-based endpoint agent extended with Kotlin for Android system access, a this http URL central server that authenticates devices and coordinates secure communication, and an administrative dashboard for live monitoring and remote actions such as device locking, application removal, and warning notification dispatch. Threat detection is implemented through signature-based comparison against a maintained threat database, prioritizing low computational overhead, explainability, and ease of deployment over generalized anomaly detection. Communication security is achieved using WebSocket over TLS (WSS), JSON Web Token (JWT) authentication, and HMAC-based message integrity verification. The system was evaluated through unit, integration, system, load, and preliminary security testing. Under a simulated deployment of 50 concurrent endpoints, average command-dispatch latency was approximately 1.5 seconds and remained below 2 seconds under load. Invalid authentication tokens were rejected, while manual SQL injection and replay attempts were unsuccessful in the evaluated scenarios. The results demonstrate that an open-source technology stack can provide real-time endpoint visibility and coordinated administrative response without commercial licensing costs. The contribution is architectural and empirical rather than algorithmic, with current limitations including reliance on static threat signatures, Android-focused implementation, and controlled-environment evaluation.

---


### 88. [FlashTrie: A GPU-Accelerated Constrained Beam Search for Generative Retrieval](https://arxiv.org/abs/2607.10044)

**<font color=#1a73e8>作者：</font>** Dakshitha Anandakumar, Anurag Mukkara, Wenxiang Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constrained decoding is essential in generative retrieval, where document identifiers generated directly from a query must exactly match a predefined library of valid IDs. At scale, decoding is often constrained using a trie with beam search but most implementations run on CPU. Limited parallelism then makes trie traversal and candidate validation a serving bottleneck as beam width grows.
We present FlashTrie, which addresses this limitation by optimizing constrained beam search on GPUs. It introduces an integer-aware succinct trie layout that uses bit compression to reduce memory footprint while keeping the full index in GPU high-bandwidth memory reducing memory stalls, and a cooperative CUDA kernel that performs beam expansion, validation, and pruning entirely on-device without per-step host orchestration. It further replaces CPU-style irregular lookup and heap maintenance with GPU-aware parallel primitives, improving warp utilization and reducing divergence.
Together, these designs significantly reduce decoding latency and increase throughput while preserving retrieval quality. On a library of 800M keywords with beam widths up to 1000, FlashTrie reduces trie-search latency to under 3 ms, achieving up to 24x speedup over a highly optimized multi-threaded CPU baseline. These improvements enable FlashTrie to scale beam sizes by up to 5x in latency-critical applications such as sponsored search. In a large-scale online A/B experiment on a popular commercial search engine, it delivers a statistically significant +0.71% revenue lift, enabling real-time constrained decoding at a scale previously feasible only offline. The FlashTrie code will be publicly released after the review process.

---


### 89. [SyncSpace: Layout-Conditioned 3D Gaussian Splatting for Space Reskinning in Mixed Reality](https://arxiv.org/abs/2607.10050)

**<font color=#1a73e8>作者：</font>** Qinchuan Zhang, Weibo Xu, Yunge Wen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present SyncSpace, a system that achieves both spatial alignment and visual consistency between a generated 3DGS world and physical space. We first scan the space via depth sensing to extract 3D bounding boxes, which we render into a layout-only panorama and feed as a geometric prior to a generative world model, producing a Gaussian splat scene in which objects are re-semantized to fit a target style without per-object control. We then align the generated scene to physical space with a coarse-to-fine registration algorithm, refined manually via pinch gestures when automatic registration does not converge. We demonstrate a hand-tracked engulfment interaction in which the virtual world rises to replace the physical space, and show a single space reskinned into multiple stylistically distinct worlds with its layout preserved.

---


### 90. [Federated Cybersecurity Testbed as a Service (FCTaaS): A framework to federate cybersecurity testbeds](https://arxiv.org/abs/2607.10061)

**<font color=#1a73e8>作者：</font>** Josh Dean, Yu-Zheng Lin, John Paul Martin Encinas 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Rapid technological change is reshaping society through emerging domains such as autonomous vehicles and smart manufacturing, creating new research challenges in system design, operation, security, and training. Researchers often rely on testbeds to reproduce experimental scenarios, collect and analyze data, observe system behavior, and evaluate proposed solutions. However, the fast pace of innovation makes it difficult and costly for individual testbeds to remain representative of state-of-the-art systems, as doing so requires frequent upgrades and new capabilities. Moreover, access to specialized testbeds is often limited to a small group of researchers, leaving valuable infrastructure underutilized during its operational lifetime. This paper presents FCTaaS, a Federated Cybersecurity Testbed as a Service framework that enables heterogeneous cybersecurity testbeds to participate in a single experiment across geographical boundaries. By connecting independently managed testbeds through a Virtual Private Network (VPN), FCTaaS supports remote testbed discovery, experiment design, and coordinated experimentation. We evaluate FCTaaS across three case studies involving denial-of-service scenarios on smart infrastructure and intrusion detection and prevention workflows using a Suricata-based IDS/IPS testbed. The results show that FCTaaS enables effective cross-testbed experimentation while preserving visibility into attack traffic, IDS alerts, and detection-system resource stress. Even under resource-intensive attack scenarios, FCTaaS achieves limiting network utilization of 49%, introduces only 1% overhead, and supports latency ranging from 5.63 ms between local nodes to 147 ms between geographically dispersed nodes.

---


### 91. [Conservation Laws for Diffusion Models](https://arxiv.org/abs/2607.10067)

**<font color=#1a73e8>作者：</font>** Ziv Aharoni, Henry D. Pfister  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While autoregressive models optimize the exact data likelihood via the chain rule, diffusion models are typically trained with denoising objectives. We develop conservation laws based on generalized extrinsic information transfer (GEXIT) functions for a broad class of memoryless noise processes, showing that the data--model cross-entropy (CE) can be characterized exactly as an integral of local information-theoretic derivatives along the noise path. This yields a unified characterization of the likelihood for discrete and continuous diffusion, with the Gaussian case reducing to the well-known mutual information--minimum mean-square error (I-MMSE) relationship. An immediate implication is a locality property: one can compute the information-theoretic derivatives using only the marginal posteriors along the noise path. As a result, training reduces to learning the marginal posteriors by minimizing the negative log-likelihood. While the conservation law implies that the entropy does not depend on the noise path, finite-capacity denoisers approximate the posteriors with varying accuracy across noise types, leading to differences in performance. We validate these predictions on synthetic Markov sources and standard benchmarks, including text8 and CIFAR-10.

---


### 92. [Error Aware Distribution Prediction for Lightweight Implicit Neural Representations](https://arxiv.org/abs/2607.10068)

**<font color=#1a73e8>作者：</font>** Zhimin Li, Jake D. Balla, Joshua A. Levine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) offer compact encoding of volumes, but as lossy approximators, inevitably have prediction errors. We consider INRs that can simultaneously encode relative error scales by predicting distributions using tools from uncertainty estimation. Typically, uncertainty estimation relies on computationally expensive approaches or on predefined parametric assumptions about the predictive distribution (e.g., Gaussian). In this study, we propose a lightweight method that reformulates regression-based INR training as a classification task by discretizing continuous targets into bins, enabling flexible distribution modeling to capture complex multimodal behaviors. We analyze the trade-off between regression and classification for INR training and demonstrate that the classification setting tends to achieve high reconstruction quality and competitive error awareness through uncertainty estimation, compared to regression-based approaches.

---


### 93. [From ambiguous utterances to governed reuse classes: canonicalization, quotient invariance, and conditional decidability](https://arxiv.org/abs/2607.10069)

**<font color=#1a73e8>作者：</font>** Cosimo Spera, Ray Garcia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semantic caching defines answer reuse on embedding similarity: two utterances share a stored answer when a similarity score clears a threshold, with no notion of authorization, versioning, or of what makes two demands the same. This note changes the object on which reuse is defined: in a governed domain, reuse should operate on a mathematically characterized quotient of resolved conversational demands, not on a similarity heuristic. Three independently defined relations on resolved utterances -- reading identity, resolution identity, and reuse identity -- form a refinement chain, strict under realized nondegeneracy conditions checkable on deployment logs; the pipeline's outputs are invariant along the chain, and reuse identity is exactly the kernel of the resolution map into the governed answer partition, so the reuse quotient is the utterance-side object that partition induces, not a relabeling of it. Reuse identity licenses the governed query key and its certified answer space; reuse of a particular answer requires resolution identity or an applicability certificate. The supporting layer is stated at exactly the strength proved: exact-denotation normal forms; join aggregation as a design operator, with closure-stable cells characterizing no-escape; total computability of the full pipeline relative to an untrusted proposal layer; policy admissibility for arbitrary proposers -- and provably not factual grounding or intent fidelity; and elicitation terminating after finitely many informative replies, sound under target consistency.

---


### 94. [FlashBEV: Fast and Memory-Efficient Exact BEV Transformation with IO-Awareness](https://arxiv.org/abs/2607.10071)

**<font color=#1a73e8>作者：</font>** Shunsuke Yokokawa, Hironori Kasahara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bird's-eye-view (BEV) perception is a core component of camera-based 3D understanding in autonomous driving, where view transformation (VT) maps multi-camera image features into a unified BEV representation. Sampling-based view transformation (Sampling-VT) is attractive because it supports dense and continuous BEV aggregation for high-resolution and long-range perception. Its deployment bottleneck, however, is systems-level: standard tensorized implementations of Sampling-VT -- which we refer to as Tensorized Sampling-VT -- explicitly materialize large height-dependent intermediate tensors, causing memory and latency costs that scale poorly with vertical resolution and the number of cameras. We revisit Tensorized Sampling-VT from an operator-execution perspective and show that it follows a gather-reduction pattern: each BEV query independently accumulates contributions across cameras and height bins, enabling thread-local accumulation with on-the-fly recomputation that eliminates the need to materialize height- and camera-dependent intermediates. Based on this insight, we propose FlashBEV, a fully fused and IO-aware execution strategy mathematically equivalent to Tensorized Sampling-VT (same operator output) while substantially reducing global memory traffic and kernel-launch overhead. Experiments show that FlashBEV achieves more than an order of magnitude lower peak GPU memory and significant inference-latency speedups, with memory effectively independent of the number of height bins, reducing the operator's peak memory to O(BCXY) (output only). This unlocks higher BEV range/resolution and vertical discretization within fixed deployment budgets on memory-constrained devices. Our contribution is an execution redesign -- same math, different execution -- that removes a key scalability barrier for deployment-ready Sampling-VT. Code available at this https URL

---


### 95. [Distance-Preserving Embeddings in Inhomogeneous Random Graphs](https://arxiv.org/abs/2607.10074)

**<font color=#1a73e8>作者：</font>** My Le, Luana Ruiz, Souvik Dhara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph machine learning provides powerful tools for understanding complex networks and learning meaningful node representations. A central challenge, however, is designing embeddings with minimal distortion of both local and global functionals, such as shortest path lengths. Prior distortion guarantees for distance-preserving embeddings are worst-case in nature, producing overly pessimistic bounds that fail to capture the structure of typical large-scale networks. To address this, we analyze shortest-path approximation via landmark-based embeddings on inhomogeneous random graphs, a general model with type-dependent edge probabilities. By retaining shortest paths to a small set of reference nodes called landmarks, landmark-based methods effectively function as virtual graph spanners, where structural heterogeneity and controlled neighborhood expansion modeled via multi-type branching processes enable significantly tighter dimension-distortion trade-offs than classical worst-case bounds. We extend these guarantees to global, component-wide averages and unify the analysis across finite-type and continuous latent spaces through a novel metric sandwiching framework, establishing universal distortion bounds for general $L^2$ kernel models, including heavy-tailed and power-law networks. Finally, we introduce a GNN-augmented variant that replaces rigid, computationally expensive exact shortest-path queries with flexible, structure-aware neural surrogates. By leveraging the inherent alignment between graph neural message-passing and the dynamic programming principles of shortest-path algorithms, our approach demonstrates that models trained on small-scale random graphs learn to extract universal distance-preserving features, achieving robust generalization to large-scale, real-world networks that match or exceed the fidelity of classical, exact landmark-based embeddings.

---


### 96. [TabLoRA: Parameter-Efficient Low-Rank Ensemble Learning for Large-Scale Tabular Data](https://arxiv.org/abs/2607.10077)

**<font color=#1a73e8>作者：</font>** Jiaqi Luo, Shixin Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular learning is still dominated by gradient-boosted decision trees (GBDTs), while recent deep learning approaches have become increasingly competitive. However, applying deep tabular models to large-scale datasets remains challenging, as large sample sizes, high feature dimensionality, or many target classes can introduce substantial computational cost. We propose TabLoRA, a parameter-efficient trainable neural ensemble for large-scale tabular learning. Instead of using fully independent ensemble backbones, TabLoRA shares a common backbone across predictors and introduces predictor-specific low-rank adaptations, enabling ensemble-style prediction without full parameter duplication. Across benchmarks, TabLoRA achieves a favorable balance between predictive performance and practical efficiency compared with GBDT methods and recent deep learning baselines under the same resource constraints. Memory analysis and ablation studies further show that the proposed design improves the feasibility of neural ensemble learning while preserving much of the benefit of full ensembles.

---


### 97. [Label-Free Target-Domain Adaptation for Unconstrained Event-Image Feature Matching via Dual-Stage Distillation](https://arxiv.org/abs/2607.10082)

**<font color=#1a73e8>作者：</font>** Zhonghua Yi, Hao Shi, Qi Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building pixel-level correspondence between event and image data is a fundamental task for multi-sensor systems. However, existing cross-modal matching methods are largely restricted by their reliance on either matching labels or strictly aligned hardware, which limits them to unlabeled and unconstrained real-world scenarios where neither matching ground truth nor prior sensor relationships are available. To address this, we propose a novel two-stage training paradigm. First, we leverage large-scale data to perform label-agnostic distillation pretraining, upgrading optimization objectives with distribution-based and contrastive losses to learn highly generalizable representations. Second, to tackle unlabeled and unconstrained downstream data, we introduce an epipolar-guided self-distillation framework. By utilizing consistency verification to isolate robust matches and incorporating geometric confidence derived from an external epipolar prior, our model can effectively self-evolve directly on target domains without any supervision. Furthermore, we introduce a rigorous cross-modal evaluation benchmark based on TUM-VIE, featuring physically separated cameras with distinct intrinsic parameters and resolutions. Extensive experiments demonstrate that our proposed method achieves state-of-the-art performance on both MVSEC and TUM-VIE pose estimation tasks. The source code and benchmark will be made publicly available at this https URL.

---


### 98. [CVKD-UDA: Cross-View Knowledge Distillation for 3D Unsupervised Domain Adaptive Segmentation](https://arxiv.org/abs/2607.10087)

**<font color=#1a73e8>作者：</font>** Zhimin Yuan, Ming Cheng, Shangshu Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D unsupervised domain adaptive (UDA) segmentation mitigates the high cost of manual annotations of the new domain data. Self-training has emerged as the dominant approach in this area, where its success heavily depends on a well-initialized warm-up model to generate reliable pseudo labels. However, existing methods often depend on source supervision or output-level adversarial alignment to obtain the warm-up model, which suffer from limited generalization and training instability due to the large domain gap between domains. Constructing domain-similar representations is an effective way to bridge this gap. In this work, we propose CVKD-UDA, which revisits voxel size as a core design factor to construct domain-similar representations and leverages cross-view complementary cues to balance transferability and discriminability of the warm-up model. First, we generate two complementary views by varying voxel sizes and introduce a cross-view knowledge distillation (CVKD) to enhance generalization and target perception of the model. Second, to balance transferability and discriminability, we design a lightweight Decouple-Adapter and an auxiliary imitation classifier to decouple cross-view knowledge transfer. Extensive experiments on two benchmarks demonstrate that CVKD-UDA effectively improves the performance of self-training methods and provides a new perspective for 3D UDA segmentation. Our code will be available at GitHub.

---


### 99. [EMBRACE: A Multi-task Framework for Comprehensive Quality Assessment in Cleavage-stage Embryo](https://arxiv.org/abs/2607.10093)

**<font color=#1a73e8>作者：</font>** Anwar Hussain Sofi, Jung-Hua Wang, Ming-Jer Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cleavage-stage embryo assessment in in vitro fertilization requires the integrated interpretation of cytoplasmic fragmentation, developmental stage, and blastomere symmetry. However, conventional visual assessment is affected by observer variability, particularly when fragmented regions are small, irregular, or low contrast. This study presents EMBRACE, a multi-task deep learning framework for jointly performing cytoplasmic-fragmentation segmentation, t2/t4 developmental-stage classification, and blastomere-symmetry grading from static cleavage-stage embryo microscopy images. EMBRACE combines a shared ResNet-50 backbone, a concatenation-based multi-scale feature-fusion (C-MSFF) module, a U-Net-style segmentation decoder, and two task-specific classification heads. After predefined inclusion and exclusion criteria, 9,137 annotated embryo images were divided into 7,309 training, 914 validation, and 914 held-out test images. On the held-out test set, EMBRACE achieved a Dice coefficient of 0.781 and an intersection over union of 0.677 for fragmentation segmentation. Developmental-stage classification achieved an accuracy of 0.995, macro-F1 of 0.994, and AUC of 1.000. Blastomere-symmetry grading achieved a balanced accuracy of 0.901, macro-F1 of 0.907, and quadratic weighted kappa of 0.859. These findings support the feasibility of combining spatially inspectable fragmentation localization with embryo-level morphology assessment in a single framework. External and prospective validation is required before clinical deployment.

---


### 100. [LFD: Enabling Real-World Lensless Face Recognition with a Large-Scale Dataset](https://arxiv.org/abs/2607.10094)

**<font color=#1a73e8>作者：</font>** Junho Kim, Salman S. Khan, Sara Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition is a ubiquitously used computer vision task that has a wide range of applications ranging from everyday smartphone biometrics to high-stakes security systems. Most face recognition systems rely on traditional cameras, which often suffer from limitations such as bulky form factors, high costs, and limited privacy protection. To address these limitations, lensless cameras have emerged as an alternative. Lensless cameras use thin optical encoders, enabling smaller size, lower cost, and greater design flexibility. These cameras are typically paired with reconstruction algorithms that convert raw captures into recognizable images. However, reconstructed images often contain artifacts, and the reconstruction methods struggle to generalize well to real-world conditions. Furthermore, existing face datasets do not account for the artifacts present in lensless images. To address this issue, we introduce the Lensless Face Dataset (LFD). LFD comprises 21,080 lensless raw measurements, reconstructions, and standard images of faces captured under diverse lighting, angle, and distance. Our key contributions are: (1) Real-world lensless face data: LFD focuses on capturing a diverse face dataset with varying levels of artifacts introduced under different environments; (2) In-the-wild captures: 4,976 images are captured in outdoor settings with varying intensities of natural light and different background patterns; (3) Multiple lensless devices: LFD includes face images collected from three different types of lensless cameras, each with a unique optical encoder. We use this hardware diversity to demonstrate generalization across different lensless cameras. Through comprehensive evaluations and analysis, we show that LFD effectively captures shared features and artifacts across different lensless imaging devices, making it a valuable dataset for advancing lensless face recognition.

---


> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-420](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
