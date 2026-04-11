# 📦 其他研究 | 2026年04月12日

> 本类共 **242** 篇论文

> 未进入大模型主领域展示范围的其他研究。

---

### 1. [Contextual Earnings-22: A Speech Recognition Benchmark with Custom Vocabulary in the Wild](https://arxiv.org/abs/2604.07354)

**<font color=#1a73e8>作者：</font>** Berkin Durmus, Chen Cen, Eduardo Pacheco 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The accuracy frontier of speech-to-text systems has plateaued on academic benchmarks.1 In contrast, industrial benchmarks and adoption in high-stakes domains suggest otherwise. We hypothesize that the primary difference between the two is contextual conditioning: Academic benchmarks are dominated by frequently encountered general vocabulary that is relatively easy to recognize compared with rare and context-defined custom vocabulary that has disproportionate impact on the usability of speech transcripts. Despite progress on contextual speech-to-text, there is no standardized benchmark. We introduce Contextual Earnings-22, an open dataset built upon Earnings-22, with realistic custom vocabulary contexts to foster research and reveal latent progress. We set six strong baselines for two dominant approaches: keyword prompting and keyword boosting. Experiments show both reach comparable and significantly improved accuracy when scaled from proof-of-concept to large-scale systems.

---


### 2. [Prediction Arena: Benchmarking AI Models on Real-World Prediction Markets](https://arxiv.org/abs/2604.07355)

**<font color=#1a73e8>作者：</font>** Jaden Zhang, Gardenia Liu, Oliver Johansson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Prediction Arena, a benchmark for evaluating AI models' predictive accuracy and decision-making by enabling them to trade autonomously on live prediction markets with real capital. Unlike synthetic benchmarks, Prediction Arena tests models in environments where trades execute on actual exchanges (Kalshi and Polymarket), providing objective ground truth that cannot be gamed or overfitted. Each model operates as an independent agent starting with $10,000, making autonomous decisions every 15-45 minutes. Over a 57-day longitudinal evaluation (January 12 to March 9, 2026), we track two cohorts: six frontier models in live trading (Cohort 1, full period) and four next-generation models in paper trading (Cohort 2, 3-day preliminary). For Cohort 1, final Kalshi returns range from -16.0% to -30.8%. Our analysis identifies a clear performance hierarchy: initial prediction accuracy and the ability to capitalize on correct predictions are the main drivers, while research volume shows no correlation with outcomes. A striking cross-platform contrast emerges from parallel Polymarket live trading: Cohort 1 models averaged only -1.1% on Polymarket vs. -22.6% on Kalshi, with grok-4-20-checkpoint achieving a 71.4% settlement win rate - the highest across any platform or cohort. gemini-3.1-pro-preview (Cohort 2), which executed zero trades on Kalshi, achieved +6.02% on Polymarket in 3 days - the best return of any model across either cohort - demonstrating that platform design has a profound effect on which models succeed. Beyond performance, we analyze computational efficiency (token usage, cycle time), settlement accuracy, exit patterns, and market preferences, providing a comprehensive view of how frontier models behave under real financial pressure.

---


### 3. [Hybrid CNN-Transformer Architecture for Arabic Speech Emotion Recognition](https://arxiv.org/abs/2604.07357)

**<font color=#1a73e8>作者：</font>** Youcef Soufiane Gheffari, Oussama Mustapha Benouddane, Samiya Silarbi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recognizing emotions from speech using machine learning has become an active research area due to its importance in building human-centered applications. However, while many studies have been conducted in English, German, and other European and Asian languages, research in Arabic remains scarce because of the limited availability of annotated datasets. In this paper, we present an Arabic Speech Emotion Recognition (SER) system based on a hybrid CNN-Transformer architecture. The model leverages convolutional layers to extract discriminative spectral features from Mel-spectrogram inputs and Transformer encoders to capture long-range temporal dependencies in speech. Experiments were conducted on the EYASE (Egyptian Arabic speech emotion) corpus, and the proposed model achieved 97.8% accuracy and a macro F1-score of 0.98. These results demonstrate the effectiveness of combining convolutional feature extraction with attention-based modeling for Arabic SER and highlight the potential of Transformer-based approaches in low-resource languages.

---


### 4. [Flow Learners for PDEs: Toward a Physics-to-Physics Paradigm for Scientific Computing](https://arxiv.org/abs/2604.07366)

**<font color=#1a73e8>作者：</font>** Yilong Dai, Shengyu Chen, Xiaowei Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial differential equations (PDEs) govern nearly every physical process in science and engineering, yet solving them at scale remains prohibitively expensive. Generative AI has transformed language, vision, and protein science, but learned PDE solvers have not undergone a comparable shift. Existing paradigms each capture part of the problem. Physics-informed neural networks embed residual structure, yet they are often difficult to optimize in stiff, multiscale, or large-domain regimes. Neural operators amortize across instances, yet they commonly inherit a snapshot-prediction view of solving and can degrade over long rollouts. Diffusion-based solvers model uncertainty, yet they are often built on a solver template that still centers on state regression. We argue that the core issue is the abstraction used to train learned solvers. Many models are asked to predict states, while many scientific settings require modeling how uncertainty moves through constrained dynamics. The relevant object is transport over physically admissible futures. This motivates \emph{flow learners}: models that parameterize transport vector fields and generate trajectories through integration, echoing the continuous dynamics that define PDE evolution. This physics-to-physics alignment supports continuous-time prediction, native uncertainty quantification, and new opportunities for physics-aware solver design. We explain why transport-based learning offers a stronger organizing principle for learned PDE solving and outline the research agenda that follows from this shift.

---


### 5. [The Lifecycle of the Spectral Edge: From Gradient Learning to Weight-Decay Compression](https://arxiv.org/abs/2604.07380)

**<font color=#1a73e8>作者：</font>** Yongzhong Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We decompose the spectral edge -- the dominant direction of the Gram matrix of parameter updates -- into its gradient and weight-decay components during grokking in two sequence tasks (Dyck-1 and SCAN). We find a sharp two-phase lifecycle: before grokking the edge is gradient-driven and functionally active; at grokking, gradient and weight decay align, and the edge becomes a compression axis that is perturbation-flat yet ablation-critical (>4000x more impactful than random directions). Three universality classes emerge (functional, mixed, compression), predicted by the gap flow equation. Nonlinear probes show information is re-encoded, not lost (MLP $R^2=0.99$ where linear $R^2=0.86$), and removing weight decay post-grok reverses compression while preserving the algorithm.

---


### 6. [SCOT: Multi-Source Cross-City Transfer with Optimal-Transport Soft-Correspondence Objective](https://arxiv.org/abs/2604.07383)

**<font color=#1a73e8>作者：</font>** Yuyao Wang, Min Yang, Meng Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-city transfer improves prediction in label-scarce cities by leveraging labeled data from other cities, but it becomes challenging when cities adopt incompatible partitions and no ground-truth region correspondences exist. Existing approaches either rely on heuristic region matching, which is often sensitive to anchor choices, or perform distribution-level alignment that leaves correspondences implicit and can be unstable under strong heterogeneity. We propose SCOT, a cross-city representation learning framework that learns explicit soft correspondences between unequal region sets via Sinkhorn-based entropic optimal transport. SCOT further sharpens transferable structure with an OT-weighted contrastive objective and stabilizes optimization through a cycle-style reconstruction regularizer. For multi-source transfer, SCOT aligns each source and the target to a shared prototype hub using balanced entropic transport guided by a target-induced prototype prior. Across real-world cities and tasks, SCOT consistently improves transfer accuracy and robustness, while the learned transport couplings and hub assignments provide interpretable diagnostics of alignment quality.

---


### 7. [Decisions and Deployment: The Five-Year SAHELI Project (2020-2025) on Restless Multi-Armed Bandits for Improving Maternal and Child Health](https://arxiv.org/abs/2604.07384)

**<font color=#1a73e8>作者：</font>** Shresth Verma, Arpan Dasgupta, Neha Madhiwalla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Maternal and child health is a critical concern around the world. In many global health programs disseminating preventive care and health information, limited healthcare worker resources prevent continuous, personalised engagement with vulnerable beneficiaries. In such scenarios, it becomes crucial to optimally schedule limited live-service resources to maximise long-term engagement. To address this fundamental challenge, the multi-year SAHELI project (2020-2025), in collaboration with partner NGO ARMMAN, leverages AI to allocate scarce resources in a maternal and child health program in India. The SAHELI system solves this sequential resource allocation problem using a Restless Multi-Armed Bandit (RMAB) framework. A key methodological innovation is the transition from a traditional Two-Stage "predict-then-optimize" approach to Decision-Focused Learning (DFL), which directly aligns the framework's learning method with the ultimate goal of maximizing beneficiary engagement. Empirical evaluation through large-scale randomized controlled trials demonstrates that the DFL policy reduced cumulative engagement drops by 31% relative to the current standard of care, significantly outperforming the Two-Stage model. Crucially, the studies also confirmed that this increased program engagement translates directly into statistically significant improvements in real-world health behaviors, notably the continued consumption of vital iron and calcium supplements by new mothers. Ultimately, the SAHELI project provides a scalable blueprint for applying sequential decision-making AI to optimize resource allocation in health programs.

---


### 8. [Label Leakage Attacks in Machine Unlearning: A Parameter and Inversion-Based Approach](https://arxiv.org/abs/2604.07386)

**<font color=#1a73e8>作者：</font>** Weidong Zheng, Kongyang Chen, Yao Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the widespread application of artificial intelligence technologies in face recognition and other fields, data privacy security issues have received extensive attention, especially the \textit{right to be forgotten} emphasized by numerous privacy protection laws. Existing technologies have proposed various unlearning methods, but they may inadvertently leak the categories of unlearned data. This paper focuses on the category unlearning scenario, analyzes the potential problems of category leakage of unlearned data in multiple scenarios, and proposes four attack methods from the perspectives of model parameters and model inversion based on attackers with different knowledge backgrounds. At the level of model parameters, we construct discriminative features by computing either dot products or vector differences between the parameters of the target model and those of auxiliary models trained on subsets of retained data and unrelated data, respectively. These features are then processed via k-means clustering, Youden's Index, and decision tree algorithms to achieve accurate identification of the forgotten class. In the model inversion domain, we design a gradient optimization-based white-box attack and a genetic algorithm-based black-box attack to reconstruct class-prototypical samples. The prediction profiles of these synthesized samples are subsequently analyzed using a threshold criterion and an information entropy criterion to infer the forgotten class. We evaluate the proposed attacks on four standard datasets against five state-of-the-art unlearning algorithms, providing a detailed analysis of the strengths and limitations of each method. Experimental results demonstrate that our approach can effectively infer the classes forgotten by the target model.

---


### 9. [A Novel Edge-Assisted Quantum-Classical Hybrid Framework for Crime Pattern Learning and Classification](https://arxiv.org/abs/2604.07389)

**<font color=#1a73e8>作者：</font>** Niloy Das, Apurba Adhikary, Sheikh Salman Hassan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Crime pattern analysis is critical for law enforcement and predictive policing, yet the surge in criminal activities from rapid urbanization creates high-dimensional, imbalanced datasets that challenge traditional classification methods. This study presents a quantum-classical comparison framework for crime analytics, evaluating four computational paradigms: quantum models, classical baseline machine learning models, and two hybrid quantum-classical architectures. Using 16-year Bangladesh crime statistics, we systematically assess classification performance and computational efficiency under rigorous cross-validation methods. Experimental results show that quantum-inspired approaches, particularly QAOA, achieve up to 84.6% accuracy, while requiring fewer trainable parameters than classical baselines, suggesting practical advantages for memory-constrained edge deployment. The proposed correlation-aware circuit design demonstrates the potential of incorporating domain-specific feature relationships into quantum models. Furthermore, hybrid approaches exhibit competitive training efficiency, making them suitable candidates for resource-constrained environments. The framework's low computational overhead and compact parameter footprint suggest potential advantages for wireless sensor network deployments in smart city surveillance systems, where distributed nodes perform localized crime analytics with minimal communication costs. Our findings provide a preliminary empirical assessment of quantum-enhanced machine learning for structured crime data and motivate further investigation with larger datasets and realistic quantum hardware considerations.

---


### 10. [DSPR: Dual-Stream Physics-Residual Networks for Trustworthy Industrial Time Series Forecasting](https://arxiv.org/abs/2604.07393)

**<font color=#1a73e8>作者：</font>** Yeran Zhang, Pengwei Yang, Guoqing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of industrial time series requires balancing predictive accuracy with physical plausibility under non-stationary operating conditions. Existing data-driven models often achieve strong statistical performance but struggle to respect regime-dependent interaction structures and transport delays inherent in real-world systems. To address this challenge, we propose DSPR (Dual-Stream Physics-Residual Networks), a forecasting framework that explicitly decouples stable temporal patterns from regime-dependent residual dynamics. The first stream models the statistical temporal evolution of individual variables. The second stream focuses on residual dynamics through two key mechanisms: an Adaptive Window module that estimates flow-dependent transport delays, and a Physics-Guided Dynamic Graph that incorporates physical priors to learn time-varying interaction structures while suppressing spurious correlations. Experiments on four industrial benchmarks spanning heterogeneous regimes demonstrate that DSPR consistently improves forecasting accuracy and robustness under regime shifts while maintaining strong physical plausibility. It achieves state-of-the-art predictive performance, with Mean Conservation Accuracy exceeding 99% and Total Variation Ratio reaching up to 97.2%. Beyond forecasting, the learned interaction structures and adaptive lags provide interpretable insights that are consistent with known domain mechanisms, such as flow-dependent transport delays and wind-to-power scaling behaviors. These results suggest that architectural decoupling with physics-consistent inductive biases offers an effective path toward trustworthy industrial time-series forecasting. Furthermore, DSPR's demonstrated robust performance in long-term industrial deployment bridges the gap between advanced forecasting models and trustworthy autonomous control systems.

---


### 11. [Data Warmup: Complexity-Aware Curricula for Efficient Diffusion Training](https://arxiv.org/abs/2604.07397)

**<font color=#1a73e8>作者：</font>** Jinhong Lin, Pan Wang, Zitong Zhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A key inefficiency in diffusion training occurs when a randomly initialized network, lacking visual priors, encounters gradients from the full complexity spectrum--most of which it lacks the capacity to resolve. We propose Data Warmup, a curriculum strategy that schedules training images from simple to complex without modifying the model or loss. Each image is scored offline by a semantic-aware complexity metric combining foreground dominance (how much of the image salient objects occupy) and foreground typicality (how closely the salient content matches learned visual prototypes). A temperature-controlled sampler then prioritizes low-complexity images early and anneals toward uniform sampling. On ImageNet 256x256 with SiT backbones (S/2 to XL/2), Data Warmup improves IS by up to 6.11 and FID by up to 3.41, reaching baseline quality tens of thousands of iterations earlier. Reversing the curriculum (exposing hard images first) degrades performance below the uniform baseline, confirming that the simple-to-complex ordering itself drives the gains. The method combines with orthogonal accelerators such as REPA and requires only ~10 minutes of one-time preprocessing with zero per-iteration overhead.

---


### 12. [Critical Patch-Aware Sparse Prompting with Decoupled Training for Continual Learning on the Edge](https://arxiv.org/abs/2604.07399)

**<font color=#1a73e8>作者：</font>** Wonseon Lim, Jaesung Lee, Dae-Won Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) on edge devices requires not only high accuracy but also training-time efficiency to support on-device adaptation under strict memory and computational constraints. While prompt-based continual learning (PCL) is parameter-efficient and achieves competitive accuracy, prior work has focused mainly on accuracy or inference-time performance, often overlooking the memory and computational costs of on-device training. In this paper, we propose CPS-Prompt, a critical patch-aware sparse prompting framework that explicitly targets training-time memory usage and computational cost by integrating critical patch sampling (CPS) for task-aware token reduction and decoupled prompt and classifier training (DPCT) to reduce backpropagation overhead. Experiments on three public benchmarks and real edge hardware show that CPS-Prompt improves peak memory, training time, and energy efficiency by about 1.6x over the balanced CODA-Prompt baseline, while maintaining accuracy within 2% of the state-of-the-art C-Prompt on average and remaining competitive with CODA-Prompt in accuracy. The code is available at this https URL.

---


### 13. [Accelerating Training of Autoregressive Video Generation Models via Local Optimization with Representation Continuity](https://arxiv.org/abs/2604.07402)

**<font color=#1a73e8>作者：</font>** Yucheng Zhou, Jianbing Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive models have shown superior performance and efficiency in image generation, but remain constrained by high computational costs and prolonged training times in video generation. In this study, we explore methods to accelerate training for autoregressive video generation models through empirical analyses. Our results reveal that while training on fewer video frames significantly reduces training time, it also exacerbates error accumulation and introduces inconsistencies in the generated videos. To address these issues, we propose a Local Optimization (Local Opt.) method, which optimizes tokens within localized windows while leveraging contextual information to reduce error propagation. Inspired by Lipschitz continuity, we propose a Representation Continuity (ReCo) strategy to improve the consistency of generated videos. ReCo utilizes continuity loss to constrain representation changes, improving model robustness and reducing error accumulation. Extensive experiments on class- and text-to-video datasets demonstrate that our approach achieves superior performance to the baseline while halving the training cost without sacrificing quality.

---


### 14. [Conservation Law Breaking at the Edge of Stability: A Spectral Theory of Non-Convex Neural Network Optimization](https://arxiv.org/abs/2604.07405)

**<font color=#1a73e8>作者：</font>** Daniel Nobrega Medeiros  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Why does gradient descent reliably find good solutions in non-convex neural network optimization, despite the landscape being NP-hard in the worst case? We show that gradient flow on L-layer ReLU networks without bias preserves L-1 conservation laws C_l = ||W_{l+1}||_F^2 - ||W_l||_F^2, confining trajectories to lower-dimensional manifolds. Under discrete gradient descent, these laws break with total drift scaling as eta^alpha where alpha is approximately 1.1-1.6 depending on architecture, loss function, and width. We decompose this drift exactly as eta^2 * S(eta), where the gradient imbalance sum S(eta) admits a closed-form spectral crossover formula with mode coefficients c_k proportional to e_k(0)^2 * lambda_{x,k}^2, derived from first principles and validated for both linear (R=0.85) and ReLU (R>0.80) networks. For cross-entropy loss, softmax probability concentration drives exponential Hessian spectral compression with timescale tau = Theta(1/eta) independent of training set size, explaining why cross-entropy self-regularizes the drift exponent near alpha=1.0. We identify two dynamical regimes separated by a width-dependent transition: a perturbative sub-Edge-of-Stability regime where the spectral formula applies, and a non-perturbative regime with extensive mode coupling. All predictions are validated across 23 experiments.

---


### 15. [GAN-based Domain Adaptation for Image-aware Layout Generation in Advertising Poster Design](https://arxiv.org/abs/2604.07409)

**<font color=#1a73e8>作者：</font>** Chenchen Xu, Min Zhou, Tiezheng Ge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Layout plays a crucial role in graphic design and poster generation. Recently, the application of deep learning models for layout generation has gained significant attention. This paper focuses on using a GAN-based model conditioned on images to generate advertising poster graphic layouts, requiring a dataset of paired product images and layouts. To address this task, we introduce the Content-aware Graphic Layout Dataset (CGL-Dataset), consisting of 60,548 paired inpainted posters with annotations and 121,000 clean product images. The inpainting artifacts introduce a domain gap between the inpainted posters and clean images. To bridge this gap, we design two GAN-based models. The first model, CGL-GAN, uses Gaussian blur on the inpainted regions to generate layouts. The second model combines unsupervised domain adaptation by introducing a GAN with a pixel-level discriminator (PD), abbreviated as PDA-GAN, to generate image-aware layouts based on the visual texture of input images. The PD is connected to shallow-level feature maps and computes the GAN loss for each input-image pixel. Additionally, we propose three novel content-aware metrics to assess the model's ability to capture the intricate relationships between graphic elements and image content. Quantitative and qualitative evaluations demonstrate that PDA-GAN achieves state-of-the-art performance and generates high-quality image-aware layouts.

---


### 16. [Reinforcement Learning with Reward Machines for Sleep Control in Mobile Networks](https://arxiv.org/abs/2604.07411)

**<font color=#1a73e8>作者：</font>** Kristina Levina, Nikolaos Pappas, Athanasios Karapantelakis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy efficiency in mobile networks is crucial for sustainable telecommunications infrastructure, particularly as network densification continues to increase power consumption. Sleep mechanisms for the components in mobile networks can reduce energy use, but deciding which components to put to sleep, when, and for how long while preserving quality of service (QoS) remains a difficult optimisation problem. In this paper, we utilise reinforcement learning with reward machines (RMs) to make sleep-control decisions that balance immediate energy savings and long-term QoS impact, i.e. time-averaged packet drop rates for deadline-constrained traffic and time-averaged minimum-throughput guarantees for constant-rate users. A challenge is that time-averaged constraints depend on cumulative performance over time rather than immediate performance. As a result, the effective reward is non-Markovian, and optimal actions depend on operational history rather than the instantaneous system state. RMs account for the history dependence by maintaining an abstract state that explicitly tracks the QoS constraint violations over time. Our framework provides a principled, scalable approach to energy management for next-generation mobile networks under diverse traffic patterns and QoS requirements.

---


### 17. [Physics-informed neural operators for the in situ characterization of locally reacting sound absorbers](https://arxiv.org/abs/2604.07412)

**<font color=#1a73e8>作者：</font>** Jonas M. Schmid, Johannes D. Schmid, Martin Eser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate knowledge of acoustic surface admittance or impedance is essential for reliable wave-based simulations, yet its in situ estimation remains challenging due to noise, model inaccuracies, and restrictive assumptions of conventional methods. This work presents a physics-informed neural operator approach for estimating frequency-dependent surface admittance directly from near-field measurements of sound pressure and particle velocity. A deep operator network is employed to learn the mapping from measurement data, spatial coordinates, and frequency to acoustic field quantities, while simultaneously inferring a globally consistent surface admittance spectrum without requiring an explicit forward model. The governing acoustic relations, including the Helmholtz equation, the linearized momentum equation, and Robin boundary conditions, are embedded into the training process as physics-based regularization, enabling physically consistent and noise-robust predictions while avoiding frequency-wise inversion. The method is validated using synthetically generated data from a simulation model for two planar porous absorbers under semi free-field conditions across a broad frequency range. Results demonstrate accurate reconstruction of both real and imaginary admittance components and reliable prediction of acoustic field quantities. Parameter studies confirm improved robustness to noise and sparse sampling compared to purely data-driven approaches, highlighting the potential of physics-informed neural operators for in situ acoustic material characterization.

---


### 18. [Bayesian Optimization for Mixed-Variable Problems in the Natural Sciences](https://arxiv.org/abs/2604.07416)

**<font color=#1a73e8>作者：</font>** Yuhao Zhang, Ti John, Matthias Stosiek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing expensive black-box objectives over mixed search spaces is a common challenge across the natural sciences. Bayesian optimization (BO) offers sample-efficient strategies through probabilistic surrogate models and acquisition functions. However, its effectiveness diminishes in mixed or high-cardinality discrete spaces, where gradients are unavailable and optimizing the acquisition function becomes computationally demanding. In this work, we generalize the probabilistic reparameterization (PR) approach of Daulton et al. to handle non-equidistant discrete variables, enabling gradient-based optimization in fully mixed-variable settings with Gaussian process (GP) surrogates. With real-world scientific optimization tasks in mind, we conduct systematic benchmarks on synthetic and experimental objectives to obtain an optimized kernel formulations and demonstrate the robustness of our generalized PR method. We additionally show that, when combined with a modified BO workflow, our approach can efficiently optimize highly discontinuous and discretized objective landscapes. This work establishes a practical BO framework for addressing fully mixed optimization problems in the natural sciences, and is particularly well suited to autonomous laboratory settings where noise, discretization, and limited data are inherent.

---


### 19. [An Analysis of Artificial Intelligence Adoption in NIH-Funded Research](https://arxiv.org/abs/2604.07424)

**<font color=#1a73e8>作者：</font>** Navapat Nananukul, Mayank Kejriwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding the landscape of artificial intelligence (AI) and machine learning (ML) adoption across the National Institutes of Health (NIH) portfolio is critical for research funding strategy, institutional planning, and health policy. The advent of large language models (LLMs) has fundamentally transformed research landscape analysis, enabling researchers to perform large-scale semantic extraction from thousands of unstructured research documents. In this paper, we illustrate a human-in-the-loop research methodology for LLMs to automatically classify and summarize research descriptions at scale. Using our methodology, we present a comprehensive analysis of 58,746 NIH-funded biomedical research projects from 2025. We show that: (1) AI constitutes 15.9% of the NIH portfolio with a 13.4% funding premium, concentrated in discovery, prediction, and data integration across disease domains; (2) a critical research-to-deployment gap exists, with 79% of AI projects remaining in research/development stages while only 14.7% engage in clinical deployment or implementation; and (3) health disparities research is severely underrepresented at just 5.7% of AI-funded work despite its importance to NIH's equity mission. These findings establish a framework for evidence-based policy interventions to align the NIH AI portfolio with health equity goals and strategic research priorities.

---


### 20. [GIRL: Generative Imagination Reinforcement Learning via Information-Theoretic Hallucination Control](https://arxiv.org/abs/2604.07426)

**<font color=#1a73e8>作者：</font>** Prakul Sunil Hiremath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (MBRL) improves sample efficiency by optimizing policies inside imagined rollouts, but long-horizon planning degrades when model errors compound and imagined trajectories drift off the training manifold. We introduce GIRL (Generative Imagination Reinforcement Learning), a latent world-model framework that addresses this failure mode with two key components. First, a cross-modal grounding signal derived from a frozen foundation model (DINOv2) anchors the latent transition prior to a semantically consistent embedding space, penalizing inconsistent or implausible predictions. Second, an uncertainty-adaptive trust-region bottleneck interprets the KL regularizer as the Lagrange multiplier of a constrained optimization problem, restricting imagination drift within a learned region calibrated by Expected Information Gain and a Relative Performance Loss signal.
We re-derive a value-gap bound using the Performance Difference Lemma and Integral Probability Metrics, yielding a bound that remains informative as the discount factor approaches one and connects the objective to real-environment regret. Experiments across three benchmark suites, including DeepMind Control, Adroit Hand Manipulation, and Meta-World with visual distractors, show that GIRL reduces latent rollout drift by 38 to 61 percent across tasks relative to DreamerV3, improves asymptotic return, and requires fewer environment interactions on long-horizon tasks. GIRL also outperforms TD-MPC2 on sparse-reward and high-contact settings under standard evaluation metrics. A distilled-prior variant reduces inference overhead and improves computational efficiency relative to the full model.

---


### 21. [Personalizing Text-to-Image Generation to Individual Taste](https://arxiv.org/abs/2604.07427)

**<font color=#1a73e8>作者：</font>** Anne-Sofie Maerten, Juliane Verwiebe, Shyamgopal Karthik 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image (T2I) models generate high-fidelity visuals but remain indifferent to individual user preferences. While existing reward models optimize for "average" human appeal, they fail to capture the inherent subjectivity of aesthetic judgment. In this work, we introduce a novel dataset and predictive framework, called PAMELA, designed to model personalized image evaluations. Our dataset comprises 70,000 ratings across 5,000 diverse images generated by state-of-the-art models (Flux 2 and Nano Banana). Each image is evaluated by 15 unique users, providing a rich distribution of subjective preferences across domains such as art, design, fashion, and cinematic photography. Leveraging this data, we propose a personalized reward model trained jointly on our high-quality annotations and existing aesthetic assessment subsets. We demonstrate that our model predicts individual liking with higher accuracy than the majority of current state-of-the-art methods predict population-level preferences. Using our personalized predictor, we demonstrate how simple prompt optimization methods can be used to steer generations towards individual user preferences. Our results highlight the importance of data quality and personalization to handle the subjectivity of user preferences. We release our dataset and model to facilitate standardized research in personalized T2I alignment and subjective visual quality assessment.

---


### 22. [Regret-Aware Policy Optimization: Environment-Level Memory for Replay Suppression under Delayed Harm](https://arxiv.org/abs/2604.07428)

**<font color=#1a73e8>作者：</font>** Prakul Sunil Hiremath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety in reinforcement learning (RL) is typically enforced through objective shaping while keeping environment dynamics stationary with respect to observable state-action pairs. Under delayed harm, this can lead to replay: after a washout period, reintroducing the same stimulus under matched observable conditions reproduces a similar harmful cascade.
We introduce the Replay Suppression Diagnostic (RSD), a controlled exposure-decay-replay protocol that isolates this failure mode under frozen-policy evaluation. We show that, under stationary observable transition kernels, replay cannot be structurally suppressed without inducing a persistent shift in replay-time action distributions.
Motivated by platform-mediated systems, we propose Regret-Aware Policy Optimization (RAPO), which augments the environment with persistent harm-trace and scar fields and applies a bounded, mass-preserving transition reweighting to reduce reachability of historically harmful regions.
On graph diffusion tasks (50-1000 nodes), RAPO suppresses replay, reducing re-amplification gain (RAG) from 0.98 to 0.33 on 250-node graphs while retaining 82\% of task return. Disabling transition deformation only during replay restores re-amplification (RAG 0.91), isolating environment-level deformation as the causal mechanism.

---


### 23. [Munkres' General Topology Autoformalized in Isabelle/HOL](https://arxiv.org/abs/2604.07455)

**<font color=#1a73e8>作者：</font>** Dustin Bryant, Jonathan Julián Huerta y Munive, Cezary Kaliszyk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We describe an experiment in LLM-assisted autoformalization that produced over 85,000 lines of Isabelle/HOL code covering all 39 sections of Munkres' Topology (general topology, Chapters 2--8), from topological spaces through dimension theory. The LLM-based coding agents (initially ChatGPT 5.2 and then Claude Opus 4.6) used 24 active days for that. The formalization is complete: all 806 formal results are fully proved with zero sorry's. Proved results include the Tychonoff theorem, the Baire category theorem, the Nagata--Smirnov and Smirnov metrization theorems, the Stone--Čech compactification, Ascoli's theorem, the space-filling curve, and others. The methodology is based on a "sorry-first" declarative proof workflow combined with bulk use of sledgehammer - two of Isabelle major strengths. This leads to relatively fast autoformalization progress. We analyze the resulting formalization in detail, analyze the human--LLM interaction patterns from the session log, and briefly compare with related autoformalization efforts in Megalodon, HOL Light, and Naproche. The results indicate that LLM-assisted formalization of standard mathematical textbooks in Isabelle/HOL is quite feasible, cheap and fast, even if some human supervision is useful.

---


### 24. [Lexical Tone is Hard to Quantize: Probing Discrete Speech Units in Mandarin and Yorùbá](https://arxiv.org/abs/2604.07467)

**<font color=#1a73e8>作者：</font>** Opeyemi Osakuade, Simon King  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discrete speech units (DSUs) are derived by quantising representations from models trained using self-supervised learning (SSL). They are a popular representation for a wide variety of spoken language tasks, including those where prosody matters. DSUs are especially convenient for tasks where text and speech are jointly modelled, such as text-to-speech and multimodal dialogue systems. But we have found that DSUs encode suprasegmental information less reliably than segmental structure, which we demonstrate in this work using lexical tone, though this limitation likely extends to other suprasegmental features such as prosody.
Our investigations using the tone languages Mandarin and Yorùbá show that the SSL latent representations themselves do encode tone, yet DSUs obtained using quantisation tend to prioritise phonetic structure, which makes lexical tone less reliably encoded. This remains true for a variety of quantisation methods, not only the most common, K-means.
We conclude that current DSU quantisation strategies have limitations for suprasegmental features, which suggests a need for new, tone-aware (or prosody-aware) techniques in speech representation learning. We point towards a potential form of the solution by performing K-means clustering once to encode phonetic information, then again on the residual representation, which better encodes lexical tone.

---


### 25. [SMFD-UNet: Semantic Face Mask Is The Only Thing You Need To Deblur Faces](https://arxiv.org/abs/2604.07477)

**<font color=#1a73e8>作者：</font>** Abduz Zami  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For applications including facial identification, forensic analysis, photographic improvement, and medical imaging diagnostics, facial image deblurring is an essential chore in computer vision allowing the restoration of high-quality images from blurry inputs. Often based on general picture priors, traditional deblurring techniques find it difficult to capture the particular structural and identity-specific features of human faces. We present SMFD-UNet (Semantic Mask Fusion Deblurring UNet), a new lightweight framework using semantic face masks to drive the deblurring process, therefore removing the need for high-quality reference photos in order to solve these difficulties. First, our dual-step method uses a UNet-based semantic mask generator to directly extract detailed facial component masks (e.g., eyes, nose, mouth) straight from blurry photos. Sharp, high-fidelity facial images are subsequently produced by integrating these masks with the blurry input using a multi-stage feature fusion technique within a computationally efficient UNet framework. We created a randomized blurring pipeline that roughly replicates real-world situations by simulating around 1.74 trillion deterioration scenarios, hence guaranteeing resilience. Examined on the CelebA dataset, SMFD-UNet shows better performance than state-of-the-art models, attaining higher Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index Measure (SSIM) while preserving satisfactory naturalness measures, including NIQE, LPIPS, and FID. Powered by Residual Dense Convolution Blocks (RDC), a multi-stage feature fusion strategy, efficient and effective upsampling techniques, attention techniques like CBAM, post-processing techniques, and the lightweight design guarantees scalability and efficiency, enabling SMFD-UNet to be a flexible solution for developing facial image restoration research and useful applications.

---


### 26. [Cluster Attention for Graph Machine Learning](https://arxiv.org/abs/2604.07492)

**<font color=#1a73e8>作者：</font>** Oleg Platonov, Liudmila Prokhorenkova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Message Passing Neural Networks have recently become the most popular approach to graph machine learning tasks; however, their receptive field is limited by the number of message passing layers. To increase the receptive field, Graph Transformers with global attention have been proposed; however, global attention does not take into account the graph topology and thus lacks graph-structure-based inductive biases, which are typically very important for graph machine learning tasks. In this work, we propose an alternative approach: cluster attention (CLATT). We divide graph nodes into clusters with off-the-shelf graph community detection algorithms and let each node attend to all other nodes in each cluster. CLATT provides large receptive fields while still having strong graph-structure-based inductive biases. We show that augmenting Message Passing Neural Networks or Graph Transformers with CLATT significantly improves their performance on a wide range of graph datasets including datasets from the recently introduced GraphLand benchmark representing real-world applications of graph machine learning.

---


### 27. [Differentially Private Modeling of Disease Transmission within Human Contact Networks](https://arxiv.org/abs/2604.07493)

**<font color=#1a73e8>作者：</font>** Shlomi Hod, Debanuj Nayak, Jason R. Gantenberg 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Epidemiologic studies of infectious diseases often rely on models of contact networks to capture the complex interactions that govern disease spread, and ongoing projects aim to vastly increase the scale at which such data can be collected. However, contact networks may include sensitive information, such as sexual relationships or drug use behavior. Protecting individual privacy while maintaining the scientific usefulness of the data is crucial. We propose a privacy-preserving pipeline for disease spread simulation studies based on a sensitive network that integrates differential privacy (DP) with statistical network models such as stochastic block models (SBMs) and exponential random graph models (ERGMs). Our pipeline comprises three steps: (1) compute network summary statistics using \emph{node-level} DP (which corresponds to protecting individuals' contributions); (2) fit a statistical model, like an ERGM, using these summaries, which allows generating synthetic networks reflecting the structure of the original network; and (3) simulate disease spread on the synthetic networks using an agent-based model. We evaluate the effectiveness of our approach using a simple Susceptible-Infected-Susceptible (SIS) disease model under multiple configurations. We compare both numerical results, such as simulated disease incidence and prevalence, as well as qualitative conclusions such as intervention effect size, on networks generated with and without differential privacy constraints. Our experiments are based on egocentric sexual network data from the ARTNet study (a survey about HIV-related behaviors). Our results show that the noise added for privacy is small relative to other sources of error (sampling and model misspecification). This suggests that, in principle, curators of such sensitive data can provide valuable epidemiologic insights while protecting privacy.

---


### 28. [Rhizome OS-1: Rhizome's Semi-Autonomous Operating System for Small Molecule Drug Discovery](https://arxiv.org/abs/2604.07512)

**<font color=#1a73e8>作者：</font>** Yiwen Wang, Gregory Sinenka, Xhuliano Brace  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce a semi-autonomous discovery system in which multi-modal AI agents function as a multi-disciplinary discovery team, acting as computational chemists, medicinal chemists, and patent agents, writing and executing analysis code, visually evaluating molecular candidates, assessing patentability, and adapting generation strategy from empirical screening feedback, while r1, a 246M-parameter Graph Neural Network (GNN) trained on 800M molecules, generates novel chemical matter directly on molecular graphs. Agents executed two campaigns in oncology (BCL6, EZH2), formulating medicinal chemistry hypotheses across three strategy tiers and generating libraries of 2,355-2,876 novel molecules per target. Across both targets, 91.9% of generated Murcko scaffolds are absent from ChEMBL for their respective targets, with Tanimoto distances of 0.56-0.69 to the nearest known active, confirming that the engine produces structurally distinct chemical matter rather than recapitulating known compounds. Binding affinity predictions using Boltz-2 were calibrated against ChEMBL experimental data, achieving Spearman correlations of -0.53 to -0.64 and ROC AUC values of 0.88 to 0.93. These results demonstrate that semi-autonomous agent systems, equipped with graph-native generative tools and physics-informed scoring, provide a foundation for a modern operating system for small molecule discovery. We show that Rhizome OS-1 enables a new paradigm for early-stage drug discovery by supporting scaled, rapid, and adaptive inverse design.

---


### 29. [Decompose, Look, and Reason: Reinforced Latent Reasoning for VLMs](https://arxiv.org/abs/2604.07518)

**<font color=#1a73e8>作者：</font>** Mengdan Zhu, Senhao Cheng, Liang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models often struggle with complex visual reasoning due to the visual information loss in textual CoT. Existing methods either add the cost of tool calls or rely on localized patch-based embeddings that are insufficient to extract semantics in multi-step reasoning. We propose \emph{"Decompose, Look, and Reason" (DLR)}, a reinforced latent reasoning framework that dynamically decomposes queries into textual premises, extracts premise-conditioned continuous visual latents, and deduces answers through grounded rationales. We introduce a three-stage training pipeline and propose a novel Spherical Gaussian Latent Policy to enable effective exploration in the latent space. Extensive experiments on vision-centric benchmarks show that DLR consistently outperforms strong baselines, including text-only, interleaved multimodal CoT, and latent reasoning methods, while providing superior stepwise interpretability.

---


### 30. [Training-free Spatially Grounded Geometric Shape Encoding (Technical Report)](https://arxiv.org/abs/2604.07522)

**<font color=#1a73e8>作者：</font>** Yuhang He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Positional encoding has become the de facto standard for grounding deep neural networks on discrete point-wise positions, and it has achieved remarkable success in tasks where the input can be represented as a one-dimensional sequence. However, extending this concept to 2D spatial geometric shapes demands carefully designed encoding strategies that account not only for shape geometry and pose, but also for compatibility with neural network learning. In this work, we address these challenges by introducing a training-free, general-purpose encoding strategy, dubbed XShapeEnc, that encodes an arbitrary spatially grounded 2D geometric shape into a compact representation exhibiting five favorable properties, including invertibility, adaptivity, and frequency richness. Specifically, a 2D spatially grounded geometric shape is decomposed into its normalized geometry within the unit disk and its pose vector, where the pose is further transformed into a harmonic pose field that also lies within the unit disk. A set of orthogonal Zernike bases is constructed to encode shape geometry and pose either independently or jointly, followed by a frequency-propagation operation to introduce high-frequency content into the encoding. We demonstrate the theoretical validity, efficiency, discriminability, and applicability of XShapeEnc via extensive analysis and experiments across a wide range of shape-aware tasks and our self-curated XShapeCorpus. We envision XShapeEnc as a foundational tool for research that goes beyond one-dimensional sequential data toward frontier 2D spatial intelligence.

---


### 31. [Learning Markov Processes as Sum-of-Square Forms for Analytical Belief Propagation](https://arxiv.org/abs/2604.07525)

**<font color=#1a73e8>作者：</font>** Peter Amorese, Morteza Lahijanian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Harnessing the predictive capability of Markov process models requires propagating probability density functions (beliefs) through the model. For many existing models however, belief propagation is analytically infeasible, requiring approximation or sampling to generate predictions. This paper proposes a functional modeling framework leveraging sparse Sum-of-Squares (SoS) forms for valid (conditional) density estimation. We study the theoretical restrictions of modeling conditional densities using the SoS form, and propose a novel functional form for addressing such limitations. The proposed architecture enables generalized simultaneous learning of basis functions and coefficients, while preserving analytical belief propagation. In addition, we propose a training method that allows for exact adherence to the normalization and non-negativity constraints. Our results show that the proposed method achieves accuracy comparable to state-of-the-art approaches while requiring significantly less memory in low-dimensional spaces, and it further scales to 12D systems when existing methods fail beyond 2D.

---


### 32. [Trust the AI, Doubt Yourself: The Effect of Urgency on Self-Confidence in Human-AI Interaction](https://arxiv.org/abs/2604.07535)

**<font color=#1a73e8>作者：</font>** Baran Shajari, Xiaoran Liu, Kyanna Dagenais 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Studies show that interactions with an AI system fosters trust in human users towards AI. An often overlooked element of such interaction dynamics is the (sense of) urgency when the human user is prompted by an AI agent, e.g., for advice or guidance. In this paper, we show that although the presence of urgency in human-AI interactions does not affect the trust in AI, it may be detrimental to the human user's self-confidence and self-efficacy. In the long run, the loss of confidence may lead to performance loss, suboptimal decisions, human errors, and ultimately, unsustainable AI systems. Our evidence comes from an experiment with 30 human participants. Our results indicate that users may feel more confident in their work when they are eased into the human-AI setup rather than exposed to it without preparation. We elaborate on the implications of this finding for software engineers and decision-makers.

---


### 33. [The Day My Chatbot Changed: Characterizing the Mental Health Impacts of Social AI App Updates via Negative User Reviews](https://arxiv.org/abs/2604.07548)

**<font color=#1a73e8>作者：</font>** Sirajam Munira, Lydia Manikonda  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) chatbots are increasingly used for emotional, creative, and social support, leading to sustained and routine user interaction with these systems. As these applications evolve through frequent version updates, changes in functionality or behavior may influence how users evaluate them. However, work on how publicly expressed user feedback varies across app versions in real-world deployment contexts is limited. This study analyzes 210,840 Google Play reviews of the chatbot application Character AI, linking each review to the app version active at the time of posting. We specifically examine negative reviews to study how version-level rating trends, and linguistic patterns reflect user experiences. Our results show that user ratings fluctuate across successive versions, with certain releases associated with stronger negative evaluations. Thematic analysis indicates that dissatisfaction is concentrated around recurring issues related to technical malfunctions and errors. A subset of reviews additionally frames these concerns in terms of potential psychological or addiction-related effects. The findings highlight how aggregate user evaluations and expressed concerns vary across software iterations and provide empirical insight into how update cycles relate to user feedback patterns and underscore the importance of stability and transparent communication in evolving AI systems.

---


### 34. [Validated Synthetic Patient Generation for Small Longitudinal Cohorts: Coagulation Dynamics Across Pregnancy](https://arxiv.org/abs/2604.07557)

**<font color=#1a73e8>作者：</font>** Jeffrey D. Varner, Maria Cristina Bravo, Carole McBride 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small longitudinal clinical cohorts, common in maternal health, rare diseases, and early-phase trials, limit computational modeling: too few patients to train reliable models, yet too costly and slow to expand through additional enrollment. We present multiplicity-weighted Stochastic Attention (SA), a generative framework based on modern Hopfield network theory that addresses this gap. SA embeds real patient profiles as memory patterns in a continuous energy landscape and generates novel synthetic patients via Langevin dynamics that interpolate between stored patterns while preserving the geometry of the original cohort. Per-pattern multiplicity weights enable targeted amplification of rare clinical subgroups at inference time without retraining. We applied SA to a longitudinal coagulation dataset from 23 pregnant patients spanning 72 biochemical features across 3 visits (pre-pregnancy baseline, first trimester, and third trimester), including rare subgroups such as polycystic ovary syndrome and preeclampsia. Synthetic patients generated by SA were statistically, structurally, and mechanistically indistinguishable from their real counterparts across multiple independent validation tests, including an ordinary differential equation model of the coagulation cascade. A downstream utility test further showed that a mechanistic model calibrated entirely on synthetic patients predicted held-out real patient outcomes as well as one calibrated on real data. These results demonstrate that SA can produce clinically useful synthetic cohorts from very small longitudinal datasets, enabling data-augmented modeling in small-cohort settings.

---


### 35. [Generative Experiences for Digital Mental Health Interventions: Evidence from a Randomized Study](https://arxiv.org/abs/2604.07558)

**<font color=#1a73e8>作者：</font>** Ananya Bhattacharjee, Michael Liut, Matthew Jörke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital mental health (DMH) tools have extensively explored personalization of interventions to users' needs and contexts. However, this personalization often targets what support is provided, not how it is experienced. Even well-matched content can fail when the interaction format misaligns with how someone can engage. We introduce generative experience as a paradigm for DMH support, where the intervention experience is composed at runtime. We instantiate this in GUIDE, a system that generates personalized intervention content and multimodal interaction structure through rubric-guided generation of modular components. In a preregistered study with N = 237 participants, GUIDE significantly reduced stress (p = .02) and improved the user experience (p = .04) compared to an LLM-based cognitive restructuring control. GUIDE also supported diverse forms of reflection and action through varied interaction flows, while revealing tensions around personalization across the interaction sequence. This work lays the foundation for interventions that dynamically shape how support is experienced and enacted in digital settings.

---


### 36. [Dual-Loop Control in DCVerse: Advancing Reliable Deployment of AI in Data Centers via Digital Twins](https://arxiv.org/abs/2604.07559)

**<font color=#1a73e8>作者：</font>** Qingang Zhang, Yuejun Yan, Guangyu Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing scale and complexity of modern data centers present major challenges in balancing energy efficiency with outage risk. Although Deep Reinforcement Learning (DRL) shows strong potential for intelligent control, its deployment in mission-critical systems is limited by data scarcity and the lack of real-time pre-evaluation mechanisms. This paper introduces the Dual-Loop Control Framework (DLCF), a digital twin-based architecture designed to overcome these challenges. The framework comprises three core entities: the physical system, a digital twin, and a policy reservoir of diverse DRL agents. These components interact through a dual-loop mechanism involving real-time data acquisition, data assimilation, DRL policy training, pre-evaluation, and expert verification. Theoretical analysis shows how DLCF can improve sample efficiency, generalization, safety, and optimality. Leveraging DLCF, we implemented the DCVerse platform and validated it through case studies on a real-world data center cooling system. The evaluation shows that our approach achieves up to 4.09% energy savings over conventional control strategies without violating SLA requirements. Additionally, the framework improves policy interpretability and supports more trustworthy DRL deployment. This work provides a foundation for reliable AI-based control in data centers and points toward future extensions for holistic, system-wide optimization.

---


### 37. [On the Uphill Battle of Image frequency Analysis](https://arxiv.org/abs/2604.07563)

**<font color=#1a73e8>作者：</font>** Nader Bazyari, Hedieh Sajedi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work is a follow up on the newly proposed clustering algorithm called The Inverse Square Mean Shift Algorithm. In this paper a special case of algorithm for dealing with non-homogenous data is formulated and the three dimensional Fast Fourier Transform of images is investigated with the aim of finding hidden patterns.

---


### 38. [MEV-ACE: Identity-Authenticated Fair Ordering for Proposer-Controlled MEV Mitigation](https://arxiv.org/abs/2604.07568)

**<font color=#1a73e8>作者：</font>** Jian Sheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Maximal Extractable Value, or MEV, remains a structural threat to blockchain fairness because a block producer can often observe pending transactions and unilaterally decide their ordering or inclusion. Existing mitigations hide transaction contents or outsource ordering, but they often leave two gaps unresolved. First, commitments are not authenticated by slashable identities. Second, inclusion obligations are not backed by transferable evidence that other validators can verify. This paper presents MEV ACE, a fair ordering protocol for proposer controlled ordering MEV. MEV ACE combines three mechanisms. First, it uses registered economic identities whose authentication keys are deterministically derived from the ACE GF framework and bonded on chain. Second, it uses authenticated commit and open messages with validator receipt thresholds, which make admissibility and inclusion obligations independently auditable. Third, it uses verifiable delay based randomness to determine transaction order only after the admissible commitment set is fixed. We formalize the protocol in a Byzantine fault tolerant validator model with threshold receipts and show three properties under standard assumptions: order unpredictability after the admissible set is locked, commitment authenticity under signature unforgeability, and accountable inclusion for transactions that obtain threshold commit and open receipts. Under these conditions, and when producer and user bonds exceed the one slot gain from invalid execution or selective non opening, MEV ACE removes unilateral proposer discretion over front running, sandwich attacks, and censorship against admitted transactions. The protocol remains single slot in structure, requires no threshold decryption committee, and is compatible with post quantum signature schemes such as ML DSA 44.

---


### 39. [Mathematical Analysis of Image Matching Techniques](https://arxiv.org/abs/2604.07574)

**<font color=#1a73e8>作者：</font>** Oleh Samoilenko  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image matching is a fundamental problem in Computer Vision with direct applications in robotics, remote sensing, and geospatial data analysis. We present an analytical and experimental evaluation of classical local feature-based image matching algorithms on satellite imagery, focusing on the Scale-Invariant Feature Transform (SIFT) and the Oriented FAST and Rotated BRIEF (ORB). Each method is evaluated through a common pipeline: keypoint detection, descriptor extraction, descriptor matching, and geometric verification via RANSAC with homography estimation. Matching quality is assessed using the Inlier Ratio - the fraction of correspondences consistent with the estimated homography. The study uses a manually constructed dataset of GPS-annotated satellite image tiles with intentional overlaps. We examine the impact of the number of extracted keypoints on the resulting Inlier Ratio.

---


### 40. [Event-Level Detection of Surgical Instrument Handovers in Videos with Interpretable Vision Models](https://arxiv.org/abs/2604.07577)

**<font color=#1a73e8>作者：</font>** Katerina Katsarou, George Zountsas, Karam Tomotaki-Dawoud 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable monitoring of surgical instrument exchanges is essential for maintaining procedural efficiency and patient safety in the operating room. Automatic detection of instrument handovers in intraoperative video remains challenging due to frequent occlusions, background clutter, and the temporally evolving nature of interaction events. We propose a spatiotemporal vision framework for event-level detection and direction classification of surgical instrument handovers in surgical videos. The model combines a Vision Transformer (ViT) backbone for spatial feature extraction with a unidirectional Long Short-Term Memory (LSTM) network for temporal aggregation. A unified multi-task formulation jointly predicts handover occurrence and interaction direction, enabling consistent modeling of transfer dynamics while avoiding error propagation typical of cascaded pipelines. Predicted confidence scores form a temporal signal over the video, from which discrete handover events are identified via peak detection. Experiments on a dataset of kidney transplant procedures demonstrate strong performance, achieving an F1-score of 0.84 for handover detection and a mean F1-score of 0.72 for direction classification, outperforming both a single-task variant and a VideoMamba-based baseline for direction prediction while maintaining comparable detection performance. To improve interpretability, we employ Layer-CAM attribution to visualize spatial regions driving model decisions, highlighting hand-instrument interaction cues.

---


### 41. [MSGL-Transformer: A Multi-Scale Global-Local Transformer for Rodent Social Behavior Recognition](https://arxiv.org/abs/2604.07578)

**<font color=#1a73e8>作者：</font>** Muhammad Imran Sharif, Doina Caragea  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognition of rodent behavior is important for understanding neural and behavioral mechanisms. Traditional manual scoring is time-consuming and prone to human error. We propose MSGL-Transformer, a Multi-Scale Global-Local Transformer for recognizing rodent social behaviors from pose-based temporal sequences. The model employs a lightweight transformer encoder with multi-scale attention to capture motion dynamics across different temporal scales. The architecture integrates parallel short-range, medium-range, and global attention branches to explicitly capture behavior dynamics at multiple temporal scales. We also introduce a Behavior-Aware Modulation (BAM) block, inspired by SE-Networks, which modulates temporal embeddings to emphasize behavior-relevant features prior to attention. We evaluate on two datasets: RatSI (5 behavior classes, 12D pose inputs) and CalMS21 (4 behavior classes, 28D pose inputs). On RatSI, MSGL-Transformer achieves 75.4% mean accuracy and F1-score of 0.745 across nine cross-validation splits, outperforming TCN, LSTM, and Bi-LSTM. On CalMS21, it achieves 87.1% accuracy and F1-score of 0.8745, a +10.7% improvement over HSTWFormer, and outperforms ST-GCN, MS-G3D, CTR-GCN, and STGAT. The same architecture generalizes across both datasets with only input dimensionality and number of classes adjusted.

---


### 42. [Interpreting the Error of Differentially Private Median Queries through Randomization Intervals](https://arxiv.org/abs/2604.07581)

**<font color=#1a73e8>作者：</font>** Thomas Humphries, Tim Li, Shufan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> It can be difficult for practitioners to interpret the quality of differentially private (DP) statistics due to the added noise. One method to help analysts understand the amount of error introduced by DP is to return a Randomization Interval (RI), along with the statistic. A RI is a type of confidence interval that bounds the error introduced by DP. For queries where the noise distribution depends on the input, such as the median, prior work degrades the quality of the median itself to obtain a high-quality RI. In this work, we propose PostRI, a solution to compute a RI after the median has been estimated. PostRI enables a median estimation with 14%-850% higher utility than related work, while maintaining a narrow RI.

---


### 43. [COSMIC: Emotionally Intelligent Agents to Support Mental and Emotional Well-being in Extreme Isolation: Lessons from Analog Astronaut Training Missions](https://arxiv.org/abs/2604.07589)

**<font color=#1a73e8>作者：</font>** A. Xygkou-Tsiamoulou, Alexandra Covaci, Zeqi Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As humanity pivots toward long-duration interplanetary travel, the psychological constraints of Isolated and Confined Environments (ICE) emerge as a primary mission risk. This paper presents COSMIC (COmpanion System for Mission Interaction and Communication) representing the inaugural investigation into the deployment of a high-fidelity, emotionally intelligent AI companion in an analog astronaut setting. By integrating a Large Language Model (LLM) architecture with a diffusion-based digital avatar interface, COSMIC transcends traditional task-oriented automation to provide longitudinal affective support. We detail a modular system architecture designed for temporal continuity through short- and long-term memory systems and outline a robust naturalistic observational framework for evaluating psychological resilience at the LunAres Research Station. This work constitutes the first formal submission in the field to evaluate the efficacy of state-of-the-art generative AI and synthesized visual empathy in mitigating the effects of extreme isolation.

---


### 44. [Too long; didn't solve](https://arxiv.org/abs/2604.07593)

**<font color=#1a73e8>作者：</font>** Lucía M. Cabrera, Isaac Saxton-Knight  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical benchmarks consisting of a range of mathematics problems are widely used to evaluate the reasoning abilities of large language models, yet little is known about how their structural properties influence model behaviour. In this work, we investigate two structural length variables, prompt length and solution length, and analyse how they relate to model performance on a newly constructed adversarial dataset of expert-authored mathematics problems. We find that both prompt and solution lengths correlate positively with increased model failure across models. We also include a secondary, exploratory analysis of cross-model disagreement. Under a difficulty-adjusted normalised analysis, both variables retain weak negative associations with realised model separation, slightly stronger for prompt length. Overall, our main robust finding is that structural length is linked to empirical difficulty in this dataset.

---


### 45. [Reasoning Graphs: Deterministic Agent Accuracy through Evidence-Centric Chain-of-Thought Feedback](https://arxiv.org/abs/2604.07595)

**<font color=#1a73e8>作者：</font>** Matthew Penaroza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model agents reason from scratch on every query: each time an agent retrieves evidence and deliberates, the chain of thought is discarded and the next similar query starts with no prior insight. This produces lower accuracy and high variance, as the same type of query can succeed or fail unpredictably. We introduce reasoning graphs, a graph structure that persists an agent's per-evidence chain of thought as structured edges connected to the evidence items they evaluate. Unlike prior memory mechanisms that store distilled strategies as flat records indexed by query similarity or appended by recency, reasoning graphs enable evidence-centric feedback: given a new candidate set, the system traverses all incoming evaluation edges for each evidence item across all prior runs, surfacing how that specific item has been judged before. This backward traversal from evidence inward is a structurally different capability from query-similarity retrieval, because the feedback is tied to the specific evidence the agent is currently examining, not to the query. We further introduce retrieval graphs, a complementary structure that feeds a pipeline planner to tighten the candidate funnel over successive runs. Together, both graphs form a self-improving feedback loop: accuracy rises and variance collapses over successive runs, with every decision fully traceable through the graph. This improvement requires no retraining; the base model remains frozen and all gains come from context engineering via graph traversal. We formalize the graph structure, traversal algorithms, and feedback mechanisms, and describe a sequential cluster evaluation protocol for measuring accuracy convergence and variance collapse on multi-hop question answering benchmarks.

---


### 46. [Implicit Regularization and Generalization in Overparameterized Neural Networks](https://arxiv.org/abs/2604.07603)

**<font color=#1a73e8>作者：</font>** Zeran Johannsen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical statistical learning theory predicts that overparameterized models should exhibit severe overfitting, yet modern deep neural networks with far more parameters than training samples consistently generalize well. This contradiction has become a central theoretical question in machine learning.
This study investigates the role of optimization dynamics and implicit regularization in enabling generalization in overparameterized neural networks through controlled experiments. We examine stochastic gradient descent (SGD) across batch sizes, the geometry of flat versus sharp minima via Hessian eigenvalue estimation and weight perturbation analysis, the Neural Tangent Kernel (NTK) regime through wide-network experiments, double descent across model scales, and the Lottery Ticket Hypothesis through iterative magnitude pruning. All experiments use PyTorch on CIFAR-10 and MNIST with multiple random seeds.
Our findings demonstrate that generalization is strongly influenced by the interaction between network architecture, optimization algorithms, and loss landscape geometry. Smaller batch sizes consistently produced lower test error and flatter minima, with an 11.8x difference in top Hessian eigenvalue between small-batch and large-batch solutions corresponding to 1.61 percentage points higher test accuracy. Sparse subnetworks retaining only 10% of parameters achieved within 1.15 percentage points of full model performance when retrained from their original initialization. These results highlight the need for revised learning-theoretic frameworks capable of explaining generalization in high-dimensional model regimes.

---


### 47. [Auto-Configured Networks for Multi-Scale Multi-Output Time-Series Forecasting](https://arxiv.org/abs/2604.07610)

**<font color=#1a73e8>作者：</font>** Yumeng Zha, Shengxiang Yang, Xianpeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial forecasting often involves multi-source asynchronous signals and multi-output targets, while deployment requires explicit trade-offs between prediction error and model complexity. Current practices typically fix alignment strategies or network designs, making it difficult to systematically co-design preprocessing, architecture, and hyperparameters in budget-limited training-based evaluations. To address this issue, we propose an auto-configuration framework that outputs a deployable Pareto set of forecasting models balancing error and complexity. At the model level, a Multi-Scale Bi-Branch Convolutional Neural Network (MS--BCNN) is developed, where short- and long-kernel branches capture local fluctuations and long-term trends, respectively, for multi-output regression. At the search level, we unify alignment operators, architectural choices, and training hyperparameters into a hierarchical-conditional mixed configuration space, and apply Player-based Hybrid Multi-Objective Evolutionary Algorithm (PHMOEA) to approximate the error--complexity Pareto frontier within a limited computational budget. Experiments on hierarchical synthetic benchmarks and a real-world sintering dataset demonstrate that our framework outperforms competitive baselines under the same budget and offers flexible deployment choices.

---


### 48. [ADAG: Automatically Describing Attribution Graphs](https://arxiv.org/abs/2604.07615)

**<font color=#1a73e8>作者：</font>** Aryaman Arora, Zhengxuan Wu, Jacob Steinhardt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In language model interpretability research, \textbf{circuit tracing} aims to identify which internal features causally contributed to a particular output and how they affected each other, with the goal of explaining the computations underlying some behaviour. However, all prior circuit tracing work has relied on ad-hoc human interpretation of the role that each feature in the circuit plays, via manual inspection of data artifacts such as the dataset examples the component activates on. We introduce \textbf{ADAG}, an end-to-end pipeline for describing these attribution graphs which is fully automated. To achieve this, we introduce \textit{attribution profiles} which quantify the functional role of a feature via its input and output gradient effects. We then introduce a novel clustering algorithm for grouping features, and an LLM explainer--simulator setup which generates and scores natural-language explanations of the functional role of these feature groups. We run our system on known human-analysed circuit-tracing tasks and recover interpretable circuits, and further show ADAG can find steerable clusters which are responsible for a harmful advice jailbreak in Llama 3.1 8B Instruct.

---


### 49. [DIVERSED: Relaxed Speculative Decoding via Dynamic Ensemble Verification](https://arxiv.org/abs/2604.07622)

**<font color=#1a73e8>作者：</font>** Ziyi Wang, Siva Rajesh Kasa, Ankith M S 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding is an effective technique for accelerating large language model inference by drafting multiple tokens in parallel. In practice, its speedup is often bottlenecked by a rigid verification step that strictly enforces the accepted token distribution to exactly match the target model. This constraint leads to the rejection of many plausible tokens, lowering the acceptance rate and limiting overall time speedup. To overcome this limitation, we propose Dynamic Verification Relaxed Speculative Decoding (DIVERSED), a relaxed verification framework that improves time efficiency while preserving generation quality. DIVERSED learns an ensemble-based verifier that blends the draft and target model distributions with a task-dependent and context-dependent weight. We provide theoretical justification for our approach and demonstrate empirically that DIVERSED achieves substantially higher inference efficiency compared to standard speculative decoding methods. Code is available at: this https URL.

---


### 50. [Behavior Latticing: Inferring User Motivations from Unstructured Interactions](https://arxiv.org/abs/2604.07629)

**<font color=#1a73e8>作者：</font>** Dora Zhao, Michelle S. Lam, Diyi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A long-standing vision of computing is the personal AI system: one that understands us well enough to address our underlying needs. Today's AI focuses on what users do, ignoring why they might be doing such things in the first place. As a result, AI systems default to optimizing or repeating existing behaviors (e.g., user has ChatGPT complete their homework) even when they run counter to users' needs (e.g., gaining subject expertise). Instead we require systems that can make connections across observations, synthesizing them into insights about the motivations underlying these behaviors (e.g., user's ongoing commitments make it difficult to prioritize learning despite expressed desire to do so). We introduce an architecture for building user understanding through behavior latticing, connecting seemingly disparate behaviors, synthesizing them into insights, and repeating this process over long spans of interaction data. Doing so affords new capabilities, including being able to infer users' needs rather than just their tasks and connecting subtle patterns to produce conclusions that users themselves may not have previously realized. In an evaluation, we validate that behavior latticing produces accurate insights about the user with significantly greater interpretive depth compared to state-of-the-art approaches. To demonstrate the new interactive capabilities that behavior lattices afford, we instantiate a personal AI agent steered by user insights, finding that our agent is significantly better at addressing users' needs while still providing immediate utility.

---


### 51. [Sheaf-Laplacian Obstruction and Projection Hardness for Cross-Modal Compatibility on a Modality-Independent Site](https://arxiv.org/abs/2604.07632)

**<font color=#1a73e8>作者：</font>** Tibor Sloboda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a unified framework for analyzing cross-modal compatibility in learned representations. The core object is a modality-independent neighborhood site on sample indices, equipped with a cellular sheaf of finite-dimensional real inner-product spaces. For a directed modality pair $(a\to b)$, we formalize two complementary incompatibility mechanisms: projection hardness, the minimal complexity within a nested Lipschitz-controlled projection family needed for a single global map to align whitened embeddings; and sheaf-Laplacian obstruction, the minimal spatial variation required by a locally fit field of projection parameters to achieve a target alignment error. The obstruction invariant is implemented via a projection-parameter sheaf whose 0-Laplacian energy exactly matches the smoothness penalty used in sheaf-regularized regression, making the theory directly operational. This separates two distinct failure modes: hardness failure, where no low-complexity global projection exists, and obstruction failure, where local projections exist but cannot be made globally consistent over the semantic neighborhood graph without large parameter variation. We link the sheaf spectral gap to stability of global alignment, derive bounds relating obstruction energy to excess global-map error under mild Lipschitz assumptions, and give explicit constructions showing that compatibility is generally non-transitive. We further define bridging via composed projection families and show, in a concrete ReLU setting, that an intermediate modality can strictly reduce effective hardness even when direct alignment remains infeasible.

---


### 52. [VSAS-BENCH: Real-Time Evaluation of Visual Streaming Assistant Models](https://arxiv.org/abs/2604.07634)

**<font color=#1a73e8>作者：</font>** Pavan Kumar Anasosalu Vasu, Cem Koc, Fartash Faghri 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming vision-language models (VLMs) continuously generate responses given an instruction prompt and an online stream of input frames. This is a core mechanism for real-time visual assistants. Existing VLM frameworks predominantly assess models in offline settings. In contrast, the performance of a streaming VLM depends on additional metrics beyond pure video understanding, including proactiveness, which reflects the timeliness of the model's responses, and consistency, which captures the robustness of its responses over time. To address this limitation, we propose VSAS-Bench, a new framework and benchmark for Visual Streaming Assistants. In contrast to prior benchmarks that primarily employ single-turn question answering on video inputs, VSAS-Bench features temporally dense annotations with over 18,000 annotations across diverse input domains and task types. We introduce standardized synchronous and asynchronous evaluation protocols, along with metrics that isolate and measure distinct capabilities of streaming VLMs. Using this framework, we conduct large-scale evaluations of recent video and streaming VLMs, analyzing the accuracy-latency trade-off under key design factors such as memory buffer length, memory access policy, and input resolution, yielding several practical insights. Finally, we show empirically that conventional VLMs can be adapted to streaming settings without additional training, and demonstrate that these adapted models outperform recent streaming VLMs. For example, Qwen3-VL-4B surpasses Dispider, the best streaming VLM on our benchmark, by 3% under the asynchronous protocol. The benchmark and code will be available at this https URL.

---


### 53. [From Uncertainty to Possibility: Early Computing Experiences for Rural Girls](https://arxiv.org/abs/2604.07638)

**<font color=#1a73e8>作者：</font>** Poornima Meegammana, Niranjan Meegammana, Chathurika Jayalath 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Girls remain underrepresented in computing, and rural contexts often compound barriers of access, language, and gender norms. Prior work in computing education highlights that confidence and belonging can shape participation, yet most evidence comes from well-resourced, English-dominant settings. Less is known about how locally grounded pathways can build programming self-efficacy and broaden career interest for adolescent girls. We addressed this gap by delivering a curriculum that began with digital foundations and unplugged problem-solving, then progressed to block-based programming activities, supported by parent awareness and teacher training in gender-responsive practices. Pre and post-surveys showed a reliable increase in programming self-efficacy, and career aspirations shifted toward technology. Complementary qualitative data indicate that mastery experiences, peer collaboration, and the creation of personal projects were key drivers of confidence, suggesting design priorities for scalable, locally relevant programmes in low-resource communities that can shift perceptions of who belongs in computing.

---


### 54. [Narrix: Remixing Narrative Strategies from Examples for Story Writing](https://arxiv.org/abs/2604.07643)

**<font color=#1a73e8>作者：</font>** Chao Zhang, Shunan Guo, Abe Davis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Experienced storytellers decompose stories into local narrative strategies and how these strategies shape higher-level arcs. This decomposition helps writers recognize patterns in others' work and adapt those patterns to tell new stories. Novices, however, struggle to identify these strategies or to reuse them effectively. We present Narrix, a novel writing tool that helps novice writers recognize narrative strategies in example stories and repurpose these strategies in their own writing. Narrix analyzes strategies in example stories, highlights them with color-coded lexical cues and explanations, and situates them on an interactive story arc for exploration by emotional shifts and turning points. Writers then drag strategies onto multi-dimensional tracks and apply block-scoped edits to revise or continue their drafts through controlled generation steered by specified strategies. Through a within-subjects study (N=12), Narrix showed improved participants' retention, confidence, and creative adaptation of narrative strategies compared to a baseline chat-based writing interface.

---


### 55. [PRIME: Training Free Proactive Reasoning via Iterative Memory Evolution for User-Centric Agent](https://arxiv.org/abs/2604.07645)

**<font color=#1a73e8>作者：</font>** Prince Zizhuang Wang, Shuli Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The development of autonomous tool-use agents for complex, long-horizon tasks in collaboration with human users has become the frontier of agentic research. During multi-turn Human-AI interactions, the dynamic and uncertain nature of user demands poses a significant challenge; agents must not only invoke tools but also iteratively refine their understanding of user intent through effective communication. While recent advances in reinforcement learning offer a path to more capable tool-use agents, existing approaches require expensive training costs and struggle with turn-level credit assignment across extended interaction horizons. To this end, we introduce PRIME (Proactive Reasoning via Iterative Memory Evolution), a gradient-free learning framework that enables continuous agent evolvement through explicit experience accumulation rather than expensive parameter optimization. PRIME distills multi-turn interaction trajectories into structured, human-readable experiences organized across three semantic zones: successful strategies, failure patterns, and user preferences. These experiences evolve through meta-level operations and guide future agent behavior via retrieval-augmented generation. Our experiments across several diverse user-centric environments demonstrate that PRIME achieves competitive performance with gradient-based methods while offering cost-efficiency and interpretability. Together, PRIME presents a practical paradigm for building proactive, collaborative agents that learn from Human-AI interaction without the computational burden of gradient-based training.

---


### 56. [Cognitive-Causal Multi-Task Learning with Psychological State Conditioning for Assistive Driving Perception](https://arxiv.org/abs/2604.07651)

**<font color=#1a73e8>作者：</font>** Keito Inoshita, Nobuhiro Hayashida, Akira Imanishi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task learning for advanced driver assistance systems requires modeling the complex interplay between driver internal states and external traffic environments. However, existing methods treat recognition tasks as flat and independent objectives, failing to exploit the cognitive causal structure underlying driving behavior. In this paper, we propose CauPsi, a cognitive science-grounded causal multi-task learning framework that explicitly models the hierarchical dependencies among Traffic Context Recognition (TCR), Vehicle Context Recognition (VCR), Driver Emotion Recognition (DER), and Driver Behavior Recognition (DBR). The proposed framework introduces two key mechanisms. First, a Causal Task Chain propagates upstream task predictions to downstream tasks via learnable prototype embeddings, realizing the cognitive cascade from environmental perception to behavioral regulation in a differentiable manner. Second, Cross-Task Psychological Conditioning (CTPC) estimates a psychological state signal from driver facial expressions and body posture and injects it as a conditioning input to all tasks including environmental recognition, thereby modeling the modulatory effect of driver internal states on cognitive and decision-making processes. Evaluated on the AIDE dataset, CauPsi achieves a mean accuracy of 82.71% with only 5.05M parameters, surpassing prior work by +1.0% overall, with notable improvements on DER (+3.65%) and DBR (+7.53%). Ablation studies validate the independent contribution of each component, and analysis of the psychological state signal confirms that it acquires systematic task-label-dependent patterns in a self-supervised manner without explicit psychological annotations.

---


### 57. [Optimal Decay Spectra for Linear Recurrences](https://arxiv.org/abs/2604.07658)

**<font color=#1a73e8>作者：</font>** Yang Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear recurrent models offer linear-time sequence processing but often suffer from suboptimal long-range memory. We trace this to the decay spectrum: for $N$ channels, random initialization collapses the minimum spectral gap to $O(N^{-2})$, yielding sub-exponential error $\exp(-\Omega(N/\log N))$; linear spacing avoids collapse but degrades to $\exp(-O(N/\sqrt{T}))$, practically algebraic over long contexts. We introduce Position-Adaptive Spectral Tapering (PoST), an architecture-agnostic framework combining two mechanisms: (1) Spectral Reparameterization, which structurally enforces geometrically spaced log-decay rates, proven minimax optimal at rate $O(\exp(-cN/\log T))$; and (2) Position-Adaptive Scaling, the provably unique mechanism that eliminates the scale mismatch of static spectra (where only $N\log t/\log T$ of $N$ channels are effective at position $t$) by stretching the spectrum to the actual dependency range, sharpening the rate to $O(\exp(-cN/\log t))$. This scaling natively induces fractional invariance: the impulse response becomes scale-free, with channels interpolating between relative and absolute temporal coordinates. PoST integrates into any diagonal linear recurrence without overhead. We instantiate it across Mamba-2, RWKV-7, Gated DeltaNet, Gated Linear Attention, and RetNet. Pre-training at 180M-440M scales shows consistent zero-shot language modeling improvements, significant long-context retrieval gains for Mamba-2 (MQAR and NIAH), and competitive or improved performance across other architectures. Code: this https URL.

---


### 58. [Monocular Depth Estimation From the Perspective of Feature Restoration: A Diffusion Enhanced Depth Restoration Approach](https://arxiv.org/abs/2604.07664)

**<font color=#1a73e8>作者：</font>** Huibin Bai, Shuai Li, Hanxiao Zhai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular Depth Estimation (MDE) is a fundamental computer vision task with important applications in 3D vision. The current mainstream MDE methods employ an encoder-decoder architecture with multi-level/scale feature processing. However, the limitations of the current architecture and the effects of different-level features on the prediction accuracy are not evaluated. In this paper, we first investigate the above problem and show that there is still substantial potential in the current framework if encoder features can be improved. Therefore, we propose to formulate the depth estimation problem from the feature restoration perspective, by treating pretrained encoder features as degraded features of an assumed ground truth feature that yields the ground truth depth map. Then an Invertible Transform-enhanced Indirect Diffusion (InvT-IndDiffusion) module is developed for feature restoration. Due to the absence of direct supervision on feature, only indirect supervision from the final sparse depth map is used. During the iterative procedure of diffusion, this results in feature deviations among steps. The proposed InvT-IndDiffusion solves this problem by using an invertible transform-based decoder under the bi-Lipschitz condition. Finally, a plug-and-play Auxiliary Viewpoint-based Low-level Feature Enhancement module (AV-LFE) is developed to enhance local details with auxiliary viewpoint when available. Experiments demonstrate that the proposed method achieves better performance than the state-of-the-art methods on various datasets. Specifically on the KITTI benchmark, compared with the baseline, the performance is improved by 4.09% and 37.77% under different training settings in terms of RMSE. Code is available at this https URL.

---


### 59. [Adaptive Depth-converted-Scale Convolution for Self-supervised Monocular Depth Estimation](https://arxiv.org/abs/2604.07665)

**<font color=#1a73e8>作者：</font>** Yanbo Gao, Huibin Bai, Huasong Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised monocular depth estimation (MDE) has received increasing interests in the last few years. The objects in the scene, including the object size and relationship among different objects, are the main clues to extract the scene structure. However, previous works lack the explicit handling of the changing sizes of the object due to the change of its depth. Especially in a monocular video, the size of the same object is continuously changed, resulting in size and depth ambiguity. To address this problem, we propose a Depth-converted-Scale Convolution (DcSConv) enhanced monocular depth estimation framework, by incorporating the prior relationship between the object depth and object scale to extract features from appropriate scales of the convolution receptive field. The proposed DcSConv focuses on the adaptive scale of the convolution filter instead of the local deformation of its shape. It establishes that the scale of the convolution filter matters no less (or even more in the evaluated task) than its local deformation. Moreover, a Depth-converted-Scale aware Fusion (DcS-F) is developed to adaptively fuse the DcSConv features and the conventional convolution features. Our DcSConv enhanced monocular depth estimation framework can be applied on top of existing CNN based methods as a plug-and-play module to enhance the conventional convolution block. Extensive experiments with different baselines have been conducted on the KITTI benchmark and our method achieves the best results with an improvement up to 11.6% in terms of SqRel reduction. Ablation study also validates the effectiveness of each proposed module.

---


### 60. [FireSenseNet: A Dual-Branch CNN with Cross-Attentive Feature Interaction for Next-Day Wildfire Spread Prediction](https://arxiv.org/abs/2604.07675)

**<font color=#1a73e8>作者：</font>** Jinzhen Han, JinByeong Lee, Hak Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of next-day wildfire spread is critical for disaster response and resource allocation. Existing deep learning approaches typically concatenate heterogeneous geospatial
inputs into a single tensor, ignoring the fundamental physical distinction between static fuel/terrain properties and dynamic meteorological conditions. We propose FireSenseNet, a
dual-branch convolutional neural network equipped with a novel Cross-Attentive Feature Interaction Module (CAFIM) that explicitly models the spatially varying interaction between fuel and
weather modalities through learnable attention gates at multiple encoder scales. Through a systematic comparison of seven architectures -- spanning pure CNNs, Vision Transformers, and hybrid
designs -- on the Google Next-Day Wildfire Spread benchmark, we demonstrate that FireSenseNet achieves an F1 of 0.4176 and AUC-PR of 0.3435, outperforming all alternatives including a
SegFormer with 3.8* more parameters (F1 = 0.3502). Ablation studies confirm that CAFIM provides a 7.1% relative F1 gain over naive concatenation, and channel-wise feature importance
analysis reveals that the previous-day fire mask dominates prediction while wind speed acts as noise at the dataset's coarse temporal resolution. We further incorporate Monte Carlo Dropout
for pixel-level uncertainty quantification and present a critical analysis showing that common evaluation shortcuts inflate reported F1 scores by over 44%.

---


### 61. [Tensor-based computation of the Koopman generator via operator logarithm](https://arxiv.org/abs/2604.07685)

**<font color=#1a73e8>作者：</font>** Tatsuya Kishimoto, Jun Ohkubo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying governing equations of nonlinear dynamical systems from data is challenging. While sparse identification of nonlinear dynamics (SINDy) and its extensions are widely used for system identification, operator-logarithm approaches use the logarithm to avoid time differentiation, enabling larger sampling intervals. However, they still suffer from the curse of dimensionality. Then, we propose a data-driven method to compute the Koopman generator in a low-rank tensor train (TT) format by taking logarithms of Koopman eigenvalues while preserving the TT format. Experiments on 4-dimensional Lotka-Volterra and 10-dimensional Lorenz-96 systems show accurate recovery of vector field coefficients and scalability to higher-dimensional systems.

---


### 62. [Joint Task Offloading, Inference Optimization and UAV Trajectory Planning for Generative AI Empowered Intelligent Transportation Digital Twin](https://arxiv.org/abs/2604.07687)

**<font color=#1a73e8>作者：</font>** Xiaohuan Li, Junchuan Fan, Bingqi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To implement the intelligent transportation digital twin (ITDT), unmanned aerial vehicles (UAVs) are scheduled to process the sensing data from the roadside sensors. At this time, generative artificial intelligence (GAI) technologies such as diffusion models are deployed on the UAVs to transform the raw sensing data into the high-quality and valuable. Therefore, we propose the GAI-empowered ITDT. The dynamic processing of a set of diffusion model inference (DMI) tasks on the UAVs with dynamic mobility simultaneously influences the DT updating fidelity and delay. In this paper, we investigate a joint optimization problem of DMI task offloading, inference optimization and UAV trajectory planning as the system utility maximization (SUM) problem to address the fidelity-delay tradeoff for the GAI-empowered ITDT. To seek a solution to the problem under the network dynamics, we model the SUM problem as the heterogeneous-agent Markov decision process, and propose the sequential update-based heterogeneous-agent twin delayed deep deterministic policy gradient (SU-HATD3) algorithm, which can quickly learn a near-optimal solution. Numerical results demonstrate that compared with several baseline algorithms, the proposed algorithm has great advantages in improving the system utility and convergence rate.

---


### 63. [Designing Annotations in Visualization: Considerations from Visualization Practitioners and Educators](https://arxiv.org/abs/2604.07691)

**<font color=#1a73e8>作者：</font>** Md Dilshadur Rahman, Devin Lange, Ghulam Jilani Quadri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Annotation is a central mechanism in visualization design that enables people to communicate key insights. Prior research has provided essential accounts of the visual forms annotations take, but less attention has been paid to the decisions behind them. This paper examines how annotations are designed in practice and how educators reflect on those practices. We conducted a two-phase qualitative study: interviews with ten practitioners from diverse backgrounds revealed the heuristics they draw on when creating annotations, and interviews with seven visualization educators offered complementary perspectives situated within broader concerns of clarity, guidance, and viewer agency. These studies provide a systematic account of annotation design knowledge in professional settings, highlighting the considerations, trade-offs, and contextual judgments that shape the use of annotations. By making this tacit expertise explicit, our work complements prior form-focused studies, strengthens understanding of annotation as a design activity, and points to opportunities for improved tool and guideline support.

---


### 64. [AITH: A Post-Quantum Continuous Delegation Protocol for Human-AI Trust Establishment](https://arxiv.org/abs/2604.07695)

**<font color=#1a73e8>作者：</font>** Zhaoliang Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid deployment of AI agents acting autonomously on behalf of human principals has outpaced the development of cryptographic protocols for establishing, bounding, and revoking human-AI trust relationships. Existing frameworks (TLS, OAuth 2.0, Macaroons) assume deterministic software and cannot address probabilistic AI agents operating continuously within variable trust boundaries.
We present AITH (AI Trust Handshake), a post-quantum continuous delegation protocol. AITH introduces: (1) a Continuous Delegation Certificate signed once with ML-DSA-87 (FIPS 204, NIST Level 5), replacing per-operation signing with sub-microsecond boundary checks at 4.7M ops/sec; (2) a six-check Boundary Engine enforcing hard constraints, rate limits, and escalation triggers with zero cryptographic overhead on the critical path; (3) a push-based Revocation Protocol propagating invalidation within one second. A three-tier SHA-256 Responsibility Chain provides tamper-evident audit logging. All five security theorems are machine-verified via Tamarin Prover under the Dolev-Yao model.
We validate AITH through five rounds of multi-model adversarial auditing, resolving 12 vulnerabilities across four severity layers. Simulation of 100,000 operations shows 79.5% autonomous execution, 6.1% human escalation, and 14.4% blocked.

---


### 65. [Smells Like Fire: Exploring the Impact of Olfactory Cues in VR Wildfire Evacuation Training](https://arxiv.org/abs/2604.07699)

**<font color=#1a73e8>作者：</font>** Alison Crosby, MJ Johns, Eunsol Sol Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents a pilot study exploring the effects of an olfactory stimulus (smoke) for a Virtual Reality game designed to support wildfire evacuation preparedness. Participants (N=18) were split evenly into either a smoke or a control condition, and both completed the same evacuation task. Post-task surveys assessed the participants' perceived preparedness and overall experience. Initial findings suggest participants in the smoke condition reported significantly higher immersion compared to those in the control condition. Across both groups, participants expressed an increased sense of preparedness for real-world wildfire evacuations following the experience.

---


### 66. [Mathematical analysis of one-layer neural network with fixed biases, a new activation function and other observations](https://arxiv.org/abs/2604.07715)

**<font color=#1a73e8>作者：</font>** Fabricio Macià, Shu Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We analyze a simple one-hidden-layer neural network with ReLU activation functions and fixed biases, with one-dimensional input and output. We study both continuous and discrete versions of the model, and we rigorously prove the convergence of the learning process with the $L^2$ squared loss function and the gradient descent procedure. We also prove the spectral bias property for this learning process.
Several conclusions of this analysis are discussed; in particular, regarding the structure and properties that activation functions should possess, as well as the relationships between the spectrum of certain operators and the learning process. Based on this, we also propose an alternative activation function, the full-wave rectified exponential function (FReX), and we discuss the convergence of the gradient descent with this alternative activation function.

---


### 67. [Sima 1.0: A Collaborative Multi-Agent Framework for Documentary Video Production](https://arxiv.org/abs/2604.07721)

**<font color=#1a73e8>作者：</font>** Zhao Song  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Content creation for major video-sharing platforms demands significant manual labor, particularly for long-form documentary videos spanning one to two hours. In this work, we introduce Sima 1.0, a multi-agent system designed to optimize the weekly production pipeline for high-quality video generation. The framework partitions the production process into an 11-step pipeline distributed across a hybrid workforce. While foundational creative tasks and physical recording are executed by a human operator, time-intensive editing, caption refinement, and supplementary asset integration are delegated to specialized junior and senior-level AI agents. By systematizing tasks from script annotation to final asset exportation, Sima 1.0 significantly reduces the production workload, empowering a single creator to efficiently sustain a rigorous weekly publishing schedule.

---


### 68. [Needle in a Haystack -- One-Class Representation Learning for Detecting Rare Malignant Cells in Computational Cytology](https://arxiv.org/abs/2604.07722)

**<font color=#1a73e8>作者：</font>** Swarnadip Chatterjee, Vladimir Basic, Arrigo Capitanio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In computational cytology, detecting malignancy on whole-slide images is difficult because malignant cells are morphologically diverse yet vanishingly rare amid a vast background of normal cells. Accurate detection of these extremely rare malignant cells remains challenging due to large class imbalance and limited annotations. Conventional weakly supervised approaches, such as multiple instance learning (MIL), often fail to generalize at the instance level, especially when the fraction of malignant cells (witness rate) is exceedingly low. In this study, we explore the use of one-class representation learning techniques for detecting malignant cells in low-witness-rate scenarios. These methods are trained exclusively on slide-negative patches, without requiring any instance-level supervision. Specifically, we evaluate two OCC approaches, DSVDD and DROC, and compare them with FS-SIL, WS-SIL, and the recent ItS2CLR method. The one-class methods learn compact representations of normality and detect deviations at test time. Experiments on a publicly available bone marrow cytomorphology dataset (TCIA) and an in-house oral cancer cytology dataset show that DSVDD achieves state-of-the-art performance in instance-level abnormality ranking, particularly in ultra-low witness-rate regimes ($\leq 1\%$) and, in some cases, even outperforming fully supervised learning, which is typically not a practical option in whole-slide cytology due to the infeasibility of exhaustive instance-level annotations. DROC is also competitive under extreme rarity, benefiting from distribution-augmented contrastive learning. These findings highlight one-class representation learning as a robust and interpretable superior choice to MIL for malignant cell detection under extreme rarity.

---


### 69. [Direct Segmentation without Logits Optimization for Training-Free Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2604.07723)

**<font color=#1a73e8>作者：</font>** Jiahao Li, Yang Lu, Yachao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation (OVSS) aims to segment arbitrary category regions in images using open-vocabulary prompts, necessitating that existing methods possess pixel-level vision-language alignment capability. Typically, this capability involves computing the cosine similarity, \ie, logits, between visual and linguistic features, and minimizing the distribution discrepancy between the logits and the ground truth (GT) to generate optimal logits that are subsequently used to construct segmentation maps, yet it depends on time-consuming iterative training or model-specific attention modulation. In this work, we propose a more direct approach that eschews the logits-optimization process by directly deriving an analytic solution for the segmentation map. We posit a key hypothesis: the distribution discrepancy encodes semantic information; specifically, this discrepancy exhibits consistency across patches belonging to the same category but inconsistency across different categories. Based on this hypothesis, we directly utilize the analytic solution of this distribution discrepancy as the semantic maps. In other words, we reformulate the optimization of the distribution discrepancy as deriving its analytic solution, thereby eliminating time-consuming iterative training, freeing us from model-specific attention modulation, and achieving state-of-the-art performance on eight benchmark datasets.

---


### 70. [Squeeze Evolve: Unified Multi-Model Orchestration for Verifier-Free Evolution](https://arxiv.org/abs/2604.07725)

**<font color=#1a73e8>作者：</font>** Monishwaran Maheswaran, Leon Lakhani, Zhongzhu Zhou 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We show that verifier-free evolution is bottlenecked by both diversity and efficiency: without external correction, repeated evolution accelerates collapse toward narrow modes, while the uniform use of a high-cost model wastes compute and quickly becomes economically impractical. We introduce Squeeze Evolve, a unified multi-model orchestration framework for verifier-free evolutionary inference. Our approach is guided by a simple principle: allocate model capability where it has the highest marginal utility. Stronger models are reserved for high-impact stages, while cheaper models handle the other stages at much lower costs. This principle addresses diversity and cost-efficiency jointly while remaining lightweight. Squeeze Evolve naturally supports open-source, closed-source, and mixed-model deployments. Across AIME 2025, HMMT 2025, LiveCodeBench V6, GPQA-Diamond, ARC-AGI-V2, and multimodal vision benchmarks, such as MMMU-Pro and BabyVision, Squeeze Evolve consistently improves the cost-capability frontier over single-model evolution and achieves new state-of-the-art results on several tasks. Empirically, Squeeze Evolve reduces API cost by up to $\sim$3$\times$ and increases fixed-budget serving throughput by up to $\sim$10$\times$. Moreover, on discovery tasks, Squeeze Evolve is the first verifier-free evolutionary method to match, and in some cases exceed, the performance of verifier-based evolutionary methods.

---


### 71. [TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense](https://arxiv.org/abs/2604.07727)

**<font color=#1a73e8>作者：</font>** Cheng Liu, Xiaolei Liu, Xingyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing jailbreak defense paradigms primarily rely on static detection of prompts, outputs, or internal states, often neglecting the dynamic evolution of risk during decoding. This oversight leaves risk signals embedded in decoding trajectories underutilized, constituting a critical blind spot in current defense systems. In this work, we empirically demonstrate that hidden states in critical layers during the decoding phase carry stronger and more stable risk signals than input jailbreak prompts. Specifically, the hidden representations of tokens generated during jailbreak attempts progressively approach high-risk regions in the latent space. Based on this observation, we propose TrajGuard, a training-free, decoding-time defense framework. TrajGuard aggregates hidden-state trajectories via a sliding window to quantify risk in real time, triggering a lightweight semantic adjudication only when risk within a local window persistently exceeds a threshold. This mechanism enables the immediate interruption or constraint of subsequent decoding. Extensive experiments across 12 jailbreak attacks and various open-source LLMs show that TrajGuard achieves an average defense rate of 95%. Furthermore, it reduces detection latency to 5.2 ms/token while maintaining a false positive rate below 1.5%. These results confirm that hidden-state trajectories during decoding can effectively support real-time jailbreak detection, highlighting a promising direction for defenses without model modification.

---


### 72. [GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting](https://arxiv.org/abs/2604.07728)

**<font color=#1a73e8>作者：</font>** Jialin Li, Bin Fu, Ruiping Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity interactive digital assets are essential for embodied intelligence and robotic interaction, yet articulated objects remain challenging to reconstruct due to their complex structures and coupled geometry-motion relationships. Existing methods suffer from instability in geometry-motion joint optimization, while their generalization remains limited on complex multi-joint or out-of-distribution objects. To address these challenges, we propose GEAR, an EM-style alternating optimization framework that jointly models geometry and motion as interdependent components within a Gaussian Splatting representation. GEAR treats part segmentation as a latent variable and joint motion parameters as explicit variables, alternately refining them for improved convergence and geometric-motion consistency. To enhance part segmentation quality without sacrificing generalization, we leverage a vanilla 2D segmentation model to provide multi-view part priors, and employ a weakly supervised constraint to regularize the latent variable. Experiments on multiple benchmarks and our newly constructed dataset GEAR-Multi demonstrate that GEAR achieves state-of-the-art results in geometric reconstruction and motion parameters estimation, particularly on complex articulated objects with multiple movable parts.

---


### 73. [Twitch Third-Party Developers' Support Seeking and Provision Practices on Discord](https://arxiv.org/abs/2604.07732)

**<font color=#1a73e8>作者：</font>** Jie Cai, He Zhang, Yueyan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Third-party developers (TPDs) often turn to online communities for support when they can't get immediate responses from the platform. Twitch, as a leading live streaming platform, attracted many TPDs and formed an online support community on Discord. This study explores TPDs' support practices via mixed method (a topic modeling to identify topics related to support seeking and provision first and a follow-up in-depth qualitative analysis with these topics) and found that: (1) TPDs' support-seeking practices around social, technical, and policy matters are highly dependent on Twitch, and this dependence acts as a form of platform labor; (2) TPDs need to switch between Discord and Twitch regarding seeking and provision, exacerbating TPDs' platform labor; (3) TPDs' flexible role practices reflect the community's flourishing on Discord but require roles to bridge the two platforms and transfer informal support seeking to possible formal support from Twitch. We propose implications for effectively managing support seeking and provision between formal and informal spaces to improve the development of TPDs. We also contribute to community support practice and to platform ecology work in CSCW.

---


### 74. [MSCT: Differential Cross-Modal Attention for Deepfake Detection](https://arxiv.org/abs/2604.07741)

**<font color=#1a73e8>作者：</font>** Fangda Wei, Miao Liu, Yingxue Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual deepfake detection typically employs a complementary multi-modal model to check the forgery traces in the video. These methods primarily extract forgery traces through audio-visual alignment, which results from the inconsistency between audio and video modalities. However, the traditional multi-modal forgery detection method has the problem of insufficient feature extraction and modal alignment deviation. To address this, we propose a multi-scale cross-modal transformer encoder (MSCT) for deepfake detection. Our approach includes a multi-scale self-attention to integrate the features of adjacent embeddings and a differential cross-modal attention to fuse multi-modal features. Our experiments demonstrate competitive performance on the FakeAVCeleb dataset, validating the effectiveness of the proposed structure.

---


### 75. [Towards Rapid Constitutive Model Discovery from Multi-Modal Data: Physics Augmented Finite Element Model Updating (paFEMU)](https://arxiv.org/abs/2604.07746)

**<font color=#1a73e8>作者：</font>** Jingye Tan, Govinda Anantha Padmanabha, Steven J. Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in AI-enabled constitutive modeling has concentrated on moving from a purely data-driven paradigm to the enforcement of physical constraints and mechanistic principles, a concept referred to as physics augmentation. Classical phenomenological approaches rely on selecting a pre-defined model and calibrating its parameters, while machine learning methods often focus on discovery of the model itself. Sparse regression approaches lie in between, where large libraries of pre-defined models are probed during calibration. Sparsification in the aforementioned paradigm, but also in the context of neural network architecture, has been shown to enable interpretability, uncertainty quantification, but also heterogeneous software integration due to the low-dimensional nature of the resulting models. Most works in AI-enabled constitutive modeling have also focused on data from a single source, but in reality, materials modeling workflows can contain data from many different sources (multi-modal data), and also from testing other materials within the same materials class (multi-fidelity data). In this work, we introduce physics augmented finite element model updating (paFEMU), as a transfer learning approach that combines AI-enabled constitutive modeling, sparsification for interpretable model discovery, and finite element-based adjoint optimization utilizing multi-modal data. This is achieved by combining simple mechanical testing data, potentially from a distinct material, with digital image correlation-type full-field data acquisition to ultimately enable rapid constitutive modeling discovery. The simplicity of the sparse representation enables easy integration of neural constitutive models in existing finite element workflows, and also enables low-dimensional updating during transfer learning.

---


### 76. [Mitigating Distribution Sharpening in Math RLVR via Distribution-Aligned Hint Synthesis and Backward Hint Annealing](https://arxiv.org/abs/2604.07747)

**<font color=#1a73e8>作者：</font>** Pei-Xi Xie, Che-Yu Lin, Cheng-Lin Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) can improve low-$k$ reasoning accuracy while narrowing solution coverage on challenging math questions, and pass@1 gains do not necessarily translate into better large-$k$ performance. Existing hint-based approaches can make challenging questions trainable, but they leave two issues underexplored: teacher-student distribution mismatch and the need to reduce hint exposure to match no-hint evaluation. We address these issues through two components. Distribution-Aligned Hint Synthesis (DAHS) constructs verified teacher hints conditioned on student-style responses. Backward Hint Annealing (BHA) anneals hint exposure across difficulty buckets and uses per-question hint dropout to preserve no-hint updates throughout RL training. We evaluate the method in math RLVR under the DAPO training framework across AIME24, AIME25, and AIME26 using $\texttt{Qwen3-1.7B-Base}$ and $\texttt{Llama-3.2-1B-Instruct}$. On $\texttt{Qwen3-1.7B-Base}$, our method improves both pass@1 and pass@2048 relative to DAPO across the three AIME benchmarks. On $\texttt{Llama-3.2-1B-Instruct}$, the gains are concentrated in the large-$k$ regime. These results suggest that, in math RLVR, hint scaffolding is effective when it restores learnable updates on challenging questions early in training and is then gradually removed before no-hint evaluation.

---


### 77. [An Empirical Analysis of Static Analysis Methods for Detection and Mitigation of Code Library Hallucinations](https://arxiv.org/abs/2604.07755)

**<font color=#1a73e8>作者：</font>** Clarissa Miranda-Pena, Andrew Reeson, Cécile Paris 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite extensive research, Large Language Models continue to hallucinate when generating code, particularly when using libraries. On NL-to-code benchmarks that require library use, we find that LLMs generate code that uses non-existent library features in 8.1-40% of this http URL intuitive approach for detection and mitigation of hallucinations is static analysis. In this paper, we analyse the potential of static analysis tools, both in terms of what they can solve and what they cannot. We find that static analysis tools can detect 16-70% of all errors, and 14-85% of library hallucinations, with performance varying by LLM and dataset. Through manual analysis, we identify cases a static method could not plausibly catch, which gives an upper bound on their potential from 48.5% to 77%. Overall, we show that static analysis methods are cheap method for addressing some forms of hallucination, and we quantify how far short of solving the problem they will always be.

---


### 78. [DailyArt: Discovering Articulation from Single Static Images via Latent Dynamics](https://arxiv.org/abs/2604.07758)

**<font color=#1a73e8>作者：</font>** Hang Zhang, Qijian Tian, Jingyu Gong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Articulated objects are essential for embodied AI and world models, yet inferring their kinematics from a single closed-state image remains challenging because crucial motion cues are often occluded. Existing methods either require multi-state observations or rely on explicit part priors, retrieval, or other auxiliary inputs that partially expose the structure to be inferred. In this work, we present DailyArt, which formulates articulated joint estimation from a single static image as a synthesis-mediated reasoning problem. Instead of directly regressing joints from a heavily occluded observation, DailyArt first synthesizes a maximally articulated opened state under the same camera view to expose articulation cues, and then estimates the full set of joint parameters from the discrepancy between the observed and synthesized states. Using a set-prediction formulation, DailyArt recovers all joints simultaneously without requiring object-specific templates, multi-view inputs, or explicit part annotations at test time. Taking estimated joints as conditions, the framework further supports part-level novel state synthesis as a downstream capability. Extensive experiments show that DailyArt achieves strong performance in articulated joint estimation and supports part-level novel state synthesis conditioned on joints. Project page is available at this https URL.

---


### 79. [WUTDet: A 100K-Scale Ship Detection Dataset and Benchmarks with Dense Small Objects](https://arxiv.org/abs/2604.07759)

**<font color=#1a73e8>作者：</font>** Junxiong Liang, Mengwei Bao, Tianxiang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ship detection for navigation is a fundamental perception task in intelligent waterway transportation systems. However, existing public ship detection datasets remain limited in terms of scale, the proportion of small-object instances, and scene diversity, which hinders the systematic evaluation and generalization study of detection algorithms in complex maritime environments. To this end, we construct WUTDet, a large-scale ship detection dataset. WUTDet contains 100,576 images and 381,378 annotated ship instances, covering diverse operational scenarios such as ports, anchorages, navigation, and berthing, as well as various imaging conditions including fog, glare, low-lightness, and rain, thereby exhibiting substantial diversity and challenge. Based on WUTDet, we systematically evaluate 20 baseline models from three mainstream detection architectures, namely CNN, Transformer, and Mamba. Experimental results show that the Transformer architecture achieves superior overall detection accuracy (AP) and small-object detection performance (APs), demonstrating stronger adaptability to complex maritime scenes; the CNN architecture maintains an advantage in inference efficiency, making it more suitable for real-time applications; and the Mamba architecture achieves a favorable balance between detection accuracy and computational efficiency. Furthermore, we construct a unified cross-dataset test set, Ship-GEN, to evaluate model generalization. Results on Ship-GEN show that models trained on WUTDet exhibit stronger generalization under different data distributions. These findings demonstrate that WUTDet provides effective data support for the research, evaluation, and generalization analysis of ship detection algorithms in complex maritime scenarios. The dataset is publicly available at: this https URL.

---


### 80. [Beyond Surface Artifacts: Capturing Shared Latent Forgery Knowledge Across Modalities](https://arxiv.org/abs/2604.07763)

**<font color=#1a73e8>作者：</font>** Jingtong Dou, Chuancheng Shi, Jian Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As generative artificial intelligence evolves, deepfake attacks have escalated from single-modality manipulations to complex, multimodal threats. Existing forensic techniques face a severe generalization bottleneck: by relying excessively on superficial, modality-specific artifacts, they neglect the shared latent forgery knowledge hidden beneath variable physical appearances. Consequently, these models suffer catastrophic performance degradation when confronted with unseen "dark modalities." To break this limitation, this paper introduces a paradigm shift that redefines multimodal forensics from conventional "feature fusion" to "modality generalization." We propose the first modality-agnostic forgery (MAF) detection framework. By explicitly decoupling modality-specific styles, MAF precisely extracts the essential, cross-modal latent forgery knowledge. Furthermore, we define two progressive dimensions to quantify model generalization: transferability toward semantically correlated modalities (Weak MAF), and robustness against completely isolated signals of "dark modality" (Strong MAF). To rigorously assess these generalization limits, we introduce the DeepModal-Bench benchmark, which integrates diverse multimodal forgery detection algorithms and adapts state-of-the-art generalized learning methods. This study not only empirically proves the existence of universal forgery traces but also achieves significant performance breakthroughs on unknown modalities via the MAF framework, offering a pioneering technical pathway for universal multimodal defense.

---


### 81. [Sensitivity-Positional Co-Localization in GQA Transformers](https://arxiv.org/abs/2604.07766)

**<font color=#1a73e8>作者：</font>** Manoj Chandrashekar Rao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate a fundamental structural question in Grouped Query Attention (GQA) transformers: do the layers most sensitive to task correctness coincide with the layers where positional encoding adaptation has the greatest leverage? We term this the co-localization hypothesis and test it on Llama 3.1 8B, a 32-layer GQA model with a 4:1 query-to-key-value head ratio. We introduce \LSLORA, which restricts LoRA adaptation to layers identified via a novel correctness-differential hidden-state metric, and GARFA (GQA-Aware RoPE Frequency Adaptation), which attaches 8 learnable per-KV-head scalar multipliers to each targeted layer. Contrary to the co-localization hypothesis, we discover strong anti-localization: task-sensitive layers concentrate in the late network ($\ell\in\{23\text{-}31\}$) while RoPE-influential layers dominate the early network ($\ell\in\{0\text{-}9\}$), yielding Spearman $r_s = -0.735$ ($p = 1.66\times10^{-6}$). Despite this anti-localization, a 4-way cross-layer ablation shows that applying both interventions to the sensitivity-identified layers outperforms all alternative configurations by 4-16 percentage points across six diverse benchmarks (MMLU, GPQA, HumanEval+, MATH, MGSM, ARC), approaching Claude 3.5 Haiku on HumanEval+ (67.1% vs. 68.3%) at \$100 total compute cost.

---


### 82. [Anamorphic Encryption with CCA Security: A Standard Model Construction](https://arxiv.org/abs/2604.07771)

**<font color=#1a73e8>作者：</font>** Shujun Wang, Jianting Ning, Qinyi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anamorphic encryption serves as a vital tool for covert communication, maintaining secrecy even during post-compromise scenarios. Particularly in the receiver-anamorphic setting, a user can shield hidden messages even when coerced into surrendering their secret keys. However, a major bottleneck in existing research is the reliance on CPA-security, leaving the construction of a generic, CCA-secure anamorphic scheme in the standard model as a persistent open challenge. To bridge this gap, we formalize the Anamorphic Key Encapsulation Mechanism (AKEM), encompassing both Public-Key (PKAKEM) and Symmetric-Key (SKAKEM) variants. We propose generic constructions for these primitives, which can be instantiated using any KEM that facilitates randomness recovery. Notably, our framework achieves strong IND-CCA (sIND-CCA) security for the covert channel. We provide a rigorous formal proof in the standard model, demonstrating resilience against a "dictator" who controls the decapsulation key. The security of our approach is anchored in the injective property of the base KEM, which ensures a unique mapping between ciphertexts and randomness. By integrating anamorphism into the KEM-DEM paradigm, our work significantly enhances the practical utility of covert channels within modern cryptographic infrastructures.

---


### 83. [ESOM: Efficiently Understanding Streaming Video Anomalies with Open-world Dynamic Definitions](https://arxiv.org/abs/2604.07772)

**<font color=#1a73e8>作者：</font>** Zihao Liu, Xiaoyu Wu, Wenna Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world video anomaly detection (OWVAD) aims to detect and explain abnormal events under different anomaly definitions, which is important for applications such as intelligent surveillance and live-streaming content moderation. Recent MLLM-based methods have shown promising open-world generalization, but still suffer from three major limitations: inefficiency for practical deployment, lack of streaming processing adaptation, and limited support for dynamic anomaly definitions in both modeling and evaluation. To address these issues, this paper proposes ESOM, an efficient streaming OWVAD model that operates in a training-free manner. ESOM includes a Definition Normalization module to structure user prompts for reducing hallucination, an Inter-frame-matched Intra-frame Token Merging module to compress redundant visual tokens, a Hybrid Streaming Memory module for efficient causal inference, and a Probabilistic Scoring module that converts interval-level textual outputs into frame-level anomaly scores. In addition, this paper introduces OpenDef-Bench, a new benchmark with clean surveillance videos and diverse natural anomaly definitions for evaluating performance under varying conditions. Extensive experiments show that ESOM achieves real-time efficiency on a single GPU and state-of-the-art performance in anomaly temporal localization, classification, and description generation. The code and benchmark will be released at this https URL.

---


### 84. [ACIArena: Toward Unified Evaluation for Agent Cascading Injection](https://arxiv.org/abs/2604.07775)

**<font color=#1a73e8>作者：</font>** Hengyu An, Minxi Li, Jinghuai Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collaboration and information sharing empower Multi-Agent Systems (MAS) but also introduce a critical security risk known as Agent Cascading Injection (ACI). In such attacks, a compromised agent exploits inter-agent trust to propagate malicious instructions, causing cascading failures across the system. However, existing studies consider only limited attack strategies and simplified MAS settings, limiting their generalizability and comprehensive evaluation. To bridge this gap, we introduce ACIArena, a unified framework for evaluating the robustness of MAS. ACIArena offers systematic evaluation suites spanning multiple attack surfaces (i.e., external inputs, agent profiles, inter-agent messages) and attack objectives (i.e., instruction hijacking, task disruption, information exfiltration). Specifically, ACIArena establishes a unified specification that jointly supports MAS construction and attack-defense modules. It covers six widely used MAS implementations and provides a benchmark of 1,356 test cases for systematically evaluating MAS robustness. Our benchmarking results show that evaluating MAS robustness solely through topology is insufficient; robust MAS require deliberate role design and controlled interaction patterns. Moreover, defenses developed in simplified environments often fail to transfer to real-world settings; narrowly scoped defenses may even introduce new vulnerabilities. ACIArena aims to provide a solid foundation for advancing deeper exploration of MAS design principles.

---


### 85. [The Accountability Horizon: An Impossibility Theorem for Governing Human-Agent Collectives](https://arxiv.org/abs/2604.07778)

**<font color=#1a73e8>作者：</font>** Haileleol Tibebu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing accountability frameworks for AI systems, legal, ethical, and regulatory, rest on a shared assumption: for any consequential outcome, at least one identifiable person had enough involvement and foresight to bear meaningful responsibility. This paper proves that agentic AI systems violate this assumption not as an engineering limitation but as a mathematical necessity once autonomy exceeds a computable threshold. We introduce Human-Agent Collectives, a formalisation of joint human-AI systems where agents are modelled as state-policy tuples within a shared structural causal model. Autonomy is characterised through a four-dimensional information-theoretic profile (epistemic, executive, evaluative, social); collective behaviour through interaction graphs and joint action spaces. We axiomatise legitimate accountability through four minimal properties: Attributability (responsibility requires causal contribution), Foreseeability Bound (responsibility cannot exceed predictive capacity), Non-Vacuity (at least one agent bears non-trivial responsibility), and Completeness (all responsibility must be fully allocated). Our central result, the Accountability Incompleteness Theorem, proves that for any collective whose compound autonomy exceeds the Accountability Horizon and whose interaction graph contains a human-AI feedback cycle, no framework can satisfy all four properties simultaneously. The impossibility is structural: transparency, audits, and oversight cannot resolve it without reducing autonomy. Below the threshold, legitimate frameworks exist, establishing a sharp phase transition. Experiments on 3,000 synthetic collectives confirm all predictions with zero violations. This is the first impossibility result in AI governance, establishing a formal boundary below which current paradigms remain valid and above which distributed accountability mechanisms become necessary.

---


### 86. [Cross-Modal Emotion Transfer for Emotion Editing in Talking Face Video](https://arxiv.org/abs/2604.07786)

**<font color=#1a73e8>作者：</font>** Chanhyuk Choi, Taesoo Kim, Donggyu Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Talking face generation has gained significant attention as a core application of generative models. To enhance the expressiveness and realism of synthesized videos, emotion editing in talking face video plays a crucial role. However, existing approaches often limit expressive flexibility and struggle to generate extended emotions. Label-based methods represent emotions with discrete categories, which fail to capture a wide range of emotions. Audio-based methods can leverage emotionally rich speech signals - and even benefit from expressive text-to-speech (TTS) synthesis - but they fail to express the target emotions because emotions and linguistic contents are entangled in emotional speeches. Images-based methods, on the other hand, rely on target reference images to guide emotion transfer, yet they require high-quality frontal views and face challenges in acquiring reference data for extended emotions (e.g., sarcasm). To address these limitations, we propose Cross-Modal Emotion Transfer (C-MET), a novel approach that generates facial expressions based on speeches by modeling emotion semantic vectors between speech and visual feature spaces. C-MET leverages a large-scale pretrained audio encoder and a disentangled facial expression encoder to learn emotion semantic vectors that represent the difference between two different emotional embeddings across modalities. Extensive experiments on the MEAD and CREMA-D datasets demonstrate that our method improves emotion accuracy by 14% over state-of-the-art methods, while generating expressive talking face videos - even for unseen extended emotions. Code, checkpoint, and demo are available at this https URL

---


### 87. [ORACLE-SWE: Quantifying the Contribution of Oracle Information Signals on SWE Agents](https://arxiv.org/abs/2604.07789)

**<font color=#1a73e8>作者：</font>** Kenan Li, Qirui Jin, Liao Zhu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recent advances in language model (LM) agents have significantly improved automated software engineering (SWE). Prior work has proposed various agentic workflows and training strategies as well as analyzed failure modes of agentic systems on SWE tasks, focusing on several contextual information signals: Reproduction Test, Regression Test, Edit Location, Execution Context, and API Usage. However, the individual contribution of each signal to overall success remains underexplored, particularly their ideal contribution when intermediate information is perfectly obtained. To address this gap, we introduce Oracle-SWE, a unified method to isolate and extract oracle information signals from SWE benchmarks and quantify the impact of each signal on agent performance. To further validate the pattern, we evaluate the performance gain of signals extracted by strong LMs when provided to a base agent, approximating real-world task-resolution settings. These evaluations aim to guide research prioritization for autonomous coding systems.

---


### 88. [SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents](https://arxiv.org/abs/2604.07791)

**<font color=#1a73e8>作者：</font>** Xinshun Feng, Xinhao Song, Lijun Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Reinforcement Learning with Verifiable Rewards (RLVR) have demonstrated significant potential in single-turn reasoning tasks. With the paradigm shift toward self-evolving agentic learning, models are increasingly expected to learn from trajectories by synthesizing tools or accumulating explicit experiences. However, prevailing methods typically rely on large-scale LLMs or multi-agent frameworks, which hinder their deployment in resource-constrained environments. The inherent sparsity of outcome-based rewards also poses a substantial challenge, as agents typically receive feedback only upon completion of tasks. To address these limitations, we introduce a Tool-Memory based self-evolving agentic framework SEARL. Unlike approaches that directly utilize interaction experiences, our method constructs a structured experience memory that integrates planning with execution. This provides a novel state abstraction that facilitates generalization across analogous contexts, such as tool reuse. Consequently, agents extract explicit knowledge from historical data while leveraging inter-trajectory correlations to densify reward signals. We evaluate our framework on knowledge reasoning and mathematics tasks, demonstrating its effectiveness in achieving more practical and efficient learning.

---


### 89. [Image-Guided Geometric Stylization of 3D Meshes](https://arxiv.org/abs/2604.07795)

**<font color=#1a73e8>作者：</font>** Changwoon Choi, Hyunsoo Lee, Clément Jambon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent generative models can create visually plausible 3D representations of objects. However, the generation process often allows for implicit control signals, such as contextual descriptions, and rarely supports bold geometric distortions beyond existing data distributions. We propose a geometric stylization framework that deforms a 3D mesh, allowing it to express the style of an image. While style is inherently ambiguous, we utilize pre-trained diffusion models to extract an abstract representation of the provided image. Our coarse-to-fine stylization pipeline can drastically deform the input 3D model to express a diverse range of geometric variations while retaining the valid topology of the original mesh and part-level semantics. We also propose an approximate VAE encoder that provides efficient and reliable gradients from mesh renderings. Extensive experiments demonstrate that our method can create stylized 3D meshes that reflect unique geometric features of the pictured assets, such as expressive poses and silhouettes, thereby supporting the creation of distinctive artistic 3D creations. Project page: this https URL

---


### 90. [BRASP: Boolean Range Queries over Encrypted Spatial Data with Access and Search Pattern Privacy](https://arxiv.org/abs/2604.07797)

**<font color=#1a73e8>作者：</font>** Jing Zhang, Ganxuan Yang, Yifei Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Searchable Encryption (SE) enables users to query outsourced encrypted data while preserving data confidentiality. However, most efficient schemes still leak the search pattern and access pattern, which may allow an honest-but-curious cloud server to infer query contents, user interests, or returned records from repeated searches and observed results. Existing pattern-hiding solutions mainly target keyword queries and do not naturally support Boolean range queries over encrypted spatial data. This paper presents BRASP, a searchable encryption scheme for Boolean range queries over encrypted spatial data. BRASP combines Hilbert-curve-based prefix encoding with encrypted prefix--ID and keyword--ID inverted indexes to support efficient spatial range filtering and conjunctive keyword matching. To hide the search pattern and access pattern under a dual-server setting, BRASP integrates index shuffling for encrypted keyword and prefix entries with ID-field redistribution across two non-colluding cloud servers. BRASP also supports dynamic updates and achieves forward security. We formalize the security of BRASP through confidentiality, shuffle indistinguishability, query unforgeability, and forward-security analyses, and we evaluate its performance experimentally on a real-world dataset. The results show that BRASP effectively protects query privacy while incurring relatively low computation and communication overhead. To facilitate reproducibility and further research, the source code of BRASP is publicly available at this https URL

---


### 91. [TEMPER: Testing Emotional Perturbation in Quantitative Reasoning](https://arxiv.org/abs/2604.07801)

**<font color=#1a73e8>作者：</font>** Atahan Dokme, Benjamin Reichman, Larry Heck  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are trained and evaluated on quantitative reasoning tasks written in clean, emotionally neutral language. However, real-world queries are often wrapped in frustration, urgency or enthusiasm. Does emotional framing alone degrade reasoning when all numerical content is preserved? To investigate this, a controlled emotion translation framework is developed that rewrites problems into emotional variants while preserving all quantities and relationships. Using this framework, Temper-5400 (5,400 semantically verified emotion--neutral pairs) is constructed across GSM8K, MultiArith, and ARC-Challenge, and evaluated on eighteen models (1B to frontier scale). Two core results emerge: First, emotional framing reduces accuracy by 2-10 percentage points even though all numerical content is preserved. Second, neutralizing emotional variants recovers most of the lost performance, showing both that the degradation is tied to emotional style rather than content corruption and that neutralization can serve as a lightweight inference-time mitigation. Non-emotional paraphrases cause no such degradation, implicating emotional content rather than surface-level changes. Beyond emotion specifically, the benchmark construction procedure provides a general framework for controlled stylistic translation and robustness evaluation.

---


### 92. [PolicyLong: Towards On-Policy Context Extension](https://arxiv.org/abs/2604.07809)

**<font color=#1a73e8>作者：</font>** Junlong Jia, Ziyang Chen, Xing Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extending LLM context windows is hindered by scarce high-quality long-context data. Recent methods synthesize data with genuine long-range dependencies via information-theoretic verification, selecting contexts that reduce a base model's predictive entropy. However, their single-pass offline construction with a fixed model creates a fundamental off-policy gap: the static screening landscape misaligns with the model's evolving capabilities, causing the training distribution to drift. We propose PolicyLong, shifting data construction towards a dynamic on-policy paradigm. By iteratively re-executing data screening (entropy computation, retrieval, and verification) using the current model, PolicyLong ensures the training distribution tracks evolving capabilities, yielding an emergent self-curriculum. Crucially, both positive and hard negative contexts derive from the current model's entropy landscape, co-evolving what the model learns to exploit and resist. Experiments on RULER, HELMET, and LongBench-v2 (Qwen2.5-3B) show PolicyLong consistently outperforms EntropyLong and NExtLong, with gains growing at longer contexts (e.g., +2.54 at 128K on RULER), confirming the value of on-policy data evolution.

---


### 93. [Agentivism: a learning theory for the age of artificial intelligence](https://arxiv.org/abs/2604.07813)

**<font color=#1a73e8>作者：</font>** Lixiang Yan, Dragan Gašević  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning theories have historically changed when the conditions of learning evolved. Generative and agentic AI create a new condition by allowing learners to delegate explanation, writing, problem solving, and other cognitive work to systems that can generate, recommend, and sometimes act on the learner's behalf. This creates a fundamental challenge for learning theory: successful performance can no longer be assumed to indicate learning. Learners may complete tasks effectively with AI support while developing less understanding, weaker judgment, and limited transferable capability. We argue that this problem is not fully captured by existing learning theories. Behaviourism, cognitivism, constructivism, and connectivism remain important, but they do not directly explain when AI-assisted performance becomes durable human capability. We propose Agentivism, a learning theory for human-AI interaction. Agentivism defines learning as durable growth in human capability through selective delegation to AI, epistemic monitoring and verification of AI contributions, reconstructive internalization of AI-assisted outputs, and transfer under reduced support. The importance of Agentivism lies in explaining how learning remains possible when intelligent delegation is easy and human-AI interaction is becoming a persistent and expanding part of human learning.

---


### 94. [Automatic Generation of Executable BPMN Models from Medical Guidelines](https://arxiv.org/abs/2604.07817)

**<font color=#1a73e8>作者：</font>** Praveen Kumar Menaka Sekar, Ion Matei, Maksym Zhenirovskyy 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an end-to-end pipeline that converts healthcare policy documents into executable, data-aware Business Process Model and Notation (BPMN) models using large language models (LLMs) for simulation-based policy evaluation. We address the main challenges of automated policy digitization with four contributions: data-grounded BPMN generation with syntax auto-correction, executable augmentation, KPI instrumentation, and entropy-based uncertainty detection. We evaluate the pipeline on diabetic nephropathy prevention guidelines from three Japanese municipalities, generating 100 models per backend across three LLMs and executing each against 1,000 synthetic patients. On well-structured policies, the pipeline achieves a 100% ground-truth match with perfect per-patient decision agreement. Across all conditions, raw per-patient decision agreement exceeds 92%, and entropy scores increase monotonically with document complexity, confirming that the detector reliably separates unambiguous policies from those requiring targeted human clarification.

---


### 95. [Loop, Think, & Generalize: Implicit Reasoning in Recurrent-Depth Transformers](https://arxiv.org/abs/2604.07822)

**<font color=#1a73e8>作者：</font>** Harsh Kohli, Srinivasan Parthasarathy, Huan Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study implicit reasoning, i.e. the ability to combine knowledge or rules within a single forward pass. While transformer-based large language models store substantial factual knowledge and rules, they often fail to compose this knowledge for implicit multi-hop reasoning, suggesting a lack of compositional generalization over their parametric knowledge. To address this limitation, we study recurrent-depth transformers, which enables iterative computation over the same transformer layers. We investigate two compositional generalization challenges under the implicit reasoning scenario: systematic generalization, i.e. combining knowledge that is never used for compositions during training, and depth extrapolation, i.e. generalizing from limited reasoning depth (e.g. training on up to 5-hop) to deeper compositions (e.g. 10-hop). Through controlled studies with models trained from scratch, we show that while vanilla transformers struggle with both generalization challenges, recurrent-depth transformers can effectively make such generalization. For systematic generalization, we find that this ability emerges through a three-stage grokking process, transitioning from memorization to in-distribution generalization and finally to systematic generalization, supported by mechanistic analysis. For depth extrapolation, we show that generalization beyond training depth can be unlocked by scaling inference-time recurrence, with more iterations enabling deeper reasoning. We further study how training strategies affect extrapolation, providing guidance on training recurrent-depth transformers, and identify a key limitation, overthinking, where excessive recurrence degrades predictions and limits generalization to very deep compositions.

---


### 96. [LPM 1.0: Video-based Character Performance Model](https://arxiv.org/abs/2604.07823)

**<font color=#1a73e8>作者：</font>** Ailing Zeng, Casper Yang, Chauncey Ge 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Performance, the externalization of intent, emotion, and personality through visual, vocal, and temporal behavior, is what makes a character alive. Learning such performance from video is a promising alternative to traditional 3D pipelines. However, existing video models struggle to jointly achieve high expressiveness, real-time inference, and long-horizon identity stability, a tension we call the performance trilemma. Conversation is the most comprehensive performance scenario, as characters simultaneously speak, listen, react, and emote while maintaining identity over time. To address this, we present LPM 1.0 (Large Performance Model), focusing on single-person full-duplex audio-visual conversational performance. Concretely, we build a multimodal human-centric dataset through strict filtering, speaking-listening audio-video pairing, performance understanding, and identity-aware multi-reference extraction; train a 17B-parameter Diffusion Transformer (Base LPM) for highly controllable, identity-consistent performance through multimodal conditioning; and distill it into a causal streaming generator (Online LPM) for low-latency, infinite-length interaction. At inference, given a character image with identity-aware references, LPM 1.0 generates listening videos from user audio and speaking videos from synthesized audio, with text prompts for motion control, all at real-time speed with identity-stable, infinite-length generation. LPM 1.0 thus serves as a visual engine for conversational agents, live streaming characters, and game NPCs. To systematically evaluate this setting, we propose LPM-Bench, the first benchmark for interactive character performance. LPM 1.0 achieves state-of-the-art results across all evaluated dimensions while maintaining real-time inference.

---


### 97. [Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection](https://arxiv.org/abs/2604.07831)

**<font color=#1a73e8>作者：</font>** Wenkui Yang, Chao Jin, Haisu Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing red-teaming studies on GUI agents have important limitations. Adversarial perturbations typically require white-box access, which is unavailable for commercial systems, while prompt injection is increasingly mitigated by stronger safety alignment. To study robustness under a more practical threat model, we propose Semantic-level UI Element Injection, a red-teaming setting that overlays safety-aligned and harmless UI elements onto screenshots to misdirect the agent's visual grounding. Our method uses a modular Editor-Overlapper-Victim pipeline and an iterative search procedure that samples multiple candidate edits, keeps the best cumulative overlay, and adapts future prompt strategies based on previous failures. Across five victim models, our optimized attacks improve attack success rate by up to 4.4x over random injection on the strongest victims. Moreover, elements optimized on one source model transfer effectively to other target models, indicating model-agnostic vulnerabilities. After the first successful attack, the victim still clicks the attacker-controlled element in more than 15% of later independent trials, versus below 1% for random injection, showing that the injected element acts as a persistent attractor rather than simple visual clutter.

---


### 98. [A Hardware-Anchored Privacy Middleware for PII Sharing Across Heterogeneous Embedded Consumer Devices](https://arxiv.org/abs/2604.07839)

**<font color=#1a73e8>作者：</font>** Aditya Sabbineni, Pravin Nagare, Devendra Dahiphale 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of the Internet of Things (IoT) and smart home ecosystems has led to a fragmented landscape of user data management across consumer electronics (CE) such as Smart TVs, gaming consoles, and set-top boxes. Current onboarding processes on these devices are characterized by high friction due to manual data entry and opaque data-sharing practices. This paper introduces the User Data Sharing System (UDSS), a platform-agnostic framework designed to facilitate secure, privacy-first PII (Personally Identifiable Information) exchange between device platforms and third-party applications. Our system implements a Contextual Scope Enforcement (CSE) mechanism that programmatically restricts data exposure based on user intent - specifically distinguishing between Sign-In and Sign-Up workflows. Unlike cloud-anchored identity standards such as FIDO2/WebAuthn, UDSS is designed for shared, device-centric CE environments where persistent user-to-device binding cannot be assumed. We further propose a tiered access model that balances developer needs with regulatory compliance (GDPR/CCPA). A proof-of-concept implementation on a reference ARMv8 Linux-based middleware demonstrates that UDSS reduces user onboarding latency by 65% and measurably reduces PII over-exposure risk through protocol-enforced data minimization. This framework provides a standardized approach to identity management in the heterogeneous CE market.

---


### 99. [Language Preferences and Practices in Multilingual EdTech: Flexible Primary Language Use with Secondary Language Support](https://arxiv.org/abs/2604.07843)

**<font color=#1a73e8>作者：</font>** Christine Kwon, Phenyo Phemelo Moletsane, Michael W. Asher 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The benefits of learning in one's mother tongue are well documented, yet colonial languages dominate education, marginalizing local languages and limiting access for learners who rely on their mother tongue for understanding. With the rapid growth of educational technology, there is potential to integrate multilingual instruction supporting both colonial and local languages. This study is part of a larger quasi-experiment conducted in Uganda, where learners could choose to learn in English, Leb-Lango (a local language), or in Hybrid mode (a combination of both) in a remote EdTech course. We examined how learners who chose the Hybrid option navigated English and Leb-Lango. While many Hybrid learners did not consistently use both languages, those who did persisted longer in the course. Learners also shared how they managed language complexities. We provide the first empirical evidence of learner agency in bilingual remote EdTech instruction and offer insights for designing inclusive multilingual learning solutions.

---


### 100. [Information-Theoretic Requirements for Gradient-Based Task Affinity Estimation in Multi-Task Learning](https://arxiv.org/abs/2604.07848)

**<font color=#1a73e8>作者：</font>** Jasper Zhang, Bryan Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task learning shows strikingly inconsistent results -- sometimes joint training helps substantially, sometimes it actively harms performance -- yet the field lacks a principled framework for predicting these outcomes. We identify a fundamental but unstated assumption underlying gradient-based task analysis: tasks must share training instances for gradient conflicts to reveal genuine relationships. When tasks are measured on the same inputs, gradient alignment reflects shared mechanistic structure; when measured on disjoint inputs, any apparent signal conflates task relationships with distributional shift. We discover this sample overlap requirement exhibits a sharp phase transition: below 30% overlap, gradient-task correlations are statistically indistinguishable from noise; above 40%, they reliably recover known biological structure. Comprehensive validation across multiple datasets achieves strong correlations and recovers biological pathway organization. Standard benchmarks systematically violate this requirement -- MoleculeNet operates at <5% overlap, TDC at 8-14% -- far below the threshold where gradient analysis becomes meaningful. This provides the first principled explanation for seven years of inconsistent MTL results.

---


### 101. [Hidden Biases in Conditioning Autoregressive Models](https://arxiv.org/abs/2604.07855)

**<font color=#1a73e8>作者：</font>** Francois Pachet, Pierre Roy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language and music models are increasingly used for constrained generation: rhyming lines, fixed meter, inpainting or infilling, positional endings, and other global form requirements. These systems often perform strikingly well, but the induced procedures are usually not exact conditioning of the underlying autoregressive model. This creates a hidden inferential bias, distinct from the better-known notion of bias inherited from the training set: samples are distorted relative to the true constrained distribution, with no generic guarantee of complete coverage of the admissible solution space or of correct conditional probabilities over valid completions. We formalize several exact inference tasks for autoregressive models and prove corresponding hardness results. For succinctly represented autoregressive models whose next-token probabilities are computable in polynomial time, exact sentence-level maximum a posteriori (MAP) decoding is NP-hard. This hardness persists under unary and metrical constraints. On the sampling side, exact conditioned normalization is \#P-hard even for regular constraints such as fixed-length terminal events. Unlike finite-state Markov models, general autoregressive models do not admit a bounded-state dynamic program for these tasks. These results formalize a standard claim in the neural decoding literature: local autoregressive sampling is easy, whereas exact decoding and exact conditioning under global form constraints are computationally intractable in general.

---


### 102. [MemReader: From Passive to Active Extraction for Long-Term Agent Memory](https://arxiv.org/abs/2604.07877)

**<font color=#1a73e8>作者：</font>** Jingyi Kang, Chunyu Li, Ding Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is fundamental for personalized and autonomous agents, yet populating it remains a bottleneck. Existing systems treat memory extraction as a one-shot, passive transcription from context to structured entries, which struggles with noisy dialogue, missing references, and cross-turn dependencies, leading to memory pollution, low-value writes, and inconsistency. In this paper, we introduce the MemReader family for active long-term memory extraction in agent systems: MemReader-0.6B, a compact and cost-efficient passive extractor distilled for accurate and schema-consistent structured outputs, and MemReader-4B, an active extractor optimized with Group Relative Policy Optimization (GRPO) to make memory writing decisions. Under a ReAct-style paradigm, MemReader-4B explicitly evaluates information value, reference ambiguity, and completeness before acting, and can selectively write memories, defer incomplete inputs, retrieve historical context, or discard irrelevant chatter. Experiments on LOCOMO, LongMemEval, and HaluMem show that MemReader consistently outperforms existing extraction-based baselines. In particular, MemReader-4B achieves state-of-the-art performance on tasks involving knowledge updating, temporal reasoning, and hallucination reduction. These results suggest that effective agent memory requires not merely extracting more information, but performing reasoning-driven and selective memory extraction to build low-noise and dynamically evolving long-term memory. Furthermore, MemReader has been integrated into MemOS and is being deployed in real-world applications. To support future research and adoption, we release the models and provide public API access.

---


### 103. [FlowGuard: Towards Lightweight In-Generation Safety Detection for Diffusion Models via Linear Latent Decoding](https://arxiv.org/abs/2604.07879)

**<font color=#1a73e8>作者：</font>** Jinghan Yang, Yihe Fan, Xudong Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based image generation models have advanced rapidly but pose a safety risk due to their potential to generate Not-Safe-For-Work (NSFW) content. Existing NSFW detection methods mainly operate either before or after image generation. Pre-generation methods rely on text prompts and struggle with the gap between prompt safety and image safety. Post-generation methods apply classifiers to final outputs, but they are poorly suited to intermediate noisy images. To address this, we introduce FlowGuard, a cross-model in-generation detection framework that inspects intermediate denoising steps. This is particularly challenging in latent diffusion, where early-stage noise obscures visual signals. FlowGuard employs a novel linear approximation for latent decoding and leverages a curriculum learning approach to stabilize training. By detecting unsafe content early, FlowGuard reduces unnecessary diffusion steps to cut computational costs. Our cross-model benchmark spanning nine diffusion-based backbones shows the effectiveness of FlowGuard for in-generation NSFW detection in both in-distribution and out-of-distribution settings, outperforming existing methods by over 30% in F1 score while delivering transformative efficiency gains, including slashing peak GPU memory demand by over 97% and projection time from 8.1 seconds to 0.2 seconds compared to standard VAE decoding.

---


### 104. [From Clicking to Moving: Embodied Micro-Movements as a New Modality for Data Literacy Learning](https://arxiv.org/abs/2604.07881)

**<font color=#1a73e8>作者：</font>** Annabella Sakunkoo, Jonathan Sakunkoo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Widespread digital learning has expanded access to education but has resulted in highly sedentary, click-based interaction, contributing to digital fatigue, reduced cognitive flexibility, and health risks associated with prolonged passive screen time. Meanwhile, data literacy has become an essential competency in a data-driven society, yet it is typically taught through passive, disembodied interfaces that offer little physical engagement. We present Kinetiq (Kinetic+IQ), a novel system that integrates fun, full-body micro-movements directly into data and numeracy problem solving. Instead of selecting answers with a mouse, learners interact through natural gestures such as reaching, dodging, heading, elbowing, or knee-raising, thus turning abstract data problem-solving into embodied experiences that integrate thinking with movement. In a preliminary within-subjects study comparing Kinetiq with conventional platforms, participants reported significantly higher affective valence, enjoyment, engagement, and motivation, while maintaining comparable learning gains. We contribute: (1) a task-integrated movement paradigm for data learning, (2) a cross-platform web and mobile app system enabling full-body learning in constrained everyday spaces, and (3) preliminary empirical evidence that embodied micro-movements can enrich the affective experience of data literacy learning.

---


### 105. [ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video](https://arxiv.org/abs/2604.07882)

**<font color=#1a73e8>作者：</font>** Boyuan Wang, Xiaofeng Wang, Yongkang Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing non-rigid objects with physical plausibility remains a significant challenge. Existing approaches leverage differentiable rendering for per-scene optimization, recovering geometry and dynamics but requiring expensive tuning or manual annotation, which limits practicality and generalizability. To address this, we propose ReconPhys, the first feedforward framework that jointly learns physical attribute estimation and 3D Gaussian Splatting reconstruction from a single monocular video. Our method employs a dual-branch architecture trained via a self-supervised strategy, eliminating the need for ground-truth physics labels. Given a video sequence, ReconPhys simultaneously infers geometry, appearance, and physical attributes. Experiments on a large-scale synthetic dataset demonstrate superior performance: our method achieves 21.64 PSNR in future prediction compared to 13.27 by state-of-the-art optimization baselines, while reducing Chamfer Distance from 0.349 to 0.004. Crucially, ReconPhys enables fast inference (<1 second) versus hours required by existing methods, facilitating rapid generation of simulation-ready assets for robotics and graphics.

---


### 106. [Reinforcement-Guided Synthetic Data Generation for Privacy-Sensitive Identity Recognition](https://arxiv.org/abs/2604.07884)

**<font color=#1a73e8>作者：</font>** Xuemei Jia, Jiawei Du, Hui Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity generative models are increasingly needed in privacy-sensitive scenarios, where access to data is severely restricted due to regulatory and copyright constraints. This scarcity hampers model development--ironically, in settings where generative models are most needed to compensate for the lack of data. This creates a self-reinforcing challenge: limited data leads to poor generative models, which in turn fail to mitigate data scarcity. To break this cycle, we propose a reinforcement-guided synthetic data generation framework that adapts general-domain generative priors to privacy-sensitive identity recognition tasks. We first perform a cold-start adaptation to align a pretrained generator with the target domain, establishing semantic relevance and initial fidelity. Building on this foundation, we introduce a multi-objective reward that jointly optimizes semantic consistency, coverage diversity, and expression richness, guiding the generator to produce both realistic and task-effective samples. During downstream training, a dynamic sample selection mechanism further prioritizes high-utility synthetic samples, enabling adaptive data scaling and improved domain alignment. Extensive experiments on benchmark datasets demonstrate that our framework significantly improves both generation fidelity and classification accuracy, while also exhibiting strong generalization to novel categories in small-data regimes.

---


### 107. [Contextualising (Im)plausible Events Triggers Figurative Language](https://arxiv.org/abs/2604.07885)

**<font color=#1a73e8>作者：</font>** Annerose Eichel, Tonmoy Rakshit, Sabine Schulte im Walde  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work explores the connection between (non-)literalness and plausibility at the example of subject-verb-object events in English. We design a systematic setup of plausible and implausible event triples in combination with abstract and concrete constituent categories. Our analysis of human and LLM-generated judgments and example contexts reveals substantial differences between assessments of plausibility. While humans excel at nuanced detection and contextualization of (non-)literal vs. implausible events, LLM results reveal only shallow contextualization patterns with a bias to trade implausibility for non-literal, plausible interpretations.

---


### 108. [Sampling-Aware 3D Spatial Analysis in Multiplexed Imaging](https://arxiv.org/abs/2604.07890)

**<font color=#1a73e8>作者：</font>** Ido Harlev, Tamar Oukhanov, Raz Ben-Uri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Highly multiplexed microscopy enables rich spatial characterization of tissues at single-cell resolution, yet most analyses rely on two-dimensional sections despite inherently three-dimensional tissue organization. Acquiring dense volumetric data in spatial proteomics remains costly and technically challenging, leaving practitioners to choose between 2D sections or 3D serial sections under limited imaging budgets. In this work, we study how sampling geometry impacts the stability of commonly used spatial statistics, and we introduce a geometry-aware reconstruction module that enables sparse yet consistent 3D analysis from serial sections. Using controlled simulations, we show that planar sampling reliably recovers global cell-type abundance but exhibits high variance for local statistics such as cell clustering and cell-cell interactions, particularly for rare or spatially localized populations. We observe consistent behavior in real multiplexed datasets, where interaction metrics and neighborhood relationships fluctuate substantially across individual sections. To support sparse 3D analysis in practice, we present a reconstruction approach that links cell projections across adjacent sections using phenotype and proximity constraints and recovers single-cell 3D centroids using cell-type-specific shape priors. We further analyze the trade-off between section spacing, coverage, and redundancy, identifying acquisition regimes that maximize reconstruction utility under fixed imaging budgets. We validate the reconstruction module on a public imaging mass cytometry dataset with dense axial sampling and demonstrate its downstream utility on an in-house CODEX dataset by enabling structure-level 3D analyses that are unreliable in 2D. Together, our results provide diagnostic tools and practical guidance for deciding when 2D sampling suffices and when sparse 3D reconstruction is warranted.

---


### 109. [DialBGM: A Benchmark for Background Music Recommendation from Everyday Multi-Turn Dialogues](https://arxiv.org/abs/2604.07895)

**<font color=#1a73e8>作者：</font>** Joonhyeok Shin, Jaehoon Kang, Yujun Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Selecting an appropriate background music (BGM) that supports natural human conversation is a common production step in media and interactive systems. In this paper, we introduce dialogue-conditioned BGM recommendation, where a model should select non-intrusive, fitting music for a multi-turn conversation that often contains no music descriptors. To study this novel problem, we present DialBGM, a benchmark of 1,200 open-domain daily dialogues, each paired with four candidate music clips and annotated with human preference rankings. Rankings are determined by background suitability criteria, including contextual relevance, non-intrusiveness, and consistency. We evaluate a wide range of open-source and proprietary models, including audio-language models and multimodal LLMs, and show that current models fall far short of human judgments; no model exceeds 35% Hit@1 when selecting the top-ranked clip. DialBGM provides a standardized benchmark for developing discourse-aware methods for BGM selection and for evaluating both retrieval-based and generative models.

---


### 110. [Visual Perceptual to Conceptual First-Order Rule Learning Networks](https://arxiv.org/abs/2604.07897)

**<font color=#1a73e8>作者：</font>** Kun Gao, Davide Soldà, Thomas Eiter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning rules plays a crucial role in deep learning, particularly in explainable artificial intelligence and enhancing the reasoning capabilities of large language models. While existing rule learning methods are primarily designed for symbolic data, learning rules from image data without supporting image labels and automatically inventing predicates remains a challenge. In this paper, we tackle these inductive rule learning problems from images with a framework called {\gamma}ILP, which provides a fully differentiable pipeline from image constant substitution to rule structure induction. Extensive experiments demonstrate that {\gamma}ILP achieves strong performance not only on classical symbolic relational datasets but also on relational image data and pure image datasets, such as Kandinsky patterns.

---


### 111. [PanoSAM2: Lightweight Distortion- and Memory-aware Adaptions of SAM2 for 360 Video Object Segmentation](https://arxiv.org/abs/2604.07901)

**<font color=#1a73e8>作者：</font>** Dingwen Xiao, Weiming Zhang, Shiqi Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 360 video object segmentation (360VOS) aims to predict temporally-consistent masks in 360 videos, offering full-scene coverage, benefiting applications, such as VR/AR and embodied AI. Learning 360VOS model is nontrivial due to the lack of high-quality labeled dataset. Recently, Segment Anything Models (SAMs), especially SAM2 -- with its design of memory module -- shows strong, promptable VOS capability. However, directly using SAM2 for 360VOS yields implausible results as 360 videos suffer from the projection distortion, semantic inconsistency of left-right sides, and sparse object mask information in SAM2's memory. To this end, we propose PanoSAM2, a novel 360VOS framework based on our lightweight distortion- and memory-aware adaptation strategies of SAM2 to achieve reliable 360VOS while retaining SAM2's user-friendly prompting design. Concretely, to tackle the projection distortion and semantic inconsistency issues, we propose a Pano-Aware Decoder with seam-consistent receptive fields and iterative distortion refinement to maintain continuity across the 0/360 degree boundary. Meanwhile, a Distortion-Guided Mask Loss is introduced to weight pixels by distortion magnitude, stressing stretched regions and boundaries. To address the object sparsity issue, we propose a Long-Short Memory Module to maintain a compact long-term object pointer to re-instantiate and align short-term memories, thereby enhancing temporal coherence. Extensive experiments show that PanoSAM2 yields substantial gains over SAM2: +5.6 on 360VOTS and +6.7 on PanoVOS, showing the effectiveness of our method.

---


### 112. [Kuramoto Oscillatory Phase Encoding: Neuro-inspired Synchronization for Improved Learning Efficiency](https://arxiv.org/abs/2604.07904)

**<font color=#1a73e8>作者：</font>** Mingqing Xiao, Yansen Wang, Dongqi Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal neural dynamics and oscillatory synchronization are widely implicated in biological information processing and have been hypothesized to support flexible coordination such as feature binding. By contrast, most deep learning architectures represent and propagate information through activation values, neglecting the joint dynamics of rate and phase. In this work, we introduce Kuramoto oscillatory Phase Encoding (KoPE) as an additional, evolving phase state to Vision Transformers, incorporating a neuro-inspired synchronization mechanism to advance learning efficiency. We show that KoPE can improve training, parameter, and data efficiency of vision models through synchronization-enhanced structure learning. Moreover, KoPE benefits tasks requiring structured understanding, including semantic and panoptic segmentation, representation alignment with language, and few-shot abstract visual reasoning (ARC-AGI). Theoretical analysis and empirical verification further suggest that KoPE can accelerate attention concentration for learning efficiency. These results indicate that synchronization can serve as a scalable, neuro-inspired mechanism for advancing state-of-the-art neural network models.

---


### 113. [Capture-Quiet Decomposition: A Verification Theorem for Chess Endgame Tablebases](https://arxiv.org/abs/2604.07907)

**<font color=#1a73e8>作者：</font>** Alexander Pavlov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present the Capture-Quiet Decomposition (CQD), a structural theorem for verifying Win-Draw-Loss (WDL) labelings of chess endgame tablebases. The theorem decomposes every legal position into exactly one of three categories -- terminal, capture, or quiet -- and shows that a WDL labeling is correct if and only if: (1) terminal positions are labeled correctly, (2) capture positions are consistent with verified sub-models of smaller piece count, and (3) quiet positions satisfy retrograde consistency within the same endgame. The key insight is that capture positions anchor the labeling to externally verified sub-models, breaking the circularity that allows trivial fixpoints (such as the all-draw labeling) to satisfy self-consistency alone. We validate CQD exhaustively on all 35 three- and four-piece endgames (42 million positions), all 110 five-piece endgames, and all 372 six-piece endgames -- 517 endgames in total -- with the decomposed verifier producing identical violation counts to a full retrograde baseline in every case.

---


### 114. [SAT: Balancing Reasoning Accuracy and Efficiency with Stepwise Adaptive Thinking](https://arxiv.org/abs/2604.07922)

**<font color=#1a73e8>作者：</font>** Weiyang Huang, Xuefeng Bai, Kehai Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) have revolutionized complex problem-solving, yet they exhibit a pervasive "overthinking", generating unnecessarily long reasoning chains. While current solutions improve token efficiency, they often sacrifice fine-grained control or risk disrupting the logical integrity of the reasoning process. To address this, we introduce Stepwise Adaptive Thinking (SAT), a framework that performs step-level, difficulty-aware pruning while preserving the core reasoning structure. SAT formulates reasoning as a Finite-State Machine (FSM) with distinct thinking modes (Slow, Normal, Fast, Skip). It navigates these states dynamically using a lightweight Process Reward Model (PRM), compressing easy steps while preserving depth for hard ones. Experiments across 9 LRMs and 7 benchmarks show that SAT achieves up to 40% reduction in reasoning tokens while generally maintaining or improving accuracy.

---


### 115. [Stitch4D: Sparse Multi-Location 4D Urban Reconstruction via Spatio-Temporal Interpolation](https://arxiv.org/abs/2604.07923)

**<font color=#1a73e8>作者：</font>** Hina Kogure, Kei Katsumata, Taiki Miyanishi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic urban environments are often captured by cameras placed at spatially separated locations with little or no view overlap. However, most existing 4D reconstruction methods assume densely overlapping views. When applied to such sparse observations, these methods fail to reconstruct intermediate regions and often introduce temporal artifacts. To address this practical yet underexplored sparse multi-location setting, we propose Stitch4D, a unified 4D reconstruction framework that explicitly compensates for missing spatial coverage in sparse observations. Stitch4D (i) synthesizes intermediate bridge views to densify spatial constraints and improve spatial coverage, and (ii) jointly optimizes real and synthesized observations within a unified coordinate frame under explicit inter-location consistency constraints. By restoring intermediate coverage before optimization, Stitch4D prevents geometric collapse and reconstructs coherent geometry and smooth scene dynamics even in sparsely observed environments. To evaluate this setting, we introduce Urban Sparse 4D (U-S4D), a CARLA-based benchmark designed to assess spatiotemporal alignment under sparse multi-location configurations. Experimental results on U-S4D show that Stitch4D surpasses representative 4D reconstruction baselines and achieves superior visual quality. These results indicate that recovering intermediate spatial coverage is essential for stable 4D reconstruction in sparse urban environments.

---


### 116. [Sinkhorn doubly stochastic attention rank decay analysis](https://arxiv.org/abs/2604.07925)

**<font color=#1a73e8>作者：</font>** Michela Lapenna, Rita Fioresi, Bahman Gharesifard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The self-attention mechanism is central to the success of Transformer architectures. However, standard row-stochastic attention has been shown to suffer from significant signal degradation across layers. In particular, it can induce rank collapse, resulting in increasingly uniform token representations, as well as entropy collapse, characterized by highly concentrated attention distributions. Recent work has highlighted the benefits of doubly stochastic attention as a form of entropy regularization, promoting a more balanced attention distribution and leading to improved empirical performance. In this paper, we study rank collapse across network depth and show that doubly stochastic attention matrices normalized with Sinkhorn algorithm preserve rank more effectively than standard Softmax row-stochastic ones. As previously shown for Softmax, skip connections are crucial to mitigate rank collapse. We empirically validate this phenomenon on both sentiment analysis and image classification tasks. Moreover, we derive a theoretical bound for the pure self-attention rank decay when using Sinkhorn normalization and find that rank decays to one doubly exponentially with depth, a phenomenon that has already been shown for Softmax.

---


### 117. [EigentSearch-Q+: Enhancing Deep Research Agents with Structured Reasoning Tools](https://arxiv.org/abs/2604.07927)

**<font color=#1a73e8>作者：</font>** Boer Zhang, Mingyan Wu, Dongzhuoran Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research requires reasoning over web evidence to answer open-ended questions, and it is a core capability for AI agents. Yet many deep research agents still rely on implicit, unstructured search behavior that causes redundant exploration and brittle evidence aggregation. Motivated by Anthropic's "think" tool paradigm and insights from the information-retrieval literature, we introduce Q+, a set of query and evidence processing tools that make web search more deliberate by guiding query planning, monitoring search progress, and extracting evidence from long web snapshots. We integrate Q+ into the browser sub-agent of Eigent, an open-source, production-ready multi-agent workforce for computer use, yielding EigentSearch-Q+. Across four benchmarks (SimpleQA-Verified, FRAMES, WebWalkerQA, and X-Bench DeepSearch), Q+ improves Eigent's browser agent benchmark-size-weighted average accuracy by 3.0, 3.8, and 0.6 percentage points (pp) for GPT-4.1, GPT-5.1, and Minimax M2.5 model backends, respectively. Case studies further suggest that EigentSearch-Q+ produces more coherent tool-calling trajectories by making search progress and evidence handling explicit.

---


### 118. [Generative 3D Gaussian Splatting for Arbitrary-ResolutionAtmospheric Downscaling and Forecasting](https://arxiv.org/abs/2604.07928)

**<font color=#1a73e8>作者：</font>** Tao Hana, Zhibin Wen, Zhenghao Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While AI-based numerical weather prediction (NWP) enables rapid forecasting, generating high-resolution outputs remains computationally demanding due to limited multi-scale adaptability and inefficient data representations. We propose the 3D Gaussian splatting-based scale-aware vision transformer (GSSA-ViT), a novel framework for arbitrary-resolution forecasting and flexible downscaling of high-dimensional atmospheric fields. Specifically, latitude-longitude grid points are treated as centers of 3D Gaussians. A generative 3D Gaussian prediction scheme is introduced to estimate key parameters, including covariance, attributes, and opacity, for unseen samples, improving generalization and mitigating overfitting. In addition, a scale-aware attention module is designed to capture cross-scale dependencies, enabling the model to effectively integrate information across varying downscaling ratios and support continuous resolution adaptation. To our knowledge, this is the first NWP approach that combines generative 3D Gaussian modeling with scale-aware attention for unified multi-scale prediction. Experiments on ERA5 show that the proposed method accurately forecasts 87 atmospheric variables at arbitrary resolutions, while evaluations on ERA5 and CMIP6 demonstrate its superior performance in downscaling tasks. The proposed framework provides an efficient and scalable solution for high-resolution, multi-scale atmospheric prediction and downscaling. Code is available at: this https URL.

---


### 119. [Robust Length Prediction: A Perspective from Heavy-Tailed Prompt-Conditioned Distributions](https://arxiv.org/abs/2604.07931)

**<font color=#1a73e8>作者：</font>** Jing Wang, Yu-Yang Qian, Ke Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Output-length prediction is important for efficient LLM serving, as it directly affects batching, memory reservation, and scheduling. For prompt-only length prediction, most existing methods use a one-shot sampled length as the label, implicitly treating each prompt as if it had one true target length. We show that this is unreliable: even under a fixed model and decoding setup, the same prompt induces a \emph{prompt-conditioned output length distribution}, not a deterministic scalar, and this distribution is consistent with \emph{heavy-tailed} behavior. Motivated by this, we cast length prediction as robust estimation from heavy-tailed prompt-conditioned length distributions. We propose prompt-conditioned length distribution (ProD) methods, which construct training targets from multiple independent generations of the same prompt. Two variants are developed to reuse the served LLM's hidden states: \mbox{ProD-M}, which uses a median-based target for robust point prediction, and ProD-D, which uses a distributional target that preserves prompt-conditioned uncertainty. We provide theoretical justifications by analyzing the estimation error under a surrogate model. Experiments across diverse scenarios show consistent gains in prediction quality.

---


### 120. [Shortcut Learning in Glomerular AI: Adversarial Penalties Hurt, Entropy Helps](https://arxiv.org/abs/2604.07936)

**<font color=#1a73e8>作者：</font>** Mohammad Daouk, Jan Ulrich Becker, Neeraja Kambham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stain variability is a pervasive source of distribution shift and potential shortcut learning in renal pathology AI. We ask whether lupus nephritis glomerular lesion classifiers exploit stain as a shortcut, and how to mitigate such bias without stain or site labels. We curate a multi-center, multi-stain dataset of 9{,}674 glomerular patches (224$\times$224) from 365 WSIs across three centers and four stains (PAS, H\&E, Jones, Trichrome), labeled as proliferative vs.\ non-proliferative. We evaluate Bayesian CNN and ViT backbones with Monte Carlo dropout in three settings: (1) stain-only classification; (2) a dual-head model jointly predicting lesion and stain with supervised stain loss; and (3) a dual-head model with label-free stain regularization via entropy maximization on the stain head. In (1), stain identity is trivially learnable, confirming a strong candidate shortcut. In (2), varying the strength and sign of stain supervision strongly modulates stain performance but leaves lesion metrics essentially unchanged, indicating no measurable stain-driven shortcut learning on this multi-stain, multi-center dataset, while overly adversarial stain penalties inflate predictive uncertainty. In (3), entropy-based regularization holds stain predictions near chance without degrading lesion accuracy or calibration. Overall, a carefully curated multi-stain dataset can be inherently robust to stain shortcuts, and a Bayesian dual-head architecture with label-free entropy regularization offers a simple, deployment-friendly safeguard against potential stain-related drift in glomerular AI.

---


### 121. [A Systematic Framework for Tabular Data Disentanglement](https://arxiv.org/abs/2604.07940)

**<font color=#1a73e8>作者：</font>** Ivan Tjuawinata, Andre Gunawan, Anh Quan Tran 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data, widely used in various applications such as industrial control systems, finance, and supply chain, often contains complex interrelationships among its attributes. Data disentanglement seeks to transform such data into latent variables with reduced interdependencies, facilitating more effective and efficient processing. Despite the extensive studies on data disentanglement over image, text, or audio data, tabular data disentanglement may require further investigation due to the more intricate attribute interactions typically found in tabular data. Moreover, due to the highly complex interrelationships, direct translation from other data domains results in suboptimal data disentanglement. Existing tabular data disentanglement methods, such as factor analysis, CT-GAN, and VAE face limitations including scalability issues, mode collapse, and poor extrapolation. In this paper, we propose the use of a framework to provide a systematic view on tabular data disentanglement that modularizes the process into four core components: data extraction, data modeling, model analysis, and latent representation extrapolation. We believe this work provides a deeper understanding of tabular data disentanglement and existing methods, and lays the foundation for potential future research in developing robust, efficient, and scalable data disentanglement techniques. Finally, we demonstrate the framework's applicability through a case study on synthetic tabular data generation, showcasing its potential in the particular downstream task of data synthesis.

---


### 122. [Fraud Detection System for Banking Transactions](https://arxiv.org/abs/2604.07952)

**<font color=#1a73e8>作者：</font>** Ranya Batsyas, Ritesh Yaduwanshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The expansion of digital payment systems has heightened both the scale and intricacy of online financial transactions, thereby increasing vulnerability to fraudulent activities. Detecting fraud effectively is complicated by the changing nature of attack strategies and the significant disparity between genuine and fraudulent transactions. This research introduces a machine learning-based fraud detection framework utilizing the PaySim synthetic financial transaction dataset. Following the CRISP-DM methodology, the study includes hypothesis-driven exploratory analysis, feature refinement, and a comparative assessment of baseline models such as Logistic Regression and tree-based classifiers like Random Forest, XGBoost, and Decision Tree. To tackle class imbalance, SMOTE is employed, and model performance is enhanced through hyperparameter tuning with GridSearchCV. The proposed framework provides a robust and scalable solution to enhance fraud prevention capabilities in FinTech transaction systems. Keywords: fraud detection, imbalanced data, HPO, SMOTE

---


### 123. [Pruning Extensions and Efficiency Trade-Offs for Sustainable Time Series Classification](https://arxiv.org/abs/2604.07953)

**<font color=#1a73e8>作者：</font>** Raphael Fischer, Angus Dempster, Sebastian Buschjäger 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series classification (TSC) enables important use cases, however lacks a unified understanding of performance trade-offs across models, datasets, and hardware. While resource awareness has grown in the field, TSC methods have not yet been rigorously evaluated for energy efficiency. This paper introduces a holistic evaluation framework that explicitly explores the balance of predictive performance and resource consumption in TSC. To boost efficiency, we apply a theoretically bounded pruning strategy to leading hybrid classifiers - Hydra and Quant - and present Hydrant, a novel, prunable combination of both. With over 4000 experimental configurations across 20 MONSTER datasets, 13 methods, and three compute setups, we systematically analyze how model design, hyperparameters, and hardware choices affect practical TSC performance. Our results showcase that pruning can significantly reduce energy consumption by up to 80% while maintaining competitive predictive quality, usually costing the model less than 5% of accuracy. The proposed methodology, experimental results, and accompanying software advance TSC toward sustainable and reproducible practice.

---


### 124. [ImVideoEdit: Image-learning Video Editing via 2D Spatial Difference Attention Blocks](https://arxiv.org/abs/2604.07958)

**<font color=#1a73e8>作者：</font>** Jiayang Xu, Fan Zhuo, Majun Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current video editing models often rely on expensive paired video data, which limits their practical scalability. In essence, most video editing tasks can be formulated as a decoupled spatiotemporal process, where the temporal dynamics of the pretrained model are preserved while spatial content is selectively and precisely modified. Based on this insight, we propose ImVideoEdit, an efficient framework that learns video editing capabilities entirely from image pairs. By freezing the pre-trained 3D attention modules and treating images as single-frame videos, we decouple the 2D spatial learning process to help preserve the original temporal dynamics. The core of our approach is a Predict-Update Spatial Difference Attention module that progressively extracts and injects spatial differences. Rather than relying on rigid external masks, we incorporate a Text-Guided Dynamic Semantic Gating mechanism for adaptive and implicit text-driven modifications. Despite training on only 13K image pairs for 5 epochs with exceptionally low computational overhead, ImVideoEdit achieves editing fidelity and temporal consistency comparable to larger models trained on extensive video datasets.

---


### 125. [Is your algorithm unlearning or untraining?](https://arxiv.org/abs/2604.07962)

**<font color=#1a73e8>作者：</font>** Eleni Triantafillou, Ahmed Imtiaz Humayun, Monica Ribero 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As models are getting larger and are trained on increasing amounts of data, there has been an explosion of interest into how we can ``delete'' specific data points or behaviours from a trained model, after the fact. This goal has been referred to as ``machine unlearning''. In this note, we argue that the term ``unlearning'' has been overloaded, with different research efforts spanning two distinct problem formulations, but without that distinction having been observed or acknowledged in the literature. This causes various issues, including ambiguity around when an algorithm is expected to work, use of inappropriate metrics and baselines when comparing different algorithms to one another, difficulty in interpreting results, as well as missed opportunities for pursuing critical research directions. In this note, we address this issue by establishing a fundamental distinction between two notions that we identify as \unlearning and \untraining, illustrated in Figure 1. In short, \untraining aims to reverse the effect of having trained on a given forget set, i.e. to remove the influence that that specific forget set examples had on the model during training. On the other hand, the goal of \unlearning is not just to remove the influence of those given examples, but to use those examples for the purpose of more broadly removing the entire underlying distribution from which those examples were sampled (e.g. the concept or behaviour that those examples represent). We discuss technical definitions of these problems and map problem settings studied in the literature to each. We hope to initiate discussions on disambiguating technical definitions and identify a set of overlooked research questions, as we believe that this a key missing step for accelerating progress in the field of ``unlearning''.

---


### 126. [Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966)

**<font color=#1a73e8>作者：</font>** Ziqi Cai, Taoyu Yang, Zheng Chang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved remarkable progress in video generation, but their controllability remains a major limitation. Key scene factors such as layout, lighting, and camera trajectory are often entangled or only weakly modeled, restricting their applicability in domains like filmmaking and virtual production where explicit scene control is essential. We present LiVER, a diffusion-based framework for scene-controllable video generation. To achieve this, we introduce a novel framework that conditions video synthesis on explicit 3D scene properties, supported by a new large-scale dataset with dense annotations of object layout, lighting, and camera parameters. Our method disentangles these properties by rendering control signals from a unified 3D representation. We propose a lightweight conditioning module and a progressive training strategy to integrate these signals into a foundational video diffusion model, ensuring stable convergence and high fidelity. Our framework enables a wide range of applications, including image-to-video and video-to-video synthesis where the underlying 3D scene is fully editable. To further enhance usability, we develop a scene agent that automatically translates high-level user instructions into the required 3D control signals. Experiments show that LiVER achieves state-of-the-art photorealism and temporal consistency while enabling precise, disentangled control over scene factors, setting a new standard for controllable video generation.

---


### 127. [AtomEval: Atomic Evaluation of Adversarial Claims in Fact Verification](https://arxiv.org/abs/2604.07967)

**<font color=#1a73e8>作者：</font>** Hongyi Cen, Mingxin Wang, Yule Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adversarial claim rewriting is widely used to test fact-checking systems, but standard metrics fail to capture truth-conditional consistency and often label semantically corrupted rewrites as successful. We introduce AtomEval, a validity-aware evaluation framework that decomposes claims into subject-relation-object-modifier (SROM) atoms and scores adversarial rewrites with Atomic Validity Scoring (AVS), enabling detection of factual corruption beyond surface similarity. Experiments on the FEVER dataset across representative attack strategies and LLM generators show that AtomEval provides more reliable evaluation signals in our experiments. Using AtomEval, we further analyze LLM-based adversarial generators and observe that stronger models do not necessarily produce more effective adversarial claims under validity-aware evaluation, highlighting previously overlooked limitations in current adversarial evaluation practices.

---


### 128. [Kathleen: Oscillator-Based Byte-Level Text Classification Without Tokenization or Attention](https://arxiv.org/abs/2604.07969)

**<font color=#1a73e8>作者：</font>** George Fountzoulas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Kathleen, a text classification architecture that operates directly on raw UTF-8 bytes using frequency-domain processing -- requiring no tokenizer, no attention mechanism, and only 733K parameters. Kathleen introduces three novel components: (1) RecurrentOscillatorBanks -- damped sinusoid convolutions with temporal memory for O(L) sequence processing; (2) an FFT-Rotate Wavetable Encoder that maps all 256 byte values using a single learnable vector (256 floats), replacing conventional embedding tables (65K parameters) while improving accuracy; (3) PhaseHarmonics -- a sinusoidal non-linearity with just 6 learnable phase parameters that our ablation identifies as the single most impactful component (+2.6% accuracy, <0.001% of model parameters). Through comprehensive ablation of a 1.8M-parameter predecessor, we show that frequency-domain components systematically outperform complex cognitive architectures: removing a 560K-parameter bio-inspired framework costs only -0.2%, while removing the 6-parameter PhaseHarmonics costs -2.6%. The resulting Kathleen-Clean achieves 88.6% on IMDB, 92.3% on AG News, and 83.3% on SST-2 -- outperforming a tokenized counterpart with 16x more parameters on IMDB (+1.6%) and AG News (+2.1%). Kathleen processes sequences in O(L) time and memory, enabling byte-level operation at sequence lengths where O(L^2) Transformers exhaust GPU memory.

---


### 129. [Object-Centric Stereo Ranging for Autonomous Driving: From Dense Disparity to Census-Based Template Matching](https://arxiv.org/abs/2604.07980)

**<font color=#1a73e8>作者：</font>** Qihao Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate depth estimation is critical for autonomous driving perception systems, particularly for long range vehicle detection on highways. Traditional dense stereo matching methods such as Block Matching (BM) and Semi Global Matching (SGM) produce per pixel disparity maps but suffer from high computational cost, sensitivity to radiometric differences between stereo cameras, and poor accuracy at long range where disparity values are small. In this report, we present a comprehensive stereo ranging system that integrates three complementary depth estimation approaches: dense BM/SGM disparity, object centric Census based template matching, and monocular geometric priors, within a unified detection ranging tracking pipeline. Our key contribution is a novel object centric Census based template matching algorithm that performs GPU accelerated sparse stereo matching directly within detected bounding boxes, employing a far close divide and conquer strategy, forward backward verification, occlusion aware sampling, and robust multi block aggregation. We further describe an online calibration refinement framework that combines auto rectification offset search, radar stereo voting based disparity correction, and object level radar stereo association for continuous extrinsic drift compensation. The complete system achieves real time performance through asynchronous GPU pipeline design and delivers robust ranging across diverse driving conditions including nighttime, rain, and varying illumination.

---


### 130. [DP-DeGauss: Dynamic Probabilistic Gaussian Decomposition for Egocentric 4D Scene Reconstruction](https://arxiv.org/abs/2604.07986)

**<font color=#1a73e8>作者：</font>** Tingxi Chen, Zhengxue Cheng, Houqiang Zhong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video is crucial for next-generation 4D scene reconstruction, with applications in AR/VR and embodied AI. However, reconstructing dynamic first-person scenes is challenging due to complex ego-motion, occlusions, and hand-object interactions. Existing decomposition methods are ill-suited, assuming fixed viewpoints or merging dynamics into a single foreground. To address these limitations, we introduce DP-DeGauss, a dynamic probabilistic Gaussian decomposition framework for egocentric 4D reconstruction. Our method initializes a unified 3D Gaussian set from COLMAP priors, augments each with a learnable category probability, and dynamically routes them into specialized deformation branches for background, hands, or object modeling. We employ category-specific masks for better disentanglement and introduce brightness and motion-flow control to improve static rendering and dynamic reconstruction. Extensive experiments show that DP-DeGauss outperforms baselines by +1.70dB in PSNR on average with SSIM and LPIPS gains. More importantly, our framework achieves the first and state-of-the-art disentanglement of background, hand, and object components, enabling explicit, fine-grained separation, paving the way for more intuitive ego scene understanding and editing.

---


### 131. [SceneScribe-1M: A Large-Scale Video Dataset with Comprehensive Geometric and Semantic Annotations](https://arxiv.org/abs/2604.07990)

**<font color=#1a73e8>作者：</font>** Yunnan Wang, Kecheng Zheng, Jianyuan Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The convergence of 3D geometric perception and video synthesis has created an unprecedented demand for large-scale video data that is rich in both semantic and spatio-temporal information. While existing datasets have advanced either 3D understanding or video generation, a significant gap remains in providing a unified resource that supports both domains at scale. To bridge this chasm, we introduce SceneScribe-1M, a new large-scale, multi-modal video dataset. It comprises one million in-the-wild videos, each meticulously annotated with detailed textual descriptions, precise camera parameters, dense depth maps, and consistent 3D point tracks. We demonstrate the versatility and value of SceneScribe-1M by establishing benchmarks across a wide array of downstream tasks, including monocular depth estimation, scene reconstruction, and dynamic point tracking, as well as generative tasks such as text-to-video synthesis, with or without camera control. By open-sourcing SceneScribe-1M, we aim to provide a comprehensive benchmark and a catalyst for research, fostering the development of models that can both perceive the dynamic 3D world and generate controllable, realistic video content.

---


### 132. [SAT: Selective Aggregation Transformer for Image Super-Resolution](https://arxiv.org/abs/2604.07994)

**<font color=#1a73e8>作者：</font>** Dinh Phu Tran, Thao Do, Saad Wazir 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based approaches have revolutionized image super-resolution by modeling long-range dependencies. However, the quadratic computational complexity of vanilla self-attention mechanisms poses significant challenges, often leading to compromises between efficiency and global context exploitation. Recent window-based attention methods mitigate this by localizing computations, but they often yield restricted receptive fields. To mitigate these limitations, we propose Selective Aggregation Transformer (SAT). This novel transformer efficiently captures long-range dependencies, leading to an enlarged model receptive field by selectively aggregating key-value matrices (reducing the number of tokens by 97\%) via our Density-driven Token Aggregation algorithm while maintaining the full resolution of the query matrix. This design significantly reduces computational costs, resulting in lower complexity and enabling scalable global interactions without compromising reconstruction fidelity. SAT identifies and represents each cluster with a single aggregation token, utilizing density and isolation metrics to ensure that critical high-frequency details are preserved. Experimental results demonstrate that SAT outperforms the state-of-the-art method PFT by up to 0.22dB, while the total number of FLOPs can be reduced by up to 27\%.

---


### 133. [Benchmarking Deep Learning for Future Liver Remnant Segmentation in Colorectal Liver Metastasis](https://arxiv.org/abs/2604.07999)

**<font color=#1a73e8>作者：</font>** Anthony T. Wu, Arghavan Rezvani, Kela Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of the future liver remnant (FLR) is critical for surgical planning in colorectal liver metastases (CRLM) to prevent fatal post-hepatectomy liver failure. However, this segmentation task is technically challenging due to complex resection boundaries, convoluted hepatic vasculature and diffuse metastatic lesions. A primary bottleneck in developing automated AI tools has been the lack of high-fidelity, validated data. We address this gap by manually refining all 197 volumes from the public CRLM-CT-Seg dataset, creating the first open-source, validated benchmark for this task. We then establish the first segmentation baselines, comparing cascaded (Liver->CRLM->FLR) and end-to-end (E2E) strategies using nnU-Net, SwinUNETR, and STU-Net. We find a cascaded nnU-Net achieves the best final FLR segmentation Dice (0.767), while the pretrained STU-Net provides superior CRLM segmentation (0.620 Dice) and is significantly more robust to cascaded errors. This work provides the first validated benchmark and a reproducible framework to accelerate research in AI-assisted surgical planning.

---


### 134. [PASK: Toward Intent-Aware Proactive Agents with Long-Term Memory](https://arxiv.org/abs/2604.08000)

**<font color=#1a73e8>作者：</font>** Zhifei Xie, Zongzheng Hu, Fangda Ye 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proactivity is a core expectation for AGI. Prior work remains largely confined to laboratory settings, leaving a clear gap in real-world proactive agent: depth, complexity, ambiguity, precision and real-time constraints. We study this setting, where useful intervention requires inferring latent needs from ongoing context and grounding actions in evolving user memory under latency and long-horizon constraints. We first propose DD-MM-PAS (Demand Detection, Memory Modeling, Proactive Agent System) as a general paradigm for streaming proactive AI agent. We instantiate this paradigm in Pask, with streaming IntentFlow model for DD, a hybrid memory (workspace, user, global) for long-term MM, PAS infra framework and introduce how these components form a closed loop. We also introduce LatentNeeds-Bench, a real-world benchmark built from user-consented data and refined through thousands of rounds of human editing. Experiments show that IntentFlow matches leading Gemini3-Flash models under latency constraints, while identifying deeper user intent.

---


### 135. [The ecosystem of machine learning competitions: Platforms, participants, and their impact on AI development](https://arxiv.org/abs/2604.08001)

**<font color=#1a73e8>作者：</font>** Ioannis Nasios  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning competitions (MLCs) play a pivotal role in advancing artificial intelligence (AI) by fostering innovation, skill development, and practical problem-solving. This study provides a comprehensive analysis of major competition platforms such as Kaggle and Zindi, examining their workflows, evaluation methodologies, and reward structures. It further assesses competition quality, participant expertise, and global reach, with particular attention to demographic trends among top-performing competitors. By exploring the motivations of competition hosts, this paper underscores the significant role of MLCs in shaping AI development, promoting collaboration, and driving impactful technological progress. Furthermore, by combining literature synthesis with platform-level data analysis and practitioner insights a comprehensive understanding of the MLC ecosystem is provided.
Moreover, the paper demonstrates that MLCs function at the intersection of academic research and industrial application, fostering the exchange of knowledge, data, and practical methodologies across domains. Their strong ties to open-source communities further promote collaboration, reproducibility, and continuous innovation within the broader ML ecosystem. By shaping research priorities, informing industry standards, and enabling large-scale crowdsourced problem-solving, these competitions play a key role in the ongoing evolution of AI. The study provides insights relevant to researchers, practitioners, and competition organizers, and includes an examination of the future trajectory and sustained influence of MLCs on AI development.

---


### 136. [Evaluating Counterfactual Explanation Methods on Incomplete Inputs](https://arxiv.org/abs/2604.08004)

**<font color=#1a73e8>作者：</font>** Francesco Leofante, Daniel Neider, Mustafa Yalçıner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing algorithms for generating Counterfactual Explanations (CXs) for Machine Learning (ML) typically assume fully specified inputs. However, real-world data often contains missing values, and the impact of these incomplete inputs on the performance of existing CX methods remains unexplored. To address this gap, we systematically evaluate recent CX generation methods on their ability to provide valid and plausible counterfactuals when inputs are incomplete. As part of this investigation, we hypothesize that robust CX generation methods will be better suited to address the challenge of providing valid and plausible counterfactuals when inputs are incomplete. Our findings reveal that while robust CX methods achieve higher validity than non-robust ones, all methods struggle to find valid counterfactuals. These results motivate the need for new CX methods capable of handling incomplete inputs.

---


### 137. [Preference Redirection via Attention Concentration: An Attack on Computer Use Agents](https://arxiv.org/abs/2604.08005)

**<font color=#1a73e8>作者：</font>** Dominik Seip, Matthias Hein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advancements in multimodal foundation models have enabled the development of Computer Use Agents (CUAs) capable of autonomously interacting with GUI environments. As CUAs are not restricted to certain tools, they allow to automate more complex agentic tasks but at the same time open up new security vulnerabilities. While prior work has concentrated on the language modality, the vulnerability of the vision modality has received less attention. In this paper, we introduce PRAC, a novel attack that, unlike prior work targeting the VLM output directly, manipulates the model's internal preferences by redirecting its attention toward a stealthy adversarial patch. We show that PRAC is able to manipulate the selection process of a CUA on an online shopping platform towards a chosen target product. While we require white-box access to the model for the creation of the attack, we show that our attack generalizes to fine-tuned versions of the same model, presenting a critical threat as multiple companies build specific CUAs based on open weights models.

---


### 138. [SearchAD: Large-Scale Rare Image Retrieval Dataset for Autonomous Driving](https://arxiv.org/abs/2604.08008)

**<font color=#1a73e8>作者：</font>** Felix Embacher, Jonas Uhrig, Marius Cordts 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieving rare and safety-critical driving scenarios from large-scale datasets is essential for building robust autonomous driving (AD) systems. As dataset sizes continue to grow, the key challenge shifts from collecting more data to efficiently identifying the most relevant samples. We introduce SearchAD, a large-scale rare image retrieval dataset for AD containing over 423k frames drawn from 11 established datasets. SearchAD provides high-quality manual annotations of more than 513k bounding boxes covering 90 rare categories. It specifically targets the needle-in-a-haystack problem of locating extremely rare classes, with some appearing fewer than 50 times across the entire dataset. Unlike existing benchmarks, which focused on instance-level retrieval, SearchAD emphasizes semantic image retrieval with a well-defined data split, enabling text-to-image and image-to-image retrieval, few-shot learning, and fine-tuning of multi-modal retrieval models. Comprehensive evaluations show that text-based methods outperform image-based ones due to stronger inherent semantic grounding. While models directly aligning spatial visual features with language achieve the best zero-shot results, and our fine-tuning baseline significantly improves performance, absolute retrieval capabilities remain unsatisfactory. With a held-out test set on a public benchmark server, SearchAD establishes the first large-scale dataset for retrieval-driven data curation and long-tail perception research in AD: this https URL

---


### 139. [Component-Adaptive and Lesion-Level Supervision for Improved Small Structure Segmentation in Brain MRI](https://arxiv.org/abs/2604.08015)

**<font color=#1a73e8>作者：</font>** Minh Sao Khue Luu, Evgeniy N. Pavlovskiy, Bair N. Tuchinov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a unified objective function, termed CATMIL, that augments the base segmentation loss with two auxiliary supervision terms operating at different levels. The first term, Component-Adaptive Tversky, reweights voxel contributions based on connected components to balance the influence of lesions of different sizes. The second term, based on Multiple Instance Learning, introduces lesion-level supervision by encouraging the detection of each lesion instance. These terms are combined with the standard nnU-Net loss to jointly optimize voxel-level segmentation accuracy and lesion-level detection. We evaluate the proposed objective on the MSLesSeg dataset using a consistent nnU-Net framework and 5-fold cross-validation. The results show that CATMIL achieves the most balanced performance across segmentation accuracy, lesion detection, and error control. It improves Dice score (0.7834) and reduces boundary error compared to standard losses. More importantly, it substantially increases small lesion recall and reduces false negatives, while maintaining the lowest false positive volume among compared methods. These findings demonstrate that integrating component-level and lesion-level supervision within a unified objective provides an effective and practical approach for improving small lesion segmentation in highly imbalanced settings. All code and pretrained models are available at \href{this https URL}{this url}.

---


### 140. [xDup: Privacy-Preserving Deduplication for Humanitarian Organizations using Fuzzy PSI](https://arxiv.org/abs/2604.08019)

**<font color=#1a73e8>作者：</font>** Tim Rausch, Sylvain Chatel, Wouter Lueks  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Humanitarian organizations help to ensure people's livelihoods in crisis situations. Typically, multiple organizations operate in the same region. To ensure that the limited budget of these organizations can help as many people as possible, organizations perform cross-organizational deduplication to detect duplicate registrations and ensure recipients receive aid from at most one organization. Current deduplication approaches risk privacy harm to vulnerable aid recipients by sharing their data with other organizations. We analyzed the needs of humanitarian organizations to identify the requirements for privacy-friendly cross-organizational deduplication fit for real-life humanitarian missions. We present xDup, a new practical deduplication system that meets the requirements of humanitarian organizations and is two orders of magnitude faster than current solutions. xDup builds on Fuzzy PSI, and we present otFPSI, a concretely efficient Fuzzy PSI protocol for Hamming Space without input assumptions. We show that it is more efficient than existing Fuzzy PSI protocols.

---


### 141. [From Universal to Individualized Actionability: Revisiting Personalization in Algorithmic Recourse](https://arxiv.org/abs/2604.08030)

**<font color=#1a73e8>作者：</font>** Lena Marie Budde, Ayan Majumdar, Richard Uth 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Algorithmic recourse aims to provide actionable recommendations that enable individuals to change unfavorable model outcomes, and prior work has extensively studied properties such as efficiency, robustness, and fairness. However, the role of personalization in recourse remains largely implicit and underexplored. While existing approaches incorporate elements of personalization through user interactions, they typically lack an explicit definition of personalization and do not systematically analyze its downstream effects on other recourse desiderata.
In this paper, we formalize personalization as individual actionability, characterized along two dimensions: hard constraints that specify which features are individually actionable, and soft, individualized constraints that capture preferences over action values and costs. We operationalize these dimensions within the causal algorithmic recourse framework, adopting a pre-hoc user-prompting approach in which individuals express preferences via rankings or scores prior to the generation of any recourse recommendation. Through extensive empirical evaluation, we investigate how personalization interacts with key recourse desiderata, including validity, cost, and plausibility. Our results highlight important trade-offs: individual actionability constraints, particularly hard ones, can substantially degrade the plausibility and validity of recourse recommendations across amortized and non-amortized approaches. Notably, we also find that incorporating individual actionability can reveal disparities in the cost and plausibility of recourse actions across socio-demographic groups. These findings underscore the need for principled definitions, careful operationalization, and rigorous evaluation of personalization in algorithmic recourse.

---


### 142. ["Why This Avoidance Maneuver?" Contrastive Explanations in Human-Supervised Maritime Autonomous Navigation](https://arxiv.org/abs/2604.08032)

**<font color=#1a73e8>作者：</font>** Joel Jose, Andreas Madsen, Andreas Brandsæter 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated maritime collision avoidance will rely on human supervision for the foreseeable future. This necessitates transparency into how the system perceives a scenario and plans a maneuver. However, the causal logic behind avoidance maneuvers is often complex and difficult to convey to a navigator. This paper explores how to explain these factors in a selective, understandable manner for supervisors with a nautical background. We propose a method for generating contrastive explanations, which provide human-centric insights by comparing a system's proposed solution against relevant alternatives. To evaluate this, we developed a framework that uses visual and textual cues to highlight key objectives from a state-of-the-art collision avoidance system. An exploratory user study with four experienced marine officers suggests that contrastive explanations support the understanding of the system's objectives. However, our findings also reveal that while these explanations are highly valuable in complex multi-vessel encounters, they can increase cognitive workload, suggesting that future maritime interfaces may benefit most from demand-driven or scenario-specific explanation strategies.

---


### 143. [Rotation Equivariant Convolutions in Deformable Registration of Brain MRI](https://arxiv.org/abs/2604.08034)

**<font color=#1a73e8>作者：</font>** Arghavan Rezvani, Kun Han, Anthony T. Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image registration is a fundamental task that aligns anatomical structures between images. While CNNs perform well, they lack rotation equivariance - a rotated input does not produce a correspondingly rotated output. This hinders performance by failing to exploit the rotational symmetries inherent in anatomical structures, particularly in brain MRI. In this work, we integrate rotation-equivariant convolutions into deformable brain MRI registration networks. We evaluate this approach by replacing standard encoders with equivariant ones in three baseline architectures, testing on multiple public brain MRI datasets.
Our experiments demonstrate that equivariant encoders have three key advantages: 1) They achieve higher registration accuracy while reducing network parameters, confirming the benefit of this anatomical inductive bias. 2) They outperform baselines on rotated input pairs, demonstrating robustness to orientation variations common in clinical practice. 3) They show improved performance with less training data, indicating greater sample efficiency. Our results demonstrate that incorporating geometric priors is a critical step toward building more robust, accurate, and efficient registration models.

---


### 144. [PriPG-RL: Privileged Planner-Guided Reinforcement Learning for Partially Observable Systems with Anytime-Feasible MPC](https://arxiv.org/abs/2604.08036)

**<font color=#1a73e8>作者：</font>** Mohsen Amiri, Mohsen Amiri, Ali Beikmohammadi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper addresses the problem of training a reinforcement learning (RL) policy under partial observability by exploiting a privileged, anytime-feasible planner agent available exclusively during training. We formalize this as a Partially Observable Markov Decision Process (POMDP) in which a planner agent with access to an approximate dynamical model and privileged state information guides a learning agent that observes only a lossy projection of the true state. To realize this framework, we introduce an anytime-feasible Model Predictive Control (MPC) algorithm that serves as the planner agent. For the learning agent, we propose Planner-to-Policy Soft Actor-Critic (P2P-SAC), a method that distills the planner agent's privileged knowledge to mitigate partial observability and thereby improve both sample efficiency and final policy performance. We support this framework with rigorous theoretical analysis. Finally, we validate our approach in simulation using NVIDIA Isaac Lab and successfully deploy it on a real-world Unitree Go2 quadruped navigating complex, obstacle-rich environments.

---


### 145. [PrivFedTalk: Privacy-Aware Federated Diffusion with Identity-Stable Adapters for Personalized Talking-Head Generation](https://arxiv.org/abs/2604.08037)

**<font color=#1a73e8>作者：</font>** Soumya Mazumdar, Vineet Kumar Rakesh, Tapas Samanta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Talking-head generation has advanced rapidly with diffusion-based generative models, but training usually depends on centralized face-video and speech datasets, raising major privacy concerns. The problem is more acute for personalized talking-head generation, where identity-specific data are highly sensitive and often cannot be pooled across users or devices. PrivFedTalk is presented as a privacy-aware federated framework for personalized talking-head generation that combines conditional latent diffusion with parameter-efficient identity adaptation. A shared diffusion backbone is trained across clients, while each client learns lightweight LoRA identity adapters from local private audio-visual data, avoiding raw data sharing and reducing communication cost. To address heterogeneous client distributions, Identity-Stable Federated Aggregation (ISFA) weights client updates using privacy-safe scalar reliability signals computed from on-device identity consistency and temporal stability estimates. Temporal-Denoising Consistency (TDC) regularization is introduced to reduce inter-frame drift, flicker, and identity drift during federated denoising. To limit update-side privacy risk, secure aggregation and client-level differential privacy are applied to adapter updates. The implementation supports both low-memory GPU execution and multi-GPU client-parallel training on heterogeneous shared hardware. Comparative experiments on the present setup across multiple training and aggregation conditions with PrivFedTalk, FedAvg, and FedProx show stable federated optimization and successful end-to-end training and evaluation under constrained resources. The results support the feasibility of privacy-aware personalized talking-head training in federated environments, while suggesting that stronger component-wise, privacy-utility, and qualitative claims need further standardized evaluation.

---


### 146. [Beyond Mamba: Enhancing State-space Models with Deformable Dilated Convolutions for Multi-scale Traffic Object Detection](https://arxiv.org/abs/2604.08038)

**<font color=#1a73e8>作者：</font>** Jun Li, Yingying Shi, Zhixuan Ruan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In a real-world traffic scenario, varying-scale objects are usually distributed in a cluttered background, which poses great challenges to accurate detection. Although current Mamba-based methods can efficiently model long-range dependencies, they still struggle to capture small objects with abundant local details, which hinders joint modeling of local structures and global semantics. Moreover, state-space models exhibit limited hierarchical feature representation and weak cross-scale interaction due to flat sequential modeling and insufficient spatial inductive biases, leading to sub-optimal performance in complex scenes. To address these issues, we propose a Mamba with Deformable Dilated Convolutions Network (MDDCNet) for accurate traffic object detection in this study. In MDDCNet, a well-designed hybrid backbone with successive Multi-Scale Deformable Dilated Convolution (MSDDC) blocks and Mamba blocks enables hierarchical feature representation from local details to global semantics. Meanwhile, a Channel-Enhanced Feed-Forward Network (CE-FFN) is further devised to overcome the limited channel interaction capability of conventional feed-forward networks, whilst a Mamba-based Attention-Aggregating Feature Pyramid Network (A^2FPN) is constructed to achieve enhanced multi-scale feature fusion and interaction. Extensive experimental results on public benchmark and real-world datasets demonstrate the superiority of our method over various advanced detectors. The code is available at this https URL.

---


### 147. [Guiding a Diffusion Model by Swapping Its Tokens](https://arxiv.org/abs/2604.08048)

**<font color=#1a73e8>作者：</font>** Weijia Zhang, Yuehao Liu, Shanyan Guan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classifier-Free Guidance (CFG) is a widely used inference-time technique to boost the image quality of diffusion models. Yet, its reliance on text conditions prevents its use in unconditional generation. We propose a simple method to enable CFG-like guidance for both conditional and unconditional generation. The key idea is to generate a perturbed prediction via simple token swap operations, and use the direction between it and the clean prediction to steer sampling towards higher-fidelity distributions. In practice, we swap pairs of most semantically dissimilar token latents in either spatial or channel dimensions. Unlike existing methods that apply perturbation in a global or less constrained manner, our approach selectively exchanges and recomposes token latents, allowing finer control over perturbation and its influence on generated samples. Experiments on MS-COCO 2014, MS-COCO 2017, and ImageNet datasets demonstrate that the proposed Self-Swap Guidance (SSG), when applied to popular diffusion models, outperforms previous condition-free methods in image fidelity and prompt alignment under different set-ups. Its fine-grained perturbation granularity also improves robustness, reducing side-effects across a wider range of perturbation strengths. Overall, SSG extends CFG to a broader scope of applications including both conditional and unconditional generation, and can be readily inserted into any diffusion model as a plug-in to gain immediate improvements.

---


### 148. [Efficient Provably Secure Linguistic Steganography via Range Coding](https://arxiv.org/abs/2604.08052)

**<font color=#1a73e8>作者：</font>** Ruiyi Yan, Yugo Murawaki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linguistic steganography involves embedding secret messages within seemingly innocuous texts to enable covert communication. Provable security, which is a long-standing goal and key motivation, has been extended to language-model-based steganography. Previous provably secure approaches have achieved perfect imperceptibility, measured by zero Kullback-Leibler (KL) divergence, but at the expense of embedding capacity. In this paper, we attempt to directly use a classic entropy coding method (range coding) to achieve secure steganography, and then propose an efficient and provably secure linguistic steganographic method with a rotation mechanism. Experiments across various language models show that our method achieves around 100% entropy utilization (embedding efficiency) for embedding capacity, outperforming the existing baseline methods. Moreover, it achieves high embedding speeds (up to 1554.66 bits/s on GPT-2). The code is available at this http URL.

---


### 149. [Automating aggregation strategy selection in federated learning](https://arxiv.org/abs/2604.08056)

**<font color=#1a73e8>作者：</font>** Dian S. Y. Pang, Endrias Y. Ergetu, Eric Topham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning enables collaborative model training without centralising data, but its effectiveness varies with the selection of the aggregation strategy. This choice is non-trivial, as performance varies widely across datasets, heterogeneity levels, and compute constraints. We present an end-to-end framework that automates, streamlines, and adapts aggregation strategy selection for federated learning. The framework operates in two modes: a single-trial mode, where large language models infer suitable strategies from user-provided or automatically detected data characteristics, and a multi-trial mode, where a lightweight genetic search efficiently explores alternatives under constrained budgets. Extensive experiments across diverse datasets show that our approach enhances robustness and generalisation under non-IID conditions while reducing the need for manual intervention. Overall, this work advances towards accessible and adaptive federated learning by automating one of its most critical design decisions, the choice of an aggregation strategy.

---


### 150. [Tensor-Augmented Convolutional Neural Networks: Enhancing Expressivity with Generic Tensor Kernels](https://arxiv.org/abs/2604.08072)

**<font color=#1a73e8>作者：</font>** Chia-Wei Hsing, Wei-Lin Tu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional Neural Networks (CNNs) excel at extracting local features hierarchically, but their performance in capturing complex correlations hinges heavily on deep architectures, which are usually computationally demanding and difficult to interpret. To address these issues, we propose a physically-guided shallow model: tensor-augmented CNN (TACNN), which replaces conventional convolution kernels with generic tensors to enhance representational capacity. This choice is motivated by the fact that an order-$N$ tensor naturally encodes an arbitrary quantum superposition state in the Hilbert space of dimension $d^N$, where $d$ is the local physical dimension, thus offering substantially richer expressivity. Furthermore, in our design the convolution output of each layer becomes a multilinear form capable of capturing high-order feature correlations, thereby equipping a shallow multilayer architecture with an expressive power competitive to that of deep CNNs. On the Fashion-MNIST benchmark, TACNN demonstrates clear advantages over conventional CNNs, achieving remarkable accuracies with only a few layers. In particular, a TACNN with only two convolution layers attains a test accuracy of 93.7$\%$, surpassing or matching considerably deeper models such as VGG-16 (93.5$\%$) and GoogLeNet (93.7$\%$). These findings highlight TACNN as a promising framework that strengthens model expressivity while preserving architectural simplicity, paving the way towards more interpretable and efficient deep learning models.

---


### 151. [AdaSpark: Adaptive Sparsity for Efficient Long-Video Understanding](https://arxiv.org/abs/2604.08077)

**<font color=#1a73e8>作者：</font>** Handong Li, Zikang Liu, Longteng Guo 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Processing long-form videos with Video Large Language Models (Video-LLMs) is computationally prohibitive. Current efficiency methods often compromise fine-grained perception through irreversible information disposal or inhibit long-range temporal modeling via rigid, predefined sparse patterns. This paper introduces AdaSpark, an adaptive sparsity framework designed to address these limitations. AdaSpark first partitions video inputs into 3D spatio-temporal cubes. It then employs two co-designed, context-aware components: (1) Adaptive Cube-Selective Attention (AdaS-Attn), which adaptively selects a subset of relevant video cubes to attend for each query token, and (2) Adaptive Token-Selective FFN (AdaS-FFN), which selectively processes only the most salient tokens within each cube. An entropy-based (Top-p) selection mechanism adaptively allocates computational resources based on input complexity. Experiments demonstrate that AdaSpark significantly reduces computational load by up to 57% FLOPs while maintaining comparable performance to dense models and preserving fine-grained, long-range dependencies, as validated on challenging hour-scale video benchmarks.

---


### 152. [From Binary Groundedness to Support Relations: Towards a Reader-Centred Taxonomy for Comprehension of AI Output](https://arxiv.org/abs/2604.08082)

**<font color=#1a73e8>作者：</font>** Advait Sarkar, Christian Poelitz, Viktor Kewenig  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI tools often answer questions using source documents, e.g., through retrieval augmented generation. Current groundedness and hallucination evaluations largely frame the relationship between an answer and its sources as binary (the answer is either supported or unsupported). However, this obscures both the syntactic moves (e.g., direct quotation vs. paraphrase) and the interpretive moves (e.g., induction vs. deduction) performed when models reformulate evidence into an answer. This limits both benchmarking and user-facing provenance interfaces.
We propose the development of a reader-centred taxonomy of grounding as a set of support relations between generated statements and source documents. We explain how this might be synthesised from prior research in linguistics and philosophy of language, and evaluated through a benchmark and human annotation protocol. Such a framework would enable interfaces that communicate not just whether a claim is grounded, but how.

---


### 153. [DiffVC: A Non-autoregressive Framework Based on Diffusion Model for Video Captioning](https://arxiv.org/abs/2604.08084)

**<font color=#1a73e8>作者：</font>** Junbo Wang, Liangyu Fu, Yuke Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current video captioning methods usually use an encoder-decoder structure to generate text autoregressively. However, autoregressive methods have inherent limitations such as slow generation speed and large cumulative error. Furthermore, the few non-autoregressive counterparts suffer from deficiencies in generation quality due to the lack of sufficient multimodal interaction modeling. Therefore, we propose a non-autoregressive framework based on Diffusion model for Video Captioning (DiffVC) to address these issues. Its parallel decoding can effectively solve the problems of generation speed and cumulative error. At the same time, our proposed discriminative conditional Diffusion Model can generate higher-quality textual descriptions. Specifically, we first encode the video into a visual representation. During training, Gaussian noise is added to the textual representation of the ground-truth caption. Then, a new textual representation is generated via the discriminative denoiser with the visual representation as a conditional constraint. Finally, we input the new textual representation into a non-autoregressive language model to generate captions. During inference, we directly sample noise from the Gaussian distribution for generation. Experiments on MSVD, MSR-VTT, and VATEX show that our method can outperform previous non-autoregressive methods and achieve comparable performance to autoregressive methods, e.g., it achieved a maximum improvement of 9.9 on the CIDEr and improvement of 2.6 on the B@4, while having faster generation speed. The source code will be available soon.

---


### 154. [Coordinate-Based Dual-Constrained Autoregressive Motion Generation](https://arxiv.org/abs/2604.08088)

**<font color=#1a73e8>作者：</font>** Kang Ding, Hongsong Wang, Jie Gui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion generation has attracted increasing attention in the research community recently, with potential applications in animation, virtual reality, robotics, and human-computer interaction. Diffusion and autoregressive models are two popular and parallel research directions for text-to-motion generation. However, diffusion models often suffer from error amplification during noise prediction, while autoregressive models exhibit mode collapse due to motion discretization. To address these limitations, we propose a flexible, high-fidelity, and semantically faithful text-to-motion framework, named Coordinate-based Dual-constrained Autoregressive Motion Generation (CDAMD). With motion coordinates as input, CDAMD follows the autoregressive paradigm and leverages diffusion-inspired multi-layer perceptrons to enhance the fidelity of predicted motions. Furthermore, a Dual-Constrained Causal Mask is introduced to guide autoregressive generation, where motion tokens act as priors and are concatenated with textual encodings. Since there is limited work on coordinate-based motion synthesis, we establish new benchmarks for both text-to-motion generation and motion editing. Experimental results demonstrate that our approach achieves state-of-the-art performance in terms of both fidelity and semantic consistency on these benchmarks.

---


### 155. [Quantum Vision Theory Applied to Audio Classification for Deepfake Speech Detection](https://arxiv.org/abs/2604.08104)

**<font color=#1a73e8>作者：</font>** Khalid Zaman, Melike Sah, Anuwat Chaiwongyenc 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose Quantum Vision (QV) theory as a new perspective for deep learning-based audio classification, applied to deepfake speech detection. Inspired by particle-wave duality in quantum physics, QV theory is based on the idea that data can be represented not only in its observable, collapsed form, but also as information waves. In conventional deep learning, models are trained directly on these collapsed representations, such as images. In QV theory, inputs are first transformed into information waves using a QV block, and then fed into deep learning models for classification. QV-based models improve performance in image classification compared to their non-QV counterparts. What if QV theory is applied speech spectrograms for audio classification tasks? This is the motivation and novelty of the proposed approach. In this work, Short-Time Fourier Transform (STFT), Mel-spectrograms, and Mel-Frequency Cepstral Coefficients (MFCC) of speech signals are converted into information waves using the proposed QV block and used to train QV-based Convolutional Neural Networks (QV-CNN) and QV-based Vision Transformers (QV-ViT). Extensive experiments are conducted on the ASVSpoof dataset for deepfake speech classification. The results show that QV-CNN and QV-ViT consistently outperform standard CNN and ViT models, achieving higher classification accuracy and improved robustness in distinguishing genuine and spoofed speech. Moreover, the QV-CNN model using MFCC features achieves the best overall performance on the ASVspoof dataset, with an accuracy of 94.20% and an EER of 9.04%, while the QV-CNN with Mel-spectrograms attains the highest accuracy of 94.57%. These findings demonstrate that QV theory is an effective and promising approach for audio deepfake detection and opens new directions for quantum-inspired learning in audio perception tasks.

---


### 156. [EPIR: An Efficient Patch Tokenization, Integration and Representation Framework for Micro-expression Recognition](https://arxiv.org/abs/2604.08106)

**<font color=#1a73e8>作者：</font>** Junbo Wang, Liangyu Fu, Yuke Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-expression recognition can obtain the real emotion of the individual at the current moment. Although deep learning-based methods, especially Transformer-based methods, have achieved impressive results, these methods have high computational complexity due to the large number of tokens in the multi-head self-attention. In addition, the existing micro-expression datasets are small-scale, which makes it difficult for Transformer-based models to learn effective micro-expression representations. Therefore, we propose a novel Efficient Patch tokenization, Integration and Representation framework (EPIR), which can balance high recognition performance and low computational complexity. Specifically, we first propose a dual norm shifted tokenization (DNSPT) module to learn the spatial relationship between neighboring pixels in the face region, which is implemented by a refined spatial transformation and dual norm projection. Then, we propose a token integration module to integrate partial tokens among multiple cascaded Transformer blocks, thereby reducing the number of tokens without information loss. Furthermore, we design a discriminative token extractor, which first improves the attention in the Transformer block to reduce the unnecessary focus of the attention calculation on self-tokens, and uses the dynamic token selection module (DTSM) to select key tokens, thereby capturing more discriminative micro-expression representations. We conduct extensive experiments on four popular public datasets (i.e., CASME II, SAMM, SMIC, and CAS(ME)3. The experimental results show that our method achieves significant performance gains over the state-of-the-art methods, such as 9.6% improvement on the CAS(ME)$^3$ dataset in terms of UF1 and 4.58% improvement on the SMIC dataset in terms of UAR metric.

---


### 157. [OV-Stitcher: A Global Context-Aware Framework for Training-Free Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2604.08110)

**<font color=#1a73e8>作者：</font>** Seungjae Moon, Seunghyun Oh, Youngmin Ro  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free open-vocabulary semantic segmentation(TF-OVSS) has recently attracted attention for its ability to perform dense prediction by leveraging the pretrained knowledge of large vision and vision-language models, without requiring additional training. However, due to the limited input resolution of these pretrained encoders, existing TF-OVSS methods commonly adopt a sliding-window strategy that processes cropped sub-images independently. While effective for managing high-resolution inputs, this approach prevents global attention over the full image, leading to fragmented feature representations and limited contextual reasoning. We propose OV-Stitcher, a training-free framework that addresses this limitation by stitching fragmented sub-image features directly within the final encoder block. By reconstructing attention representations from fragmented sub-image features, OV-Stitcher enables global attention within the final encoder block, producing coherent context aggregation and spatially consistent, semantically aligned segmentation maps. Extensive evaluations across eight benchmarks demonstrate that OV-Stitcher establishes a scalable and effective solution for open-vocabulary segmentation, achieving a notable improvement in mean Intersection over Union(mIoU) from 48.7 to 50.7 compared with prior training-free baselines.

---


### 158. [Bias Redistribution in Visual Machine Unlearning: Does Forgetting One Group Harm Another?](https://arxiv.org/abs/2604.08111)

**<font color=#1a73e8>作者：</font>** Yunusa Haruna, Adamu Lawan, Ibrahim Haruna Abdulhamid 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning enables models to selectively forget training data, driven by privacy regulations such as GDPR and CCPA. However, its fairness implications remain underexplored: when a model forgets a demographic group, does it neutralize that concept or redistribute it to correlated groups, potentially amplifying bias? We investigate this bias redistribution phenomenon on CelebA using CLIP models (ViT/B-32, ViT-L/14, ViT-B/16) under a zero-shot classification setting across intersectional groups defined by age and gender. We evaluate three unlearning methods, Prompt Erasure, Prompt Reweighting, and Refusal Vector using per-group accuracy shifts, demographic parity gaps, and a redistribution score. Our results show that unlearning does not eliminate bias but redistributes it primarily along gender rather than age boundaries. In particular, removing the dominant Young Female group consistently transfers performance to Old Female across all model scales, revealing a gender-dominant structure in CLIP's embedding space. While the Refusal Vector method reduces redistribution, it fails to achieve complete forgetting and significantly degrades retained performance. These findings highlight a fundamental limitation of current unlearning methods: without accounting for embedding geometry, they risk amplifying bias in retained groups.

---


### 159. [TADP-RME: A Trust-Adaptive Differential Privacy Framework for Enhancing Reliability of Data-Driven Systems](https://arxiv.org/abs/2604.08113)

**<font color=#1a73e8>作者：</font>** Labani Halder, Payel Sadhukhan, Sarbani Palit  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ensuring reliability in adversarial settings necessitates treating privacy as a foundational component of data-driven systems. While differential privacy and cryptographic protocols offer strong guarantees, existing schemes rely on a fixed privacy budget, leading to a rigid utility-privacy trade-off that fails under heterogeneous user trust. Moreover, noise-only differential privacy preserves geometric structure, which inference attacks exploit, causing privacy leakage.
We propose TADP-RME (Trust-Adaptive Differential Privacy with Reverse Manifold Embedding), a framework that enhances reliability under varying levels of user trust. It introduces an inverse trust score in the range [0,1] to adaptively modulate the privacy budget, enabling smooth transitions between utility and privacy. Additionally, Reverse Manifold Embedding applies a nonlinear transformation to disrupt local geometric relationships while preserving formal differential privacy guarantees through post-processing.
Theoretical and empirical results demonstrate improved privacy-utility trade-offs, reducing attack success rates by up to 3.1 percent without significant utility degradation. The framework consistently outperforms existing methods against inference attacks, providing a unified approach for reliable learning in adversarial environments.

---


### 160. [StoryEcho: A Generative Child-as-Actor Storytelling System for Picky-Eating Intervention](https://arxiv.org/abs/2604.08114)

**<font color=#1a73e8>作者：</font>** Yanuo Zhou, Jun Fang, Yuntao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Picky eating in children can undermine dietary diversity and the development of healthy eating habits, while also creating recurring tension in family feeding routines. Prior interventions have explored food-centered designs, enhanced utensils, and mealtime interactive systems, but few position children as active participants in intervention processes that extend beyond single mealtime interactions. To better understand everyday responses to picky eating and child-acceptable intervention mechanisms, we conducted a formative study with caregivers and kindergarten teachers. Based on the resulting design considerations and iterative stakeholder review, we designed StoryEcho, a generative child-as-actor storytelling system for picky eating intervention. StoryEcho engages children outside mealtimes through personalized stories in which the child appears as a persistent story character and later shapes story development through real-world food-related behavior. The system combines non-mealtime story engagement, lightweight post-meal feedback, and behavior-informed story updates to support repeated intervention across everyday family routines. We evaluated StoryEcho in a between-group field study with 11 families of preschool children. Results provide preliminary evidence that StoryEcho can significantly increase children's willingness to approach and try target low-preference foods while reducing parental pressure around feeding. These findings suggest the promise of generative child-as-actor storytelling as a design approach for home-based behavior support that unfolds through recurring family routines.

---


### 161. [Revise: A Framework for Revising OCRed text in Practical Information Systems with Data Contamination Strategy](https://arxiv.org/abs/2604.08115)

**<font color=#1a73e8>作者：</font>** Gyuho Shim, Seongtae Hong, Heuiseok Lim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have significantly improved the field of Document AI, demonstrating remarkable performance on document understanding tasks such as question answering. However, existing approaches primarily focus on solving specific tasks, lacking the capability to structurally organize and manage document information. To address this limitation, we propose Revise, a framework that systematically corrects errors introduced by OCR at the character, word, and structural levels. Specifically, Revise employs a comprehensive hierarchical taxonomy of common OCR errors and a synthetic data generation strategy that realistically simulates such errors to train an effective correction model. Experimental results demonstrate that Revise effectively corrects OCR outputs, enabling more structured representation and systematic management of document contents. Consequently, our method significantly enhances downstream performance in document retrieval and question answering tasks, highlighting the potential to overcome the structural management limitations of existing Document AI frameworks.

---


### 162. [Graph Neural Networks for Misinformation Detection: Performance-Efficiency Trade-offs](https://arxiv.org/abs/2604.08131)

**<font color=#1a73e8>作者：</font>** Soveatin Kuntur, Maciej Krzywda, Anna Wróblewska 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid spread of online misinformation has led to increasingly complex detection models, including large language models and hybrid architectures. However, their computational cost and deployment limitations raise concerns about practical applicability. In this work, we benchmark graph neural networks (GNNs) against non-graph-based machine learning methods under controlled and comparable conditions. We evaluate lightweight GNN architectures (GCN, GraphSAGE, GAT, ChebNet) against Logistic Regression, Support Vector Machines, and Multilayer Perceptrons across seven public datasets in English, Indonesian, and Polish. All models use identical TF-IDF features to isolate the impact of relational structure. Performance is measured using F1 score, with inference time reported to assess efficiency. GNNs consistently outperform non-graph baselines across all datasets. For example, GraphSAGE achieves 96.8% F1 on Kaggle and 91.9% on WELFake, compared to 73.2% and 66.8% for MLP, respectively. On COVID-19, GraphSAGE reaches 90.5% F1 vs. 74.9%, while ChebNet attains 79.1% vs. 66.4% on FakeNewsNet. These gains are achieved with comparable or lower inference times. Overall, the results show that classic GNNs remain effective and efficient, challenging the need for increasingly complex architectures in misinformation detection.

---


### 163. [Bag of Bags: Adaptive Visual Vocabularies for Genizah Join Image Retrieval](https://arxiv.org/abs/2604.08138)

**<font color=#1a73e8>作者：</font>** Sharva Gogawale, Gal Grudka, Daria Vasyutinsky-Shapira 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A join is a set of manuscript fragments identified as originally emanating from the same manuscript. We study manuscript join retrieval: Given a query image of a fragment, retrieve other fragments originating from the same physical manuscript. We propose Bag of Bags (BoB), an image-level representation that replaces the global-level visual codebook of classical Bag of Words (BoW) with a fragment-specific vocabulary of local visual words. Our pipeline trains a sparse convolutional autoencoder on binarized fragment patches, encodes connected components from each page, clusters the resulting embeddings with per image $k$-means, and compares images using set to set distances between their local vocabularies. Evaluated on fragments from the Cairo Genizah, the best BoB variant (viz.\@ Chamfer) achieves Hit@1 of 0.78 and MRR of 0.84, compared to 0.74 and 0.80, respectively, for the strongest BoW baseline (BoW-RawPatches-$\chi^2$), a 6.1\% relative improvement in top-1 accuracy. We furthermore study a mass-weighted BoB-OT variant that incorporates cluster population into prototype matching and present a formal approximation guarantee bounding its deviation from full component-level optimal transport. A two-stage pipeline using a BoW shortlist followed by BoB-OT reranking provides a practical compromise between retrieval strength and computational cost, supporting applicability to larger manuscript collections.

---


### 164. [Clickbait detection: quick inference with maximum impact](https://arxiv.org/abs/2604.08148)

**<font color=#1a73e8>作者：</font>** Soveatin Kuntur, Panggih Kusuma Ningrum, Anna Wróblewska 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a lightweight hybrid approach to clickbait detection that combines OpenAI semantic embeddings with six compact heuristic features capturing stylistic and informational cues. To improve efficiency, embeddings are reduced using PCA and evaluated with XGBoost, GraphSAGE, and GCN classifiers. While the simplified feature design yields slightly lower F1-scores, graph-based models achieve competitive performance with substantially reduced inference time. High ROC--AUC values further indicate strong discrimination capability, supporting reliable detection of clickbait headlines under varying decision thresholds.

---


### 165. [A Direct Approach for Handling Contextual Bandits with Latent State Dynamics](https://arxiv.org/abs/2604.08149)

**<font color=#1a73e8>作者：</font>** Zhen Li, Gilles Stoltz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We revisit the finite-armed linear bandit model by Nelson et al. (2022), where contexts and rewards are governed by a finite hidden Markov chain. Nelson et al. (2022) approach this model by a reduction to linear contextual bandits; but to do so, they actually introduce a simplification in which rewards are linear functions of the posterior probabilities over the hidden states given the observed contexts, rather than functions of the hidden states themselves. Their analysis (but not their algorithm) also does not take into account the estimation of the HMM parameters, and only tackles expected, not high-probability, bounds, which suffer in addition from unnecessary complex dependencies on the model (like reward gaps). We instead study the more natural model incorporating direct dependencies in the hidden states (on top of dependencies on the observed contexts, as is natural for contextual bandits) and also obtain stronger, high-probability, regret bounds for a fully adaptive strategy that estimates HMM parameters online. These bounds do not depend on the reward functions and only depend on the model through the estimation of the HMM parameters.

---


### 166. [Training Data Size Sensitivity in Unsupervised Rhyme Recognition](https://arxiv.org/abs/2604.08156)

**<font color=#1a73e8>作者：</font>** Petr Plecháč, Artjoms Šeļa, Silvie Cinková 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rhyme is deceptively intuitive: what is or is not a rhyme is constructed historically, scholars struggle with rhyme classification, and people disagree on whether two words are rhymed or not. This complicates automated rhymed recognition and evaluation, especially in multilingual context. This article investigates how much training data is needed for reliable unsupervised rhyme recognition using RhymeTagger, a language-independent tool that identifies rhymes based on repeating patterns in poetry corpora. We evaluate its performance across seven languages (Czech, German, English, French, Italian, Russian, and Slovene), examining how training size and language differences affect accuracy. To set a realistic performance benchmark, we assess inter-annotator agreement on a manually annotated subset of poems and analyze factors contributing to disagreement in expert annotations: phonetic similarity between rhyming words and their distance from each other in a poem. We also compare RhymeTagger to three large language models using a one-shot learning strategy. Our findings show that, once provided with sufficient training data, RhymeTagger consistently outperforms human agreement, while LLMs lacking phonetic representation significantly struggle with the task.

---


### 167. [State-Flow Coordinated Representation for MI-EEG Decoding](https://arxiv.org/abs/2604.08157)

**<font color=#1a73e8>作者：</font>** Guoqing Cai, Shoulin Huang, Ting Ma  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Motor Imagery (MI) Electroencephalography (EEG) signals contain two crucial and complementary types of information: state information, which captures the global context of the task, and flow information, which captures fine-grained temporal dynamics. However, existing deep decoding models typically focus on only one of these information streams, resulting in unstable learning and sub-optimal performance. To address this, we propose the State-Flow Coordinated Network (StaFlowNet), a novel architecture that explicitly separates and coordinates state and flow information. We first employ a dual-branch design to extract the global state vector and temporal flow features separately. Critically, a novel state-modulated flow module is proposed to dynamically refine the learning of flow information. This modulated mechanism effectively integrates global context with fine-grained dynamics, thereby significantly enhancing task discriminability and decoding performance. Experiments on three public MI-EEG datasets demonstrate that StaFlowNet significantly outperforms state-of-the-art methods. Ablation studies further confirm that the state-modulated mechanism plays a crucial role in enhancing feature discriminability and overall performance.

---


### 168. [Face-D(^2)CL: Multi-Domain Synergistic Representation with Dual Continual Learning for Facial DeepFake Detection](https://arxiv.org/abs/2604.08159)

**<font color=#1a73e8>作者：</font>** Yushuo Zhang, Yu Cheng, Yongkang Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of facial forgery techniques poses severe threats to public trust and information security, making facial DeepFake detection a critical research priority. Continual learning provides an effective approach to adapt facial DeepFake detection models to evolving forgery patterns. However, existing methods face two key bottlenecks in real-world continual learning scenarios: insufficient feature representation and catastrophic forgetting. To address these issues, we propose Face-D(^2)CL, a framework for facial DeepFake detection. It leverages multi-domain synergistic representation to fuse spatial and frequency-domain features for the comprehensive capture of diverse forgery traces, and employs a dual continual learning mechanism that combines Elastic Weight Consolidation (EWC), which distinguishes parameter importance for real versus fake samples, and Orthogonal Gradient Constraint (OGC), which ensures updates to task-specific adapters do not interfere with previously learned knowledge. This synergy enables the model to achieve a dynamic balance between robust anti-forgetting capabilities and agile adaptability to emerging facial forgery paradigms, all without relying on historical data replay. Extensive experiments demonstrate that our method surpasses current SOTA approaches in both stability and plasticity, achieving 60.7% relative reduction in average detection error rate, respectively. On unseen forgery domains, it further improves the average detection AUC by 7.9% compared to the current SOTA method.

---


### 169. [Shift- and stretch-invariant non-negative matrix factorization with an application to brain tissue delineation in emission tomography data](https://arxiv.org/abs/2604.08161)

**<font color=#1a73e8>作者：</font>** Anders S. Olsen, Miriam L. Navarro, Claus Svarer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic neuroimaging data, such as emission tomography measurements of radiotracer transport in blood or cerebrospinal fluid, often exhibit diffusion-like properties. These introduce distance-dependent temporal delays, scale-differences, and stretching effects that limit the effectiveness of conventional linear modeling and decomposition methods. To address this, we present the shift- and stretch-invariant non-negative matrix factorization framework. Our approach estimates both integer and non-integer temporal shifts as well as temporal stretching, all implemented in the frequency domain, where shifts correspond to phase modifications, and where stretching is handled via zero-padding or truncation. The model is implemented in PyTorch (this https URL). We demonstrate on synthetic data and brain emission tomography data that the model is able to account for stretching to provide more detailed characterization of brain tissue structure.

---


### 170. [T-Gated Adapter: A Lightweight Temporal Adapter for Vision-Language Medical Segmentation](https://arxiv.org/abs/2604.08167)

**<font color=#1a73e8>作者：</font>** Pranjal Khadka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation traditionally relies on fully supervised 3D architectures that demand a large amount of dense, voxel-level annotations from clinical experts which is a prohibitively expensive process. Vision Language Models (VLMs) offer a powerful alternative by leveraging broad visual semantic representations learned from billions of images. However, when applied independently to 2D slices of a 3D scan, these models often produce noisy and anatomically implausible segmentations that violate the inherent continuity of anatomical structures. We propose a temporal adapter that addresses this by injecting adjacent-slice context directly into the model's visual token representations. The adapter comprises a temporal transformer attending across a fixed context window at the token level, a spatial context block refining within-slice representations, and an adaptive gate balancing temporal and single-slice features. Training on 30 labeled volumes from the FLARE22 dataset, our method achieves a mean Dice of 0.704 across 13 abdominal organs with a gain of +0.206 over the baseline VLM trained with no temporal context. Zero-shot evaluation on BTCV and AMOS22 datasets yields consistent improvements of +0.210 and +0.230, with the average cross-domain performance drop reducing from 38.0% to 24.9%. Furthermore, in a cross-modality evaluation on AMOS22 MRI with neither model receiving any MRI supervision, our method achieves a mean Dice of 0.366, outperforming a fully supervised 3D baseline (DynUNet, 0.224) trained exclusively on CT, suggesting that CLIP's visual semantic representations generalize more gracefully across imaging modalities than convolutional features.

---


### 171. [Value-Guidance MeanFlow for Offline Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2604.08174)

**<font color=#1a73e8>作者：</font>** Teng Pang, Zhiqiang Dong, Yan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline multi-agent reinforcement learning (MARL) aims to learn the optimal joint policy from pre-collected datasets, requiring a trade-off between maximizing global returns and mitigating distribution shift from offline data. Recent studies use diffusion or flow generative models to capture complex joint policy behaviors among agents; however, they typically rely on multi-step iterative sampling, thereby reducing training and inference efficiency. Although further research improves sampling efficiency through methods like distillation, it remains sensitive to the behavior regularization coefficient. To address the above-mentioned issues, we propose Value Guidance Multi-agent MeanFlow Policy (VGM$^2$P), a simple yet effective flow-based policy learning framework that enables efficient action generation with coefficient-insensitive conditional behavior cloning. Specifically, VGM$^2$P uses global advantage values to guide agent collaboration, treating optimal policy learning as conditional behavior cloning. Additionally, to improve policy expressiveness and inference efficiency in multi-agent scenarios, it leverages classifier-free guidance MeanFlow for both policy training and execution. Experiments on tasks with both discrete and continuous action spaces demonstrate that, even when trained solely via conditional behavior cloning, VGM$^2$P efficiently achieves performance comparable to state-of-the-art methods.

---


### 172. [Long-Term Embeddings for Balanced Personalization](https://arxiv.org/abs/2604.08181)

**<font color=#1a73e8>作者：</font>** Andrii Dzhoha, Egor Malykh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern transformer-based sequential recommenders excel at capturing short-term intent but often suffer from recency bias, overlooking stable long-term preferences. While extending sequence lengths is an intuitive fix, it is computationally inefficient, and recent interactions tend to dominate the model's attention. We propose Long-Term Embeddings (LTE) as a high-inertia contextual anchor to bridge this gap. We address a critical production challenge: the point-in-time consistency problem caused by infrastructure constraints, as feature stores typically host only a single "live" version of features. This leads to an offline-online mismatch during model deployments and rollbacks, as models are forced to process evolved representations they never saw during training. To resolve this, we introduce an LTE framework that constrains embeddings to a fixed semantic basis of content-based item representations, ensuring cross-version compatibility. Furthermore, we investigate integration strategies for causal language modeling, considering the data leakage issue that occurs when the LTE and the transformer's short-term sequence share a temporal horizon. We evaluate two representations: a heuristic average and an asymmetric autoencoder with a fixed decoder grounded in the semantic basis to enable behavioral fine-tuning while maintaining stability. Online A/B tests on Zalando demonstrate that integrating LTE as a contextual prefix token using a lagged window yields significant uplifts in both user engagement and financial metrics.

---


### 173. [Equivariant Efficient Joint Discrete and Continuous MeanFlow for Molecular Graph Generation](https://arxiv.org/abs/2604.08189)

**<font color=#1a73e8>作者：</font>** Rongjian Xu, Teng Pang, Zhiqiang Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-structured data jointly contain discrete topology and continuous geometry, which poses fundamental challenges for generative modeling due to heterogeneous distributions, incompatible noise dynamics, and the need for equivariant inductive biases. Existing flow-matching approaches for graph generation typically decouple structure from geometry, lack synchronized cross-domain dynamics, and rely on iterative sampling, often resulting in physically inconsistent molecular conformations and slow sampling. To address these limitations, we propose Equivariant MeanFlow (EQUIMF), a unified SE(3)-equivariant generative framework that jointly models discrete and continuous components through synchronized MeanFlow dynamics. EQUIMF introduces a unified time bridge and average-velocity updates with mutual conditioning between structure and geometry, enabling efficient few-step generation while preserving physical consistency. Moreover, we develop a novel discrete MeanFlow formulation with a simple yet effective parameterization to support efficient generation over discrete graph structures. Extensive experiments demonstrate that EQUIMF consistently outperforms prior diffusion and flow-matching methods in generation quality, physical validity, and sampling efficiency.

---


### 174. [Inside-Out: Measuring Generalization in Vision Transformers Through Inner Workings](https://arxiv.org/abs/2604.08192)

**<font color=#1a73e8>作者：</font>** Yunxiang Peng, Mengmeng Ma, Ziyu Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable generalization metrics are fundamental to the evaluation of machine learning models. Especially in high-stakes applications where labeled target data are scarce, evaluation of models' generalization performance under distribution shift is a pressing need. We focus on two practical scenarios: (1) Before deployment, how to select the best model for unlabeled target data? (2) After deployment, how to monitor model performance under distribution shift? The central need in both cases is a reliable and label-free proxy metric. Yet existing proxy metrics, such as model confidence or accuracy-on-the-line, are often unreliable as they only assess model output while ignoring the internal mechanisms that produce them. We address this limitation by introducing a new perspective: using the inner workings of a model, i.e., circuits, as a predictive metric of generalization performance. Leveraging circuit discovery, we extract the causal interactions between internal representations as a circuit, from which we derive two metrics tailored to the two practical scenarios. (1) Before deployment, we introduce Dependency Depth Bias, which measures different models' generalization capability on target data. (2) After deployment, we propose Circuit Shift Score, which predicts a model's generalization under different distribution shifts. Across various tasks, both metrics demonstrate significantly improved correlation with generalization performance, outperforming existing proxies by an average of 13.4\% and 34.1\%, respectively. Our code is available at this https URL.

---


### 175. [Approximation of the Basset force in the Maxey-Riley-Gatignol equations via universal differential equations](https://arxiv.org/abs/2604.08194)

**<font color=#1a73e8>作者：</font>** Finn Sommer, Vamika Rathi, Sebastian Goetschel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Maxey-Riley-Gatignol equations (MaRGE) model the motion of spherical inertial particles in a fluid. They contain the Basset force, an integral term which models history effects due to the formation of wakes and boundary layer effects. This causes the force that acts on a particle to depend on its past trajectory and complicates the numerical solution of MaRGE. Therefore, the Basset force is often neglected, despite substantial evidence that it has both quantitative and qualitative impact on the movement patterns of modelled particles. Using the concept of universal differential equations, we propose an approximation of the history term via neural networks which approximates MaRGE by a system of ordinary differential equations that can be solved with standard numerical solvers like Runge-Kutta methods.

---


### 176. [Introducing Echo Networks for Computational Neuroevolution](https://arxiv.org/abs/2604.08204)

**<font color=#1a73e8>作者：</font>** Christian Kroos, Fabian Küch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For applications on the extreme edge, minimal networks of only a few dozen artificial neurons for event detection and classification in discrete time signals would be highly desirable. Feed-forward networks, RNNs, and CNNs evolved through evolutionary algorithms can all be successful in this respect but pose the problem of allowing little systematicity in mutation and recombination if the standard direct genetic encoding of the weights is used (as for instance in the classic NEAT algorithm). We therefore introduce Echo Networks, a type of recurrent network that consists of the connection matrix only, with the source neurons of the synapses represented as rows, destination neurons as columns and weights as entries. There are no layers, and connections between neurons can be bidirectional but are technically all recurrent. Input and output can be arbitrarily assigned to any of the neurons and only use an additional (optional) function in their computational path, e.g., a sigmoid to obtain a binary classification output. We evaluated Echo Networks successfully on the classification of electrocardiography signals but see the most promising potential in their genome representation as a single matrix, allowing matrix computations and factorisations as mutation and recombination operators.

---


### 177. [OmniJigsaw: Enhancing Omni-Modal Reasoning via Modality-Orchestrated Reordering](https://arxiv.org/abs/2604.08209)

**<font color=#1a73e8>作者：</font>** Yiduo Jia, Muzhi Zhu, Hao Zhong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To extend the reinforcement learning post-training paradigm to omni-modal models for concurrently bolstering video-audio understanding and collaborative reasoning, we propose OmniJigsaw, a generic self-supervised framework built upon a temporal reordering proxy task. Centered on the chronological reconstruction of shuffled audio-visual clips, this paradigm strategically orchestrates visual and auditory signals to compel cross-modal integration through three distinct strategies: Joint Modality Integration, Sample-level Modality Selection, and Clip-level Modality Masking. Recognizing that the efficacy of such proxy tasks is fundamentally tied to puzzle quality, we design a two-stage coarse-to-fine data filtering pipeline, which facilitates the efficient adaptation of OmniJigsaw to massive unannotated omni-modal data. Our analysis reveals a ``bi-modal shortcut phenomenon'' in joint modality integration and demonstrates that fine-grained clip-level modality masking mitigates this issue while outperforming sample-level modality selection. Extensive evaluations on 15 benchmarks show substantial gains in video, audio, and collaborative reasoning, validating OmniJigsaw as a scalable paradigm for self-supervised omni-modal learning.

---


### 178. [SciFigDetect: A Benchmark for AI-Generated Scientific Figure Detection](https://arxiv.org/abs/2604.08211)

**<font color=#1a73e8>作者：</font>** You Hu, Chenzhuo Zhao, Changfa Mo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern multimodal generators can now produce scientific figures at near-publishable quality, creating a new challenge for visual forensics and research integrity. Unlike conventional AI-generated natural images, scientific figures are structured, text-dense, and tightly aligned with scholarly semantics, making them a distinct and difficult detection target. However, existing AI-generated image detection benchmarks and methods are almost entirely developed for open-domain imagery, leaving this setting largely unexplored. We present the first benchmark for AI-generated scientific figure detection. To construct it, we develop an agent-based data pipeline that retrieves licensed source papers, performs multimodal understanding of paper text and figures, builds structured prompts, synthesizes candidate figures, and filters them through a review-driven refinement loop. The resulting benchmark covers multiple figure categories, multiple generation sources and aligned real--synthetic pairs. We benchmark representative detectors under zero-shot, cross-generator, and degraded-image settings. Results show that current methods fail dramatically in zero-shot transfer, exhibit strong generator-specific overfitting, and remain fragile under common post-processing corruptions. These findings reveal a substantial gap between existing AIGI detection capabilities and the emerging distribution of high-quality scientific figures. We hope this benchmark can serve as a foundation for future research on robust and generalizable scientific-figure forensics. The dataset is available at this https URL.

---


### 179. [Generalization Under Scrutiny: Cross-Domain Detection Progresses, Pitfalls, and Persistent Challenges](https://arxiv.org/abs/2604.08230)

**<font color=#1a73e8>作者：</font>** Saniya M.Deshmukh, Kailash A. Hambarde, Hugo Proença  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection models trained on a source domain often exhibit significant performance degradation when deployed in unseen target domains, due to various kinds of variations, such as sensing conditions, environments and data distributions. Hence, regardless the recent breakthrough advances in deep learning-based detection technology, cross-domain object detection (CDOD) remains a critical research area. Moreover, the existing literature remains fragmented, lacking a unified perspective on the structural challenges underlying domain shift and the effectiveness of adaptation strategies. This survey provides a comprehensive and systematic analysis of CDOD. We start upon a problem formulation that highlights the multi-stage nature of object detection under domain shift. Then, we organize the existing methods through a conceptual taxonomy that categorizes approaches based on adaptation paradigms, modeling assumptions, and pipeline components. Furthermore, we analyze how domain shift propagates across detection stages and discuss why adaptation in object detection is inherently more complex than in classification. In addition, we review commonly used datasets, evaluation protocols, and benchmarking practices. Finally, we identify the key challenges and outline promising future research directions. Cohesively, this survey aims to provide a unified framework for understanding CDOD and to guide the development of more robust detection systems.

---


### 180. [HiRO-Nav: Hybrid ReasOning Enables Efficient Embodied Navigation](https://arxiv.org/abs/2604.08232)

**<font color=#1a73e8>作者：</font>** He Zhao, Yijun Yang, Zichuan Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied navigation agents built upon large reasoning models (LRMs) can handle complex, multimodal environmental input and perform grounded reasoning per step to improve sequential decision-making for long-horizon tasks. However, a critical question remains: \textit{how can the reasoning capabilities of LRMs be harnessed intelligently and efficiently for long-horizon navigation tasks?} In simple scenes, agents are expected to act reflexively, while in complex ones they should engage in deliberate reasoning before this http URL achieve this, we introduce \textbf{H}ybr\textbf{i}d \textbf{R}eas\textbf{O}ning \textbf{Nav}igation (\textbf{HiRO-Nav}) agent, the first kind of agent capable of adaptively determining whether to perform thinking at every step based on its own action entropy. Specifically, by examining how the agent's action entropy evolves over the navigation trajectories, we observed that only a small fraction of actions exhibit high entropy, and these actions often steer the agent toward novel scenes or critical objects. Furthermore, studying the relationship between action entropy and task completion (i.e., Q-value) reveals that improving high-entropy actions contributes more positively to task this http URL, we propose a tailored training pipeline comprising hybrid supervised fine-tuning as a cold start, followed by online reinforcement learning with the proposed hybrid reasoning strategy to explicitly activate reasoning only for high-entropy actions, significantly reducing computational overhead while improving decision quality. Extensive experiments on the \textsc{CHORES}-$\mathbb{S}$ ObjectNav benchmark showcases that HiRO-Nav achieves a better trade-off between success rates and token efficiency than both dense-thinking and no-thinking baselines.

---


### 181. [$\oslash$ Source Models Leak What They Shouldn't $\nrightarrow$: Unlearning Zero-Shot Transfer in Domain Adaptation Through Adversarial Optimization](https://arxiv.org/abs/2604.08238)

**<font color=#1a73e8>作者：</font>** Arnav Devalapally, Poornima Jain, Kartik Srinivas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The increasing adaptation of vision models across domains, such as satellite imagery and medical scans, has raised an emerging privacy risk: models may inadvertently retain and leak sensitive source-domain specific information in the target domain. This creates a compelling use case for machine unlearning to protect the privacy of sensitive source-domain data. Among adaptation techniques, source-free domain adaptation (SFDA) calls for an urgent need for machine unlearning (MU), where the source data itself is protected, yet the source model exposed during adaptation encodes its influence. Our experiments reveal that existing SFDA methods exhibit strong zero-shot performance on source-exclusive classes in the target domain, indicating they inadvertently leak knowledge of these classes into the target domain, even when they are not represented in the target data. We identify and address this risk by proposing an MU setting called SCADA-UL: Unlearning Source-exclusive ClAsses in Domain Adaptation. Existing MU methods do not address this setting as they are not designed to handle data distribution shifts. We propose a new unlearning method, where an adversarially generated forget class sample is unlearned by the model during the domain adaptation process using a novel rescaled labeling strategy and adversarial optimization. We also extend our study to two variants: a continual version of this problem setting and to one where the specific source classes to be forgotten may be unknown. Alongside theoretical interpretations, our comprehensive empirical results show that our method consistently outperforms baselines in the proposed setting while achieving retraining-level unlearning performance on benchmark datasets. Our code is available at this https URL

---


### 182. [From Phenomenological Fitting to Endogenous Deduction: A Paradigm Leap via Meta-Principle Physics Architecture](https://arxiv.org/abs/2604.08245)

**<font color=#1a73e8>作者：</font>** Helong Hu, HongDan Pan, ShuiQing Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The essence of current neural network architectures is phenomenological fitting: they learn input-output statistical correlations via massive parameters and data, yet lack intrinsic understanding of the fundamental principles governing physical reality. This paper proposes a paradigm leap from pure phenomenological fitting to the fusion of phenomenological fitting and endogenous deduction. By embedding physical meta-principles into neural network architecture, we construct the Meta-Principle Physics Architecture (MPPA).
Specifically, MPPA embeds three core meta-principles - Connectivity, Conservation, Periodicity - into its architecture, implemented via three core components: the Gravitator realizes Connectivity via standard causal attention; the Energy Encoder implements Conservation via log-domain energy tracking and delayed compensation; the Periodicity Encoder fulfills Periodicity via FFT-based spectral analysis and delayed modulation. These components collaborate via a learnable independent gating fusion mechanism, forming a complete physical cognition framework of 'local relational connectivity - global conservation constraint - evolutionary periodic law'.
Experiments show MPPA achieves significant improvements: physical reasoning (from near zero to 0.436, 0.436 vs 0.000), 2.18x mathematical task improvement (0.330 vs 0.151), 52% logical task gain (0.456 vs 0.300), and 3.69% lower validation perplexity (259.45 vs 269.40), with only 11.8% more parameters (242.40M vs 216.91M). Notably, MPPA shows strong generalization on out-of-distribution physical scenarios, proving the robustness and interpretability of this principle-embedded design. This work establishes a new theoretical foundation and technical path for next-generation AI with physical common sense, causal reasoning, and mathematical rigor.

---


### 183. [HyperMem: Hypergraph Memory for Long-Term Conversations](https://arxiv.org/abs/2604.08256)

**<font color=#1a73e8>作者：</font>** Juwei Yue, Chuanrui Hu, Jiawei Sheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for conversational agents to maintain coherence, track persistent tasks, and provide personalized interactions across extended dialogues. However, existing approaches as Retrieval-Augmented Generation (RAG) and graph-based memory mostly rely on pairwise relations, which can hardly capture high-order associations, i.e., joint dependencies among multiple elements, causing fragmented retrieval. To this end, we propose HyperMem, a hypergraph-based hierarchical memory architecture that explicitly models such associations using hyperedges. Particularly, HyperMem structures memory into three levels: topics, episodes, and facts, and groups related episodes and their facts via hyperedges, unifying scattered content into coherent units. Leveraging this structure, we design a hybrid lexical-semantic index and a coarse-to-fine retrieval strategy, supporting accurate and efficient retrieval of high-order associations. Experiments on the LoCoMo benchmark show that HyperMem achieves state-of-the-art performance with 92.73% LLM-as-a-judge accuracy, demonstrating the effectiveness of HyperMem for long-term conversations.

---


### 184. [Behavior-Aware Item Modeling via Dynamic Procedural Solution Representations for Knowledge Tracing](https://arxiv.org/abs/2604.08260)

**<font color=#1a73e8>作者：</font>** Jun Seo, Sangwon Ryu, Heejin Do 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge Tracing (KT) aims to predict learners' future performance from past interactions. While recent KT approaches have improved via learning item representations aligned with Knowledge Components, they overlook the procedural dynamics of problem solving. We propose Behavior-Aware Item Modeling (BAIM), a framework that enriches item representations by integrating dynamic procedural solution information. BAIM leverages a reasoning language model to decompose each item's solution into four problem-solving stages (i.e., understand, plan, carry out, and look back), pedagogically grounded in Polya's framework. Specifically, it derives stage-level representations from per-stage embedding trajectories, capturing latent signals beyond surface features. To reflect learner heterogeneity, BAIM adaptively routes these stage-wise representations, introducing a context-conditioned mechanism within a KT backbone, allowing different procedural stages to be emphasized for different learners. Experiments on XES3G5M and NIPS34 show that BAIM consistently outperforms strong pretraining-based baselines, achieving particularly large gains under repeated learner interactions.

---


### 185. [An Illusion of Unlearning? Assessing Machine Unlearning Through Internal Representations](https://arxiv.org/abs/2604.08271)

**<font color=#1a73e8>作者：</font>** Yichen Gao, Altay Unal, Akshay Rangamani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While numerous machine unlearning (MU) methods have recently been developed with promising results in erasing the influence of forgotten data, classes, or concepts, they are also highly vulnerable-for example, simple fine-tuning can inadvertently reintroduce erased concepts. In this paper, we address this contradiction by examining the internal representations of unlearned models, in contrast to prior work that focuses primarily on output-level behavior. Our analysis shows that many state-of-the-art MU methods appear successful mainly due to a misalignment between last-layer features and the classifier, a phenomenon we call feature-classifier misalignment. In fact, hidden features remain highly discriminative, and simple linear probing can recover near-original accuracy. Assuming neural collapse in the original model, we further demonstrate that adjusting only the classifier can achieve negligible forget accuracy while preserving retain accuracy, and we corroborate this with experiments using classifier-only fine-tuning. Motivated by these findings, we propose MU methods based on a class-mean features (CMF) classifier, which explicitly enforces alignment between features and classifiers. Experiments on standard benchmarks show that CMF-based unlearning reduces forgotten information in representations while maintaining high retain accuracy, highlighting the need for faithful representation-level evaluation of MU.

---


### 186. [Preventing Overfitting in Deep Image Prior for Hyperspectral Image Denoising](https://arxiv.org/abs/2604.08272)

**<font color=#1a73e8>作者：</font>** Panagiotis Gkotsis, Athanasios A. Rontogiannis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep image prior (DIP) is an unsupervised deep learning framework that has been successfully applied to a variety of inverse imaging problems. However, DIP-based methods are inherently prone to overfitting, which leads to performance degradation and necessitates early stopping. In this paper, we propose a method to mitigate overfitting in DIP-based hyperspectral image (HSI) denoising by jointly combining robust data fidelity and explicit sensitivity regularization. The proposed approach employs a Smooth $\ell_1$ data term together with a divergence-based regularization and input optimization during training. Experimental results on real HSIs corrupted by Gaussian, sparse, and stripe noise demonstrate that the proposed method effectively prevents overfitting and achieves superior denoising performance compared to state-of-the-art DIP-based HSI denoising methods.

---


### 187. [Floating or Suggesting Ideas? A Large-Scale Contrastive Analysis of Metaphorical and Literal Verb-Object Constructions](https://arxiv.org/abs/2604.08275)

**<font color=#1a73e8>作者：</font>** Prisca Piccirilli, Alexander Fraser, Sabine Schulte im Walde  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metaphor pervades everyday language, allowing speakers to express abstract concepts via concrete domains. While prior work has studied metaphors cognitively and psycholinguistically, large-scale comparisons with literal language remain limited, especially for near-synonymous expressions. We analyze 297 English verb-object pairs (e.g., float idea vs. suggest idea) in ~2M corpus sentences, examining their contextual usage. Using five NLP tools, we extract 2,293 cognitive and linguistic features capturing affective, lexical, syntactic, and discourse-level properties. We address: (i) whether features differ between metaphorical and literal contexts (cross-pair analysis), and (ii) whether individual VO pairs diverge internally (within-pair analysis). Cross-pair results show literal contexts have higher lexical frequency, cohesion, and structural regularity, while metaphorical contexts show greater affective load, imageability, lexical diversity, and constructional specificity. Within-pair analyses reveal substantial heterogeneity, with most pairs showing non-uniform effects. These results suggest no single, consistent distributional pattern that distinguishes metaphorical from literal usage. Instead, differences are largely construction-specific. Overall, large-scale data combined with diverse features provides a fine-grained understanding of metaphor-literal contrasts in VO usage.

---


### 188. [ACF: A Collaborative Framework for Agent Covert Communication under Cognitive Asymmetry](https://arxiv.org/abs/2604.08276)

**<font color=#1a73e8>作者：</font>** Wansheng Wu, Kaibo Huang, Yukun Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As generative artificial intelligence evolves, autonomous agent networks present a powerful paradigm for interactive covert communication. However, because agents dynamically update internal memories via environmental interactions, existing methods face a critical structural vulnerability: cognitive asymmetry. Conventional approaches demand strict cognitive symmetry, requiring identical sequence prefixes between the encoder and decoder. In dynamic deployments, inevitable prefix discrepancies destroy synchronization, inducing severe channel degradation. To address this core challenge of cognitive asymmetry, we propose the Asymmetric Collaborative Framework (ACF), which structurally decouples covert communication from semantic reasoning via orthogonal statistical and cognitive layers. By deploying a prefix-independent decoding paradigm governed by a shared steganographic configuration, ACF eliminates the reliance on cognitive symmetry. Evaluations on realistic memory-augmented workflows demonstrate that under severe cognitive asymmetry, symmetric baselines suffer severe channel degradation, whereas ACF uniquely excels across both semantic fidelity and covert communication. It maintains computational indistinguishability, enabling reliable secret extraction with provable error bounds, and providing robust Effective Information Capacity guarantees for modern agent networks.

---


### 189. [When to Trust Tools? Adaptive Tool Trust Calibration For Tool-Integrated Math Reasoning](https://arxiv.org/abs/2604.08281)

**<font color=#1a73e8>作者：</font>** Ruotao Xu, Yixin Ji, Yu Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) have achieved strong performance enhancement through scaling test time computation, but due to the inherent limitations of the underlying language models, they still have shortcomings in tasks that require precise computation and extensive knowledge reserves. Tool-Integrated Reasoning (TIR) has emerged as a promising paradigm that incorporates tool call and execution within the reasoning trajectory. Although recent works have released some powerful open-source TIR models, our analysis reveals that these models still suffer from critical deficiencies. We find that when the reasoning of the model conflicts with the tool results, the model tends to believe in its own reasoning. And there are cases where the tool results are correct but are ignored by the model, resulting in incorrect answers, which we define as "Tool Ignored''. This indicates that the model does not know when to trust or ignore the tool. To overcome these limitations, We introduce Adaptive Tool Trust Calibration (ATTC), a novel framework that guides the model to adaptively choose to trust or ignore the tool results based on the confidence score of generated code blocks. The experimental results from various open-source TIR models of different sizes and across multiple datasets demonstrate that ATTC effectively reduces the "Tool Ignored" issue, resulting in a performance increase of 4.1% to 7.5%.

---


### 190. [Revisiting Radar Perception With Spectral Point Clouds](https://arxiv.org/abs/2604.08282)

**<font color=#1a73e8>作者：</font>** Hamza Alsharif, Jing Gu, Pavol Jancura 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radar perception models are trained with different inputs, from range-Doppler spectra to sparse point clouds. Dense spectra are assumed to outperform sparse point clouds, yet they can vary considerably across sensors and configurations, which hinders transfer. In this paper, we provide alternatives for incorporating spectral information into radar point clouds and show that, point clouds need not underperform compared to spectra. We introduce the spectral point cloud paradigm, where point clouds are treated as sparse, compressed representations of the radar spectra, and argue that, when enriched with spectral information, they serve as strong candidates for a unified input representation that is more robust against sensor-specific differences. We develop an experimental framework that compares spectral point cloud (PC) models at varying densities against a dense range-Doppler (RD) benchmark, and report the density levels where the PC configurations meet the performance of the RD benchmark. Furthermore, we experiment with two basic spectral enrichment approaches, that inject additional target-relevant information into the point clouds. Contrary to the common belief that the dense RD approach is superior, we show that point clouds can do just as well, and can surpass the RD benchmark when enrichment is applied. Spectral point clouds can therefore serve as strong candidates for unified radar perception, paving the way for future radar foundation models.

---


### 191. [CAMotion: A High-Quality Benchmark for Camouflaged Moving Object Detection in the Wild](https://arxiv.org/abs/2604.08287)

**<font color=#1a73e8>作者：</font>** Siyuan Yao, Hao Sun, Ruiqi Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discovering camouflaged objects is a challenging task in computer vision due to the high similarity between camouflaged objects and their surroundings. While the problem of camouflaged object detection over sequential video frames has received increasing attention, the scale and diversity of existing video camouflaged object detection (VCOD) datasets are greatly limited, which hinders the deeper analysis and broader evaluation of recent deep learning-based algorithms with data-hungry training strategy. To break this bottleneck, in this paper, we construct CAMotion, a high-quality benchmark covers a wide range of species for camouflaged moving object detection in the wild. CAMotion comprises various sequences with multiple challenging attributes such as uncertain edge, occlusion, motion blur, and shape complexity, etc. The sequence annotation details and statistical distribution are presented from various perspectives, allowing CAMotion to provide in-depth analyses on the camouflaged object's motion characteristics in different challenging scenarios. Additionally, we conduct a comprehensive evaluation of existing SOTA models on CAMotion, and discuss the major challenges in VCOD task. The benchmark is available at this https URL, we hope that our CAMotion can lead to further advancements in the research community.

---


### 192. [U-CECE: A Universal Multi-Resolution Framework for Conceptual Counterfactual Explanations](https://arxiv.org/abs/2604.08295)

**<font color=#1a73e8>作者：</font>** Angeliki Dimitriou, Nikolaos Chaidos, Maria Lymperaiou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI models grow more complex, explainability is essential for building trust, yet concept-based counterfactual methods still face a trade-off between expressivity and efficiency. Representing underlying concepts as atomic sets is fast but misses relational context, whereas full graph representations are more faithful but require solving the NP-hard Graph Edit Distance (GED) problem. We propose U-CECE, a unified, model-agnostic multi-resolution framework for conceptual counterfactual explanations that adapts to data regime and compute budget. U-CECE spans three levels of expressivity: atomic concepts for broad explanations, relational sets-of-sets for simple interactions, and structural graphs for full semantic structure. At the structural level, both a precision-oriented transductive mode based on supervised Graph Neural Networks (GNNs) and a scalable inductive mode based on unsupervised graph autoencoders (GAEs) are supported. Experiments on the structurally divergent CUB and Visual Genome datasets characterize the efficiency-expressivity trade-off across levels, while human surveys and LVLM-based evaluation show that the retrieved structural counterfactuals are semantically equivalent to, and often preferred over, exact GED-based ground-truth explanations.

---


### 193. [GroundingAnomaly: Spatially-Grounded Diffusion for Few-Shot Anomaly Synthesis](https://arxiv.org/abs/2604.08301)

**<font color=#1a73e8>作者：</font>** Yishen Liu, Hongcang Chen, Pengcheng Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The performance of visual anomaly inspection in industrial quality control is often constrained by the scarcity of real anomalous samples. Consequently, anomaly synthesis techniques have been developed to enlarge training sets and enhance downstream inspection. However, existing methods either suffer from poor integration caused by inpainting or fail to provide accurate masks. To address these limitations, we propose GroundingAnomaly, a novel few-shot anomaly image generation framework. Our framework introduces a Spatial Conditioning Module that leverages per-pixel semantic maps to enable precise spatial control over the synthesized anomalies. Furthermore, a Gated Self-Attention Module is designed to inject conditioning tokens into a frozen U-Net via gated attention layers. This carefully preserves pretrained priors while ensuring stable few-shot adaptation. Extensive evaluations on the MVTec AD and VisA datasets demonstrate that GroundingAnomaly generates high-quality anomalies and achieves state-of-the-art performance across multiple downstream tasks, including anomaly detection, segmentation, and instance-level detection.

---


### 194. [Weakly-Supervised Lung Nodule Segmentation via Training-Free Guidance of 3D Rectified Flow](https://arxiv.org/abs/2604.08313)

**<font color=#1a73e8>作者：</font>** Richard Petersen, Fredrik Kahl, Jennifer Alvén  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense annotations, such as segmentation masks, are expensive and time-consuming to obtain, especially for 3D medical images where expert voxel-wise labeling is required. Weakly supervised approaches aim to address this limitation, but often rely on attribution-based methods that struggle to accurately capture small structures such as lung nodules. In this paper, we propose a weakly-supervised segmentation method for lung nodules by combining pretrained state-of-the-art rectified flow and predictor models in a plug-and-play manner. Our approach uses training-free guidance of a 3D rectified flow model, requiring only fine-tuning of the predictor using image-level labels and no retraining of the generative model. The proposed method produces improved-quality segmentations for two separate predictors, consistently detecting lung nodules of varying size and shapes. Experiments on LUNA16 demonstrate improvements over baseline methods, highlighting the potential of generative foundation models as tools for weakly supervised 3D medical image segmentation.

---


### 195. [InstAP: Instance-Aware Vision-Language Pre-Train for Spatial-Temporal Understanding](https://arxiv.org/abs/2604.08337)

**<font color=#1a73e8>作者：</font>** Ashutosh Kumar, Rajat Saini, Jingjing Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current vision-language pre-training (VLP) paradigms excel at global scene understanding but struggle with instance-level reasoning due to global-only supervision. We introduce InstAP, an Instance-Aware Pre-training framework that jointly optimizes global vision-text alignment and fine-grained, instance-level contrastive alignment by grounding textual mentions to specific spatial-temporal regions. To support this, we present InstVL, a large-scale dataset (2 million images, 50,000 videos) with dual-granularity annotations: holistic scene captions and dense, grounded instance descriptions. On the InstVL benchmark, InstAP substantially outperforms existing VLP models on instance-level retrieval, and also surpasses a strong VLP baseline trained on the exact same data corpus, isolating the benefit of our instance-aware objective. Moreover, instance-centric pre-training improves global understanding: InstAP achieves competitive zero-shot performance on multiple video benchmarks, including MSR-VTT and DiDeMo. Qualitative visualizations further show that InstAP localizes textual mentions to the correct instances, while global-only models exhibit more diffuse, scene-level attention.

---


### 196. [EgoEverything: A Benchmark for Human Behavior Inspired Long Context Egocentric Video Understanding in AR Environment](https://arxiv.org/abs/2604.08342)

**<font color=#1a73e8>作者：</font>** Qiance Tang, Ziqi Wang, Jieyu Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long context egocentric video understanding has recently attracted significant research attention, with augmented reality (AR) highlighted as one of its most important application domains. Nevertheless, the task remains highly challenging due to the need for reasoning over extended temporal contexts and diverse, unstructured activities. Although several benchmarks exist, most egocentric datasets rely on human worn cameras and focus mainly on visual content, with limited consideration of underlying user behavior when forming video-related queries. EgoEverything is a benchmark that explicitly considers human behavior by leveraging human attention signals, abstracted from gaze data, when generating questions. It comprises over 5,000 multiple choice question answer pairs, spanning more than 100 hours of video. By integrating human attention signals during question generation, it more faithfully captures natural human behavior and offers a realistic evaluation setting for long-context egocentric video understanding in AR.

---


### 197. [Human-AI Collaboration Reconfigures Group Regulation from Socially Shared to Hybrid Co-Regulation](https://arxiv.org/abs/2604.08344)

**<font color=#1a73e8>作者：</font>** Yujing Zhang, Xianghui Meng, Shihui Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) is increasingly used in collaborative learning, yet its effects on how groups regulate collaboration remain unclear. Effective collaboration depends not only on what groups discuss, but on how they jointly manage goals, participation, strategy use, monitoring, and repair through co-regulation and socially shared regulation. We compared collaborative regulation between Human-AI and Human-Human groups in a parallel-group randomised experiment with 71 university students completing the same collaborative tasks with GenAI either available or unavailable. Focusing on human discourse, we used statistical analyses to examine differences in the distribution of collaborative regulation across regulatory modes, regulatory processes, and participatory focuses. Results showed that GenAI availability shifted regulation away from predominantly socially shared forms towards more hybrid co-regulatory forms, with selective increases in directive, obstacle-oriented, and affective regulatory processes. Participatory-focus distributions, however, were broadly similar across conditions. These findings suggest that GenAI reshapes the distribution of regulatory responsibility in collaboration and offer implications for the human-centred design of AI-supported collaborative learning.

---


### 198. [ASPECT:Analogical Semantic Policy Execution via Language Conditioned Transfer](https://arxiv.org/abs/2604.08355)

**<font color=#1a73e8>作者：</font>** Ajsal Shereef Palattuparambil, Thommen George Karimpanal, Santu Rana  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) agents often struggle to generalize knowledge to new tasks, even those structurally similar to ones they have mastered. Although recent approaches have attempted to mitigate this issue via zero-shot transfer, they are often constrained by predefined, discrete class systems, limiting their adaptability to novel or compositional task variations. We propose a significantly more generalized approach, replacing discrete latent variables with natural language conditioning via a text-conditioned Variational Autoencoder (VAE). Our core innovation utilizes a Large Language Model (LLM) as a dynamic \textit{semantic operator} at test time. Rather than relying on rigid rules, our agent queries the LLM to semantically remap the description of the current observation to align with the source task. This source-aligned caption conditions the VAE to generate an imagined state compatible with the agent's original training, enabling direct policy reuse. By harnessing the flexible reasoning capabilities of LLMs, our approach achieves zero-shot transfer across a broad spectrum of complex and truly novel analogous tasks, moving beyond the limitations of fixed category mappings. Code and videos are available \href{this https URL}{here}.

---


### 199. [Bias-Constrained Diffusion Schedules for PDE Emulations: Reconstruction Error Minimization and Efficient Unrolled Training](https://arxiv.org/abs/2604.08357)

**<font color=#1a73e8>作者：</font>** Constantin Le Cleï, Nils Thürey, Xiaoxiang Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional Diffusion Models are powerful surrogates for emulating complex spatiotemporal dynamics, yet they often fail to match the accuracy of deterministic neural emulators for high-precision tasks. In this work, we address two critical limitations of autoregressive PDE diffusion models: their sub-optimal single-step accuracy and the prohibitive computational cost of unrolled training. First, we characterize the relationship between the noise schedule, the reconstruction error reduction rate and the diffusion exposure bias, demonstrating that standard schedules lead to suboptimal reconstruction error. Leveraging this insight, we propose an \textit{Adaptive Noise Schedule} framework that minimizes inference reconstruction error by dynamically constraining the model's exposure bias. We further show that this optimized schedule enables a fast \textit{Proxy Unrolled Training} method to stabilize long-term rollouts without the cost of full Markov Chain sampling. Both proposed methods enable significant improvements in short-term accuracy and long-term stability over diffusion and deterministic baselines on diverse benchmarks, including forced Navier-Stokes, Kuramoto-Sivashinsky and Transonic Flow.

---


### 200. [MegaStyle: Constructing Diverse and Scalable Style Dataset via Consistent Text-to-Image Style Mapping](https://arxiv.org/abs/2604.08364)

**<font color=#1a73e8>作者：</font>** Junyao Gao, Sibo Liu, Jiaxing Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce MegaStyle, a novel and scalable data curation pipeline that constructs an intra-style consistent, inter-style diverse and high-quality style dataset. We achieve this by leveraging the consistent text-to-image style mapping capability of current large generative models, which can generate images in the same style from a given style description. Building on this foundation, we curate a diverse and balanced prompt gallery with 170K style prompts and 400K content prompts, and generate a large-scale style dataset MegaStyle-1.4M via content-style prompt combinations. With MegaStyle-1.4M, we propose style-supervised contrastive learning to fine-tune a style encoder MegaStyle-Encoder for extracting expressive, style-specific representations, and we also train a FLUX-based style transfer model MegaStyle-FLUX. Extensive experiments demonstrate the importance of maintaining intra-style consistency, inter-style diversity and high-quality for style dataset, as well as the effectiveness of the proposed MegaStyle-1.4M. Moreover, when trained on MegaStyle-1.4M, MegaStyle-Encoder and MegaStyle-FLUX provide reliable style similarity measurement and generalizable style transfer, making a significant contribution to the style transfer community. More results are available at our project website this https URL.

---


### 201. [Scaling-Aware Data Selection for End-to-End Autonomous Driving Systems](https://arxiv.org/abs/2604.08366)

**<font color=#1a73e8>作者：</font>** Tolga Dimlioglu, Nadine Chang, Maying Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale deep learning models for physical AI applications depend on diverse training data collection efforts. These models and correspondingly, the training data, must address different evaluation criteria necessary for the models to be deployable in real-world environments. Data selection policies can guide the development of the training set, but current frameworks do not account for the ambiguity in how data points affect different metrics. In this work, we propose Mixture Optimization via Scaling-Aware Iterative Collection (MOSAIC), a general data selection framework that operates by: (i) partitioning the dataset into domains; (ii) fitting neural scaling laws from each data domain to the evaluation metrics; and (iii) optimizing a data mixture by iteratively adding data from domains that maximize the change in metrics. We apply MOSAIC to autonomous driving (AD), where an End-to-End (E2E) planner model is evaluated on the Extended Predictive Driver Model Score (EPDMS), an aggregate of driving rule compliance metrics. Here, MOSAIC outperforms a diverse set of baselines on EPDMS with up to 80\% less data.

---


### 202. [SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370)

**<font color=#1a73e8>作者：</font>** Chensheng Dai, Shengjun Zhang, Min Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has demonstrated impressive performance in 3D scene reconstruction. Beyond novel view synthesis, it shows great potential for multi-view surface reconstruction. Existing methods employ optimization-based reconstruction pipelines that achieve precise and complete surface extractions. However, these approaches typically require dense input views and high time consumption for per-scene optimization. To address these limitations, we propose SurfelSplat, a feed-forward framework that generates efficient and generalizable pixel-aligned Gaussian surfel representations from sparse-view images. We observe that conventional feed-forward structures struggle to recover accurate geometric attributes of Gaussian surfels because the spatial frequency of pixel-aligned primitives exceeds Nyquist sampling rates. Therefore, we propose a cross-view feature aggregation module based on the Nyquist sampling theorem. Specifically, we first adapt the geometric forms of Gaussian surfels with spatial sampling rate-guided low-pass filters. We then project the filtered surfels across all input views to obtain cross-view feature correlations. By processing these correlations through a specially designed feature fusion network, we can finally regress Gaussian surfels with precise geometry. Extensive experiments on DTU reconstruction benchmarks demonstrate that our model achieves comparable results with state-of-the-art methods, and predict Gaussian surfels within 1 second, offering a 100x speedup without costly per-scene training.

---


### 203. [Let Me Introduce You: Stimulating Taste-Broadening Serendipity Through Song Introductions](https://arxiv.org/abs/2604.08385)

**<font color=#1a73e8>作者：</font>** Brett Binst, Ulysse Maes, Martijn C. Willemsen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Research on how people experience music emphasizes the importance of exploration and diversity in listening. However, music recommender systems struggle with facilitating exploration. Even when music recommender systems are able to recommend something valuable to users that is outside their typical preferences, it still remains difficult to spark their interest. This paper presents a user study examining the efficacy of immersive and informative introductions in stimulating interest in songs that are beyond one's usual preferences, an experience called Taste-Broadening Serendipity. We uncover two important mechanisms behind the effect of introductions: transportation and cognitive elaboration. Our findings indicate that transportation (i.e., being absorbed into a narrative world) is the strongest predictor of Taste-Broadening Serendipity, while cognitive elaboration (i.e., learning something new about the artist or social context in which the music emerged) has a weaker effect but is easier to stimulate. We propose that song introductions can play an important role in facilitating exploration and increasing diversity of listening on music streaming platforms.

---


### 204. [Zero-shot Multivariate Time Series Forecasting Using Tabular Prior Fitted Networks](https://arxiv.org/abs/2604.08400)

**<font color=#1a73e8>作者：</font>** Mayuka Jayawardhana, Nihal Sharma, Kazem Meidani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models, particularly Prior-data Fitted Networks like TabPFN have emerged as the leading contender in a myriad of tasks ranging from data imputation to label prediction on the tabular data format surpassing the historical successes of tree-based models. This has led to investigations on their applicability to forecasting time series data which can be formulated as a tabular problem. While recent work to this end has displayed positive results, most works have limited their treatment of multivariate time series problems to several independent univariate time series forecasting subproblems, thus ignoring any inter-channel interactions. Overcoming this limitation, we introduce a generally applicable framework for multivariate time series forecasting using tabular foundation models. We achieve this by recasting the multivariate time series forecasting problem as a series of scalar regression problems which can then be solved zero-shot by any tabular foundation model with regression capabilities. We present results of our method using the TabPFN-TS backbone and compare performance with the current state of the art tabular methods.

---


### 205. [Adversarial Label Invariant Graph Data Augmentations for Out-of-Distribution Generalization](https://arxiv.org/abs/2604.08404)

**<font color=#1a73e8>作者：</font>** Simon Zhang, Ryan P. DeMilt, Kun Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OoD) generalization occurs when representation learning encounters a distribution shift. This occurs frequently in practice when training and testing data come from different environments. Covariate shift is a type of distribution shift that occurs only in the input data, while the concept distribution stays invariant. We propose RIA - Regularization for Invariance with Adversarial training, a new method for OoD generalization under convariate shift. Motivated by an analogy to $Q$-learning, it performs an adversarial exploration for training data environments. These new environments are induced by adversarial label invariant data augmentations that prevent a collapse to an in-distribution trained learner. It works with many existing OoD generalization methods for covariate shift that can be formulated as constrained optimization problems. We develop an alternating gradient descent-ascent algorithm to solve the problem, and perform extensive experiments on OoD graph classification for various kinds of synthetic and natural distribution shifts. We demonstrate that our method can achieve high accuracy compared with OoD baselines.

---


### 206. [BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields](https://arxiv.org/abs/2604.08410)

**<font color=#1a73e8>作者：</font>** Fan Yang, Wenrui Chen, Guorun Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In unstructured environments, functional dexterous grasping calls for the tight integration of semantic understanding, precise 3D functional localization, and physically interpretable execution. Modular hierarchical methods are more controllable and interpretable than end-to-end VLA approaches, but existing ones still rely on predefined affordance labels and lack the tight semantic--pose coupling needed for functional dexterous manipulation. To address this, we propose BLaDA (Bridging Language to Dexterous Actions in 3DGS fields), an interpretable zero-shot framework that grounds open-vocabulary instructions as perceptual and control constraints for functional dexterous manipulation. BLaDA establishes an interpretable reasoning chain by first parsing natural language into a structured sextuple of manipulation constraints via a Knowledge-guided Language Parsing (KLP) module. To achieve pose-consistent spatial reasoning, we introduce the Triangular Functional Point Localization (TriLocation) module, which utilizes 3D Gaussian Splatting as a continuous scene representation and identifies functional regions under triangular geometric constraints. Finally, the 3D Keypoint Grasp Matrix Transformation Execution (KGT3D+) module decodes these semantic-geometric constraints into physically plausible wrist poses and finger-level commands. Extensive experiments on complex benchmarks demonstrate that BLaDA significantly outperforms existing methods in both affordance grounding precision and the success rate of functional manipulation across diverse categories and tasks. Code will be publicly available at this https URL.

---


### 207. [Synthetic Data for any Differentiable Target](https://arxiv.org/abs/2604.08423)

**<font color=#1a73e8>作者：</font>** Tristan Thrush, Sung Min Park, Herman Brunborg 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> What are the limits of controlling language models via synthetic training data? We develop a reinforcement learning (RL) primitive, the Dataset Policy Gradient (DPG), which can precisely optimize synthetic data generators to produce a dataset of targeted examples. When used for supervised fine-tuning (SFT) of a target model, these examples cause the target model to do well on a differentiable metric of our choice. Our approach achieves this by taking exact data attribution via higher-order gradients and using those scores as policy gradient rewards. We prove that this procedure closely approximates the true, intractable gradient for the synthetic data generator. To illustrate the potential of DPG, we show that, using only SFT on generated examples, we can cause the target model's LM head weights to (1) embed a QR code, (2) embed the pattern $\texttt{67}$, and (3) have lower $\ell^2$ norm. We additionally show that we can cause the generator to (4) rephrase inputs in a new language and (5) produce a specific UUID, even though neither of these objectives is conveyed in the generator's input prompts. These findings suggest that DPG is a powerful and flexible technique for shaping model properties using only synthetic training examples.

---


### 208. [On-board Telemetry Monitoring in Autonomous Satellites: Challenges and Opportunities](https://arxiv.org/abs/2604.08424)

**<font color=#1a73e8>作者：</font>** Lorenzo Capelli, Leandro de Souza Rosa, Maurizio De Tommasi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The increasing autonomy of spacecraft demands fault-detection systems that are both reliable and explainable. This work addresses eXplainable Artificial Intelligence for onboard Fault Detection, Isolation and Recovery within the Attitude and Orbit Control Subsystem by introducing a framework that enhances interpretability in neural anomaly detectors. We propose a method to derive low-dimensional, semantically annotated encodings from intermediate neural activations, called peepholes. Applied to a convolutional autoencoder, the framework produces interpretable indicators that enable the identification and localization of anomalies in reaction-wheel telemetry. Peepholes analysis further reveals bias detection and supports fault localization. The proposed framework enables the semantic characterization of detected anomalies while requiring only a marginal increase in computational resources, thus supporting its feasibility for on-board deployment.

---


### 209. [Learning Who Disagrees: Demographic Importance Weighting for Modeling Annotator Distributions with DiADEM](https://arxiv.org/abs/2604.08425)

**<font color=#1a73e8>作者：</font>** Samay U. Shetty, Tharindu Cyril Weerasooriya, Deepak Pandita 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When humans label subjective content, they disagree, and that disagreement is not noise. It reflects genuine differences in perspective shaped by annotators' social identities and lived experiences. Yet standard practice still flattens these judgments into a single majority label, and recent LLM-based approaches fare no better: we show that prompted large language models, even with chain-of-thought reasoning, fail to recover the structure of human disagreement. We introduce DiADEM, a neural architecture that learns "how much each demographic axis matters" for predicting who will disagree and on what. DiADEM encodes annotators through per-demographic projections governed by a learned importance vector $\boldsymbol{\alpha}$, fuses annotator and item representations via complementary concatenation and Hadamard interactions, and is trained with a novel item-level disagreement loss that directly penalizes mispredicted annotation variance. On the DICES conversational-safety and VOICED political-offense benchmarks, DiADEM substantially outperforms both the LLM-as-a-judge and neural model baselines across standard and perspectivist metrics, achieving strong disagreement tracking ($r{=}0.75$ on DICES). The learned $\boldsymbol{\alpha}$ weights reveal that race and age consistently emerge as the most influential demographic factors driving annotator disagreement across both datasets. Our results demonstrate that explicitly modeling who annotators are not just what they label is essential for NLP systems that aim to faithfully represent human interpretive diversity.

---


### 210. [KV Cache Offloading for Context-Intensive Tasks](https://arxiv.org/abs/2604.08426)

**<font color=#1a73e8>作者：</font>** Andrey Bocharnikov, Ivan Ermakov, Denis Kuznedelev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the growing demand for long-context LLMs across a wide range of applications, the key-value (KV) cache has become a critical bottleneck for both latency and memory usage. Recently, KV-cache offloading has emerged as a promising approach to reduce memory footprint and inference latency while preserving accuracy. Prior evaluations have largely focused on tasks that do not require extracting large amounts of information from the context. In this work, we study KV-cache offloading on context-intensive tasks: problems where the solution requires looking up a lot of information from the input prompt. We create and release the Text2JSON benchmark, a highly context-intensive task that requires extracting structured knowledge from raw text. We evaluate modern KV offloading on Text2JSON and other context-intensive tasks and find significant performance degradation on both Llama 3 and Qwen 3 models. Our analysis identifies two key reasons for poor accuracy: low-rank projection of keys and unreliable landmarks, and proposes a simpler alternative strategy that significantly improves accuracy across multiple LLM families and benchmarks. These findings highlight the need for a comprehensive and rigorous evaluation of long-context compression techniques.

---


### 211. [HST-HGN: Heterogeneous Spatial-Temporal Hypergraph Networks with Bidirectional State Space Models for Global Fatigue Assessment](https://arxiv.org/abs/2604.08435)

**<font color=#1a73e8>作者：</font>** Changdao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> It remains challenging to assess driver fatigue from untrimmed videos under constrained computational budgets, due to the difficulty of modeling long-range temporal dependencies in subtle facial expressions. Some existing approaches rely on computationally heavy architectures, whereas others employ traditional lightweight pairwise graph networks, despite their limited capacity to model high-order synergies and global temporal context. Therefore, we propose HST-HGN, a novel Heterogeneous Spatial-Temporal Hypergraph Network driven by Bidirectional State Space Models. Spatially, we introduce a hierarchical hypergraph network to fuse pose-disentangled geometric topologies with multi-modal texture patches dynamically. This formulation encapsulates high-order synergistic facial deformations, effectively overcoming the limitations of conventional methods. In temporal terms, a Bi-Mamba module with linear complexity is applied to perform bidirectional sequence modeling. This explicit temporal-evolution filtering enables the network to distinguish highly ambiguous transient actions, such as yawning versus speaking, while encompassing their complete physiological lifecycles. Extensive evaluations across diverse fatigue benchmarks demonstrate that HST-HGN achieves state-of-the-art performance. In particular, our method strikes a balance between discriminative power and computational efficiency, making it well-suited for real-time in-cabin edge deployment.

---


### 212. [Provably Adaptive Linear Approximation for the Shapley Value and Beyond](https://arxiv.org/abs/2604.08438)

**<font color=#1a73e8>作者：</font>** Weida Li, Yaoliang Yu, Bryan Kian Hsiang Low  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Shapley value, and its broader family of semi-values, has received much attention in various attribution problems. A fundamental and long-standing challenge is their efficient approximation, since exact computation generally requires an exponential number of utility queries in the number of players $n$. To meet the challenges of large-scale applications, we explore the limits of efficiently approximating semi-values under a $\Theta(n)$ space constraint. Building upon a vector concentration inequality, we establish a theoretical framework that enables sharper query complexities for existing unbiased randomized algorithms. Within this framework, we systematically develop a linear-space algorithm that requires $O(\frac{n}{\epsilon^{2}}\log\frac{1}{\delta})$ utility queries to ensure $P(\|\hat{\boldsymbol\phi}-\boldsymbol\phi\|_{2}\geq\epsilon)\leq \delta$ for all commonly used semi-values. In particular, our framework naturally bridges OFA, unbiased kernelSHAP, SHAP-IQ and the regression-adjusted approach, and definitively characterizes when paired sampling is beneficial. Moreover, our algorithm allows explicit minimization of the mean square error for each specific utility function. Accordingly, we introduce the first adaptive, linear-time, linear-space randomized algorithm, Adalina, that theoretically achieves improved mean square error. All of our theoretical findings are experimentally validated.

---


### 213. [AfriVoices-KE: A Multilingual Speech Dataset for Kenyan Languages](https://arxiv.org/abs/2604.08448)

**<font color=#1a73e8>作者：</font>** Lilian Wanzare, Cynthia Amol, zekiel Maina 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AfriVoices-KE is a large-scale multilingual speech dataset comprising approximately 3,000 hours of audio across five Kenyan languages: Dholuo, Kikuyu, Kalenjin, Maasai, and Somali. The dataset includes 750 hours of scripted speech and 2,250 hours of spontaneous speech, collected from 4,777 native speakers across diverse regions and demographics. This work addresses the critical underrepresentation of African languages in speech technology by providing a high-quality, linguistically diverse resource. Data collection followed a dual methodology: scripted recordings drew from compiled text corpora, translations, and domain-specific generated sentences spanning eleven domains relevant to the Kenyan context, while unscripted speech was elicited through textual and image prompts to capture natural linguistic variation and dialectal nuances. A customized mobile application enabled contributors to record using smartphones. Quality assurance operated at multiple layers, encompassing automated signal-to-noise ratio validation prior to recording and human review for content accuracy. Though the project encountered challenges common to low-resource settings, including unreliable infrastructure, device compatibility issues, and community trust barriers, these were mitigated through local mobilizers, stakeholder partnerships, and adaptive training protocols. AfriVoices-KE provides a foundational resource for developing inclusive automatic speech recognition and text-to-speech systems, while advancing the digital preservation of Kenya's linguistic heritage.

---


### 214. [KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://arxiv.org/abs/2604.08455)

**<font color=#1a73e8>作者：</font>** Tongbo Chen, Zhengxi Lu, Zhan Xu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized mobile agents that infer user preferences and calibrate proactive assistance hold great promise as everyday digital assistants, yet existing benchmarks fail to capture what this requires. Prior work evaluates preference recovery from static histories or intent prediction from fixed contexts. Neither tests whether an agent can elicit missing preferences through interaction, nor whether it can decide when to intervene, seek consent, or remain silent in a live GUI environment. We introduce KnowU-Bench, an online benchmark for personalized mobile agents built on a reproducible Android emulation environment, covering 42 general GUI tasks, 86 personalized tasks, and 64 proactive tasks. Unlike prior work that treats user preferences as static context, KnowU-Bench hides the user profile from the agent and exposes only behavioral logs, forcing genuine preference inference rather than context lookup. To support multi-turn preference elicitation, it instantiates an LLM-driven user simulator grounded in structured profiles, enabling realistic clarification dialogues and proactive consent handling. Beyond personalization, KnowU-Bench provides comprehensive evaluation of the complete proactive decision chain, including grounded GUI execution, consent negotiation, and post-rejection restraint, evaluated through a hybrid protocol combining rule-based verification with LLM-as-a-Judge scoring. Our experiments reveal a striking degradation: agents that excel at explicit task execution fall below 50% under vague instructions requiring user preference inference or intervention calibration, even for frontier models like Claude Sonnet 4.6. The core bottlenecks are not GUI navigation but preference acquisition and intervention calibration, exposing a fundamental gap between competent interface operation and trustworthy personal assistance.

---


### 215. [CrashSight: A Phase-Aware, Infrastructure-Centric Video Benchmark for Traffic Crash Scene Understanding and Reasoning](https://arxiv.org/abs/2604.08457)

**<font color=#1a73e8>作者：</font>** Rui Gan, Junyi Ma, Pei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cooperative autonomous driving requires traffic scene understanding from both vehicle and infrastructure perspectives. While vision-language models (VLMs) show strong general reasoning capabilities, their performance in safety-critical traffic scenarios remains insufficiently evaluated due to the ego-vehicle focus of existing benchmarks. To bridge this gap, we present \textbf{CrashSight}, a large-scale vision-language benchmark for roadway crash understanding using real-world roadside camera data. The dataset comprises 250 crash videos, annotated with 13K multiple-choice question-answer pairs organized under a two-tier taxonomy. Tier 1 evaluates the visual grounding of scene context and involved parties, while Tier 2 probes higher-level reasoning, including crash mechanics, causal attribution, temporal progression, and post-crash outcomes. We benchmark 8 state-of-the-art VLMs and show that, despite strong scene description capabilities, current models struggle with temporal and causal reasoning in safety-critical scenarios. We provide a detailed analysis of failure scenarios and discuss directions for improving VLM crash understanding. The benchmark provides a standardized evaluation framework for infrastructure-assisted perception in cooperative autonomous driving. The CrashSight benchmark, including the full dataset and code, is accessible at this https URL.

---


### 216. [A Machine Learning Framework for Turbofan Health Estimation via Inverse Problem Formulation](https://arxiv.org/abs/2604.08460)

**<font color=#1a73e8>作者：</font>** Milad Leyli-Abadi, Lucas Thil, Sebastien Razakarivony 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating the health state of turbofan engines is a challenging ill-posed inverse problem, hindered by sparse sensing and complex nonlinear thermodynamics. Research in this area remains fragmented, with comparisons limited by the use of unrealistic datasets and insufficient exploration of the exploitation of temporal information. This work investigates how to recover component-level health indicators from operational sensor data under realistic degradation and maintenance patterns. To support this study, we introduce a new dataset that incorporates industry-oriented complexities such as maintenance events and usage changes. Using this dataset, we establish an initial benchmark that compares steady-state and nonstationary data-driven models, and Bayesian filters, classic families of methods used to solve this problem. In addition to this benchmark, we introduce self-supervised learning (SSL) approaches that learn latent representations without access to true health labels, a scenario reflective of real-world operational constraints. By comparing the downstream estimation performance of these unsupervised representations against the direct prediction baselines, we establish a practical lower bound on the difficulty of solving this inverse problem. Our results reveal that traditional filters remain strong baselines, while SSL methods reveal the intrinsic complexity of health estimation and highlight the need for more advanced and interpretable inference strategies. For reproducibility, both the generated dataset and the implementation used in this work are made accessible.

---


### 217. [OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance](https://arxiv.org/abs/2604.08461)

**<font color=#1a73e8>作者：</font>** Haoxi Zeng, Qiankun Liu, Yi Bin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-Vocabulary Segmentation (OVS) aims to segment image regions beyond predefined category sets by leveraging semantic descriptions. While CLIP based approaches excel in semantic generalization, they frequently lack the fine-grained spatial awareness required for dense prediction. Recent efforts have incorporated Vision Foundation Models (VFMs) like DINO to alleviate these limitations. However, these methods still struggle with the precise edge perception necessary for high fidelity segmentation. In this paper, we analyze internal representations of DINO and discover that its inherent boundary awareness is not absent but rather undergoes progressive attenuation as features transition into deeper transformer blocks. To address this, we propose OVS-DINO, a novel framework that revitalizes latent edge-sensitivity of DINO through structural alignment with the Segment Anything Model (SAM). Specifically, we introduce a Structure-Aware Encoder (SAE) and a Structure-Modulated Decoder (SMD) to effectively activate boundary features of DINO using SAM's structural priors, complemented by a supervision strategy utilizing SAM generated pseudo-masks. Extensive experiments demonstrate that our method achieves state-of-the-art performance across multiple weakly-supervised OVS benchmarks, improving the average score by 2.1% (from 44.8% to 46.9%). Notably, our approach significantly enhances segmentation accuracy in complex, cluttered scenarios, with a gain of 6.3% on Cityscapes (from 36.6% to 42.9%).

---


### 218. [TTVS: Boosting Self-Exploring Reinforcement Learning via Test-time Variational Synthesis](https://arxiv.org/abs/2604.08468)

**<font color=#1a73e8>作者：</font>** Sikai Bai, Haoxi Li, Jie Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite significant advances in Large Reasoning Models (LRMs) driven by reinforcement learning with verifiable rewards (RLVR), this paradigm is fundamentally limited in specialized or novel domains where such supervision is prohibitively expensive or unavailable, posing a key challenge for test-time adaptation. While existing test-time methods offer a potential solution, they are constrained by learning from static query sets, risking overfitting to textual patterns. To address this gap, we introduce Test-Time Variational Synthesis (TTVS), a novel framework that enables LRMs to self-evolve by dynamically augmenting the training stream from unlabeled test queries. TTVS comprises two synergistic modules: (1) Online Variational Synthesis, which transforms static test queries into a dynamic stream of diverse, semantically-equivalent variations, enforcing the model to learn underlying problem logic rather than superficial patterns; (2) Test-time Hybrid Exploration, which balances accuracy-driven exploitation with consistency-driven exploration across synthetic variants. Extensive experiments show TTVS yields superior performance across eight model architectures. Notably, using only unlabeled test-time data, TTVS not only surpasses other test-time adaptation methods but also outperforms state-of-the-art supervised RL-based techniques trained on vast, high-quality labeled data.

---


### 219. [Persistence-Augmented Neural Networks](https://arxiv.org/abs/2604.08469)

**<font color=#1a73e8>作者：</font>** Elena Xinyi Wang, Arnur Nigmetov, Dmitriy Morozov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Topological Data Analysis (TDA) provides tools to describe the shape of data, but integrating topological features into deep learning pipelines remains challenging, especially when preserving local geometric structure rather than summarizing it globally. We propose a persistence-based data augmentation framework that encodes local gradient flow regions and their hierarchical evolution using the Morse-Smale complex. This representation, compatible with both convolutional and graph neural networks, retains spatially localized topological information across multiple scales. Importantly, the augmentation procedure itself is efficient, with computational complexity $O(n \log n)$, making it practical for large datasets. We evaluate our method on histopathology image classification and 3D porous material regression, where it consistently outperforms baselines and global TDA descriptors such as persistence images and landscapes. We also show that pruning the base level of the hierarchy reduces memory usage while maintaining competitive performance. These results highlight the potential of local, structured topological augmentation for scalable and interpretable learning across data modalities.

---


### 220. [Quantization Impact on the Accuracy and Communication Efficiency Trade-off in Federated Learning for Aerospace Predictive Maintenance](https://arxiv.org/abs/2604.08474)

**<font color=#1a73e8>作者：</font>** Abdelkarim Loukili  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables privacy-preserving predictive maintenance across distributed aerospace fleets, but gradient communication overhead constrains deployment on bandwidth-limited IoT nodes. This paper investigates the impact of symmetric uniform quantization ($b \in \{32,8,4,2\}$ bits) on the accuracy--efficiency trade-off of a custom-designed lightweight 1-D convolutional model (AeroConv1D, 9\,697 parameters) trained via FL on the NASA C-MAPSS benchmark under a realistic Non-IID client partition. Using a rigorous multi-seed evaluation ($N=10$ seeds), we show that INT4 achieves accuracy \emph{statistically indistinguishable} from FP32 on both FD001 ($p=0.341$) and FD002 ($p=0.264$ MAE, $p=0.534$ NASA score) while delivering an $8\times$ reduction in gradient communication cost (37.88~KiB $\to$ 4.73~KiB per round). A key methodological finding is that naïve IID client partitioning artificially suppresses variance; correct Non-IID evaluation reveals the true operational instability of extreme quantization, demonstrated via a direct empirical IID vs.\ Non-IID comparison. INT2 is empirically characterized as unsuitable: while it achieves lower MAE on FD002 through extreme quantization-induced over-regularization, this apparent gain is accompanied by catastrophic NASA score instability (CV\,=\,45.8\% vs.\ 22.3\% for FP32), confirming non-reproducibility under heterogeneous operating conditions. Analytical FPGA resource projections on the Xilinx ZCU102 confirm that INT4 fits within hardware constraints (85.5\% DSP utilization), potentially enabling a complete FL pipeline on a single SoC. The full simulation codebase and FPGA estimation scripts are publicly available at this https URL.

---


### 221. [LAMP: Lift Image-Editing as General 3D Priors for Open-world Manipulation](https://arxiv.org/abs/2604.08475)

**<font color=#1a73e8>作者：</font>** Jingjing Wang, Zhengdong Hong, Chong Bao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-like generalization in open-world remains a fundamental challenge for robotic manipulation. Existing learning-based methods, including reinforcement learning, imitation learning, and vision-language-action-models (VLAs), often struggle with novel tasks and unseen environments. Another promising direction is to explore generalizable representations that capture fine-grained spatial and geometric relations for open-world manipulation. While large-language-model (LLMs) and vision-language-model (VLMs) provide strong semantic reasoning based on language or annotated 2D representations, their limited 3D awareness restricts their applicability to fine-grained manipulation. To address this, we propose LAMP, which lifts image-editing as 3D priors to extract inter-object 3D transformations as continuous, geometry-aware representations. Our key insight is that image-editing inherently encodes rich 2D spatial cues, and lifting these implicit cues into 3D transformations provides fine-grained and accurate guidance for open-world manipulation. Extensive experiments demonstrate that \codename delivers precise 3D transformations and achieves strong zero-shot generalization in open-world manipulation. Project page: this https URL.

---


### 222. [AI generates well-liked but templatic empathic responses](https://arxiv.org/abs/2604.08479)

**<font color=#1a73e8>作者：</font>** Emma Gueorguieva, Hongli Zhan, Jina Suh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent research shows that greater numbers of people are turning to Large Language Models (LLMs) for emotional support, and that people rate LLM responses as more empathic than human-written responses. We suggest a reason for this success: LLMs have learned and consistently deploy a well-liked template for expressing empathy. We develop a taxonomy of 10 empathic language "tactics" that include validating someone's feelings and paraphrasing, and apply this taxonomy to characterize the language that people and LLMs produce when writing empathic responses. Across a set of 2 studies comparing a total of n = 3,265 AI-generated (by six models) and n = 1,290 human-written responses, we find that LLM responses are highly formulaic at a discourse functional level. We discovered a template -- a structured sequence of tactics -- that matches between 83--90% of LLM responses (and 60--83\% in a held out sample), and when those are matched, covers 81--92% of the response. By contrast, human-written responses are more diverse. We end with a discussion of implications for the future of AI-generated empathy.

---


### 223. [Post-Quantum Cryptographic Analysis of Message Transformations Across the Network Stack](https://arxiv.org/abs/2604.08480)

**<font color=#1a73e8>作者：</font>** Ashish Kundu, Vishal Chakraborty, Ramana Kompella  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When a user sends a message over a wireless network, the message does not travel as-is. It is encrypted, authenticated, encapsulated, and transformed as it descends the protocol stack from the application layer to the physical medium. Each layer may apply its own cryptographic operations using its own algorithms, and these algorithms differ in their vulnerability to quantum computers. The security of the overall communication depends not on any single layer but on the \emph{composition} of transformations across all layers.
We develop a preliminary formal framework for analyzing these cross-layer cryptographic transformations with respect to post-quantum cryptographic (PQC) readiness. We classify every per-layer cryptographic operation into one of four quantum vulnerability categories, define how per-layer PQC statuses compose across the full message transformation chain, and prove that this composition forms a bounded lattice with confidentiality composing via the join (max) operator and authentication via the meet (min). We apply the framework to five communication scenarios spanning Linux and iOS platforms, and identify several research challenges. Among our findings: WPA2-Personal provides strictly better PQC posture than both WPA3-Personal and WPA2-Enterprise; a single post-quantum layer suffices for payload confidentiality but \emph{every} layer must migrate for complete authentication; and metadata protection depends solely on the outermost layer.

---


### 224. [The Impact of Dimensionality on the Stability of Node Embeddings](https://arxiv.org/abs/2604.08492)

**<font color=#1a73e8>作者：</font>** Tobias Schumacher, Simon Reichelt, Markus Strohmaier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Previous work has established that neural network-based node embeddings return different outcomes when trained with identical parameters on the same dataset, just from using different training seeds. Yet, it has not been thoroughly analyzed how key hyperparameters such as embedding dimension could impact this instability. In this work, we investigate how varying the dimensionality of node embeddings influences both their stability and downstream performance. We systematically evaluate five widely used methods -- ASNE, DGI, GraphSAGE, node2vec, and VERSE -- across multiple datasets and embedding dimensions. We assess stability from both a representational perspective and a functional perspective, alongside performance evaluation. Our results show that embedding stability varies significantly with dimensionality, but we observe different patterns across the methods we consider: while some approaches, such as node2vec and ASNE, tend to become more stable with higher dimensionality, other methods do not exhibit the same trend. Moreover, we find that maximum stability does not necessarily align with optimal task performance. These findings highlight the importance of carefully selecting embedding dimension, and provide new insights into the trade-offs between stability, performance, and computational effectiveness in graph representation learning.

---


### 225. [Bridging the Gap between Micro-scale Traffic Simulation and 4D Digital Cityscapes](https://arxiv.org/abs/2604.08497)

**<font color=#1a73e8>作者：</font>** Longxiang Jiao, Lukas Hofmann, Yiru Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While micro-scale traffic simulations provide essential data for urban planning, they are rarely coupled with the high-fidelity visualization or auralization necessary for effective stakeholder communication. In this work, we present a real-time 4D visualization framework that couples the SUMO traffic with a photorealistic, geospatially accurate VR representation of Zurich in Unreal Engine 5. Our architecture implements a robust C++ data pipeline for synchronized vehicle visualization and features an Open Sound Control (OSC) interface to support external auralization engines. We validate the framework through a user study assessing the correlation between simulated traffic dynamics and human perception. Results demonstrate a high degree of perceptual alignment, where users correctly interpret safety risks from the 4D simulation. Furthermore, our findings indicate that the inclusion of spatialized audio alters the user's sense of safety, showing the importance of multimodality in traffic simulations.

---


### 226. [PIArena: A Platform for Prompt Injection Evaluation](https://arxiv.org/abs/2604.08499)

**<font color=#1a73e8>作者：</font>** Runpeng Geng, Chenlong Yin, Yanting Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection attacks pose serious security risks across a wide range of real-world applications. While receiving increasing attention, the community faces a critical gap: the lack of a unified platform for prompt injection evaluation. This makes it challenging to reliably compare defenses, understand their true robustness under diverse attacks, or assess how well they generalize across tasks and benchmarks. For instance, many defenses initially reported as effective were later found to exhibit limited robustness on diverse datasets and attacks. To bridge this gap, we introduce PIArena, a unified and extensible platform for prompt injection evaluation that enables users to easily integrate state-of-the-art attacks and defenses and evaluate them across a variety of existing and new benchmarks. We also design a dynamic strategy-based attack that adaptively optimizes injected prompts based on defense feedback. Through comprehensive evaluation using PIArena, we uncover critical limitations of state-of-the-art defenses: limited generalizability across tasks, vulnerability to adaptive attacks, and fundamental challenges when an injected task aligns with the target task. The code and datasets are available at this https URL.

---


### 227. [Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500)

**<font color=#1a73e8>作者：</font>** Qi Wu, Khiem Vuong, Minsik Jeon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We tackle the problem of sparse novel view synthesis (NVS) using video diffusion models; given $K$ ($\approx 5$) multi-view images of a scene and their camera poses, we predict the view from a target camera pose. Many prior approaches leverage generative image priors encoded via diffusion models. However, models trained on single images lack multi-view knowledge. We instead argue that video models already contain implicit multi-view knowledge and so should be easier to adapt for NVS. Our key insight is to formulate sparse NVS as a low frame-rate video completion task. However, one challenge is that sparse NVS is defined over an unordered set of inputs, often too sparse to admit a meaningful order, so the models should be $\textit{invariant}$ to permutations of that input set. To this end, we present FrameCrafter, which adapts video models (naturally trained with coherent frame orderings) to permutation-invariant NVS through several architectural modifications, including per-frame latent encodings and removal of temporal positional embeddings. Our results suggest that video models can be easily trained to "forget" about time with minimal supervision, producing competitive performance on sparse-view NVS benchmarks. Project page: this https URL

---


### 228. [Quantifying Explanation Consistency: The C-Score Metric for CAM-Based Explainability in Medical Image Classification](https://arxiv.org/abs/2604.08502)

**<font color=#1a73e8>作者：</font>** Kabilan Elangovan, Daniel Ting  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class Activation Mapping (CAM) methods are widely used to generate visual explanations for deep learning classifiers in medical imaging. However, existing evaluation frameworks assess whether explanations are correct, measured by localisation fidelity against radiologist annotations, rather than whether they are consistent: whether the model applies the same spatial reasoning strategy across different patients with the same pathology. We propose the C-Score (Consistency Score), a confidence-weighted, annotation-free metric that quantifies intra-class explanation reproducibility via intensity-emphasised pairwise soft IoU across correctly classified instances. We evaluate six CAM techniques: GradCAM, GradCAM++, LayerCAM, EigenCAM, ScoreCAM, and MS GradCAM++ across three CNN architectures (DenseNet201, InceptionV3, ResNet50V2) over thirty training epochs on the Kermany chest X-ray dataset, covering transfer learning and fine-tuning phases. We identify three distinct mechanisms of AUC-consistency dissociation, invisible to standard classification metrics: threshold-mediated gold list collapse, technique-specific attribution collapse at peak AUC, and class-level consistency masking in global aggregation. C-Score provides an early warning signal of impending model instability. ScoreCAM deterioration on ResNet50V2 is detectable one full checkpoint before catastrophic AUC collapse and yields architecture-specific clinical deployment recommendations grounded in explanation quality rather than predictive ranking alone.

---


### 229. [Phantom: Physics-Infused Video Generation via Joint Modeling of Visual and Latent Physical Dynamics](https://arxiv.org/abs/2604.08503)

**<font color=#1a73e8>作者：</font>** Ying Shen, Jerry Xiong, Tianjiao Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative video modeling, driven by large-scale datasets and powerful architectures, have yielded remarkable visual realism. However, emerging evidence suggests that simply scaling data and model size does not endow these systems with an understanding of the underlying physical laws that govern real-world dynamics. Existing approaches often fail to capture or enforce such physical consistency, resulting in unrealistic motion and dynamics. In his work, we investigate whether integrating the inference of latent physical properties directly into the video generation process can equip models with the ability to produce physically plausible videos. To this end, we propose Phantom, a Physics-Infused Video Generation model that jointly models the visual content and latent physical dynamics. Conditioned on observed video frames and inferred physical states, Phantom jointly predicts latent physical dynamics and generates future video frames. Phantom leverages a physics-aware video representation that serves as an abstract yet informaive embedding of the underlying physics, facilitating the joint prediction of physical dynamics alongside video content without requiring an explicit specification of a complex set of physical dynamics and properties. By integrating the inference of physical-aware video representation directly into the video generation process, Phantom produces video sequences that are both visually realistic and physically consistent. Quantitative and qualitative results on both standard video generation and physics-aware benchmarks demonstrate that Phantom not only outperforms existing methods in terms of adherence to physical dynamics but also delivers competitive perceptual fidelity.

---


### 230. [Visually-grounded Humanoid Agents](https://arxiv.org/abs/2604.08509)

**<font color=#1a73e8>作者：</font>** Hang Ye, Xiaoxuan Ma, Fan Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital human generation has been studied for decades and supports a wide range of real-world applications. However, most existing systems are passively animated, relying on privileged state or scripted control, which limits scalability to novel environments. We instead ask: how can digital humans actively behave using only visual observations and specified goals in novel scenes? Achieving this would enable populating any 3D environments with digital humans at scale that exhibit spontaneous, natural, goal-directed behaviors. To this end, we introduce Visually-grounded Humanoid Agents, a coupled two-layer (world-agent) paradigm that replicates humans at multiple levels: they look, perceive, reason, and behave like real people in real-world 3D scenes. The World Layer reconstructs semantically rich 3D Gaussian scenes from real-world videos via an occlusion-aware pipeline and accommodates animatable Gaussian-based human avatars. The Agent Layer transforms these avatars into autonomous humanoid agents, equipping them with first-person RGB-D perception and enabling them to perform accurate, embodied planning with spatial awareness and iterative reasoning, which is then executed at the low level as full-body actions to drive their behaviors in the scene. We further introduce a benchmark to evaluate humanoid-scene interaction in diverse reconstructed environments. Experiments show our agents achieve robust autonomous behavior, yielding higher task success rates and fewer collisions than ablations and state-of-the-art planning methods. This work enables active digital human population and advances human-centric embodied AI. Data, code, and models will be open-sourced.

---


### 231. ["Because we are no longer ashamed of our disabilities, we are proud": Advocating and Reclaiming Next-Gen Accessibility Symbols](https://arxiv.org/abs/2604.08514)

**<font color=#1a73e8>作者：</font>** Karen Joy, Chris Dodge, Harsh Chavda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Our study investigates the relationship between accessibility symbols and emerging technologies in supporting disability disclosure. We conducted twenty three remote design creation sessions with semi structured interviews to examine participants awareness of existing symbols, how they use symbols across online and offline contexts, and barriers to adoption and interpretation. Through participant sketching and future oriented storyboard probes, participants proposed ways to integrate symbols into wearable devices, mobile interfaces, and portable tools, emphasizing customizable and context sensitive disclosure. Our findings suggest symbols are most effective when paired with technologies that provide user control over visibility and optional pathways for explanation, helping reduce misinterpretation while supporting agency in disclosure moments. By reimagining symbol based assistance as part of a broader disclosure system where meaning depends on the symbol, its carrier, and context, this work informs more inclusive accessibility supports across diverse settings.

---


### 232. [MolmoWeb: Open Visual Web Agent and Open Data for the Open Web](https://arxiv.org/abs/2604.08516)

**<font color=#1a73e8>作者：</font>** Tanmay Gupta, Piper Wolters, Zixian Ma 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Web agents--autonomous systems that navigate and execute tasks on the web on behalf of users--have the potential to transform how people interact with the digital world. However, the most capable web agents today rely on proprietary models with undisclosed training data and recipes, limiting scientific understanding, reproducibility, and community-driven progress.
We believe agents for the open web should be built in the open. To this end, we introduce (1) MolmoWebMix, a large and diverse mixture of browser task demonstrations and web-GUI perception data and (2) MolmoWeb, a family of fully open multimodal web agents. Specifically, MolmoWebMix combines over 100K synthetic task trajectories from multiple complementary generation pipelines with 30K+ human demonstrations, atomic web-skill trajectories, and GUI perception data, including referring expression grounding and screenshot question answering. MolmoWeb agents operate as instruction-conditioned visual-language action policies: given a task instruction and a webpage screenshot, they predict the next browser action, requiring no access to HTML, accessibility trees, or specialized APIs.
Available in 4B and 8B size, on browser-use benchmarks like WebVoyager, Online-Mind2Web, and DeepShop, MolmoWeb agents achieve state-of-the-art results outperforming similar scale open-weight-only models such as Fara-7B, UI-Tars-1.5-7B, and Holo1-7B. MolmoWeb-8B also surpasses set-of-marks (SoM) agents built on much larger closed frontier models like GPT-4o. We further demonstrate consistent gains through test-time scaling via parallel rollouts with best-of-N selection, achieving 94.7% and 60.5% pass@4 (compared to 78.2% and 35.3% pass@1) on WebVoyager and Online-Mind2Web respectively. We will release model checkpoints, training data, code, and a unified evaluation harness to enable reproducibility and accelerate open research on web agents.

---


### 233. [ClawBench: Can AI Agents Complete Everyday Online Tasks?](https://arxiv.org/abs/2604.08523)

**<font color=#1a73e8>作者：</font>** Yuxuan Zhang, Yubo Wang, Yipeng Zhu 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI agents may be able to automate your inbox, but can they automate other routine aspects of your life? Everyday online tasks offer a realistic yet unsolved testbed for evaluating the next generation of AI agents. To this end, we introduce ClawBench, an evaluation framework of 153 simple tasks that people need to accomplish regularly in their lives and work, spanning 144 live platforms across 15 categories, from completing purchases and booking appointments to submitting job applications. These tasks require demanding capabilities beyond existing benchmarks, such as obtaining relevant information from user-provided documents, navigating multi-step workflows across diverse platforms, and write-heavy operations like filling in many detailed forms correctly. Unlike existing benchmarks that evaluate agents in offline sandboxes with static pages, ClawBench operates on production websites, preserving the full complexity, dynamic nature, and challenges of real-world web interaction. A lightweight interception layer captures and blocks only the final submission request, ensuring safe evaluation without real-world side effects. Our evaluations of 7 frontier models show that both proprietary and open-source models can complete only a small portion of these tasks. For example, Claude Sonnet 4.6 achieves only 33.3%. Progress on ClawBench brings us closer to AI agents that can function as reliable general-purpose assistants.

---


### 234. [FIT: A Large-Scale Dataset for Fit-Aware Virtual Try-On](https://arxiv.org/abs/2604.08526)

**<font color=#1a73e8>作者：</font>** Johanna Karras, Yuanhao Wang, Yingwei Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given a person and a garment image, virtual try-on (VTO) aims to synthesize a realistic image of the person wearing the garment, while preserving their original pose and identity. Although recent VTO methods excel at visualizing garment appearance, they largely overlook a crucial aspect of the try-on experience: the accuracy of garment fit -- for example, depicting how an extra-large shirt looks on an extra-small person. A key obstacle is the absence of datasets that provide precise garment and body size information, particularly for "ill-fit" cases, where garments are significantly too large or too small. Consequently, current VTO methods default to generating well-fitted results regardless of the garment or person size.
In this paper, we take the first steps towards solving this open problem. We introduce FIT (Fit-Inclusive Try-on), a large-scale VTO dataset comprising over 1.13M try-on image triplets accompanied by precise body and garment measurements. We overcome the challenges of data collection via a scalable synthetic strategy: (1) We programmatically generate 3D garments using GarmentCode and drape them via physics simulation to capture realistic garment fit. (2) We employ a novel re-texturing framework to transform synthetic renderings into photorealistic images while strictly preserving geometry. (3) We introduce person identity preservation into our re-texturing model to generate paired person images (same person, different garments) for supervised training. Finally, we leverage our FIT dataset to train a baseline fit-aware virtual try-on model. Our data and results set the new state-of-the-art for fit-aware virtual try-on, as well as offer a robust benchmark for future research. We will make all data and code publicly available on our project page: this https URL.

---


### 235. [PSI: Shared State as the Missing Layer for Coherent AI-Generated Instruments in Personal AI Agents](https://arxiv.org/abs/2604.08529)

**<font color=#1a73e8>作者：</font>** Zhiyuan Wang, Erzhen Hu, Mark Rucker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Personal AI tools can now be generated from natural-language requests, but they often remain isolated after creation. We present PSI, a shared-state architecture that turns independently generated modules into coherent instruments: persistent, connected, and chat-complementary artifacts accessible through both GUIs and a generic chat agent. By publishing current state and write-back affordances to a shared personal-context bus, modules enable cross-module reasoning and synchronized actions across interfaces. We study PSI through a three-week autobiographical deployment in a self-developed personal AI environment and show that later-generated instruments can be integrated automatically through the same contract. PSI identifies shared state as the missing systems layer that transforms AI-generated personal software from isolated apps into coherent personal computing environments.

---


### 236. [Self-Improving 4D Perception via Self-Distillation](https://arxiv.org/abs/2604.08532)

**<font color=#1a73e8>作者：</font>** Nan Huang, Pengcheng Yu, Weijia Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale multi-view reconstruction models have made remarkable progress, but most existing approaches still rely on fully supervised training with ground-truth 3D/4D annotations. Such annotations are expensive and particularly scarce for dynamic scenes, limiting scalability. We propose SelfEvo, a self-improving framework that continually improves pretrained multi-view reconstruction models using unlabeled videos. SelfEvo introduces a self-distillation scheme using spatiotemporal context asymmetry, enabling self-improvement for learning-based 4D perception without external annotations. We systematically study design choices that make self-improvement effective, including loss signals, forms of asymmetry, and other training strategies. Across eight benchmarks spanning diverse datasets and domains, SelfEvo consistently improves pretrained baselines and generalizes across base models (e.g. VGGT and $\pi^3$), with significant gains on dynamic scenes. Overall, SelfEvo achieves up to 36.5% relative improvement in video depth estimation and 20.1% in camera estimation, without using any labeled data. Project Page: this https URL.

---


### 237. [RewardFlow: Generate Images by Optimizing What You Reward](https://arxiv.org/abs/2604.08536)

**<font color=#1a73e8>作者：</font>** Onkar Susladkar, Dong-Hwan Jang, Tushar Prakash 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce RewardFlow, an inversion-free framework that steers pretrained diffusion and flow-matching models at inference time through multi-reward Langevin dynamics. RewardFlow unifies complementary differentiable rewards for semantic alignment, perceptual fidelity, localized grounding, object consistency, and human preference, and further introduces a differentiable VQA-based reward that provides fine-grained semantic supervision through language-vision reasoning. To coordinate these heterogeneous objectives, we design a prompt-aware adaptive policy that extracts semantic primitives from the instruction, infers edit intent, and dynamically modulates reward weights and step sizes throughout sampling. Across several image editing and compositional generation benchmarks, RewardFlow delivers state-of-the-art edit fidelity and compositional alignment.

---


### 238. [Scal3R: Scalable Test-Time Training for Large-Scale 3D Reconstruction](https://arxiv.org/abs/2604.08542)

**<font color=#1a73e8>作者：</font>** Tao Xie, Peishan Yang, Yudong Jin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the task of large-scale 3D scene reconstruction from long video sequences. Recent feed-forward reconstruction models have shown promising results by directly regressing 3D geometry from RGB images without explicit 3D priors or geometric constraints. However, these methods often struggle to maintain reconstruction accuracy and consistency over long sequences due to limited memory capacity and the inability to effectively capture global contextual cues. In contrast, humans can naturally exploit the global understanding of the scene to inform local perception. Motivated by this, we propose a novel neural global context representation that efficiently compresses and retains long-range scene information, enabling the model to leverage extensive contextual cues for enhanced reconstruction accuracy and consistency. The context representation is realized through a set of lightweight neural sub-networks that are rapidly adapted during test time via self-supervised objectives, which substantially increases memory capacity without incurring significant computational overhead. The experiments on multiple large-scale benchmarks, including the KITTI Odometry~\cite{Geiger2012CVPR} and Oxford Spires~\cite{tao2025spires} datasets, demonstrate the effectiveness of our approach in handling ultra-large scenes, achieving leading pose accuracy and state-of-the-art 3D reconstruction accuracy while maintaining efficiency. Code is available at this https URL.

---


### 239. [E-3DPSM: A State Machine for Event-Based Egocentric 3D Human Pose Estimation](https://arxiv.org/abs/2604.08543)

**<font color=#1a73e8>作者：</font>** Mayur Deshmukh, Hiroyasu Akada, Helge Rhodin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras offer multiple advantages in monocular egocentric 3D human pose estimation from head-mounted devices, such as millisecond temporal resolution, high dynamic range, and negligible motion blur. Existing methods effectively leverage these properties, but suffer from low 3D estimation accuracy, insufficient in many applications (e.g., immersive VR/AR). This is due to the design not being fully tailored towards event streams (e.g., their asynchronous and continuous nature), leading to high sensitivity to self-occlusions and temporal jitter in the estimates. This paper rethinks the setting and introduces E-3DPSM, an event-driven continuous pose state machine for event-based egocentric 3D human pose estimation. E-3DPSM aligns continuous human motion with fine-grained event dynamics; it evolves latent states and predicts continuous changes in 3D joint positions associated with observed events, which are fused with direct 3D human pose predictions, leading to stable and drift-free final 3D pose reconstructions. E-3DPSM runs in real-time at 80 Hz on a single workstation and sets a new state of the art in experiments on two benchmarks, improving accuracy by up to 19% (MPJPE) and temporal stability by up to 2.7x. See our project page for the source code and trained models.

---


### 240. [When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models](https://arxiv.org/abs/2604.08546)

**<font color=#1a73e8>作者：</font>** Zhengyang Sun, Yu Chen, Xin Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video diffusion models have enabled open-ended video synthesis, but often struggle with generating the correct number of objects specified in a prompt. We introduce NUMINA , a training-free identify-then-guide framework for improved numerical alignment. NUMINA identifies prompt-layout inconsistencies by selecting discriminative self- and cross-attention heads to derive a countable latent layout. It then refines this layout conservatively and modulates cross-attention to guide regeneration. On the introduced CountBench, NUMINA improves counting accuracy by up to 7.4% on Wan2.1-1.3B, and by 4.9% and 5.5% on 5B and 14B models, respectively. Furthermore, CLIP alignment is improved while maintaining temporal consistency. These results demonstrate that structural guidance complements seed search and prompt enhancement, offering a practical path toward count-accurate text-to-video diffusion. The code is available at this https URL.

---


### 241. [GaussiAnimate: Reconstruct and Rig Animatable Categories with Level of Dynamics](https://arxiv.org/abs/2604.08547)

**<font color=#1a73e8>作者：</font>** Jiaxin Wang, Dongxin Lyu, Zeyu Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Free-form bones, that conform closely to the surface, can effectively capture non-rigid deformations, but lack a kinematic structure necessary for intuitive control. Thus, we propose a Scaffold-Skin Rigging System, termed "Skelebones", with three key steps: (1) Bones: compress temporally-consistent deformable Gaussians into free-form bones, approximating non-rigid surface deformations; (2) Skeleton: extract a Mean Curvature Skeleton from canonical Gaussians and refine it temporally, ensuring a category-agnostic, motion-adaptive, and topology-correct kinematic structure; (3) Binding: bind the skeleton and bones via non-parametric partwise motion matching (PartMM), synthesizing novel bone motions by matching, retrieving, and blending existing ones. Collectively, these three steps enable us to compress the Level of Dynamics of 4D shapes into compact skelebones that are both controllable and expressive. We validate our approach on both synthetic and real-world datasets, achieving significant improvements in reanimation performance across unseen poses-with 17.3% PSNR gains over Linear Blend Skinning (LBS) and 21.7% over Bag-of-Bones (BoB)-while maintaining excellent reconstruction fidelity, particularly for characters exhibiting complex non-rigid surface dynamics. Our Partwise Motion Matching algorithm demonstrates strong generalization to both Gaussian and mesh representations, especially under low-data regime (~1000 frames), achieving 48.4% RMSE improvement over robust LBS and outperforming GRU- and MLP-based learning methods by >20%. Code will be made publicly available for research purposes at this http URL.

---


### 242. [ETCH-X: Robustify Expressive Body Fitting to Clothed Humans with Composable Datasets](https://arxiv.org/abs/2604.08548)

**<font color=#1a73e8>作者：</font>** Xiaoben Li, Jingyi Wu, Zeyu Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human body fitting, which aligns parametric body models such as SMPL to raw 3D point clouds of clothed humans, serves as a crucial first step for downstream tasks like animation and texturing. An effective fitting method should be both locally expressive-capturing fine details such as hands and facial features-and globally robust to handle real-world challenges, including clothing dynamics, pose variations, and noisy or partial inputs. Existing approaches typically excel in only one aspect, lacking an all-in-one this http URL upgrade ETCH to ETCH-X, which leverages a tightness-aware fitting paradigm to filter out clothing dynamics ("undress"), extends expressiveness with SMPL-X, and replaces explicit sparse markers (which are highly sensitive to partial data) with implicit dense correspondences ("dense fit") for more robust and fine-grained body fitting. Our disentangled "undress" and "dense fit" modular stages enable separate and scalable training on composable data sources, including diverse simulated garments (CLOTH3D), large-scale full-body motions (AMASS), and fine-grained hand gestures (InterHand2.6M), improving outfit generalization and pose robustness of both bodies and hands. Our approach achieves robust and expressive fitting across diverse clothing, poses, and levels of input completeness, delivering a substantial performance improvement over ETCH on both: 1) seen data, such as 4D-Dress (MPJPE-All, 33.0% ) and CAPE (V2V-Hands, 35.8% ), and 2) unseen data, such as BEDLAM2.0 (MPJPE-All, 80.8% ; V2V-All, 80.5% ). Code and models will be released at this https URL.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
