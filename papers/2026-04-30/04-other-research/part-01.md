# 📦 其他研究 | 2026年04月30日

> 本类共 **190** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-190](./part-04.md)

---

### 1. [GCA-BULF: A Bottom-Up Framework for Short-Term Load Forecasting Using Grouped Critical Appliances](https://arxiv.org/abs/2604.24766)

**<font color=#1a73e8>作者：</font>** Yunhao Yao, Jinwei Fang, Puhan Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the rise of time-of-use and tiered electricity pricing, energy consumers are encouraged to adopt peak-shifting strategies by automatically controlling high-power appliances. These help lower energy costs while enhancing the power grid's stability. To support such energy management with high resilience and responsiveness, reliable short-term load forecasting (STLF) plays a critical role. STLF predicts electricity consumption over time horizons ranging from minutes to days, using historical data, temporal patterns, and contextual factors. Traditional top-down forecasting methods struggle to capture the complex consumption patterns of diverse and mixed appliance loads. Although bottom-up methods improve forecasting accuracy by integrating appliance-level data, monitoring all appliances is costly, and many do not meaningfully impact total load prediction. Therefore, we propose GCA-BULF, a bottom-up short-term load forecasting framework based on grouped critical appliances, supported by three key designs. First, the Critical Appliance Filtering module ranks appliances according to their power consumption, switching frequency, and usage pattern periodicity, and identifies critical ones through iterative load decomposition. Next, the Related Appliance Grouping module clusters these appliances based on spatial and temporal correlations for group-level forecasting. Finally, the Collaborative Load Forecasting module refines the total load prediction by combining multiple group-level forecasts. We evaluate GCA-BULF on residential and office building load forecasting tasks. Experimental results reveal that GCA-BULF improves hourly total load forecasting by 20.85%-57.88% compared to existing top-down methods and by 33.03%-92.48% compared to bottom-up methods.

---


### 2. [Automated detection of pediatric congenital heart disease from phonocardiograms using deep and handcrafted feature fusion](https://arxiv.org/abs/2604.24767)

**<font color=#1a73e8>作者：</font>** Abdul Jabbar, Ethan Grooby, Yang Yi Poh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Congenital heart disease (CHD) is the most common type of birth defect, impacting about 1% of live births worldwide. Echocardiography, the gold-standard diagnostic method, is costly and inaccessible in low-resource settings. Diagnosis is delayed due to limited skilled experts, whose ability to interpret pathological patterns varies significantly, causing inter- and intra-clinician variability. Therefore, we present a new method for a more accessible diagnostic modality, the digital stethoscope, to detect CHDs. Our method is based on deep feature fusion, integrating deep and handcrafted features for the automated early detection of CHDs. For this work, Phonocardiography (PCG) recordings were obtained from 751 pediatric subjects (Age:1 month- 16 years) in Bangladesh, ranging from infants to adults at four auscultation locations: mitral valve (MV), aortic valve (AV), pulmonary valve (PV), and tricuspid valve (TV). These recordings were labeled based on confirmed diagnoses by cardiologists as either cases of CHD or non-CHD. The results demonstrated that our proposed model achieved an accuracy of 92%, a sensitivity of 91%, and a specificity of 91%, based on a patient-wise split of 70% training, 20% validation, and 10% testing. Furthermore, the Area Under the Receiver Operating Characteristic curve (AUROC) of 96%, and an F1-score of 92%. This model promises efficient real-time remote detection of CHDs as a cost-effective screening tool for low-resource settings.

---


### 3. [Comparative Study of Bending Analysis using Physics-Informed Neural Networks and Numerical Dynamic Deflection in Perforated nanobeam](https://arxiv.org/abs/2604.24768)

**<font color=#1a73e8>作者：</font>** Ramanath Garai, Iswari Sahu, S. Chakraverty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this chapter, we investigate the bending behavior of a perforated nanobeam subjected to sinusoidal loading using an efficient and computationally robust Physics-Informed Functional Link Constrained Framework with Domain Mapping (DFL-TFC) method. Our aim is to determine the relationship between static bending response and dynamic deflection of a perforated nanobeam for various perforation cases. The static bending is obtained using the FL-TFC with Domain mapped method, whereas dynamic deflection is determined using the Galerkin method. The proposed approach employs the theory of functional connections (TFC) to systematically embed governing differential equation constraints into a constrained expression (CE), which exactly satisfies all prescribed initial and boundary conditions (ICs and BCs) and domain of differential equation is mapped to domain of orthogonal polynomials. Within this framework, the free function appearing in the constrained expression is expressed through a functional link neural network (FLNN). The cost is minimized by the mean square residual of DE, allowing training without requiring complex deep network architectures. Relationship between static and dynamic defection of simply-supported (S-S) perforated nanobeams has been investigated here. FL-TFC with Domain mapped method eliminates the need for deep and complex neural network architectures while ensuring accuracy, efficiency, and strict satisfaction of boundary conditions as compared to standard PINN.

---


### 4. [Elderly-Contextual Data Augmentation via Speech Synthesis for Elderly ASR](https://arxiv.org/abs/2604.24770)

**<font color=#1a73e8>作者：</font>** Minsik Lee, Seoi Hong, Chongmin Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in automatic speech recognition (ASR), elderly ASR (EASR) remains challenging due to limited training data and the distinct acoustic and linguistic characteristics of elderly speech. In this work, we address data scarcity in EASR through a data augmentation pipeline that combines large language model (LLM)-based transcript paraphrasing with text-to-speech (TTS) synthesis. Given an elderly speech dataset, the LLM first generates elderly-contextual paraphrases of the original transcripts, and the TTS model then synthesizes corresponding speech using elderly reference speakers. The resulting synthetic audio-text pairs are merged with the original data to fine-tune Whisper without architectural modification. We further analyze the effects of augmentation ratio and reference-speaker composition in low-resource EASR. Experiments on English and Korean elderly speech datasets from speakers aged 70 and above show that the proposed method consistently improves performance over conventional augmentation baselines, achieving up to a 58.2% reduction in word error rate (WER) compared with the Whisper baseline.

---


### 5. [Liquid Neural Network Models for Natural Gas Spot Price Time-Series Forecasting](https://arxiv.org/abs/2604.24788)

**<font color=#1a73e8>作者：</font>** Yiqian Liu, Jiayi Niu, Adam Kelleher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural gas is undoubtedly an essential component of the global energy system. Accurate short-term forecasting of natural gas price is challenging due to pronounced volatility driven by seasonal demand patterns, geopolitical developments, and shifting macroeconomic conditions. The nonlinear dynamics and frequent regime changes can limit the effectiveness of traditional time-series models. In this study, we explore the use of Liquid Neural Networks (LNNs) for short-horizon forecasting of the Henry Hub spot price, a primary benchmark for pricing. LNNs are designed to adapt continuously to evolving temporal patterns through dynamic internal state updates, making them well suited for nonstationary price behavior. By improving forecast accuracy in volatile market conditions, this work aims to reduce uncertainty and enhance decision support across energy trading and power market applications.

---


### 6. [V.O.I.C.E (Voice, Ownership, Identity, Control, Expression): Risk Taxonomy of Synthetic Voice Generation From Empirical Data](https://arxiv.org/abs/2604.24794)

**<font color=#1a73e8>作者：</font>** Tanusree Sharma, Anish Krishnagiri, Lili Dudas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As generative voice models are rapidly advancing in both capabilities and public utilization, the unconsented collection, reuse, and synthesis of voice data are introducing new classes of privacy, security and governance risk that are poorly captured by existing, largely uniform threat models. To fill the gap, we present V.O.I.C.E, a taxonomy of voice generation risk grounded in a multi-source threat modeling effort with 569 incidents from major AI incident database, FTC and Internet Crime Complaint Center (IC3); 1067 direct incident reports from U.S. based participants across diverse groups (including voice actors, internet personalities, political personnel, and general public); and 2,221 Reddit discussions. Grounded in real-world data, our taxonomy explicitly models how risk emerges, interact with contextual factors such as degree of exposure, social visibility, and the availability of legal protections for various affected groups.

---


### 7. [Query-Efficient Quantum Approximate Optimization via Graph-Conditioned Trust Regions](https://arxiv.org/abs/2604.24803)

**<font color=#1a73e8>作者：</font>** Molena Huynh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In low-depth implementations of the Quantum Approximate Optimization Algorithm (QAOA), the dominant cost is often the number of objective evaluations rather than circuit depth. We introduce a graph-conditioned trust-region method for reducing this query cost. A graph neural network predicts a Gaussian distribution N(mu, Sigma) over QAOA angles. The mean initializes a local optimizer, the covariance defines an ellipsoidal trust region that constrains the search, and the predicted uncertainty determines an instance-dependent evaluation budget. Thus the learned distribution defines a search policy rather than only an initial parameter estimate.
Under explicit assumptions on local smoothness, curvature, calibration, and noise, we derive bounds on objective degradation within the trust region, lower bounds on gradient variance, preservation of expected objective ordering under depolarizing noise, and finite-sample coverage guarantees. We evaluate the method for MaxCut at depth p = 2 on Erdos-Renyi, 3-regular, Barabasi-Albert, and Watts-Strogatz graphs with n = 8-16 vertices. Relative to random restarts and the strongest learned point-prediction baseline, the method reduces the mean number of circuit evaluations from 343 and 85 to 45 +/- 7, while maintaining sampled approximation ratios within 3 percentage points of concentration-based heuristics.
The method does not improve absolute approximation ratios; its advantage is reduced query cost at comparable solution quality. The predictive uncertainty is calibrated in the experiments, with ECE = 0.052 and Spearman correlation rho = 0.770, and the learned trust regions transfer to graph sizes not used during training. The results identify a low-depth, query-dominated regime in which graph-conditioned trust regions reduce the query cost of QAOA without modifying the ansatz.

---


### 8. [minAction.net: Energy-First Neural Architecture Design -- From Biological Principles to Systematic Validation](https://arxiv.org/abs/2604.24805)

**<font color=#1a73e8>作者：</font>** Martin G. Frasch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning optimizes for accuracy without explicitly accounting for internal computational cost, even though physical and biological systems operate under intrinsic energy constraints. We evaluate energy-aware learning across 2,203 experiments spanning vision, text, neuromorphic, and physiological datasets, using 10 seeds per configuration and performing a factorial statistical analysis. Three findings emerge. First, architecture alone explains negligible variance in accuracy (partial eta^2 = 0.001). In contrast, the architecture x dataset interaction is large (partial eta^2 = 0.44, p < 0.001), demonstrating that optimal architecture depends critically on task modality and rejecting the assumption of a universal best architecture. Second, a controlled lambda-sweep over four orders of magnitude validates a single-parameter energy-regularized objective L = L_CE + lambda * E(theta, x): internal activation energy decreases to 6% of baseline at moderate lambda with no accuracy degradation on MNIST. Third, energy-first architectures inspired by an action-principle framework yield 5-33% within-modality training-efficiency gains over conventional baselines. These results emerge from a research program that interprets learning through a structural correspondence between the action functional in classical mechanics, free energy in statistical physics, and KL-regularized objectives in variational inference. We frame this correspondence as a design hypothesis rather than a derivation.

---


### 9. [A Comparative Analysis on the Performance of Upper Confidence Bound Algorithms in Adaptive Deep Neural Networks](https://arxiv.org/abs/2604.24810)

**<font color=#1a73e8>作者：</font>** Grigorios Papanikolaou, Ioannis Kontopoulos, Konstantinos Tserpes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge computing environments impose strict constraints on energy consumption and latency, making the deployment of deep neural networks a significant challenge. Therefore, smart and adaptive inference strategies that dynamically balance computational cost or latency with predictive accuracy are critical in edge computing scenarios. In this work, we build on Adaptive Deep Neural Networks (ADNNs) that employ the Multi-Armed Bandit (MAB) framework. Current literature leverages the first version of the Upper Confidence Bound (UCB1) strategy to dynamically select the optimal confidence threshold, enabling efficient early exits without sacrificing accuracy. However, we introduce four additional Upper Confidence Bound strategies in ADNNs, namely UCB-V, UCB-Tuned, UCB-Bayes, and UCB-BwK, and perform, for the first time, a comparative study of these strategies with respect to trade-offs between accuracy, energy consumption, and latency. The proposed UCB strategies are employed on the ResNet and MobileViT neural networks, and are evaluated on the benchmark datasets of CIFAR-10, CIFAR-10.1, and CIFAR-100. Experimental results demonstrate that all strategies achieve sub-linear cumulative regret, with UCB-Bayes converging the fastest, followed by UCB-Tuned and UCB-V. Finally, UCB-V and UCB-Tuned dominate the Pareto Frontiers of accuracy-latency and accuracy-energy trade-offs.

---


### 10. [Time-varying Interaction Graph ODE for Dynamic Graph Representation Learning](https://arxiv.org/abs/2604.24811)

**<font color=#1a73e8>作者：</font>** Xiaoyi Wang, Zhiqiang Wang, Jianqing Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural Ordinary Differential Equations (ODE) combine neural ODE with the message passing mechanism of Graph Neural Networks (GNN), providing a continuous-time modeling method for graph representation learning. However, in dynamic graph scenarios, existing graph neural ODEs typically employ a unified message passing mechanism, assuming that inter-node interactions share the same message passing function at any time, which makes it challenging to capture the diversity and time-varying nature of inter-node interaction patterns. To address this, we propose Time-varying Interaction Graph Ordinary Differential Equations (TI-ODE). The core idea of TI-ODE is to decompose the evolution function of a graph ODE into a set of learnable interaction basis functions, where each basis function corresponds to a distinct type of inter-node interaction. These basis functions are dynamically combined through time-dependent learnable weights, enabling inter-node interaction patterns to adaptively evolve over time. Experimental results on six dynamic graph datasets demonstrate that TI-ODE consistently outperforms existing methods and achieves state-of-the-art performance on attribute prediction tasks, and experiments on the \textit{Covid} dataset further verify the interpretability and generalizability of our TI-ODE. Furthermore, we demonstrate both theoretically and empirically that TI-ODE exhibits superior robustness compared to models utilizing a unified message-passing mechanism.

---


### 11. [Heterogeneous Variational Inference for Markov Degradation Hazard Models: Discretized Mixture with Interpretable Clusters](https://arxiv.org/abs/2604.24818)

**<font color=#1a73e8>作者：</font>** Takato Yasuno  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian finite mixture models can identify discrete risk clusters (low-risk vs. high-risk equipment), but face three critical bottlenecks: (1) insufficient degradation signals from coarse state discretization, (2) unstable cluster identification when data inherently supports fewer clusters than explored, and (3) computational infeasibility of Markov Chain Monte Carlo (MCMC) methods for production deployment (7+ hours per model). We propose a practical framework combining (1) 8-state global percentile discretization that amplifies degradation events, (2) 30-dimensional feature engineering integrating statistical trends (22 features), continuous health indicators, and text embeddings (PCA-compressed to 3 dimensions), (3) interpretable model selection rules enforcing minimum cluster share and separation alongside WAIC, and (4) Automatic Differentiation Variational Inference (ADVI) with full-rank covariance for stable, fast estimation. Applied to 280 industrial pump equipment with 104,703 inspection records, we demonstrate: (1) Random effect models (baseline) show ADVI and NUTS produce nearly identical estimates with 15$\times$ speedup, validating ADVI accuracy. (2) Finite mixture models identify optimal number of clusters with interpretability constraints. (3) NUTS exhibits severe convergence issues and label switching, while ADVI provides stable results in 84$\times$ less time. We contributed that (1) First demonstration that fine-grained state discretization (8-state) is essential for mixture model stability in survival analysis.(2) Comprehensive feature engineering strategy combining statistical, continuous, and semantic signals. (3) Practical interpretability rules preventing overfitting in automated model selection. (4) Empirical evidence that ADVI outperforms NUTS for finite mixture models in terms of convergence, stability, and computational efficiency.

---


### 12. [Negative Ontology of True Target for Machine Learning: Towards Evaluation and Learning under Democratic Supervision](https://arxiv.org/abs/2604.24824)

**<font color=#1a73e8>作者：</font>** Yongquan Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article philosophically examines how shifts in assumptions regarding the existence and non-existence of the true target (TT) give rise to new perspectives and insights for machine learning (ML)-based predictive modeling and, correspondingly, proposes a knowledge system for evaluation and learning under Democratic Supervision. By systematically analysing the existence assumption of the TT in current mainstream ML paradigms, we explicitly adopt a negative ontology perspective, positing that the TT does not objectively exist in the real world, and, grounded in this non-existence assumption, define Democratic Supervision for ML. We further present Multiple Inaccurate True Targets (MIATTs) as an instance-level realization of Democratic Supervision. Building upon MIATTs, we derive principles, for the logic-driven generation and assessment of MIATTs, a logical assessment formulation for evaluation with MIATTs, and undefinable true target learning for learning with MIATTs. Based on these components, we establish the evaluation and learning with MIATTs (EL-MIATTs) framework for ML-based predictive modelling. A real-world application demonstrates the potential of the proposed EL-MIATTs framework in supporting education and professional development for individuals, aligning with prior discussions of Democratic Supervision in the fields of education and professional development.

---


### 13. [A Comparative Evaluation of AI Agent Security Guardrails](https://arxiv.org/abs/2604.24826)

**<font color=#1a73e8>作者：</font>** Qi Li, Jiu Li, Pingtao Wei 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This report presents a comparative evaluation of DKnownAI Guard in AI agent security scenarios, benchmarked against three competing products: AWS Bedrock Guardrails, Azure Content Safety, and Lakera Guard. Using human annotation as the ground truth, we assess each guardrail's ability to detect two categories of risks: threats to the agent itself (e.g., instruction override, indirect injection, tool abuse) and requests intended to elicit harmful content (e.g., hate speech, pornography, violence). Evaluation results demonstrate that DKnownAI Guard achieves the highest recall rate at 96.5\% and ranks first in true negative rate (TNR) at 90.4\%, delivering the best overall performance among all evaluated guardrails.

---


### 14. [Network Impact of Post-Quantum Certificate Chain sizes on Time to First Byte in TLS Deployments](https://arxiv.org/abs/2604.24869)

**<font color=#1a73e8>作者：</font>** Matthew Chou, Phuong Cao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-Quantum Cryptography (PQC) is a rapidly growing deployment challenge as cryptographically relevant quantum computers (CRQC) continue to advance, leaving traditional cryptographic algorithms used in X.509 vulnerable to attack. However, PQC introduces significant deployment challenges in real-world networks, with handshake sizes increasing from 5x to over 20x compared to classical algorithms. In this work, we evaluate the time to first byte (TTFB) under CDN-focused TLS conditions to characterize the latency cost of transitioning existing internet infrastructure to quantum-safe certificate schemes. We observe discrete increases in TTFB as certificate chain sizes exceed transport layer data flight limits. To isolate the impact of certificate chains, we evaluate both ECDSA and ML-DSA-based certificate schemes, generating similarly sized certificate chains through controlled addition of certificate extensions. We additionally examine how CDN properties such as session resumption, certificate size optimizations, and geographical distribution reduce latency penalties. We utilize Zeek-monitored TLS traffic through a High-Performance Computing System (NCSA) with terabyte network connectivity across the nation to quantify real-world session resumption rates. We compare CDN-driven size optimization with Merkle Tree Certificates (MTC) to examine how size reductions allow certificate chains to remain under the flight limit threshold. We find that MTC allows for 2x-3x increase in supportable certificate chain size, whereas CDN-based optimizations yield more limited reductions, supporting up to approximately 1.6x certificate chain size increase.

---


### 15. [ESICA: A Scalable Framework for Text-Guided 3D Medical Image Segmentation](https://arxiv.org/abs/2604.24876)

**<font color=#1a73e8>作者：</font>** Yu Xin, Gorkem Can Ates, Jun Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text guided 3D medical image segmentation offers a flexible alternative to class based and spatial prompt based models by allowing users to specify regions of interest directly in natural language. This paradigm avoids reliance on predefined label sets, reduces ambiguous outputs, and aligns more naturally with clinical workflows. However, existing text guided frameworks are often computationally expensive, exhibit weak text volume feature alignment, and fail to capture fine anatomical details. We propose ESICA, a lightweight and scalable framework that addresses these challenges through three innovations: (1) a similarity matrix based mask prediction formulation that enhances semantic alignment, (2) an efficient decomposed decoder with adapter modules for accurate volumetric decoding, and (3) a two pass refinement strategy that sharpens boundaries and resolves uncertain regions. To improve training stability and generalization, ESICA adopts a two stage scheme consisting of positive only pretraining followed by balanced fine tuning. On the CVPR BiomedSegFM benchmark spanning five imaging modalities (CT, MRI, PET, ultrasound, and microscopy), ESICA achieves state of the art segmentation accuracy, while the compact ESICA4 Lite variant attains similar segmentation performance with substantially fewer parameters, yielding a superior efficiency accuracy trade off. Our framework advances text guided segmentation toward efficient, scalable, and clinically deployable systems. Code will be made publicly available at this https URL.

---


### 16. [Learning Illumination Control in Diffusion Models](https://arxiv.org/abs/2604.24877)

**<font color=#1a73e8>作者：</font>** Nishit Anand, Manan Suri, Christopher Metzler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controlling illumination in images is essential for photography and visual content creation. While closed-source models have demonstrated impressive illumination control, open-source alternatives either require heavy control inputs like depth maps or do not release their data and code. We present a fully open-source and reproducible pipeline for learning illumination control in diffusion models. Our approach builds a data engine that transforms well-lit images into supervised training triplets consisting of a poorly-illuminated input image, a natural language lighting instruction, and a well-illuminated output image. We finetune a diffusion model on this data and demonstrate significant improvements over baseline SD 1.5, SDXL, and FLUX.1-dev models in perceptual similarity, structural similarity, and identity preservation. Our work provides a reproducible solution built entirely with open-source tools and publicly available data. We release all our code, data, and model weights publicly.

---


### 17. [Transformer Approximations from ReLUs](https://arxiv.org/abs/2604.24878)

**<font color=#1a73e8>作者：</font>** Jerry Yao-Chieh Hu, Mingcheng Lu, Yi-Chen Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We provide a systematic recipe for translating ReLU approximation results to softmax attention mechanism. This recipe covers many common approximation targets. Importantly, it yields target-specific, economic resource bounds beyond universal approximation statements. We showcase the recipe on multiplication, reciprocal computation, and min/max primitives. These results provide new analytical tools for analyzing softmax transformer models.

---


### 18. [VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations](https://arxiv.org/abs/2604.24885)

**<font color=#1a73e8>作者：</font>** Maitreya Patel, Jingtao Li, Weiming Zhuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce an efficient, resolution-agnostic autoregressive (AR) image synthesis approach that generalizes to arbitrary resolutions and aspect ratios, narrowing the gap to diffusion models at scale. At its core is VibeToken, a novel resolution-agnostic 1D Transformer-based image tokenizer that encodes images into a dynamic, user-controllable sequence of 32-256 tokens, achieving a state-of-the-art efficiency and performance trade-off. Building on VibeToken, we present VibeToken-Gen, a class-conditioned AR generator with out-of-the-box support for arbitrary resolutions while requiring significantly fewer compute resources. Notably, VibeToken-Gen synthesizes 1024x1024 images using only 64 tokens and achieves 3.94 gFID; by comparison, a diffusion-based state-of-the-art alternative requires 1,024 tokens and attains 5.87 gFID. In contrast to fixed-resolution AR models such as LlamaGen -- whose inference FLOPs grow quadratically with resolution (11T FLOPs at 1024x1024) -- VibeToken-Gen maintains a constant 179G FLOPs (63.4x efficient) independent of resolution. We hope VibeToken can help unlock the wide adoption of AR visual generative models in production use cases.

---


### 19. [Verifying Provenance of Digital Media: Why the C2PA Specifications Fall Short](https://arxiv.org/abs/2604.24890)

**<font color=#1a73e8>作者：</font>** Enis Golaszewski, Neal Krawetz, Alan T. Sherman 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid rise of generative AI has made it easy to create convincing fake media at scale. In response, an industrial coalition has developed the Coalition for Content Provenance and Authenticity (C2PA), a system intended to provide verifiable provenance for digital content. Our research team conducted the first comprehensive, independent security analysis of C2PA. Our study includes the first formal-methods analysis of C2PA's core protocols. We find that the current C2PA specifications fail to achieve their claimed security goals. Furthermore, they also fail to achieve key additional goals, which all such provenance systems require for trustworthy deployment. As a result, C2PA may mislead users, platforms, and policymakers if relied upon prematurely. C2PA is a promising idea, but it should not yet be relied upon for high-stakes uses such as financial disclosures, journalism, or legal evidence.

---


### 20. [Interactive Episodic Memory with User Feedback](https://arxiv.org/abs/2604.24893)

**<font color=#1a73e8>作者：</font>** Nikesh Subedi, Loris Bazzani, Ziad Al-Halah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In episodic memory with natural language queries (EM-NLQ), a user may ask a question (e.g., "Where did I place the mug?") that requires searching a long egocentric video, captured from the user's perspective, to find the moment that answers it. However, queries can be ambiguous or incomplete, leading to incorrect responses. Current methods ignore this key aspect and address EM-NLQ in a one-shot setup, limiting their applicability in real-world scenarios. In this work, we address this gap and introduce the Episodic Memory with Questions and Feedback task (EM-QnF). Here, the user can provide feedback on the model's initial prediction or add more information (e.g., "Before this. I'm looking for the big blue mug not the white one"), helping the model refine its predictions interactively. To this end, we collect datasets for feedback-based interaction and propose a lightweight training scheme that avoids expensive sequential optimization. We also introduce a plug-and-play Feedback ALignment Module (FALM) that enables existing EM-NLQ models to incorporate user feedback effectively. Our approach significantly improves over the state of the art on three challenging benchmarks and is better than or competitive with commercial large vision-language models while remaining efficient. Evaluation with human-generated feedback shows that it generalizes well to real-world scenarios.

---


### 21. [MultiHedge: Adaptive Coordination via Retrieval-Augmented Control](https://arxiv.org/abs/2604.24905)

**<font color=#1a73e8>作者：</font>** Feliks Bańka, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Decision-making under changing conditions remains a fundamental challenge in many real-world systems. Existing approaches often fail to generalize across shifting regimes and exhibit unstable behavior under uncertainty. This raises the research question: can retrieval-augmented LLM coordination improve the robustness of modular decision pipelines? We propose MultiHedge, a hybrid architecture where an LLM produces structured allocation decisions conditioned on retrieved historical precedents, and execution is grounded in canonical option strategies. In a controlled evaluation using U.S. equities, we compare MultiHedge to rule-based and learning-based baselines. The key result is that memory-augmented retrieval confers greater robustness and stability than increasing model scale alone. Our paper contributes a controlled computational study showing that memory and architectural design play a central role in robustness in modular decision systems.

---


### 22. [Learning with Embedded Linear Equality Constraints via Variational Bayesian Inference](https://arxiv.org/abs/2604.24911)

**<font color=#1a73e8>作者：</font>** Matthew Marsh, Benoît Chachuat, Antonio del Rio Chanona  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine Learning is becoming more prevalent in science and engineering, but many approaches do not provide meaningful uncertainty estimates and predictions may also violate known physical knowledge. We propose a Bayesian framework to embed linear relationships across inputs and outputs into the learning process, whilst characterizing full predictive uncertainty over both the model parameters and the domain knowledge. We evaluated our method on learning the single particle battery model subject to voltage and energy balances, showing its ability to provide reduced credible intervals and constraint violations compared to standard Bayesian neural networks based on variational inference.

---


### 23. [Generative diffusion models for spatiotemporal influenza forecasting](https://arxiv.org/abs/2604.24913)

**<font color=#1a73e8>作者：</font>** Joseph Lemaitre, Justin Lessler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting infectious disease incidence can provide important information to guide public health planning, yet is difficult because epidemic dynamics are complex. Current mechanistic and statistical approaches often struggle to capture multimodal uncertainty or emergent trends. Influpaint adapts denoising diffusion probabilistic models to epidemic forecasting. By encoding influenza seasons as spatiotemporal images in which pixel intensity represents incidence, Influpaint learns a rich distribution of disease dynamics from a hybrid dataset of surveillance and simulated trajectories. Forecasting is formulated as a conditional generation (inpainting) task from partial observations. We show that Influpaint generates realistic, diverse epidemic trajectories and achieves forecast accuracy that is competitive with leading ensemble methods in retrospective evaluation. In real-time evaluation during the 2023--2025 U.S. CDC FluSight challenges, performance improved substantially across seasons, with highly accurate but somewhat overconfident projections in 2024--2025. The best performance was achieved with a training dataset containing 30% surveillance and 70% simulated trajectories. These results show that diffusion models can capture important spatiotemporal structure in influenza dynamics and provide a flexible framework for probabilistic infectious disease forecasting.

---


### 24. [GAIA-v2-LILT: Multilingual Adaptation of Agent Benchmark beyond Translation](https://arxiv.org/abs/2604.24929)

**<font color=#1a73e8>作者：</font>** Yunsu Kim, Kaden Uhlig, Joern Wuebker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent benchmarks remain largely English-centric, while their multilingual versions are often built with machine translation (MT) and limited post-editing. We argue that, for agentic tasks, this minimal workflow can easily break benchmark validity through query-answer misalignment or culturally off-target context. We propose a refined workflow for adapting English benchmarks into multiple languages with explicit functional alignment, cultural alignment, and difficulty calibration using both automated checks and human review. Using this workflow, we introduce GAIA-v2-LILT, a re-audited multilingual extension of GAIA covering five non-English languages. In experiments, our workflow improves agent success rates by up to 32.7% over minimally translated versions, bringing the closest audited setting to within 3.1% of English performance while substantial gaps remain in many other cases. This indicates that a substantial share of the multilingual performance gap is benchmark-induced measurement error, motivating task-level alignment when adapting English benchmarks across languages. The data is available as part of the MAPS package at this https URL. We also release the code used in our experiments at this https URL.

---


### 25. [CAN-QA: A Question-Answering Benchmark for Reasoning over In-Vehicle CAN Traffic](https://arxiv.org/abs/2604.24935)

**<font color=#1a73e8>作者：</font>** Jing Chen, Abhijay Deevi, Onat Gungor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Controller Area Network (CAN) is a safety-critical in-vehicle communication protocol that lacks built-in security mechanisms, making intrusion detection essential. Existing approaches predominantly formulate CAN intrusion detection as a classification task, mapping complex traffic patterns to attack labels. However, this formulation abstracts away the temporal and relational structure of CAN traffic and misaligns with real-world forensic workflows, which require systematic reasoning about traffic behavior. To address this gap, we introduce CAN-QA, the first benchmark that reformulates CAN traffic analysis as a question-answering (QA) task. CAN-QA converts raw CAN logs into temporally segmented windows and applies deterministic rule-based templates to generate natural-language questions paired with automatically derived ground-truth answers. The resulting dataset comprises 33,128 QA pairs across 10 categories, each targeting distinct semantic and temporal properties of CAN traffic. Using CAN-QA, we evaluate large language models across both True/False and multiple-choice formats. Our results indicate that, although these models capture superficial statistical regularities, they struggle with temporal reasoning, multi-condition inference, and higher-level behavioral interpretation. Our code is available at this https URL.

---


### 26. [A Unifying Framework for Unsupervised Concept Extraction](https://arxiv.org/abs/2604.24936)

**<font color=#1a73e8>作者：</font>** Chandler Squires, Pradeep Ravikumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Techniques for concept extraction, such as sparse autoencoders and transcoders, aim to extract high-level symbolic concepts from low-level nonsymbolic representations. When these extracted concepts are used for downstream tasks such as model steering and unlearning, it is essential to understand their guarantees, or lack thereof. In this work, we present a unified theoretical framework for unsupervised concept extraction, in which we frame the task of concept extraction as identifying a generative model. We present a general meta-theorem for identifiability, which reduces the problem of establishing identifiability guarantees to the problem of characterizing the intersection of two sets. As we demonstrate on a range of widely-used approaches, this meta-theorem substantially simplifies the task of proving such guarantees, thus paving the way for the development of new, principled approaches for concept extraction.

---


### 27. [Independent-Component-Based Encoding Models of Brain Activity During Story Comprehension](https://arxiv.org/abs/2604.24942)

**<font color=#1a73e8>作者：</font>** Kamya Hari, Taha Binhuraib, Jin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Encoding models provide a powerful framework for linking continuous stimulus features to neural activity; however, traditional voxelwise approaches are limited by measurement noise, inter-subject variability, and redundancy arising from spatially correlated voxels encoding overlapping neural signals. Here, we propose an independent component (IC)-based encoding framework that dissociates stimulus-driven and noise-driven signals in fMRI data. We decompose continuous fMRI data from naturalistic story listening into ICs using one subset of the data, and train encoding models on independent data to predict IC time series from large language model representations of linguistic input. Across subjects, a subset of ICs exhibited consistently high predictivity. These ICs were spatially and temporally consistent across subjects and included cognitive networks known to respond during story listening (auditory and language). Auditory component time series were strongly correlated with acoustic stimulus features, highlighting the interpretability of identified component time series. Components identified as noise or motion-related artifacts by ICA-AROMA showed uniformly poor predictive performance, confirming that highly predicted components reflect genuine stimulus-related neural signals rather than confounds. Overall, IC-based encoding models enable analyses at the level of functional networks, accommodating the variability in network locations across individuals and providing interpretable results that are easy to compare across subjects.

---


### 28. [Subjective Portrait Region Cropping in Landscape Videos with Temporal Annotation Smoothing](https://arxiv.org/abs/2604.24947)

**<font color=#1a73e8>作者：</font>** Cheng-Han Lee, Maniratnam Mandal, Neil Birkbeck 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rise of mobile video consumption on diverse handheld display resolutions and orientation modes, altering videos to aspect ratios poses challenges. Static cropping and border padding often compromises visual quality, while warping may distort a video's intended meaning. Here we advocate for a more effective approach: cropping significant regions within video frames in a temporal manner, while minimizing distortion and preserving essential content. One barrier to solving this problem is the lack of sufficiently large-scale database devoted to informing these tasks. Towards filling this gap, we introduce the LIVE-YouTube Video Cropping (LIVE-YT VC) database, featuring 1800 videos, annotated by 90 human subjects. Using videos sourced from the YouTube-UGC and LSVQ Databases, this new resource is the largest publicly-available subjective video portrait region cropping database. We also introduce a post-processed version of the database, called LIVE-YT VC++, whereby a novel intra-frame temporal filter was deployed to smooth subjective annotations within each video. We demonstrate the usefulness of this new data resource using the SmartVidCrop algorithm and state-of-the-art video grounding models, in hopes of establishing our subjective dataset as a benchmark for future research. Our contributions offer a resource for advancing video aspect ratio transformation models towards ensuring that reshaped mobile-friendly video content retains its quality and meaning. Since our labels bear resemblances to video saliency annotations, we also conducted an additional analysis to explore the similarity between our labels and video saliency predictions. Finally, we repurposed state-of-the-art video grounding models for aspect ratio change tasks, and fine-tuned them on our dataset. As a service to the research community, we plan to open source the project.

---


### 29. [Learning from Noisy Preferences: A Semi-Supervised Learning Approach to Direct Preference Optimization](https://arxiv.org/abs/2604.24952)

**<font color=#1a73e8>作者：</font>** Xinxin Liu, Ming Li, Zonglin Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human visual preferences are inherently multi-dimensional, encompassing aesthetics, detail fidelity, and semantic alignment. However, existing datasets provide only single, holistic annotations, resulting in severe label noise: images that excel in some dimensions but are deficient in others are simply marked as winner or loser. We theoretically demonstrate that compressing multi-dimensional preferences into binary labels generates conflicting gradient signals that misguide Diffusion Direct Preference Optimization (DPO). To address this, we propose Semi-DPO, a semi-supervised approach that treats consistent pairs as clean labeled data and conflicting ones as noisy unlabeled data. Our method starts by training on a consensus-filtered clean subset, then uses this model as an implicit classifier to generate pseudo-labels for the noisy set for iterative refinement. Experimental results demonstrate that Semi-DPO achieves state-of-the-art performance and significantly improves alignment with complex human preferences, without requiring additional human annotation or explicit reward models during training. We will release our code and models at: this https URL

---


### 30. [ViPO: Visual Preference Optimization at Scale](https://arxiv.org/abs/2604.24953)

**<font color=#1a73e8>作者：</font>** Ming Li, Jie Wu, Justin Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While preference optimization is crucial for improving visual generative models, how to effectively scale this paradigm remains largely unexplored. Current open-source preference datasets contain conflicting preference patterns, where winners excel in some dimensions but underperform in others. Naively optimizing on such noisy datasets fails to learn preferences, hindering effective scaling. To enhance robustness against noise, we propose Poly-DPO, which extends the DPO objective with an additional polynomial term that dynamically adjusts model confidence based on dataset characteristics, enabling effective learning across diverse data distributions. Beyond biased patterns, existing datasets suffer from low resolution, limited prompt diversity, and imbalanced distributions. To facilitate large-scale visual preference optimization by tackling data bottlenecks, we construct ViPO, a massive-scale preference dataset with 1M image pairs at 1024px across five categories and 300K video pairs at 720p+ across three categories. State-of-the-art generative models and diverse prompts ensure reliable preference signals with balanced distributions. Remarkably, when applying Poly-DPO to our high-quality dataset, the optimal configuration converges to standard DPO. This convergence validates dataset quality and Poly-DPO's adaptive nature: sophisticated optimization becomes unnecessary with sufficient data quality, yet remains valuable for imperfect datasets. We validate our approach across visual generation models. On noisy datasets like Pick-a-Pic V2, Poly-DPO achieves 6.87 and 2.32 gains over Diffusion-DPO on GenEval for SD1.5 and SDXL, respectively. For ViPO, models achieve performance far exceeding those trained on existing open-source preference datasets. These results confirm that addressing both algorithmic adaptability and data quality is essential for scaling visual preference optimization.

---


### 31. [Vega-Video: Integrating Video into the Grammar of Graphics](https://arxiv.org/abs/2604.24958)

**<font color=#1a73e8>作者：</font>** Dominik Winecki, Arnab Nandi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Video data is increasingly used alongside conventional data for interactive data exploration, necessitating interfaces for exploring and presenting mixed-modality data. However, integrating video into visualizations remains difficult due to its distinct paradigms and inherent performance challenges. We identify three classes of video data visualization - synchronization, annotation, and transformation - and integrate them into the Vega declarative grammar. We show that these abstractions enable high-performance implementation. To reconcile Vega's instantaneous dataflow with video player state, we introduce a split-signal architecture that preserves declarative semantics while masking video update delays. We detect continuous scrubbing interactions at compile time to apply encoding-aware optimizations that improve responsiveness by up to 4x. We also repurpose VOD protocols to transform videos in real time, delivering sub-200ms updates even on multi-hour-long compilations. These contributions enable seamless integration of conventional and video data visualization.

---


### 32. [CoreFlow: Low-Rank Matrix Generative Models](https://arxiv.org/abs/2604.24959)

**<font color=#1a73e8>作者：</font>** Dongze Wu, Linglingzhi Zhu, Yao Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning matrix-valued distributions from high-dimensional and possibly incomplete training data is challenging: ambient-space generative modeling is computationally expensive and statistically fragile when the matrix dimension is large but the sample size is limited. We propose CoreFlow, a geometry-preserving low-rank flow model that learns shared row/column subspaces across the matrix distribution, and then trains a continuous normalizing flow only on the induced low-dimensional core. CoreFlow is designed for settings where shared low-rank matrix geometry is present, especially in high-dimensional limited-sample regimes. This separates shared matrix geometry from sample-specific variation, preserves matrix structure, and substantially improves training efficiency. The same framework also handles incomplete training matrices through masked Riemannian updates and iterative completion. Across real and synthetic benchmarks, CoreFlow substantially improves spectral and moment-level generation quality in few-sample regimes while remaining competitive in data-rich settings, even under compression to 9% of the ambient dimension and with up to 40% missing training entries.

---


### 33. [Odysseys: Benchmarking Web Agents on Realistic Long Horizon Tasks](https://arxiv.org/abs/2604.24964)

**<font color=#1a73e8>作者：</font>** Lawrence Keunho Jang, Jing Yu Koh, Daniel Fried 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing web agent benchmarks have largely converged on short, single-site tasks that frontier models are approaching saturation on. However, real world web use consists of long-horizon, multi-site workflows. Common web navigation tasks, such as comparing products across different domains, planning trips across multiple services, or summarizing information from multiple search queries, require sustained context and cross-site reasoning over potentially hours of browsing. To capture and evaluate such behaviors, we introduce Odysseys: a benchmark of 200 long-horizon web tasks derived from real world browsing sessions evaluated on the live Internet. We find that binary pass/fail evaluation is inadequate for long-horizon settings and introduce a rubric-based evaluation, annotating each Odysseys task with an average of 6.1 graded rubrics. We demonstrate that this yields higher agreement with humans and provides a more fine-grained signal than commonly used trajectory-level LLM-as-a-judge evaluation metrics. We tested several leading frontier models and find that the strongest models achieve a success rate of 44.5%, which leaves substantial room for future improvements. Beyond task success, we argue that efficiency is a first-class concern for long-horizon agents. We introduce a Trajectory Efficiency metric (rubric score per step) and find that even frontier agents achieve only 1.15%, marking an evident need for agents that can succeed efficiently and not simply eventually. Odysseys isolates the critical evaluation of long-horizon proficiency in open-web environments, providing a realistic benchmark to measure progress towards computer-use agents that can potentially productively operate for hours. We release our tasks, evaluation scripts, and other results at this https URL

---


### 34. [Poisoning Learned Index Structures: Static and Dynamic Adversarial Attacks on ALEX](https://arxiv.org/abs/2604.24975)

**<font color=#1a73e8>作者：</font>** Allen Jue  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Learned index structures achieve high performance by modeling the cumulative distribution function (CDF) of keys, but this reliance on data distributions introduces potential vulnerability to adversarial manipulation. Prior work has explored both static data poisoning and dynamic algorithmic complexity attacks (ACA), though evaluations are typically limited in scale or consider only one threat model. We present a systematic study of both attack paradigms on ALEX, a state-of-the-art dynamic learned index, under a unified and reproducible framework.
Our evaluation scales to realistic workloads with up to 200K adversarial inserts and includes multiple SOSD datasets with diverse key distributions, as well as a real-key baseline to isolate adversarial effects. Our results show a clear separation between threat models. Static poisoning has minimal impact on lookup performance in ALEX under bulk-loaded settings, while dynamic ACA induces substantial degradation, with up to 2--2.8x slowdown in lookup throughput. However, attack effectiveness is highly dataset-dependent: dense key distributions limit adversarial leverage due to duplicate-heavy insertions and ALEX's localized structure.
We highlight key evaluation considerations, including the need for control workloads and the mismatch between localized structural damage and global query metrics. These results show that robustness in learned indexes depends critically on the interaction between threat model, data distribution, and evaluation methodology.

---


### 35. [Dont Stop Early: Scalable Enterprise Deep Research with Controlled Information Flow and Evidence-Aware Termination](https://arxiv.org/abs/2604.24978)

**<font color=#1a73e8>作者：</font>** Prafulla Kumar Choubey, Kung-Hsiang Huang, Pranav Narayanan Venkit 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise deep research often fails to produce decision-ready reports due to uneven information coverage, context explosion, and premature stopping. We propose a scalable Enterprise Deep Research (EDR) architecture to address these failures. Our system (i) decomposes requests into coverage-driven objectives via outline generation with reflection, (ii) localizes context with dependency-guided execution and explicit information sharing, and (iii) enforces evidence-based completion criteria so agents iteratively collect information until sufficiency conditions are met. We evaluate on an internal sales enablement task and the public DeepResearch Bench benchmark, where our proposed system design achieves the strongest overall performance compared with competitive deep-research baselines. The results show that dependency-controlled context and explicit evidence sufficiency criteria reduce premature stopping and improve the consistency and depth of enterprise research outputs.

---


### 36. [What If We Work Together? Fostering Reflections on Designer Inclusion in Open Source Software Through Speculative Design](https://arxiv.org/abs/2604.24981)

**<font color=#1a73e8>作者：</font>** Rozhan Hozhabri Nezhad, Jin L.C. Guo, Jinghui Cheng  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Open source software (OSS) often prioritizes technical functionality over usability and UX design. This imbalance limits OSS adoption among broader, non-technical users. Key underlying factors contributing to this issue are the shortage of design expertise in OSS and a dominant developer-centric mindset. To address these persistent issues, we explore the potential of speculative design as a catalyst for transforming the OSS community's mindset towards a more designer-inclusive environment. Our design was informed by an analysis of online forums, which revealed designers' motivations and challenges when contributing to OSS. Guided by these insights, we created two speculative societies, Husia (collectivist) and Reetar (individualist), in which designers are valued for different reasons and their work incorporated in different ways. Through a user study with 12 OSS practitioners (seven designers and five developers), we found that our speculative societies provoked participants' rich and critical reflections on OSS values, the root causes of challenges, and proposed actions. Our work provides insights into how speculative design can be used in the practical, sociotechnical context of OSS to stimulate critical reflection, improve awareness, and yield recommendations for fostering an equitable, sustainable, and inclusive OSS environment.

---


### 37. ["We Wanted to Do Better Than the Law": Exploring UI/UX Designers' Privacy Advocacy in Practice](https://arxiv.org/abs/2604.24982)

**<font color=#1a73e8>作者：</font>** Keyu Yao, Jinghui Cheng, Jin L.C. Guo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Designers hold primary responsibility for shaping the user interface (UI) and user experience (UX) of a product. This role goes beyond aesthetics and usability, extending to the privacy outcomes of user experience, which often emerge through collaboration with other stakeholders such as developers, product managers, and marketing teams. Previous studies on enhancing privacy for technological products primarily focused on the roles of developers -- understanding their needs and challenges -- but limited effort is devoted to examining how UI/UX designers consider and approach privacy in their work. Through 12 semi-structured interviews with privacy-advocating UI/UX designers, we explore the perceptions, influencing factors, challenges, and adaptive methods they use regarding privacy implementation. We pay special attention to how these challenges and adaptations play out in team-based settings where decisions are negotiated together. Our study reveals how personal and contextual factors shape designers' value of privacy, the collaborative nature of the challenges designers face when trying to prioritize privacy, and how they navigate tensions between business goals, team dynamics, and technical development. Based on our findings, we discuss implications for advocating a user-centered approach for supporting privacy-aware design, suggestions for organizational-level changes and bridging knowledge gaps through designer-centric tools and community building.

---


### 38. [A New Kind of Network? Review and Reference Implementation of Neural Cellular Automata](https://arxiv.org/abs/2604.24990)

**<font color=#1a73e8>作者：</font>** Martin Spitznagel, Janis Keuper  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stephen Wolfram proclaimed in his 2003 seminal work "A New Kind Of Science" that simple recursive programs in the form of Cellular Automata (CA) are a promising approach to replace currently used mathematical formalizations, e.g. differential equations, to improve the modeling of complex systems. Over two decades later, while Cellular Automata have still been waiting for a substantial breakthrough in scientific applications, recent research showed new and promising approaches which combine Wolfram's ideas with learnable Artificial Neural Networks: So-called Neural Cellular Automata (NCA) are able to learn the complex update rules of CA from data samples, allowing them to model complex, self-organizing generative systems. The aim of this paper is to review the existing work on NCA and provide a unified modular framework and notation, as well as a reference implementation in the open-source library NCAtorch.

---


### 39. [Laplace-Bridged Randomized Smoothing for Fast Certified Robustness](https://arxiv.org/abs/2604.24993)

**<font color=#1a73e8>作者：</font>** Miao Lin, MD Saifur Rahman Mazumder, Feng Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized Smoothing (RS) offers formal $\ell_2$ guarantees for arbitrary base classifiers but faces two key practical bottlenecks: (i) it often relies on noise-augmented training to achieve nontrivial certificates, which increases training cost, can reduce clean accuracy, and weakens RS as a genuinely post-hoc defense; and (ii) certification is computationally expensive, typically requiring tens of thousands of noisy forward passes per input, which hinders deployment, especially on resource-constrained edge devices. To address both limitations, we propose Laplace-Bridged Smoothing (LBS), an analytic reformulation of RS that replaces high-dimensional input-space Monte Carlo (MC) sampling with efficient computations in a low-dimensional probability space. LBS preserves formal robustness guarantees without requiring noise-augmented training while substantially reducing certification burden. On CIFAR-10 and ImageNet, LBS attains stronger certified robustness than RS and reduces per-sample certification cost by nearly an order of magnitude. Notably, on NVIDIA Jetson Orin Nano and Raspberry Pi 4, LBS achieves speedups of up to $494\times$, enabling practical certified deployment on real-world edge devices. Finally, we provide theoretical justification for the analytic formulation and certificate validity of LBS.

---


### 40. [DouC: Dual-Branch CLIP for Training-Free Open-Vocabulary Segmentation](https://arxiv.org/abs/2604.24997)

**<font color=#1a73e8>作者：</font>** Mohamad Zamini, Diksha Shukla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation requires assigning pixel-level semantic labels while supporting an open and unrestricted set of categories. Training-free CLIP-based approaches preserve strong zero-shot generalization but typically rely on a single inference mechanism, limiting their ability to jointly address unreliable local tokens and insufficient spatial coherence. We propose DouC, a training-free dual-branch CLIP framework that decomposes dense prediction into two complementary components. OG-CLIP improves patch-level reliability via lightweight, inference-time token gating, while FADE-CLIP injects external structural priors through proxy attention guided by frozen vision foundation models. The two branches are fused at the logit level, enabling local token reliability and structure-aware patch interactions to jointly influence final predictions, with optional instance-aware correction applied as post-processing. DouC introduces no additional learnable parameters, requires no retraining, and preserves CLIP's zero-shot generalization. Extensive experiments across eight benchmarks and multiple CLIP backbones demonstrate that DouC consistently outperforms prior training-free methods and scales favorably with model capacity.

---


### 41. [BifDet: A 3D Bifurcation Detection Dataset for Airway-Tree Modeling](https://arxiv.org/abs/2604.24999)

**<font color=#1a73e8>作者：</font>** Ali Keshavarzi, Quentin Bouniot, Benjamin M. Smith 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thoracic Computed Tomography (CT) scans offer detailed insights into the intricate branching network of the airway tree, which is essential for understanding various respiratory diseases. Airway bifurcations, where airway branches split, are crucial landmarks for understanding lung physiology, disease mechanisms and lesion localization. Despite the significance of bifurcation analysis, a notable lack of datasets annotated for this task hinders the development of advanced automated specialized detection or segmentation tools. In this paper, we introduce BifDet, the first publicly-available dataset specialized for 3D airway bifurcation detection, filling a critical gap in existing resources. Our dataset comprises carefully annotated CT scans from the ATM22 open-access cohort with bifurcation bounding boxes covering the parent and daughter branches. As a use-case for demonstrating the potential of BifDet, we fine-tune and evaluate RetinaNet and DETR for 3D airway bifurcations detection on CT scans. We provide detailed pipelines, including preprocessing steps and specific implementation design choices. Results are detailed over various categories of minimal bounding box sizes to serve as baseline to benchmark future research.

---


### 42. [Toward a Science of Intent: Closure Gaps and Delegation Envelopes for Open-World AI Agents](https://arxiv.org/abs/2604.25000)

**<font color=#1a73e8>作者：</font>** Maximiliano Armesto, Christophe Kolb  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work has framed intelligence in verifiable tasks as reducing time-to-solution through learned structure and test-time search, while systems work has explored learned runtimes in which computation, memory and I/O migrate into model state. These perspectives do not explain why capable models remain difficult to deploy in open institutions. We propose intent compilation: the transformation of partially specified human purpose into inspectable artifacts that bind execution. The relevant deployment distinction is closed-world solver versus open-world agent. In closed worlds, a checker is largely given; in open worlds, verification is distributed across semantic, evidentiary, procedural and institutional dimensions. Weformalize this residual openness as a closure-gap vector, define delegation envelopes as pre-authorized regions of action space, distinguish misclosure from undersearch, and outline benchmark metrics for testing when closure interventions outperform additional inference-time search.

---


### 43. [Dynamic Regret for Online Regression in RKHS via Discounted VAW and Subspace Approximation](https://arxiv.org/abs/2604.25021)

**<font color=#1a73e8>作者：</font>** Dmitry B. Rokhlin, Georgiy A. Karapetyants  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online regression with the square loss in a reproducing kernel Hilbert space under a dynamic regret criterion. The learner is compared with a time-varying comparator sequence, and the bounds depend on its path length in the RKHS norm. The proposed method transfers the finite-dimensional discounted Vovk--Azoury--Warmuth approach of Jacobsen \& Cutkosky (2024) to the RKHS setting by means of finite-dimensional subspace approximations. For a fixed subspace, we run a VAW-based ensemble of discounted VAW forecasters over a geometric grid of discount factors. The additional approximation error is controlled by the uniform projection error of kernel sections.
We then introduce a general orthogonal truncation method: starting from a feature expansion of the kernel, we construct the associated RKHS by introducing an inner product that makes the feature functions orthonormal, and then use the spans of the first basis functions as finite-dimensional approximation spaces. The resulting subspace reduction is applied to several approximation schemes. Explicit feature expansions yield fast-regime bounds for Gaussian and analytic dot-product kernels. Mercer truncations provide a spectral approximation method and lead to dynamic regret bounds in fast and slow regimes, depending on the eigenvalue decay. Finally, we study subspaces spanned by kernel sections and apply this construction to Matérn kernels.

---


### 44. [AFA: Identity-Aware Memory for Preventing Persona Confusion in Multi-User Dialogue](https://arxiv.org/abs/2604.25022)

**<font color=#1a73e8>作者：</font>** Mohammad Al-Ratrout, Pavan Uttej Ravva, Shayla Sharmin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When multiple people share a single voice assistant, the system conflates their histories: one resident's preferences can leak into another's responses, eroding utility and trust. We call this failure mode persona confusion, and we show it is a measurable problem in today's single-user dialogue systems when deployed in shared environments. We present the Adaptive Friend Agent (AFA), a modular framework that combines voice-based speaker identification with per-user memory stores to enable identity-aware, personalized dialogue across multiple users. To support training and evaluation, we construct PAT (Personalized Agent chaT), a synthetic dataset of 58,289 persona-grounded dialogue turns spanning 133 user profiles and 12 real-world scenarios. We evaluate AFA across five LLM back-ends in a standard response-quality benchmark, with a LLaMA-2-70B model fine-tuned on PAT achieving the highest overall performance. To directly measure persona confusion prevention, we introduce an interleaved multi-user evaluation protocol with a novel metric, Persona Attribution Accuracy (PAA), demonstrating that identity-aware routing improves PAA from 35.7% to 61.3%. Human evaluation confirms annotators perceive significantly higher personalization in routing-enabled responses. Our results establish that identity-aware user routing is the critical component for preventing persona confusion in multi-user conversational systems.

---


### 45. [Null Measurability at the Symmetrization Interface in VC Learning](https://arxiv.org/abs/2604.25028)

**<font color=#1a73e8>作者：</font>** Dhruv Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work revisiting measurability in the fundamental theorem of statistical learning imposes Borel measurability of ghost-gap suprema. We show that, at the one-sided ghost-gap interface actually used by the standard symmetrization proof, this requirement is stronger than necessary. For any Borel-parameterized concept class on a Polish domain, the bad event "there exists a hypothesis whose ghost empirical error exceeds its training empirical error by at least {\epsilon}/2" is analytic. By Choquet capacitability, it is therefore measurable in the completion of every finite Borel measure. We then construct a concept class whose bad event is null-measurable but not Borel, giving a strict separation from the Borel supremum condition. Finally, we prove closure under patching, fixed and countable interpolation, and fiber-product amalgamation, showing that the weaker regularity level is stable under natural concept-class constructors. In the realizable setting, where targets belong to the class and are measurable, these results weaken the measurability hypothesis needed by the symmetrization route from finite VC dimension to PAC learnability. The main results and the descriptive-set-theoretic infrastructure used by them are formalized in Lean 4.

---


### 46. [Faithful Autoformalization via Roundtrip Verification and Repair](https://arxiv.org/abs/2604.25031)

**<font color=#1a73e8>作者：</font>** Daneshvar Amrollahi, Jerry Lopez, Clark Barrett  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When an LLM formalizes natural language, how do we know the output is faithful? We propose a roundtrip verification approach which does not require ground-truth annotations: formalize a statement, translate the result back to natural language, re-formalize, and use a formal tool to check logical equivalence. When the two formalizations agree, this provides evidence of a faithful formalization. When they disagree, a diagnosis step identifies which translation stage failed, and a targeted repair operator attempts to correct that stage. We evaluate our approach on 150 traffic rules using Claude Opus 4.6 and GPT-5.2. Diagnosis-guided repair raises formal equivalence from 45--61% to 83--85% for both models, outperforming a random-repair baseline. An independent NLI analysis confirms that formal equivalence is correlated with less semantic drift.

---


### 47. [Dual-Track CoT: Budget-Aware Stepwise Guidance for Small LMs](https://arxiv.org/abs/2604.25039)

**<font color=#1a73e8>作者：</font>** Sagnik Chatterjee, Atharva Patil, Sricharan Ramesh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) solve many reasoning tasks via chain-of-thought (CoT) prompting, but smaller models (about 7 to 8B parameters) still struggle with multi-step reasoning under tight compute and token budgets. Existing test time reasoning methods such as self consistency (sampling multiple rationales and voting), Tree-of-Thoughts (search over intermediate thoughts), and critique revise loops improve performance, but often at high token cost and without fine-grained step-level control. This project1 aims to address that gap: can Small Language Models (SLMs) reason reliably using the same or fewer tokens? This question is both scientific and practical. Scientifically, it probes whether process supervision and simple test-time controls (such as token budgets and rejection of redundant steps) can substitute for model scale or large sampling counts. Practically, many deployments (on-device, low-latency, or cost-constrained settings) cannot afford huge models or dozens of sampled rationales per query. A method that improves SLM reasoning at fixed cost would therefore be directly useful.

---


### 48. [CiteRadar: A Citation Intelligence Platform for Researcher Profiling and Geographic Visualization](https://arxiv.org/abs/2604.25057)

**<font color=#1a73e8>作者：</font>** Chenxu Niu, Yiming Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the geographic reach and community structure of one's scholarly citations is increasingly valuable for career development, grant applications, and collaboration discovery -- yet accessible tools for answering these questions remain scarce. Existing bibliometric platforms either require costly institutional subscriptions or expose only aggregate citation counts without granular per-author metadata. We present CiteRadar, an open-source system that accepts a single Google Scholar user identifier and automatically produces a structured output folder containing: the author's complete publication list, all retrieved citing papers with enriched author metadata, two ranked author tables (by citation frequency and by h-index), a plain-text statistical summary, and a self-contained interactive HTML world map -- all from a single command-line invocation. CiteRadar integrates five heterogeneous data sources -- Google Scholar, OpenAlex, CrossRef, Semantic Scholar, and OpenStreetMap Nominatim -- through a carefully engineered five-stage pipeline. Key technical contributions include: (1) a Scholar meta-string parser resilient to Unicode non-breaking-space separators, a pervasive but undocumented quirk in Scholar's HTML that silently corrupts venue and year fields when unhandled; (2) a two-stage author disambiguation system using stop-word-filtered institution name similarity to guard against the well-known same-name entity-merging failure mode in bibliometric databases, demonstrated to eliminate h-index attribution errors of up to 9x the correct value; (3) an OpenAlex web-URL to API-URL conversion fix that raises the fraction of author records with city-level location data from 0% to ~60%; and (4) a logarithmically-scaled interactive Folium world map with per-city researcher popups, rendered as a fully self-contained HTML file.

---


### 49. [ShapeY: A Principled Framework for Measuring Shape Recognition Capacity via Nearest-Neighbor Matching](https://arxiv.org/abs/2604.25065)

**<font color=#1a73e8>作者：</font>** Jong Woo Nam, Amanda S. Rios, Bartlett W. Mel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object recognition (OR) in humans relies heavily on shape cues and the ability to recognize objects across varying 3D viewpoints. Unlike humans, deep networks often rely on non-shape cues such as texture and background, leading to vulnerabilities in generalization and robustness. To address this gap, we introduce ShapeY, a novel and principled benchmarking framework designed to evaluate shape-based recognition capability in OR systems. ShapeY comprises 68,200 grayscale images of 200 3D objects rendered from multiple viewpoints and optionally subjected to non-shape ``appearance'' changes. Using a nearest-neighbor matching task, ShapeY specifically probes the fine-grained structure of an OR system's embedding space by evaluating whether object views are clustered by 3D shape similarity across varying 3D viewpoints and other non-shape changes. ShapeY provides a suite of quantitative and qualitative performance readouts, including error rate graphs, viewpoint tuning curves, histograms of positive and negative matching scores, and grids showing ordered best matches, which together offer a comprehensive evaluation of an OR system's shape understanding capability. Testing of 321 pre-trained networks with diverse architectures reveals significant challenges in achieving robust shape-based recognition: even state-of-the-art models struggle to generalize consistently across 3D viewpoint and appearance changes, and are prone to infrequent but egregious matches of objects of obviously completely different shape. ShapeY establishes a principled framework for advancing artificial vision systems toward human-like shape recognition capabilities, emphasizing the importance of disentangled and invariant object encodings.

---


### 50. [Frontier Coding Agents Can Now Implement an AlphaZero Self-Play Machine Learning Pipeline For Connect Four That Performs Comparably to an External Solver](https://arxiv.org/abs/2604.25067)

**<font color=#1a73e8>作者：</font>** Joshua Sherwood, Ben Aybar, Benjamin Kaplan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Forecasting when AI systems will become capable of meaningfully accelerating AI research is a central challenge for AI safety. Existing benchmarks measure broad capability growth, but may not provide ample early warning signals for recursive self-improvement. We propose measuring AI's capability to autonomously implement end-to-end machine learning pipelines from past AI research breakthroughs, given a minimal task description. By providing a concise task description instead of the full prior work as reference, we hope to better elicit emerging AI research taste. We introduce a proof-of-concept benchmark in which frontier coding agents autonomously implement an AlphaZero-style machine learning pipeline for Connect Four on consumer hardware within a three-hour budget, and we evaluate the resulting game AIs in a round-robin tournament anchored to the Pascal Pons Connect Four solver. Across four agents with eight trials each, we find substantial differentiation: Claude Opus 4.7 won as first-mover against Pons in seven of eight trials, statistically significantly better than the other agents tested, none of which exceeded two of eight. The task, which no frontier agent could reliably complete when we began development in January of 2026, is now near-saturation. Our evaluation also surfaced anomalous behavior in GPT-5.4, which consistently used far less of its allocated time budget than other agents. A follow-up 16-trial probe using shorter, less evaluation-coded prompts substantially increased GPT-5.4's time-budget usage, consistent with but not diagnostic of sandbagging; Bradley-Terry ratings across probe conditions showed only directional differences, despite significant differences in time-budget usage. We release our data, code, and prompts to support reproduction and extension.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-190](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
