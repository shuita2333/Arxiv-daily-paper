# 📦 其他研究 | 2026年08月31日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

---

### 51. [Shared Actors Need Not Share Critics: Effects of Value Mismatch in Parallel Reinforcement Learning](https://arxiv.org/abs/2608.26481)

**<font color=#1a73e8>作者：</font>** Zhenya Liu, Yang Meng, Zhuokai Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a single policy is trained in parallel across multiple environments of the same task, such as procedurally generated levels, randomized dynamics, or curricula, implementations commonly use one critic across all sampled environments. Yet different environments can assign different expected returns to the same input visible to the critic. A critic without environment information must then reconcile distinct value targets, systematically shifting the sampled advantages within individual environments. Using illustrative bandit models with multiple environments and a common optimal arm, we characterize how this value mismatch redistributes sampled policy updates, reinforcing unhelpful actions while attenuating or even reversing useful ones. The oracle processes using no baseline, the shared value, or the value specific to the sampled environment have the same mean logit update at a fixed policy and converge to the same optimal policy, yet their realized learning paths can differ sharply. The analysis motivates a minimal intervention: give only a logged environment index to the critic so that it can separate the value targets. Controlled CartPole and MuJoCo experiments expose the predicted shifted values, advantages, and performance gaps. In the more complex BipedalWalker and Procgen settings, the same intervention yields more stable learning and higher returns. Across all $16$ Procgen games, the multihead conditional critic improves aggregate normalized return on $600$ unseen levels per game by $40.8\%$. In conclusion, the theory identifies value mismatch as a direct mechanism through which critic sharing can degrade stochastic learning dynamics, not captured by scalar estimator variance alone, and the experiments show that conditioning on an index is broadly effective in parallel reinforcement learning.

---


### 52. [Learning Woody Clearing With Loss Alignment for Zero-Shot Regrowth and Woody Segmentation](https://arxiv.org/abs/2608.26489)

**<font color=#1a73e8>作者：</font>** Kal Backman, Jared Wood, Adam Roff  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting woody clearing is vital for managing biodiversity. Deep learning models can detect change in woody vegetation from bitemporal remote sensing imagery, however generated products may not meet end-user specifications due to unaligned loss definitions. Further limitations of deep learning models are the reliance on large datasets which can be difficult to attain for spatially rare and ambiguous events such as regrowth detection. In this work we train a model to detect woody change using bitemporal Sentinel-2 imagery consisting of 7 years' worth of annual imagery across the state of New South Wales, Australia. To align the objective of the model with end-user metrics, we introduce the loss scaling coefficient $\alpha$ which transforms the objective to optimize for specific $F_{\beta}$ scores. Introducing $\alpha$ was found to increase precision by 1.85x or recall by 1.12x. We propose input imagery augmentation and generation techniques that allow the woody change detection model to zero-shot transfer to regrowth and woody segmentation tasks. For woody segmentation, image generation techniques using activation maximization with low $\alpha$ values for stability and image generation techniques derived from handcrafted features utilizing a mosaic of clearing patches and artificial trees for contextual grounding were found to outperform prior woody segmentation works of the study area, reducing the overall error by up to 18.2%. For zero-shot woody regrowth, creating pseudo-post and prior images resulted in the model achieving an F1 score of 0.845, creating a foundation for future regrowth detection work.

---


### 53. [Bayesian methods and Markov chain Monte Carlo algorithms for curve reconstruction and point cloud data analysis](https://arxiv.org/abs/2608.26490)

**<font color=#1a73e8>作者：</font>** Asir Intesar Tushar, Ioannis Sgouralis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Point-cloud data routinely captured by modern imaging and sensor technologies provide detailed geometric descriptions of objects and environments, but their analysis is hindered by large data volumes, localization noise, and missing information. In addition, existing point-cloud reconstruction pipelines typically return a single best-fit structure without uncertainty quantification. We introduce a fully Bayesian framework for representing point-cloud data and reconstructing closed curves, in which observed points are modeled as noisy perturbations of latent locations constrained to lie on the underlying curve that is regularized by a non-parametric prior. Posterior inference in our framework is carried out using a series of Markov chain Monte Carlo samplers tailored to point-cloud characteristics. Numerical experiments, including synthetic examples and real-world LiDAR datasets, show accurate reconstructions and quantified uncertainty over the recovered curves.

---


### 54. [A Unified Framework for Fair and Personalized Decentralized Learning under Communication Constraints](https://arxiv.org/abs/2608.26493)

**<font color=#1a73e8>作者：</font>** Krishnendu S. Tharakan, Carlo Fischione  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized learning systems aim to collaboratively train models across multiple clients without relying on a central coordinator. While decentralization improves scalability, privacy, and robustness, it also exacerbates three fundamental challenges: statistical heterogeneity across clients, fairness in client-level performance, and stringent communication constraints. This raises a natural question: \emph{how fair can decentralized learning be under limited communication?} We address this question by presenting a unified framework for decentralized learning under communication constraints, bringing together graph-based personalization, agnostic fairness, and compressed event-triggered communication. Specifically, we propose a new algorithm DMFL-SQ, a decentralized multi-task learning algorithm that couples personalized model training over a communication graph with an agnostic mixture fairness objective, while reducing communication through sparsification, quantization, and event-triggered synchronization. We establish convergence guarantees for general non-convex objectives and show that DMFL-SQ achieves an $\mathcal{O}(T^{-1/2})$ rate in expected squared Moreau-envelope stationarity despite sparse, quantized, and event-triggered communication. We further derive PAC-Bayes generalization guarantees for the fairness-aware mixture objective. Experiments on CIFAR-10 and the real heterogeneous MUSMET EEG dataset demonstrate that DMFL-SQ substantially reduces communication while maintaining predictive performance and improving fairness across clients. Together, our theoretical and empirical results show that personalization, fairness, and communication efficiency can be jointly achieved in decentralized learning while preserving the dominant convergence rate.

---


### 55. [Systematic Literature Review of Machine Learning Models and Applications for Text Recognition](https://arxiv.org/abs/2608.26500)

**<font color=#1a73e8>作者：</font>** Nuzhat Khan, Ab Al-Hadi Ab Rahman, Shahriyar Masud Rizvi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Character Recognition (OCR) for text recognition using machine vision has significantly improved, particularly when handling heterogeneous textual data. Traditional OCR models struggle with script variations, writing styles, and degraded documents. Advancements in technology are leading to new AI models with improved architecture for handling multiple languages and complex data formats. Despite this progress, a comprehensive evaluation of OCR advancements remains limited. Based on the established preferred reporting items for systematic reviews and meta-analysis (PRISMA) guidelines, this literature review presents an extensive assessment of OCR research to trace the evolution of AI models over the past decade. It explores the transition in AI models, application domains, data types, linguistic coverage, and challenges. Through a detailed analysis of 97 selected studies published during January 2015 - January 2025, key OCR models are identified, and their performance, strengths, and limitations are analyzed. The findings highlight how OCR technologies have evolved to address structured and unstructured text, scene text recognition, and multilingual processing. Unresolved challenges include limited resources for underrepresented languages, high variability in handwritten text, visual similarity among characters, and constraints in real-time OCR applications. To address these issues, several promising approaches are proposed. Key suggestions include self-supervised learning, multimodal AI, automated machine learning (AutoML), AI-assisted postprocessing, tiny machine learning (TinyML), and the creation of joint corpora for script matching. The future recommendations aim to enhance OCR accuracy and tackle the challenges identified for real-time industrial applications. This study will guide future research and establish a foundation for OCR field.

---


### 56. [NeuDonatello: Uncertainty-Aware Framework for Accurate Neural SDF Learning](https://arxiv.org/abs/2608.26504)

**<font color=#1a73e8>作者：</font>** Alvin Jinsung Choi, Wanhee Kim, Taeyun Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural surface reconstruction has emerged as a powerful paradigm for recovering high-quality 3D surfaces from multi-view images. However, recovering accurate geometry solely from RGB images remains challenging due to uncertainties arising from textureless regions, occlusions, and inherent scene ambiguities. Existing methods often overlook such uncertainties, leading to inaccurate estimates of the signed distance function (SDF). We introduce NeuDonatello, a novel framework that models and leverages SDF uncertainty to improve surface reconstruction. Central to our approach is to model spatially varying uncertainty using a Monte Carlo sampling strategy. Using this uncertainty, we develop an adaptive regularization that selectively strengthens geometric constraints where RGB supervision is unreliable, avoiding incorrect surface reconstruction. We further introduce an uncertainty-aware scale parameter for the SDF-to-density conversion. Conditioned on uncertainty, this design enables more accurate modeling of spatially varying densities. Extensive experiments demonstrate that NeuDonatello achieves state-of-the-art reconstruction accuracy, with robust performance across diverse scenes using only posed RGB images.

---


### 57. [Algorithmic Principles For Multiclass Learning Are Hard To Come By: Limits of Regularization and Proper Learning](https://arxiv.org/abs/2608.26516)

**<font color=#1a73e8>作者：</font>** Julian Asilis, Shaddin Dughmi, Vatsal Sharan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two of the most fundamental questions in statistical learning theory are the following: which prediction problems are learnable, and how should they be learned? For the former, elegant answers often take the form of combinatorial dimensions. The latter question, however, has proved considerably more elusive: all known general-purpose multiclass learners rely on intricate orientations of exponentially large one-inclusion structures, and familiar algorithmic principles such as proper learning and regularization remain poorly understood. Motivated by prior work, we ask whether learning reduces to proper learning---possibly over a larger hypothesis class---and whether proper or improper multiclass learning can ultimately be captured by suitable regularizers.
Our primary results answer both questions negatively, resolving three open problems from prior work. First, we exhibit a learnable multiclass problem that cannot be embedded in any properly learnable class, meaning learning cannot be reduced to proper learning by enlarging the hypothesis class. Second, we demonstrate that proper learning can require training error and characterize this phenomenon precisely: every properly learnable class admits a proper learner making $o(m)$ errors on samples of size $m$, but every prescribed sublinear scale $a_m=o(m)$ is necessary for some properly learnable problem. Third, regularization is not a general learner: we exhibit a properly learnable class that cannot be learned by any Structural Risk Minimization (SRM) learner, and a learnable class that cannot be learned by any local regularizer. We complement these impossibility results with a positive theory that gives two sufficient conditions for SRM learnability and characterizes SRM representability through integrability of revealed preferences.

---


### 58. [HUG-VIS: A Multimodal Benchmark for Human-centered Understanding and Generation in Visual Intelligence](https://arxiv.org/abs/2608.26517)

**<font color=#1a73e8>作者：</font>** Fei Ma, Zebang Cheng, Minghui Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual intelligence seeks to perceive, interpret, and synthesize the visual world and is central to modern computer vision. Human-centered visual intelligence is especially demanding because it studies people as expressive, socially situated subjects whose meaning is rarely conveyed by appearance alone. It couples vision with audio and language across four representative tasks: human emotion recognition, human video generation, human voice cloning, and human video matting. Yet existing resources remain task-specific, providing modalities and annotations for individual problems rather than a shared foundation coordinating understanding and generation. This limits multimodal signal use and broader research. We address this gap with HUG-VIS, a unified benchmark for Human-centered Understanding and Generation in Visual Intelligence. It contains 8,400 seated half-body videos of 30 professional actors, each performing the same 280 emotion-action-prompt assignments under a controlled Mandarin studio protocol, with synchronized video, audio, text, and alpha mattes. We evaluate diverse open- and closed-source models across the four tasks under a unified zero-shot protocol using automatic metrics, criterion-specific mean opinion scores, and multiple cross-task analyses. Results show that (i) linguistic content dominates current emotion recognition, while purely visual affect recognition is weakest; (ii) in video generation and voice cloning, automatic metrics and human judgment agree overall but differ in their top rankings, requiring joint reporting; (iii) boundary fidelity under motion is the main remaining obstacle for human matting; and (iv) task difficulty varies across emotions, models, and metrics, with notable cross-task correlations. The dataset and results are available at this https URL.

---


### 59. [High Probability Derivative Bounds for Random tanh Neural Networks on a Hypercube](https://arxiv.org/abs/2608.26526)

**<font color=#1a73e8>作者：</font>** Josef Dick, Michael Feischl, Fabian Zehetgruber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish high-probability bounds for mixed input derivatives of wide random neural networks whose activation derivatives satisfy a factorial growth bound. Our main result specializes these estimates to $\tanh$ networks with Xavier initialization. A direct deterministic analysis based on Euclidean operator norms of the weight matrices yields derivative bounds that generally grow exponentially with the depth. We show that this growth can be substantially improved for sufficiently wide Gaussian networks by isolating the term that is linear in the highest-order derivative and controlling the corresponding tangent directions by measurable finite nets.
For scalar-output $\tanh$ networks with Gaussian weights and Xavier initialization, we prove that there exist constants $C,C_0,C_1>0$ such that, whenever the common hidden width satisfies $n \geq C\left(L^3n_0^2(1+\log n_0)+L^2\left(1+\log(L/\eta)\right)\right)$, then, with probability at least $1-\eta$, the estimate $\left|D^u\mathcal{R}_{\Phi^{(L)}}(x)\right| \leq C_0 |u|! (C_1L)^{|u|-1}\prod_{j\in u}\beta_j(\eta,n_0)$ holds simultaneously for every non-empty $u\subseteq[n_0]$ and every $x\in[0,1]^{n_0}$. Thus, the first-order derivative bound is independent of the depth, while a square-free mixed derivative of order $|u|$ grows at most polynomially as $L^{|u|-1}$, apart from the coordinate factors. As consequences, we obtain high-probability bounds for the Euclidean Lipschitz constant and for weighted Sobolev norms of the network realization. The latter connect the derivative estimates to quasi-Monte Carlo integration and indicate how such regularity can enter the analysis of QMC-based training.

---


### 60. [PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents](https://arxiv.org/abs/2608.26530)

**<font color=#1a73e8>作者：</font>** Yang Xiao, Yusong Sun, Haoyi Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agent runs generate experience that can improve both the current run and future work. Most self-improvement methods process this experience only after execution ends, so they cannot redirect the active run or immediately apply and validate lessons learned from it. We argue that self-improvement should instead be live, using emerging experience both to redirect the active run and to update the persistent harness. Existing agent architectures do not fully support this goal. Single-agent self-correction combines task execution and trajectory assessment within one context, while subagent delegation separates execution but typically cannot redirect an active subagent. We present PILOT, a supervisor-worker harness for live self-improvement through two coupled mechanisms: (1) live steering lets a separate supervisor redirect or abort the active worker during execution; and (2) live self-evolution distils procedures and failure modes revealed during execution into reusable skills and memory. Across two frozen backbones and three benchmarks, PILOT ranks first in five of six configurations. On Terminal-Bench 2.0, PILOT outperforms counterpart harnesses by up to 9.8 percentage points. In the self-improvement setting, PILOT gains 14.6 points with GLM-5.1 and 12.4 points with Kimi-K2.6. Mean output tokens fall by 42.9% and 47.4%, while successful evaluations per million output tokens rise by 110.3% and 134.0%, respectively.

---


### 61. [Multi2AV-Safety: Benchmarking Safety in Multimodal-to-Audio-Video Generation](https://arxiv.org/abs/2608.26535)

**<font color=#1a73e8>作者：</font>** Kaichao Jiang, Changtao Miao, Baiqi Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Audio-video generation is rapidly moving from prompt-driven synthesis toward multimodal conditioning, where text, images, audio, and video can jointly shape the generated output. This shift changes the nature of safety evaluation: harmful intent may no longer reside in any single input, but instead emerge from how otherwise benign or weakly harmful conditions interact across modalities and time. Existing safety benchmarks, however, remain largely prompt-centric or tied to fixed conditioning interfaces, leaving such compositional risks difficult to study systematically. To bridge this gap, we introduce Multi2AV-Safety, the first safety benchmark, to the best of our knowledge, to cover all 11 non-singleton T/I/A/V conditioning configurations for audio-video generation, comprising 11,024 attack instances. Evaluation on Multi2AV-Safety reveals systematic weaknesses in representative multimodal safety guards across attack mechanisms and harm-evidence structures. Our evaluation reveals two complementary failure modes: harmful semantics can emerge from the combination of individually benign inputs, while explicit harmful cues can become harder to detect when mixed with benign multimodal context. Together, these results identify \emph{compositional risk perception} as a central capability gap in safeguarding multimodal-conditioned audio-video generation: current safety guards fail to reliably integrate safety evidence across modalities and time, even when all conditioning inputs are observable. The dataset will be publicly released in October 2026.

---


### 62. [Predicting Quantifiability from Primary Screens to Prioritize Dose-Response Profiling](https://arxiv.org/abs/2608.26538)

**<font color=#1a73e8>作者：</font>** Sean Lim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-throughput drug screening relies on low-cost primary assays to prioritize compounds for more expensive dose-response profiling, where potency is ultimately quantified. Current screening strategies largely focus on identifying compounds that will confirm biological activity on follow-up, implicitly assuming that confirmed activity will also yield a usable potency estimate. However, confirmed biological activity in screening does not necessarily translate into a quantifiable potency, because active compounds can still fail to produce a reportable dose-response estimate. We therefore present a framework for modeling quantifiability, whether follow-up testing will yield a usable potency estimate, as a distinct triage objective from biological activity. Quantifiability was strongly predictable from the preceding low-cost screen, with most predictive information arising from the observed screening features rather than molecular structure. Response-based predictors remained robust on previously unseen chemical scaffolds and generalized across held-out assay-mechanism families, while the probability of successful quantification varied strongly with response amplitude and assay context. These findings establish experimental measurability, distinct from biological activity, as a predictable property of screening outcomes and show that quantifiability-aware triage can improve the allocation of costly dose-response profiling capacity.

---


### 63. [EmoSay: Artificial Intelligence-Driven Text-to-Emotional-Speech System for Affective Communication in Extended Reality](https://arxiv.org/abs/2608.26566)

**<font color=#1a73e8>作者：</font>** Sikiru Ademola Adewale, Sunday D. Ubur, Nikitha Donekal Chandrashekar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While contemporary neural text-to-speech (TTS) systems have achieved high levels of intelligibility, they frequently lack the emotional nuance required for authentic affective communication. This limitation is particularly critical in Extended Reality (XR), where the absence of emotionally expressive audio can diminish user presence and spatial immersion. We present EmoSay, an Artificial Intelligence-driven Text-to-Emotional-Speech (TTES) system designed to bridge the semantic-affective gap in immersive environments. EmoSay modulates a neural synthesis pipeline using discrete emotional prompts, delivering the output through a Unity-based interface featuring high-fidelity spatialized audio. The system was evaluated through a comprehensive user study focusing on perception, engagement, and the subjective sense of empathy. Our results demonstrate that EmoSay significantly enhances the immersive experience, achieving a System Usability Scale (SUS) score of 74.76, indicating strong usability and seamless integration within the XR workflow. Subjective assessments reveal a high degree of perceived naturalness and a strong positive correlation between emotional expressiveness and user engagement. Regression analysis identifies vocal naturalness as the strongest of the tested predictors of user satisfaction, suggesting that EmoSay's affective prosody helps meet the heightened expectations for realism in immersive settings. This work contributes a scalable, affect-aware framework for inclusive XR design and demonstrates the role synthetic emotion can play in fostering human-computer rapport through voice-first interaction.

---


### 64. [Arrive and Survive: Scaling Safe Goal-Conditioned Policy Learning from One-Bit Failure Signals](https://arxiv.org/abs/2608.26571)

**<font color=#1a73e8>作者：</font>** Guopeng Li, Yiyang Duan, Yiru Jiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive reinforcement learning (CRL) scales effectively in goal-conditioned tasks by casting policy learning into a self-supervised contrastive objective. However, in a failure-terminated Markov decision process, established CRL considers pre-failure future goals only when constructing positive samples, without accounting for the probability mass removed by failure termination. Our theoretical analysis shows that this omission induces a systematic overestimation bias in goal-reaching values. Consequently, near-failure trajectories provide disproportionately strong supervision of success despite retaining little future occupancy. Unsafe actions can thereby be reinforced through catastrophic failure bootstrapping, leading to failed policy learning and unsustainable goal-reaching behaviours. To address this problem, we introduce two minimal yet strong corrections: mass-weighted InfoNCE corrects the overweighting of short surviving futures in critic learning, and a log-survival-mass score restores the missing survival mass in policy optimization. The resulting method, Safe Contrastive Reinforcement Learning (Safe-CRL), requires only the one-bit signal provided by failure termination to scale safe goal-conditioned policy learning. Across twelve failure-prone robot navigation and locomotion tasks, Safe-CRL consistently improves survival and substantially outperforms the Scaling-CRL baseline in goal-reaching performance. Additionally, deep Safe-CRL policies exhibit complex failure-avoidance behaviours. This study completes the CRL theory under failure termination and provides a scalable safe RL framework. The code is available via this https URL.

---


### 65. [Double Trouble: Bilingual Pretraining Leaves Language-Conditioned Effects in Shared-Language Representations](https://arxiv.org/abs/2608.26576)

**<font color=#1a73e8>作者：</font>** Anjishnu Mukherjee, Ziwei Zhu, Antonios Anastasopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When researchers compare multilingual models for probing, interpretability, or cross-lingual transfer, they often align embedding spaces and assume that shared-language representations are comparable. We show that this assumption can be premature for decoder-only models. We pretrain paired 310M-parameter models (one English-only, one bilingual) across eight typologically diverse languages, separately controlling for English exposure, total compute, and document overlap. After aligning on shared English vocabulary, we test held-out words and find that token embeddings look similar after alignment, but the deeper hidden states that the model uses for prediction do not. This gap holds for all eight languages and survives controls for document overlap and alternative alignment methods. This hidden-state mismatch grows through middle transformer layers, suggesting that it arises from contextual processing rather than the input representations where alignment is performed. Embedding alignment can mask real differences in how models internally represent a shared language, which matters for any downstream study that treats aligned models as interchangeable.

---


### 66. [GRAS: Guided Reduced-Variance Proposals and Adaptive Selection for Training-Free Reward Alignment in Discrete Diffusion](https://arxiv.org/abs/2608.26585)

**<font color=#1a73e8>作者：</font>** Kwanyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models have become a strong, widely adopted class of generators for sequence data, and steering them toward a downstream reward at inference time, without any retraining, is increasingly important. Such training-free steering is done by gradient guidance, by search, or by combining the two. We study the combined regime and identify two weaknesses in how it is usually run: the guided proposal estimates its gradient from a single noisy sample, and the search then resamples particles at a fixed temperature that ignores how rewards spread across each denoising step. We address both with a small set of changes that add no denoiser cost. For the proposal, we lower the estimator variance with a Rao-Blackwellized reveal for differentiable rewards and a leave-one-out baseline for non-differentiable ones; for the search, we standardize the per-step values into a group-relative advantage and prove it collapses to a single active ingredient, an adaptive resampling temperature. We call the resulting method Guided Reduced-variance proposals and Adaptive Selection (GRAS). GRAS is simple yet effective: across regulatory DNA and protein design it attains the best training-free reward, outperforming prior training-free methods and matching or surpassing a reward-fine-tuned model, and it remains effective even for non-differentiable rewards.

---


### 67. [DPA-I2P: Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration in Autonomous Driving](https://arxiv.org/abs/2608.26589)

**<font color=#1a73e8>作者：</font>** Wenxin Zhang, Hang Li, Zhiwei Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-Point Cloud Registration aims to estimate the camera pose of a given image within a 3D scene point cloud, which is a fundamental task in autonomous driving and large-scale outdoor localization. Recent implicit correspondence learning methods have improved registration performance by learning cross-modal alignment in an end-to-end framework, leading to more accurate camera pose estimation. However, due to the inherent modality discrepancy between images and sparse LiDAR point clouds, reliable cross-modal correspondence learning remains challenging. To address this issue, we propose Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration (DPA-I2P). Unlike naive depth or feature concatenation, Ray-Conditioned Metric Depth Encoding (RMDE) and Projection-Consistent Vision Lifting (PVL) exploit depth and visual cues in a structured, geometry-aware manner. In addition, Cross-Modal Query Pruning (CQP) suppresses unreliable queries during early refinement to improve matching stability. Experiments on KITTI and nuScenes demonstrate the effectiveness of the proposed method. On KITTI, DPA-I2P reduces RTE and RRE by 45.0% and 55.6% over the strongest implicit baseline, respectively. On nuScenes, DPA-I2P also improves registration accuracy over the evaluated baselines, suggesting better transferability to different driving scenes.

---


### 68. [SimCast-S2S: An Efficient Generative Model for Subseasonal Precipitation Forecasting via Transfer Learning from Climate Simulations](https://arxiv.org/abs/2608.26594)

**<font color=#1a73e8>作者：</font>** Hiep V. Dang, Antonios Mamalakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subseasonal-to-seasonal (S2S) precipitation forecasting has substantial financial and societal impact, yet remains challenging because of weak predictive signals, high associated uncertainty, and the computational cost of operational systems, which constrains simulation fidelity. We introduce SimCast-S2S, a generative latent-diffusion framework for probabilistic S2S precipitation forecasting that addresses three major bottlenecks in data-driven prediction. First, because S2S prediction requires uncertainty quantification rather than only deterministic point forecasts, SimCast-S2S is the first data-driven system that uses a diffusion-based generative pipeline for S2S prediction, enabling effective sampling from the underlying conditional distribution. Second, since generating large probabilistic ensembles is computationally costly in physical space, SimCast-S2S instead operates in a compact latent space learned by variational autoencoders, enabling efficient large-ensemble generation. Third, diffusion models typically require large training datasets; SimCast-S2S overcomes this via transfer learning with low-rank adaptation (LoRA), pretraining on large ensembles of climate simulations before fine-tuning on limited reanalysis data. On reanalysis data, SimCast-S2S outperforms deep learning baselines, including convolutional neural networks and U-Net architectures. Notably, despite using only a subset of atmospheric input variables and no post-processing, bias correction, or calibration, SimCast-S2S remains competitive with, and in many cases outperforms, state-of-the-art operational systems such as the ECMWF-S2S baseline. These results indicate that latent generative modeling combined with simulation-to-reanalysis transfer learning offers an efficient and scalable path toward data-driven probabilistic S2S precipitation forecasting.

---


### 69. [FU-Mamba: A Frequency-Enhanced Dynamic Scanning Framework for Oralscan Image Segmentation](https://arxiv.org/abs/2608.26607)

**<font color=#1a73e8>作者：</font>** Xinxin Zhao, Jinpeng Ye, Bo Wei 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Oralscan image segmentation is essential for computer-aided diagnosis and treatment planning in digital dentistry. However, existing visual state space models (SSMs) often rely on manually designed scanning orders to flatten image patches into sequences, which disrupts the semantic spatial continuity and hinders coherent feature extraction from key foreground regions. Moreover, elements such as inconsistent lighting, reflective surfaces, and noise during data acquisition disrupt the frequency distribution by diminishing high-frequency details while enhancing low-frequency components, consequently hindering the accurate localization of boundaries. In response to these challenges, we introduce FU-Mamba, an innovative framework that incorporates dynamic scanning and frequency domain enhancement within the SSM architecture. Specifically, the Dynamic Mamba Block (DMB) adaptively learns sampling offsets via a trainable offset prediction network and performs flexible bilinear interpolation, enabling content-aware scanning that preserves spatial coherence. Furthermore, a frequency domain enhancement block balances spectral components through wavelet-guided decomposition and spectrum pooling, improving robustness under adverse imaging conditions. Experimental findings indicate that FU-Mamba attains a notable enhancement in segmentation accuracy, evidenced by a 1.1% increase in the mean intersection over union (mIoU) metric when evaluated on the dental segmentation dataset. Project page: this https URL

---


### 70. [Technical Comparative Benchmarking Study: Advanced AI Hybrid Methods for Renewable Energy Farm Optimization and Forecasting](https://arxiv.org/abs/2608.26613)

**<font color=#1a73e8>作者：</font>** Majid Masoumi, Asghar Dashtiy, Mohammad Dehghan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study provides a comprehensive benchmarking of conventional machine learning (ML), ensemble learning, deep neural networks, recurrent architectures, Transformers, graph based models, and hybrid ensemble deep learning approaches under complementary renewable energy scenarios. Three datasets are considered: a large scale WEC dataset, a 16 WEC dataset, and operational 10 min SCADA measurements at the Penmanshiel wind farm. For structured WEC layout data, tree ensembles exhibited a clear advantage over conventional ML and neural predictors because randomized partitioning and boosting efficiently captured nonlinear layout power interactions without requiring explicit feature representation learning. The Extra Trees was the strongest model, achieving considerable results. Relative to the MLP baseline, this corresponds to an approximately 63.7% reduction in MAE, demonstrating the suitability of randomized tree ensembles for high dimensional structured WEC data. Also, STGCN reduced the MAE to approximately 167.0 kW and achieved R = 0.93 by explicitly learning spatial and temporal turbine interactions. The best overall forecasting accuracy was obtained by the RF BiLSTM hybrid, with an MAE=150.5 kW. Compared with standalone LSTM, this represents an approximately 75% reduction in MAE, while improving on STGCN by approximately 10.0%. Finally, the experiments reveal that no single AI architecture is universally optimal: randomized and boosted ensembles are particularly effective for structured WEC surrogate modeling, graph networks become advantageous when explicit spatial interactions dominate, and ensemble recurrent hybrids provide the strongest balance when nonlinear tabular relationships and temporal dynamics coexist.

---


### 71. [Text-to-seed generation: Training-free open-vocabulary seeded semantic segmentation via re-purposing diffusion as text-guided seed generator](https://arxiv.org/abs/2608.26624)

**<font color=#1a73e8>作者：</font>** Kumju Jo, Heesun Jung, Sungyong Baik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation (OVSS) aims to segment image regions corresponding to arbitrary text queries. Although the Segment Anything Model (SAM) is a powerful foundation model for segmentation, its standalone performance on OVSS remains limited. Existing methods therefore often use SAM to refine coarse masks predicted by other models, but this strategy is unreliable when the initial masks are inaccurate. In this work, we argue that more reliable segmentation can be achieved by exploiting SAM as a region expansion module guided by accurate object points (i.e., seeds) rather than inaccurate coarse masks. Inspired by classical seeded segmentation, we reformulate OVSS as text-guided seed localization followed by seed-based region expansion. To realize this idea, we propose Text-to-Seed (T2S), a training-free framework that leverages the text-to-region correspondence of Stable Diffusion to generate attention-based seed points for target categories described by text. These sparse seeds are then used as point prompts for SAM to produce full object masks. Without task-specific training or additional annotations, T2S achieves strong performance on standard OVSS benchmarks, demonstrating the effectiveness of combining semantic grounding with seed-driven spatial segmentation.

---


### 72. [Risks and Controls for Multi-Agent Systems: an analytical framework for deployment of AI agents across organisational boundaries](https://arxiv.org/abs/2608.26626)

**<font color=#1a73e8>作者：</font>** Alistair Reid, Simon O'Callaghan, Dustin Venini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This report presents a framework to help organisations, policymakers and researchers reason about the risks that emerge when AI agents interact with each other, how those risks change as interactions cross organisational boundaries, and the controls that may help address them.
As organisations deploy AI agents, those agents will increasingly interact with each other: inside the organisation, with the agents of partners, customers and suppliers, and with unknown counterparties on the open internet. Failures can emerge from the interactions themselves, and once those interactions cross an organisation's perimeter, no single organisation can fully see, control or govern them.
The report introduces three deployment tiers, defined by the minimum common governance binding any two interacting agents: singular governance, where one organisation governs every agent; federated governance, where multiple organisations deploy into a shared environment under agreed rules; and open environments, where agents operate with no central authority and shared standards are adopted voluntarily if at all.
Within each tier, the report examines risk factors, failure modes and available controls. It identifies who is positioned to apply the controls, and where no actor is positioned to act, it characterises the gap and the collective action required to close it.

---


### 73. [Which Metrics Save the Most Human Annotation? Prediction-Powered Evaluation and Meta-Evaluation](https://arxiv.org/abs/2608.26638)

**<font color=#1a73e8>作者：</font>** Mingqi Gao, Anthony Sicilia, Weiyan Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Across various non-verifiable tasks, human evaluation is reliable but expensive, while automatic metrics are more scalable but often biased. Building on prediction-powered inference (PPI), we propose prediction-powered evaluation, a framework that combines limited human judgments with large-scale automatic scores to obtain data-efficient system comparisons that are provably unbiased. We develop parametric and non-parametric procedures, analyze the efficiency trade-off between paired and unpaired designs, and validate the framework on six WMT datasets. We further introduce the Prediction-Powered Saving Ratio (PPSR), a meta-metric that measures how much human annotation an automatic metric can save when used within prediction-powered evaluation. PPSR directly targets metric utility for prediction-powered evaluation and yields more discriminative and stable metric rankings than existing system-level meta-metrics. Overall, our new paradigm reframes automatic metrics as tools for reducing human annotation cost rather than replacing human judgment, and applies broadly to non-verifiable tasks.

---


### 74. [Real-time Unsupervised Object Discovery from Asynchronous Event Streams](https://arxiv.org/abs/2608.26644)

**<font color=#1a73e8>作者：</font>** Pratham G. Shenwai, Hemant Kumar Singh, Sridhar Ravi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras capture pixel-level intensity changes with microsecond resolution to produce highly sparse asynchronous data streams. For visual perception in latency-critical environments, we propose a lightweight, training-free framework for discovery of moving objects based on spatio-temporal clustering. This framework is driven by two core contributions. First, a linear-time Spatio-temporal Probabilistic Event Filter (SPEF) that introduces an adaptive event acceptance threshold to distinguish salient motion structures from background noise. Second, an Event Morton Code Clustering (EMCC) module that bypasses expensive distance matrix computation to efficiently group events for unsupervised discovery of moving objects. On the E-MLB dataset benchmark, SPEF achieves the best denoising performance among classical filtering methods and remains competitive with learning-based approaches without requiring any offline training. On object discovery, EMCC achieves the highest overall accuracy and lowest execution time across the FRED and eTraM datasets, outperforming established density-based clustering baselines by a substantial margin. Overall, this work establishes a new performance benchmark for classical object discovery in event data, providing a highly scalable, training-free solution for resource-constrained visual perception. The code is available at this https URL

---


### 75. [Tissue-Mixture Entropy-Weighted Reconstruction for Partial-Volume-Aware Brain MRI Super-Resolution](https://arxiv.org/abs/2608.26647)

**<font color=#1a73e8>作者：</font>** Xiao Tong, Wenyun Yang, Ziheng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Full-image objectives in brain magnetic resonance imaging (MRI) super-resolution (SR) can underweight tissue-transition regions affected by the partial-volume effect (PVE), as these regions occupy only a small fraction of the image. Binary boundaries also do not capture the continuous mixture of cerebrospinal fluid, gray matter, and white matter within a voxel. We propose Anatomy-Guided Gaussian-Parameter Warping with PVE-Balanced Reconstruction (AGW-PBR), which combines a low-resolution (LR)-only reconstruction backbone with a training-time objective that emphasizes tissue transitions. The backbone integrates LR-derived Sobel guidance, soft latent-basis assignment, and bounded grid-anchored residual warping. Fixed, quality-controlled tissue fractions derived from registered T1/T2/PD IXI images are converted into tissue-mixture entropy, which defines mean-normalized reconstruction weights within validated PVE support. These sidecars are used only during training, and inference requires only the LR image. AGW-PBR is evaluated on T2-weighted IXI images at 2x, 4x, and 6x using three seeds and subject-level paired analyses. At 4x, test-only SynthSeg masks independently assess reconstruction in tissue-interface and non-interface regions. Targeted ablations examine valid-support supervision, spatially aligned entropy weighting, and soft latent assignment. The AGW-backbone is also trained from scratch on fastMRI at 4x without PVE supervision. AGW-PBR improves full-image reconstruction across the tested IXI scales and regional fidelity at 4x, while the PVE-free backbone retains strong performance on fastMRI. These findings support tissue-mixture entropy weighting for partial-volume-aware brain MRI SR.

---


### 76. [Hierarchical Channel Stacking: A Structured Decision Framework for AI-Generated Image Detection](https://arxiv.org/abs/2608.26648)

**<font color=#1a73e8>作者：</font>** Saifullah Shoaib, Akash Borigi, Rupendra Lekkala 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many synthetic-image detectors produce accurate predictions but offer limited insight into how those decisions are formed. This paper introduces Hierarchical Channel Stacking (HCS), a compact framework for AI-generated image detection that converts intermediate CNN activations into a structured 60-dimensional representation organized across three progressively deeper backbone stages. HCS uses per-channel Level-1 classifiers and a Level-2 aggregator to produce image-level predictions while preserving explicit hierarchical structure for analysis. On a benchmark spanning GAN and diffusion generators, HCS achieves 86.7% accuracy and 86.7% macro-F1 on the held-out test set. Stage ablation shows that the full three-stage system outperforms reduced single-stage and two-stage variants, indicating that the hierarchy carries complementary predictive information. Stage-level contribution analysis further shows that, in the analyzed detector setting, fake GAN and fake diffusion images exhibit distinct stage-level contribution profiles. These results position HCS not simply as a compact detector, but as a structured framework for studying how synthetic-image detectors assemble evidence across representation levels.

---


### 77. [Robust Neural Stimulation Response Modeling Through Meta-Learning and Pretraining](https://arxiv.org/abs/2608.26649)

**<font color=#1a73e8>作者：</font>** Matthew J Bryan, Daniel C Muir, Felix Schwock 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective: Model-based closed-loop neural stimulation holds promise for therapeutic applications ranging from Parkinson's disease to sensory restoration, but deployment has been limited by two obstacles: 1) forecasting models for predicting the consequences of stimulation fail catastrophically on a meaningful fraction of sessions, and 2) per-session calibration requirements are often incompatible with clinical constraints. We address both by demonstrating, for the first time, that meta-learning and pretraining can be applied to neural stimulation response modeling. Methods: Temporal basis function models (TBFMs) forecast state-dependent neural responses to stimulation. We extend TBFMs with cross-session pretraining using a novel architecture and algorithm based on model-agnostic meta-learning (MAML), evaluating them on 40 sessions of optogenetic stimulation in primary sensorimotor cortex of two non-human primates. Results: Meta-learning substantially reduces catastrophic forecast failure: for a 1k calibration set size, sessions with test R-squared < 0.05 drop from 16 of 40 (single-session training) to 1 (MAML-pretrained), and prediction intervals become significantly narrower (p < 0.05). Calibration requirements are reduced by 50-90% at matched accuracy, enabling experiments otherwise infeasible within clinical session-time constraints. Conclusion: Our results demonstrate that cross-session structure in stimulation responses is consistent enough to support pretraining, providing the first empirical evidence that meta-learning approaches are viable for neural stimulation. Significance: The robustness and sample efficiency gains directly address known obstacles to deploying model-based stimulation controllers. Our results motivate community efforts to assemble standardized multi-site stimulation datasets and to further explore meta-learning for robust closed-loop stimulation.

---


### 78. [When Privacy Hurts Mergeability: Geometry-Aware Model Merging under Differential Privacy](https://arxiv.org/abs/2608.26655)

**<font color=#1a73e8>作者：</font>** Jin Liu, Junkang Liu, Ning Xi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging promises to construct a single multi-task model from independently fine-tuned task models without accessing the original task data. This makes it attractive when task data cannot be centralized, but released task models may still leak private fine-tuning data. Differential privacy (DP) provides a principled mechanism for limiting such leakage, yet its effect on model merging remains poorly understood. In this paper, we study the geometry of differentially private model merging and identify two geometric obstacles that make private task models difficult to merge: \emph{local sharpness}, which makes task losses sensitive to the parameter displacement induced by merging, and \emph{reference drift}, which measures the displacement of private task models from the shared pretrained initialization and amplifies cross-task interference. Based on these observations, we propose \textbf{DP-Merging}, a geometry-aware framework that improves the mergeability of differentially private task models. DP-Merging uses a DP-compatible sharpness-aware objective to guide each private task model toward flatter loss regions, and a reference-based alignment regularizer to keep task models close to the shared pretrained initialization. We derive a merge-gap upper bound showing that reducing local curvature and reference drift tightens the bound on the loss increase induced by merging. Experiments on vision and language tasks across multiple privacy budgets show that DP-Merging consistently improves private merged-model performance while preserving the privacy guarantees of the underlying DP fine-tuning procedures.

---


### 79. [CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes](https://arxiv.org/abs/2608.26656)

**<font color=#1a73e8>作者：</font>** Yuanxiang Ni, Xianliang Huang, Chenhang Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object removal in 3D scenes is challenging due to severe occlusions, semantic entanglement, and the difficulty of maintaining geometric and multi-view consistency. Existing 3D Gaussian Splatting (3DGS) methods perform well for single-object editing but scale poorly to multi-object scenarios, often requiring repetitive optimization and yielding unstable geometry in removed regions. We propose CoGeo-GS, a concept-driven framework for controllable multi-object removal in 3D scenes. CoGeo-GS assigns concept-aware semantic tags to Gaussians, enabling flexible object selection and reducing interference between foreground objects and background structures within a single optimization stage. To recover plausible geometry, we introduce a geometry-aware completion pipeline that combines monocular depth priors with diffusion-based refinement and boundary-aligned blending. A geometry-regularized refinement strategy further stabilizes reconstruction and preserves multi-view consistency. Experiments demonstrate that CoGeo-GS outperforms existing methods in visual quality and reconstruction fidelity.

---


### 80. [Simple Actors and Deep Critics for Scalable Reinforcement Learning](https://arxiv.org/abs/2608.26659)

**<font color=#1a73e8>作者：</font>** Guhyeon Kang, Jaehwi Lee, Minhae Kwon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in offline reinforcement learning (RL) has been driven by expressive generative actors such as diffusion and flow-matching policies, which capture multimodal behavior in offline datasets. However, these actors require multiple denoising or integration steps per action and thus incur substantial overhead at every decision in deployment. In this work, we revisit where capacity should be invested in an offline actor--critic method. Since the critic is used only during training and is discarded at deployment while the actor runs at every decision step, allocating capacity to the critic rather than the actor is more favorable for inference-time efficiency. However, scaling MLP critics in offline RL is known to introduce several distinct instabilities that have, in practice, kept critics shallow. We identify three distinct failure modes that arise when critics are deepened in offline RL---optimization, bootstrap-noise amplification, and value-range drift---and address each with a corresponding ingredient: a residual MLP backbone, n-step bootstrap targets, and a categorical cross-entropy loss. Combining these ingredients with a lightweight deterministic actor, we propose LAC (Light Actor, deep Critic). On OGBench, LAC matches the strongest diffusion- and flow-matching baselines while achieving up to 4x lower inference latency, comparable to one-step distilled policies without distillation. Its critic recipe also transfers across actor parametrizations.

---


### 81. [Hull First, Wake Second: Wake-Reliance Suppression for Robust Maritime Vessel Detection](https://arxiv.org/abs/2608.26665)

**<font color=#1a73e8>作者：</font>** Yefan Wang, Xingyu Wang, Ruibiao Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maritime vessel detectors often face scenes where hulls are small, low-contrast, or blurred, while wakes are longer and easier to detect. This creates a wake-reliance problem: detectors may miss slow or stationary vessels with weak wakes, or produce false positives on wake-like water clutter. We propose HullWake, a hull-first wake-second framework for robust maritime vessel detection. HullWake separates proposal-centered hull evidence from directional wake context, extracts wake cues with bidirectional proposal-anchored corridors, and suppresses wake-dominant predictions through wake response supervision, wake-attenuated consistency, wake-only confidence suppression, and hull--wake decorrelation. We also introduce a wake-oriented evaluation protocol covering weak/no-wake vessels, wake-like hard negatives, worst-group AP, and confidence drop after wake attenuation. Experiments are conducted on Curated-Wake, a wake-oriented maritime dataset of about 10,000 images curated from Ships/Vessels in Aerial Images, the SMD benchmark, and SeaDronesSee, with newly added detection- and segmentation-level wake annotations. Compared with box-only detectors and mask-supervised segmentation baselines, HullWake improves overall AP, weak/no-wake robustness, wake-like false positives, worst-group AP, and confidence stability after wake attenuation.

---


### 82. [SIGMA: Structured Noise-Effect-Aware Grouped Multi-Agent Aggregation](https://arxiv.org/abs/2608.26683)

**<font color=#1a73e8>作者：</font>** Li Mingqian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-agent reinforcement learning (MARL) faces significant challenges in maintaining robust coordination under noisy observations. Although observation disturbances are often introduced independently across agents, their downstream effects on cooperative decision-making can become structured through underlying cooperation structures. We characterize this phenomenon as structured noise effects, where noise-induced decision effects exhibit local correlation among agents with stronger task-related dependencies while remaining globally heterogeneous across different agents and local structures. Existing robust MARL methods, however, rarely explicitly characterize or exploit such structure-dependent noise effects. To address this limitation, we propose SIGMA, a hierarchical collaboration framework that exploits cooperation structures to learn robust representations under noisy observations. SIGMA first organizes agents into adaptive local structures through density-based grouping and performs intra-group consensus aggregation to preserve shared task-relevant information while smoothing agent-specific representation deviations. Inter-group attention then adaptively integrates information across different groups to preserve global coordination while accommodating their heterogeneous contributions. Experiments on noisy-observation tasks in StarCraft II empirically validate the structured noise effects and demonstrate that SIGMA consistently improves robustness under observation noise while maintaining competitive performance in noise-free environments.

---


### 83. [Domain-Specific Self-Supervised Representation Learning for Retinal Fundus Classification](https://arxiv.org/abs/2608.26686)

**<font color=#1a73e8>作者：</font>** Bekzat Nurlanbekova, Fung Fung Ting  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the growing number of public datasets, annotated medical images remain scarce. Supervised learning methods achieve strong performance on many benchmarks, however require large amounts of labeled data, which are costly and time-consuming to obtain in the medical domain. To address this limitation, contrastive self-supervised learning (SSL) has emerged as a promising alternative for learning useful representations from unlabeled data. In this work, we investigate two SSL frameworks, SimSiam and SimCLR, for retinal disease classification from fundus images. We focus on understanding how augmentation strategies and training parameters influence representation learning under resource-constrained settings. Given limited data and computational capacity, we explore the feasibility of training SSL models with small batch sizes incorporated with retinal-specific augmentation techniques. Through a series of experiments, we assess the quality of learned representations via linear evaluation and fine-tuning across downstream tasks, including multi-disease classification and diabetic retinopathy grading. Our results show that tailoring augmentation strategies to the characteristics of retinal images plays a critical role in improving performance. Even under constrained settings, lightweight SSL frameworks can learn transferable representations that reduce dependence on large annotated datasets and achieve competitive results.

---


### 84. [Beyond Reflection: Affirmation as a Promising Behavioral Marker Associated with Quality in Text-Based Counseling](https://arxiv.org/abs/2608.26689)

**<font color=#1a73e8>作者：</font>** Michimasa Inaba  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While AI-assisted text-based counseling is gaining attention, it remains empirically unclear which counselor behaviors are associated with higher dialogue quality. Existing research often focuses heavily on Reflection, borrowing frameworks from Motivational Interviewing. To address this gap, we conduct a multi-layered analysis using KokoroChat, a large-scale Japanese text counseling dataset conducted by professional counselors and trainees, newly annotated with counselor strategy tags and client distress levels. Our results show that, under the quality indicators used in this study, Affirmation is more consistently associated with session quality than Reflection among the analyzed strategies. Cross-dataset transfer experiments further suggest that this quality signal can be observed to some extent on ESConv, an English dataset with non-expert supporters. These findings provide empirical implications for counselor training and emotional support system design. We release the additional KokoroChat annotations and experimental source code at this https URL.

---


### 85. [Five Primitives for Governing Autonomous AI Agents at Runtime](https://arxiv.org/abs/2608.26696)

**<font color=#1a73e8>作者：</font>** Jiten Oswal, John Cadeddu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise deployments of autonomous AI agents inherit a control model built for human users and long-lived services, and the fit fails in three specific ways: agent principals are ephemeral, appearing and vanishing faster than provisioning; their actions are selected by a model rather than programmed, so the set of things they may attempt is not known in advance; and the population is discovered rather than provisioned, because anyone who can call an API can create one. We argue that governing such agents is a runtime problem -- not a model-alignment problem and not a build-time problem -- and we derive five primitives from the questions that must be answered before an action takes effect and after it has: discovery, identity, governance, attestation, and supply chain. For each we state what fails if it is absent and why the others cannot structurally supply it. We describe an implementation in which an agent's action is mediated against policy before it takes effect, authorised against a per-tenant action vocabulary, and recorded in a hash-linked signed ledger a third party can verify with the vendor out of the loop. We report what the architecture costs: the enforcement point sits on the request's critical path, identity requires a sidecar per workload, and fail-closed mediation converts availability incidents into denial. We are explicit about implementation status: four primitives are built and running in private pilots, and the fifth is built as separate tooling and not yet integrated into the request path. We keep it in the set deliberately: a five-part decomposition that exactly matches what its authors happened to build is not a taxonomy but a description of a codebase.

---


### 86. [Scaling phoneme-based TTS augmentation for ASR: A unified pipeline and controlled study](https://arxiv.org/abs/2608.26697)

**<font color=#1a73e8>作者：</font>** Zhen Wang, TianRui Wu, RongQi Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic speech provides scalable supervision for automatic speech recognition (ASR), but its benefit depends on the selected texts, reference speech, and amount of synthesized data. We present a unified phoneme-based TTS-to-ASR augmentation pipeline built around a multilingual TTS model trained from scratch using the F5-TTS architecture with language-ID conditioning. The pipeline combines language-specific grapheme-to-phoneme conversion, reference-speech filtering, candidate-text selection, synthesis, and matched ASR continuation. We further propose phoneme-frequency-guided selection (PFGS), which ranks candidate sentences using phoneme frequencies estimated from real ASR training labels. Experiments with separate monolingual ASR systems for Arabic, French, Italian, and Portuguese span 13 test sets. Across the synthesis-scale sweep, random augmentation improves over matched real-only continuation on 11 test sets. Under a nominal 60% synthesis budget, PFGS improves over real-only training on 12 test sets and over random selection on 9. Its largest relative word error rate (WER) reduction against random selection is 19.3%. With target texts and synthesis counts fixed, reference-speech filtering reduces absolute WER by 0.29 and 0.59 points on Italian and French Common Voice, respectively. These results identify synthesis scale, candidate-text content, and reference quality as important control variables in TTS-based ASR augmentation.

---


### 87. [PragAlign: Evidence-Sensitive Reply Assistance Across Chinese and Japanese Appropriateness Judgments](https://arxiv.org/abs/2608.26700)

**<font color=#1a73e8>作者：</font>** Xin Zhong, Satori Hachisuka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reply assistance in multilingual settings requires linguistic competence and culturally situated judgments of appropriateness. We present PragAlign, which separates context reading from selective clarification, and evaluate it alongside Direct and Rule. Nine native Chinese speakers judged Chinese materials, while three native Japanese speakers judged matched Japanese versions. In the Chinese evaluation, PragAlign received significantly better ranks than both baselines. In the Japanese evaluation, Direct had the lowest mean rank, PragAlign had the highest top-rank rate, and the omnibus difference was not significant. The groups selected the same top condition in 5 of 10 scenarios, including four shared PragAlign selections. The results identify shared and language-specific judgment patterns and inform reply assistance designed to support linguistic and cultural understanding.

---


### 88. [Style as a Confound: False Positives in AI Detection of Non-Native Academic Writing](https://arxiv.org/abs/2608.26710)

**<font color=#1a73e8>作者：</font>** Hyeonchu Park, Gahye Jeong, Bugeun Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI text detectors are increasingly employed in academic settings, but it remains unclear whether their outputs reflect AI authorship itself or broader linguistic features associated with polished academic English. Previous studies have reported high false-positive rates (FPRs) for non-native English writing, but population-level comparisons confound authorship with differences in topic, domain, and writing style. Professional editing provides a useful setting for examining this issue because it changes the linguistic form of manuscripts while preserving authorship and content. We examined 135,389 document pairs from a professional English editing service (2018-2025), comprising non-native manuscripts and their native-edited versions, to assess how editing affects detector responses controlling for content and authorship. For the 13 AI text detectors, FPRs for human-written texts varied widely, from 0.0% to 100.0%. Responses varied across detectors: the same edits increased AI scores in some detectors but decreased them in others. Notably, score changes correlated with the extent of editing. The findings identify professional editing style as a key confounding variable in AI detector outputs, rather than establishing a full separation of text origin from linguistic style, raising concerns about fairness and reliability in academic settings.

---


### 89. [LiveVVT: High-Fidelity Video Virtual Try-On in Real Time](https://arxiv.org/abs/2608.26714)

**<font color=#1a73e8>作者：</font>** Yushe Cao, Shikun Feng, Ruxiang Duan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based Video Virtual Try-On (VVT) achieves high visual fidelity through bidirectional spatio-temporal modeling, but complete-clip dependence incurs prohibitive latency and computational overhead in practical continuous deployment. Naively enforcing causality disrupts pretrained bidirectional priors and substantially degrades synthesis quality. We introduce LiveVVT, a rolling streaming diffusion framework that preserves bounded bidirectional modeling within causal recurrent generation. Within a fixed-size window, LiveVVT jointly denoises multiple video chunks under bounded look-ahead, preserving local bidirectional interactions while emitting one clean chunk per iteration. Beyond the window, two complementary memories sustain long-term consistency: a bounded temporal memory propagates recent dynamics and occlusion context, whereas a persistent global appearance memory, constructed once from the target garment and a frontal try-on keyframe, anchors garment details and dressed appearance throughout the stream. We further introduce a progressive distillation framework integrating bidirectional VVT learning, teacher-trajectory regression for causal few-step adaptation, and Collaborative Matching Distillation, which couples teacher-distribution matching with rolling flow matching on real videos to align optimization with recurrent inference. Experiments on paired and unpaired long-sequence benchmarks demonstrate superior generation quality over similarly sized models, with $26\times$ lower latency and $11\times$ higher throughput, enabling high-fidelity real-time streaming VVT.

---


### 90. [Parameter Efficient Continual Learning for Sparse Event-Based Transformers](https://arxiv.org/abs/2608.26720)

**<font color=#1a73e8>作者：</font>** Vaishnavi Nagabhushana, Kartikay Agrawal, Ayon Borthakur  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic and edge intelligence systems operate in dynamic environments where data arrives continuously, requiring models to adapt while preserving previously learned knowledge under strict memory and energy constraints. While parameter-efficient fine-tuning has shown promise for continual learning with vision transformers, conventional architectures rely on dense computation and remain costly for real-world deployment. Sparse event-based vision transformers provide energy-efficient event-driven computation, yet their continual learning capabilities remain largely unexplored. We here introduce sLoTh, a parameter-efficient continual learning framework for pretrained sparse event-based (spiking) vision transformers. sLoTh freezes the backbone and restricts plasticity to scalable-efficient low-rank attention updates (seLoRA) and shared neuronal threshold modulation, enabling adaptation without replay buffers by updating less than 1% of model parameters. Experiments across CIFAR-100, Tiny-ImageNet, ImageNet-100, and ImageNet-R with up to 100 tasks demonstrate competitive rehearsal-free performance in class-incremental learning and online continual learning, while enabling approximately 6.5x lower energy consumption than conventional dense vision transformers.

---


### 91. [GeoMAD: Geometry-Aware Multi-View Anomaly Detection via Deformable Fusion and Distributional Alignment](https://arxiv.org/abs/2608.26724)

**<font color=#1a73e8>作者：</font>** Shang-Fu Chen, Jhih-Ciang Wu, Kuan-Chuan Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view anomaly detection (MvAD) detects defects by exploiting complementary observations from multiple camera viewpoints. The central challenge is to fuse views with sufficient geometric awareness while remaining scalable to multi-class industrial settings. Existing methods typically fall into two extremes: voxel-based fusion provides explicit geometric alignment but requires costly 3D construction and class-specific assumptions, whereas lightweight patch-based fusion is efficient but relies on discrete candidate matching and lacks continuous cross-view correspondence. In this paper, we propose GeoMAD, a unified multi-view, multi-class AD framework that addresses both geometric correspondence deficiency and distributional inconsistency. Our \textit{Cross-view Deformable Fusion Module} (CDFM) learns content-adaptive, view-pair-specific sampling offsets directly on 2D feature maps and arranges them across a multi-scale window pyramid with image-global reference sampling, enabling hierarchical cross-view correspondence without camera calibration, voxel construction, or class-specific 3D supervision. We further introduce \textit{Distributional View Alignment} (DVA), a self-supervised cross-view regularization loss that aligns each view's bottleneck distribution against a per-instance view-centric target, enforcing global consistency without pixel-level correspondence. Together, CDFM and DVA bridge local geometric correspondence and global distributional consistency, providing geometry-aware and distribution-consistent fusion while preserving the efficiency of 2D feature-space learning. Extensive experiments on Real-IAD and MANTA-Tiny show that GeoMAD achieves strong detection and localization performance in unified MvAD.

---


### 92. [Neural Regression with Embeddings for Numerical Attribute Prediction in Knowledge Graphs](https://arxiv.org/abs/2608.26729)

**<font color=#1a73e8>作者：</font>** Rupesh Sapkota, Louis Mozart Kamdem Teyou, Moshood Yekini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, transductive knowledge graph embedding models have been applied to tasks such as link prediction and query answering. Although knowledge graphs often contain rich numerical attributes, most embedding models neglect them, limiting their ability to represent real-world knowledge graphs with diverse information. In this work, we propose a neural regression model (LitEm) that enables transductive knowledge graph embedding models to predict numerical attributes within knowledge graphs. Experimental results demonstrate that LitEm achieves the best or second-best results on most attributes across FB15K-237, YAGO15K, DB15K, and Mutagenesis. Furthermore, we propose a co-training framework that jointly trains state-of-the-art transductive knowledge graph embedding models with LitEm, which improves link prediction performance mainly for bilinear models and simultaneously enables them to predict numerical attributes. In addition, the literal-awareness evaluation demonstrates that co-training helps models to encode and exploit attribute information in a "literal-aware'' manner, suggesting that the observed gains are not merely due to additional parameters. We publicly release our implementation at this https URL.

---


### 93. [Dynamic Tree Colors: Adaptive Discriminable Hierarchies with Minimum Instability](https://arxiv.org/abs/2608.26734)

**<font color=#1a73e8>作者：</font>** Tobias Mertz, Steven Lamarr Reynolds, Jörn Kohlhammer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Hierarchical color maps can support users in the analysis of hierarchical data. For large hierarchies, dynamic color maps can improve discriminability upon user interactions, but the incremental color changes may cause users to lose their orientation in the data set. To address this challenge, we present Dynamic Tree Colors, a dynamic hierarchical color map that can be configured to a suitable tradeoff between discriminability and color stability. We also define quality metrics for both criteria and investigate our algorithm's performance with respect to these metrics as well as a user study with 18 participants. Our results indicate that Dynamic Tree Colors yields good results in a wide range of application scenarios, but it does not achieve the performance of the state-of-the-art algorithm Cuttlefish in the specific scenario that algorithm was designed for.

---


### 94. [Generative Semantic Scene Completion](https://arxiv.org/abs/2608.26737)

**<font color=#1a73e8>作者：</font>** Shi Chen, Weifeng Ge  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Outdoor LiDAR semantic scene completion (SSC) recovers a dense semantic voxel grid from a scan observing 1% of the target volume, under class imbalance beyond 7,000x. We recast SSC as generative semantic scene completion (GSSC): a single discrete-diffusion formulation in three roles. First, paired sparse-dense scene synthesis (PS$^3$) generates matched sparse LiDAR observations with their dense semantic completions, addressing the long tail at its source and yielding the PS$^3$-SemanticKITTI corpus we train on alongside SemanticKITTI. Second, semantic-guided generative scene completion (SGSC) generates the scene from noise with multinomial discrete diffusion, conditioned on the sparse scan through a bird's-eye-view semantic map and a sparse 3D feature stream. Third, the same framework instead refines an existing completion in one flow-matching step: structured source discrete diffusion (S$^2$D$^2$). S$^2$D$^2$ improves the mIoU of SGSC's own output and every external SSC base tested, without base retraining or test-time adaptation. On the strongest base, one step without test-time augmentation reaches 38.8% mIoU on the SemanticKITTI hidden test. To our knowledge that is the best causal, single-sweep, single-sample result on that leaderboard, +2.1 pp over the previous best published score under the same restriction. Four correction steps with eight-view test-time augmentation reach 39.2%, outside that restriction.

---


### 95. [Self-Augmented Diffusion Guidance for Physics-Informed Generation](https://arxiv.org/abs/2608.26748)

**<font color=#1a73e8>作者：</font>** Akira Osaka, Naoya Takeishi, Takehisa Yairi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models can be used to generate spatiotemporal signals of physical phenomena, such as time-series images of fluid dynamics. However, a major limitation of standard diffusion models is that they do not incorporate constraints derived from the underlying physical laws. Consequently, generated samples may appear visually plausible while deviating substantially from the true dynamics. In this study, we propose a simple yet effective physics-informed approach based on diffusion guidance with self-generated data augmentation. The proposed method learns the data distribution conditioned on the degree of deviation from the physically correct dynamics and generates samples by explicitly setting the deviation condition to be zero. The method decouples the evaluation of the governing equations from the diffusion model training and sampling processes, avoiding the need to solve the governing equations at every iteration of the denoising process. This design makes the method applicable to problems requiring computationally expensive numerical simulations and enables faster sample generation. Experimental results demonstrate that the proposed model not only significantly reduces the deviations compared with standard diffusion models but also achieves further reductions when combined with existing physics-constrained diffusion methods.

---


### 96. [Letters hide the truth from our eyes: English homophones have meaningfully different phonetic realizations](https://arxiv.org/abs/2608.26749)

**<font color=#1a73e8>作者：</font>** Yu-Hsiang Tseng, Mirjam T. C. Ernestus, Louis F. M. ten Bosch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The distribution of spoken word duration of English homophones is known to co-vary with frequency of use. This study investigates whether other aspects of the phonetic realization of homophones also differ. A series of quantitative investigations of 14,000 homophone tokens in American television news broadcasts revealed that the tokens of homophone pairs such as \textit{weight} and \textit{wait} have different phonetic realizations, and that these can be predicted from their meanings in utterance context. These systematic differences remain even when taking duration-related variation into account. Time-normalized spectrograms emerged as an excellent tool for probing the fine details of phonetic realization, and obviate the need for phonetic transcriptions, which inevitably hide the phonetic truth from our eyes.

---


### 97. [Glass Surface Detection Grounded in 3D Visual Geometry](https://arxiv.org/abs/2608.26752)

**<font color=#1a73e8>作者：</font>** Yiwei Lu, Ke Xu, Tao Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Glass surface detection (GSD) is critical for scene understanding and reconstruction, and yet remains challenging due to the transparency and reflectivity of glass surfaces. Existing GSD methods typically rely on 2D appearance cues, which may fail in geometrically ambiguous scenes. In this paper, we propose a paradigm shift: grounding GSD in 3D visual geometry to explicitly model the physical existence of glass surfaces. Our method first distills rich 3D priors from the visual geometry grounded transformer (VGGT) and generates glass-aware 3D representations. It then exploits multi-tasking learning with a novel glass detection head, consisting of two core modules: a Frequency Self-Attention Module (FSAM) that identifies glass-specific spectral features for glass surface localization, and a Geometry Grounding Block (GeGB) that selectively grounds 2D features in 3D geometry for glass surface segmentation. Extensive experiments demonstrate that our method achieves state-of-the-art performance across seven standard GSD benchmarks, generalizes well to video/multi-modal data, and substantially improves reconstruction in glass scenes. Code is available in this https URL.

---


### 98. [Safety by Design: Realized-Cost Constraints for Contextual Bandits with Continuous Actions](https://arxiv.org/abs/2608.26755)

**<font color=#1a73e8>作者：</font>** Spyros Dragazis, Aldo Pacchiano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual bandits are a standard framework for sequential decision-making under uncertainty, with applications in clinical trials, dosage selection, recommendation systems, and autonomous systems. Safety is central in many of these applications, since a single unsafe decision in settings such as dosage selection or autonomous driving can have catastrophic consequences. A common way to model safety in bandit problems is to associate each action with both a reward signal and a cost signal, and to optimize reward subject to constraints on cost. Most existing safety-constrained bandit models enforce safety by requiring the expected cost of each action to remain below a prescribed threshold. However, this may be insufficient in heteroscedastic settings, where the chosen action affects not only the expected reward and cost, but also the variability of the observed outcomes. We study contextual bandits with one-dimensional continuous actions and stage-wise high-probability constraints on the realized cost. We propose High-Probability Constrained UCB, an optimistic-pessimistic algorithm that explores for reward while conservatively estimating the safe action set. For linear reward and cost models, we prove a tight $\tilde{\mathcal{O}}(d\sqrt{T})$ regret bound, and we extend the analysis to general function classes using the eluder dimension. Experiments show that enforcing realized-cost safety substantially reduces violations compared with expected-cost constrained baselines.

---


### 99. [Fixed-Haven Reservation for Online Multi-Agent Pickup and Delivery in Dense Warehouses](https://arxiv.org/abs/2608.26759)

**<font color=#1a73e8>作者：</font>** Taisei Hirayama, Kohei Yoshida, Hiroki Sakaji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Dense warehouses often contain single-lane aisles, dead ends, and tree-like guidepaths that leave little room for idle agents to wait without blocking others. Existing Multi-Agent Pickup and Delivery (MAPD) guarantees for completing all finitely released tasks typically rely on extra waiting endpoints that planned paths can avoid, or on biconnected topology; these assumptions may fail in such layouts. We study fixed-Haven reservation for online MAPD, where pickup-delivery tasks are released over time. Each agent owns a fixed Safe Haven (Haven for short), usually its start cell, that only the owner may occupy and that other agents treat as blocked. For finite task releases, we prove that this fixed-Haven contract completes all released tasks under Haven-Reachability and explicit planning/progress assumptions. We implement the contract in SHARP, a Safe-Haven Retreat Planner that keeps every busy or retreating agent on a collision-free reserved route ending at its Haven. We compare SHARP with representative TP and PIBT-family MAPD baselines: Token Passing (TP), Priority Inheritance with Backtracking (PIBT), and PIBT with Temporary Priority and Temporary Avoidance (PIBTTP-TA) for biconnected main areas with attached trees. In the robustness sweep, SHARP is the only method with 100% success on all tested configurations, at substantially higher centralized planning cost on tree-like layouts. A TP-style fixed-home-return counterfactual with full-route validation also recovers robustness on tested tree-like layouts, suggesting that fixed return is a central robustness mechanism there. A no-overwrite variant shows that disabling mid-retreat reassignment worsens service time (release-to-delivery latency) by 1.89 times and makespan by 1.53 times in the tested high-load tree condition.

---


### 100. [Categorizer Automata for Discounted-Sum Payoffs](https://arxiv.org/abs/2608.26763)

**<font color=#1a73e8>作者：</font>** Nathalie Bertrand, Pranav Ghorpade, Senthil Rajasekaran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Categorizing continuous data into discrete bins is a fundamental operation in artificial intelligence. We introduce the categorizer automaton, a deterministic automaton that reads an infinite sequence of rewards and identifies which of finitely many bins contains its discounted sum. Categorizer automata generalize comparator automata, the special case of two bins, which have already proven useful in quantitative synthesis. Our main technical contribution is the construction of a categorizer automaton whose state space is linear in the number of bins, rather than exponential as obtained by a cross-product of comparator automata. We then apply categorizer automata to Markov decision processes, where they allow one to synthesize policies that maximize the expected utility of a discounted-sum payoff for utility functions that may be discontinuous. For piecewise-constant utility functions, the resulting algorithm is exact and runs in pseudo-polynomial time. For piecewise-Lipschitz utility functions, a class that includes any utility with bounded slope between finitely many jumps, it again runs in pseudo-polynomial time and yields an $\varepsilon$-optimal policy. We also show that the synthesis problem considered is PSPACE-hard already for piecewise-constant utilities.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
