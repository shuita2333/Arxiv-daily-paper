# 📦 其他研究 | 2026年11月03日

> 本类共 **193** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-193](./part-04.md)

---

### 101. [BDNet: Fast-slow thinking is all you need](https://arxiv.org/abs/2610.41485)

**<font color=#1a73e8>作者：</font>** Chenzhi Zheng, Zhuoran Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present BDNet, a hierarchical image-classification backbone built around fast image features and slow statistical references. Its baseline deformation operator (BDO) transforms the deviation of a feature from a stage-specific reference through a low-rank projection and a learned channel scale. Rather than computing pairwise token similarity, the branch operates directly on baseline-relative residuals with complexity linear in the token count. Each of four reference buffers accumulates detached stage statistics during training and remains frozen at inference. A four-stage pyramid with depths $(2,2,6,2)$ and widths $(96,192,384,768)$ yields a 20.70M-parameter classifier at $224\times224$ resolution. We organize an ImageNet-1K study around clean classification, eight controlled ablations, and Gaussian-noise, contrast, and brightness perturbations. The central hypothesis is that a slow reference can improve the robustness of a compact representation while retaining a simple tensor implementation. We distinguish this training-time statistical mechanism from input-dependent attention and make its linear inference behavior explicit.

---


### 102. [Sparse Text Diffusion under Dual Budgets: Context Connectivity and Expert Activation](https://arxiv.org/abs/2610.41487)

**<font color=#1a73e8>作者：</font>** Alexandros Christoforos, Chadbourne Davis, Paul Raj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context diffusion repeatedly pays for both token interaction and feed-forward computation. We formulate these costs as two separate budgets: the edges available to an attention graph and the experts activated for each token. This view connects local, dilated, and global attention with conditional expert computation without assuming that sparsity alone preserves document-level information. We specify normalized masked attention, distinguish denoising depth from sampling iterations, and derive graph and compute bounds. A reported sparse-expert configuration, denoted DualBudget, is analyzed across scientific summarization, multi-hop question answering, dialogue, and sentence-pair prediction. All supplied table measurements are retained. The length study shows gains over the listed baselines through 16K, together with measurable degradation as length increases. Ablations reveal mixed changes across the three reported scores, while the cost record indicates a 20% reduction relative to DiffuSeq under an unspecified timing convention. The analysis separates these observations from unmeasured claims about training speed, absorbing states, global coherence, and deployment memory.

---


### 103. [VariaFlow: Uncertainty-Aware Flow Matching for Unsupervised Anomaly Detection](https://arxiv.org/abs/2610.41494)

**<font color=#1a73e8>作者：</font>** Arnela Hadzic, Martin Urschler, Cosmin I. Bercea  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstruction-based anomaly detection no longer fails at reconstruction. Generative models produce high-quality pseudo-healthy reconstructions, and the remaining difficulty is the step of scoring residuals. The residual between a scan and its reconstruction has two indistinguishable sources, genuine pathology and the anatomical variation that separates one healthy brain from another. Scoring against a single reconstruction treats both as anomalous, inflating false positives where healthy anatomy varies most while small or subtle lesions are lost in the surrounding reconstruction error. We identify the missing quantity as the predictive variance, how much a healthy reconstruction can vary at each location. We introduce VariaFlow, which estimates this variance from an ensemble of mask-guided restorations under an unconditional flow matching prior, each started from a different noise initialization, and which normalizes the residual by the resulting standard deviation. Few-step flow matching keeps the ensemble computationally affordable, and restoring at two spatial scales captures lesions of different size. Across three brain MRI datasets spanning stroke and tumor, VariaFlow is trained once on healthy anatomy and generalizes across all three, attaining the highest AUROC (0.94, 0.80, 0.78) on each and the highest AUPRC on both cross-domain datasets, exceeding the strongest baseline by 37% and 50%. Under domain shift, the same baseline drops by up to 52% in AUPRC, whereas VariaFlow stays more stable and achieves the best small-lesion Dice on all three datasets.

---


### 104. [Altered Visual Hand Feedback in Virtual Reality: An Exploratory Study in Essential Tremor](https://arxiv.org/abs/2610.41496)

**<font color=#1a73e8>作者：</font>** Alejandro Pascual-Valdunciel, Marcos Sacristán-Moraleda, Verónica Giménez de Béjar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Pathological tremor is the most prevalent movement disorder worldwide, characterized by involuntary muscular oscillations within a frequency of 3 to 12 Hz. Despite extensive research, the underlying mechanisms that generate and modulate tremor are not yet understood, and treatments are usually insufficient. While it is known that visual feedback is an important afferent pathway, little is known about the impact of altering the hand's visual representation on tremor expression. With the development of immersive technologies, VR poses an excellent tool to study how alterations to the representation of the hands affect tremor. In this work, we study this through two complementary experiments. In the first one, we show that a consumer-level hand-tracking system substantially attenuates tremor-band movements without preventing successful task completion. In the second one, with eight patients with essential tremor, we observe task-dependent differences in physical tremor between VR and the real world, with several patients exhibiting lower tremor-band activity in both hand kinematics and muscle oscillations, particularly during reaching tasks. Our findings represent an initial step toward validating the use of VR as an experimental tool for the research and treatment of pathological tremor, while highlighting strong user- and task-dependent effects.

---


### 105. [VoxLution: Evolving Voxels for High-Fidelity 3D Scene Generation](https://arxiv.org/abs/2610.41501)

**<font color=#1a73e8>作者：</font>** Daoyi Gao, Xinyi Zhang, Alexey Bokhovkin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution 3D indoor scene generation is crucial for immersive applications such as virtual reality, spatial computing, and robotics simulation. We introduce VoxLution, a coarse-to-fine transformer-based approach that generates high-fidelity indoor scenes with rich details, overcoming the overly smooth geometry typical of existing generative models. First, we generate a low-resolution spatial layout; then, based on this structural information, we progressively refine the scene geometry locally in chunks. Key to our approach is formulating 3D super-resolution as a sequence modeling problem over multi-resolution sparse voxel grids. To achieve this, we introduce a training-free, resolution-invariant tokenization scheme that compactly encodes the geometric information of eight octants into a single decimal number. We formulate the transformer sequence to include multiple resolutions, allowing the coarse layout to guide the generation of fine local details. To ensure coherence across local chunks, we incorporate adjacent chunk boundary information directly into the transformer sequencing. VoxLution achieves scene generation at a finer voxel resolution than existing baselines, demonstrating state-of-the-art performance on standard benchmarks with 59.6% lower FPD and 51.1% lower FID on 3D-FRONT, and 70.5% lower FPD and 73.8% lower FID on Scannet++.

---


### 106. [PCD: Predictive Coding Dynamics for Irregularly Sampled Time Series](https://arxiv.org/abs/2610.41506)

**<font color=#1a73e8>作者：</font>** Tianrui Gou, Jiayangmei Xu, Xingzhou Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic systems evolve continuously over time, whereas observations in real scenarios are often sparse, irregular, and asynchronous. Accurate prediction therefore requires inferring latent state evolution between observations, as future values depend on partially observed trajectories. We propose Predictive Coding Dynamics (PCD), a residual feedback mechanism for irregular continuous dynamic models. PCD maintains previous reconstructions, predicts observed entries from them, and incorporates masked signed residuals into state recognition through an energy penalty. The mechanism is implemented with ODE-RNN and Latent ODE, supporting event-based hidden updates and latent state recognition. Experiments on forecasting and trajectory recovery tasks show that PCD improves continuous dynamic backbones under sparse and irregular sampling. The results further indicate that predictive error feedback improves latent state estimation when observations constrain the current trajectory. These results suggest that PCD provides a residual feedback framework that jointly supports trajectory generation, observation consistency checking, and state refinement in continuous-time series modeling. The source code is available at this https URL.

---


### 107. [Parameter-Efficient Fine-Tuning of Transformer Encoders for Audio-Image-Symbolic Music Retrieval](https://arxiv.org/abs/2610.41512)

**<font color=#1a73e8>作者：</font>** Eliseo Fuentes-Martinez, Antonio Hidalgo-Centeno, Jorge Calvo-Zaragoza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Score-based multimodal music retrieval requires representations that are both discriminative within each modality and compatible across audio recordings, sheet music images, and symbolic scores. This paper investigates the effectiveness of parameter-efficient fine-tuning (PEFT) for adapting pretrained music encoders and examines whether modality-specific improvements translate into better multimodal representations. We compare full fine-tuning, LoRA, and QLoRA across nine pretrained audio, image, and symbolic score encoders on TriScore and the Musical Theme Dataset. Encoders are first evaluated and selected through supervised unimodal classification, using frozen-encoder linear probing as a reference. We then introduce a controlled 2x2 design crossing encoder adaptation with task-specific shared projection, comparing frozen and adapted representations before and after projection. LoRA or QLoRA is selected in 14 of 18 modality-target combinations, frequently matching or outperforming full fine-tuning while optimizing substantially fewer parameters. However, these unimodal gains do not transfer uniformly to multimodal classification. Adaptation and projection are complementary for composer classification on TriScore, largely redundant for TriScore instrument and the Musical Theme Dataset instrument and ensemble tasks, and partially interfering for composer classification on the Musical Theme Dataset. The final adapted-and-projected title representation on TriScore supports piece-level retrieval, reaching average Top-5 and Top-10 accuracies of 55.32 and 64.68, respectively. Cross-modal exclusion and neighborhood analyses further reveal strong modality-specific local structure in the projected spaces. Overall, PEFT provides an effective and computationally efficient alternative to full fine-tuning, but improved unimodal discrimination alone does not guarantee better multimodal organization.

---


### 108. [Infinite ResNets are Gaussian Mean ODEs](https://arxiv.org/abs/2610.41514)

**<font color=#1a73e8>作者：</font>** Louis-Pierre Chaintron, Lénaïc Chizat, Javier Maass  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the training dynamics of deep neural networks in large-scale limits is a question both of foundational and of practical importance. Prior works have obtained such descriptions through dynamical mean field theory (DMFT), yielding a system of non-Markovian dynamics that are challenging to analyze and that obscure the optimization structure of the original dynamics. In this paper, we obtain instead a simple description of the large-scale limit training dynamics for ResNets in standard shape scalings and in the $1/\text{depth}$ branch scaling that allows maximal (local) feature updates. For a model trained with gradient descent (GD) from a random initialization, the limit dynamics is simply GD on a Neural Mean ODE with Gaussian initial weights. Our analysis covers population or empirical risk GD in the joint limit of large width, depth and embedding, input, and output dimensions. We obtain approximation scaling laws that depend on the shape of the ResNet and the covariance spectrum of the data. We also illustrate the flexibility of our approach by discussing Mixture of Expert models, where likewise the limit admits an intuitive (nested) Mean ODE description.

---


### 109. [Enhancing Sentiment Classification on Small Datasets through Data Augmentation and Transfer Learning](https://arxiv.org/abs/2610.41518)

**<font color=#1a73e8>作者：</font>** Mahmoud S. Mayaleh, Samer A. Mayaleh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small-scale sentiment classification often suffers from data scarcity, which limits the generalization ability of the models. This study evaluates and compares the effectiveness of three data augmentation strategies: Easy Data Augmentation (EDA), back-translation, and contextual token substitution (nlpaug-style), with both traditional machine learning classifiers (Logistic Regression, Random Forest) and transformer-based models (BERT). We perform a comprehensive empirical comparison with low-resource sentiment datasets by summarizing the results of recent studies and performing targeted head-to-head experiments. Our findings indicate that all augmentation methods improve performance. Contextual augmentation yields the most consistent gains for BERT models, while EDA and back-translation provide greater benefits for traditional classifiers. These insights help guide the selection of data augmentation techniques tailored to model type and dataset size, filling a critical gap in research on data augmentation for sentiment classification on small datasets.

---


### 110. [TACO: Trajectory-Aware Curvature Observation for Memorization Localization and Mitigation in Diffusion Models](https://arxiv.org/abs/2610.41520)

**<font color=#1a73e8>作者：</font>** Ruxi Gu, Zilei Wang, Wei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models can reproduce memorized training content within localized image regions, making precise localization essential for targeted mitigation. However, curvature observations at a single denoising state can contain transient responses, while spatially uniform mitigation may disrupt prompt-relevant content. We present Trajectory-Aware Curvature Observation (TACO), a unified framework for local memorization detection and mitigation in diffusion models. Our empirical analysis reveals that memorization-related curvature becomes pronounced during late-stage denoising and persists at consistent spatial locations across neighboring states. Motivated by these observations, TACO aggregates prompt-dependent curvature responses along the late denoising trajectory and applies latent-guided spatial refinement to improve spatial coherence. The resulting memorization map serves both as a localization signal and as a spatial control signal for mitigation. Specifically, TACO uses this map to steer existing inference-time interventions toward memorization-related regions through spatial reweighting and localized guidance correction. Extensive experiments demonstrate that TACO consistently outperforms competing localization methods, and improves the Pareto trade-off between memorization suppression, semantic alignment, and perceptual quality. These results establish trajectory-aware spatial analysis as an effective link between memorization localization and targeted mitigation.

---


### 111. [FOCUS: First-Order Control Using Optimal Transport Supervision for Imitation from Observations](https://arxiv.org/abs/2610.41540)

**<font color=#1a73e8>作者：</font>** João A. Cândido Ramos, Lionel Blondé, Hugues Vinzant 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imitation learning from observations must recover behavior from state-only demonstrations without known temporal correspondence. Differentiable simulators provide pathwise policy gradients, but differentiating through long, contact-rich trajectories can make optimization unstable. We introduce FOCUS, which combines local optimal-transport alignment with short-horizon differentiable actor-critic learning. FOCUS matches agent rollout windows to multiple sampled expert segments using a soft best-of-$K$ objective that emphasizes locally compatible matches. The resulting transport-based costs provide differentiable imitation rewards, while a learned critic bootstraps value beyond the rollout horizon. FOCUS requires neither temporally aligned trajectories nor expert-aligned initialization or teacher forcing. Across contact-rich locomotion tasks in DFlex, including a musculoskeletal humanoid controlled by 152 muscle activations, FOCUS improves sample efficiency and training stability over adversarial imitation-from-observation methods and prior differentiable imitation baselines.

---


### 112. [DeepWeave: Weaving Neural and Symbolic Evidence for ML-Based Network Intrusion Detection System](https://arxiv.org/abs/2610.41541)

**<font color=#1a73e8>作者：</font>** Raoul Saad, Enkeleda Bardhi, Andrea Agiollo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning-based network intrusion detection systems can recognize complex traffic patterns, but often require substantial labelled attack data, degrade under deployment shift, and provide limited evidence for analysts. We present DeepWeave, a probabilistic neuro-symbolic Network Intrusion Detection System (NIDS) that makes logic an integral part of detection. DeepWeave automatically constructs and validates interpretable rules, represents neural predictions as probabilistic predicates, and reconciles both evidence sources through explicit coupling policies over packet-, flow-, and hybrid-views. The resulting proofs provide intrinsic explanations for rule-supported alerts. Across multiple datasets, DeepWeave improves low-data detection, false-positive control, transferability, and robustness. With only 50 labelled packet observations per attack class, it improves macro-F1 from 0.632 to 0.924 and reduces the attack false-positive rate from 0.075 to 0.008 over the matched neural baseline. Its proofs are also more stable than post-hoc neural attributions, while batched inference keeps probabilistic reasoning practical. These results demonstrate label-efficient, adaptable, and inspectable neuro-symbolic intrusion detection.

---


### 113. [CEFR Level Assessment across Languages and Text Granularities](https://arxiv.org/abs/2610.41553)

**<font color=#1a73e8>作者：</font>** Eugene Matsumura, Yuki Arase  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic assessment of textual CEFR levels is an important task in educational natural language processing. However, accurate CEFR level prediction remains challenging due to the naturally imbalanced distribution of CEFR levels and the ambiguous boundaries between adjacent levels. To address these challenges, we propose a unified training objective that combines focal loss with supervised contrastive learning. Focal loss mitigates class imbalance by emphasizing underrepresented and difficult examples, while supervised contrastive learning learns more discriminative representations by encouraging intra-class compactness and inter-class separation. We evaluate the proposed method on sentence- and document-level CEFR assessment in both monolingual and multilingual settings. Experimental results demonstrate that our method consistently outperforms strong baselines across all settings, establishing new state-of-the-art performance on multiple CEFR assessment benchmarks.

---


### 114. [Digital sovereignty in professional translation workflows: a case study of migrating from Windows to Linux](https://arxiv.org/abs/2610.41561)

**<font color=#1a73e8>作者：</font>** Michael Farrell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines digital sovereignty in professional translation through a screening of computer-assisted translation tools and translation management systems, and a case study of migrating a translator's workstation from Windows to Linux. The framework combines three principles - Control, Continuity and Exit - with three practical requirements: native Linux operation, independence from mandatory external services, and independent access to essential data and resources. Drawing on documentary evidence and the limited number of responses received from providers, the ecosystem screening distinguishes Linux accessibility from operational independence: browser-based platforms may remain dependent on provider-controlled infrastructure. The migration case demonstrates the feasibility of reconstructing one professional workflow around a locally operable Linux core, using LoopCAT, LibreOffice and locally run TranslateGemma, alongside tools for optical character recognition, communication, credential management and backup. Selected cloud services remained available where needed. The findings suggest that digital sovereignty depends on how workflow dependencies are organized, rather than on individual applications or operating systems. It does not require technological isolation, but meaningful control over essential components, continuity of work and practical exit options. The framework is tailored to the case examined here and may require adaptation to other professional workflows.

---


### 115. [Poly Versus Polyval](https://arxiv.org/abs/2610.41565)

**<font color=#1a73e8>作者：</font>** Kaushik Nath, Palash Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We revisit the basic construction of polynomial evaluation based hash function, which we call Poly, over binary extension fields over $GF(2^n)$, where $n=64k$ and $k\geq 2$. Unlike GHASH, the NIST standard polynomial evaluation based hash function for $n=128$, Poly does not perform the unnecessary bit reversals of each $n$-bit block, and consequently is faster than GHASH. Further, Poly differs from Polyval, -- a faster alternative to GHASH, -- in that Poly performs usual reduction, while Polyval performs Montgomery reduction. We identify suitable choices of the field representing irreducible polynomials which makes usual and Montgomery reductions efficient. We provide detailed algorithms, and associated proofs of correctness for both kinds of reductions. Based on the algorithms, we report carefully optimised assembly implementation of both Poly and Polyval for $n=128,256$ and $512$. Our theoretical analysis and experimental timing results show that for $n=128$, Polyval is faster than Poly, while for $n=256$ and $512$ (as well as for higher values of $n$), Poly is faster than Polyval. The cases $n=128$ and $256$ are of current relevance due to the ongoing NIST process for developing cryptographic accordions.

---


### 116. [Connectivity-Aware Client Selection in Decentralized Federated Learning](https://arxiv.org/abs/2610.41570)

**<font color=#1a73e8>作者：</font>** Usevalad Milasheuski, Monica Nicoli, Stefano Savazzi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decentralized federated learning (DFL) has emerged as a scalable alternative to centralized federated learning, removing the single point of failure and communication bottleneck at the server. However, most existing decentralized approaches rely on full-neighborhood broadcasting, where each client transmits its model update to all of its neighbors in each communication round. While effective, this results in significant communication overhead and high energy consumption. This paper applies spectral graph tools as lightweight client selection methods that leverage the graph topology by analyzing the spectral properties of the graph Laplacian over a fixed communication graph. Specifically, we exploit eigenvector embeddings and heat/diffusion kernel similarities to guide each client in selecting only a subset of structurally relevant neighbors, i.e., those that are most beneficial for the convergence of the federation process. This topology aware randomization matches or outperforms uniform neighborhood subsampling and approaches the accuracy of full broadcasting. The largest gains, about $3$ percentage points, emerge under strong data heterogeneity on larger, structurally rich graphs, while the total number of transmitted messages is reduced by $50\%$ compared to naive broadcasting.

---


### 117. [Saidzoda-Tajik-LFM-2.6B: Adapting a 2.6B Hybrid Model to Tajik Tool Calling, and What Continued Pretraining Takes Away](https://arxiv.org/abs/2610.41576)

**<font color=#1a73e8>作者：</font>** Tohir Saidzoda, Nekruz Maxudov, Bedil Karimov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We release Saidzoda-Tajik-LFM-2.6B, a Tajik adaptation of the 2.6B-parameter hybrid model LFM2.5-2.6B-Base, built for tool calling in Tajik on modest hardware. The recipe has two stages: LoRA continued pretraining (CPT) on 1,485,319 cleaned Tajik web documents for 3 epochs, then one epoch of supervised fine-tuning (SFT) on a mix of machine-translated Tajik tool calls, English tool calls kept as replay, and Tajik instructions. On a 174-item tool-calling test set built from BFCL v3 and machine-translated to Tajik, strict full-call accuracy on Tajik prompts rises from 20.69 for the base model to 64.14 (paired difference +43.45 points, 95% interval +35.2 to +51.7); a lenient parser that also accepts the base model's own call formats puts the base at 31.72. English shows no detectable change (76.55 and 77.24). Every CPT checkpoint scores zero: CPT removes the native tool-call format and, as the lenient re-scoring shows, part of the skill itself. Outside tool calling, accuracy on a Tajik knowledge benchmark rises from 28.0 to 35.0, Belebele Tajik shows no significant change, and English MMLU falls from 60.8 to 52.5. The model is not a general Tajik assistant. It almost never declines when no tool fits (6.9% correct on Tajik, against 31.0% for the base under the lenient parser), it is weak at multi-turn calls, and its calls should be checked before they are executed. We describe the data, the training settings and every evaluation in enough detail to repeat them.

---


### 118. [Patch-Based Deep Kernel Learning for Data Assimilation and Bias Correction with Extremely Sparse Observations](https://arxiv.org/abs/2610.41596)

**<font color=#1a73e8>作者：</font>** Emanuele Mele, Angelo Coluccia, Massimo Cafaro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data Assimilation (DA) reconstructs the state of a spatio-temporal system by combining sensor observations with the output of a numerical model. Since model states are high-dimensional while observations cover only a small fraction of the domain, DA is a challenging large-scale estimation problem, central to weather forecasting and oceanography. Classical variational methods such as 3D-Var rely on a hand-crafted background error covariance that assumes unbiased errors, and therefore cannot capture state-dependent correlations or systematic model biases. Moreover, their cost grows with the size of the domain. Deep learning (DL) methods can perform DA and bias correction (BC) non-linearly, but typically offer limited interpretability and no calibrated uncertainty estimates. We propose a hybrid framework that couples a convolutional neural network (CNN) with a learnable-kernel Gaussian Process (GP) to jointly perform DA and BC from extremely sparse observations. The model is trained end-to-end by maximizing the marginal log-likelihood, learns a data-driven covariance over the whole grid, and provides both the Maximum A Posteriori analysis and its uncertainty by design. A patch-based strategy reduces the $O(N^3)$ training cost of exact GPs over $N$ grid points to $O(N)$ for a fixed patch size. Inference remains exact and only requires solving a linear system whose $O(m^3)$ cost depends on the number of observations $m \ll N$, not on the domain. The learned covariance can also replace the hand-crafted one in 3D-Var, improving its accuracy without changing the variational formulation. Experiments on sea surface temperature and salinity, with both synthetic and real, extremely sparse in-situ observations, show that the framework outperforms 3D-Var, a classical GP and a competing DL model, while reducing inference time by more than 98% with respect to 3D-Var.

---


### 119. [Scout-Refine-Correct: Teaching Flow Models to Refine Their Own Samples](https://arxiv.org/abs/2610.41598)

**<font color=#1a73e8>作者：</font>** Sergey Karpukhin, Aibek Alanov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The quality of image generation models trained with diffusion or flow matching is largely fixed by the training budget: at inference, the only available lever is the number of sampling steps, and additional steps improve quality only up to a point. We present a training recipe, Scout-Refine-Correct (SRC), that instead gives a flow-matching generator a genuine inference-time refinement capability. At each sampling step the model takes a scout rollout -- $K$ steps ahead along its own trajectory -- extrapolates a full-sample estimate, and feeds that estimate back to itself as a self-conditioning signal before taking the real step. This can be repeated for $R$ refinement rounds. Two correction losses, applied during training at states the model's own rollouts actually reach rather than only on the ground-truth path, teach the model to use this signal to reach new samples instead of collapsing to a suboptimal one. On ImageNet-256, SRC improves LightningDiT-B from FID~14.5 to FID~7.26 at NFE~550, matching a privileged best-of-$N$ baseline that uses an oracle FID verifier to choose among samples. SRC uses no external verifier, no reward signal, and, after ablation, almost no extra parameters over the base architecture. Combining SRC with best-of-$N$ improves the result further, to FID~3.81 at NFE~4400, showing that the two axes are complementary. We ablate the main design choices -- the architectural pathway for the scout signal, the scout horizon, each correction loss, and the training schedule to demonstrate key working components of training.

---


### 120. [DrawSplat: Atlanta World-Guided Implicit Gaussian SLAM for Indoor Reconstruction](https://arxiv.org/abs/2610.41602)

**<font color=#1a73e8>作者：</font>** Fan Zhu, Zhisong Xu, Ziyu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-D SLAM requires accurate online tracking, high-quality rendering, and geometrically consistent reconstruction. Existing Gaussian SLAM methods mainly optimize Gaussian primitives with photometric, depth, or local frame-to-model constraints, which are often insufficient in indoor scenes with weak textures, large planar structures, noisy depth, and long trajectories. The resulting maps may suffer from pose drift, surface thickness artifacts, noisy normals, and blurred structural boundaries. We propose DrawSplat, an Atlanta World-guided implicit Gaussian SLAM framework for indoor reconstruction. DrawSplat follows a drawing-like process: explicit point-line geometry first sketches the structural layout, and implicit neural Gaussians then fill in high-fidelity appearance and continuous geometric details. It estimates camera poses, sparse geometry, and gravity direction through point-line joint tracking, infers structural planes from tracked lines using the shared-gravity component of the Atlanta World prior, and converts them into differentiable regularization terms on Gaussian centers and normals. To improve compactness and efficiency, DrawSplat further combines an anchor-based implicit neural Gaussian representation with adaptive structural sampling, which allocates Gaussian capacity to structurally informative regions. Experiments on multiple datasets show that DrawSplat achieves robust tracking, high-fidelity rendering, and strong geometric reconstruction among Gaussian-based SLAM systems, while maintaining a practical balance among quality, efficiency, and model size.

---


### 121. [Chance-Constrained Inspection Viewpoint Sequencing for On-Orbit Servicing via Safe Reinforcement Learning](https://arxiv.org/abs/2610.41639)

**<font color=#1a73e8>作者：</font>** Chloé Carer, Adam Abdin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous inspection of a target spacecraft is typically the initial step in on-orbit servicing. Planning close-proximity observation viewpoints involves a complex combinatorial problem constrained by coverage, fuel, and safety considerations. This paper models the viewpoint selection as a Constrained Markov Decision Process (CMDP) and applies Proximal Policy Optimization with Lagrangian relaxation to solve it. The system combines a high-level planner, which sequences camera viewpoints on an observation sphere around the target, with a low-level model that assesses each transfer using the Clohessy--Wiltshire (CW) equations for relative motion. The deterministic constraints on single-impulse reachability and $\Delta v$ cap are enforced directly on the action set. Safety margins are affected by navigation and manoeuvre errors, making the actual clearance stochastic. To address this, a chance constraint on the realised trajectory is implemented, with a Lagrangian multiplier governed by PID control to adapt the penalty during training. The approach is tested on a Galileo-class navigation satellite in medium Earth orbit, modelled as a point cloud where visibility from each viewpoint considers field-of-view and line-of-sight occlusion. Across various risk budgets, the trained policy maintains the keep-out violation rate within the specified limit, achieving coverage close to its maximum and staying within the mission $\Delta v$ budget. Compared to the usual practice of applying a fixed margin to the keep-out radius and planning deterministically, the chance-constrained policy attains less than half the violation rate at comparable coverage. This makes the collision risk an explicit design parameter, eliminating the need for re-tuning per case. The learned policy selects a viewpoint without the repeated Monte Carlo risk estimates required by a greedy, chance-constrained planner at every decision point.

---


### 122. [A Constructive Orbit-Based Theory of Learnability](https://arxiv.org/abs/2610.41641)

**<font color=#1a73e8>作者：</font>** Yunied Puig  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a finite-dimensional orbit framework for constructing data-adapted dictionaries, sparse realizations, and predictive extensions. The method uses wrapped weighted shifts to generate orbit dictionaries and local interpolation maps from independent orbit representatives, turning the learning problem into three explicit tasks: scaffold discovery, sparse realization on the discovered dictionary, and prediction through learned sparse coordinates. We introduce CCDS as the main constructive ingredient: a deviation-controlled sparse realization procedure that recovers MP/OMP-type behavior at the minimal-deviation boundary while allowing feasible interior paths with prescribed residual geometry that is inaccessible to MP/OMP. We prove generic orbit independence, exact block interpolation with norm control, observable bounds on sparse approximation distortion, sparse realization guarantees on selected supports, and fixed-path stability under admissible perturbations of the block interpolants. These results connect sparse approximation, interpolation, and finite-dimensional operator dynamics through the construction and analysis of data-induced orbit dictionaries. Experiments on synthetic geometry, controlled realization tests, and standard classification benchmarks show that selected orbit scaffolds have substantially better matched-rank projection behavior than random orbit or unstructured alternatives, that CCDS attains near-zero realization error at the minimal-deviation boundary, and that predictors trained from the sparse CCDS certificates give competitive performance.

---


### 123. [TADP: Dual-Branch Temporally Adaptive Differential Privacy for Expression-Aware Video Anonymization](https://arxiv.org/abs/2610.41642)

**<font color=#1a73e8>作者：</font>** Feng Xu, Xun Li, Lars Petersson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present TADP, a temporally adaptive differential privacy (DP) framework for inference-time privacy-preserving video generation under fixed-length clip-replacement adjacency. TADP uses a dual-branch design to extract identity and expression representations, clips and privatizes both branches with temporally adaptive Gaussian mechanisms whose noise scales depend only on preceding privatized releases within the same clip and are bounded below by history-uniform calibrated minima, and accounts for their joint release via adaptive Rényi Differential Privacy (RDP) composition. The clip-level RDP guarantee is converted to $(\varepsilon,\delta)$-differential privacy, while soft quantization and subsequent temporal processing are applied only after privatization as DP post-processing. Experiments on facial expression datasets show reduced identity leakage under evaluated attacks, usable perceptual quality and temporal stability, and high facial expression recognition utility relative to the evaluated privacy-preserving baselines. TADP formally satisfies clip-level DP and empirically provides a favorable privacy--utility trade-off under the evaluated threat models and datasets.

---


### 124. [Look Over There! Dynamic Visual Guidance for AI-Narrated Slides](https://arxiv.org/abs/2610.41645)

**<font color=#1a73e8>作者：</font>** Jiongning Allen Lian, Yutong Alison Mei, Ho Ting Cheung 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Slides present information spatially, but narration unfolds linearly, leaving the viewer struggling to locate what the narration refers to. This split attention between audio and visual channels forces viewers to search the slide manually, imposing extraneous cognitive load and disrupting comprehension. The problem is especially acute on mobile devices, where dense layouts compressed onto small screens make visual search particularly effortful. In teacher-led settings, however, instructors naturally direct attention through pointing, pacing, and emphasis. Inspired by this, we present GuideSlide, a system that automatically generates Dynamic Visual Guidance for slide presentations, providing viewers with narration-synchronized visual cues that direct attention in real time. Given a PDF slide deck, GuideSlide automatically produces region-level zoom and time-aligned highlights without manual annotation. In a within-subjects study with 24 participants, GuideSlide substantially reduced perceived cognitive load and yielded higher immediate comprehension scores compared to static slides with identical narration. Participants strongly preferred the Dynamic Visual Guidance condition, reporting that it made narration easier to follow and reduced uncertainty about where to look. These findings suggest that narration-synchronized visual guidance is a valuable design strategy for slide-based presentations, with potential to extend to other instructional and presentation scenarios.

---


### 125. [Risk-Sensitive Mission Planning for Multi-Target On-Orbit Inspection via Distributional Reinforcement Learning](https://arxiv.org/abs/2610.41647)

**<font color=#1a73e8>作者：</font>** Adam Abdin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-target on-orbit servicing missions require planning tools that can adapt to evolving operational conditions while accounting for the outcome variability inherent to safety-critical spaceflight. This paper presents an adaptive planning approach for multi-target servicing campaigns in low Earth orbit and applies it to inspection missions flown by a low-thrust servicer. The approach is based on Distributional Reinforcement Learning, which learns the full distribution of mission returns and thereby supports explicit risk-sensitive decision-making at each planning step. Specifically, a Quantile-Regression Deep Q-Network (QR-DQN) agent selects which target to inspect next by jointly considering the expectation and the variance of the predicted return through a mean-variance criterion. The mission environment models circular orbits with a spread in inclination and uses Edelbaum's combined-manoeuvre low-thrust transfer estimates. The observation comprises the orbital elements, the visit history, the observed risk state of each target and the remaining mission-time budget. The risk state of each target changes stochastically during the campaign, making the outcome of an inspection uncertain and creating operationally meaningful distinctions between risk-neutral and risk-averse planning strategies. Because the mission-time budget generally admits only a subset of the candidate targets, the planner must also select which targets to inspect. Numerical experiments on scenarios with five target satellites show that one risk-aversion weight moves the policy across a range of mean return and return variance, over an unchanged environment and reward. Risk-averse agents reduce the variance of the episodic return by approximately one half relative to risk-neutral agents and lower the probability of a mission loss, at a cost in mean return. To validate the learned policies, the efficient frontier, which gives the highest mean return attainable at each level of return variance, is computed exactly by enumerating the admissible visit orders. At equal variance, the learned policies lie close to this frontier in mean return, and the risk-averse policies have a lower probability of a mission loss than the frontier policies.

---


### 126. [On the Generation Order in GFlowNets](https://arxiv.org/abs/2610.41648)

**<font color=#1a73e8>作者：</font>** Timofei Gritsaev, Evgeny Katasonov, Ildus Sadrtdinov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from discrete distributions specified by unnormalised probability functions is a classical statistical problem. GFlowNets address this problem by constructing objects sequentially, adding one discrete component at a time in either a predefined or a learned order. The choice of order determines which conditional distributions the neural network must learn, some of which may be easier to learn than others. Yet whether existing GFlowNet algorithms discover interpretable generation orders and make use of them during training remains unexplored. We introduce controlled problems where generation order is experimentally shown to affect convergence and standard GFlowNet training struggles to discover useful orders. To address this difficulty, we develop Learning-Order GFlowNet, a training recipe that learns interpretable generation orders without order annotations and improves convergence on these problems. Finally, we investigate gradient signal-to-noise ratio (SNR) as a possible explanation for order emergence: orders associated with faster convergence exhibit higher SNR at comparable validation loss, suggesting both a mechanism favouring their emergence and an SNR-based characterisation of a good generation order.

---


### 127. [Fooling Relying Parties of the EUDI Wallet Architecture: Credential Pooling Attacks and CRESTA, a Standard-Compliant Countermeasure](https://arxiv.org/abs/2610.41655)

**<font color=#1a73e8>作者：</font>** Leonardo Rufini, Ivan Visconti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The European Digital Identity (EUDI) Wallet will let millions of EU citizens prove who they are and what they are entitled to, disclosing only what is needed. Many services need several credentials at once, such as an identity card and a university degree, so combined presentations are essential.
We present credential pooling attacks on relying parties of the EUDI Wallet reference architecture. Colluding users, each holding some credentials in their own wallet, cooperate through a proxy that acts as a single synthetic user and presents all the requested credentials, although no single user holds them all. Every signature is genuine and computed by certified hardware, and nothing is extracted or forged. We ran the attack against the European Commission's reference implementation, also on two Android phones.
The attack would fail if all credentials of a user carried the same public key, but colluding relying parties could then link all presentations of that user. For this reason, the Architecture and Reference Framework (ARF) requires a fresh key for each credential and recommends batches of single-use copies, each with its own key: precisely what makes pooling possible. One might think that preventing pooling requires giving up unlinkability or adopting non-standard cryptography, such as zero-knowledge proofs.
We show that this is not the case: we present CRESTA (CREdential STApling), an efficient countermeasure that uses only standard cryptography and credential formats and preserves unlinkability. In CRESTA, an ordinary issuer checks at issuance that a set of keys was generated in the same secure hardware, and certifies it in a binding attestation: a standard credential whose attributes can be selectively disclosed. CRESTA works entirely within the EUDI Wallet framework and costs a relying party one additional signature verification per presentation.

---


### 128. [A Self-Supervised Pose Estimation Approach for Construction Machines](https://arxiv.org/abs/2610.41673)

**<font color=#1a73e8>作者：</font>** Alaa Alshubbak, Daniel Görges  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose estimation is a computer vision task used to estimate a skeleton of dynamic systems to predict future movements. Most of the research in this direction is based on a supervised learning approach which requires a massive amount of labeled datasets. In this paper, a self-supervised three-stage model based on a contrastive learning approach is introduced for estimating a skeleton of dynamic construction machines; such as excavators without using any labeled images for the first stage. The whole model structure is divided into three stages: the pre-train stage using the SimCLR contrastive approach, and two fine-tuning stages for the transfer learning and the downstream task. The model can leverage the features and learn from a huge unlabeled dataset called ACID to two small datasets generated from NVIDIA Isaac and MATLAB Simscape simulators as well as transfer the knowledge to a smaller dataset with a ratio of 3.5% from the original ACID dataset. The results show that the proposed approach can improve the accuracy of pose estimation for heavy construction machines in real images by 11% and 13% in comparison to the normal self-supervised approach with two backbones ResNet-50 and HRNet-W32, respectively.

---


### 129. [Radial Kernel Attention for Long-Range Modeling in Polymer Machine Learning Force Fields](https://arxiv.org/abs/2610.41675)

**<font color=#1a73e8>作者：</font>** Wenbo Fu, Chenghui Mao, Chengwen Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Radial Kernel Attention (RKA) for long-range modeling in polymer machine learning force fields. Local neighbor graphs constrain communication across polymer chains and their surrounding environments, while explicit all-pair attention incurs quadratic cost. RKA maps atomic distances from the cluster centroid to learned radial features and combines their overlap with content-dependent queries and keys. Factorized aggregation and readout enable global feature exchange at linear cost in atom count for fixed feature dimensions. We insert the invariant scalar update between EquiformerV3 local blocks and obtain conservative forces by differentiating the total energy, including its radial coordinate dependence. We evaluate energy and force prediction for finite polymer-derived clusters in OPoly26. Our models are trained on the official training split for 12 epochs and evaluated directly after training on the complete official validation split. A matched 5M comparison shows that RKA reduces per-atom energy and force MAEs by 67.4% and 36.3%, respectively. The 20M RKA model is compared with UMA-S-1.2 and UMA-S-1.2.1 on the same validation structures. The 20M model attains a total-energy MAE of 15.81 meV and a force MAE of 2.619 meV/angstrom; its per-atom energy MAE is 0.1182 meV/atom. RKA provides a compact global communication pathway that improves energy and force prediction on the evaluated polymer-derived clusters.

---


### 130. [OT-CAL: Optimal-Transport-Guided Adaptive Sample Selection for Efficient Visual Learning](https://arxiv.org/abs/2610.41677)

**<font color=#1a73e8>作者：</font>** Suryansh Talukdar, Jin Soung Yoo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks for image recognition are typically trained using mini-batches, with a forward pass to compute predictions and losses followed by a more computationally expensive backward pass to update model parameters. However, not all training samples contribute equally to learning, suggesting that computation can be reduced by performing backward passes only on informative samples. The challenge is that sample informativeness changes throughout training: difficult samples may be valuable early on, improving samples become important later, and class diversity becomes increasingly relevant toward the end. Existing methods often rely on fixed selection rules or computationally expensive per-sample gradient calculations. We propose OT-CAL, an adaptive data selection method that automatically adjusts its sampling preferences during training. OT-CAL represents each sample using five informativeness features, including difficulty, learnability, and uncertainty. A curriculum vector describes the currently preferred sample characteristics, and optimal-transport-based matching assigns selection weights according to how closely samples match this target. The curriculum vector is then updated using the selected samples, forming a feedback loop that adapts without a manually defined schedule. Experiments on three standard visual learning benchmarks show that, when selecting 50% of each mini-batch, OT-CAL improves performance by 1.3--2.1 points over AdaSelection while achieving 1.18--1.24 times faster training than full-data training.

---


### 131. [Designing wearable haptic cueing for neurological gait rehabilitation: user requirements across residential care and community settings](https://arxiv.org/abs/2610.41680)

**<font color=#1a73e8>作者：</font>** Riasat Islam, Annemarie Zijlema, Theodoros Georgiou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wearable haptic cueing offers rhythmic prompts for neurological gait rehabilitation while leaving hearing available for communication and environmental awareness. We investigated the user, design, and implementation requirements needed to make these systems usable in practice. We analysed six linked studies involving 17 people with neurological conditions affecting gait and three physiotherapists across formative sessions, residential care, and community self-management. Wearable devices served as technology probes. Observations, interviews, diaries, physiotherapist records, gait analysis, and activity logs informed thematic analysis and cross-study comparison. Seven recurring requirement areas concerned haptic perceptibility and placement, wearability and fastening, interaction burden, rhythm personalisation, real-world walking contexts, supported use, and perceived value beyond gait outcomes. Requirements interacted: perceptible cue locations could be difficult to access for fastening or control, while fixed rhythms did not always accommodate terrain, fatigue, interruptions, or changing pace. Carers and clinicians supported configuration, operation, safety, and interpretation. Participants described confidence, routine formation, and willingness to walk; these accounts were interpreted as perceived value rather than evidence of therapeutic efficacy. Low sensation, cognitive burden, and mobility limitations could make wearable cueing impractical. Future systems should offer adjustable haptic output, flexible placement, accessible fastening, simple controls, personalised rhythms, and robustness during everyday walking. Design should accommodate support from carers and clinicians and consider trade-offs between requirements. These findings inform wearable rehabilitation design rather than establish clinical efficacy.

---


### 132. [From WSIs to Bulk, Spatial and Single-Cell Transcriptomics via Multi-Scale Graph Neural Networks](https://arxiv.org/abs/2610.41692)

**<font color=#1a73e8>作者：</font>** Miguel Andrade, José Almeida, Carlos Santiago 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the spatial distribution of gene expression is key to studying complex diseases like cancer. While Spatial Transcriptomics (ST) and Single-Cell Transcriptomics (scT) provide high-resolution insights, they remain expensive and scarce. In contrast, standard histopathology Whole-Slide Images (WSIs) paired with bulk RNA sequencing are widely available. This work introduces a Multi-Scale Graph Neural Network (GNN) capable of simultaneously predicting bulk, spatial, and single-cell transcriptomics directly from WSIs. By extracting morphological features using a Pathology Foundation Model (PFM) (UNI2-h) and constructing spatial graphs at both patch and cell levels, the model learns the hierarchical relationships within the tissue. The network is trained on a combined dataset of The Cancer Genome Atlas Program (TCGA), Visium, and Xenium samples across lung, kidney, and breast tissues. A hybrid training strategy is employed, leveraging direct supervision alongside weakly supervised consistency losses to ensure predictions align across biological scales. Results show the model accurately predicts gene expression at the slide level and moderately at the patch level (strongest on Xenium), and achieves moderate correlation at the challenging single-cell level. Furthermore, downstream tasks explore the clinical relevance of these predictions, demonstrating their utility in survival analysis, spatial hazard mapping, and tumor classification via molecular signatures.

---


### 133. [Retrieval-Augmented Initialization with Dual-Guided Inversion for Flow-Based Inverse Problem Solvers](https://arxiv.org/abs/2610.41695)

**<font color=#1a73e8>作者：</font>** Hansam Cho, Seoung Bum Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow models have recently emerged as powerful generative priors for solving inverse problems. Despite their success, most existing flow-based inverse problem solvers initialize the reconstruction process with random Gaussian noise. However, recent studies in image generation have shown that the choice of initial noise can significantly influence generation outcomes. The role of initialization as a distinct design choice in flow-based inverse problem solving remains comparatively underexplored. In this work, we systematically evaluate noise initialization strategies while holding the downstream flow-based inverse solver fixed. We propose Retrieval-Augmented Initialization with Dual-Guided Inversion (RA-DGI), a method that constructs improved initial noise by leveraging retrieved proxy clean images and dual-guided inversion. Extensive experiments across multiple inverse problems demonstrate that the quality of the initial noise substantially affects reconstruction fidelity and perceptual performance. RA-DGI outperforms standard random initialization and achieves superior results compared to inference-time scaling strategies, while requiring less computational overhead. These findings highlight initialization as a critical yet previously overlooked factor in flow-based inverse problem solvers.

---


### 134. [From fleet trajectories to single-cell promises: hierarchically weighted conformal prediction for battery SOH monitoring](https://arxiv.org/abs/2610.41696)

**<font color=#1a73e8>作者：</font>** Xiangyu Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interval predictions from conformal prediction are usually read as "90% coverage", but on nested battery data that number promises the fleet average, not the individual cell. We measure the gap on 124 public LFP cells under a preregistered three-tier reporting protocol (fleet, batch, cell): pooled coverage looks healthy (0.875-0.906 across splits) while the worst cell is covered 0.1-2% of the time, with exact binomial tests against the nominal level. We then repair part of the gap with a hierarchically weighted conformal engine whose weights consume only side information frozen at prediction time - signature features, batch labels, cycle indices - and never touch residuals. The preregistered repair criterion passes: 10th-percentile cell coverage moves 0.750 to 0.830 (53% of the gap), the worst cell 0.642 to 0.694, with zero deferrals and a flat sensitivity spectrum. What the engine does not repair is localized rather than left open: under protocol drift the frozen weights harm monotonically on the SOH scale (the absolute scale is reported in full), a structural dead end we report instead of tuning away; and repair capacity is bounded by calibration-pool battery diversity, measured on both datasets. On a cross-chemistry external set the calibrated intervals collapse (0.286), while the within-domain skeleton replicates (pooled 0.933, worst cell 0.686). The deliverable is a reporting protocol - three tiers of promise anchored to measured regimes, worst-cell statistics, deferral share - that makes per-cell interval claims auditable before deployment.

---


### 135. [Nereus: A Large-Scale Underwater Dataset for Fine-Grained Attribute Understanding and Grounded Counting Perception](https://arxiv.org/abs/2610.41705)

**<font color=#1a73e8>作者：</font>** Jingtao Deng, Zihao Jin, Yuehe Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater imagery records rich ecological information and supports applications such as science communication, fishery monitoring, ecological conservation, and oceanographic research. Beyond general scene understanding, these applications require models to recognize fine-grained biological traits and reason over spatially grounded evidence. However, existing underwater datasets often provide coarse category labels, generic captions, or total-count supervision, which limits their use for organism-level analysis and ecological reasoning. We introduce Nereus, a large-scale dataset for Underwater Fine-grained Perception that jointly supports Fine-Grained Object Attribute Understanding and Grounded Counting Perception. Nereus contains 88K images and 2.68M question-answer pairs, including annotations for 136K marine organism objects across 2,690 species and 1,515 genera, as well as 65K point annotations and 67K grounded counting QA pairs. Experiments with representative multimodal models show that Nereus improves downstream adaptation over existing underwater-domain data and provides a foundation for future research on fine-grained marine perception.

---


### 136. [Hierarchical Residuals: A Minimalist Decoupling of Residual Width from Compute Width](https://arxiv.org/abs/2610.41711)

**<font color=#1a73e8>作者：</font>** Ziteng Wang, Jianqiao Lu, Xinyu Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual connections underpin Transformers, but they implicitly tie the residual width carried through depth to the compute width used inside each layer. We introduce Hierarchical Residuals (HiRes), a minimalist architectural change that decouples these dimensions, widening the residual state while keeping per-layer compute width fixed. HiRes groups layers into blocks: standard d-dimensional PreNorm layers operate inside each block, while a wider D-dimensional PostNorm outer residual connects blocks. Learned read/write projections bridge the two spaces at block boundaries, leaving individual Transformer layers unchanged. Across different model sizes and depths, HiRes consistently outperforms vanilla residual addition, with fitted scaling laws indicating a 1.30-fold improvement in FLOPs efficiency. On OLMoE-1B-7B pretraining for 500B tokens, HiRes achieves 0.0208 lower training loss and 1.14-point higher downstream accuracy. HiRes is also competitive with other residual expansion methods such as VWN, mHC and AttnRes with less activation memory and I/O costs. Built from only dense projections and normalizations, it requires neither specialized kernels nor infrastructure-level optimizations. HiRes thus exposes residual width as a practical scaling variable using only standard operators.

---


### 137. [SAR-TS-BERT: Physics-Guided Self-Supervised Pre-Training With Polarimetric Features for SAR Time-Series Crop Classification](https://arxiv.org/abs/2610.41728)

**<font color=#1a73e8>作者：</font>** Jieqiu Wang, Yuhan Zhang, Bo Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multitemporal synthetic aperture radar (SAR) imagery provides continuous, cloud-free observations of crop phenology for agricultural monitoring in cloudy and rainy regions, yet high-accuracy classification typically requires extensive labeled samples. Although self-supervised pre-training mitigates label dependency in remote sensing, existing frameworks primarily target optical imagery or generic spatial SAR scenes, underutilizing temporal backscatter dynamics and polarimetric scattering mechanisms. We propose SAR-TS-BERT, a physics-guided BERT-style self-supervised pre-training framework for SAR time-series crop classification. SAR-TS-BERT integrates backscatter intensities and polarimetric ratio features (VV, VH, and VV/VH) with dual-polarimetric Cloude-Pottier decomposition parameters ($H/\alpha/A$) into a six-band input representation through two core designs: 1) a physics-guided span masking strategy (SpanPhysics) that adaptively selects contiguous masked spans based on temporal backscatter change rates to prioritize key phenological transitions; and 2) a dual-branch cross-modal fusion encoder that models backscatter and polarimetric decomposition features through separate Transformer branches followed by bidirectional cross-attention fusion. On independent test sets in Estonia (EuroCropsML) and the USA (California CDL), SAR-TS-BERT achieves overall accuracies (OAs) of 96.78% and 87.29%, respectively, and attains a mean monthly OA of 99.37% on Chongming Island, Shanghai. On the Estonia benchmark, pre-training improves OA and Macro F1 by 1.17 and 1.59 percentage points over training from scratch under full supervision, and by 2.58 and 5.19 percentage points using only 1% labeled data. Incorporating SAR scattering physics into temporal self-supervised pre-training effectively enhances crop classification accuracy, parcel-level mapping consistency, and few-shot transferability.

---


### 138. [Leakage-Controlled Structure-Preserving Augmentation and Template-Aware Evaluation for Bangla Symptom-Based Disease Prediction](https://arxiv.org/abs/2610.41733)

**<font color=#1a73e8>作者：</font>** Sabah Nushra, Shovan Samanta Turzo, Moinul Hossain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bangla symptom-based disease prediction is commonly evaluated on a small, imbalanced structured benchmark containing many profiles that differ by only one or two symptoms. We test whether train-only asymmetric Bernoulli perturbation improves classification using 725 unique profiles spanning 85 diseases and 172 binary symptoms. Experiments use ten repeated real-profile holdouts and parent-grouped inner cross-validation. The 2 x 2 design separates augmentation from hyperparameter tuning, with exact duplication, random oversampling, class weighting, and SMOTEN as balancing controls. For Bernoulli Naive Bayes (BNB), the gain over tuned raw training does not withstand Holm correction, although BNB attains the highest mean accuracy (97.50%). The boosted-tree models benefit substantially: XGBoost, LightGBM, and CatBoost improve by 18.10, 28.45, and 10.09 percentage points, respectively. A Hamming-distance audit places 91.0% of standard held-out profiles within one symptom bit of the training data. Accuracy decreases on a same-disease 1-bit-purged challenge; nevertheless, XGBoost and LightGBM retain large augmentation gains. We also evaluate robustness to missing and spurious symptoms and the faithfulness of BNB explanations. Overall, Bernoulli perturbation is useful for some model families, but benchmark accuracy should be interpreted together with template proximity.

---


### 139. [Locality-Controlled Out-of-Distribution Guidance for Robust Regulatory DNA Sequence Design](https://arxiv.org/abs/2610.41736)

**<font color=#1a73e8>作者：</font>** Dabin Jeong, Marwane Bourdim, Mo Lotfollahi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing regulatory DNA sequences for targeted gene-expression control is an important challenge. Recent approaches frame this task as property-conditioned generation, where diffusion models trained on natural sequences are guided toward high predicted activity through reward-based fine-tuning or sampling-time guidance. We show that single-reward evaluation can obscure reward-hacking behavior. By decomposing evaluation into property, novelty, and plausibility, we identify an empirically underexplored region of the evaluation space in which all three objectives are satisfied, but no existing baseline succeeds. We postulate that this gap arises because prior methods treat guidance primarily as a matter of magnitude. In regulatory DNA, however, sequence grammar is spatially nonuniform: motif positions are sensitive to perturbation, while background regions allow more exploration. We therefore propose LOCOGEN by reformulating guidance as a problem of locality. LOCOGEN learns an invariant motif mask through sequence-level invariance learning to protect motif positions, while applying OOD damping only to background positions. It operates at sampling time on a frozen diffusion backbone, without retraining the backbone. Across HepG2, K562, and SK-N-SH, LOCOGEN reaches this previously underexplored region of the property-novelty-plausibility space. Code is available at this https URL.

---


### 140. [Measuring What Matters: A Causal Reliance Score for Histopathology Image Segmentation](https://arxiv.org/abs/2610.41763)

**<font color=#1a73e8>作者：</font>** Samuel Thomas, Daniel Tweneboah Anyimadu, Ahmed Karam Eldaly 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable histopathology segmentation requires models that rely on pathology-relevant structures rather than spurious background correlations. In this work, we argue that improving architectures alone is insufficient if models continue to rely on spurious correlations rather than pathology-relevant features. We introduce a causality-inspired evaluation framework based on controlled interventions that explicitly probes model sensitivity to foreground tissue structure and background/domain variation. Building on this, we propose the Causal Reliance Score (CRS), a metric that quantifies the relative sensitivity of model predictions to foreground perturbation versus background/domain variation under controlled interventions. To support this analysis, we design augmentation strategies that act as implicit counterfactual interventions during training, encouraging invariance to nuisance factors while preserving morphology. We demonstrate how these interventions reveal behavioural differences between models that are not captured by standard metrics such as Dice or IoU. While we instantiate our framework using a self-supervised transformer (CAUSE-ViT), the primary contribution of this work is not a new architecture, but a principled intervention-based methodology and evaluation metric for auditing model behaviour in medical image segmentation. Our results suggest that evaluating model behaviour through counterfactual interventions is essential for developing reliable and clinically robust medical image segmentation systems.

---


### 141. [WorkIng: A Real-World and Synthetic Highway Work-Zone Benchmark Dataset for Autonomous Navigation](https://arxiv.org/abs/2610.41772)

**<font color=#1a73e8>作者：</font>** Xujun Xie, Dominik Rößle, Adithya Mohan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Highway work zones are critical edge cases for autonomous vehicles (AVs), combining atypical geometries and jurisdiction-specific regulations that existing benchmarks fail to capture: real-world datasets lack 360° multi-modal, full-scene 3D work zone annotation, and no single recorded site can span the layouts and regulatory variants needed for generalizable models. We present WorkIng, a dual-domain benchmark and training resource. WorkIng-Highway provides a 360° multi-modal work zone benchmark with synchronized 128-channel LiDAR, six RGB cameras, and RTK-GPS across 32 km, yielding 12,000+ annotated frames and 227,399 tracked 3D bounding boxes. WorkIng-CARLA complements this with procedural simulation spanning 24 regulation-aware scenarios across six canonical topologies and six international traffic standards, populated by 100+ custom 3D assets. Benchmarking representative 3D detection and end-to-end planning architectures shows that real-world data remains the primary performance driver, and that scenario-stratified synthetic augmentation improves architectures across 2D recognition, 3D detection, and trajectory planning. Resources: this https URL

---


### 142. [MERIDIAN: Memory-Encoded Rituals for Intimacy across Distance in an Interactive, Asynchronous Neighbourhood](https://arxiv.org/abs/2610.41776)

**<font color=#1a73e8>作者：</font>** Jingyi Chen, Yifan Yang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> How can shared memories become playable structures for partners who live in different time zones? We present MERIDIAN, a pre-deployment design case of Yi Town, a bilingual browser game developed by one member of a long-distance couple as a gift for the other. Nine levels translate personally meaningful events, places and cultural references into tasks within a navigable pixel town. A birthday prologue and a fictional wedding frame the intended experience. Drawing on research through design, we reconstruct four design changes from 109 development commits, 28 changelog versions and three design specifications. These records support six situated design commitments, including memory-derived mechanics, staged access, local progress storage and bilingual coverage. The implementation combines a union-based progress model with manually exchanged, checksummed codes and time-zone-dependent scenery. An implementation audit reproduced 153 passing unit tests and examined all 1,024 canonical progress codes, while identifying limits involving resets, unversioned level registries and residual transcription errors. The application has no author-operated backend for progress, but external media services and browser speech recognition limit its privacy and offline guarantees. No recipient evaluation or relationship outcomes are reported. The contribution is an inspectable account of design decisions and their trade-offs, including the tension between authoring a personal gift and preserving the recipient's freedom to interpret, decline or reshape it. The game is playable at this https URL and its source is public at this https URL.

---


### 143. [Clinical-Protocol-Aware Cyber Resilience for Connected Clinical Technologies Under AI-Enabled Adversarial Conditions](https://arxiv.org/abs/2610.41784)

**<font color=#1a73e8>作者：</font>** Pranav Patel, Siva Kannathasan, Prerak Patel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare increasingly relies on connected medical devices, clinical information systems, cloud services, and distributed-care technologies, creating cybersecurity risks across clinical workflows. AI-enabled capabilities can accelerate vulnerability discovery and attack-path analysis, increasing the need to limit compromise propagation. This paper proposes a clinical-protocol-aware cyber-resilience framework based on bounded clinical micro-networks and controlled interconnections. The framework integrates clinical factors into cybersecurity design, management, and evaluation, covering prevention, containment, and incident response. A parameterized Monte Carlo simulation distinguishes technical cyber exposure from modeled clinical consequence. Experiments investigate architectural connectivity, adversarial capability, security controls, protocol dependency, risk alignment, communication directionality, lifecycle integration, and response timing. Under the simulation assumptions, connected architecture increases mean cyber exposure by 56.3% relative to segmented architecture, while combined prevention and containment reduce exposure by 60.1% relative to no controls. Increasing protocol dependency raises the modeled clinical-impact index from 1.021 to 7.567 without changing mean cyber exposure, demonstrating that technical exposure and clinical consequence can diverge. Risk-alignment experiments further indicate higher modeled clinical impact when greater technical risk corresponds to greater clinical significance. The findings support comparative architectural analysis, not calibrated estimates of real-world cyber risk, control effectiveness, or patient harm. The framework provides a clinical-context-aware approach to security-boundary design, control prioritization, and coordinated containment in connected healthcare environments.

---


### 144. [Hard Sample-Conditioned Decorrelated Attention for Robust Face Recognition](https://arxiv.org/abs/2610.41789)

**<font color=#1a73e8>作者：</font>** Tahar Chettaoui, Guray Ozgur, Eduarda Caldeira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-head attention in Vision Transformers (ViTs) allows independent attention patterns across heads, but without explicit regularization, heads may learn redundant patterns rather than complementary roles. Correlation-based penalties encourage head disentanglement, yet apply uniform regularization across all training samples. In face recognition (FR), hard samples whose embeddings lie close to competing identities are critical for optimization and generalization. Motivated by this, we propose ViT-HarDis, which conditions attention head disentanglement on sample difficulty: samples with high cosine similarity to negative class centers receive stronger head decorrelation, enforcing specialization where identity ambiguity is highest. Experiments show improvements over both the baseline and uniform disentanglement on most benchmarks. Our analysis shows that ViT-HarDis reduces the similarity of hard samples to competing class centers while decreasing inter-head attention similarity, and that applying disentanglement only to the final transformer layers outperforms regularizing the entire network. Trained on WebFace4M, ViT-HarDis achieves SOTA results among ViT-based methods on IJB-B, IJB-C, and TinyFace Rank-1, while achieving the best IJB-B and TinyFace results when trained on MS1MV3, improving FR without architectural modifications or additional inference cost. Code: this https URL.

---


### 145. [Different Models, Shared Failures: Auditing Frozen-Encoder Pools for Medical Segmentation](https://arxiv.org/abs/2610.41790)

**<font color=#1a73e8>作者：</font>** Eunseob Choi, Kyeonghun Kim, Hyuk-Jae Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Average segmentation accuracy and model count do not reveal whether models fail on the same cases. We present CoFailMed, an audit of correlated failures in pretrained-encoder pools for medical segmentation. Across five 2D tasks, we evaluate 11 public pretrained encoders (a controlled sample, not a census) using frozen features and separately trained $1\times 1$ readouts with four seeds per encoder. Shared-checkpoint pairs have the highest mean per-case Dice correlation. An expanded 17-encoder analysis shows that distinct checkpoints within the same encoder family remain more correlated than cross-family pairs. At the pooled 33rd-percentile Dice threshold, four-member pools drawn from distinct encoders have mean effective sizes of 1.56-2.92, estimated from failure correlations in pools with enough failures and passes per member. In the primary pool, richer readouts and fine-tuning narrow the Dice-correlation gap between pairs sharing a checkpoint (or the DINOv2-B/S release) and all other pairs. Yet dependence between different encoders can increase, and fine-tuning does not consistently increase effective pool size at 33rd-percentile thresholds recomputed for each training recipe. A smaller between-group gap can coexist with greater dependence. Pool evaluation should therefore report absolute dependence and threshold-specific effective size alongside accuracy and nominal pool size. The CoFailMed release provides aligned per-case traces, analysis scripts and study code to reproduce the central audit results.

---


### 146. [Implicit Assumptions About Tasks in Continual Learning](https://arxiv.org/abs/2610.41792)

**<font color=#1a73e8>作者：</font>** Kathrin Korte, Christian Metzner, Akshay Bedhotiya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning is the study of how a model accumulates knowledge from data received over time, rather than all at once. In practice, this is typically achieved by dividing a dataset into tasks and presenting them sequentially. Explanations of the resulting measurements take into account factors such as the similarity between segments, the rate at which the data changes and the order of presentation. Each of these factors can be defined in terms of the underlying data, the partition imposed on it, or the learner that encounters it. These levels do not necessarily coincide, and it is usually left implicit which level a reported quantity refers to. We separate these and identify which properties acquire a value at each level. In controlled teacher--student experiments, we demonstrate that partitioning the same underlying trajectory at different levels of granularity, changing the order of presentation, and varying the similarity structure of the underlying data all result in different measured outcomes. We review representative benchmarks to determine which of these properties are stated. Where the underlying data cannot be inspected, as in foundation models built on undisclosed pre-training corpora, its properties are inherited by the model's initial state, and the training applied on top of it can be described.

---


### 147. [Accurate and Auditable ECG Classification via Visibility Graph Neural Networks](https://arxiv.org/abs/2610.41795)

**<font color=#1a73e8>作者：</font>** Artur Xavier, Guilherme Henrique Gomes Evangelista, Aitazaz Khan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physicians read electrocardiograms (ECGs) from waveform shape and timing, yet accurate deep-learning classifiers rarely show which waveform regions drive their predictions. We introduce LYNX-ECG, a graph neural network that represents each heartbeat as a sparse visibility graph of timestamped turning points. On CODE-Test, LYNX-ECG reaches a macro F1 score of 0.889, outperforming five baselines including the ECGFounder foundation model, while its graphs need about 14% of the storage of graphs built from every sample. Because each node maps to a specific ECG time, we can delete clinically defined waveform regions and alter beat timing to audit predictions. For conduction disorders, the clinically expected region was the strongest evidence in more than 90% of correct predictions. Bradycardia and tachycardia calls follow heart rate with conduction intervals held fixed, and atrial fibrillation calls vanish when beat-to-beat variation is removed. Sparse visibility graphs thus pair accurate ECG classification with clinically grounded, testable explanations.

---


### 148. [On-device Detection of Wearer-induced NLOS on Chest-worn UWB Tags: Machine Learning, Link Indicators, or Both?](https://arxiv.org/abs/2610.41799)

**<font color=#1a73e8>作者：</font>** Markus Gallacher, Vu Anh Minh Le, Matteo Trobinger 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ultra-wideband (UWB) enables high-accuracy distance estimation (ranging), but performance degrades in non-line-of-sight (NLOS) conditions. When UWB tags are worn, the human body inevitably causes a wearer-induced NLOS (WNLOS), yielding significant errors; still, despite its relevance, WNLOS remains understudied. Moreover, WNLOS detection typically must occur on-device at the tag, requiring classification accuracy to be balanced against tight runtime and energy constraints often hard to meet with machine learning (ML) -- the dominating NLOS classification approach. Meanwhile, UWB radio link indicators (LI) offer a faster and lightweight alternative that has rarely been explored. We study existing on-device ML and LI classifiers when applied to WNLOS, and propose novel hybrid ones exploiting their complementarity. We focus on chest-worn tags and analyze 21 classifiers on a dataset of 1.5 million samples across channels, PHY settings, environments, subjects, and orientations. Results show that while all of them achieve good classification accuracy, relative performance, including ranging errors due to misclassification, depends heavily on channel and PHY configuration. Runtime and energy efficiency also vary dramatically; some techniques offer marginal accuracy gains while consuming up to 39.6x more energy. Therefore, we also introduce a recommender tool to identify optimal classifiers under user-defined constraints, publicly released with our dataset.

---


### 149. [Towards Out-of-Distribution Uncertainty Quantification for Machine-Learned Interatomic Potentials via Pre-Training](https://arxiv.org/abs/2610.41801)

**<font color=#1a73e8>作者：</font>** Stefan P. Schmid, Tobias Setzer, Maximilian Scheurer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Informative uncertainty quantification (UQ) is essential for the practical deployment of machine-learned interatomic potentials (MLIPs), as it provides insight into their reliability across chemical space. Although numerous post-hoc uncertainty estimation methods for MLIPs have recently been proposed, most have been trained in low-data regimes, restricting their applicability to narrow domains of interest. Inspired by the emergence of foundational MLIPs, we propose pre-training uncertainty estimators on large, diverse datasets to enable broader applicability. We pre-train several UQ models on large materials science datasets to quantify the uncertainty of different MLIPs, and evaluate their performance on both in-distribution and out-of-domain (OOD) adsorption-energy predictions. We find that pre-trained uncertainty estimators provide viable zero-shot uncertainty estimates across multiple datasets, while fine-tuning consistently yields positive correlations between predicted uncertainty and prediction error, even on the most challenging datasets. These results lay the groundwork for foundational UQ models for MLIPs, ultimately facilitating their deployment in practical settings by providing users with a priori information about model reliability and applicability.

---


### 150. [Backpropagation-free Deep Learning for Time-Series Classification](https://arxiv.org/abs/2610.41805)

**<font color=#1a73e8>作者：</font>** Miha Kapš, Blaž Bertalanič, Carolina Fortuna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks for time series classification (TSC) are trained almost exclusively by error backpropagation, which imposes update locking and the weight-transport problem. Backpropagation-free learning rules such as Direct Feedback Alignment (DFA), Direct Random Target Projection (DRTP), and the diffusion-inspired NoProp relax these constraints but have been evaluated almost exclusively on 2D image benchmarks. We adapt these three learners to univariate TSC with 1D convolutional architectures and present the first systematic study of them across 112 datasets from the UCR time series archive, with one hyperparameter-optimized configuration per method. The optimized learners reach mean F1 scores of 0.76 to 0.79, below ROCKET (0.83) and InceptionTime (0.84). We propose an analysis framework that relates the per-dataset gap to InceptionTime to dataset properties and tests convolutional feature learning by replacing the flatten readout with global average pooling, measured as a difference-in-differences (DD) against a backpropagation control on the identical architecture. Intra-class temporal variability is the dataset property most consistently associated with the gap for all three learners (partial Spearman $\rho$ from $0.28$ to $0.40$). Pooling harms DFA and DRTP more than backpropagation (DD $-0.025$ and $-0.055$), consistent with near-random convolutional features, whereas NoProp tolerates pooling as backpropagation does (DD $+0.013$). Relative to backpropagation on the same architectures, DRTP reduces training floating-point operations (FLOPs) by 33% and trains faster only on series longer than about 700 time steps, DFA yields no computational reduction, and NoProp reduces peak memory by 38% at the cost of 48% longer training.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-193](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
