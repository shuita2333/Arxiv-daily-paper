# 📦 其他研究 | 2026年06月02日

> 本类共 **317** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-317](./part-07.md)

---

### 51. [AMNESIA: A Large Scale Medical Unlearning Benchmark Suite with Disease-Informed Analysis](https://arxiv.org/abs/2605.30599)

**<font color=#1a73e8>作者：</font>** Saeedeh Davoudi, Reihaneh Iranmanesh, Ophir Frieder 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical knowledge is continuously evolving. This creates a need to update or selectively forget information encoded in already-trained medical LLMs. Machine unlearning aims to remove the influence of specific training data from a model without full retraining. Yet, existing unlearning benchmarks rely on synthetic or small-scale general data, leaving clinical unlearning understudied. We introduce AMNESIA, the first large-scale, open source benchmark for medical unlearning, with 70,560 question-answer pairs from 8,820 patient notes across 11 disease categories. AMNESIA includes both factual questions testing direct recall and reasoning questions testing clinical inference. We use it to evaluate four widely used unlearning methods at both random patient and disease-level, and introduce a new metric for detecting leakage of medical terminology. We show that unlearning individual patients erodes knowledge of others with the same condition, calling for methods that can better separate patients from shared clinical knowledge.

---


### 52. [The Fast Mixing Mechanism for Differential Privacy](https://arxiv.org/abs/2605.30600)

**<font color=#1a73e8>作者：</font>** Omri Lev, Moshe Shenfeld, Vishwak Srinivasan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized sketching is a central tool for compressing large-scale optimization problems while preserving accuracy. In particular, sketches that are based on structured matrices, such as the Hadamard matrix, can be applied efficiently and often yield solutions that approximate those of the original problem at much lower computational cost. In differential privacy (DP), Gaussian sketching has been used to solve DP linear regression, beginning with \citet{sheffet2017differentially, sheffet2019old} and later refined by \citet{lev2025gaussianmix, lev2026near}. However, although these methods achieve strong utility guarantees, they usually do not improve runtime over classical DP approaches. In this work, we introduce a new DP sketching mechanism based on fast transforms, which, in certain cases, matches the runtime of classical fast sketching methods. We prove state-of-the-art privacy guarantees for this mechanism and show that, in favorable regimes, they match those of the Gaussian sketch up to a constant factor. As an application, we combine this mechanism with recent sketch-based methods for DP linear regression to obtain a new algorithm with strong utility and improved runtime. We establish privacy and accuracy guarantees for this algorithm, yielding, to the best of our knowledge, the first fast method for DP ordinary least squares.

---


### 53. [TASER: Task-Aware Stein Regularisation for Geometry-Driven Robustness](https://arxiv.org/abs/2605.30601)

**<font color=#1a73e8>作者：</font>** Michał Kozyra, Gesine Reinert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep networks remain fragile under distribution shift and adversarial perturbations, often due to excessive or poorly structured input sensitivity. We introduce TASER (Task-Aware Stein Regularisation), a training-time regularisation framework derived from Langevin Stein operators. By penalising pointwise Stein residuals under the training distribution, TASER encourages geometric compatibility between predictors and data density, inducing anisotropic, data-aware smoothness. We provide theoretical links between Stein regularisation and reduced first-order shift sensitivity, develop scalable implementation variants compatible with modern architectures, and demonstrate improved robustness and stability across regression and vision benchmarks. Across CIFAR-10 experiments, TASER consistently improves the adversarial robustness of established training methods without incurring statistically significant clean-accuracy degradation.

---


### 54. [Semantic Motion Anchors: Bridging Motion and Meaning in Co-Speech Gestures](https://arxiv.org/abs/2605.30608)

**<font color=#1a73e8>作者：</font>** Varsha Suresh, Mohammad Mahdi Abootorabi, Mohamed Salman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Learning a shared representation between spoken text and gesture is central to co-speech gesture retrieval, synthesis, and understanding, but remains challenging for semantically meaningful gestures whose communicative intent is not captured by motion alone. Direct contrastive alignment between transcripts and continuous motion embeddings often overemphasizes low-level kinematics and misses the symbolic content of semantic gestures. We propose semantic motion anchors, natural-language abstractions of gesture motion capturing physical form and communicative intent. Our method discretizes 3D gestures into body-hand motion primitives, verbalizes them into structured descriptions, and grounds them in the transcript to provide auxiliary contrastive supervision. On BEAT2, our method improves text-to-gesture R@1 by 8.2% over a direct text-motion baseline and outperforms prior retrieval approaches on text to gesture and gesture to text retrieval directions. Beyond aggregate retrieval metrics, semantic motion anchor supervision helps retrieve gestures that are semantically meaningful for the spoken query, rather than defaulting to generic motion patterns. A downstream retrieval-augmented gesture generation study showed that users significantly preferred gestures retrieved by our approach over a retrieval-augmented generation baseline, demonstrating that semantically grounded retrieval translates to gestures that better convey communicative intent in downstream generation.

---


### 55. [Constrained Flow Optimization via Sequential Fine Tuning for Molecular Design](https://arxiv.org/abs/2605.30610)

**<font color=#1a73e8>作者：</font>** Sven Gutjahr, Riccardo De Santi, Luca Schaufelberger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting generative foundation models, in particular diffusion and flow models, to optimize given reward functions (e.g., binding affinity) while satisfying constraints (e.g., molecular synthesizability) is fundamental for their adoption in real-world scientific discovery applications such as molecular design or protein engineering. While recent works have introduced scalable methods for reward-guided fine-tuning of such models via reinforcement learning and control schemes, it remains an open problem how to algorithmically trade-off reward maximization and constraint satisfaction in a reliable and predictable manner. Motivated by this challenge, we first present a rigorous framework for Constrained Generative Optimization, which brings an optimization viewpoint to the introduced adaptation problem and retrieves the relevant task of constrained generation as a sub-case. Then, we introduce Constrained Flow Optimization (CFO), an algorithm that automatically and provably balances reward maximization and constraint satisfaction by reducing the original problem to sequential fine-tuning via established, scalable methods. We provide convergence guarantees for constrained generative optimization and constrained generation via CFO. Ultimately, we present an experimental evaluation of CFO on both synthetic, yet illustrative, settings, and a molecular design task. Across these evaluations, CFO achieves consistent increases in reward while ensuring high constraint satisfaction, showcasing its practical utility for constrained generative optimization.

---


### 56. [Crafter: A Multi-Agent Harness for Editable Scientific Figure Generation from Diverse Inputs](https://arxiv.org/abs/2605.30611)

**<font color=#1a73e8>作者：</font>** Haozhe Zhao, Shuzheng Si, Zhenhailong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific figures are among the most effective means of communicating complex research ideas, yet producing publication-quality illustrations remains one of the most labor-intensive parts of paper preparation. Existing automated systems each target a single figure type under text-only input, leaving the diversity of types and conditions researchers actually use unaddressed; their raster outputs further cannot be locally revised. Because scientific figures are structured compositions of discrete semantic components, the localized errors generators produce on such layouts demand not a stronger backbone but a harness. We instantiate this harness in two complementary systems: Crafter, a multi-agent harness for figure generation that generalizes across figure types and input conditions without architectural changes, and CraftEditor, which applies the same pattern to convert raster outputs into editable SVGs. Moreover, we introduce CraftBench, a benchmark spanning three figure types and four input conditions with human quality annotation. Experiments show that Crafter substantially outperforms both standalone generators and the agentic baseline on PaperBanana-Bench and CraftBench, with ablations confirming each component's independent contribution; CraftEditor faithfully converts outputs into editable SVGs that surpass all baselines. Our code and benchmark are available at this https URL.

---


### 57. [CacheProbe: Auditing Prompt Cache Isolation in Gateway APIs](https://arxiv.org/abs/2605.30613)

**<font color=#1a73e8>作者：</font>** Ryan Fahey  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Over the past year, prompt caching in Large Language Models (LLMs) has become increasingly more popular across inference APIs. Prompt caching helps save precious compute resources and speeds up response times by reusing parts of the KV cache of a specific prompt for another request. However, many implementations of prompt caching are not secure against timing attacks or even basic metadata disclosure. Gu et al. (ICML 2025) develop a method to audit prompt caching in LLMs. This paper investigates whether OpenRouter's API gateway architecture introduces prompt caching vulnerabilities that bypass provider-level prompt cache isolation guarantees. Most LLM inference providers implement per-account or per-organization prompt caching to prevent data leaks, but does routing through OpenRouter with shared organizational credentials inadvertently create global cache sharing across all OpenRouter users?

---


### 58. [Audio Pirates: Black-box Audio Watermark Removal via Diffusion Priors](https://arxiv.org/abs/2605.30614)

**<font color=#1a73e8>作者：</font>** Lingfeng Yao, Xincong Zhong, Chenpei Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rise of AI-generated audio, watermarking has become widely used for detecting misuse and protecting intellectual property. However, adversaries may try to remove these watermarks, making it critical to evaluate how well watermarking schemes withstand removal attacks. Existing attacks are often impractical: they either noticeably degrade perceptual quality or require access to the watermarking scheme. We propose DiffErase, a black-box watermark removal attack that assumes no knowledge of the target watermarking scheme while maintaining perceptual quality. DiffErase perturbs watermarked audio to an intermediate diffusion noise level and regenerates it using a pretrained denoising model, effectively suppressing watermark signals. Theoretical analysis and extensive experiments demonstrate that inaudible audio watermarks are highly vulnerable: across multiple audio domains, DiffErase consistently removes watermarks while preserving perceptual quality. These findings highlight the need for future audio watermarking designs to consider diffusion-based threats. Code and demos are available at this https URL.

---


### 59. [Improving Selective Classification with Pairwise Queries for Binary Classification](https://arxiv.org/abs/2605.30615)

**<font color=#1a73e8>作者：</font>** Harsh Vardhan, Sunav Choudhary, Natwar Modani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In selective classification, a model predicts the labels of data samples where it is confident, and abstains from predicting labels for samples on which it is not confident. The rejected samples are often labeled by an expert, which is expensive. The budget for the expert is best utilized when the model has low error on non-rejected samples. However, the estimate of a model's confidence might be inconsistent with the model's predictions, which can lead to high error on non-rejected points. Such situations can readily occur in in-context binary classification by LLMs. To remedy this, we propose making additional pairwise queries to the same model. These pairwise queries can detect high-error samples and be incorporated into selective classification techniques to reduce the error on non-rejected samples. Theoretically, we establish the conditions under which a simple algorithm using pairwise queries outperforms an inconsistent confidence estimate. We support this insight through extensive experiments for $1$ synthetic and $4$ in-context learning-based real binary classification datasets. In all these cases, we show that our algorithms, using pairwise queries, obtain a better accuracy-cost tradeoff than using only the raw confidence estimates, for instance, the LLM's next-token logits.

---


### 60. [Active Timepoint Selection for Learning Measure-Valued Trajectories](https://arxiv.org/abs/2605.30625)

**<font color=#1a73e8>作者：</font>** Nicolas Huynh, Mihaela van der Schaar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring continuous probability paths from sparse snapshots is a fundamental challenge in domains like single-cell biology, where high-fidelity data acquisition is often destructive and constrained by prohibitive sequencing costs. This motivates the need for active learning strategies to strategically select optimal measurement times. However, designing active learning policies for this setting remains an open problem: the target objects reside on the infinite dimensional Wasserstein space where standard Euclidean metrics are ill-defined, and current interpolation methods lack epistemic uncertainty quantification. We introduce a framework which extends active experimentation to the space of measures. By leveraging Linearized Optimal Transport (LOT), we map distributional snapshots into a tangent space amenable to Gaussian Process modeling, allowing us to construct a tractable probabilistic surrogate for the underlying probability path. This yields an acquisition policy that iteratively selects measurement times to minimize uncertainty. Empirical results demonstrate that our strategy outperforms uncertainty-agnostic baselines on both synthetic and real-world datasets.

---


### 61. [Controllable Lung Nodule Synthesis via Histogram-Regularized Latent Diffusion Models](https://arxiv.org/abs/2605.30631)

**<font color=#1a73e8>作者：</font>** Arunkumar Kannan, Yanbo Zhang, Han Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While automated diagnosis systems have achieved remarkable success in computed tomography (CT)-based lung cancer screening, their development remains limited by the scarcity of diverse, annotated pulmonary nodule datasets. Diffusion-based generative models offer a promising strategy for data synthesis; however, many existing conditional approaches primarily optimize spatial reconstruction losses, which encourage voxel-wise similarity but may inadequately constrain lesion-level intensity distributions. As a result, these methods may produce over-smoothed texture profiles and underrepresent the distinct attenuation characteristics of different nodule subtypes, including solid, part-solid, and ground-glass nodules. To address this challenge, we propose a controllable latent diffusion model that synthesizes pulmonary nodules within full 3D CT volumes while accurately modeling nodule-specific intensity distributions. Specifically, rather than relying solely on spatial losses, we introduce a histogram-based regularization term that constrains voxel intensity distributions during the generative process. The model combines subtype, spatial mask, and Hounsfield unit (HU) histogram conditioning with the differentiable feature-space histogram regularization term to better align lesion-level intensity distributions, improving the visual plausibility and subtype consistency of synthesized nodules. Extensive experiments on lung CT data demonstrate that our framework achieves strong visual realism, validated through both quantitative metrics and a visual Turing test. Furthermore, when used for data augmentation, the generated nodules improve performance in downstream clinical tasks, particularly for underrepresented nodule subtypes, and show a potential benefit for subtype-informed malignancy classification.

---


### 62. [Score Broadcast and Decorrelation: A General Framework for Broadcast-Based Credit Assignment](https://arxiv.org/abs/2605.30638)

**<font color=#1a73e8>作者：</font>** Mustafa Uzun, Mete Erdogan, Cengiz Pehlevan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Score Broadcast and Decorrelation (SBD), a principled framework for broadcast-based credit assignment for general families of differentiable losses. Error broadcast is a biologically plausible alternative to backpropagation that sends output information to hidden layers without weight transport. The Error Broadcast and Decorrelation (EBD) framework, recently introduced for the mean-squared-error (MSE) setting, grounded this mechanism in the stochastic orthogonality of optimal estimators, under which the optimal residual is orthogonal to functions of the input. We generalize that foundation by introducing an orthogonality principle between the output score (the gradient of loss with respect to the final-layer output) and hidden-layer activations, which holds whenever the optimal score has conditional mean zero. This single principle unifies broadcast-based credit assignment across the standard differentiable-loss families, including cross-entropy, Bregman divergences, proper scoring rules, and exponential-family negative log-likelihoods. The framework supplies a theoretical grounding for the three-factor learning rule under general losses, with the neuromodulatory factor derived as the broadcast loss score. We derive the cross-entropy case explicitly, characterize the admissible loss class, and introduce a score vector expansion technique that enriches the broadcast signal while preserving the orthogonality framework. Experiments on CIFAR-10 and Tiny ImageNet show that SBD substantially improves over existing broadcast approaches, with score vector expansion delivering further gains. Overall, this work identifies the loss score as the signal to broadcast, supplies the orthogonality theory and theoretical grounding for the three-factor learning rule from neuroscience, and shows how score vector expansion enriches the decorrelation directions of the resulting objective.

---


### 63. [CSULoRA: Closest Safe Update Low-Rank Adaptation](https://arxiv.org/abs/2605.30640)

**<font color=#1a73e8>作者：</font>** Oleksandr Marchenko Breneur, Adelaide Danilov, Aria Nourbakhsh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation has become a standard method for parameter-efficient fine-tuning of large language models, but even small amounts of unsafe or adversarial fine-tuning data can substantially weaken the safety behavior of aligned models. Existing safety-preserving LoRA methods often rely on hard interventions such as projection, pruning, thresholding, or additional training objectives. While these methods can suppress unsafe update directions, they may also remove task-relevant information or require extra tuning. We introduce CSULoRA, a post-hoc method for correcting trained LoRA adapters through closest safe update estimation. CSULoRA estimates a safety-aligned subspace from the weight displacement between a safety-aligned model and its corresponding base checkpoint. It then decomposes each LoRA update into fully aligned, partially aligned, and off-subspace components. Instead of discarding components outside the estimated safety subspace, CSULoRA solves a closed-form penalized minimum-change problem that preserves the fully aligned component while smoothly attenuating potentially unsafe directions according to their relative energy. In adversarial fine-tuning experiments, CSULoRA substantially reduces attack success rate while preserving most of the utility gains obtained from standard LoRA fine-tuning.

---


### 64. [Diffusion Models Preferentially Memorize Prototypical Examples or: Why Does My Diffusion Model Love Slop?](https://arxiv.org/abs/2605.30642)

**<font color=#1a73e8>作者：</font>** Marta Aparicio Rodriguez, Anastasia Borovykh, Grigorios A. Pavliotis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models have a persistent limitation: their tendency to memorize training data can create legal liabilities and erode creative diversity. Understanding which samples are memorized in whole or in part, and under what conditions, therefore remains an important open problem. Here we answer the question "Are atypical or rare samples memorized first?" in the negative. We train diffusion models on strings generated according to the production rules of the Random Hierarchy Model (RHM), and find that samples composed of common substrings are preferentially memorized. This holds true even if the training data consists of entirely unique samples, indicating that deduplication at the data point level does not provide a meaningful privacy guarantee. Correspondingly we predict, then observe, delayed memorization for fat-tailed datasets (i.e., those with more atypical samples). This effect is amplified when fat-tails are introduced into high-level production rules. These together suggest that dataset diversity, particularly at higher levels of abstraction, plays an important role in staving off memorization. Finally, we identify an intermediate regime of partial memorization in which common substrings are learned first and subsequently overproduced during generation. If training is stopped in this regime, models will exhibit the reversion-to-the-mean blandness often derided as "slop".

---


### 65. [Convergence of Steepest Descent and Adam under Non-Uniform Smoothness](https://arxiv.org/abs/2605.30648)

**<font color=#1a73e8>作者：</font>** Sharan Vaswani, Yifan Sun, Reza Babanezhad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has analyzed the convergence of first-order methods under non-uniform smoothness assumptions that better model the loss landscape in machine learning tasks. We generalize this assumption to objectives whose curvature is an affine function of the objective value. This property is satisfied by a broad class of problems, including logistic regression, generalized linear models with a logistic link function, softmax policy gradient in reinforcement learning, and a class of neural networks. Under this assumption and gradient domination conditions, we establish a general convergence rate for the steepest descent method, and deterministic, diagonal variants of RMSProp and Adam. Our results imply that for logistic regression on separable data and the softmax policy gradient objective, sign GD converges linearly and is provably faster than GD. Furthermore, we show that for a class of two-layer neural networks on separable data, RMSProp and Adam can converge at a linear rate with a constant step-size and momentum parameter. Finally, we present a lower bound demonstrating that, under our assumption, RMSProp and Adam are provably faster than AdaGrad, AMSGrad, gradient descent, and heavy-ball momentum.

---


### 66. [When AI Meets Wall Street: A Survey on Trustworthy AI in Fintech](https://arxiv.org/abs/2605.30650)

**<font color=#1a73e8>作者：</font>** Qingwen Zeng, Zhenghao Zhao, Yitian Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is now embedded as a primary decision engine in continuously operated financial AI pipelines spanning training and updating, deployment and inference, and operation with monitoring and feedback. The automation and scale that make these pipelines effective also create novel attack surfaces, where small algorithmic perturbations can amplify into persistent, system-level financial harm. Existing surveys, however, either treat AI as a defensive tool or analyse adversarial machine learning in a domain-agnostic manner, abstracting away finance-specific constraints such as accounting plausibility, non-IID federated data, continuous retraining, and automation-amplified downstream effects. We address this gap with a unified, lifecycle-centric and mechanism-driven framework. We partition financial AI into three lifecycle stages: training and updating, deployment and inference, and operation, monitoring, and feedback. We further propose the Financial AI Security and Robustness Taxonomy, organising seventeen attack subtypes across data and model poisoning, adversarial attacks on decision boundaries, prompt injection in LLM-mediated workflows, and deepfake-driven subversion of KYC verification layers. For each subtype, we analyse algorithmic strategy, feasibility constraints, stealth and persistence, and downstream financial consequences. Finally, we identify open challenges and outline a research agenda toward lifecycle-aware stress testing and finance-relevant robustness benchmarks.

---


### 67. [LARK: Learnability-Grounded Trajectory Selection for Efficient Reasoning Distillation](https://arxiv.org/abs/2605.30651)

**<font color=#1a73e8>作者：</font>** Tianrun Yu, Kaixiang Zhao, Chih-Chun Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study trajectory selection for reasoning distillation, where teacher-generated reasoning trajectories are selectively used as supervision for a student model. Existing methods rely on heuristics such as trajectory quality or model confidence, but they often overlook whether a trajectory is learnable by the student. In this paper, we present LARK, a learnability-grounded method for reasoning trajectory selection. LARK selects trajectories that the student can learn efficiently while preserving the generalization of the full training distribution. At the core of LARK is a learnability factor $\rho$, which characterizes the rate at which the student's training loss decreases. To estimate this rate efficiently and maintain generalization, we introduce a learnability proxy and a $\chi^2$-regularized selection policy that balances learnability and distributional coverage, both with strong theoretical guarantees on their estimation error. Empirically, LARK consistently outperforms data selection baselines across multiple base models and reasoning tasks. Diagnostic analyses show that the LARK score predicts downstream training utility and that LARK-selected trajectories induce faster supervised fine-tuning loss reduction. Our code is available at this https URL.

---


### 68. [Bridging the Gap Between Natural Language and Market Dynamics via High-Dimensional Representation Learning](https://arxiv.org/abs/2605.30652)

**<font color=#1a73e8>作者：</font>** Yujin Jeong, Noelle Jung, Brian Y. C. Leung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional multi-modal financial forecasting often relies on scalar sentiment scores, which fail to capture the nuances of financial news. To address this information loss, this paper explores high-dimensional representation learning by replacing discrete polarity ratings with dense FinBERT embeddings within a Transformer-based forecasting architecture. We benchmarked various embedding strategies on the FNSPID dataset, including raw embeddings, attention-weighted aggregation, and a custom Siamese network. While the attention-based mechanism struggled with the low signal-to-noise ratio typical of financial data, the integration of Siamese-optimized embeddings outperformed both the scalar baseline and raw embedding approaches, demonstrating that preserving high-dimensional narrative context yields improved predictive accuracy for short-term stock price movements.

---


### 69. [Learning to Perceive the World Through Control: Empowerment-Based Representation Learning](https://arxiv.org/abs/2605.30656)

**<font color=#1a73e8>作者：</font>** Mahsa Bastankhah, Sophie Broderick, Benjamin Eysenbach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many practical reinforcement learning environments, observations are far higher-dimensional than the variables that matter for control. In this work, we ask: can we learn representations that capture only control-relevant features of the environment? We study this question through the empowerment objective, which maximizes an agent's influence over the environment and is widely used for unsupervised skill learning. We show that empowerment agents induce two distinct representations -- forward and backward -- that capture complementary aspects of the state, and both of which are invariant to control-irrelevant features. Thus, empowerment maximization leads agents to learn an implicit, control-centric model of the world. Our analysis highlights the importance of learning representations through interaction rather than from passive datasets: interaction aimed at maximizing control is essential for learning useful invariance properties, a perspective that aligns closely with the causal learning literature.

---


### 70. [BOKBO (Best of K Bad Options): Calibrated Abstention for VLA Policies](https://arxiv.org/abs/2605.30660)

**<font color=#1a73e8>作者：</font>** Anya Singh, Cabrel Happi, Jai Relan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling for vision-language-action (VLA) policies, methods such as RoboMonkey, SEAL, MG-Select, and V-GPS, samples K candidate action chunks at inference and executes the verifier-best. When all K candidates are unsafe, the system executes a violating action with no warning. We propose BOKBO, the first conformal abstention layer for K-sample VLA inference, providing finite-sample distribution-free guarantees on executed-violation rate. We provide both global and per-task (Mondrian) variants, with the per-task variant closing the conditional gap on the hardest tasks.
Our analysis exposes a structural failure of policy-internal nonconformity scores under perturbation-based K-sampling: the base-policy confidence proxy and K-sample disagreement correlate at 0.98 with the action-noise hyperparameter $\sigma$, while correlating at the noise floor with actual safety violations. We test the failure's scope by replicating the analysis under token-level temperature sampling and find the failure is mechanism-specific and partially mitigated under policy-stochasticity-based sampling. A learned violation predictor conditioned on semantic visual features and task identity supports tight calibration: at $\epsilon$ = 0.05 on libero_object_temp_x0.1 with OpenVLA-OFT, the conditional CRC bound holds on 86% of bootstrap splits with 78% coverage and 70% net task success. Mondrian-BOKBO raises the minimum per-task conditional hold fraction from 0.71 to 0.93. Results are stable across 5 training seeds, replicate within bootstrap noise on $\pi_0$-FAST, hold on libero_spatial_temp_x0.1 as a co-equal benchmark, and survive four within-suite distribution shifts. We additionally identify and correct a methodological pitfall: globally-set force thresholds well below expert-typical manipulation forces conflate unsafe behavior with normal manipulation, inflating violation rates by $5\times$.

---


### 71. [Spatio-temporal stochastic graph-based learning for infectious disease forecasting](https://arxiv.org/abs/2605.30662)

**<font color=#1a73e8>作者：</font>** Luz Stefani Sotomayor Valenzuela, Susanna Cramb, Darren Wraith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal graph-based models have typically been used to forecast new cases of infectious diseases such as COVID-19 and chickenpox outbreaks. However, the use of stochastic modelling into their learning process has been surprisingly under-investigated and rarely considered entire data sets of large countries. As a result, it is unknown whether these models would provide accurate forecasts in real-world disease spread scenarios. In this work, we propose a spatio-temporal stochastic graph-based architecture that integrates a stochastic formulation and uncertainty approximation process to forecast new infectious disease cases. We find that our approach can adapt to encode large and small population geographical networks within a single model architecture. Using two real-world data sets, COVID-19 in the US and chickenpox in Hungary, we report an enhanced effect of the proposed architecture across predictions of the 2022 first wave for COVID-19 in the US and comparative results of chickenpox waves during 2012-2014 in Hungary. By benchmarking with four spatio-temporal graph-based models, quantitative results show competitive overall weekly performance of the proposed approach on forecasting new cases for all 3,218 US counties and all 20 Hungary counties. The proposed approach can represent overall epidemic progression relative to baselines, though with a one-step delay; while exhibiting a reduced sensitivity to high-frequency and low-amplitude variability.

---


### 72. [Structure-Induced Information for Rerooting Levin Tree Search](https://arxiv.org/abs/2605.30664)

**<font color=#1a73e8>作者：</font>** Jake Tuero, Michael Buro, Laurent Orseau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Subgoal-based policy tree search, which uses a policy to guide search, is effective for complex single-agent deterministic problems but often relies on explicit subgoal generation that can incur substantial overhead and hinders scalability. In this paper, we overcome these limitations by using a learned ``rerooter'' through the recently-introduced $\sqrt{\text{LTS}}$ algorithm. A rerooter implicitly decomposes the problem into soft subtasks. While previous work focused on the formal guarantees for given or handcrafted rerooters, in this work we propose three rerooter designs: (i) a clustering-based rerooter that exploits global state-space structure, (ii) a heuristic-based rerooter that leverages learned cost-to-go estimates, and (iii) a hybrid that combines both signals. Our framework avoids having to explicitly reconstruct and reason over generated subgoals, thereby enabling scalable allocation of search effort with significantly lower computational overhead. Empirically, our rerooting-based methods scale to complex environments where subgoal-based policy tree search fails, and achieve state-of-the-art online training efficiency on the domains tested.

---


### 73. [CobSeg: Coherence Boundary Modeling for Dialogue Topic Segmentation](https://arxiv.org/abs/2605.30668)

**<font color=#1a73e8>作者：</font>** Sijin Sun, Liangbin Zhao, Jiaxiang Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialogue topic segmentation is critical in many human-AI collaborative applications which requires identifying heterogeneous boundary cues, including lexical transitions near utterance edges and semantic discontinuities across utterances. Existing utterance models often dilute these local lexical signals. We propose CobSeg, a novel multi-branch architecture that separates coherence-level semantic continuity from lexical boundary transitions and recovers both through directional boundary prediction. CobSeg further uses boundary informativeness weighting to emphasize high-utility utterance positions, and incorporates a corpus-derived topic coherence cue with learned combination weights. While CobSeg is evaluated as a compact trainable segmenter under supervised gold-boundary training and a pseudo-label setting with automatically induced boundaries, it performs enhanced boundary prediction without LLM calls during inference. Across five benchmarks, it improves $P_k$ and $W_d$ particularly when local lexical cues are prominent: under gold supervision, it reduces $P_k$ by 0.7 points and $W_d$ by 0.6 points on VHF, and reaches $P_k$ of 1.0 on DialSeg711; with induced boundaries, it reduces $P_k$ by 14.8 points on VHF, by 1.5 points on DialSeg711, and by 1.1 points on TIAGE, outperforming prior non-LLM approaches.

---


### 74. [WristCompass: Kinematic Coupling as a Learnable Visual Concept for Ego-Camera Orientation](https://arxiv.org/abs/2605.30671)

**<font color=#1a73e8>作者：</font>** Varun Nair, Vidyut Baradwaj, Jiahang He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering ego-camera orientation from manipulation video is a prerequisite for disentangling hand motion from camera motion, a key step in imitation learning from egocentric demonstrations. The obvious approach, inferring orientation from scene geometry, fails when hands occlude the frame: VGGT, a 1B-parameter scene reconstruction model, scores worse than a constant predictor on the TACO benchmark. We identify an alternative visual concept that is present precisely when scene geometry is absent: kinematic coupling dynamics, the structured physical relationship between wrist motion and camera orientation imposed by the arm-shoulder-head chain. We find that this concept is compact (4D inter-wrist features outperform 126D full hand keypoints), temporal (requiring a GRU over short windows rather than per-frame retrieval), and physically grounded (transferring zero-shot across datasets because it is rooted in anatomy rather than scene appearance). Trained only on tabletop manipulation, WristCompass transfers zero-shot to Epic Kitchens cooking video, achieving 14.3$^\circ$ median geodesic error and approaching the performance of a 1B-parameter scene model at 200K GRU parameters.

---


### 75. [Investigating Detection and Obfuscation of Prompt Injection Attacks Against Software Reverse Engineering AI Agents](https://arxiv.org/abs/2605.30677)

**<font color=#1a73e8>作者：</font>** Brian Crawford, Patrick McClure  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic software reverse engineering systems are vulnerable to prompt injection attacks placed into the source code of executable binary files. This research demonstrates defensive tactics for detecting the presences of prompt injection strings in the decompiler output of adversarial example programs. Methods for obfuscating these attacks and subsequent methods for defending against these obfuscations are also explored. This research advances the understanding of risk and security of agentic software analysis systems necessary for their deployment into production-level cyber workflows.

---


### 76. [Healthcare Mechanisms from Policy-as-Code Search under Strategic Provider Response](https://arxiv.org/abs/2605.30680)

**<font color=#1a73e8>作者：</font>** Zihan Wang, Xiang Xu, Hongyuan Zha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare mechanisms are inseparable from the strategic provider response they induce: existing healthcare AI benchmarks hold this response fixed and so cannot evaluate mechanisms by the equilibrium they produce. We recast hospital mechanism design as program synthesis for language models: typed, inspectable rule programs are executed and scored by Medi-Sim, a multi-agent simulator with five strategic provider channels (coding, selection, delay, effort, triage). An incentive sweep recovers classical health-economics findings as adjacent regimes -- up-coding and low-complexity-patient selection under profit pressure, and Goodhart-style drift where measured performance becomes anti-correlated with true outcomes -- and a single audit lever exposes pressure migration: closing the coding channel more than doubles low-complexity selection. LLM-guided evolutionary code search over the same rule-program space then synthesizes an inspectable mixed-objective program that eliminates up-coding, halves rejection, and retains most of the profit-oriented baseline's funds.

---


### 77. [Depth-Dependent Indirect Prompt Injection in Tool-Calling ReAct Agents: Injection Depth, Payload Framing, and Turn-Budget Sensitivity](https://arxiv.org/abs/2605.30686)

**<font color=#1a73e8>作者：</font>** Mohammadreza Rashidi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> ReAct agents that interleave chain-of-thought reasoning with tool calls are increasingly deployed for real tasks such as scheduling, file retrieval, and data access. Their tool observation loop creates a direct attack surface: an adversary who controls any tool's return value can embed instructions that redirect the agent away from the user's goal, a threat known as indirect prompt injection. Existing benchmarks evaluate attack success rate (ASR) at a fixed injection position under fixed conditions, leaving three risk dimensions unexplored: where in the tool sequence the payload appears (injection depth), what rhetorical register it uses (framing), and how many turns the agent is permitted (turn cap). We conduct four controlled studies on 20 scenarios spanning five attack categories, totalling 460 trials against GPT-4o-mini and Claude Haiku at a combined API cost under 0.36 USD. Study 1 shows that ASR against GPT-4o-mini decays from 60% at depth 1 to 0% at depths 4 and 5 (Cramer's V = 0.58, p < 0.001; restricted to within-sequence depths 1-3: V = 0.47, p = 0.0013), driven by model resistance at depth 1 and task completion before payload encounter at deeper positions. Study 2 replicates the depth experiment on Claude Haiku, which achieves 0% ASR at every depth through a combination of conservative tool invocation and genuine instruction resistance. Study 3 shows that framing modulates ASR between 25% (neutral) and 75% (persona) at depth 1, a 50-percentage-point range that does not reach statistical significance at N = 20 per condition. Study 4 confirms that ASR is stable across turn caps of 3, 5, and 7, indicating the turn budget is not a risk factor in this setting. Our results establish injection depth as the dominant variable and show that sanitising only the first tool observation captures 67% of measured injection successes.

---


### 78. [ConTrans: Learning Text-enhanced Local-global Temporal Representations for Zero-shot Temporal Action Localization](https://arxiv.org/abs/2605.30689)

**<font color=#1a73e8>作者：</font>** Kanchan Keisham, Thenukan Pathmanathan, Thangarajah Akilan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot Temporal Action Localization (ZS-TAL) aims to detect and locate previously unseen actions in untrimmed videos. However, existing approaches primarily focus on modeling long-range contextual information, often neglecting the critical relative-offset-based local correlations between video frames. Furthermore, their performance is hindered by limited feature representation capabilities due to the shallow nature of their network architectures. In this paper, we address these limitations by introducing a novel local-global multi-scale feature representation module. We propose a novel multi-scale encoder architecture, termed ConTrans, that integrates convolutional (Conv) inductive biases with transformer Self-attention to jointly capture fine-grained local dependencies and long-range global context, leading to more comprehensive feature representations than existing methods. Experimental evaluations on the ActivityNet-1.3 and THUMOS14 datasets demonstrate that ConTrans significantly outperforms existing methods, establishing a new benchmark for ZS-TAL.

---


### 79. [Triaging Threats to Specialized Guardrails](https://arxiv.org/abs/2605.30693)

**<font color=#1a73e8>作者：</font>** Wenjie Jacky Mo, Xiaofei Wen, Rui Cai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Building robust safety guardrails is essential for deploying Large Language Models across diverse real-world applications. However, this goal remains challenging because safety risks span heterogeneous threat domains, while existing datasets cover only fragmented risk subsets and rely on inconsistent taxonomies. Consequently, it remains unclear whether current guardrails can generalize beyond narrow evaluation settings. To better understand the robustness of guardrail models, we first introduce GuardZoo, a unified human-annotated benchmark with 32,460 samples covering 15 distinct unsafe categories. Evaluation on GuardZoo reveals that monolithic guardrails suffer from task interference: different threat domains require distinct decision boundaries that are difficult to compress into a single model. We therefore propose RouteGuard, a router-expert framework that triages each conversation to specialized expert guardrails for threat-specific detection. Experiments show that RouteGuard improves fine-grained threat detection over strong guardrail baselines, generalizes better under out-of-domain evaluation, and supports flexible modular expansion to emerging threats.

---


### 80. [Universal Decision Learners](https://arxiv.org/abs/2605.30694)

**<font color=#1a73e8>作者：</font>** Sridhar Mahadevan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many theories of decision making -- planning, reinforcement learning, causal intervention, online learning, and game-theoretic equilibrium -- turn local information into globally coherent behavior. This paper proposes a common categorical formulation: a Universal Decision Learner (UDL) extends a partially specified decision functor from observed contexts to new contexts by a pair of universal constructions. Left Kan extensions express rollout, aggregation, and candidate generation; right Kan extensions express consistency, constraint satisfaction, and fixed-point semantics. The central claim is not that every decision problem has the same algorithm, but that many decision formalisms instantiate the same universal problem: extend local behavioral data canonically, then characterize the globally coherent extensions. We give the abstract UDL construction, prove its universal comparison property, define Kan-invariant behavioral equivalence and minimal abstractions, and show how Bellman equations, planning recursions, causal interventions, online regret, and equilibria arise as special cases. The supplementary material develops the reinforcement-learning specialization in more detail.

---


### 81. [FASR: Automated Identification of Unsafe Control Actions in STPA](https://arxiv.org/abs/2605.30697)

**<font color=#1a73e8>作者：</font>** Ian Dardik, Yining She, Sam Procter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The System-Theoretic Process Analysis (STPA) is a well-established hazard analysis technique that has been applied to a wide range of safety-critical systems. Despite its popularity, there is relatively little automation support for STPA, and most of its steps are carried out manually by a human analyst, which can be time consuming and error prone. This paper investigates the potential use of model-based engineering and formal methods to assist human analysts in efficiently and accurately carrying out STPA. The proposed tool, called FASR (Formalizing and Automating STPA with Robustness), enables automated, complete identification of unsafe control actions (UCAs), leveraging recent advances in robustness analysis to identify UCAs as undesirable deviations in the controller's actions. The use of the tool is demonstrated on a case study involving a Braking System Control Unit (BSCU) in an avionics system. As a preliminary exploration of the potential benefits and limitations of the tool, the paper reports on a user study involving nine participants with varying backgrounds in STPA, model-based engineering, and formal methods; the study found that most participants considered the tool a useful aid in identifying UCAs, while suggesting improvements that would make a tool such as FASR usable and applicable to a wider range of systems and analysts.

---


### 82. [A Context-Aware Middleware for Medical Image Based Reports: An approach based on image feature extraction and association rules](https://arxiv.org/abs/2605.30699)

**<font color=#1a73e8>作者：</font>** Erick O. Rodrigues, Jose Viterbo, Aura Conci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work proposes a context-aware middleware for medical workflow organization and efficiency improvement. In hospitals, laboratories and teleradiology companies, each physician or technician is specialized in a specific kind of diagnosis or analysis. Therefore, certain types of medical images are often forwarded to a certain physician or a certain group. This forwarding is time consuming. That is, repeatedly deciding who would be the best physician, whether he is available at a certain moment given a certain context is exhaustive and may be very inefficient. Thus, the proposed middleware has the ability to process and collect data from images analyzed by each medical staff. Based on the collected data and current clinical context, the middleware is able to infer who would be the best fit staff to receive a certain incoming medical image.

---


### 83. [Mathematical Morphology in Machine Learning](https://arxiv.org/abs/2605.30700)

**<font color=#1a73e8>作者：</font>** Erick Oliveira Rodrigues, Aura Conci  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work introduces mathematical morphology-an established visual computing theory-into machine learning to exploit shape and density aspects often overlooked by standard techniques. We propose a fast clustering algorithm based on morphological reconstruction that accurately preserves cluster shapes and density. This scheme offers unique features: an intrinsic sense of maximal clusters, cost-free noise removal, and diverse growth patterns controlled by structuring this http URL, we propose a novel distance metric combining Minkowski and Chebyshev distances, highly efficient for morphological dilations. In $Z^2$ discrete neighbourhood iterations, it is roughly 1.3 times faster than Manhattan and 329.5 times faster than Euclidean distances. When evaluated using a k-Nearest Neighbours (k-NN) classifier across 33 UCI datasets against 14 other distances, our metric achieved above-average accuracies most frequently (26 of 33 cases) and the best overall accuracy in 9 this http URL, we introduce novel morphological classifiers. Unlike current literature, this proposal uniquely models shape, density, and fractal information in datasets.

---


### 84. [Relational Aesthesis in Permacomputing Practice: Building a Solar Powered Website from Reclaimed Materials](https://arxiv.org/abs/2605.30706)

**<font color=#1a73e8>作者：</font>** Nadia Mariyan Smith, Nils Bonfils, Han Qiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Permacomputing is a nascent concept and community of practice concerned with developing alternative computing systems grounded in principles of resilience, reuse, sufficiency, and ecological limits. However, research engaging with permacomputing remains in an early stage of development, raising concerns about whether permacomputing can move beyond reflective critique to become a meaningful alternative practice. Through a research-through-design case study, we documented our experience moving a personal website from a data centre in Texas to a self-hosted solar-powered server built from reclaimed electronics. Guided by permacomputing principles and relational aesthesis, we explore what it takes for permacomputing to reconfigure material and perceptual relations. Our findings reveal the frictions of moving away from a maximalist techno-aesthetic while attempting to re-use already existing technologies, potential ways to overcome these challenges through building a community of practice, and the transformative potential of visibilizing and visceralizing digital infrastructures to cultivate more responsible ways of relating to technology. This paper contributes to emerging research on permacomputing and its aesthetics by bringing it into dialogue with theories of non-place and relational aesthesis. Rather than functioning as a purely symbolic gesture, permacomputing practices can cultivate greater collective autonomy, agency, and responsibility in how communities engage and create meaning within digital infrastructures. In the context of socio-ecological crises and anti-colonial transformation, our research offers a situated approach to building and relating to computing technologies in the ashes of dominant technological paradigms.

---


### 85. [Vision-Based Localization in Dense Urban Environments: A Case Study of an Urban Village in China](https://arxiv.org/abs/2605.30714)

**<font color=#1a73e8>作者：</font>** Menglin Wu, Rui Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban villages, the widespread informal settlements which have emerged as a result of rapid urbanization, are now major residential hubs for migrant workers in large cities in China. The dense arrangement of buildings in these areas often leads to unreliable GPS signals, while incomplete mapping data further impairs accurate route planning and navigation. These issues not only hinder everyday mobility but also pose significant challenges for emergency response, as confusing road layouts and GPS inaccuracies can complicate evacuation efforts. To address these challenges, we propose a practical vision-based geo-localization solution tailored for dense urban environments. Our approach features a low-cost data collection pipeline utilizing a dual-camera system, comprising a panoramic camera and a smartphone camera, to capture synchronized 360-degree panoramas and query images. Using Shipai Village, a well-known densely populated urban village in Guangzhou, as a case study, we develop a specialized image geo-localization dataset. We then assess and compare the performance of existing models across various scene types to identify their strengths and weaknesses. The findings demonstrate both the potential and limitations of visual-based localization in dense urban-village environments. Our framework aims to enhance pedestrian navigation, last-mile delivery, and emergency management in areas with poor GPS coverage, ultimately supporting the vulnerable populations living within these informal settlements.

---


### 86. [Kalimati Vegetable Price Index Forecasting with a Momentum Corrected Online Stacking Ensemble](https://arxiv.org/abs/2605.30720)

**<font color=#1a73e8>作者：</font>** Sahaj Raj Malla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting agricultural commodity prices in emerging economies is difficult due to high volatility, frequent supply disruptions, and strong cultural influences on demand. This study introduces the Kalimati Vegetable Price Index (KVPI), a new inverse-volatility weighted composite index that aggregates 135 daily wholesale commodities from Kathmandu over ten years (2013-2023). By creating a stable macro-level signal, the KVPI reduces the noise inherent in modelling individual crops. A rich set of 64 causally valid features was developed, including festival lead-lag effects, rolling statistics, and calendar variables. Fourteen forecasting models spanning statistical, tree-based, deep learning, hybrid, and transformer architectures were rigorously evaluated across short (7-day), medium (14- and 30-day), and long-term (90-day) horizons. Tree-based ensembles proved notably robust, while classical statistical models and complex transformers struggled with the noisy dataset. The proposed Momentum-Corrected Online Stacking Ensemble achieved the strongest performance, yielding a Root Mean Square Error (RMSE) of 1.771, an exceptionally low Mean Absolute Percentage Error (MAPE) of 0.68%, and explaining 84.5% of the variance (R-squared = 0.845) at the 90-day horizon. This open-source pipeline provides policymakers and supply chain actors in Nepal and similar markets with a practical, reliable tool for anticipating price movements and strengthening food security.

---


### 87. [Self-Certifying Transport MCMC via Dual Spectral-Gap Certificates](https://arxiv.org/abs/2605.30722)

**<font color=#1a73e8>作者：</font>** Jun Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose CerT-MCMC, a framework that equips learned-transport Markov chain Monte Carlo with automatic, rigorous convergence certificates. A normalising flow maps a Gaussian reference to an approximation of the target posterior; the same flow then serves as both the independence Metropolis-Hastings proposal and the basis for a computable spectral-gap bound. We develop two complementary certificates. The covering certificate bounds the weight-ratio oscillation over the full proposal support via finite-sample covering arguments, yielding full-support spectral-gap bounds when a conservative gradient bound is available; its correction term scales as O(n^{-1/D}), making it rapidly weak and eventually vacuous as dimension increases. We prove a matching Omega(n^{-1/D}) lower bound, establishing that this barrier is intrinsic to pointwise Lipschitz certification. The quantile-core certificate restricts attention to a high-probability residual core on which the oscillation is controlled by one-dimensional empirical quantiles, with a finite-sample probability slack of O(n^{-1/2}), independent of the ambient dimension. On synthetic targets (D=2-20), structural-engineering posteriors (D=6,8), real-data logistic regression on the Heart Disease data set (D=13), and synthetic Bayesian logistic regression (D=20), the quantile-core certificate delivers non-vacuous spectral-gap bounds where the covering certificate is vacuous, and its spectral-gap proxy tracks empirical effective sample sizes within 7%. A negative control experiment confirms that the certificate discriminates flow quality by a factor exceeding 10x, whereas acceptance rates differ by only 1.15x. To our knowledge, the dual-certificate framework is the first to provide automatic, dimension-aware convergence certificates for learned-transport MCMC, distinguishing genuine transport failure from proof-technique limitations.

---


### 88. [MosaicLeaks:Privacy Risks in Querying-in-the-Open for Deep Research Agents](https://arxiv.org/abs/2605.30727)

**<font color=#1a73e8>作者：</font>** Alexander Gurung, Spandana Gella, Alexandre Drouin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research agents increasingly combine private local documents with external tools like web retrieval, creating a privacy risk: an agent's external queries may leak sensitive information from its local context. This risk is amplified by the mosaic effect, where individual queries may appear harmless but become revealing in aggregate. We introduce MosaicLeaks, a benchmark of 1,001 multi-hop deep research tasks that chain private enterprise documents and a public web corpus, forcing agents to make external queries that depend on local information. We evaluate leakage with an adversary LLM that observes only the agent's external queries and attempts to infer private information at three levels: the agent's research intent, answers to specific private questions and verifiable claims about the enterprise documents. We find that models across families and sizes frequently leak at all three levels, that zero-shot privacy prompting reduces but does not eliminate leakage and that reinforcement learning for task performance alone worsens leakage. To address this, we propose Privacy-Aware Deep Research (PA-DR), an RL framework that combines situational rewards for task success with a learned privacy classifier to provide dense credit assignment over both per-query and mosaic-level leakage. Training Qwen3-4B-Instruct with PA-DR improves accuracy from 48.7% to 58.7% and reduces answer and full-information leakage from 34.0% to 9.9%.

---


### 89. [Reducing the GPU Memory Bottleneck with Lossless Compression for ML -- Extended](https://arxiv.org/abs/2605.30728)

**<font color=#1a73e8>作者：</font>** Aditya K Kamath, Arvind Krishnamurthy, Marco Canini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) training and inference often process data sets far exceeding GPU memory capacity, forcing them to rely on PCIe for on-demand tensor transfers, causing critical transfer bottlenecks. Lossy compression has been proposed to relieve bottlenecks but introduces workload-dependent accuracy loss, making it complex or even prohibitive to use in existing ML deployments. We explore lossless compression as an alternative that avoids this deployment complexity. We identify where lossless compression can be integrated into ML pipelines while minimizing interference with GPU execution. Based on our findings, we introduce Invariant Bit Packing (IBP), a novel lossless compression algorithm designed to minimize data transfer time for ML. IBP identifies and eliminates invariant bits across groups of tensors, improving throughput through GPU-optimized decompression that leverages warp parallelism, low-overhead bit operations, and asynchronous PCIe transfers. We provide easy-to-use APIs, showcasing them by adding IBP support to GNN training, as well as DLRM and LLM inference frameworks. IBP achieves, on average, 74% faster GNN training, 180% faster DLRM embedding lookup, and 24% faster LLM inference.

---


### 90. [SemStruct: Contextualizing Semantic Embeddings with Structural Information for Schema Matching](https://arxiv.org/abs/2605.30729)

**<font color=#1a73e8>作者：</font>** Inwon Kang, Kavitha Srinivas, Nandana Mihindukulasooriya 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Schema matching is a fundamental step in integrating heterogeneous data sources. While Pre-trained Language Models (PLMs) have revolutionized this task by capturing linguistic semantics, they typically process tabular data as serialized text sequences of standalone column descriptions. This serialization discards critical structural information -- specifically, the row-level co-occurrences, i.e. the relational context -- forcing models to rely solely on column header semantics or standalone distributions. To bridge this gap, we propose SemStruct, a framework that joins the semantic power of frozen PLMs with the structural inductive bias of Graph Neural Networks (GNNs). We model the table as a heterogeneous graph where columns and values are nodes connected by rows, allowing the GNN to propagate disambiguating context across the structure. Unlike other state-of-the-art methods that require proprietary LLM access and fine-tuning of language models, SemStruct keeps the language model frozen and trains only a lightweight structural encoder. Extensive experiments on the Valentine and SOTAB-SM benchmarks demonstrate that SemStruct achieves state-of-the-art performance, outperforming fully fine-tuned baselines on complex, semantically joinable datasets. Furthermore, our ablation studies reveal that row representations serve primarily as topological conduits rather than semantic entities, validating the necessity of explicit structural modeling in schema matching.

---


### 91. [Beyond Accuracy: Evaluating Efficiency, Robustness and Explainability in Deep Learning for Malaria Diagnosis](https://arxiv.org/abs/2605.30734)

**<font color=#1a73e8>作者：</font>** Olivier Kanamugire, Kerol Djoumessi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Malaria remains a leading cause of mortality in sub-Saharan Africa, where scarce diagnostic infrastructure makes timely, accurate diagnosis particularly challenging. While deep learning offers a compelling path toward automated malaria screening, clinical adoption is hindered by computational cost and opacity in decision-making. This work benchmarks four deep learning models spanning a wide range of designed design architectures and model capacities on the NLM-Malaria dataset, jointly evaluating predictive performance, robustness, and post-hoc explainability. We find that lightweight, efficient-by-design models match their heavier counterparts in predictive performance, and the Friedman test confirms no statistically significant performance differences. CAM-based XAI methods consistently localize diagnostically relevant regions, while fine-grained attribution methods produce less targeted explanations, particularly with heavier backbones. Robustness evaluation under three types of image corruption further reveals that model confidence degrades faster than accuracy, providing a practical signal for human review. However, no XAI method is robust to corruption, with explanation reliability degrading at noise levels plausible in clinical practice, even when predictions remain accurate. These findings support the deployment of lightweight architectures for malaria diagnosis in resource-constrained settings, while highlighting the vulnerability of post-hoc explanations as an important consideration for responsible clinical deployment.

---


### 92. [Annotations Are Not All You Need: A Cross-modal Knowledge Transfer Network for Unsupervised Temporal Sentence Grounding](https://arxiv.org/abs/2605.30742)

**<font color=#1a73e8>作者：</font>** Xiang Fang, Daizong Liu, Wanlong Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the task of temporal sentence grounding (TSG). Although many respectable works have made decent achievements in this important topic, they severely rely on massive expensive video-query paired annotations, which require a tremendous amount of human effort to collect in real-world applications. To this end, in this paper, we target a more practical but challenging TSG setting: unsupervised temporal sentence grounding, where both paired video-query and segment boundary annotations are unavailable during the network training. Considering that some other cross-modal tasks provide many easily available yet cheap labels, we tend to collect and transfer their simple cross-modal alignment knowledge into our complex scenarios: 1) We first explore the entity-aware object-guided appearance knowledge from the paired Image-Noun task, and adapt them into each independent video frame; 2) Then, we extract the event-aware action representation from the paired Video-Verb task, and further refine the action representation into more practical but complicated real-world cases by a newly proposed copy-paste approach; 3) By modulating and transferring both appearance and action knowledge into our challenging unsupervised task, our model can directly utilize this general knowledge to correlate videos and queries, and accurately retrieve the relevant segment without training. Extensive experiments on two challenging datasets (ActivityNet Captions and Charades-STA) show our effectiveness, outperforming existing unsupervised methods and even competitively beating supervised works.

---


### 93. [Generating Graph-like Rules for Knowledge Graph Reasoning via Diffusion Models](https://arxiv.org/abs/2605.30747)

**<font color=#1a73e8>作者：</font>** Haoxiang Cheng, Yunfei Wang, Chao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Logical rules constitute a cornerstone of knowledge graph (KG) reasoning, valued for their interpretability and ability to model relational patterns. However, existing rule mining methods predominantly focus on simple chain-like rules and therefore neglect the richer relational information encoded in graph-like structures, such as cycles and branches. This limitation is further exacerbated by computational bottlenecks caused by the combinatorial explosion of the search space, which is especially challenging for graph-like rules. Meanwhile, generative approaches such as diffusion models, despite their success in other domains, can not be directly applied to rule mining because their training objectives are not aligned with the goal of learning high-quality rules, and non-differentiable KG rule quality metrics cannot directly guide model optimization. To address these limitations, we propose GRiD, a framework that reformulates graph-like rule discovery as a discrete generative process conditioned on the target relation. GRiD employs a two-phase training strategy. First, supervised pre-training enables GRiD to capture structural priors from subgraphs sampled from the KG meta-graph. Subsequently, reinforcement learning is applied to fine-tune GRiD through policy gradient optimization guided directly by non-differentiable rule-quality metrics. Experiments on six benchmark datasets show that GRiD achieves competitive performance on KG completion tasks. Ablation studies confirm the efficiency and robustness of GRiD and further show that graph-like rules complement chain-like rules in KG completion. Our codes and datasets are available in this https URL

---


### 94. [FLAG: Flow Policy MaxEnt-RL by Latent Augmented Guidance](https://arxiv.org/abs/2605.30749)

**<font color=#1a73e8>作者：</font>** Sungha Kim, Gawon Lee, Jusuk Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Maximum entropy reinforcement learning (MaxEnt-RL) enables robust exploration, yet practical implementations often restrict policies to simple Gaussians.
While recent approaches incorporate expressive generative policies via importance-weighted supervised learning, they are prone to importance weight collapse, which limits their scalability in high-dimensional action spaces.
Our key insight is to mitigate this limitation by localizing the sampling region, avoiding the weight degeneracy induced by importance sampling over the entire action space.
To instantiate this insight, we introduce \textbf{FLAG} (\textbf{F}low policy with \textbf{L}atent-\textbf{A}ugmented \textbf{G}uidance).
FLAG augments the state space with a flow latent variable and optimizes a provably consistent proxy MaxEnt-RL objective.
We empirically demonstrate that FLAG enables expressive policy optimization with limited importance samples and scales to high-dimensional control tasks.
Furthermore, FLAG achieves state-of-the-art performance across challenging benchmarks. Our project webpage: this https URL

---


### 95. [Chain-of-Thought and Compressed Looped Transformers: A Memory-Budget Separation](https://arxiv.org/abs/2605.30757)

**<font color=#1a73e8>作者：</font>** Haozhou Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought prompting and looped Transformers both give a fixed model more test-time computation, but they differ in what they remember. Chain-of-thought stores intermediate state in generated tokens that remain in the context, whereas a looped Transformer carries state through recurrent hidden activations. We argue that this persistent mutable memory is a central resource for test-time reasoning.
We compare three memory regimes, the compressed latent loop, the full sequence-state loop, and the chain-of-thought scratchpad. Our main result shows that a compressed loop is limited by the size of its recurrent state. Running the loop longer adds computation but does not by itself create a growing scratchpad, so a loop with a small recurrent state remains a small-space reasoner even when run for many steps. Under a standard complexity assumption, such loops cannot decide problems that are P-complete under logspace reductions, whereas polynomial-length chain-of-thought can.
The separation is specific to compressed loops, as full sequence-state loops carry state at every input position and live in a memory-rich regime closer to explicit scratchpads. Controlled pointer-chasing and associative-recall sweeps illustrate this memory-budget view, with performance sensitive to whether the persistent-state budget matches the task's working-memory demand.

---


### 96. [DisPlace: Discriminative Place Projections for Multi-Reference Visual Place Recognition](https://arxiv.org/abs/2605.30769)

**<font color=#1a73e8>作者：</font>** Dhyey Manish Rajani, Michael Milford, Tobias Fischer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A key challenge in Visual Place Recognition (VPR) is matching query images against reference maps captured under diverse environmental conditions and viewpoints. While multiple reference traversals improve robustness, existing fusion strategies either aggregate references uniformly or rely on heuristic selection, without distinguishing descriptor variations that preserve stable place identity from those caused by changing conditions or viewpoints. In this paper, we propose DisPlace, a multi-reference VPR framework that fuses multiple reference descriptors into a single compact and discriminative place representation. DisPlace formulates descriptor fusion as a generalized eigenvalue problem that maximizes between-place separability while suppressing within-place variation across references, rather than preserving overall descriptor variance. Unlike existing multi-reference fusion methods, DisPlace exploits variation across reference traversals to identify which linear combinations of descriptor dimensions preserve place identity and which capture condition- or viewpoint-specific variation. We evaluate DisPlace on Oxford RobotCar, Nordland, Pittsburgh30k, and Google Landmarks v2 across six state-of-the-art VPR descriptors. DisPlace outperforms seven multi-reference baselines in 49 out of 54 appearance-varying conditions, consistently improves descriptor-level fusion performance under viewpoint and unstructured settings, and requires less storage during inference than all compared fusion methods.

---


### 97. [Eywa: Provenance-Grounded Long-Term Memory for AI Agents](https://arxiv.org/abs/2605.30771)

**<font color=#1a73e8>作者：</font>** Resham Joshi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI agents that persist across sessions need memory they can retrieve, audit, update, and erase. Existing memory systems often collapse source evidence, extracted facts, retrieved context, and answer policy into one opaque prompt path, making failures difficult to diagnose: a wrong answer may come from missing evidence, unsupported extraction, stale state, retrieval loss, or answer-model behavior. We present Eywa, a provenance-grounded memory architecture built around evidence before belief. Eywa stores immutable source evidence before deriving canonical facts, validates extracted memories against typed signals and source support, and retrieves bounded memory context through a deterministic multi-route read path with zero LLM calls inside retrieval. Retrieved context is returned separately from answer instructions, allowing the same memory substrate to be evaluated across frontier, budget, and local answer models. Under a frozen, artifact-recorded retrieval configuration, Eywa reaches 90.19% judge accuracy on the LoCoMo C1-C4 split with Claude Sonnet 4.6 write and QA roles. On LongMemEval-S, it reaches 88.2% retrieval-sufficiency accuracy. On BEAM, a 700-question technical-memory stress benchmark, it reaches 81.45% mean nugget score and 85.29% pass@score >= 0.5. Full per-question artifacts, including questions, gold answers, model answers, retrieved context, and labels, are published at this https URL.

---


### 98. [CameraNoise: Enabling Faithful Camera Control in Video Diffusion through Geometry-Flow-Guided Noise Warping](https://arxiv.org/abs/2605.30774)

**<font color=#1a73e8>作者：</font>** Haoyu Zhao, Jiaxi Gu, Haoran Chen 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise camera pose control is critical for video diffusion, yet maintaining geometric consistency remains a challenge. Existing methods that directly inject numerical camera parameters into the diffusion backbone often fail to bridge the gap between abstract coordinates and visual content, leading to structural distortions. To address this issue, we propose CameraNoise, a flow-to-noise warping method that encodes camera motion into a temporally coherent stochastic representation. Unlike conventional conditioning, CameraNoise embeds camera poses directly into the noise space. This decouples motion from scene appearance while faithfully preserving trajectory dynamics. Specifically, we introduce a novel Geometry-guided Reprojection Flow and a noise warping algorithm, which jointly preserve the Gaussian prior of diffusion and ensure consistent noise propagation under camera transformations. By integrating CameraNoise into the diffusion process, our framework delivers stable, high-fidelity videos. Extensive experiments demonstrate that our approach significantly outperforms prior methods in both visual quality and trajectory faithfulness. The project page and code are available at: this https URL.

---


### 99. [Efficient and Uncertainty-Aware Diffusion Framework for Offline-to-Online Reinforcement Learning](https://arxiv.org/abs/2605.30776)

**<font color=#1a73e8>作者：</font>** Ha Manh Bui, Metod Jazbec, Eric Nalisnick 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline-to-Online Reinforcement Learning (O2O-RL) leverages an offline, pre-trained policy to minimize costly online interactions. Although data-efficient, O2O-RL is susceptible to shifts between offline and online distributions. Existing work aims to mitigate the harm of this shift by finetuning the policy on trajectory data sampled from a diffusion model. Inspired by this line of work, we propose DUAL: an efficient \textbf{D}iffusion \textbf{U}ncertainty-\textbf{A}ware framework for offline-to-online reinforcement \textbf{L}earning. DUAL utilizes the prior knowledge of the diffusion model to distill a fast-sampling diffusion actor policy and transition model in the offline phase. DUAL also employs a Laplace approximation and distance transition-state-shift detection, thereby using uncertainty quantification to improve exploration versus exploitation in the online phase. We formally show that our actor loss with the Laplace approximation provides a proxy for a principled estimate of epistemic uncertainty. Empirically, DUAL improves the online expected return over O2O-RL baselines across multiple settings and environments.

---


### 100. [Text-guided Feature Disentanglement for Cross-modal Gait Recognition](https://arxiv.org/abs/2605.30784)

**<font color=#1a73e8>作者：</font>** Zhiyang Lu, Ming Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait recognition is a biometric technique that identifies individuals based on their walking patterns, offering advantages in long-range, non-intrusive scenarios. However, real-world scenarios often involve heterogeneous sensing modalities such as LiDAR and RGB cameras, making LiDAR-Camera Cross-modal Gait recognition (LCCGR) a critical yet challenging task due to the substantial modality gap between 2D videos and 3D point cloud sequences. To address this challenge, we propose TCFDNet, a Text-guided Cross-modal Feature Disentanglement Network, which leverages modality-aware textual priors as semantic anchors to guide the learning of disentangled modality-shared representations. Specifically, we construct a Gait Modality Text Dictionary (GMTD) using large language models to generate rich semantic descriptions of gait across modalities and viewpoints. A CLIP-based Multi-grained Feature Encoder then aligns visual and textual features within a unified vision-language space. Furthermore, the Text-guided Feature Disentanglement (TFD) module selects the topk matched textual descriptions to reconstruct modality-specific representations and derive modality-shared features via residual decomposition and orthogonality constraints. To mitigate the fragility of the disentangled shared features, we propose a Feature Stability Enhancement (FSE) module, which models spatial and channel-wise correlations to improve feature robustness. In addition, a cross-modal patch exchange strategy is introduced to further improve generalization. Extensive experiments on SUSTech1K and FreeGait datasets demonstrate that TCFDNet achieves new state-of-the-art results and validate the effectiveness of the proposed modules.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-317](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
