# 📦 其他研究 | 2026年04月16日

> 本类共 **209** 篇论文

> 未进入大模型主领域展示范围的其他研究。

---

### 1. [The Non-Optimality of Scientific Knowledge: Path Dependence, Lock-In, and The Local Minimum Trap](https://arxiv.org/abs/2604.11828)

**<font color=#1a73e8>作者：</font>** Mohamed Mabrok  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Science is widely regarded as humanity's most reliable method for uncovering truths about the natural world. Yet the \emph{trajectory} of scientific discovery is rarely examined as an optimization problem in its own right. This paper argues that the body of scientific knowledge, at any given historical moment, represents a \emph{local optimum} rather than a global one--that the frameworks, formalisms, and paradigms through which we understand nature are substantially shaped by historical contingency, cognitive path dependence, and institutional lock-in. Drawing an analogy to gradient descent in machine learning, we propose that science follows the steepest local gradient of tractability, empirical accessibility, and institutional reward, and in doing so may bypass fundamentally superior descriptions of nature. We develop this thesis through detailed case studies spanning mathematics, physics, chemistry, biology, neuroscience, and statistical methodology. We identify three interlocking mechanisms of lock-in--cognitive, formal, and institutional--and argue that recognizing these mechanisms is a prerequisite for designing meta-scientific strategies capable of escaping local optima. We conclude by proposing concrete interventions and discussing the epistemological implications of our thesis for the philosophy of science.

---


### 2. [Uncertainty Quantification in CNN Through the Bootstrap of Convex Neural Networks](https://arxiv.org/abs/2604.11833)

**<font color=#1a73e8>作者：</font>** Hongfei Du, Emre Barut, Fang Jin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the popularity of Convolutional Neural Networks (CNN), the problem of uncertainty quantification (UQ) of CNN has been largely overlooked. Lack of efficient UQ tools severely limits the application of CNN in certain areas, such as medicine, where prediction uncertainty is critically important. Among the few existing UQ approaches that have been proposed for deep learning, none of them has theoretical consistency that can guarantee the uncertainty quality. To address this issue, we propose a novel bootstrap based framework for the estimation of prediction uncertainty. The inference procedure we use relies on convexified neural networks to establish the theoretical consistency of bootstrap. Our approach has a significantly less computational load than its competitors, as it relies on warm-starts at each bootstrap that avoids refitting the model from scratch. We further explore a novel transfer learning method so our framework can work on arbitrary neural networks. We experimentally demonstrate our approach has a much better performance compared to other baseline CNNs and state-of-the-art methods on various image datasets.

---


### 3. [Beyond Static Sandboxing: Learned Capability Governance for Autonomous AI Agents](https://arxiv.org/abs/2604.11839)

**<font color=#1a73e8>作者：</font>** Bronislav Sidik, Lior Rokach  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents built on open-source runtimes such as OpenClaw expose every available tool to every session by default, regardless of the task. A summarization task receives the same shell execution, subagent spawning, and credential access capabilities as a code deployment task, a 15x overprovision ratio that we call the capability overprovisioning problem. Existing defenses, including the NemoClaw container sandbox and the Cisco DefenseClaw skill scanner, address containment and threat detection but do not learn the minimum viable capability set for each task type.
We present Aethelgard, a four layer adaptive governance framework that enforces least privilege for AI agents through a learned policy. Layer 1, the Capability Governor, dynamically scopes which tools the agent is aware of in each session. Layer 3, the Safety Router, intercepts tool calls before execution using a hybrid rule based and fine tuned classifier. Layer 2, the RL Learning Policy, trains a PPO policy on the accumulated audit log to learn the minimum viable skill set for each task type.

---


### 4. [DBGL: Decay-aware Bipartite Graph Learning for Irregular Medical Time Series Classification](https://arxiv.org/abs/2604.11842)

**<font color=#1a73e8>作者：</font>** Jian Chen, Yuzhu Hu, Xiaoyan Yuan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregular Medical Time Series play a critical role in the clinical domain to better understand the patient's condition. However, inherent irregularity arising from heterogeneous sampling rates, asynchronous observations, and variable gaps poses key challenges for reliable modeling. Existing methods often distort temporal sampling irregularity and missingness patterns while failing to capture variable decay irregularity, resulting in suboptimal representations. To address these limitations, we introduce DBGL, Decay-Aware Bipartite Graph Learning for Irregular Medical Time Series. DBGL first introduces a patient-variable bipartite graph that simultaneously captures irregular sampling patterns without artificial alignment and adaptively models variable relationships for temporal sampling irregularity modeling, enhancing representation learning. To model variable decay irregularity, DBGL designs a novel node-specific temporal decay encoding mechanism that captures each variable's decay rates based on sampling interval, yielding a more accurate and faithful representation of irregular temporal dynamics. We evaluate the performance of DBGL on four publicly available datasets, and the results show that DBGL outperforms all baselines.

---


### 5. [UniMark: Unified Adaptive Multi-bit Watermarking for Autoregressive Image Generators](https://arxiv.org/abs/2604.11843)

**<font color=#1a73e8>作者：</font>** Yigit Yilmaz, Elena Petrova, Mehmet Kaya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Invisible watermarking for autoregressive (AR) image generation has recently gained attention as a means of protecting image ownership and tracing AI-generated content. However, existing approaches suffer from three key limitations: (1) they embed only zero-bit watermarks for binary verification, lacking the ability to convey multi-bit messages; (2) they rely on static codebook partitioning strategies that are vulnerable to security attacks once the partition is exposed; and (3) they are designed for specific AR architectures, failing to generalize across diverse AR paradigms. We propose \method{}, a training-free, unified watermarking framework for autoregressive image generators that addresses all three limitations. \method{} introduces three core components: \textbf{Adaptive Semantic Grouping (ASG)}, which dynamically partitions codebook entries based on semantic similarity and a secret key, ensuring both image quality preservation and security; \textbf{Block-wise Multi-bit Encoding (BME)}, which divides the token sequence into blocks and encodes different bits across blocks with error-correcting codes for reliable message transmission; and \textbf{a Unified Token-Replacement Interface (UTRI)} that abstracts the watermark embedding process to support both next-token prediction (e.g., LlamaGen) and next-scale prediction (e.g., VAR) paradigms. We provide theoretical analysis on detection error rates and embedding capacity. Extensive experiments on three AR models demonstrate that \method{} achieves state-of-the-art performance in image quality (FID), watermark detection accuracy, and multi-bit message extraction, while maintaining robustness against cropping, JPEG compression, Gaussian noise, blur, color jitter, and random erasing attacks.

---


### 6. [Evaluating Lightweight Block Cipher Payload Encryption for Real-Time CAN Traffic](https://arxiv.org/abs/2604.11853)

**<font color=#1a73e8>作者：</font>** Kevin Setterstrom, Jeremy Straub  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This study evaluates the feasibility of integrating lightweight block cipher payload encryption into a real-time embedded controller area network (CAN) node using a QT PY ESP32-S2 microcontroller. This work seeks to determine whether the use of a block cipher can prevent semantic taxonomy-based reverse engineering, which infers signal meaning from unencrypted CAN traffic using observation and statistical analysis. CAN payloads are encrypted using a lightweight block cipher and evaluated through experiments that measure timing impact, payload pattern observability, and correlation-based inference. Results indicate that encryption masks constant values and predictable signal patterns while preserving a 100 Hz transmission schedule. These findings suggest that lightweight payload encryption can reduce passive, observation based inference of CAN signal semantics on resource-constrained hardware with limited timing overhead impact.

---


### 7. [Subcritical Signal Propagation at Initialization in Normalization-Free Transformers](https://arxiv.org/abs/2604.11890)

**<font color=#1a73e8>作者：</font>** Sergey Alekseev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study signal propagation at initialization in transformers through the averaged partial Jacobian norm (APJN), a measure of gradient amplification across layers. We extend APJN analysis to transformers with bidirectional attention and permutation-symmetric input token configurations by deriving recurrence relations for activation statistics and APJNs across layers. Our theory predicts how attention modifies the asymptotic behavior of the APJN at large depth and matches APJNs measured in deep vision transformers. The criticality picture known from residual networks carries over to transformers: the pre-LayerNorm architecture exhibits power-law APJN growth, whereas transformers with LayerNorm replaced by elementwise $\tanh$-like nonlinearities have stretched-exponential APJN growth, indicating that the latter are subcritical. Applied to Dynamic Tanh (DyT) and Dynamic erf (Derf) transformers, the theory explains why these architectures can be more sensitive to initialization and optimization choices and require careful tuning for stable training.

---


### 8. [Thermodynamic Liquid Manifold Networks: Physics-Bounded Deep Learning for Solar Forecasting in Autonomous Off-Grid Microgrids](https://arxiv.org/abs/2604.11909)

**<font color=#1a73e8>作者：</font>** Mohammed Ezzaldin Babiker Abdullah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The stable operation of autonomous off-grid photovoltaic systems requires solar forecasting algorithms that respect atmospheric thermodynamics. Contemporary deep learning models consistently exhibit critical anomalies, primarily severe temporal phase lags during cloud transients and physically impossible nocturnal power generation. To resolve this divergence between data-driven modeling and deterministic celestial mechanics, this research introduces the Thermodynamic Liquid Manifold Network. The methodology projects 22 meteorological and geometric variables into a Koopman-linearized Riemannian manifold to systematically map complex climatic dynamics. The architecture integrates a Spectral Calibration unit and a multiplicative Thermodynamic Alpha-Gate. This system synthesizes real-time atmospheric opacity with theoretical clear-sky boundary models, structurally enforcing strict celestial geometry compliance. This completely neutralizes phantom nocturnal generation while maintaining zero-lag synchronization during rapid weather shifts. Validated against a rigorous five-year testing horizon in a severe semi-arid climate, the framework achieves an RMSE of 18.31 Wh/m2 and a Pearson correlation of 0.988. The model strictly maintains a zero-magnitude nocturnal error across all 1826 testing days and exhibits a sub-30-minute phase response during high-frequency optical transients. Comprising exactly 63,458 trainable parameters, this ultra-lightweight design establishes a robust, thermodynamically consistent standard for edge-deployable microgrid controllers.

---


### 9. [How Transformers Learn to Plan via Multi-Token Prediction](https://arxiv.org/abs/2604.11912)

**<font color=#1a73e8>作者：</font>** Jianhao Huang, Zhanpeng Zhou, Renqiu Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While next-token prediction (NTP) has been the standard objective for training language models, it often struggles to capture global structure in reasoning tasks. Multi-token prediction (MTP) has recently emerged as a promising alternative, yet its underlying mechanisms remain poorly understood. In this paper, we study how MTP facilitates reasoning, with a focus on planning. Empirically, we show that MTP consistently outperforms NTP on both synthetic graph path-finding tasks and more realistic reasoning benchmarks, such as Countdown and boolean satisfiability problems. Theoretically, we analyze a simplified two-layer Transformer on a star graph task. We prove that MTP induces a two-stage reverse reasoning process: the model first attends to the end node and then reconstructs the path by tracing intermediate nodes backward. This behavior arises from a gradient decoupling property of MTP, which provides a cleaner training signal compared to NTP. Ultimately, our results highlight how multi-token objectives inherently bias optimization toward robust and interpretable reasoning circuits.

---


### 10. [V-Nutri: Dish-Level Nutrition Estimation from Egocentric Cooking Videos](https://arxiv.org/abs/2604.11913)

**<font color=#1a73e8>作者：</font>** Chengkun Yue, Chuanzhi Xu, Jiangpeng He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nutrition estimation of meals from visual data is an important problem for dietary monitoring and computational health, but existing approaches largely rely on single images of the finally completed dish. This setting is fundamentally limited because many nutritionally relevant ingredients and transformations, such as oils, sauces, and mixed components, become visually ambiguous after cooking, making accurate calorie and macronutrient estimation difficult. In this paper, we investigate whether the cooking process information from egocentric cooking videos can contribute to dish-level nutrition estimation. First, we further manually annotated the HD-EPIC dataset and established the first benchmark for video-based nutrition estimation. Most importantly, we propose V-Nutri, a staged framework that combines Nutrition5K-pretrained visual backbones with a lightweight fusion module that aggregates features from the final dish frame and cooking process keyframes extracted from the egocentric videos. V-Nutri also includes a cooking keyframes selection module, a VideoMamba-based event-detection model that targets ingredient-addition moments. Experiments on the HD-EPIC dataset show that process cues can provide complementary nutritional evidence, improving nutrition estimation under controlled conditions. Our results further indicate that the benefit of process keyframes depends strongly on backbone representation capacity and event detection quality. Our code and annotated dataset is available at this https URL.

---


### 11. [Self-Monitoring Benefits from Structural Integration: Lessons from Metacognition in Continuous-Time Multi-Timescale Agents](https://arxiv.org/abs/2604.11914)

**<font color=#1a73e8>作者：</font>** Ying Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-monitoring capabilities -- metacognition, self-prediction, and subjective duration -- are often proposed as useful additions to reinforcement learning agents. But do they actually help? We investigate this question in a continuous-time multi-timescale agent operating in predator-prey survival environments of varying complexity, including a 2D partially observable variant. We first show that three self-monitoring modules, implemented as auxiliary-loss add-ons to a multi-timescale cortical hierarchy, provide no statistically significant benefit across 20 random seeds, 1D and 2D predator-prey environments with standard and non-stationary variants, and training horizons up to 50,000 steps. Diagnosing the failure, we find the modules collapse to near-constant outputs (confidence std < 0.006, attention allocation std < 0.011) and the subjective duration mechanism shifts the discount factor by less than 0.03%. Policy sensitivity analysis confirms the agent's decisions are unaffected by module outputs in this design. We then show that structurally integrating the module outputs -- using confidence to gate exploration, surprise to trigger workspace broadcasts, and self-model predictions as policy input -- produces a medium-large improvement over the add-on approach (Cohen's d = 0.62, p = 0.06, paired) in a non-stationary environment. Component-wise ablations reveal that the TSM-to-policy pathway contributes most of this gain. However, structural integration does not significantly outperform a baseline with no self-monitoring (d = 0.15, p = 0.67), and a parameter-matched control without modules performs comparably, so the benefit may lie in recovering from the trend-level harm of ignored modules rather than in self-monitoring content. The architectural implication is that self-monitoring should sit on the decision pathway, not beside it.

---


### 12. [Can AI Detect Life? Lessons from Artificial Life](https://arxiv.org/abs/2604.11915)

**<font color=#1a73e8>作者：</font>** Ankit Gupta, Christoph Adami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning methods have been proposed to detect life in extraterrestrial samples, drawing on their ability to distinguish biotic from abiotic samples based on training models using natural and synthetic organic molecular mixtures. Here we show using Artificial Life that such methods are easily fooled into detecting life with near 100% confidence even if the analyzed sample is not capable of life. This is due to modern machine learning methods' propensity to be easily fooled by out-of-distribution samples. Because extra-terrestrial samples are very likely out of the distribution provided by terrestrial biotic and abiotic samples, using AI methods for life detection is bound to yield significant false positives.

---


### 13. [A Workflow to Efficiently Generate Dense Tissue Ground Truth Masks for Digital Breast Tomosynthesis](https://arxiv.org/abs/2604.11927)

**<font color=#1a73e8>作者：</font>** Tamerlan Mustafaev, Oleg Kruglov, Margarita Zuley 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital breast tomosynthesis (DBT) is now the standard of care for breast cancer screening in the USA. Accurate segmentation of fibroglandular tissue in DBT images is essential for personalized risk estimation, but algorithm development is limited by scarce human-delineated training data. In this study we introduce a time- and labor-saving framework to generate a human-annotated binary segmentation mask for dense tissue in DBT. Our framework enables a user to outline a rough region of interest (ROI) enclosing dense tissue on the central reconstructed slice of a DBT volume and select a segmentation threshold to generate the dense tissue mask. The algorithm then projects the ROI to the remaining slices and iteratively adjusts slice-specific thresholds to maintain consistent dense tissue delineation across the DBT volume. By requiring annotation only on the central slice, the framework substantially reduces annotation time and labor. We used 44 DBT volumes from the DBTex dataset for evaluation. Inter-reader agreement was assessed by computing patient-wise Dice similarity coefficients between segmentation masks produced by two radiologists, yielding a median of 0.84. Accuracy of the proposed method was evaluated by having a radiologist manually segment the 20th and 80th percentile slices from each volume (CC and MLO views; 176 slices total) and calculate Dice scores between the manual and proposed segmentations, yielding a median of 0.83.

---


### 14. [INTARG: Informed Real-Time Adversarial Attack Generation for Time-Series Regression](https://arxiv.org/abs/2604.11928)

**<font color=#1a73e8>作者：</font>** Gamze Kirman Tokgoz, Onat Gungor, Tajana Rosing 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting aims to predict future values by modeling temporal dependencies in historical observations. It is a critical component of many real-world systems, where accurate forecasts improve operational efficiency and help mitigate uncertainty and risk. More recently, machine learning (ML), and especially deep learning (DL)-based models, have gained widespread adoption for time-series forecasting, but they remain vulnerable to adversarial attacks. However, many state-of-the-art attack methods are not directly applicable in time-series settings, where storing complete historical data or performing attacks at every time step is often impractical. This paper proposes an adversarial attack framework for time-series forecasting under an online bounded-buffer setting, leveraging an informed and selective attack strategy. By selectively targeting time steps where the model exhibits high confidence and the expected prediction error is maximal, our framework produces fewer but substantially more effective attacks. Experiments show that our framework can increase the prediction error up to 2.42x, while performing attacks in fewer than 10% of time steps.

---


### 15. [Fast and principled equation discovery from chaos to climate](https://arxiv.org/abs/2604.11929)

**<font color=#1a73e8>作者：</font>** Yuzheng Zhang, Weizhen Li, Rui Carvalho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Our ability to predict, control, and ultimately understand complex systems rests on discovering the equations that govern their dynamics. Identifying these equations directly from noisy, limited observations has therefore become a central challenge in data-driven science, yet existing library-based sparse regression methods force a compromise between automation, statistical rigor, and computational efficiency. Here we develop Bayesian-ARGOS, a hybrid framework that reconciles these demands by combining rapid frequentist screening with focused Bayesian inference, enabling automated equation discovery with principled uncertainty quantification at a fraction of the computational cost of existing methods. Tested on seven chaotic systems under varying data scarcity and noise levels, Bayesian-ARGOS outperforms two state-of-the-art methods in most scenarios. It surpasses SINDy in data efficiency for all systems and noise tolerance for six out of the seven, with a two-order-of-magnitude reduction in computational cost compared to bootstrap-based ARGOS. The probabilistic formulation additionally enables a suite of standard statistical diagnostics, including influence analysis and multicollinearity detection that expose failure modes otherwise opaque. When integrated with representation learning (SINDy-SHRED) for high dimensional sea surface temperature reconstruction, Bayesian-ARGOS increases the yield of valid latent equations with significantly improved long horizon stability. Bayesian-ARGOS thus provides a principled, automated, and computationally efficient route from scarce and noisy observations to interpretable governing equations, offering a practical framework for equation discovery across scales, from benchmark chaotic systems to the latent dynamics underlying global climate patterns.

---


### 16. [EigenCoin: sassanid coins classification based on Bhattacharyya distance](https://arxiv.org/abs/2604.11932)

**<font color=#1a73e8>作者：</font>** Rahele Allahverdi, Mohammad Mahdi Dehshibi, Azam Bastanfard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Solving pattern recognition problems using imbalanced databases is a hot topic, which entices researchers to bring it into focus. Therefore, we consider this problem in the application of Sassanid coins classification. Our focus is not only on proposing EigenCoin manifold with Bhattacharyya distance for the classification task, but also on testing the influence of the holistic and feature-based approaches. EigenCoin consists of three main steps namely manifold construction, mapping test data, and classification. Conducted experiments show EigenCoin outperformed other observed algorithms and achieved the accuracy from 9.45% up to 21.75%, while it has the capability of handling the over-fitting problem.

---


### 17. [A unified data format for managing diabetes time-series data: DIAbetes eXchange (DIAX)](https://arxiv.org/abs/2604.11944)

**<font color=#1a73e8>作者：</font>** Elliott C. Pryor, Marc D. Breton, Anas El Fathi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diabetes devices, including Continuous Glucose Monitoring (CGM), Smart Insulin Pens, and Automated Insulin Delivery systems, generate rich time-series data widely used in research and machine learning. However, inconsistent data formats across sources hinder sharing, integration, and analysis.
We present DIAX (DIAbetes eXchange), a standardized JSON-based format for unifying diabetes time-series data, including CGM, insulin, and meal signals. DIAX promotes interoperability, reproducibility, and extensibility, particularly for machine learning applications. An open-source repository provides tools for dataset conversion, cross-format compatibility, visualization, and community contributions. DIAX is a translational resource, not a data host, ensuring flexibility without imposing data-sharing constraints.
Currently, DIAX is compatible with other standardization efforts and supports major datasets (DCLP3, DCLP5, IOBP2, PEDAP, T1Dexi, Loop), totaling over 10 million patient-hours of data. this https URL

---


### 18. [ResBM: Residual Bottleneck Models for Low-Bandwidth Pipeline Parallelism](https://arxiv.org/abs/2604.11947)

**<font color=#1a73e8>作者：</font>** Alan Aboudib, Rodrigo Lopez Portillo A., Kalei Brady 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlocking large-scale low-bandwidth decentralized training has the potential to utilize otherwise untapped compute resources. In centralized settings, large-scale multi-node training is primarily enabled by data and pipeline parallelism, two techniques that require ultra-high-bandwidth communication. While efficient methods now exist for decentralized data parallelism, pipeline parallelism remains the primary challenge. Recent efforts, such as Subspace Models (SM), have claimed up to 100x activation compression but rely on complex constrained optimization and diverge from true end-to-end training. In this paper, we propose a different approach, based on an architecture designed from the ground up to be native to low-bandwidth communication environments while still applicable to any standard transformer-based architecture. We call this architecture the Residual Bottleneck Model or ResBM, it introduces a residual encoder-decoder bottleneck module across pipeline boundaries that can be trained end-to-end as part of the model's parameters while preserving an explicit low-rank identity path. We show that ResBMs achieve state-of-the-art 128x activation compression without significant loss in convergence rates and without significant memory or compute overhead.

---


### 19. [Active Imitation Learning for Thermal- and Kernel-Aware LFM Inference on 3D S-NUCA Many-Cores](https://arxiv.org/abs/2604.11948)

**<font color=#1a73e8>作者：</font>** Yixian Shen, Chaoyao Shen, Jan Deen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Foundation Model (LFM) inference is both memory- and compute-intensive, traditionally relying on GPUs. However, the limited availability and high cost have motivated the adoption of high-performance general-purpose CPUs, especially emerging 3D-stacked Static Non-Uniform Cache Architecture (3D S-NUCA) systems. These architectures offer enhanced bandwidth and locality but suffer from severe thermal challenges and uneven cache latencies due to 3D Networks-on-Chip (NoC). Optimal management of thread migration and V/f scaling is non-trivial due to LFM kernel diversity and system heterogeneity. Existing thermal management approaches often rely on oversimplified analytical models and lack adaptability. We propose AILFM, an Active Imitation Learning (AIL)-based scheduling framework that learns near-optimal thermal-aware scheduling policies from Oracle demonstrations with minimal run-time overhead. AILFM accounts for both core-level performance heterogeneity and kernel-specific behavior in LFMs to maintain thermal safety while maximizing performance. Extensive experiments show that AILFM outperforms state-of-the-art baselines and generalizes well across diverse LFM workloads.

---


### 20. [Fall Risk and Gait Analysis in Community-Dwelling Older Adults using World-Spaced 3D Human Mesh Recovery](https://arxiv.org/abs/2604.11961)

**<font color=#1a73e8>作者：</font>** Chitra Banarjee, Patrick Kwon, Ania Lipat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait assessment is a key clinical indicator of fall risk and overall health in older adults. However, standard clinical practice is largely limited to stopwatch-measured gait speed. We present a pipeline that leverages a 3D Human Mesh Recovery (HMR) model to extract gait parameters from recordings of older adults completing the Timed Up and Go (TUG) test. From videos recorded across different community centers, we extract and analyze spatiotemporal gait parameters, including step time, sit-to-stand duration, and step length. We found that video-derived step time was significantly correlated with IMU-based insole measurements. Using linear mixed effects models, we confirmed that shorter, more variable step lengths and longer sit-to-stand durations were predicted by higher self-rated fall risk and fear of falling. These findings demonstrate that our pipeline can enable accessible and ecologically valid gait analysis in community settings.

---


### 21. [The Linear Centroids Hypothesis: How Deep Network Features Represent Data](https://arxiv.org/abs/2604.11962)

**<font color=#1a73e8>作者：</font>** Thomas Walker, Ahmed Imtiaz Humayun, Randall Balestriero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying and understanding the features that a deep network (DN) extracts from its inputs to produce its outputs is a focal point of interpretability research. The Linear Representation Hypothesis (LRH) identifies features in terms of the linear directions formed by the inputs in a DN's latent space. However, the LRH is limited as it abstracts away from individual components (e.g., neurons and layers), is susceptible to identifying spurious features, and cannot be applied across sub-components (e.g., multiple layers). In this paper, we introduce the Linear Centroids Hypothesis (LCH) as a new framework for identifying the features of a DN. The LCH posits that features correspond to linear directions of centroids, which are vector summarizations of the functional behavior of a DN in a local region of its input space. Interpretability studies under the LCH can leverage existing LRH tools, such as sparse autoencoders, by applying them to the DN's centroids rather than to its latent activations. We demonstrate that doing so yields sparser feature dictionaries for DINO vision transformers, which also perform better on downstream tasks. The LCH also inspires novel approaches to interpretability; for example, LCH can readily identify circuits in GPT2-Large. For code to study the LCH this https URL .

---


### 22. [Narrative-Driven Paper-to-Slide Generation via ArcDeck](https://arxiv.org/abs/2604.11969)

**<font color=#1a73e8>作者：</font>** Tarik Can Ozden, Sachidanand VS, Furkan Horoz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce ArcDeck, a multi-agent framework that formulates paper-to-slide generation as a structured narrative reconstruction task. Unlike existing methods that directly summarize raw text into slides, ArcDeck explicitly models the source paper's logical flow. It first parses the input to construct a discourse tree and establish a global commitment document, ensuring the high-level intent is preserved. These structural priors then guide an iterative multi-agent refinement process, where specialized agents iteratively critique and revise the presentation outline before rendering the final visual layouts and designs. To evaluate our approach, we also introduce ArcBench, a newly curated benchmark of academic paper-slide pairs. Experimental results demonstrate that explicit discourse modeling, combined with role-specific agent coordination, significantly improves the narrative flow and logical coherence of the generated presentations.

---


### 23. [Classification of Epileptic iEEG using Topological Machine Learning](https://arxiv.org/abs/2604.11971)

**<font color=#1a73e8>作者：</font>** Sunia Tanweer, Narayan Puthanmadam Subramaniyam, Firas A. Khasawneh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Epileptic seizure detection from EEG signals remains challenging due to the high dimensionality and nonlinear, potentially stochastic, dynamics of neural activity. In this work, we investigate whether features derived from topological data analysis (TDA) can improve the classification of brain states in preictal, ictal and interictal iEEG recordings from epilepsy patients using multichannel data. We analyze data from 55 patients, significantly larger than many previous studies that rely on patient-specific models. Persistence diagrams derived from iEEG signals are vectorized using several TDA representations, including Carlsson coordinates, persistence images, and template functions. To understand how topological representations interact with modern machine learning pipelines, we conduct a large-scale ablation study across multiple iEEG frequency bands, dimensionality reduction techniques, feature representations, and classifier architectures. Our experiments show that dimension-reduced topological representations achieve up to 80\% balanced accuracy for three-class classification. Interestingly, classical machine learning models perform comparably to deep learning models, achieving up to 79.17\% balanced accuracy, suggesting that carefully designed topological features can substantially reduce model complexity requirements. In contrast, pipelines preserving the full multichannel feature structure exhibit severe overfitting due to the high-dimensional feature space. These findings highlight the importance of structure-preserving dimensionality reduction when applying topology-based representations to multichannel neural data.

---


### 24. [Multi-Head Residual-Gated DeepONet for Coherent Nonlinear Wave Dynamics](https://arxiv.org/abs/2604.11972)

**<font color=#1a73e8>作者：</font>** Zhiwei Fan, Yiming Pan, Daniel Coca  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coherent nonlinear wave dynamics are often strongly shaped by a compact set of physically meaningful descriptors of the initial state. Traditional neural operators typically treat the input-output mapping as a largely black-box high-dimensional regression problem, without explicitly exploiting this structured physical context. Common feature-integration strategies usually rely on direct concatenation or FiLM-style affine modulation in hidden latent spaces. Here we introduce a different paradigm, loosely inspired by the complementary roles of state evolution and physically meaningful observables in quantum mechanics: the wave field is learned through a standard DeepONet state pathway, while compact physical descriptors follow a parallel conditioning pathway and act as residual modulation factors on the state prediction. Based on this idea, we develop a Multi-Head Residual-Gated DeepONet (MH-RG), which combines a pre-branch residual modulator, a branch residual gate, and a trunk residual gate with a low-rank multi-head mechanism to capture multiple complementary conditioned response patterns without prohibitive parameter growth. We evaluate the framework on representative benchmarks including highly nonlinear conservative wave dynamics and dissipative trapped dynamics and further perform detailed mechanistic analyses of the learned multi-head gating behavior. Compared with feature-augmented baselines, MH-RG DeepONet achieves consistently lower error while better preserving phase coherence and the fidelity of physically relevant dynamical quantities.

---


### 25. [Exploring Concept Subspace for Self-explainable Text-Attributed Graph Learning](https://arxiv.org/abs/2604.11986)

**<font color=#1a73e8>作者：</font>** Xiaoxue Han, Libo Zhang, Zining Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Graph Concept Bottleneck (GCB) as a new paradigm for self-explainable text-attributed graph learning. GCB maps graphs into a subspace, concept bottleneck, where each concept is a meaningful phrase, and predictions are made based on the activation of these concepts. Unlike existing interpretable graph learning methods that primarily rely on subgraphs as explanations, the concept bottleneck provides a new form of interpretation. To refine the concept space, we apply the information bottleneck principle to focus on the most relevant concepts. This not only yields more concise and faithful explanations but also explicitly guides the model to "think" toward the correct decision. We empirically show that GCB achieves intrinsic interpretability with accuracy on par with black-box Graph Neural Networks. Moreover, it delivers better performance under distribution shifts and data perturbations, showing improved robustness and generalizability, benefitting from concept-guided prediction.

---


### 26. [Ultra-low-light computer vision using trained photon correlations](https://arxiv.org/abs/2604.11993)

**<font color=#1a73e8>作者：</font>** Mandar M. Sohoni, Jérémie Laydevant, Mathieu Ouellet 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Illumination using correlated photon sources has been established as an approach to allowing high-fidelity images to be reconstructed from noisy camera frames by taking advantage of the knowledge that signal photons are spatially correlated whereas detector clicks due to noise are uncorrelated. However, in computer-vision tasks, the goal is often not ultimately to reconstruct an image, but to make inferences about a scene -- such as what object is present. Here we show how correlated-photon illumination can be used to gain an advantage in a hybrid optical-electronic computer-vision pipeline for object recognition. We demonstrate correlation-aware training (CAT): end-to-end optimization of a trainable correlated-photon illumination source and a Transformer backend in a way that the Transformer can learn to benefit from the correlations, using a small number (<= 100) of shots. We show a classification accuracy enhancement of up to 15 percentage points over conventional, uncorrelated-illumination-based computer vision in ultra-low-light and noisy imaging conditions, as well as an improvement over using untrained correlated-photon illumination. Our work illustrates how specializing to a computer-vision task -- object recognition -- and training the pattern of photon correlations in conjunction with a digital backend allows us to push the limits of accuracy in highly photon-budget-constrained scenarios beyond existing methods focused on image reconstruction.

---


### 27. [Offline-Online Reinforcement Learning for Linear Mixture MDPs](https://arxiv.org/abs/2604.11994)

**<font color=#1a73e8>作者：</font>** Zhongjun Zhang, Sean R. Sinclair  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study offline-online reinforcement learning in linear mixture Markov decision processes (MDPs) under environment shift. In the offline phase, data are collected by an unknown behavior policy and may come from a mismatched environment, while in the online phase the learner interacts with the target environment. We propose an algorithm that adaptively leverages offline data. When the offline data are informative, either due to sufficient coverage or small environment shift, the algorithm provably improves over purely online learning. When the offline data are uninformative, it safely ignores them and matches the online-only performance. We establish regret upper bounds that explicitly characterize when offline data are beneficial, together with nearly matching lower bounds. Numerical experiments further corroborate our theoretical findings.

---


### 28. [Loss-Driven Bayesian Active Learning](https://arxiv.org/abs/2604.11995)

**<font color=#1a73e8>作者：</font>** Zhuoyue Huang, Freddie Bickford Smith, Tom Rainforth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The central goal of active learning is to gather data that maximises downstream predictive performance, but popular approaches have limited flexibility in customising this data acquisition to different downstream problems and losses. We propose a rigorous loss-driven approach to Bayesian active learning that allows data acquisition to directly target the loss associated with a given decision problem. In particular, we show how any loss can be used to derive a unique objective for optimal data acquisition. Critically, we then show that any loss taking the form of a weighted Bregman divergence permits analytic computation of a central component of its corresponding objective, making the approach applicable in practice. In regression and classification experiments with a range of different losses, we find our approach reduces test losses relative to existing techniques.

---


### 29. [The Second Challenge on Cross-Domain Few-Shot Object Detection at NTIRE 2026: Methods and Results](https://arxiv.org/abs/2604.11998)

**<font color=#1a73e8>作者：</font>** Xingyu Qiu, Yuqian Fu, Jiawei Geng 等 74 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-domain few-shot object detection (CD-FSOD) remains a challenging problem for existing object detectors and few-shot learning approaches, particularly when generalizing across distinct domains. As part of NTIRE 2026, we hosted the second CD-FSOD Challenge to systematically evaluate and promote progress in detecting objects in unseen target domains under limited annotation conditions. The challenge received strong community interest, with 128 registered participants and a total of 696 submissions. Among them, 31 teams actively participated, and 19 teams submitted valid final results. Participants explored a wide range of strategies, introducing innovative methods that push the performance frontier under both open-source and closed-source tracks. This report presents a detailed overview of the NTIRE 2026 CD-FSOD Challenge, including a summary of the submitted approaches and an analysis of the final results across all participating teams. Challenge Codes: this https URL.

---


### 30. [Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision](https://arxiv.org/abs/2604.12002)

**<font color=#1a73e8>作者：</font>** Yinghui He, Simran Kaur, Adithya Bhaskar 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current post-training methods in verifiable settings fall into two categories. Reinforcement learning (RLVR) relies on binary rewards, which are broadly applicable and powerful, but provide only sparse supervision during training. Distillation provides dense token-level supervision, typically obtained from an external teacher or using high-quality demonstrations. Collecting such supervision can be costly or unavailable. We propose Self-Distillation Zero (SD-Zero), a method that is substantially more training sample-efficient than RL and does not require an external teacher or high-quality demonstrations. SD-Zero trains a single model to play two roles: a Generator, which produces an initial response, and a Reviser, which conditions on that response and its binary reward to produce an improved response. We then perform on-policy self-distillation to distill the reviser into the generator, using the reviser's token distributions conditioned on the generator's response and its reward as supervision. In effect, SD-Zero trains the model to transform binary rewards into dense token-level self-supervision. On math and code reasoning benchmarks with Qwen3-4B-Instruct and Olmo-3-7B-Instruct, SD-Zero improves performance by at least 10% over the base models and outperforms strong baselines, including Rejection Fine-Tuning (RFT), GRPO, and Self-Distillation Fine-Tuning (SDFT), under the same question set and training sample budget. Extensive ablation studies show two novel characteristics of our proposed algorithm: (a) token-level self-localization, where the reviser can identify the key tokens that need to be revised in the generator's response based on reward, and (b) iterative self-evolution, where the improving ability to revise answers can be distilled back into generation performance with regular teacher synchronization.

---


### 31. [BayMOTH: Bayesian optiMizatiOn with meTa-lookahead -- a simple approacH](https://arxiv.org/abs/2604.12005)

**<font color=#1a73e8>作者：</font>** Rahman Ejaz, Varchas Gopalaswamy, Ricardo Luna 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) has for sequential optimization of expensive black-box functions demonstrated practicality and effectiveness in many real-world settings. Meta-Bayesian optimization (meta-BO) focuses on improving the sample efficiency of BO by making use of information from related tasks. Although meta-BO is sample-efficient when task structure transfers, poor alignment between meta-training and test tasks can cause suboptimal queries to be suggested during online optimization. To this end, we propose a simple meta-BO algorithm that utilizes related-task information when determined useful, falling back to lookahead otherwise, within a unified framework. We demonstrate competitiveness of our method with existing approaches on function optimization tasks, while retaining strong performance in low task-relatedness regimes where test tasks share limited structure with the meta-training set.

---


### 32. [When to Forget: A Memory Governance Primitive](https://arxiv.org/abs/2604.12007)

**<font color=#1a73e8>作者：</font>** Baris Simsek  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent memory systems accumulate experience but currently lack a principled operational metric for memory quality governance -- deciding which memories to trust, suppress, or deprecate as the agent's task distribution shifts. Write-time importance scores are static; dynamic management systems use LLM judgment or structural heuristics rather than outcome feedback. This paper proposes Memory Worth (MW): a two-counter per-memory signal that tracks how often a memory co-occurs with successful versus failed outcomes, providing a lightweight, theoretically grounded foundation for staleness detection, retrieval suppression, and deprecation decisions. We prove that MW converges almost surely to the conditional success probability p+(m) = Pr[y_t = +1 | m in M_t] -- the probability of task success given that memory m is retrieved -- under a stationary retrieval regime with a minimum exploration condition. Importantly, p+(m) is an associational quantity, not a causal one: it measures outcome co-occurrence rather than causal contribution. We argue this is still a useful operational signal for memory governance, and we validate it empirically in a controlled synthetic environment where ground-truth utility is known: after 10,000 episodes, the Spearman rank-correlation between Memory Worth and true utilities reaches rho = 0.89 +/- 0.02 across 20 independent seeds, compared to rho = 0.00 for systems that never update their assessments. A retrieval-realistic micro-experiment with real text and neural embedding retrieval (all-MiniLM-L6-v2) further shows stale memories crossing the low-value threshold (MW = 0.17) while specialist memories remain high-value (MW = 0.77) across 3,000 episodes. The estimator requires only two scalar counters per memory unit and can be added to architectures that already log retrievals and episode outcomes.

---


### 33. [Sample Complexity of Autoregressive Reasoning: Chain-of-Thought vs. End-to-End](https://arxiv.org/abs/2604.12013)

**<font color=#1a73e8>作者：</font>** Steve Hanneke, Idan Mehalel, Shay Moran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern large language models generate text autoregressively, producing tokens one at a time. To study the learnability of such systems, Joshi et al. (COLT 2025) introduced a PAC-learning framework for next-token generators, the primitive underlying autoregressive models. In this framework, an unknown next-token generator maps a sequence of tokens to the next token and is iteratively applied for $T$ steps, producing a chain of tokens whose final token constitutes the model's output. The learning task is to learn the input-output mapping induced by this autoregressive process. Depending on the available supervision, training examples may reveal only the final output (End-to-End supervision) or the entire generated chain (Chain-of-Thought supervision). This raises two natural questions: how the sample complexity depends on the generation length $T$, and how much Chain-of-Thought supervision can reduce this dependence.
In this work we give a nearly complete answer to both questions by uncovering a taxonomy of how the sample complexity scales with $T$. For End-to-End learning, we show that the landscape is remarkably rich: subject to mild conditions, essentially any growth rate $r(T)$ between constant and linear can arise as the sample complexity, and combined with the linear upper bound of Joshi et al., this yields an essentially complete characterization. In contrast, under Chain-of-Thought supervision we show that the sample complexity is independent of $T$, demonstrating that access to intermediate reasoning steps can eliminate the dependence on the generation length altogether. Our analysis introduces new combinatorial tools, and as corollaries we resolve several open questions posed by Joshi et al. regarding the dependence of learnability on the generation length and the role of Chain-of-Thought supervision.

---


### 34. [A longitudinal health agent framework](https://arxiv.org/abs/2604.12019)

**<font color=#1a73e8>作者：</font>** Georgianna, Rencong Jiang, Noémie Elhadad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although artificial intelligence (AI) agents are increasingly proposed to support potentially longitudinal health tasks, such as symptom management, behavior change, and patient support, most current implementations fall short of facilitating user intent and fostering accountability. This contrasts with prior work on supporting longitudinal needs, where follow-up, coherent reasoning, and sustained alignment with individuals' goals are critical for both effectiveness and safety. In this paper, we draw on established clinical and personal health informatics frameworks to define what it would mean to orchestrate longitudinal health interactions with AI agents. We propose a multi-layer framework and corresponding agent architecture that operationalizes adaptation, coherence, continuity, and agency across repeated interactions. Through representative use cases, we demonstrate how longitudinal agents can maintain meaningful engagement, adapt to evolving goals, and support safe, personalized decision-making over time. Our findings underscore both the promise and the complexity of designing systems capable of supporting health trajectories beyond isolated interactions, and we offer guidance for future research and development in multi-session, user-centered health AI.

---


### 35. [WiseOWL: A Methodology for Evaluating Ontological Descriptiveness and Semantic Correctness for Ontology Reuse and Ontology Recommendations](https://arxiv.org/abs/2604.12025)

**<font color=#1a73e8>作者：</font>** Aryan Singh Dalal, Maria Baloch, Asiyah Yu Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Semantic Web standardizes concept meaning for humans and machines, enabling machine-operable content and consistent interpretation that improves advanced analytics. Reusing ontologies speeds development and enforces consistency, yet selecting the optimal choice is challenging because authors lack systematic selection criteria and often rely on intuition that is difficult to justify, limiting reuse. To solve this, WiseOWL is proposed, a methodology with scoring and guidance to select ontologies for reuse. It scores four metrics: (i) Well-Described, measuring documentation coverage; (ii) Well-Defined, using state-of-the-art embeddings to assess label-definition alignment; (iii) Connection, capturing structural interconnectedness; and (iv) Hierarchical Breadth, reflecting hierarchical balance. WiseOWL outputs normalized 0-10 scores with actionable feedback. Implemented as a Streamlit app, it ingests OWL format, converts to RDF Turtle, and provides interactive visualizations. Evaluation across six ontologies, including the Plant Ontology (PO), Gene Ontology (GO), Semanticscience Integrated Ontology (SIO), Food Ontology (FoodON), Dublin Core (DC), and GoodRelations, demonstrates promising effectiveness.

---


### 36. [TriFit: Trimodal Fusion with Protein Dynamics for Mutation Fitness Prediction](https://arxiv.org/abs/2604.12026)

**<font color=#1a73e8>作者：</font>** Seungik Cho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the functional impact of single amino acid substitutions (SAVs) is central to understanding genetic disease and engineering therapeutic proteins. While protein language models and structure-based methods have achieved strong performance on this task, they systematically neglect protein dynamics; residue flexibility, correlated motions, and allosteric coupling are well-established determinants of mutational tolerance in structural biology, yet have not been incorporated into supervised variant effect predictors. We present TriFit, a multimodal framework that integrates sequence, structure, and protein dynamics through a four-expert Mixture-of-Experts (MoE) fusion module with trimodal cross-modal contrastive learning. Sequence embeddings are extracted via masked marginal scoring with ESM-2 (650M); structural embeddings from AlphaFold2-predicted C-alpha geometries; and dynamics embeddings from Gaussian Network Model (GNM) B-factors, mode shapes, and residue-residue cross-correlations. The MoE router adaptively weights modality combinations conditioned on the input, enabling protein-specific fusion without fixed modality assumptions. On the ProteinGym substitution benchmark (217 DMS assays, 696k SAVs), TriFit achieves AUROC 0.897 +/- 0.0002, outperforming all supervised baselines including Kermut (0.864) and ProteinNPT (0.844), and the best zero-shot model ESM3 (0.769). Ablation studies confirm that dynamics provides the largest marginal contribution over pairwise modality combinations, and TriFit achieves well-calibrated probabilistic outputs (ECE = 0.044) without post-hoc correction.

---


### 37. [Curvelet-Based Frequency-Aware Feature Enhancement for Deepfake Detection](https://arxiv.org/abs/2604.12028)

**<font color=#1a73e8>作者：</font>** Salar Adel Sabri, Ramadhan J. Mstafa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proliferation of sophisticated generative models has significantly advanced the realism of synthetic facial content, known as deepfakes, raising serious concerns about digital trust. Although modern deep learning-based detectors perform well, many rely on spatial-domain features that degrade under compression. This limitation has prompted a shift toward integrating frequency-domain representations with deep learning to improve robustness. Prior research has explored frequency transforms such as Discrete Cosine Transform (DCT), Fast Fourier Transform (FFT), and Wavelet Transform, among others. However, to the best of our knowledge, the Curvelet Transform, despite its superior directional and multiscale properties, remains entirely unexplored in the context of deepfake detection. In this work, we introduce a novel Curvelet-based detection approach that enhances feature quality through wedge-level attention and scale-aware spatial masking, both trained to selectively emphasize discriminative frequency components. The refined frequency cues are reconstructed and passed to a modified pretrained Xception network for classification. Evaluated on two compression qualities in the challenging FaceForensics++ dataset, our method achieves 98.48% accuracy and 99.96% AUC on FF++ low compression, while maintaining strong performance under high compression, demonstrating the efficacy and interpretability of Curvelet-informed forgery detection.

---


### 38. [Memory as Metabolism: A Design for Companion Knowledge Systems](https://arxiv.org/abs/2604.12034)

**<font color=#1a73e8>作者：</font>** Stefan Miteski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation remains the dominant pattern for giving LLMs persistent memory, but a visible cluster of personal wiki-style memory architectures emerged in April 2026 -- design proposals from Karpathy, MemPalace, and LLM Wiki v2 that compile knowledge into an interlinked artifact for long-term use by a single user. They sit alongside production memory systems that the major labs have shipped for over a year, and an active academic lineage including MemGPT, Generative Agents, Mem0, Zep, A-Mem, MemMachine, SleepGate, and Second Me. Within a 2026 landscape of emerging governance frameworks for agent context and memory -- including Context Cartography and MemOS -- this paper proposes a companion-specific governance profile: a set of normative obligations, a time-structured procedural rule, and testable conformance invariants for the specific failure mode of entrenchment under user-coupled drift in single-user knowledge wikis built on the LLM wiki pattern.
The design principle is that personal LLM memory is a companion system: its job is to mirror the user on operational dimensions (working vocabulary, load-bearing structure, continuity of context) and compensate on epistemic failure modes (entrenchment, suppression of contradicting evidence, Kuhnian ossification). Five operations implement this split -- TRIAGE, DECAY, CONTEXTUALIZE, CONSOLIDATE, AUDIT -- supported by memory gravity and minority-hypothesis retention. The sharpest prediction: accumulated contradictory evidence should have a structural path to updating a centrality-protected dominant interpretation through multi-cycle buffer pressure accumulation, a failure mode no existing benchmark captures. The safety story at the single-agent level is partial, and the paper is explicit about what it does and does not solve.

---


### 39. [SIR-Bench: Evaluating Investigation Depth in Security Incident Response Agents](https://arxiv.org/abs/2604.12040)

**<font color=#1a73e8>作者：</font>** Daniel Begimher, Cristian Leo, Jack Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present SIR-Bench, a benchmark of 794 test cases for evaluating autonomous security incident response agents that distinguishes genuine forensic investigation from alert parroting. Derived from 129 anonymized incident patterns with expert-validated ground truth, SIR-Bench measures not only whether agents reach correct triage decisions, but whether they discover novel evidence through active investigation. To construct SIR-Bench, we develop Once Upon A Threat (OUAT), a framework that replays real incident patterns in controlled cloud environments, producing authentic telemetry with measurable investigation outcomes. Our evaluation methodology introduces three complementary metrics: triage accuracy (M1), novel finding discovery (M2), and tool usage appropriateness (M3), assessed through an adversarial LLM-as-Judge that inverts the burden of proof -- requiring concrete forensic evidence to credit investigations. Evaluating our SIR agent on the benchmark demonstrates 97.1% true positive (TP) detection, 73.4% false positive (FP) rejection, and 5.67 novel key findings per case, establishing a baseline against which future investigation agents can be measured.

---


### 40. [VISTA: Validation-Informed Trajectory Adaptation via Self-Distillation](https://arxiv.org/abs/2604.12044)

**<font color=#1a73e8>作者：</font>** Eli Corn, Daphna Weinshall  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models may converge to suboptimal solutions despite strong validation accuracy, masking an optimization failure we term Trajectory Deviation. This is because as training proceeds, models can abandon high generalization states for specific data sub-populations, thus discarding previously learned latent features without triggering classical overfitting signals. To address this problem we introduce VISTA, an online self-distillation framework that enforces consistency along the optimization trajectory. Using a validation-informed Marginal Coverage score, VISTA identifies expert anchors, which are earlier model states that retain specialized competence over distinct data regions. A coverage-weighted ensemble of these anchors is integrated online during training, regularizing the loss landscape and preserving mastered knowledge. When evaluated across multiple benchmarks, VISTA demonstrates improved robustness and generalization over standard training and prior self-distillation methods, while a lightweight implementation reduces storage overhead by 90% without performance loss.

---


### 41. [REGREACT: Self-Correcting Multi-Agent Pipelines for Structured Regulatory Information Extraction](https://arxiv.org/abs/2604.12054)

**<font color=#1a73e8>作者：</font>** Mohammed Ali, Abdelrahman Abdallah, Adam Jatowt  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Extracting structured, machine-readable compliance criteria from regulatory documents remains an open challenge. Single-pass language models hallucinate structural elements, lose hierarchical relationships, and fail to resolve inter-document dependencies. We introduce \textsc{RegReAct}, a self-correcting multi-agent framework that decomposes regulatory information extraction into seven specialized stages, each with an \textit{Observe--Diagnose--Repair} (ODR) loop that validates outputs against the source, correcting not only model hallucinations but also cross-reference errors in the regulations themselves. To ensure structural accuracy, \textsc{RegReAct} constructs a typed criterion graph; to ensure completeness, it resolves external dependencies by retrieving, summarizing, and embedding referenced legal content inline, producing self-contained outputs. Applying \textsc{RegReAct} to three EU Taxonomy Delegated Acts, we construct a dataset comprising 242 activities with over 4,800 hierarchical criteria, thresholds, and enriched source summaries. Evaluation against a GPT-4o single-pass baseline confirms that \textsc{RegReAct} outperforms it across all structural and semantic metrics. Code and data will be made publicly available: this https URL

---


### 42. [Interpretable DNA Sequence Classification via Dynamic Feature Generation in Decision Trees](https://arxiv.org/abs/2604.12060)

**<font color=#1a73e8>作者：</font>** Nicolas Huynh, Krzysztof Kacprzyk, Ryan Sheridan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The analysis of DNA sequences has become critical in numerous fields, from evolutionary biology to understanding gene regulation and disease mechanisms. While deep neural networks can achieve remarkable predictive performance, they typically operate as black boxes. Contrasting these black boxes, axis-aligned decision trees offer a promising direction for interpretable DNA sequence analysis, yet they suffer from a fundamental limitation: considering individual raw features in isolation at each split limits their expressivity, which results in prohibitive tree depths that hinder both interpretability and generalization performance. We address this challenge by introducing DEFT, a novel framework that adaptively generates high-level sequence features during tree construction. DEFT leverages large language models to propose biologically-informed features tailored to the local sequence distributions at each node and to iteratively refine them with a reflection mechanism. Empirically, we demonstrate that DEFT discovers human-interpretable and highly predictive sequence features across a diverse range of genomic tasks.

---


### 43. [Mathematics Teachers Interactions with a Multi-Agent System for Personalized Problem Generation](https://arxiv.org/abs/2604.12066)

**<font color=#1a73e8>作者：</font>** Candace Walkington, Theodora Beauchamp, Fareya Ikram 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can increasingly adapt educational tasks to learners characteristics. In the present study, we examine a multi-agent teacher-in-the-loop system for personalizing middle school math problems. The teacher enters a base problem and desired topic, the LLM generates the problem, and then four AI agents evaluate the problem using criteria that each specializes in (mathematical accuracy, authenticity, readability, and realism). Eight middle school mathematics teachers created 212 problems in ASSISTments using the system and assigned these problems to their students. We find that both teachers and students wanted to modify the fine-grained personalized elements of the real-world context of the problems, signaling issues with authenticity and fit. Although the agents detected many issues with realism as the problems were being written, there were few realism issues noted by teachers and students in the final versions. Issues with readability and mathematical hallucinations were also somewhat rare. Implications for multi-agent systems for personalization that support teacher control are given.

---


### 44. [Privacy-Preserving Structureless Visual Localization via Image Obfuscation](https://arxiv.org/abs/2604.12068)

**<font color=#1a73e8>作者：</font>** Vojtech Panek, Patrik Beliansky, Zuzana Kukelova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual localization is the task of estimating the camera pose of an image relative to a scene representation. In practice, visual localization systems are often cloud-based. Naturally, this raises privacy concerns in terms of revealing private details through the images sent to the server or through the representations stored on the server. Privacy-preserving localization aims to avoid such leakage of private details. However, the resulting localization approaches are significantly more complex, slower, and less accurate than their non-privacy-preserving counterparts. In this paper, we consider structureless localization methods in the context of privacy preservation. Structureless methods represent the scene through a set of reference images with known camera poses and intrinsics. In contrast to existing methods proposing representations that are as privacy-preserving as possible, we study a simple image obfuscation approach based on common image operations, e.g., replacing RGB images with (semantic) segmentations. We show that existing structureless pipelines do not need any special adjustments, as modern feature matchers can match obfuscated images out of the box. The results are easy-to-implement pipelines that can ensure both the privacy of the query images and the scene representations. Detailed experiments on multiple datasets show that the resulting methods achieve state-of-the-art pose accuracy for privacy-preserving approaches.

---


### 45. [OpenTME: An Open Dataset of AI-powered H&E Tumor Microenvironment Profiles from TCGA](https://arxiv.org/abs/2604.12075)

**<font color=#1a73e8>作者：</font>** Maaike Galama, Nina Kozar-Gillan, Christina Embacher 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The tumor microenvironment (TME) plays a central role in cancer progression, treatment response, and patient outcomes, yet large-scale, consistent, and quantitative TME characterization from routine hematoxylin and eosin (H&E)-stained histopathology remains scarce. We introduce OpenTME, an open-access dataset of pre-computed TME profiles derived from 3,634 H&E-stained whole-slide images across five cancer types (bladder, breast, colorectal, liver, and lung cancer) from The Cancer Genome Atlas (TCGA). All outputs were generated using Atlas H&E-TME, an AI-powered application built on the Atlas family of pathology foundation models, which performs tissue quality control, tissue segmentation, cell detection and classification, and spatial neighborhood analysis, yielding over 4,500 quantitative readouts per slide at cell-level resolution. OpenTME is available for non-commercial academic research on Hugging Face. We will continue to expand OpenTME over time and anticipate it will serve as a resource for biomarker discovery, spatial biology research, and the development of computational methods for TME analysis.

---


### 46. [Robust Optimization for Mitigating Reward Hacking with Correlated Proxies](https://arxiv.org/abs/2604.12086)

**<font color=#1a73e8>作者：</font>** Zixuan Liu, Xiaolin Sun, Zizhan Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing robust reinforcement learning (RL) agents in the presence of imperfect reward signals remains a core challenge. In practice, agents are often trained with proxy rewards that only approximate the true objective, leaving them vulnerable to reward hacking, where high proxy returns arise from unintended or exploitative behaviors. Recent work formalizes this issue using r-correlation between proxy and true rewards, but existing methods like occupancy-regularized policy optimization (ORPO) optimize against a fixed proxy and do not provide strong guarantees against broader classes of correlated proxies. In this work, we formulate reward hacking as a robust policy optimization problem over the space of all r-correlated proxy rewards. We derive a tractable max-min formulation, where the agent maximizes performance under the worst-case proxy consistent with the correlation constraint. We further show that when the reward is a linear function of known features, our approach can be adapted to incorporate this prior knowledge, yielding both improved policies and interpretable worst-case rewards. Experiments across several environments show that our algorithms consistently outperform ORPO in worst-case returns, and offer improved robustness and stability across different levels of proxy-true reward correlation. These results show that our approach provides both robustness and transparency in settings where reward design is inherently uncertain. The code is available at this https URL.

---


### 47. [PC-MIL: Decoupling Feature Resolution from Supervision Scale in Whole-Slide Learning](https://arxiv.org/abs/2604.12100)

**<font color=#1a73e8>作者：</font>** Syed Fahim Ahmed, Gnanesh Rasineni, Florian Koehler 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide image (WSI) classification in computational pathology is commonly formulated as slide-level Multiple Instance Learning (MIL) with a single global bag representation. However, slide-level MIL is fundamentally underconstrained: optimizing only global labels encourages models to aggregate features without learning anatomically meaningful localization. This creates a mismatch between the scale of supervision and the scale of clinical reasoning. Clinicians assess tumor burden, focal lesions, and architectural patterns within millimeter-scale regions, whereas standard MIL is trained only to predict whether "somewhere in the slide there is cancer." As a result, the model's inductive bias effectively erases anatomical structure. We propose Progressive-Context MIL (PC-MIL), a framework that treats the spatial extent of supervision as a first-class design dimension. Rather than altering magnification, patch size, or introducing pixel-level segmentation, we decouple feature resolution from supervision scale. Using fixed 20x features, we vary MIL bag extent in millimeter units and anchor supervision at a clinically motivated 2mm scale to preserve comparable tumor burden and avoid confounding scale with lesion density. PC-MIL progressively mixes slide- and region-level supervision in controlled proportions, enabling explicit train-context x test-context analysis. On 1,476 prostate WSIs from five public datasets for binary cancer detection, we show that anatomical context is an independent axis of generalization in MIL, orthogonal to feature resolution: modest regional supervision improves cross-context performance, and balanced multi-context training stabilizes accuracy across slide and regional evaluation without sacrificing global performance. These results demonstrate that supervision extent shapes MIL inductive bias and support anatomically grounded WSI generalization.

---


### 48. [Spatial Atlas: Compute-Grounded Reasoning for Spatial-Aware Research Agent Benchmarks](https://arxiv.org/abs/2604.12102)

**<font color=#1a73e8>作者：</font>** Arun Sharma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce compute-grounded reasoning (CGR), a design paradigm for spatial-aware research agents in which every answerable sub-problem is resolved by deterministic computation before a language model is asked to generate. Spatial Atlas instantiates CGR as a single Agent-to-Agent (A2A) server that handles two challenging benchmarks: FieldWorkArena, a multimodal spatial question-answering benchmark spanning factory, warehouse, and retail environments, and MLE-Bench, a suite of 75 Kaggle machine learning competitions requiring end-to-end ML engineering. A structured spatial scene graph engine extracts entities and relations from vision descriptions, computes distances and safety violations deterministically, then feeds computed facts to large language models, thereby avoiding hallucinated spatial reasoning. Entropy-guided action selection maximizes information gain per step and routes queries across a three-tier frontier model stack (OpenAI + Anthropic). A self-healing ML pipeline with strategy-aware code generation, a score-driven iterative refinement loop, and a prompt-based leak audit registry round out the system. We evaluate across both benchmarks and show that CGR yields competitive accuracy while maintaining interpretability through structured intermediate representations and deterministic spatial computations.

---


### 49. [SOLARIS: Speculative Offloading of Latent-bAsed Representation for Inference Scaling](https://arxiv.org/abs/2604.12110)

**<font color=#1a73e8>作者：</font>** Zikun Liu, Liang Luo, Qianru Li 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in recommendation scaling laws have led to foundation models of unprecedented complexity. While these models offer superior performance, their computational demands make real-time serving impractical, often forcing practitioners to rely on knowledge distillation-compromising serving quality for efficiency. To address this challenge, we present SOLARIS (Speculative Offloading of Latent-bAsed Representation for Inference Scaling), a novel framework inspired by speculative decoding. SOLARIS proactively precomputes user-item interaction embeddings by predicting which user-item pairs are likely to appear in future requests, and asynchronously generating their foundation model representations ahead of time. This approach decouples the costly foundation model inference from the latency-critical serving path, enabling real-time knowledge transfer from models previously considered too expensive for online use. Deployed across Meta's advertising system serving billions of daily requests, SOLARIS achieves 0.67% revenue-driving top-line metrics gain, demonstrating its effectiveness at scale.

---


### 50. [PR-MaGIC: Prompt Refinement Via Mask Decoder Gradient Flow For In-Context Segmentation](https://arxiv.org/abs/2604.12113)

**<font color=#1a73e8>作者：</font>** Minjae Lee, Sungwoo Hur, Soojin Hwang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Foundation Models (VFMs) such as the Segment Anything Model (SAM) have significantly advanced broad use of image segmentation. However, SAM and its variants necessitate substantial manual effort for prompt generation and additional training for specific applications. Recent approaches address these limitations by integrating SAM into in-context (one/few shot) segmentation, enabling auto-prompting through semantic alignment between query and support images. Despite these efforts, they still generate sub-optimal prompts that degrade segmentation quality due to visual inconsistencies between support and query images. To tackle this limitation, we introduce PR-MaGIC (Prompt Refinement via Mask Decoder Gradient Flow for In-Context Segmentation), a training-free test-time framework that refines prompts via gradient flow derived from SAM's mask decoder. PR-MaGIC seamlessly integrates into in-context segmentation frameworks, being theoretically grounded yet practically stabilized through a simple top-1 selection strategy that ensures robust performance across samples. Extensive evaluations demonstrate that PR-MaGIC consistently improves segmentation quality across various benchmarks, effectively mitigating inadequate prompts without requiring additional training or architectural modifications.

---


### 51. [Aethon: A Reference-Based Replication Primitive for Constant-Time Instantiation of Stateful AI Agents](https://arxiv.org/abs/2604.12129)

**<font color=#1a73e8>作者：</font>** Swanand Rao, Kiran Kashalkar, Parvathi Somashekar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The transition from stateless model inference to stateful agentic execution is reshaping the systems assumptions underlying modern AI infrastructure. While large language models have made persistent, tool-using, and collaborative agents technically viable, existing runtime architectures remain constrained by materialization-heavy instantiation models that impose significant latency and memory overhead.
This paper introduces Aethon, a reference-based replication primitive for near-constant-time instantiation of stateful AI agents. Rather than reconstructing agents as fully materialized objects, Aethon represents each instance as a compositional view over stable definitions, layered memory, and local contextual overlays. By shifting instantiation from duplication to reference, Aethon decouples creation cost from inherited structure.
We present the conceptual framework, system architecture, and memory model underlying Aethon, including layered inheritance and copy-on-write semantics. We analyze its implications for complexity, scalability, multi-agent orchestration, and enterprise governance. We argue that reference-based instantiation is not merely an optimization, but a more appropriate systems abstraction for production-scale agentic software.
Aethon points toward a new class of AI infrastructure in which agents become lightweight, composable execution identities that can be spawned, specialized, and governed at scale.

---


### 52. [XANE(3): An E(3)-Equivariant Graph Neural Network for Accurate Prediction of XANES Spectra from Atomic Structures](https://arxiv.org/abs/2604.12140)

**<font color=#1a73e8>作者：</font>** Vitor F. Grizzi, Luke N. Pretzie, Jiayi Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present XANE(3), a physics-based E(3)-equivariant graph neural network for predicting X-ray absorption near-edge structure (XANES) spectra directly from atomic structures. The model combines tensor-product message passing with spherical harmonic edge features, absorber-query attention pooling, custom equivariant layer normalization, adaptive gated residual connections, and a spectral readout based on a multi-scale Gaussian basis with an optional sigmoidal background term. To improve line-shape fidelity, training is performed with a composite objective that includes pointwise spectral reconstruction together with first- and second-derivative matching terms. We evaluate the model on a dataset of 5,941 FDMNES simulations of iron oxide surface facets and obtain a spectrum mean squared error of $1.0 \times 10^{-3}$ on the test set. The model accurately reproduces the main edge structure, relative peak intensities, pre-edge features, and post-edge oscillations. Ablation studies show that the derivative-aware objective, custom equivariant normalization, absorber-conditioned attention pooling, adaptive gated residual mixing, and global background term each improve performance. Interestingly, a capacity-matched scalar-only variant achieves comparable pointwise reconstruction error but reduced derivative-level fidelity, indicating that explicit tensorial channels are not strictly required for low intensity error on this dataset, although they remain beneficial for capturing finer spectral structure. These results establish XANE(3) as an accurate and efficient surrogate for XANES simulation and offer a promising route toward accelerated spectral prediction, ML-assisted spectroscopy, and data-driven materials discovery.

---


### 53. [Domain-Specific Latent Representations Improve the Fidelity of Diffusion-Based Medical Image Super-Resolution](https://arxiv.org/abs/2604.12152)

**<font color=#1a73e8>作者：</font>** Sebastian Cajas, Ashaba Judith, Rahul Gorijavolu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models for medical image super-resolution universally inherit variational autoencoders designed for natural photographs. We show that this default choice, not the diffusion architecture, is the dominant constraint on reconstruction quality. In a controlled experiment holding all other pipeline components fixed, replacing the generic Stable Diffusion VAE with MedVAE, a domain-specific autoencoder pretrained on more than 1.6 million medical images, yields +2.91 to +3.29 dB PSNR improvement across knee MRI, brain MRI, and chest X-ray (n = 1,820; Cohen's d = 1.37 to 1.86, all p < 10^{-20}, Wilcoxon signed-rank). Wavelet decomposition localises the advantage to the finest spatial frequency bands encoding anatomically relevant fine structure. Ablations across inference schedules, prediction targets, and generative architectures confirm the gap is stable within plus or minus 0.15 dB, while hallucination rates remain comparable between methods (Cohen's h < 0.02 across all datasets), establishing that reconstruction fidelity and generative hallucination are governed by independent pipeline components. These results provide a practical screening criterion: autoencoder reconstruction quality, measurable without diffusion training, predicts downstream SR performance (R^2 = 0.67), suggesting that domain-specific VAE selection should precede diffusion architecture search. Code and trained model weights are publicly available at this https URL.

---


### 54. [VidTAG: Temporally Aligned Video to GPS Geolocalization with Denoising Sequence Prediction at a Global Scale](https://arxiv.org/abs/2604.12159)

**<font color=#1a73e8>作者：</font>** Parth Parag Kulkarni, Rohit Gupta, Prakash Chandra Chhipa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The task of video geolocalization aims to determine the precise GPS coordinates of a video's origin and map its trajectory; with applications in forensics, social media, and exploration. Existing classification-based approaches operate at a coarse city-level granularity and fail to capture fine-grained details, while image retrieval methods are impractical on a global scale due to the need for extensive image galleries which are infeasible to compile. Comparatively, constructing a gallery of GPS coordinates is straightforward and inexpensive. We propose VidTAG, a dual-encoder framework that performs frame-to-GPS retrieval using both self-supervised and language-aligned features. To address temporal inconsistencies in video predictions, we introduce the TempGeo module, which aligns frame embeddings, and the GeoRefiner module, an encoder-decoder architecture that refines GPS features using the aligned frame embeddings. Evaluations on Mapillary (MSLS) and GAMa datasets demonstrate our model's ability to generate temporally consistent trajectories and outperform baselines, achieving a 20% improvement at the 1 km threshold over GeoCLIP. We also beat current State-of-the-Art by 25% on global coarse grained video geolocalization (CityGuessr68k). Our approach enables fine-grained video geolocalization and lays a strong foundation for future research. More details on the project webpage: this https URL

---


### 55. [PubSwap: Public-Data Off-Policy Coordination for Federated RLVR](https://arxiv.org/abs/2604.12160)

**<font color=#1a73e8>作者：</font>** Anupam Nayak, Baris Askin, Muhammed Ustaomeroglu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning post-training with reinforcement learning from verifiable rewards (RLVR) is typically studied in centralized settings, yet many realistic applications involve decentralized private data distributed across organizations. Federated training is a natural solution, but scaling RLVR in this regime is challenging: full-model synchronization is expensive, and performing many local steps can cause severe client drift under heterogeneous data. We propose a federated RLVR framework that combines LoRA-based local adaptation with public-data-based off-policy steps to improve both communication efficiency and cross-client coordination. In particular, a small shared public dataset is used to periodically exchange and reuse response-level training signals across organizations, providing a lightweight anchor toward a more globally aligned objective without exposing private data. Our method selectively replaces locally incorrect responses with globally correct ones during public-data steps, thereby keeping training closer to the local policy while still benefiting from cross-client coordination. Across mathematical and medical reasoning benchmarks and models, our method consistently improves over standard baselines. Our results highlight a simple and effective recipe for federated reasoning post-training: combining low-rank communication with limited public-data coordination.

---


### 56. [Development, Evaluation, and Deployment of a Multi-Agent System for Thoracic Tumor Board](https://arxiv.org/abs/2604.12161)

**<font color=#1a73e8>作者：</font>** Tim Ellis-Caleo, Timothy Keyes, Nerissa Ambers 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tumor boards are multidisciplinary conferences dedicated to producing actionable patient care recommendations with live review of primary radiology and pathology data. Succinct patient case summaries are needed to drive efficient and accurate case discussions. We developed a manual AI-based workflow to generate patient summaries to display live at the Stanford Thoracic Tumor board. To improve on this manually intensive process, we developed several automated AI chart summarization methods and evaluated them against physician gold standard summaries and fact-based scoring rubrics. We report these comparative evaluations as well as our deployment of the final state automated AI chart summarization tool along with post-deployment monitoring. We also validate the use of an LLM as a judge evaluation strategy for fact-based scoring. This work is an example of integrating AI-based workflows into routine clinical practice.

---


### 57. [AlphaEval: Evaluating Agents in Production](https://arxiv.org/abs/2604.12162)

**<font color=#1a73e8>作者：</font>** Pengrui Lu, Bingyu Xu, Wenjun Zhang 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid deployment of AI agents in commercial settings has outpaced the development of evaluation methodologies that reflect production realities. Existing benchmarks measure agent capabilities through retrospectively curated tasks with well-specified requirements and deterministic metrics -- conditions that diverge fundamentally from production environments where requirements contain implicit constraints, inputs are heterogeneous multi-modal documents with information fragmented across sources, tasks demand undeclared domain expertise, outputs are long-horizon professional deliverables, and success is judged by domain experts whose standards evolve over time. We present AlphaEval, a production-grounded benchmark of 94 tasks sourced from seven companies deploying AI agents in their core business, spanning six O*NET (Occupational Information Network) domains. Unlike model-centric benchmarks, AlphaEval evaluates complete agent products -- Claude Code, Codex, etc. -- as commercial systems, capturing performance variations invisible to model-level evaluation. Our evaluation framework covers multiple paradigms (LLM-as-a-Judge, reference-driven metrics, formal verification, rubric-based assessment, automated UI testing, etc.), with individual domains composing multiple paradigms. Beyond the benchmark itself, we contribute a requirement-to-benchmark construction framework -- a systematic methodology that transforms authentic production requirements into executable evaluation tasks in minimal time. This framework standardizes the entire pipeline from requirement to evaluation, providing a reproducible, modular process that any organization can adopt to construct production-grounded benchmarks for their own domains.

---


### 58. [COBALT-TLA: A Neuro-Symbolic Verification Loop for Cross-Chain Bridge Vulnerability Discovery](https://arxiv.org/abs/2604.12172)

**<font color=#1a73e8>作者：</font>** Dominik Blain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present COBALT-TLA, a neuro-symbolic verification loop that pairs an LLM with TLC, the TLA+ model checker, in an automated REPL. The LLM generates bounded TLA+ specifications; TLC acts as a semantic oracle; structured error traces are parsed and injected back into the model's context to drive convergence. We evaluate the system against three cross-chain bridge targets, including a faithful model of the Nomad $190M exploit. COBALT-TLA reaches a verified BUG_FOUND state in at most 2 iterations on all targets, with TLC execution consistently below 0.30 seconds. Notably, the system autonomously discovers an unprompted vulnerability class -- the Optimistic Relay Attack -- not present in the human-written baseline specification. We argue that deterministic prover feedback is sufficient to neutralize LLM hallucination in formal methods, transforming zero-shot code generation into a convergent proof-finding strategy.

---


### 59. [Mitigating S-RAHA: An On-device Framework to Prevent Forwarding of Re-Captured Images](https://arxiv.org/abs/2604.12178)

**<font color=#1a73e8>作者：</font>** Keshav Sood, Iynkaran Natgunanathan, Purathani Praitheeshan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Protecting sensitive visual content from unauthorized redistribution is a growing challenge for privacy focused mobile applications, including dating platforms. Screenshot prevention mechanisms, rely on server side monitoring or are limited to digital screenshot detection, are commonly deployed to stop forwarding sensitive images. However, an adversary uses another smartphone to take a photo of the mobile screen, in this scenario the existing solutions offer no protection against psychically screen recapture attacks. Since the attack happens in the physical plane rather than on a digital plane and shows a void or hole in the existing solutions, we name this the Screen Recaptured Analog Hole Attack (S RAHA). Such physically recaptured images bypass digital safeguards and can be freely forwarded, creating substantial privacy, personal safety, and forensic risks. We present a low computational secure by design on device framework that aims to detect and prevent the forwarding of recaptured images directly to the users device. The proposed system integrates a deep learning assisted recapture detection model capable of distinguishing original digital content from camera to screen captures under diverse environmental conditions, together with an on device enforcement mechanism that automatically blocks the sharing of suspected recaptured images between applications. We also introduce the concept of an invisible metadata identifier (IMI) that can be embedded into protected images to enable forensic traceability of potential leakage paths. Although the IMI component is explored at a conceptual and feasibility level rather than fully implemented, it demonstrates a promising direction for integrating lightweight, invisible identifiers into client side security architectures.

---


### 60. [CycloneMAE: A Scalable Multi-Task Learning Model for Global Tropical Cyclone Probabilistic Forecasting](https://arxiv.org/abs/2604.12180)

**<font color=#1a73e8>作者：</font>** Renlong Hang, Zihao Xu, Jiuwei Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tropical cyclones (TCs) rank among the most destructive natural hazards, yet their forecasting faces fundamental trade-offs: numerical weather prediction (NWP) models are computationally prohibitive and struggle to leverage historical data, while existing deep learning (DL)-based intelligent models are variable-specific and deterministic, which fail to generalize across different forecasting variables. Here we present CycloneMAE, a scalable multi-task forecasting model that learns transferable TC representations from multi-modal data using a TC structure-aware masked autoencoder. By coupling a discrete probabilistic gridding mechanism with a pre-train/fine-tune paradigm, CycloneMAE simultaneously delivers deterministic forecasts and probability distributions. Evaluated across five global ocean basins, CycloneMAE outperforms leading NWP systems in pressure and wind forecasting up to 120 hours and in track forecasting up to 24 hours. Attribution analysis via integrated gradients reveals physically interpretable learning dynamics: short-term forecasts rely predominantly on the internal core convective structure from satellite imagery, whereas longer-term forecasts progressively shift attention to external environmental factors. Our framework establishes a scalable, probabilistic, and interpretable pathway for operational TC forecasting.

---


### 61. [Clustering-Enhanced Domain Adaptation for Cross-Domain Intrusion Detection in Industrial Control Systems](https://arxiv.org/abs/2604.12183)

**<font color=#1a73e8>作者：</font>** Luyao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial control systems operate in dynamic environments where traffic distributions vary across scenarios, labeled samples are limited, and unknown attacks frequently emerge, posing significant challenges to cross-domain intrusion detection. To address this issue, this paper proposes a clustering-enhanced domain adaptation method for industrial control traffic. The framework contains two key components. First, a feature-based transfer learning module projects source and target domains into a shared latent subspace through spectral-transform-based feature alignment and iteratively reduces distribution discrepancies, enabling accurate cross-domain detection. Second, a clustering enhancement strategy combines K-Medoids clustering with PCA-based dimensionality reduction to improve cross-domain correlation estimation and reduce performance degradation caused by manual parameter tuning. Experimental results show that the proposed method significantly improves unknown attack detection. Compared with five baseline models, it increases detection accuracy by up to 49%, achieves larger gains in F-score, and demonstrates stronger stability. Moreover, the clustering enhancement strategy further boosts detection accuracy by up to 26% on representative tasks. These results suggest that the proposed method effectively alleviates data scarcity and domain shift, providing a practical solution for robust cross-domain intrusion detection in dynamic industrial environments.

---


### 62. [TRUST Agents: A Collaborative Multi-Agent Framework for Fake News Detection, Explainable Verification, and Logic-Aware Claim Reasoning](https://arxiv.org/abs/2604.12184)

**<font color=#1a73e8>作者：</font>** Gautama Shastry Bulusu Venkata, Santhosh Kakarla, Maheedhar Omtri Mohan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> TRUST Agents is a collaborative multi-agent framework for explainable fact verification and fake news detection. Rather than treating verification as a simple true-or-false classification task, the system identifies verifiable claims, retrieves relevant evidence, compares claims against that evidence, reasons under uncertainty, and generates explanations that humans can inspect. The baseline pipeline consists of four specialized agents. A claim extractor uses named entity recognition, dependency parsing, and LLM-based extraction to identify factual claims. A retrieval agent performs hybrid sparse and dense search using BM25 and FAISS. A verifier agent compares claims with retrieved evidence and produces verdicts with calibrated confidence. An explainer agent then generates a human-readable report with explicit evidence citations. To handle complex claims more effectively, we introduce a research-oriented extension with three additional components: a decomposer agent inspired by LoCal-style claim decomposition, a Delphi-inspired multi-agent jury with specialized verifier personas, and a logic aggregator that combines atomic verdicts using conjunction, disjunction, negation, and implication. We evaluate both pipelines on the LIAR benchmark against fine-tuned BERT, fine-tuned RoBERTa, and a zero-shot LLM baseline. Although supervised encoders remain stronger on raw metrics, TRUST Agents improves interpretability, evidence transparency, and reasoning over compound claims. Results also show that retrieval quality and uncertainty calibration remain the main bottlenecks in trustworthy automated fact verification.

---


### 63. [Representing expertise accelerates learning from pedagogical interaction data](https://arxiv.org/abs/2604.12195)

**<font color=#1a73e8>作者：</font>** Dhara Yu, Karthikeya Kaushik, Bill D. Thompson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Work in cognitive science and artificial intelligence has suggested that exposing learning agents to traces of interaction between multiple individuals can improve performance in a variety of settings, yet it remains unknown which features of interactions contribute to this improvement. We examined the factors that support the effectiveness of interaction data, using a controlled paradigm that allowed us to precisely operationalize key distinctions between interaction and an expert acting alone. We generated synthetic datasets of simple interactions between an expert and a novice in a spatial navigation task, and then trained transformer models on those datasets, evaluating performance after exposure to different datasets. Our experiments showed that models trained on pedagogical interactions were more robust across a variety of scenarios compared to models trained only on expert demonstrations, and that having the ability to represent epistemically distinct agents led to expert-like behavior even when expert behavior was rarely observed.

---


### 64. [Latent patterns of urban mixing in mobility analysis across five global cities](https://arxiv.org/abs/2604.12202)

**<font color=#1a73e8>作者：</font>** Z. Fan, B. P. Y. Loo, F. Duarte 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study leverages large-scale travel surveys for over 200,000 residents across Boston, Chicago, Hong Kong, London, and Sao Paulo. With rich individual-level data, we make systematic comparisons and reveal patterns in social mixing, which cannot be identified by analyzing high-resolution mobility data alone. Using the same set of data, inferring socioeconomic status from residential neighborhoods yield social mixing levels 16% lower than using self-reported survey data. Besides, individuals over the age of 66 experience greater social mixing than those in late working life (aged 55 to 65), lending data-driven support to the "second youth" hypothesis. Teenagers and women with caregiving responsibilities exhibit lower social mixing levels. Across the five cities, proximity to major transit stations reduces the influence of individual socioeconomic status on social mixing. Finally, we construct detailed spatio-temporal place networks for each city using a graph neural network. Inputs of home-space, activity-space and demographic attributes are embedded and fed into a supervised autoencoder to predict individual exposure vectors. Results show that the structure of individual activity space, i.e., where people travel to, explains most of the variations in place exposure, suggesting that mobility shapes experienced social mixing more than sociodemographic characteristics, home environment, and transit proximity. The ablation tests further discover that, while different income groups may experience similar levels of social mixing, their activity spaces remain stratified by income, resulting in structurally different social mixing experiences.

---


### 65. [Socially Fluent, Socially Awkward: Artificial Intelligence Relational Talk Backfires in Commercial Interactions](https://arxiv.org/abs/2604.12206)

**<font color=#1a73e8>作者：</font>** Stephanie Kwari Dharmaputri, Anish Nagpal, Greg Nyilasy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Advancements in Artificial Intelligence (AI) technologies' social fluency are being integrated into commercial interactions. As tools such as OpenAI's assistant are integrated into platforms such as Shopify, Klarna, and Visa, understanding consumer responses to AI social features become essential. One such feature is relational talk, an informal and non-obligatory social communication embedded in transactional exchanges. Across four experiments, we find: 1) a negative main effect of AI relational talk on satisfaction, mediated by expectancy violation and perceived interaction awkwardness, and 2) goal-relevant relational talk to attenuate this effect. This paper extends the literature by challenging the assumption that increased social fluency will improve satisfaction, and highlights the complexity of integrating social features into AI systems. It also identifies awkwardness as a key emotional response and barrier to effective human-AI interaction, showing that even in the absence of real social repercussions, perceived awkwardness in AI-led commercial interactions can elicit negative responses.

---


### 66. [Beyond Prompt: Fine-grained Simulation of Cognitively Impaired Standardized Patients via Stochastic Steering](https://arxiv.org/abs/2604.12210)

**<font color=#1a73e8>作者：</font>** Weikang Zhang, Zimo Zhu, Zhichuan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulating Standardized Patients with cognitive impairment offers a scalable and ethical solution for clinical training. However, existing methods rely on discrete prompt engineering and fail to capture the heterogeneity of deficits across varying domains and severity levels. To address this limitation, we propose StsPatient for the fine-grained simulation of cognitively impaired patients. We innovatively capture domain-specific features by extracting steering vectors from contrastive pairs of instructions and responses. Furthermore, we introduce a Stochastic Token Modulation (STM) mechanism to regulate the intervention probability. STM enables precise control over impairment severity while mitigating the instability of conventional vector methods. Comprehensive experiments demonstrate that StsPatient significantly outperforms baselines in both clinical authenticity and severity controllability.

---


### 67. [A Residual-Shell-Based Lower Bound for Ollivier-Ricci Curvature](https://arxiv.org/abs/2604.12211)

**<font color=#1a73e8>作者：</font>** Xiang Gu, Huichun Zhang, Jian Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ollivier-Ricci curvature (ORC), defined via the Wasserstein distance that captures rich geometric information, has received growing attention in both theory and applications. However, the high computational cost of Wasserstein distance evaluation has significantly limited the broader practical use of ORC. To alleviate this issue, previous work introduced a computationally efficient lower bound as a proxy for ORC based on 1-hop random walks, but this approach empirically exhibits large gaps from the exact ORC. In this paper, we establish a substantially tighter lower bound for ORC than the existing lower bound, while retaining much lower computational cost than exact ORC computation, with practical speedups of tens of times. Moreover, our bound is not restricted to 1-hop random walks, but also applies to k-hop random walks (k > 1). Experiments on several fundamental graph structures demonstrate the effectiveness of our bound in terms of both approximation accuracy and computational efficiency.

---


### 68. [TimeMark: A Trustworthy Time Watermarking Framework for Exact Generation-Time Recovery from AIGC](https://arxiv.org/abs/2604.12216)

**<font color=#1a73e8>作者：</font>** Shangkun Che, Silin Du, Ge Gao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The widespread use of Large Language Models (LLMs) in text generation has raised increasing concerns about intellectual property disputes. Watermarking techniques, which embed meta information into AI-generated content (AIGC), have the potential to serve as judicial evidence. However, existing methods rely on statistical signals in token distributions, leading to inherently probabilistic detection and reduced reliability, especially in multi-bit encoding (e.g., timestamps). Moreover, such methods introduce detectable statistical patterns, making them vulnerable to forgery attacks and enabling model providers to fabricate arbitrary watermarks. To address these issues, we propose the concept of trustworthy watermark, which achieves reliable recovery with 100% identification accuracy while resisting both user-side statistical attacks and provider-side forgery. We focus on trustworthy time watermarking for use as judicial evidence. Our framework integrates cryptographic techniques and encodes time information into time-dependent secret keys under regulatory supervision, preventing arbitrary timestamp fabrication. The watermark payload is decoupled from time and generated as a random, non-stored bit sequence for each instance, eliminating statistical patterns. To ensure verifiability, we design a two-stage encoding mechanism, which, combined with error-correcting codes, enables reliable recovery of generation time with theoretically perfect accuracy. Both theoretical analysis and experiments demonstrate that our framework satisfies the reliability requirements for judicial evidence and offers a practical solution for future AIGC-related intellectual property disputes.

---


### 69. [Ride the Wave: Precision-Allocated Sparse Attention for Smooth Video Generation](https://arxiv.org/abs/2604.12219)

**<font color=#1a73e8>作者：</font>** Wentai Zhang, Ronghui Xi, Shiyao Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Diffusion Transformers have revolutionized high-fidelity video generation but suffer from the massive computational burden of self-attention. While sparse attention provides a promising acceleration solution, existing methods frequently provoke severe visual flickering caused by static sparsity patterns and deterministic block routing. To resolve these limitations, we propose Precision-Allocated Sparse Attention (PASA), a training-free framework designed for highly efficient and temporally smooth video generation. First, we implement a curvature-aware dynamic budgeting mechanism. By profiling the generation trajectory acceleration across timesteps, we elastically allocate the exact-computation budget to secure high-precision processing strictly during critical semantic transitions. Second, we replace global homogenizing estimations with hardware-aligned grouped approximations, successfully capturing fine-grained local variations while maintaining peak compute throughput. Finally, we incorporate a stochastic selection bias into the attention routing mechanism. This probabilistic approach softens rigid selection boundaries and eliminates selection oscillation, effectively eradicating the localized computational starvation that drives temporal flickering. Extensive evaluations on leading video diffusion models demonstrate that PASA achieves substantial inference acceleration while consistently producing remarkably fluid and structurally stable video sequences.

---


### 70. [BarbieGait: An Identity-Consistent Synthetic Human Dataset with Versatile Cloth-Changing for Gait Recognition](https://arxiv.org/abs/2604.12221)

**<font color=#1a73e8>作者：</font>** Qingyuan Cai, Saihui Hou, Xuecai Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait recognition, as a reliable biometric technology, has seen rapid development in recent years while it faces significant challenges caused by diverse clothing styles in the real world. This paper introduces BarbieGait, a synthetic gait dataset where real-world subjects are uniquely mapped into a virtual engine to simulate extensive clothing changes while preserving their gait identity information. As a pioneering work, BarbieGait provides a controllable gait data generation method, enabling the production of large datasets to validate cross-clothing issues that are difficult to verify with real-world data. However, the diversity of clothing increases intra-class variance and makes one of the biggest challenges to learning cloth-invariant features under varying clothing conditions. Therefore, we propose GaitCLIF (Gait-oriented CLoth-Invariant Feature) as a robust baseline model for cross-clothing gait recognition. Through extensive experiments, we validate that our method significantly improves cross-clothing performance on BarbieGait and the existing popular gait benchmarks. We believe that BarbieGait, with its extensive cross-clothing gait data, will further advance the capabilities of gait recognition in cross-clothing scenarios and promote progress in related research.

---


### 71. [Physics-Grounded Monocular Vehicle Distance Estimation Using Standardized License Plate Typography](https://arxiv.org/abs/2604.12239)

**<font color=#1a73e8>作者：</font>** Manognya Lokesh Reddy, Zheng Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate inter-vehicle distance estimation is a cornerstone of Advanced Driver Assistance Systems (ADAS) and autonomous driving. While LiDAR and radar provide high precision, their high cost prohibits widespread adoption in mass-market vehicles. Monocular camera-based estimation offers a low-cost alternative but suffers from fundamental scale ambiguity. Recent deep learning methods for monocular depth achieve impressive results yet require expensive supervised training, suffer from domain shift, and produce predictions that are difficult to certify for safety-critical deployment. This paper presents a framework that exploits the standardized typography of United States license plates as passive fiducial markers for metric ranging, resolving scale ambiguity through explicit geometric priors without any training data or active illumination. First, a four-method parallel plate detector achieves robust plate reading across the full automotive lighting range. Second, a three-stage state identification engine fusing OCR text matching, multi-design color scoring, and a lightweight neural network classifier provides robust identification across all ambient conditions. Third, hybrid depth fusion with inverse-variance weighting and online scale alignment, combined with a one-dimensional constant-velocity Kalman filter, delivers smoothed distance, relative velocity, and time-to-collision for collision warning. Baseline validation reproduces a 2.3% coefficient of variation in character height measurements and a 36% reduction in distance-estimate variance compared with plate-width methods from prior work. Extensive outdoor experiments confirm a mean absolute error of 2.3% at 10 m and continuous distance output during brief plate occlusions, outperforming deep learning baselines by a factor of five in relative error.

---


### 72. [Continuous Knowledge Metabolism: Generating Scientific Hypotheses from Evolving Literature](https://arxiv.org/abs/2604.12243)

**<font color=#1a73e8>作者：</font>** Jinkai Tao, Yubo Wang, Xiaoyu Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific hypothesis generation requires tracking how knowledge evolves, not just what is currently known. We introduce Continuous Knowledge Metabolism (CKM), a framework that processes scientific literature through sliding time windows and incrementally updates a structured knowledge base as new findings arrive. We present CKM-Lite, an efficient variant that achieves strong predictive coverage through incremental accumulation, outperforming batch processing on hit rate (+2.8%, p=0.006), hypothesis yield (+3.6, p<0.001), and best-match alignment (+0.43, p<0.001) while reducing token cost by 92%. To understand what drives these differences, we develop CKM-Full, an instrumented variant that categorizes each new finding as novel, confirming, or contradicting, detects knowledge change signals, and conditions hypothesis generation on the full evolution trajectory. Analyzing 892 hypotheses generated by CKM-Full across 50 research topics, alongside parallel runs of the other variants, we report four empirical observations: (1) incremental processing outperforms batch baseline across predictive and efficiency metrics; (2) change-aware instrumentation is associated with higher LLM-judged novelty (Cohen's d=3.46) but lower predictive coverage, revealing a quality-coverage trade-off; (3) a field's trajectory stability is associated with hypothesis success (r=-0.28, p=0.051), suggesting boundary conditions for literature-based prediction; (4) knowledge convergence signals are associated with nearly 5x higher hit rate than contradiction signals, pointing to differential predictability across change types. These findings suggest that the character of generated hypotheses is shaped not only by how much literature is processed, but also by how it is processed. They further indicate that evaluation frameworks must account for the quality-coverage trade-off rather than optimize for a single metric.

---


### 73. [ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251)

**<font color=#1a73e8>作者：</font>** Xinliang Wang, Yifeng Shi, Zhenyu Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) delivers high-fidelity real-time rendering but suffers from geometric and photometric degradations under sparse-view constraints. Current generative restoration approaches are often limited by insufficient temporal coherence, a lack of explicit spatial constraints, and a lack of large-scale training data, resulting in multi-view inconsistencies, erroneous geometric hallucinations, and limited generalization to diverse real-world artifact distributions. In this paper, we present ArtifactWorld, a framework that resolves 3DGS artifact repair through systematic data expansion and a homogeneous dual-model paradigm. To address the data bottleneck, we establish a fine-grained phenomenological taxonomy of 3DGS artifacts and construct a comprehensive training set of 107.5K diverse paired video clips to enhance model robustness. Architecturally, we unify the restoration process within a video diffusion backbone, utilizing an isomorphic predictor to localize structural defects via an artifact heatmap. This heatmap then guides the restoration through an Artifact-Aware Triplet Fusion mechanism, enabling precise, intensity-guided spatio-temporal repair within native self-attention. Extensive experiments demonstrate that ArtifactWorld achieves state-of-the-art performance in sparse novel view synthesis and robust 3D reconstruction. Code and dataset will be made public.

---


### 74. [SpanKey: Dynamic Key Space Conditioning for Neural Network Access Control](https://arxiv.org/abs/2604.12254)

**<font color=#1a73e8>作者：</font>** WenBin Yan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> SpanKey is a lightweight way to gate inference without encrypting weights or chasing leaderboard accuracy on gated inference. The idea is to condition activations on secret keys. A basis matrix $B$ defines a low-dimensional key subspace $Span(B)$; during training we sample coefficients $\alpha$ and form keys $k=\alpha^\top B$, then inject them into intermediate activations with additive or multiplicative maps and strength $\gamma$. Valid keys lie in $Span(B)$; invalid keys are sampled outside that subspace. We make three points. (i) Mechanism: subspace key injection and a multi-layer design space. (ii) Failure mode: key absorption, together with two analytical results (a Beta-energy split and margin-tail diagnostics), explains weak baseline separation in energy and margin terms -- these are not a security theorem. iii) Deny losses and experiments: Modes A--C and extensions, with CIFAR-10 ResNet-18 runs and MNIST ablations for Mode B. We summarize setup and first-order analysis, injectors, absorption, deny losses and ablations, a threat discussion that does not promise cryptography, and closing remarks on scale. Code: \texttt{this https URL}

---


### 75. [ARGen: Affect-Reinforced Generative Augmentation towards Vision-based Dynamic Emotion Perception](https://arxiv.org/abs/2604.12255)

**<font color=#1a73e8>作者：</font>** Huanzhen Wang, Ziheng Zhou, Jiaqi Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic facial expression recognition in the wild remains challenging due to data scarcity and long-tail distributions, which hinder models from effectively learning the temporal dynamics of scarce emotions. To address these limitations, we propose ARGen, an Affect-Reinforced Generative Augmentation Framework that enables data-adaptive dynamic expression generation for robust emotion perception. ARGen operates in two stages: Affective Semantic Injection (ASI) and Adaptive Reinforcement Diffusion (ARD). The ASI stage establishes affective knowledge alignment through facial Action Units and employs a retrieval-augmented prompt generation strategy to synthesize consistent and fine-grained affective descriptions via large-scale visual-language models, thereby injecting interpretable emotional priors into the generation process. The ARD stage integrates text-conditioned image-to-video diffusion with reinforcement learning, introducing inter-frame conditional guidance and a multi-objective reward function to jointly optimize expression naturalness, facial integrity, and generative efficiency. Extensive experiments on both generation and recognition tasks verify that ARGen substantially enhances synthesis fidelity and improves recognition performance, establishing an interpretable and generalizable generative augmentation paradigm for vision-based affective computing.

---


### 76. [Style-Decoupled Adaptive Routing Network for Underwater Image Enhancement](https://arxiv.org/abs/2604.12257)

**<font color=#1a73e8>作者：</font>** Hang Xu, Chen Long, Bing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater Image Enhancement (UIE) is essential for robust visual perception in marine applications. However, existing methods predominantly rely on uniform mapping tailored to average dataset distributions, leading to over-processing mildly degraded images or insufficient recovery for severe ones. To address this challenge, we propose a novel adaptive enhancement framework, SDAR-Net. Unlike existing uniform paradigms, it first decouples specific degradation styles from the input and subsequently modulates the enhancement process adaptively. Specifically, since underwater degradation primarily shifts the appearance while keeping the scene structure, SDAR-Net formulates image features into dynamic degradation style embeddings and static scene structural representations through a carefully designed training framework. Subsequently, we introduce an adaptive routing mechanism. By evaluating style features and adaptively predicting soft weights at different enhancement states, it guides the weighted fusion of the corresponding image representations, accurately satisfying the adaptive restoration demands of each image. Extensive experiments show that SDAR-Net achieves a new state-of-the-art (SOTA) performance with a PSNR of 25.72 dB on real-world benchmark, and demonstrates its utility in downstream vision tasks. Our code is available at this https URL.

---


### 77. [Decentralized Learning via Random Walk with Jumps](https://arxiv.org/abs/2604.12260)

**<font color=#1a73e8>作者：</font>** Zonghong Liu, Matthew Dwyer, Salim El Rouayheb  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study decentralized learning over networks where data are distributed across nodes without a central coordinator. Random walk learning is a token-based approach in which a single model is propagated across the network and updated at each visited node using local data, thereby incurring low communication and computational overheads. In weighted random-walk learning, the transition matrix is designed to achieve a desired sampling distribution, thereby speeding up convergence under data heterogeneity. We show that implementing weighted sampling via the Metropolis-Hastings algorithm can lead to a previously unexplored phenomenon we term entrapment. The random walk may become trapped in a small region of the network, resulting in highly correlated updates and severely degraded convergence. To address this issue, we propose Metropolis-Hastings with Levy jumps, which introduces occasional long-range transitions to restore exploration while respecting local information constraints. We establish a convergence rate that explicitly characterizes the roles of data heterogeneity, network spectral gap, and jump probability, and demonstrate through experiments that MHLJ effectively eliminates entrapment and significantly speeds up decentralized learning.

---


### 78. [DreamStereo: Towards Real-Time Stereo Inpainting for HD Videos](https://arxiv.org/abs/2604.12270)

**<font color=#1a73e8>作者：</font>** Yuan Huang, Sijie Zhao, Jing Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereo video inpainting, which aims to fill the occluded regions of warped videos with visually coherent content while maintaining temporal consistency, remains a challenging open problem. The regions to be filled are scattered along object boundaries and occupy only a small fraction of each frame, leading to two key challenges. First, existing approaches perform poorly on such tasks due to the scarcity of high-quality stereo inpainting datasets, which limits their ability to learn effective inpainting priors. Second, these methods apply equal processing to all regions of the frame, even though most pixels require no modification, resulting in substantial redundant computation. To address these issues, we introduce three interconnected components. We first propose Gradient-Aware Parallax Warping (GAPW), which leverages backward warping and the gradient of the coordinate mapping function to obtain continuous edges and smooth occlusion regions. Then, a Parallax-Based Dual Projection (PBDP) strategy is introduced, which incorporates GAPW to produce geometrically consistent stereo inpainting pairs and accurate occlusion masks without requiring stereo videos. Finally, we present Sparsity-Aware Stereo Inpainting (SASI), which reduces over 70% of redundant tokens, achieving a 10.7x speedup during diffusion inference and delivering results comparable to its full-computation counterpart, enabling real-time processing of HD (768 x 1280) videos at 25 FPS on a single A100 GPU.

---


### 79. [SubFlow: Sub-mode Conditioned Flow Matching for Diverse One-Step Generation](https://arxiv.org/abs/2604.12273)

**<font color=#1a73e8>作者：</font>** Yexiong Lin, Jia Shi, Shanshan Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching has emerged as a powerful generative framework, with recent few-step methods achieving remarkable inference acceleration. However, we identify a critical yet overlooked limitation: these models suffer from severe diversity degradation, concentrating samples on dominant modes while neglecting rare but valid variations of the target distribution. We trace this degradation to averaging distortion: when trained with MSE objectives, class-conditional flows learn a frequency-weighted mean over intra-class sub-modes, causing the model to over-represent high-density modes while systematically neglecting low-density ones. To address this, we propose SubFlow, Sub-mode Conditioned Flow Matching, which eliminates averaging distortion by decomposing each class into fine-grained sub-modes via semantic clustering and conditioning the flow on sub-mode indices. Each conditioned sub-distribution is approximately unimodal, so the learned flow accurately targets individual modes with no averaging distortion, restoring full mode coverage in a single inference step. Crucially, SubFlow is entirely plug-and-play: it integrates seamlessly into existing one-step models such as MeanFlow and Shortcut Models without any architectural modifications. Extensive experiments on ImageNet-256 demonstrate that SubFlow yields substantial gains in generation diversity (Recall) while maintaining competitive image quality (FID), confirming its broad applicability across different one-step generation frameworks. Project page: this https URL.

---


### 80. [Models Know Their Shortcuts: Deployment-Time Shortcut Mitigation](https://arxiv.org/abs/2604.12277)

**<font color=#1a73e8>作者：</font>** Jiayi Li, Shijie Tang, Gün Kaynar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained language models often rely on superficial features that appear predictive during training yet fail to generalize at test time, a phenomenon known as shortcut learning. Existing mitigation methods generally operate at training time and require heavy supervision such as access to the original training data or prior knowledge of shortcut type. We propose Shortcut Guardrail, a deployment-time framework that mitigates token-level shortcuts without access to the original training data or shortcut annotations. Our key insight is that gradient-based attribution on a biased model highlights shortcut tokens. Building on this finding, we train a lightweight LoRA-based debiasing module with a Masked Contrastive Learning (MaskCL) objective that encourages consistent representations with or without individual tokens. Across sentiment classification, toxicity detection, and natural language inference under both naturally occurring and controlled shortcuts, Shortcut Guardrail improves overall accuracy and worst-group accuracy over the unmitigated model under distribution shifts while preserving in-distribution performance.

---


### 81. [MAST: Mask-Guided Attention Mass Allocation for Training-Free Multi-Style Transfer](https://arxiv.org/abs/2604.12281)

**<font color=#1a73e8>作者：</font>** Dongkyung Kang, Jaeyeon Hwang, Junseo Park 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Style transfer aims to render a content image with the visual characteristics of a reference style while preserving its underlying semantic layout and structural geometry. While recent diffusion-based models demonstrate strong stylization capabilities by leveraging powerful generative priors and controllable internal representations, they typically assume a single global style. Extending them to multi-style scenarios often leads to boundary artifacts, unstable stylization, and structural inconsistency due to interference between multiple style representations. To overcome these limitations, we propose MAST (Mask-Guided Attention Mass Allocation for Training-Free Multi-Style Transfer), a novel training-free framework that explicitly controls content-style interactions within the diffusion attention mechanism. To achieve artifact-free and structure-preserving stylization, MAST integrates four connected modules. First, Layout-preserving Query Anchoring prevents global layout collapse by firmly anchoring the semantic structure using content queries. Second, Logit-level Attention Mass Allocation deterministically distributes attention probability mass across spatial regions, seamlessly fusing multiple styles without boundary artifacts. Third, Sharpness-aware Temperature Scaling restores the attention sharpness degraded by multi-style expansion. Finally, Discrepancy-aware Detail Injection adaptively compensates for localized high-frequency detail losses by measuring structural discrepancies. Extensive experiments demonstrate that MAST effectively mitigates boundary artifacts and maintains structural consistency, preserving texture fidelity and spatial coherence even as the number of applied styles increases.

---


### 82. [LiveMoments: Reselected Key Photo Restoration in Live Photos via Reference-guided Diffusion](https://arxiv.org/abs/2604.12286)

**<font color=#1a73e8>作者：</font>** Clara Xue, Zizheng Yan, Zhenning Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Live Photo captures both a high-quality key photo and a short video clip to preserve the precious dynamics around the captured moment. While users may choose alternative frames as the key photo to capture better expressions or timing, these frames often exhibit noticeable quality degradation, as the photo capture ISP pipeline delivers significantly higher image quality than the video pipeline. This quality gap highlights the need for dedicated restoration techniques to enhance the reselected key photo. To this end, we propose LiveMoments, a reference-guided image restoration framework tailored for the reselected key photo in Live Photos. Our method employs a two-branch neural network: a reference branch that extracts structural and textural information from the original high-quality key photo, and a main branch that restores the reselected frame using the guidance provided by the reference branch. Furthermore, we introduce a unified Motion Alignment module that incorporates motion guidance for spatial alignment at both the latent and image levels. Experiments on real and synthetic Live Photos demonstrate that LiveMoments significantly improves perceptual quality and fidelity over existing solutions, especially in scenes with fast motion or complex structures. Our code is available at this https URL.

---


### 83. [Labeled TrustSet Guided: Batch Active Learning with Reinforcement Learning](https://arxiv.org/abs/2604.12303)

**<font color=#1a73e8>作者：</font>** Guofeng Cui, Yang Liu, Pichao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Batch active learning (BAL) is a crucial technique for reducing labeling costs and improving data efficiency in training large-scale deep learning models. Traditional BAL methods often rely on metrics like Mahalanobis Distance to balance uncertainty and diversity when selecting data for annotation. However, these methods predominantly focus on the distribution of unlabeled data and fail to leverage feedback from labeled data or the model's performance. To address these limitations, we introduce TrustSet, a novel approach that selects the most informative data from the labeled dataset, ensuring a balanced class distribution to mitigate the long-tail problem. Unlike CoreSet, which focuses on maintaining the overall data distribution, TrustSet optimizes the model's performance by pruning redundant data and using label information to refine the selection process. To extend the benefits of TrustSet to the unlabeled pool, we propose a reinforcement learning (RL)-based sampling policy that approximates the selection of high-quality TrustSet candidates from the unlabeled data. Combining TrustSet and RL, we introduce the Batch Reinforcement Active Learning with TrustSet (BRAL-T) framework. BRAL-T achieves state-of-the-art results across 10 image classification benchmarks and 2 active fine-tuning tasks, demonstrating its effectiveness and efficiency in various domains.

---


### 84. [Beyond Weather Correlation: A Comparative Study of Static and Temporal Neural Architectures for Fine-Grained Residential Energy Consumption Forecasting in Melbourne, Australia](https://arxiv.org/abs/2604.12304)

**<font color=#1a73e8>作者：</font>** Prasad Nimantha Madusanka Ukwatta Hewage, Hao Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate short-term residential energy consumption forecasting at sub-hourly resolution is critical for smart grid management, demand response programmes, and renewable energy integration. While weather variables are widely acknowledged as key drivers of residential electricity demand, the relative merit of incorporating temporal autocorrelation - the sequential memory of past consumption; over static meteorological features alone remains underexplored at fine-grained (5-minute) temporal resolution for Australian households. This paper presents a rigorous empirical comparison of a Multilayer Perceptron (MLP) and a Long Short-Term Memory (LSTM) recurrent network applied to two real-world Melbourne households: House 3 (a standard grid-connected dwelling) and House 4 (a rooftop solar photovoltaic-integrated household). Both models are trained on 14 months of 5-minute interval smart meter data (March 2023-April 2024) merged with official Bureau of Meteorology (BOM) daily weather observations, yielding over 117,000 samples per household. The LSTM, operating on 24-step (2-hour) sliding consumption windows, achieves coefficients of determination of R^2 = 0.883 (House 3) and R^2 = 0.865 (House 4), compared to R^2 = -0.055 and R^2 = 0.410 for the corresponding weather-driven MLPs - differences of 93.8 and 45.5 percentage points. These results establish that temporal autocorrelation in the consumption sequence dominates meteorological information for short-term forecasting at 5-minute granularity. Additionally, we demonstrate an asymmetry introduced by solar generation: for the PV-integrated household, the MLP achieves R^2 = 0.410, revealing implicit solar forecasting from weather-time correlations. A persistence baseline analysis and seasonal stratification contextualise model performance. We propose a hybrid weather-augmented LSTM and federated learning extensions as directions for future work.

---


### 85. [Boosting Robust AIGI Detection with LoRA-based Pairwise Training](https://arxiv.org/abs/2604.12307)

**<font color=#1a73e8>作者：</font>** Ruiyang Xia, Qi Zhang, Yaowen Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proliferation of highly realistic AI-Generated Image (AIGI) has necessitated the development of practical detection methods. While current AIGI detectors perform admirably on clean datasets, their detection performance frequently decreases when deployed "in the wild", where images are subjected to unpredictable, complex distortions. To resolve the critical vulnerability, we propose a novel LoRA-based Pairwise Training (LPT) strategy designed specifically to achieve robust detection for AIGI under severe distortions. The core of our strategy involves the targeted finetuning of a visual foundation model, the deliberate simulation of data distribution during the training phase, and a unique pairwise training process. Specifically, we introduce distortion and size simulations to better fit the distribution from the validation and test sets. Based on the strong visual representation capability of the visual foundation model, we finetune the model to achieve AIGI detection. The pairwise training is utilized to improve the detection via decoupling the generalization and robustness optimization. Experiments show that our approach secured the 3th placement in the NTIRE Robust AI-Generated Image Detection in the Wild challenge

---


### 86. [Towards Realistic and Consistent Orbital Video Generation via 3D Foundation Priors](https://arxiv.org/abs/2604.12309)

**<font color=#1a73e8>作者：</font>** Rong Wang, Ruyi Zha, Ziang Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a novel method for generating geometrically realistic and consistent orbital videos from a single image of an object. Existing video generation works mostly rely on pixel-wise attention to enforce view consistency across frames. However, such mechanism does not impose sufficient constraints for long-range extrapolation, e.g. rear-view synthesis, in which pixel correspondences to the input image are limited. Consequently, these works often fail to produce results with a plausible and coherent structure. To tackle this issue, we propose to leverage rich shape priors from a 3D foundational generative model as an auxiliary constraint, motivated by its capability of modeling realistic object shape distributions learned from large 3D asset corpora. Specifically, we prompt the video generation with two scales of latent features encoded by the 3D foundation model: (i) a denoised global latent vector as an overall structural guidance, and (ii) a set of latent images projected from volumetric features to provide view-dependent and fine-grained geometry details. In contrast to commonly used 2.5D representations such as depth or normal maps, these compact features can model complete object shapes, and help to improve inference efficiency by avoiding explicit mesh extraction. To achieve effective shape conditioning, we introduce a multi-scale 3D adapter to inject feature tokens to the base video model via cross-attention, which retains its capabilities from general video pretraining and enables a simple and model-agonistic fine-tuning process. Extensive experiments on multiple benchmarks show that our method achieves superior visual quality, shape realism and multi-view consistency compared to state-of-the-art methods, and robustly generalizes to complex camera trajectories and in-the-wild images.

---


### 87. [Dialogue Agents that Share Family Information to Strengthen Grandparent-Grandchild Relationships](https://arxiv.org/abs/2604.12310)

**<font color=#1a73e8>作者：</font>** Seiya Mitsuno, Midori Ban, Hiroshi Ishiguro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social isolation among older adults has become a critical concern, as reduced opportunities for conversation and weakened family relationships negatively affect mental health. This study proposes a dialogue agent that supports older adults by fostering both a relationship with the agent and a relationship with their grandchild through sharing everyday information. The agent operates on a chatbot platform and engages in daily conversations with older adults and their grandchildren, exchanging information gathered from each party to enhance conversational engagement and social connection. We conducted a ten-day empirical experiment with 108 grandparent-grandchild pairs. The results suggest that older adults became more willing to interact with the proposed agent, which shared information about their grandchildren, and that the psychological connection between grandparents and grandchildren was strengthened. Furthermore, daily interactions with the agent were associated with reduced anxiety in both older adults and their grandchildren. These findings indicate that a dialogue agent that shares personal information can be an effective approach to supporting older adults by simultaneously offering conversational opportunities and promoting family connectedness. Overall, this study provides valuable insights into the design of dialogue agents that effectively address social isolation among older adults.

---


### 88. [GTPBD-MM: A Global Terraced Parcel and Boundary Dataset with Multi-Modality](https://arxiv.org/abs/2604.12315)

**<font color=#1a73e8>作者：</font>** Zhiwei Zhang, Xingyuan Zeng, Xinkai Kong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agricultural parcel extraction plays an important role in remote sensing-based agricultural monitoring, supporting parcel surveying, precision management, and ecological assessment. However, existing public benchmarks mainly focus on regular and relatively flat farmland scenes. In contrast, terraced parcels in mountainous regions exhibit stepped terrain, pronounced elevation variation, irregular boundaries, and strong cross-regional heterogeneity, making parcel extraction a more challenging problem that jointly requires visual recognition, semantic discrimination, and terrain-aware geometric understanding. Although recent studies have advanced visual parcel benchmarks and image-text farmland understanding, a unified benchmark for complex terraced parcel extraction under aligned image-text-DEM settings remains absent. To fill this gap, we present GTPBD-MM, the first multimodal benchmark for global terraced parcel extraction. Built upon GTPBD, GTPBD-MM integrates high-resolution optical imagery, structured text descriptions, and DEM data, and supports systematic evaluation under Image-only, Image+Text, and Image+Text+DEM settings. We further propose Elevation and Text guided Terraced parcel network (ETTerra), a multimodal baseline for terraced parcel delineation. Extensive experiments demonstrate that textual semantics and terrain geometry provide complementary cues beyond visual appearance alone, yielding more accurate, coherent, and structurally consistent delineation results in complex terraced scenes.

---


### 89. [Cell Instance Segmentation via Multi-Task Image-to-Image Schrödinger Bridge](https://arxiv.org/abs/2604.12318)

**<font color=#1a73e8>作者：</font>** Hayato Inoue, Shota Harada, Shumpei Takezaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing cell instance segmentation pipelines typically combine deterministic predictions with post-processing, which imposes limited explicit constraints on the global structure of instance masks. In this work, we propose a multi-task image-to-image Schrödinger Bridge framework that formulates instance segmentation as a distribution-based image-to-image generation problem. Boundary-aware supervision is integrated through a reverse distance map, and deterministic inference is employed to produce stable predictions. Experimental results on the PanNuke dataset demonstrate that the proposed method achieves competitive or superior performance without relying on SAM pre-training or additional post-processing. Additional results on the MoNuSeg dataset show robustness under limited training data. These findings indicate that Schrödinger Bridge-based image-to-image generation provides an effective framework for cell instance segmentation.

---


### 90. [EgoEsportsQA: An Egocentric Video Benchmark for Perception and Reasoning in Esports](https://arxiv.org/abs/2604.12320)

**<font color=#1a73e8>作者：</font>** Jianzhe Ma, Zhonghao Cao, Shangkui Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While video large language models (Video-LLMs) excel in understanding slow-paced, real-world egocentric videos, their capabilities in high-velocity, information-dense virtual environments remain under-explored. Existing benchmarks focus on daily activities, yet lack a rigorous testbed for evaluating fast, rule-bound reasoning in virtual scenarios. To fill this gap, we introduce EgoEsportsQA, a pioneering video question-answering (QA) benchmark for grounding perception and reasoning in expert esports knowledge. We curate 1,745 high-quality QA pairs from professional matches across 3 first-person shooter games via a scalable six-stage pipeline. These questions are structured into a two-dimensional decoupled taxonomy: 11 sub-tasks in the cognitive capability dimension (covering perception and reasoning levels) and 6 sub-tasks in the esports knowledge dimension. Comprehensive evaluations of state-of-the-art Video-LLMs reveal that current models still fail to achieve satisfactory performance, with the best model only 71.58%. The results expose notable gaps across both axes: models exhibit stronger capabilities in basic visual perception than in deep tactical reasoning, and they grasp overall macro-progression better than fine-grained micro-operations. Extensive ablation experiments demonstrate the intrinsic weaknesses of current Video-LLM architectures. Further analysis suggests that our dataset not only reveals the connections between real-world and virtual egocentric domains, but also offers guidance for optimizing downstream esports applications, thereby fostering the future advancement of Video-LLMs in various egocentric environments.

---


### 91. [ToxiTrace: Gradient-Aligned Training for Explainable Chinese Toxicity Detection](https://arxiv.org/abs/2604.12321)

**<font color=#1a73e8>作者：</font>** Boyang Li, Hongzhe Shou, Yuanyuan Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing Chinese toxic content detection methods mainly target sentence-level classification but often fail to provide readable and contiguous toxic evidence spans. We propose \textbf{ToxiTrace}, an explainability-oriented method for BERT-style encoders with three components: (1) \textbf{CuSA}, which refines encoder-derived saliency cues into fine-grained toxic spans with lightweight LLM guidance; (2) \textbf{GCLoss}, a gradient-constrained objective that concentrates token-level saliency on toxic evidence while suppressing irrelevant activations; and (3) \textbf{ARCL}, which constructs sample-specific contrastive reasoning pairs to sharpen the semantic boundary between toxic and non-toxic content. Experiments show that ToxiTrace improves classification accuracy and toxic span extraction while preserving efficient encoder-based inference and producing more coherent, human-readable explanations. We have released the model at this https URL.

---


### 92. [Self-Adversarial One Step Generation via Condition Shifting](https://arxiv.org/abs/2604.12322)

**<font color=#1a73e8>作者：</font>** Deyuan Liu, Peng Sun, Yansen Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The push for efficient text to image synthesis has moved the field toward one step sampling, yet existing methods still face a three way tradeoff among fidelity, inference speed, and training efficiency. Approaches that rely on external discriminators can sharpen one step performance, but they often introduce training instability, high GPU memory overhead, and slow convergence, which complicates scaling and parameter efficient tuning. In contrast, regression based distillation and consistency objectives are easier to optimize, but they typically lose fine details when constrained to a single step. We present APEX, built on a key theoretical insight: adversarial correction signals can be extracted endogenously from a flow model through condition shifting. Using a transformation creates a shifted condition branch whose velocity field serves as an independent estimator of the model's current generation distribution, yielding a gradient that is provably GAN aligned, replacing the sample dependent discriminator terms that cause gradient vanishing. This discriminator free design is architecture preserving, making APEX a plug and play framework compatible with both full parameter and LoRA based tuning. Empirically, our 0.6B model surpasses FLUX-Schnell 12B (20$\times$ more parameters) in one step quality. With LoRA tuning on Qwen-Image 20B, APEX reaches a GenEval score of 0.89 at NFE=1 in 6 hours, surpassing the original 50-step teacher (0.87) and providing a 15.33$\times$ inference speedup. Code is available this https URL.

---


### 93. [Black-Box Optimization From Small Offline Datasets via Meta Learning with Synthetic Tasks](https://arxiv.org/abs/2604.12325)

**<font color=#1a73e8>作者：</font>** Azza Fadhel, Hung Tran, Trong Nghia Hoang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of offline black-box optimization, where the goal is to discover optimal designs (e.g., molecules or materials) from past experimental data. A key challenge in this setting is data scarcity: in many scientific applications, only small or poor-quality datasets are available, which severely limits the effectiveness of existing algorithms. Prior work has theoretically and empirically shown that performance of offline optimization algorithms depends on how well the surrogate model captures the optimization bias (i.e., ability to rank input designs correctly), which is challenging to accomplish with limited experimental data. This paper proposes Surrogate Learning with Optimization Bias via Synthetic Task Generation (OptBias), a meta-learning framework that directly tackles data scarcity. OptBias learns a reusable optimization bias by training on synthetic tasks generated from a Gaussian process, and then fine-tunes the surrogate model on the small data for the target task. Across diverse continuous and discrete offline optimization benchmarks, OptBias consistently outperforms state-of-the-art baselines in small data regimes. These results highlight OptBias as a robust and practical solution for offline optimization in realistic small data settings.

---


### 94. [HyperLiDAR: Adaptive Post-Deployment LiDAR Segmentation via Hyperdimensional Computing](https://arxiv.org/abs/2604.12331)

**<font color=#1a73e8>作者：</font>** Ivannia Gomez Moreno, Yi Yao, Ye Tian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR semantic segmentation plays a pivotal role in 3D scene understanding for edge applications such as autonomous driving. However, significant challenges remain for real-world deployments, particularly for on-device post-deployment adaptation. Real-world environments can shift as the system navigates through different locations, leading to substantial performance degradation without effective and timely model adaptation. Furthermore, edge systems operate under strict computational and energy constraints, making it infeasible to adapt conventional segmentation models (based on large neural networks) directly on-device. To address the above challenges, we introduce HyperLiDAR, the first lightweight, post-deployment LiDAR segmentation framework based on Hyperdimensional Computing (HDC). The design of HyperLiDAR fully leverages the fast learning and high efficiency of HDC, inspired by how the human brain processes information. To further improve the adaptation efficiency, we identify the high data volume per scan as a key bottleneck and introduce a buffer selection strategy that focuses learning on the most informative points. We conduct extensive evaluations on two state-of-the-art LiDAR segmentation benchmarks and two representative devices. Our results show that HyperLiDAR outperforms or achieves comparable adaptation performance to state-of-the-art segmentation methods, while achieving up to a 13.8x speedup in retraining.

---


### 95. [CoLA: A Choice Leakage Attack Framework to Expose Privacy Risks in Subset Training](https://arxiv.org/abs/2604.12342)

**<font color=#1a73e8>作者：</font>** Qi Li, Cheng-Long Wang, Yinzhi Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Training models on a carefully chosen portion of data rather than the full dataset is now a standard preprocess for modern ML. From vision coreset selection to large-scale filtering in language models, it enables scalability with minimal utility loss. A common intuition is that training on fewer samples should also reduce privacy risks. In this paper, we challenge this assumption. We show that subset training is not privacy free: the very choices of which data are included or excluded can introduce new privacy surface and leak more sensitive information. Such information can be captured by adversaries either through side-channel metadata from the subset selection process or via the outputs of the target model. To systematically study this phenomenon, we propose CoLA (Choice Leakage Attack), a unified framework for analyzing privacy leakage in subset selection. In CoLA, depending on the adversary's knowledge of the side-channel information, we define two practical attack scenarios: Subset-aware Side-channel Attacks and Black-box Attacks. Under both scenarios, we investigate two privacy surfaces unique to subset training: (1) Training-membership MIA (TM-MIA), which concerns only the privacy of training data membership, and (2) Selection-participation MIA (SP-MIA), which concerns the privacy of all samples that participated in the subset selection process. Notably, SP-MIA enlarges the notion of membership from model training to the entire data-model supply chain. Experiments on vision and language models show that existing threat models underestimate subset-training privacy risks: the expanded privacy surface leaks both training and selection membership, extending risks from individual models to the broader ML ecosystem.

---


### 96. [Detecting Precise Hand Touch Moments in Egocentric Video](https://arxiv.org/abs/2604.12343)

**<font color=#1a73e8>作者：</font>** Huy Anh Nguyen, Feras Dayoub, Minh Hoai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the challenging task of detecting the precise moment when hands make contact with objects in egocentric videos. This frame-level detection is crucial for augmented reality, human-computer interaction, assistive technologies, and robot learning applications, where contact onset signals action initiation or completion. Temporally precise detection is particularly challenging due to subtle hand motion variations near contact, frequent occlusions, fine-grained manipulation patterns, and the inherent motion dynamics of first-person perspectives.
To tackle these challenges, we propose a Hand-informed Context Enhanced module (HiCE; pronounced `high-see') that leverages spatiotemporal features from hand regions and their surrounding context through cross-attention mechanisms, learning to identify potential contact patterns. Our approach is further refined with a grasp-aware loss and soft label that emphasizes hand pose patterns and movement dynamics characteristic of touch events, enabling the model to distinguish between near-contact and actual contact frames. We also introduce TouchMoment, an egocentric dataset containing 4,021 videos and 8,456 annotated contact moments spanning over one million frames. Experiments on TouchMoment show that, under a strict evaluation criterion that counts a prediction as correct only if it falls within a two-frame tolerance of the ground-truth moment, our method achieves substantial gains and outperforms state-of-the-art event-spotting baselines by 16.91% average precision.

---


### 97. [Unlocking the Potential of Grounding DINO in Videos: Parameter-Efficient Adaptation for Limited-Data Spatial-Temporal Localization](https://arxiv.org/abs/2604.12346)

**<font color=#1a73e8>作者：</font>** Zanyi Wang, Fan Li, Dengyang Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal video grounding (STVG) aims to localize queried objects within dynamic video segments. Prevailing fully-trained approaches are notoriously data-hungry. However, gathering large-scale STVG data is exceptionally challenging: dense frame-level bounding boxes and complex temporal language alignments are prohibitively expensive to annotate, especially for specialized video domains. Consequently, conventional models suffer from severe overfitting on these inherently limited datasets, while zero-shot foundational models lack the task-specific temporal awareness needed for precise localization. To resolve this small-data challenge, we introduce ST-GD, a data-efficient framework that adapts pre-trained 2D visual-language models (e.g., Grounding DINO) to video tasks. To avoid destroying pre-trained priors on small datasets, ST-GD keeps the base model frozen and strategically injects lightweight adapters (~10M trainable parameters) to instill spatio-temporal awareness, alongside a novel temporal decoder for boundary prediction. This design naturally counters data scarcity. Consequently, ST-GD excels in data-scarce scenarios, achieving highly competitive performance on the limited-scale HC-STVG v1/v2 benchmarks, while maintaining robust generalization on the VidSTG dataset. This validates ST-GD as a powerful paradigm for complex video understanding under strict small-data constraints.

---


### 98. [PrivEraserVerify: Efficient, Private, and Verifiable Federated Unlearning](https://arxiv.org/abs/2604.12348)

**<font color=#1a73e8>作者：</font>** Parthaw Goswami, Md Khairul Islam, Ashfak Yeafi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative model training without sharing raw data, offering a promising path toward privacy preserving artificial intelligence. However, FL models may still memorize sensitive information from participants, conflicting with the right to be forgotten (RTBF). To meet these requirements, federated unlearning has emerged as a mechanism to remove the contribution of departing clients. Existing solutions only partially address this challenge: FedEraser improves efficiency but lacks privacy protection, FedRecovery ensures differential privacy (DP) but degrades accuracy, and VeriFi enables verifiability but introduces overhead without efficiency or privacy guarantees. We present PrivEraserVerify (PEV), a unified framework that integrates efficiency, privacy, and verifiability into federated unlearning. PEV employs (i) adaptive checkpointing to retain critical historical updates for fast reconstruction, (ii) layer adaptive differentially private calibration to selectively remove client influence while minimizing accuracy loss, and (iii) fingerprint based verification, enabling participants to confirm unlearning in a decentralized and noninvasive manner. Experiments on image, handwritten character, and medical datasets show that PEV achieves up to 2 to 3 times faster unlearning than retraining, provides formal indistinguishability guarantees with reduced performance degradation, and supports scalable verification. To the best of our knowledge, PEV is the first framework to simultaneously deliver efficiency, privacy, and verifiability for federated unlearning, moving FL closer to practical and regulation compliant deployment.

---


### 99. [Responsible Trauma Research: Designing Effective and Sustainable Virtual Reality Exposure Studies](https://arxiv.org/abs/2604.12349)

**<font color=#1a73e8>作者：</font>** Annalisa Degenhard, Sophia Ppali, Fotis Liarokapis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual reality exposure therapy (VRET) enables controlled exposure to trauma-related stimuli to facilitate memory access and emotional processing. However, the field remains underexplored for complex post-traumatic stress disorder (C-PTSD). Unlike single-trauma PTSD, C-PTSD requires highly individualized triggers that are difficult to identify and implement safely. We conducted a feasibility study with 11 patients, two trauma therapists, and a VR developer to explore integrating VRET into C-PTSD treatment while safeguarding all stakeholders. Initial findings indicate that simple objects can be just as effective as complex scenes, therapeutic success does not correlate with VR presence levels, and the design process itself became integral to therapy rather than preparatory. However, involving developers in therapy sessions led to considerable emotional stress and role confusion, which required a cautious approach. Based on these insights, we provide methodological recommendations for safe and patient-centered VRET studies that balance therapeutic effectiveness with stakeholder safety across the research process.

---


### 100. [Fundus Image-based Glaucoma Screening via Retinal Knowledge-Oriented Dynamic Multi-Level Feature Integration](https://arxiv.org/abs/2604.12351)

**<font color=#1a73e8>作者：</font>** Yuzhuo Zhou, Chi Liu, Sheng Shen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated diagnosis based on color fundus photography is essential for large-scale glaucoma screening. However, existing deep learning models are typically data-driven and lack explicit integration of retinal anatomical knowledge, which limits their robustness across heterogeneous clinical datasets. Moreover, pathological cues in fundus images may appear beyond predefined anatomical regions, making fixed-region feature extraction insufficient for reliable diagnosis. To address these challenges, we propose a retinal knowledge-oriented glaucoma screening framework that integrates dynamic multi-scale feature learning with domain-specific retinal priors. The framework adopts a tri-branch structure to capture complementary retinal representations, including global retinal context, structural features of the optic disc/cup, and dynamically localized pathological regions. A Dynamic Window Mechanism is devised to adaptively identify diagnostically informative regions, while a Knowledge-Enhanced Convolutional Attention Module incorporates retinal priors extracted from a pre-trained foundation model to guide attention learning. Extensive experiments on the large-scale AIROGS dataset demonstrate that the proposed method outperforms diverse baselines, achieving an AUC of 98.5% and an accuracy of 94.6%. Additional evaluations on multiple datasets from the SMDG-19 benchmark further confirm its strong cross-domain generalization capability, indicating that knowledge-guided attention combined with adaptive lesion localization can significantly improve the robustness of automated glaucoma screening systems.

---


### 101. [Combating Pattern and Content Bias: Adversarial Feature Learning for Generalized AI-Generated Image Detection](https://arxiv.org/abs/2604.12353)

**<font color=#1a73e8>作者：</font>** Haifeng Zhang, Qinghui He, Xiuli Bi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, the rapid development of generative artificial intelligence technology has significantly lowered the barrier to creating high-quality fake images, posing a serious challenge to information authenticity and credibility. Existing generated image detection methods typically enhance generalization through model architecture or network design. However, their generalization performance remains susceptible to data bias, as the training data may drive models to fit specific generative patterns and content rather than the common features shared by images from different generative models (asymmetric bias learning). To address this issue, we propose a Multi-dimensional Adversarial Feature Learning (MAFL) framework. The framework adopts a pretrained multimodal image encoder as the feature extraction backbone, constructs a real-fake feature learning network, and designs an adversarial bias-learning branch equipped with a multi-dimensional adversarial loss, forming an adversarial training mechanism between authenticity-discriminative feature learning and bias feature learning. By suppressing generation-pattern and content biases, MAFL guides the model to focus on the generative features shared across different generative models, thereby effectively capturing the fundamental differences between real and generated images, enhancing cross-model generalization, and substantially reducing the reliance on large-scale training data. Through extensive experimental validation, our method outperforms existing state-of-the-art approaches by 10.89% in accuracy and 8.57% in Average Precision (AP). Notably, even when trained with only 320 images, it can still achieve over 80% detection accuracy on public datasets.

---


### 102. [OmniFood8K: Single-Image Nutrition Estimation via Hierarchical Frequency-Aligned Fusion](https://arxiv.org/abs/2604.12356)

**<font color=#1a73e8>作者：</font>** Dongjian Yu, Weiqing Min, Qian Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of food nutrition plays a vital role in promoting healthy dietary habits and personalized diet management. Most existing food datasets primarily focus on Western cuisines and lack sufficient coverage of Chinese dishes, which restricts accurate nutritional estimation for Chinese meals. Moreover, many state-of-the-art nutrition prediction methods rely on depth sensors, restricting their applicability in daily scenarios. To address these limitations, we introduce OmniFood8K, a comprehensive multimodal dataset comprising 8,036 food samples, each with detailed nutritional annotations and multi-view images. In addition, to enhance models' capability in nutritional prediction, we construct NutritionSynth-115K, a large-scale synthetic dataset that introduces compositional variations while preserving precise nutritional labels. Moreover, we propose an end-to-end framework for nutritional prediction from a single RGB image. First, we predict a depth map from a single RGB image and design the Scale-Shift Residual Adapter (SSRA) to refine it for global scale consistency and local structural preservation. Second, we propose the Frequency-Aligned Fusion Module (FAFM) to hierarchically align and fuse RGB and depth features in the frequency domain. Finally, we design a Mask-based Prediction Head (MPH) to emphasize key ingredient regions via dynamic channel selection for more accurate prediction. Extensive experiments on multiple datasets demonstrate the superiority of our method over existing approaches. Project homepage: this https URL

---


### 103. [Compiling Activation Steering into Weights via Null-Space Constraints for Stealthy Backdoors](https://arxiv.org/abs/2604.12359)

**<font color=#1a73e8>作者：</font>** Rui Yin, Tianxu Han, Naen Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety-aligned large language models (LLMs) are increasingly deployed in real-world pipelines, yet this deployment also enlarges the supply-chain attack surface: adversaries can distribute backdoored checkpoints that behave normally under standard evaluation but jailbreak when a hidden trigger is present. Recent post-hoc weight-editing methods offer an efficient approach to injecting such backdoors by directly modifying model weights to map a trigger to an attacker-specified response. However, existing methods typically optimize a token-level mapping that forces an affirmative prefix (e.g., ``Sure''), which does not guarantee sustained harmful output -- the model may begin with apparent agreement yet revert to safety-aligned refusal within a few decoding steps. We address this reliability gap by shifting the backdoor objective from surface tokens to internal representations. We extract a steering vector that captures the difference between compliant and refusal behaviors, and compile it into a persistent weight modification that activates only when the trigger is present. To preserve stealthiness and benign utility, we impose a null-space constraint so that the injected edit remains dormant on clean inputs. The method is efficient, requiring only a small set of examples and admitting a closed-form solution. Across multiple safety-aligned LLMs and jailbreak benchmarks, our method achieves high triggered attack success while maintaining non-triggered safety and general utility.

---


### 104. [Is Sliding Window All You Need? An Open Framework for Long-Sequence Recommendation](https://arxiv.org/abs/2604.12372)

**<font color=#1a73e8>作者：</font>** Sayak Chakrabarty, Souradip Pal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long interaction histories are central to modern recommender systems, yet training with long sequences is often dismissed as impractical under realistic memory and latency budgets. This work demonstrates that it is not only practical but also effective-at academic scale. We release a complete, end-to-end framework that implements industrial-style long-sequence training with sliding windows, including all data processing, training, and evaluation scripts. Beyond reproducing prior gains, we contribute two capabilities missing from earlier reports: (i) a runtime-aware ablation study that quantifies the accuracy-compute frontier across windowing regimes and strides, and (ii) a novel k-shift embedding layer that enables million-scale vocabularies on commodity GPUs with negligible accuracy loss. Our implementation trains reliably on modest university clusters while delivering competitive retrieval quality (e.g., up to +6.04% MRR and +6.34% Recall@10 on Retailrocket) with $\sim 4 \times $ training-time overheads. By packaging a robust pipeline, reporting training time costs, and introducing an embedding mechanism tailored for low-resource settings, we transform long-sequence training from a closed, industrial technique into a practical, open, and extensible methodology for the community.

---


### 105. [Modality-Agnostic Prompt Learning for Multi-Modal Camouflaged Object Detection](https://arxiv.org/abs/2604.12380)

**<font color=#1a73e8>作者：</font>** Hao Wang, Jiqing Zhang, Xin Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflaged Object Detection (COD) aims to segment objects that blend seamlessly into complex backgrounds, with growing interest in exploiting additional visual modalities to enhance robustness through complementary information. However, most existing approaches generally rely on modality-specific architectures or customized fusion strategies, which limit scalability and cross-modal generalization. To address this, we propose a novel framework that generates modality-agnostic multi-modal prompts for the Segment Anything Model (SAM), enabling parameter-efficient adaptation to arbitrary auxiliary modalities and significantly improving overall performance on COD tasks. Specifically, we model multi-modal learning through interactions between a data-driven content domain and a knowledge-driven prompt domain, distilling task-relevant cues into unified prompts for SAM decoding. We further introduce a lightweight Mask Refine Module to calibrate coarse predictions by incorporating fine-grained prompt cues, leading to more accurate camouflaged object boundaries. Extensive experiments on RGB-Depth, RGB-Thermal, and RGB-Polarization benchmarks validate the effectiveness and generalization of our modality-agnostic framework.

---


### 106. [Dual-Modality Anchor-Guided Filtering for Test-time Prompt Tuning](https://arxiv.org/abs/2604.12403)

**<font color=#1a73e8>作者：</font>** Jungwon Choi, Eunwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-Time Prompt Tuning (TPT) adapts vision-language models using augmented views, but its effectiveness is hindered by the challenge of determining which views are beneficial. Standard entropy-based filtering relies on the internal confidence scores of the model, which are often miscalibrated under distribution shift, assigning high confidence to irrelevant crops or background regions while ignoring semantic content. To address this, we propose a dual-modality anchor-guided framework that grounds view selection in semantic evidence. We introduce a text anchor from attribute-rich descriptions, to provide fine-grained class semantics, and an adaptive image anchor that captures evolving test-time statistics. Using these anchors, we filter views based on alignment and confidence, ensuring that only informative views guide adaptation. Moreover, we treat the anchors as auxiliary predictive heads and combine their predictions with the original output in a confidence-weighted ensemble, yielding a stable supervision signal for prompt updates. Extensive experiments on 15 benchmark datasets demonstrate new state-of-the-art performance, highlighting the contribution of anchor-guided supervision as a foundation for robust prompt updates.

---


### 107. [Tamper-Proofing with Self-Modifying Code](https://arxiv.org/abs/2604.12407)

**<font color=#1a73e8>作者：</font>** Gregory Morse, Tamás Kozsik  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Classical computability theory tells us that self-modifying code (SMC) on a deterministic universal Turing machine can be simulated by non-SMC code on the same model. That abstraction, however, omits the external timing inputs, concurrency, and microarchitectural state that dominate practical execution on modern processors. We argue that once timing, ordering, and self-introspective effects are treated as observables, a practically faithful non-SMC reproduction of timed SMC becomes detectably expensive on commodity systems. We present a tamper-proofing model that combines introspective and polymorphic SMC, reliable clocks, and runtime timing predicates to bind integrity checks to execution behavior. We distinguish static and dynamic SMC generation, characterize the timing semantics needed to avoid catastrophic pipeline clears, and give x86-64 design primitives for checksum-driven self-patching. We also report timer measurements, performance comparisons, and performance-monitoring counter evidence showing that careful engineering -- especially loop unrolling and cross-page modification -- substantially reduces the overhead of SMC while preserving its tamper-detection value. The paper concludes with an efficiency analysis, a threat model, and deployment guidance for trusted code executing in untrusted environments.

---


### 108. [Security and Resilience in Autonomous Vehicles: A Proactive Design Approach](https://arxiv.org/abs/2604.12408)

**<font color=#1a73e8>作者：</font>** Chieh Tsai, Murad Mehrab Abrar, Salim Hariri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles (AVs) promise efficient, clean and cost-effective transportation systems, but their reliance on sensors, wireless communications, and decision-making systems makes them vulnerable to cyberattacks and physical threats. This chapter presents novel design techniques to strengthen the security and resilience of AVs. We first provide a taxonomy of potential attacks across different architectural layers, from perception and control manipulation to Vehicle-to-Any (V2X) communication exploits and software supply chain compromises. Building on this analysis, we present an AV Resilient architecture that integrates redundancy, diversity, and adaptive reconfiguration strategies, supported by anomaly- and hash-based intrusion detection techniques. Experimental validation on the Quanser QCar platform demonstrates the effectiveness of these methods in detecting depth camera blinding attacks and software tampering of perception modules. The results highlight how fast anomaly detection combined with fallback and backup mechanisms ensures operational continuity, even under adversarial conditions. By linking layered threat modeling with practical defense implementations, this work advances AV resilience strategies for safer and more trustworthy autonomous vehicles.

---


### 109. [DeferredSeg: A Multi-Expert Deferral Framework for Trustworthy Medical Image Segmentation](https://arxiv.org/abs/2604.12411)

**<font color=#1a73e8>作者：</font>** Qiuyu Tian, Haoliang Sun, Yunshan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation models based on deep neural networks demonstrate strong generalization for medical image segmentation. However, they often exhibit overconfidence or underconfidence, leading to unreliable confidence scores for segmentation masks, especially in ambiguous regions. This undermines the trustworthiness required for clinical deployment. Motivated by the learning-to-defer (L2D) paradigm, we introduce DeferredSeg, a deferral-aware segmentation framework, i.e., a Human--AI collaboration system that determines whether to defer predictions to human experts in specific regions.
DeferredSeg extends the base segmentor with an aggregated deferral predictor and additional routing channels that dynamically route each pixel to either the base segmentor or a human expert. To train this routing efficiently, we introduce a pixel-wise surrogate collaboration loss that supervises deferral decisions. In addition, to preserve spatial coherence within deferral regions, we propose a spatial-coherence loss that enforces smooth deferral masks, thereby enhancing reliability.
Beyond single-expert deferral, we further extend the framework to a multi-expert setting by introducing multiple discrepancy experts for collaborative decision-making. To prevent overloading or underutilizing individual experts, we further design a load-balancing penalty that evenly distributes workload across expert branches. We evaluate DeferredSeg on three challenging medical datasets using MedSAM and CENet as the base segmentor for fair comparison. Experimental results show that DeferredSeg consistently outperforms the baseline, demonstrating its effectiveness for trustworthy dense medical segmentation. Moreover, the proposed framework is model-agnostic and can be readily applied to other segmentation architectures.

---


### 110. [Forecasting the Past: Gradient-Based Distribution Shift Detection in Trajectory Prediction](https://arxiv.org/abs/2604.12425)

**<font color=#1a73e8>作者：</font>** Michele De Vita, Julian Wiederer, Vasileios Belagiannis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory prediction models often fail in real-world automated driving due to distributional shifts between training and test conditions. Such distributional shifts, whether behavioural or environmental, pose a critical risk by causing the model to make incorrect forecasts in unfamiliar situations. We propose a self-supervised method that trains a decoder in a post-hoc fashion on the self-supervised task of forecasting the second half of observed trajectories from the first half. The L2 norm of the gradient of this forecasting loss with respect to the decoder's final layer defines a score to identify distribution shifts. Our approach, first, does not affect the trajectory prediction model, ensuring no interference with original prediction performance and second, demonstrates substantial improvements on distribution shift detection for trajectory prediction on the Shifts and Argoverse datasets. Moreover, we show that this method can also be used to early detect collisions of a deep Q-Network motion planner in the Highway simulator. Source code is available at this https URL.

---


### 111. [Do Transformers Use their Depth Adaptively? Evidence from a Relational Reasoning Task](https://arxiv.org/abs/2604.12426)

**<font color=#1a73e8>作者：</font>** Alicia Curth, Rachel Lawrence, Sushrut Karmalkar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether transformers use their depth adaptively across tasks of increasing difficulty. Using a controlled multi-hop relational reasoning task based on family stories, where difficulty is determined by the number of relationship hops that must be composed, we monitor (i) how predictions evolve across layers via early readouts (the logit lens) and (ii) how task-relevant information is integrated across tokens via causal patching. For pretrained models, we find some limited evidence for adaptive depth use: some larger models need fewer layers to arrive at plausible answers for easier tasks, and models generally use more layers to integrate information across tokens as chain length increases. For models finetuned on the task, we find clearer and more consistent evidence of adaptive depth use, with the effect being stronger for less constrained finetuning regimes that do not preserve general language modeling abilities.

---


### 112. [Practical Evaluation of the Crypto-Agility Maturity Model](https://arxiv.org/abs/2604.12428)

**<font color=#1a73e8>作者：</font>** Leonie Wolf, Samson Umezulike, Gurur Öndarö 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographic agility is a key prerequisite for maintaining the long-term security of digital communication, particularly in light of the transition to post-quantum cryptography. To systematically assess this capability, Hohm et al. proposed the Crypto Agility Maturity Model (CAMM).
In this work, we present the first evaluation of the CAMM against established design principles for maturity models. Our analysis reveals that the CAMM only partially satisfies these principles: its scope and target groups remain ambiguous; acceptance criteria are insufficiently operationalized, limiting verifiability and replicability; and dependency relations exhibit redundancies, cycles, and omissions. Applying the CAMM to a simple real-world scenario further confirmed these issues, as several requirements at higher maturity levels proved inapplicable or unclear. Based on these findings, we propose concrete improvements to the CAMM to enable more consistent and reliable assessments of cryptographic agility.

---


### 113. [VeriX-Anon: A Multi-Layered Framework for Mathematically Verifiable Outsourced Target-Driven Data Anonymization](https://arxiv.org/abs/2604.12431)

**<font color=#1a73e8>作者：</font>** Miit Daga, Swarna Priya Ramu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Organisations increasingly outsource privacy-sensitive data transformations to cloud providers, yet no practical mechanism lets the data owner verify that the contracted algorithm was faithfully executed. VeriX-Anon is a multi-layered verification framework for outsourced Target-Driven k-anonymization combining three orthogonal mechanisms: deterministic verification via Merkle-style hashing of an Authenticated Decision Tree, probabilistic verification via Boundary Sentinels near the Random Forest decision boundary and exact-duplicate Twins with cryptographic identifiers, and utility-based verification via Explainable AI fingerprinting that compares SHAP value distributions before and after anonymization using the Wasserstein distance. Evaluated on three cross-domain datasets against Lazy (drops 5 percent of records), Dumb (random splitting, fake hash), and Approximate (random splitting, valid hash) adversaries, VeriX-Anon correctly detected deviations in 11 of 12 scenarios. No single layer achieved this alone. The XAI layer was the only mechanism that caught the Approximate adversary, succeeding on Adult and Bank but failing on the severely imbalanced Diabetes dataset where class imbalance suppresses the SHAP signal, confirming the need for adaptive thresholding. An 11-point k-sweep showed Target-Driven anonymization preserves significantly more utility than Blind anonymization (Wilcoxon $p = 0.000977$, Cohen's $d = 1.96$, mean F1 gap $+0.1574$). Client-side verification completes under one second at one million rows. The threat model covers three empirically evaluated profiles and one theoretical profile (Informed Attacker) aware of trap embedding but unable to defeat the cryptographic salt. Sentinel evasion probability ranges from near-zero for balanced datasets to 0.52 for imbalanced ones, a limitation the twin layer compensates for in every tested scenario.

---


### 114. [A Hybrid Architecture for Benign-Malignant Classification of Mammography ROIs](https://arxiv.org/abs/2604.12437)

**<font color=#1a73e8>作者：</font>** Mohammed Asad, Mohit Bajpai, Sudhir Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate characterization of suspicious breast lesions in mammography is important for early diagnosis and treatment planning. While Convolutional Neural Networks (CNNs) are effective at extracting local visual patterns, they are less suited to modeling long-range dependencies. Vision Transformers (ViTs) address this limitation through self-attention, but their quadratic computational cost can be prohibitive. This paper presents a hybrid architecture that combines EfficientNetV2-M for local feature extraction with Vision Mamba, a State Space Model (SSM), for efficient global context modeling. The proposed model performs binary classification of abnormality-centered mammography regions of interest (ROIs) from the CBIS-DDSM dataset into benign and malignant classes. By combining a strong CNN backbone with a linear-complexity sequence model, the approach achieves strong lesion-level classification performance in an ROI-based setting.

---


### 115. [IAD-Unify: A Region-Grounded Unified Model for Industrial Anomaly Segmentation, Understanding, and Generation](https://arxiv.org/abs/2604.12440)

**<font color=#1a73e8>作者：</font>** Haoyu Zheng, Tianwei Lin, Wei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world industrial inspection requires not only localizing defects, but also explaining them in natural language and generating controlled defect edits. However, existing approaches fail to jointly support all three capabilities within a unified framework and evaluation protocol. We propose IAD-Unify, a dual-encoder unified framework in which a frozen DINOv2-based region expert supplies precise anomaly evidence to a shared Qwen3.5-4B vision-language backbone via lightweight token injection, jointly enabling anomaly segmentation, region-grounded understanding, and mask-guided generation. To enable unified evaluation, we further construct Anomaly-56K, a comprehensive unified multi-task IAD evaluation platform, spanning 59,916 images across 24 categories and 104 defect variants. Controlled ablations yield four findings: (i) region grounding is the decisive mechanism for understanding, removing it degrades location accuracy by >76 pp; (ii) predicted-region performance closely matches oracle, confirming deployment viability; (iii) region-grounded generation achieves the best full-image fidelity and masked-region perceptual quality; and (iv) pre-initialized joint training improves understanding at negligible generation cost (-0.16 dB). IAD-Unify further achieves strong performance on the MMAD benchmark, including categories unseen during training, demonstrating robust cross-category generalization.

---


### 116. [GLeMM: A large-scale multilingual dataset for morphological research](https://arxiv.org/abs/2604.12442)

**<font color=#1a73e8>作者：</font>** Hathout Nabil, Basilio Calderone, Fiammetta Namer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In derivational morphology, what mechanisms govern the variation in form-meaning relations between words? The answers to this type of questions are typically based on intuition and on observations drawn from limited data, even when a wide range of languages is considered. Many of these studies are difficult to replicate and generalize. To address this issue, we present GLeMM, a new derivational resource designed for experimentation and data-driven description in morphology. GLeMM is characterized by (i) its large size, (ii) its extensive coverage (currently amounting to seven European languages, i.e., German, English, Spanish, French, Italian, Polish, Russian, (iii) its fully automated design, identical across all languages, (iv) the automatic annotation of morphological features on each entry, as well as (v) the encoding of semantic descriptions for a significant subset of these entries. It enables researchers to address difficult questions, such as the role of form and meaning in word-formation, and to develop and experimentally test computational methods that identify the structures of derivational morphology. The article describes how GLeMM is created using Wiktionary articles and presents various case studies illustrating possible applications of the resource.

---


### 117. [DiffusionPrint: Learning Generative Fingerprints for Diffusion-Based Inpainting Localization](https://arxiv.org/abs/2604.12443)

**<font color=#1a73e8>作者：</font>** Paschalis Giakoumoglou, Symeon Papadopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern diffusion-based inpainting models pose significant challenges for image forgery localization (IFL), as their full regeneration pipelines reconstruct the entire image via a latent decoder, disrupting the camera-level noise patterns that existing forensic methods rely on. We propose DiffusionPrint, a patch-level contrastive learning framework that learns a forensic signal robust to the spectral distortions introduced by latent decoding. It exploits the fact that inpainted regions generated by the same model share a consistent generative fingerprint, using this as a self-supervisory signal. DiffusionPrint trains a convolutional backbone via a MoCo-style objective with cross-category hard negative mining and a generator-aware classification head, producing a forensic feature map that serves as a highly discriminative secondary modality in fusion-based IFL frameworks. Integrated into TruFor, MMFusion, and a lightweight fusion baseline, DiffusionPrint consistently improves localization across multiple generative models, with gains of up to +28% on mask types unseen during fine-tuning and confirmed generalization to unseen generative architectures. Code is available at this https URL

---


### 118. [Scaling Exposes the Trigger: Input-Level Backdoor Detection in Text-to-Image Diffusion Models via Cross-Attention Scaling](https://arxiv.org/abs/2604.12446)

**<font color=#1a73e8>作者：</font>** Zida Li, Jun Li, Yuzhe Sha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) diffusion models have achieved remarkable success in image synthesis, but their reliance on large-scale data and open ecosystems introduces serious backdoor security risks. Existing defenses, particularly input-level methods, are more practical for deployment but often rely on observable anomalies that become unreliable under stealthy, semantics-preserving trigger designs. As modern backdoor attacks increasingly embed triggers into natural inputs, these methods degrade substantially, raising a critical question: can more stable, implicit, and trigger-agnostic differences between benign and backdoor inputs be exploited for detection? In this work, we address this challenge from an active probing perspective. We introduce controlled scaling perturbations on cross-attention and uncover a novel phenomenon termed Cross-Attention Scaling Response Divergence (CSRD), where benign and backdoor inputs exhibit systematically different response evolution patterns across denoising steps. Building on this insight, we propose SET, an input-level backdoor detection framework that constructs response-offset features under multi-scale perturbations and learns a compact benign response space from a small set of clean samples. Detection is then performed by measuring deviations from this learned space, without requiring prior knowledge of the attack or access to model training. Extensive experiments demonstrate that SET consistently outperforms existing baselines across diverse attack methods, trigger types, and model settings, with particularly strong gains under stealthy implicit-trigger scenarios. Overall, SET improves AUROC by 9.1% and ACC by 6.5% over the best baseline, highlighting its effectiveness and robustness for practical deployment.

---


### 119. [Latent-Condensed Transformer for Efficient Long Context Modeling](https://arxiv.org/abs/2604.12452)

**<font color=#1a73e8>作者：</font>** Zeng You, Yaofo Chen, Qiuwu Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) face significant challenges in processing long contexts due to the linear growth of the key-value (KV) cache and quadratic complexity of self-attention. Existing approaches address these bottlenecks separately: Multi-head Latent Attention (MLA) reduces the KV cache by projecting tokens into a low-dimensional latent space, while sparse attention reduces computation. However, sparse methods cannot operate natively on MLA's compressed latent structure, missing opportunities for joint optimization. In this paper, we propose Latent-Condensed Attention (LCA), which directly condenses context within MLA's latent space, where the representation is disentangled into semantic latent vectors and positional keys. LCA separately aggregates semantic vectors via query-aware pooling and preserves positional keys via anchor selection. This approach jointly reduces both computational cost and KV cache without adding parameters. Beyond MLA, LCA's design is architecture-agnostic and readily extends to other attention mechanisms such as GQA. Theoretically, we prove a length-independent error bound. Experiments show LCA achieves up to 2.5$\times$ prefilling speedup and 90% KV cache reduction at 128K context while maintaining competitive performance.

---


### 120. [Enhancing Clustering: An Explainable Approach via Filtered Patterns](https://arxiv.org/abs/2604.12460)

**<font color=#1a73e8>作者：</font>** Motaz Ben Hassine, Saïd Jabbour  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning has become a central research area, with increasing attention devoted to explainable clustering, also known as conceptual clustering, which is a knowledge-driven unsupervised learning paradigm that partitions data into $\theta$ disjoint clusters, where each cluster is described by an explicit symbolic representation, typically expressed as a closed pattern or itemset. By providing human-interpretable cluster descriptions, explainable clustering plays an important role in explainable artificial intelligence and knowledge discovery. Recent work improved clustering quality by introducing k-relaxed frequent patterns (k-RFPs), a pattern model that relaxes strict coverage constraints through a generalized kcover definition. This framework integrates constraint-based reasoning, using SAT solvers for pattern generation, with combinatorial optimization, using Integer Linear Programming (ILP) for cluster selection. Despite its effectiveness, this approach suffers from a critical limitation: multiple distinct k-RFPs may induce identical k-covers, leading to redundant symbolic representations that unnecessarily enlarge the search space and increase computational complexity during cluster construction. In this paper, we address this redundancy through a pattern reduction framework. Our contributions are threefold. First, we formally characterize the conditions under which distinct k-RFPs induce identical kcovers, providing theoretical foundations for redundancy detection. Second, we propose an optimization strategy that removes redundant patterns by retaining a single representative pattern for each distinct k-cover. Third, we investigate the interpretability and representativeness of the patterns selected by the ILP model by analyzing their robustness with respect to their induced clusters. Extensive experiments conducted on several real-world datasets demonstrate that the proposed approach significantly reduces the pattern search space, improves computational efficiency, preserves and enhances in some cases the quality of the resulting clusters.

---


### 121. [Euler-inspired Decoupling Neural Operator for Efficient Pansharpening](https://arxiv.org/abs/2604.12463)

**<font color=#1a73e8>作者：</font>** Anqi Zhu, Mengting Ma, Yizhen Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pansharpening aims to synthesize high-resolution multispectral (HR-MS) images by fusing the spatial textures of panchromatic (PAN) images with the spectral information of low-resolution multispectral (LR-MS) images. While recent deep learning paradigms, especially diffusion-based operators, have pushed the performance boundaries, they often encounter spectral-spatial blurring and prohibitive computational costs due to their stochastic nature and iterative sampling. In this paper, we propose the Euler-inspired Decoupling Neural Operator (EDNO), a physics-inspired framework that redefines pansharpening as a continuous functional mapping in the frequency domain. Departing from conventional Cartesian feature processing, our EDNO leverages Euler's formula to transform features into a polar coordinate system, enabling a novel explicit-implicit interaction mechanism. Specifically, we develop the Euler Feature Interaction Layer (EFIL), which decouples the fusion task into two specialized modules: 1) Explicit Feature Interaction Module, utilizing a linear weighting scheme to simulate phase rotation for adaptive geometric alignment; and 2) Implicit Feature Interaction Module, employing a feed-forward network to model spectral distributions for superior color consistency. By operating in the frequency domain, EDNO inherently captures global receptive fields while maintaining discretization-invariance. Experimental results on the three datasets demonstrate that EDNO offers a superior efficiency-performance balance compared to heavyweight architectures.

---


### 122. [Intelligent ROI-Based Vehicle Counting Framework for Automated Traffic Monitoring](https://arxiv.org/abs/2604.12470)

**<font color=#1a73e8>作者：</font>** Mohamed A. Abdelwahab, Zaynab Al-Ariny, Mahmoud Fakhry 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate vehicle counting through video surveillance is crucial for efficient traffic management. However, achieving high counting accuracy while ensuring computational efficiency remains a challenge. To address this, we propose a fully automated, video-based vehicle counting framework designed to optimize both computational efficiency and counting accuracy. Our framework operates in two distinct phases: \textit{estimation} and \textit{prediction}. In the estimation phase, the optimal region of interest (ROI) is automatically determined using a novel combination of three models based on detection scores, tracking scores, and vehicle density. This adaptive approach ensures compatibility with any detection and tracking method, enhancing the framework's versatility. In the prediction phase, vehicle counting is efficiently performed within the estimated ROI. We evaluated our framework on benchmark datasets like UA-DETRAC, GRAM, CDnet 2014, and ATON. Results demonstrate exceptional accuracy, with most videos achieving 100\% accuracy, while also enhancing computational efficiency, making processing up to four times faster than full-frame processing. The framework outperforms existing techniques, especially in complex multi-road scenarios, demonstrating robustness and superior accuracy. These advancements make it a promising solution for real-time traffic monitoring.

---


### 123. [Latent Planning Emerges with Scale](https://arxiv.org/abs/2604.12493)

**<font color=#1a73e8>作者：</font>** Michael Hanna, Emmanuel Ameisen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs can perform seemingly planning-intensive tasks, like writing coherent stories or functioning code, without explicitly verbalizing a plan; however, the extent to which they implicitly plan is unknown. In this paper, we define latent planning as occurring when LLMs possess internal planning representations that (1) cause the generation of a specific future token or concept, and (2) shape preceding context to license said future token or concept. We study the Qwen-3 family (0.6B-14B) on simple planning tasks, finding that latent planning ability increases with scale. Models that plan possess features that represent a planned-for word like "accountant", and cause them to output "an" rather than "a"; moreover, even the less-successful Qwen-3 4B-8B have nascent planning mechanisms. On the more complex task of completing rhyming couplets, we find that models often identify a rhyme ahead of time, but even large models seldom plan far ahead. However, we can elicit some planning that increases with scale when steering models towards planned words in prose. In sum, we offer a framework for measuring planning and mechanistic evidence of how models' planning abilities grow with scale.

---


### 124. [Instantiating Bayesian CVaR lower bounds in Interactive Decision Making Problems](https://arxiv.org/abs/2604.12519)

**<font color=#1a73e8>作者：</font>** Raghav Bongole, Tobias J. Oechtering, Mikael Skoglund  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work established a generalized-Fano framework for lower bounding prior-predictive (Bayesian) CVaR in interactive statistical decision making. In this paper, we show how to instantiate that framework in concrete interactive problems and derive explicit Bayesian CVaR lower bounds from its abstract corollaries. Our approach compares a hard model with a reference model using squared Hellinger distance, and combines a lower bound on a reference hinge term with a bound on the distinguishability of the two models. We apply this approach to canonical examples, including Gaussian bandits, and obtain explicit bounds that make the dependence on key problem parameters transparent. These results show how the generalized-Fano Bayesian CVaR framework can be used as a practical lower-bound tool for interactive learning and risk-sensitive decision making.

---


### 125. [CoD-Lite: Real-Time Diffusion-Based Generative Image Compression](https://arxiv.org/abs/2604.12525)

**<font color=#1a73e8>作者：</font>** Zhaoyang Jia, Naifu Xue, Zihan Zheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advanced diffusion methods typically derive strong generative priors by scaling diffusion transformers. However, scaling fails to generalize when adapted for real-time compression scenarios that demand lightweight models. In this paper, we explore the design of real-time and lightweight diffusion codecs by addressing two pivotal questions. First, does diffusion pre-training benefit lightweight diffusion codecs? Through systematic analysis, we find that generation-oriented pre-training is less effective at small model scales whereas compression-oriented pre-training yields consistently better performance. Second, are transformers essential? We find that while global attention is crucial for standard generation, lightweight convolutions suffice for compression-oriented diffusion when paired with distillation. Guided by these findings, we establish a one-step lightweight convolution diffusion codec that achieves real-time $60$~FPS encoding and $42$~FPS decoding at 1080p. Further enhanced by distillation and adversarial learning, the proposed codec reduces bitrate by 85\% at a comparable FID to MS-ILLM, bridging the gap between generative compression and practical real-time deployment. Codes are released at this https URL

---


### 126. [Orthogonal Subspace Projection for Continual Machine Unlearning via SVD-Based LoRA](https://arxiv.org/abs/2604.12526)

**<font color=#1a73e8>作者：</font>** Yogachandran Rahulamathavan, Nasir Iqbal, Juncheng Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual machine unlearning aims to remove the influence of data that should no longer be retained, while preserving the usefulness of the model on everything else. This setting becomes especially difficult when deletion requests arrive sequentially, because the model must repeatedly adapt without erasing previously retained knowledge. Low-Rank Adaptation (LoRA) offers an efficient way to implement such updates, but naively combining many sequential LoRA modules leads to parameter collision, causing \textit{strong interference} between tasks. We propose a static alternative based on Singular Value Decomposition (SVD)-guided orthogonal subspace projection. Our method constrains each new LoRA update during training so that it lies in the orthogonal complement of the subspaces used by earlier unlearning tasks. This preserves task isolation without requiring dynamic routing at deployment. Experiments on CIFAR-100 with ResNet-20 and on MNIST show stable behavior across long sequences of unlearning tasks. After thirty sequential unlearning tasks, state-of-the-art static fusion reduces retained accuracy from 60.39\% to 12.70\%, whereas the proposed in-training constrained optimization maintains baseline performance ($\sim$58.1\%) while preserving strong unlearning efficacy.

---


### 127. [Technical Report -- A Context-Sensitive Multi-Level Similarity Framework for First-Order Logic Arguments: An Axiomatic Study](https://arxiv.org/abs/2604.12534)

**<font color=#1a73e8>作者：</font>** Victor David, Jérôme Delobelle, Jean-Guy Mailly  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Similarity in formal argumentation has recently gained attention due to its significance in problems such as argument aggregation in semantics and enthymeme decoding. While existing approaches focus on propositional logic, we address the richer setting of First-Order Logic (FOL), where similarity must account for structured content. We introduce a comprehensive framework for FOL argument similarity, built upon: (1) an extended axiomatic foundation; (2) a four-level parametric model covering predicates, literals, clauses, and formulae similarity; (3) two model families, one syntax-sensitive via language models, both integrating contextual weights for nuanced and explainable similarity; and (4) formal constraints enforcing desirable properties.

---


### 128. [Cross-Attentive Multiview Fusion of Vision-Language Embeddings](https://arxiv.org/abs/2604.12551)

**<font color=#1a73e8>作者：</font>** Tomas Berriel Martins, Martin R. Oswald, Javier Civera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models have been key to the development of open-vocabulary 2D semantic segmentation. Lifting these models from 2D images to 3D scenes, however, remains a challenging problem. Existing approaches typically back-project and average 2D descriptors across views, or heuristically select a single representative one, often resulting in suboptimal 3D representations. In this work, we introduce a novel multiview transformer architecture that cross-attends across vision-language descriptors from multiple viewpoints and fuses them into a unified per-3D-instance embedding. As a second contribution, we leverage multiview consistency as a self-supervision signal for this fusion, which significantly improves performance when added to a standard supervised target-class loss. Our Cross-Attentive Multiview Fusion, which we denote with its acronym CAMFusion, not only consistently outperforms naive averaging or single-view descriptor selection, but also achieves state-of-the-art results on 3D semantic and instance classification benchmarks, including zero-shot evaluations on out-of-domain datasets.

---


### 129. [FABLE: Fine-grained Fact Anchoring for Unstructured Model Editing](https://arxiv.org/abs/2604.12559)

**<font color=#1a73e8>作者：</font>** Peng Wang, Biyu Zhou, Xuehai Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unstructured model editing aims to update models with real-world text, yet existing methods often memorize text holistically without reliable fine-grained fact access. To address this, we propose FABLE, a hierarchical framework that decouples fine-grained fact injection from holistic text generation. FABLE follows a two-stage, fact-first strategy: discrete facts are anchored in shallow layers, followed by minimal updates to deeper layers to produce coherent text. This decoupling resolves the mismatch between holistic recall and fine-grained fact access, reflecting the unidirectional Transformer flow in which surface-form generation amplifies rather than corrects underlying fact representations. We also introduce UnFine, a diagnostic benchmark with fine-grained question-answer pairs and fact-level metrics for systematic evaluation. Experiments show that FABLE substantially improves fine-grained question answering while maintaining state-of-the-art holistic editing performance. Our code is publicly available at this https URL.

---


### 130. [Evolution-Inspired Sample Competition for Deep Neural Network Optimization](https://arxiv.org/abs/2604.12568)

**<font color=#1a73e8>作者：</font>** Ying Zheng, Yiyi Zhang, Yi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional deep network training generally optimizes all samples under a largely uniform learning paradigm, without explicitly modeling the heterogeneous competition among them. Such an oversimplified treatment can lead to several well-known issues, including bias under class imbalance, insufficient learning of hard samples, and the erroneous reinforcement of noisy samples. In this work, we present \textit{Natural Selection} (NS), a novel evolution-inspired optimization method that explicitly incorporates competitive interactions into deep network training. Unlike conventional sample reweighting strategies that rely mainly on predefined heuristics or static criteria, NS estimates the competitive status of each sample in a group-wise context and uses it to adaptively regulate its training contribution. Specifically, NS first assembles multiple samples into a composite image and rescales it to the original input size for model inference. Based on the resulting predictions, a natural selection score is computed for each sample to characterize its relative competitive variation within the constructed group. These scores are then used to dynamically reweight the sample-wise loss, thereby introducing an explicit competition-driven mechanism into the optimization process. In this way, NS provides a simple yet effective means of moving beyond uniform sample treatment and enables more adaptive and balanced model optimization. Extensive experiments on 12 public datasets across four image classification tasks demonstrate the effectiveness of the proposed method. Moreover, NS is compatible with diverse network architectures and does not depend on task-specific assumptions, indicating its strong generality and practical potential. The code will be made publicly available.

---


### 131. [Cross-Modal Knowledge Distillation for PET-Free Amyloid-Beta Detection from MRI](https://arxiv.org/abs/2604.12574)

**<font color=#1a73e8>作者：</font>** Francesco Chiumento, Julia Dietlmeier, Ronan P. Killeen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting amyloid-$\beta$ (A$\beta$) positivity is crucial for early diagnosis of Alzheimer's disease but typically requires PET imaging, which is costly, invasive, and not widely accessible, limiting its use for population-level screening. We address this gap by proposing a PET-guided knowledge distillation framework that enables A$\beta$ prediction from MRI alone, without requiring non-imaging clinical covariates or PET at inference. Our approach employs a BiomedCLIP-based teacher model that learns PET-MRI alignment via cross-modal attention and triplet contrastive learning with PET-informed (Centiloid-aware) online negative sampling. An MRI-only student then mimics the teacher via feature-level and logit-level distillation. Evaluated across four MRI contrasts (T1w, T2w, FLAIR, T2*) and two independent datasets, our approach demonstrates effective knowledge transfer (best AUC: 0.74 on OASIS-3, 0.68 on ADNI) while maintaining interpretability and eliminating the need for clinical variables. Saliency analysis confirms that predictions focus on anatomically relevant cortical regions, supporting the clinical viability of PET-free A$\beta$ screening. Code is available at this https URL.

---


### 132. [StructDiff: A Structure-Preserving and Spatially Controllable Diffusion Model for Single-Image Generation](https://arxiv.org/abs/2604.12575)

**<font color=#1a73e8>作者：</font>** Yinxi He, Kang Liao, Chunyu Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces StructDiff, a generative framework based on a single-scale diffusion model for single-image generation. Single-image generation aims to synthesize diverse samples with similar visual content to the source image by capturing its internal statistics, without relying on external data. However, existing methods often struggle to preserve the structural layout, especially for images with large rigid objects or strict spatial constraints. Moreover, most approaches lack spatial controllability, making it difficult to guide the structure or placement of generated content. To address these challenges, StructDiff introduces an \textit{adaptive receptive field} module to maintain both global and local distributions. Building on this foundation, StructDiff incorporates 3D positional encoding (PE) as a spatial prior, allowing flexible control over positions, scale, and local details of generated objects. To our knowledge, this spatial control capability represents the first exploration of PE-based manipulation in single-image generation. Furthermore, we propose a novel evaluation criterion for single-image generation based on large language models (LLMs). This criterion specifically addresses the limitations of existing objective metrics and the high labor costs associated with user studies. StructDiff also demonstrates broad applicability across downstream tasks, such as text-guided image generation, image editing, outpainting, and paint-to-image synthesis. Extensive experiments demonstrate that StructDiff outperforms existing methods in structural consistency, visual quality, and spatial controllability. The project page is available at this https URL.

---


### 133. [PDF-GS: Progressive Distractor Filtering for Robust 3D Gaussian Splatting](https://arxiv.org/abs/2604.12580)

**<font color=#1a73e8>作者：</font>** Kangmin Seo, MinKyu Lee, Tae-Young Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D Gaussian Splatting (3DGS) have enabled impressive real-time photorealistic rendering. However, conventional training pipelines inherently assume full multi-view consistency among input images, which makes them sensitive to distractors that violate this assumption and cause visual artifacts. In this work, we revisit an underexplored aspect of 3DGS: its inherent ability to suppress inconsistent signals. Building on this insight, we propose PDF-GS (Progressive Distractor Filtering for Robust 3D Gaussian Splatting), a framework that amplifies this self-filtering property through a progressive multi-phase optimization. The progressive filtering phases gradually remove distractors by exploiting discrepancy cues, while the following reconstruction phase restores fine-grained, view-consistent details from the purified Gaussian representation. Through this iterative refinement, PDF-GS achieves robust, high-fidelity, and distractor-free reconstructions, consistently outperforming baselines across diverse datasets and challenging real-world conditions. Moreover, our approach is lightweight and easily adaptable to existing 3DGS frameworks, requiring no architectural changes or additional inference overhead, leading to a new state-of-the-art performance. The code is publicly available at this https URL.

---


### 134. [ELoG-GS: Dual-Branch Gaussian Splatting with Luminance-Guided Enhancement for Extreme Low-light 3D Reconstruction](https://arxiv.org/abs/2604.12592)

**<font color=#1a73e8>作者：</font>** Yuhao Liu, Dingju Wang, Ziyang Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents our approach to the NTIRE 2026 3D Restoration and Reconstruction Challenge (Track 1), which focuses on reconstructing high-quality 3D representations from degraded multi-view inputs. The challenge involves recovering geometrically consistent and photorealistic 3D scenes in extreme low-light environments. To address this task, we propose Extreme Low-light Optimized Gaussian Splatting (ELoG-GS), a robust low-light 3D reconstruction pipeline that integrates learning-based point cloud initialization and luminance-guided color enhancement for stable and photorealistic Gaussian Splatting. Our method incorporates both geometry-aware initialization and photometric adaptation strategies to improve reconstruction fidelity under challenging conditions. Extensive experiments on the NTIRE Track 1 benchmark demonstrate that our approach significantly improves reconstruction quality over the baselines, achieving superior visual fidelity and geometric consistency. The proposed method provides a practical solution for robust 3D reconstruction in real-world degraded scenarios. In the final testing phase, our method achieved a PSNR of 18.6626 and an SSIM of 0.6855 on the official platform leaderboard. Code is available at this https URL.

---


### 135. [Spatial-Spectral Adaptive Fidelity and Noise Prior Reduction Guided Hyperspectral Image Denoising](https://arxiv.org/abs/2604.12600)

**<font color=#1a73e8>作者：</font>** Xuelin Xie, Xiliang Lu, Zhengshan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The core challenge of hyperspectral image denoising is striking the right balance between data fidelity and noise prior modeling. Most existing methods place too much emphasis on the intrinsic priors of the image while overlooking diverse noise assumptions and the dynamic trade-off between fidelity and priors. To address these issues, we propose a denoising framework that integrates noise prior reduction and a spatial-spectral adaptive fidelity term. This framework considers comprehensive noise priors with fewer parameters and introduces an adaptive weight tensor to dynamically balance the fidelity and prior regularization terms. Within this framework, we further develop a fast and robust pixel-wise model combined with the representative coefficient total variation regularizer to accurately remove mixed noise in HSIs. The proposed method not only efficiently handles various types of noise but also accurately captures the spectral low-rank structure and local smoothness of HSIs. An efficient optimization algorithm based on the alternating direction method of multipliers is designed to ensure stable and fast convergence. Extensive experiments on simulated and real-world datasets demonstrate that the proposed model achieves superior denoising performance while maintaining competitive computational efficiency.

---


### 136. [Efficient Semantic Image Communication for Traffic Monitoring at the Edge](https://arxiv.org/abs/2604.12622)

**<font color=#1a73e8>作者：</font>** Damir Assylbek, Nurmukhammed Aitymbetov, Marko Ristin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many visual monitoring systems operate under strict communication constraints, where transmitting full-resolution images is impractical and often unnecessary. In such settings, visual data is often used for object presence, spatial relationships, and scene context rather than exact pixel fidelity. This paper presents two semantic image communication pipelines for traffic monitoring, MMSD and SAMR, that reduce transmission cost while preserving meaningful visual information. MMSD (Multi-Modal Semantic Decomposition) targets very high compression together with data confidentiality, since sensitive pixel content is not transmitted. It replaces the original image with compact semantic representations, namely segmentation maps, edge maps, and textual descriptions, and reconstructs the scene at the receiver using a diffusion-based generative model. SAMR (Semantic-Aware Masking Reconstruction) targets higher visual quality while maintaining strong compression. It selectively suppresses non-critical image regions according to semantic importance before standard JPEG encoding and restores the missing content at the receiver through generative inpainting. Both designs follow an asymmetric sender-receiver architecture, where lightweight processing is performed at the edge and computationally intensive reconstruction is offloaded to the server. On a Raspberry Pi~5, the edge-side processing time is about 15s for MMSD and 9s for SAMR. Experimental results show average transmitted-data reductions of 99% for MMSD and 99.1% for SAMR. In addition, MMSD achieves lower payload size than the recent SPIC baseline while preserving strong semantic consistency, whereas SAMR provides a better quality-compression trade-off than standard JPEG and SQ-GAN under comparable operating conditions.

---


### 137. [GraphTide: Augmenting Knowledge-Intensive Text with Progressive Nested Graph](https://arxiv.org/abs/2604.12624)

**<font color=#1a73e8>作者：</font>** Xin Qian, Dazhen Deng, Zhaoping He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Knowledge-intensive text usually contains fruitful entities and complex relationships, such as academic articles and scientific exposition. Reading and comprehending such texts often demands considerable time and mental effort to track the relationships between entities. To reduce the burden, we present GraphTide, a visualization technique that progressively constructs nested entity-relationship graphs with animation to support the understanding of complex text. Our method features an on-demand entity-relationship decomposition pipeline that constructs nested graphs to represent intra- and inter-sentence relationships. Moreover, we propose a structure-aware force-directed layout optimization algorithm to enhance structural clarity. Sentences and their associated entities are incrementally revealed through animated transitions, helping users maintain context as the narrative unfolds. A user study shows that GraphTide significantly improves users' comprehension of knowledge-intensive texts compared to traditional graph-based techniques and static nested graph representations.

---


### 138. [Multilingual Multi-Label Emotion Classification at Scale with Synthetic Data](https://arxiv.org/abs/2604.12633)

**<font color=#1a73e8>作者：</font>** Vadim Borisov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion classification in multilingual settings remains constrained by the scarcity of annotated data: existing corpora are predominantly English, single-label, and cover few languages. We address this gap by constructing a large-scale synthetic training corpus of over 1M multi-label samples (50k per language) across 23 languages: Arabic, Bengali, Dutch, English, French, German, Hindi, Indonesian, Italian, Japanese, Korean, Mandarin, Polish, Portuguese, Punjabi, Russian, Spanish, Swahili, Tamil, Turkish, Ukrainian, Urdu, and Vietnamese, covering 11 emotion categories using culturally-adapted generation and programmatic quality filtering. We train and compare six multilingual transformer encoders, from DistilBERT (135M parameters) to XLM-R-Large (560M parameters), under identical conditions. On our in-domain test set, XLM-R-Large achieves 0.868 F1-micro and 0.987 AUC-micro. To validate against human-annotated data, we evaluate all models zero-shot on GoEmotions (English) and SemEval-2018 Task 1 E-c (English, Arabic, Spanish). On threshold-free ranking metrics, XLM-R-Large matches or exceeds English-only specialist models, tying on AP-micro (0.636) and LRAP (0.804) while surpassing on AUC-micro (0.810 vs. 0.787), while natively supporting all 23 languages. The best base-sized model is publicly available at this https URL

---


### 139. [Listening Deepfake Detection: A New Perspective Beyond Speaking-Centric Forgery Analysis](https://arxiv.org/abs/2604.12650)

**<font color=#1a73e8>作者：</font>** Miao Liu, Fangda Wei, Jing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing deepfake detection research has primarily focused on scenarios where the manipulated subject is actively speaking, i.e., generating fabricated content by altering the speaker's appearance or voice. However, in realistic interaction settings, attackers often alternate between falsifying speaking and listening states to mislead their targets, thereby enhancing the realism and persuasiveness of the scenario. Although the detection of 'listening deepfakes' remains largely unexplored and is hindered by a scarcity of both datasets and methodologies, the relatively limited quality of synthesized listening reactions presents an excellent breakthrough opportunity for current deepfake detection efforts. In this paper, we present the task of Listening Deepfake Detection (LDD). We introduce ListenForge, the first dataset specifically designed for this task, constructed using five Listening Head Generation (LHG) methods. To address the distinctive characteristics of listening forgeries, we propose MANet, a Motion-aware and Audio-guided Network that captures subtle motion inconsistencies in listener videos while leveraging speaker's audio semantics to guide cross-modal fusion. Extensive experiments demonstrate that existing Speaking Deepfake Detection (SDD) models perform poorly in listening scenarios. In contrast, MANet achieves significantly superior performance on ListenForge. Our work highlights the necessity of rethinking deepfake detection beyond the traditional speaking-centric paradigm and opens new directions for multimodal forgery analysis in interactive communication settings. The dataset and code are available at this https URL.

---


### 140. [Learning Chain Of Thoughts Prompts for Predicting Entities, Relations, and even Literals on Knowledge Graphs](https://arxiv.org/abs/2604.12651)

**<font color=#1a73e8>作者：</font>** Alkid Baci, Luke Friedrichs, Caglar Demir 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graph embedding (KGE) models perform well on link prediction but struggle with unseen entities, relations, and especially literals, limiting their use in dynamic, heterogeneous graphs. In contrast, pretrained large language models (LLMs) generalize effectively through prompting. We reformulate link prediction as a prompt learning problem and introduce RALP, which learns string-based chain-of-thought (CoT) prompts as scoring functions for triples. Using Bayesian Optimization through MIPRO algorithm, RALP identifies effective prompts from fewer than 30 training examples without gradient access. At inference, RALP predicts missing entities, relations or whole triples and assigns confidence scores based on the learned prompt. We evaluate on transductive, numerical, and OWL instance retrieval benchmarks. RALP improves state-of-the-art KGE models by over 5% MRR across datasets and enhances generalization via high-quality inferred triples. On OWL reasoning tasks with complex class expressions (e.g., $\exists this http URL$, $\geq 5 \; this http URL$), it achieves over 88% Jaccard similarity. These results highlight prompt-based LLM reasoning as a flexible alternative to embedding-based methods. We release our implementation, training, and evaluation pipeline as open source: this https URL .

---


### 141. [Robust Semi-Supervised Temporal Intrusion Detection for Adversarial Cloud Networks](https://arxiv.org/abs/2604.12655)

**<font color=#1a73e8>作者：</font>** Anasuya Chattopadhyay, Daniel Reti, Hans D. Schotten  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cloud networks increasingly rely on machine learning based Network Intrusion Detection Systems to defend against evolving cyber threats. However, real-world deployments are challenged by limited labeled data, non-stationary traffic, and adaptive adversaries. While semi-supervised learning can alleviate label scarcity, most existing approaches implicitly assume benign and stationary unlabeled traffic, leading to degraded performance in adversarial cloud environments. This paper proposes a robust semi-supervised temporal learning framework for cloud intrusion detection that explicitly addresses adversarial contamination and temporal drift in unlabeled network traffic. Operating on flow-level data, this framework combines supervised learning with consistency regularization, confidence-aware pseudo-labeling, and selective temporal invariance to conservatively exploit unlabeled traffic while suppressing unreliable samples. By leveraging the temporal structure of network flows, the proposed method improves robustness and generalization across heterogeneous cloud environments. Extensive evaluations on publicly available datasets (CIC-IDS2017, CSE-CIC-IDS2018, and UNSW-NB15) under limited-label conditions demonstrate that the proposed framework consistently outperforms state-of-the-art supervised and semi-supervised network intrusion detection systems in detection performance, label efficiency, and resilience to adversarial and non-stationary traffic.

---


### 142. [Do VLMs Truly "Read" Candlesticks? A Multi-Scale Benchmark for Visual Stock Price Forecasting](https://arxiv.org/abs/2604.12659)

**<font color=#1a73e8>作者：</font>** Kaiqi Hu, Linda Xiao, Shiyue Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models(VLMs) are increasingly applied to visual stock price forecasting, yet existing benchmarks inadequately evaluate their understanding of stock price in candlestick charts. First, prior studies fail to isolate VLMs' comprehension of visual inputs genuinely improves predictive performance and whether VLMs truly comprehend candlestick patterns. Further, most existing datasets and evaluation setups are designed around single-period or tabular inputs. However, human analysts strongly rely on multi-scale candlestick charts, where longer-term horizons capture trend direction and shorter-term horizons provide cues for inflection points, making it difficult to systematically assess VLMs' ability to integrate short-term and long-term visual market dynamics. To bridge this gap, we construct a multi-scale candlestick charts dataset and a standardized evaluation framework to assess VLMs' ability to utilize multi-scale visual market signals. Evaluation combines confusion-matrix-based diagnostics with information coefficient(IC) time series metrics and includes XGBoost as a feature-based temporal baseline. Using this dataset, we benchmark representative VLMs and analyze their ability to leverage multi-scale stock price data. Experimental results show that most VLMs perform well only under persistent uptrend or downtrend conditions, while exhibiting weak predictive capability in more common market scenarios. We also identify significant prediction biases and limited sensitivity to explicitly specified forecast horizons in prompts, indicating inherent limitations in precise temporal reasoning.

---


### 143. [Broadening the Applicability of Conditional Syntax Splitting for Reasoning from Conditional Belief Bases](https://arxiv.org/abs/2604.12660)

**<font color=#1a73e8>作者：</font>** Lars-Phillip Spiegel, Jonas Haldimann, Jesse Heyninck 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In nonmonotonic reasoning from conditional belief bases, an inference operator satisfying syntax splitting postulates allows for taking only the relevant parts of a belief base into account, provided that the belief base splits into subbases based on disjoint signatures. Because such disjointness is rare in practice, safe conditional syntax splitting has been proposed as a generalization of syntax splitting, allowing the conditionals in the subbases to share some atoms. Recently this overlap of conditionals has been shown to be limited to trivial, self-fulfilling conditionals. In this article, we propose a generalization of safe conditional syntax splittings that broadens the applicability of splitting postulates. In contrast to safe conditional syntax splitting, our generalized notion supports syntax splittings of a belief base {\Delta} where the subbases of {\Delta} may share atoms and nontrivial conditionals. We illustrate how this new notion overcomes limitations of previous splitting concepts, and we identify genuine splittings, separating them from simple splittings that do not provide benefits for inductive inference from {\Delta}. We introduce adjusted inference postulates based on our generalization of conditional syntax splitting, and we evaluate several popular inductive inference operators with respect to these postulates. Furthermore, we show that, while every inductive inference operator satisfying generalized conditional syntax splitting also satisfies conditional syntax splitting, the reverse does not hold.

---


### 144. [Human-Centric Topic Modeling with Goal-Prompted Contrastive Learning and Optimal Transport](https://arxiv.org/abs/2604.12663)

**<font color=#1a73e8>作者：</font>** Rui Wang, Yi Zheng, Dongxin Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing topic modeling methods, from LDA to recent neural and LLM-based approaches, which focus mainly on statistical coherence, often produce redundant or off-target topics that miss the user's underlying intent. We introduce Human-centric Topic Modeling, \emph{Human-TM}), a novel task formulation that integrates a human-provided goal directly into the topic modeling process to produce interpretable, diverse and goal-oriented topics. To tackle this challenge, we propose the \textbf{G}oal-prompted \textbf{C}ontrastive \textbf{T}opic \textbf{M}odel with \textbf{O}ptimal \textbf{T}ransport (GCTM-OT), which first uses LLM-based prompting to extract goal candidates from documents, then incorporates these into semantic-aware contrastive learning via optimal transport for topic discovery. Experimental results on three public subreddit datasets show that GCTM-OT outperforms state-of-the-art baselines in topic coherence and diversity while significantly improving alignment with human-provided goals, paving the way for more human-centric topic discovery systems.

---


### 145. [Hypergraph-State Collaborative Reasoning for Multi-Object Tracking](https://arxiv.org/abs/2604.12665)

**<font color=#1a73e8>作者：</font>** Zikai Song, Junqing Yu, Yi-Ping Phoebe Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion reasoning serves as the cornerstone of multi-object tracking (MOT), as it enables consistent association of targets across frames. However, existing motion estimation approaches face two major limitations: (1) instability caused by noisy or probabilistic predictions, and (2) vulnerability under occlusion, where trajectories often fragment once visual cues disappear. To overcome these issues, we propose a collaborative reasoning framework that enhances motion estimation through joint inference among multiple correlated objects. By allowing objects with similar motion states to mutually constrain and refine each other, our framework stabilizes noisy trajectories and infers plausible motion continuity even when target is occluded. To realize this concept, we design HyperSSM, an architecture that integrates Hypergraph computation and a State Space Model (SSM) for unified spatial-temporal reasoning. The Hypergraph module captures spatial motion correlations through dynamic hyperedges, while the SSM enforces temporal smoothness via structured state transitions. This synergistic design enables simultaneous optimization of spatial consensus and temporal coherence, resulting in robust and stable motion estimation. Extensive experiments on four mainstream and diverse benchmarks(MOT17, MOT20, DanceTrack, and SportsMOT) covering various motion patterns and scene complexities, demonstrate that our approach achieves state-of-the-art performance across a wide range of tracking scenarios.

---


### 146. [Safe reinforcement learning with online filtering for fatigue-predictive human-robot task planning and allocation in production](https://arxiv.org/abs/2604.12667)

**<font color=#1a73e8>作者：</font>** Jintao Xue, Xiao Li, Nianmin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-robot collaborative manufacturing, a core aspect of Industry 5.0, emphasizes ergonomics to enhance worker well-being. This paper addresses the dynamic human-robot task planning and allocation (HRTPA) problem, which involves determining when to perform tasks and who should execute them to maximize efficiency while ensuring workers' physical fatigue remains within safe limits. The inclusion of fatigue constraints, combined with production dynamics, significantly increases the complexity of the HRTPA problem. Traditional fatigue-recovery models in HRTPA often rely on static, predefined hyperparameters. However, in practice, human fatigue sensitivity varies daily due to factors such as changed work conditions and insufficient sleep. To better capture this uncertainty, we treat fatigue-related parameters as inaccurate and estimate them online based on observed fatigue progression during production. To address these challenges, we propose PF-CD3Q, a safe reinforcement learning (safe RL) approach that integrates the particle filter with constrained dueling double deep Q-learning for real-time fatigue-predictive HRTPA. Specifically, we first develop PF-based estimators to track human fatigue and update fatigue model parameters in real-time. These estimators are then integrated into CD3Q by making task-level fatigue predictions during decision-making and excluding tasks that exceed fatigue limits, thereby constraining the action space and formulating the problem as a constrained Markov decision process (CMDP).

---


### 147. [OFA-Diffusion Compression: Compressing Diffusion Model in One-Shot Manner](https://arxiv.org/abs/2604.12668)

**<font color=#1a73e8>作者：</font>** Haoyang Jiang, Zekun Wang, Mingyang Yi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Diffusion Probabilistic Model (DPM) achieves remarkable performance in image generation, while its increasing parameter size and computational overhead hinder its deployment in practical applications. To improve this, the existing literature focuses on obtaining a smaller model with a fixed architecture through model compression. However, in practice, DPMs usually need to be deployed on various devices with different resource constraints, which leads to multiple compression processes, incurring significant overhead for repeated training. To obviate this, we propose a once-for-all (OFA) compression framework for DPMs that yields different subnetworks with various computations in a one-shot training manner. The existing OFA framework typically involves massive subnetworks with different parameter sizes, while such a huge candidate space slows the optimization. Thus, we propose to restrict the candidate subnetworks with a certain set of parameter sizes, where each size corresponds to a specific subnetwork. Specifically, to construct each subnetwork with a given size, we gradually allocate the maintained channels by their importance. Furthermore, we propose a reweighting strategy to balance the optimization process of different subnetworks. Experimental results show that our approach can produce compressed DPMs for various sizes with significantly lower training overhead while achieving satisfactory performance.

---


### 148. [A hierarchical spatial-aware algorithm with efficient reinforcement learning for human-robot task planning and allocation in production](https://arxiv.org/abs/2604.12669)

**<font color=#1a73e8>作者：</font>** Jintao Xue, Xiao Li, Nianmin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In advanced manufacturing systems, humans and robots collaborate to conduct the production process. Effective task planning and allocation (TPA) is crucial for achieving high production efficiency, yet it remains challenging in complex and dynamic manufacturing environments. The dynamic nature of humans and robots, particularly the need to consider spatial information (e.g., humans' real-time position and the distance they need to move to complete a task), substantially complicates TPA. To address the above challenges, we decompose production tasks into manageable subtasks. We then implement a real-time hierarchical human-robot TPA algorithm, including a high-level agent for task planning and a low-level agent for task allocation. For the high-level agent, we propose an efficient buffer-based deep Q-learning method (EBQ), which reduces training time and enhances performance in production problems with long-term and sparse reward challenges. For the low-level agent, a path planning-based spatially aware method (SAP) is designed to allocate tasks to the appropriate human-robot resources, thereby achieving the corresponding sequential subtasks. We conducted experiments on a complex real-time production process in a 3D simulator. The results demonstrate that our proposed EBQ&SAP method effectively addresses human-robot TPA problems in complex and dynamic production processes.

---


### 149. [BID-LoRA: A Parameter-Efficient Framework for Continual Learning and Unlearning](https://arxiv.org/abs/2604.12686)

**<font color=#1a73e8>作者：</font>** Jagadeesh Rachapudi, Ritali Vatsi, Praful Hambarde 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in deep learning underscore the need for systems that can not only acquire new knowledge through Continual Learning (CL) but also remove outdated, sensitive, or private information through Machine Unlearning (MU). However, while CL methods are well-developed, MU techniques remain in early stages, creating a critical gap for unified frameworks that depend on both capabilities. We find that naively combining existing CL and MU approaches results in knowledge leakage a gradual degradation of foundational knowledge across repeated adaptation cycles. To address this, we formalize Continual Learning Unlearning (CLU) as a unified paradigm with three key goals: (i) precise deletion of unwanted knowledge, (ii) efficient integration of new knowledge while preserving prior information, and (iii) minimizing knowledge leakage across cycles. We propose Bi-Directional Low-Rank Adaptation (BID-LoRA), a novel framework featuring three dedicated adapter pathways-retain, new, and unlearn applied to attention layers, combined with escape unlearning that pushes forget-class embeddings to positions maximally distant from retained knowledge, updating only 5% of parameters. Experiments on CIFAR-100 show that BID-LoRA outperforms CLU baselines across multiple adaptation cycles. We further evaluate on CASIA-Face100, a curated face recognition subset, demonstrating practical applicability to real-world identity management systems where new users must be enrolled and withdrawn users removed.

---


### 150. [Risk-Calibrated Learning: Minimizing Fatal Errors in Medical AI](https://arxiv.org/abs/2604.12693)

**<font color=#1a73e8>作者：</font>** Abolfazl Mohammadi-Seif, Ricardo Baeza-Yates  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models often achieve expert-level accuracy in medical image classification but suffer from a critical flaw: semantic incoherence. These high-confidence mistakes that are semantically incoherent (e.g., classifying a malignant tumor as benign) fundamentally differ from acceptable errors which stem from visual ambiguity. Unlike safe, fine-grained disagreements, these fatal failures erode clinical trust. To address this, we propose Risk-Calibrated Learning, a technique that explicitly distinguishes between visual ambiguity (fine-grained errors) and catastrophic structural errors. By embedding a confusion-aware clinical severity matrix M into the optimization landscape, our method suppresses critical errors (false negatives) without requiring complex architectural changes. We validate our approach in four different imaging modalities: Brain Tumor MRI, ISIC 2018 (Dermoscopy), BreaKHis (Breast Histopathology), and SICAPv2 (Prostate Histopathology). Extensive experiments demonstrate that our Risk-Calibrated Loss consistently reduces the Critical Error Rate (CER) for all four datasets, achieving relative safety improvements ranging from 20.0% (on breast histopathology) to 92.4% (on prostate histopathology) compared to state-of-the-art baselines such as Focal Loss. These results confirm that our method offers a superior safety-accuracy trade-off across both CNN and Transformer architectures.

---


### 151. [Information-Theoretic Optimization for Task-Adapted Compressed Sensing Magnetic Resonance Imaging](https://arxiv.org/abs/2604.12709)

**<font color=#1a73e8>作者：</font>** Xinyu Peng, Ziyang Zheng, Wenrui Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task-adapted compressed sensing magnetic resonance imaging (CS-MRI) is emerging to address the specific demands of downstream clinical tasks with significantly fewer k-space measurements than required by Nyquist sampling. However, existing task-adapted CS-MRI methods suffer from the uncertainty problem for medical diagnosis and cannot achieve adaptive sampling in end-to-end optimization with reconstruction or clinical tasks. To address these limitations, we propose the first task-adapted CS-MRI from the information-theoretic perspective to simultaneously achieve probabilistic inference for uncertainty prediction and adapt to arbitrary sampling ratios and versatile clinical applications. Specifically, we formalize the task-adapted CS-MRI optimization problem by maximizing the mutual information between undersampled k-space measurements and clinical tasks to enable probabilistic inference for addressing the uncertainty problem. We leverage amortized optimization and construct tractable variational bounds for mutual information to jointly optimize sampling, reconstruction, and task-inference models, which enables flexible sampling ratio control using a single end-to-end trained model. Furthermore, the proposed framework addresses two kinds of distinct clinical scenarios within a unified approach, i.e., i) joint task and reconstruction, where reconstruction serves as an auxiliary process to enhance task performance; and ii) task implementation with suppressed reconstruction, applicable for privacy protection. Extensive experiments on large-scale MRI datasets demonstrate that the proposed framework achieves highly competitive performance on standard metrics like Dice compared to deterministic counterpart but provides better distribution matching to the ground-truth posterior distribution as measured by the generalized energy distance (GED).

---


### 152. [Transferable Expertise for Autonomous Agents via Real-World Case-Based Learning](https://arxiv.org/abs/2604.12717)

**<font color=#1a73e8>作者：</font>** Zhenyu Ma, Yuyang Song, Chunyi Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based autonomous agents perform well on general reasoning tasks but still struggle to reliably use task structure, key constraints, and prior experience in complex real-world settings. We propose a case-based learning framework that converts experience from past tasks into reusable knowledge assets, allowing agents to transfer prior case experience to new tasks and perform more structured analysis. Unlike methods based mainly on pretrained knowledge or static prompts, our framework emphasizes extracting and reusing task-relevant knowledge, analytical prompts, and operational skills from real cases. We evaluate the method on a unified benchmark of six complex task categories and compare it with Zero-Shot, Few-Shot, Checklist Prompt, and Rule Memory baselines. Results show that our method achieves consistently strong performance across all tasks and matches or outperforms the best baseline in every case, with especially clear gains on more complex tasks. Further analysis shows that the advantage of case-based learning increases with task complexity, and that practical knowledge acquired by one agent can be reused by others. These findings suggest that case-based learning offers a promising path for building professional agents for real-world work.

---


### 153. [Monte Carlo Stochastic Depth for Uncertainty Estimation in Deep Learning](https://arxiv.org/abs/2604.12719)

**<font color=#1a73e8>作者：</font>** Adam T. Müller, Tobias Rögelein, Nicolaj C. Stache  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The deployment of deep neural networks in safety-critical systems necessitates reliable and efficient uncertainty quantification (UQ). A practical and widespread strategy for UQ is repurposing stochastic regularizers as scalable approximate Bayesian inference methods, such as Monte Carlo Dropout (MCD) and MC-DropBlock (MCDB). However, this paradigm remains under-explored for Stochastic Depth (SD), a regularizer integral to the residual-based backbones of most modern architectures. While prior work demonstrated its empirical promise for segmentation, a formal theoretical connection to Bayesian variational inference and a benchmark on complex, multi-task problems like object detection are missing. In this paper, we first provide theoretical insights connecting Monte Carlo Stochastic Depth (MCSD) to principled approximate variational inference. We then present the first comprehensive empirical benchmark of MCSD against MCD and MCDB on state-of-the-art detectors (YOLO, RT-DETR) using the COCO and COCO-O datasets. Our results position MCSD as a robust and computationally efficient method that achieves highly competitive predictive accuracy (mAP), notably yielding slight improvements in calibration (ECE) and uncertainty ranking (AUARC) compared to MCD. We thus establish MCSD as a theoretically-grounded and empirically-validated tool for efficient Bayesian approximation in modern deep learning.

---


### 154. [Evaluating Differential Privacy Against Membership Inference in Federated Learning: Insights from the NIST Genomics Red Team Challenge](https://arxiv.org/abs/2604.12737)

**<font color=#1a73e8>作者：</font>** Gustavo de Carvalho Bertoli  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While Federated Learning (FL) mitigates direct data exposure, the resulting trained models remain susceptible to membership inference attacks (MIAs). This paper presents an empirical evaluation of Differential Privacy (DP) as a defense mechanism against MIAs in FL, leveraging the environment of the 2025 NIST Genomics Privacy-Preserving Federated Learning (PPFL) Red Teaming Event. To improve inference accuracy, we propose a stacking attack strategy that ensembles seven black-box estimators to train a meta-classifier on prediction probabilities and cross-entropy losses. We evaluate this methodology against target models under three privacy configurations: an unprotected convolutional neural network (CNN, $\epsilon=\infty$), a low-privacy DP model ($\epsilon=200$), and a high-privacy DP model ($\epsilon=10$). The attack outperforms all baselines in the No DP and Low Privacy settings and, critically, maintains measurable membership leakage at $\epsilon=200$ where a single-signal LiRA baseline collapses. Evaluated on an independent third-party benchmark, these results provide an empirical characterisation of how stacking-based inference degrades across calibrated DP tiers in FL.

---


### 155. [Can AI Tools Transform Low-Demand Math Tasks? An Evaluation of Task Modification Capabilities](https://arxiv.org/abs/2604.12743)

**<font color=#1a73e8>作者：</font>** Danielle S. Fox, Brenda L. Robles, Elizabeth DiPietro Brovey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While recent research has explored AI tools' ability to classify the quality of mathematical tasks (arXiv:2603.03512), little is known about their capacity to increase the quality of existing tasks. This study investigated whether AI tools could successfully upgrade low-cognitive-demand mathematics tasks. Eleven tools were tested, including six broadly available, general-purpose AI tools (e.g., ChatGPT and Claude) and five tools specialized for mathematics teachers (e.g., Khanmigo, this http URL). Using the Task Analysis Guide framework (Stein & Smith, 1998), we prompted AI tools to modify two different types of low-demand mathematical tasks. The prompting strategy aimed to represent likely approaches taken by knowledgeable teachers, rather than extensive optimization to find a more effective prompt (i.e., an optimistic typical outcome). On average, AI tools were only moderately successful: tasks were accurately upgraded only 64% of the time, with different AI tool performance ranging from quite weak (33%) to broadly successful (88%). Specialized tools were only moderately more successful than general-purpose tools. Failure modes included both "undershooting" (maintaining low cognitive demand) and "overshooting" (elevating tasks to an overly ambitious target category that likely would be rejected by teachers). Interestingly, there was a small negative correlation (r = -.35) between whether a given AI tool was able to correctly classify the cognitive demand of tasks and whether the AI was able to upgrade tasks, showing that the ability to modify tasks (i.e., a generative task) represents a distinct capability from the ability to classify them (i.e., judgement using a rubric). These findings have important implications for understanding AI's potential role in curriculum adaptation and highlight the need for specialized approaches to support teachers in modifying instructional materials.

---


### 156. [Universal NER v2: Towards a Massively Multilingual Named Entity Recognition Benchmark](https://arxiv.org/abs/2604.12744)

**<font color=#1a73e8>作者：</font>** Terra Blevins, Stephen Mayhew, Marek Šuppa 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While multilingual language models promise to bring the benefits of LLMs to speakers of many languages, gold-standard evaluation benchmarks in most languages to interrogate these assumptions remain scarce. The Universal NER project, now entering its fourth year, is dedicated to building gold-standard multilingual Named Entity Recognition (NER) benchmark datasets. Inspired by existing massively multilingual efforts for other core NLP tasks (e.g., Universal Dependencies), the project uses a general tagset and thorough annotation guidelines to collect standardized, cross-lingual annotations of named entity spans. The first installment (UNER v1) was released in 2024, and the project has continued and expanded since then, with various organizers, annotators, and collaborators in an active community.

---


### 157. [Stress Detection Using Wearable Physiological and Sociometric Sensors](https://arxiv.org/abs/2604.12746)

**<font color=#1a73e8>作者：</font>** Oscar Martinez Mozos, Virginia Sandulescu, Sally Andrews 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stress remains a significant social problem for individuals in modern societies. This paper presents a machine learning approach for the automatic detection of stress of people in a social situation by combining two sensor systems that capture physiological and social responses. We compare the performance using different classifiers including support vector machine, AdaBoost, and k-nearest neighbor. Our experimental results show that by combining the measurements from both sensor systems, we could accurately discriminate between stressful and neutral situations during a controlled Trier social stress test (TSST). Moreover, this paper assesses the discriminative ability of each sensor modality individually and considers their suitability for real-time stress detection. Finally, we present an study of the most discriminative features for stress detection.

---


### 158. [Scaling In-Context Segmentation with Hierarchical Supervision](https://arxiv.org/abs/2604.12752)

**<font color=#1a73e8>作者：</font>** T. Camaret Ndir, Marco Reisert, Robin T. Schirrmeister  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) enables medical image segmentation models to adapt to new anatomical structures from limited examples, reducing the clinical annotation burden. However, standard ICL methods typically rely on dense, global cross-attention, which scales poorly with image resolution. While recent approaches have introduced localized attention mechanisms, they often lack explicit supervision on the selection process, leading to redundant computation in non-informative regions. We propose PatchICL, a hierarchical framework that combines selective image patching with multi-level supervision. Our approach learns to actively identify and attend only to the most informative anatomical regions. Compared to UniverSeg, a strong global-attention baseline, PatchICL achieves competitive in-domain CT segmentation accuracy while reducing compute by 44\% at $512\times512$ resolution. On 35 out-of-domain datasets spanning diverse imaging modalities, PatchICL outperforms the baseline on 6 of 13 modality categories, with particular strength on modalities dominated by localized pathology such as OCT and dermoscopy. Training and evaluation code are available at this https URL

---


### 159. [GF-Score: Certified Class-Conditional Robustness Evaluation with Fairness Guarantees](https://arxiv.org/abs/2604.12757)

**<font color=#1a73e8>作者：</font>** Arya Shah, Kaveri Visavadiya, Manisha Padala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial robustness is essential for deploying neural networks in safety-critical applications, yet standard evaluation methods either require expensive adversarial attacks or report only a single aggregate score that obscures how robustness is distributed across classes. We introduce the \emph{GF-Score} (GREAT-Fairness Score), a framework that decomposes the certified GREAT Score into per-class robustness profiles and quantifies their disparity through four metrics grounded in welfare economics: the Robustness Disparity Index (RDI), the Normalized Robustness Gini Coefficient (NRGC), Worst-Case Class Robustness (WCR), and a Fairness-Penalized GREAT Score (FP-GREAT). The framework further eliminates the original method's dependence on adversarial attacks through a self-calibration procedure that tunes the temperature parameter using only clean accuracy correlations. Evaluating 22 models from RobustBench across CIFAR-10 and ImageNet, we find that the decomposition is exact, that per-class scores reveal consistent vulnerability patterns (e.g., ``cat'' is the weakest class in 76\% of CIFAR-10 models), and that more robust models tend to exhibit greater class-level disparity. These results establish a practical, attack-free auditing pipeline for diagnosing where certified robustness guarantees fail to protect all classes equally. We release our code on \href{this https URL}{GitHub}.

---


### 160. [A Dataset and Evaluation for Complex 4D Markerless Human Motion Capture](https://arxiv.org/abs/2604.12765)

**<font color=#1a73e8>作者：</font>** Yeeun Park, Miqdad Naduthodi, Suryansh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Marker-based motion capture (MoCap) systems have long been the gold standard for accurate 4D human modeling, yet their reliance on specialized hardware and markers limits scalability and real-world deployment. Advancing reliable markerless 4D human motion capture requires datasets that reflect the complexity of real-world human interactions. Yet, existing benchmarks often lack realistic multi-person dynamics, severe occlusions, and challenging interaction patterns, leading to a persistent domain gap. In this work, we present a new dataset and evaluation for complex 4D markerless human motion capture. Our proposed MoCap dataset captures both single and multi-person scenarios with intricate motions, frequent inter-person occlusions, rapid position exchanges between similarly dressed subjects, and varying subject distances. It includes synchronized multi-view RGB and depth sequences, accurate camera calibration, ground-truth 3D motion capture from a Vicon system, and corresponding SMPL/SMPL-X parameters. This setup ensures precise alignment between visual observations and motion ground truth. Benchmarking state-of-the-art markerless MoCap models reveals substantial performance degradation under these realistic conditions, highlighting limitations of current approaches. We further demonstrate that targeted fine-tuning improves generalization, validating the dataset's realism and value for model development. Our evaluation exposes critical gaps in existing models and provides a rigorous foundation for advancing robust markerless 4D human motion capture.

---


### 161. [Rethinking the Personalized Relaxed Initialization in the Federated Learning: Consistency and Generalization](https://arxiv.org/abs/2604.12768)

**<font color=#1a73e8>作者：</font>** Li Shen, Yan Sun, Dacheng Tao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a distributed paradigm that coordinates massive local clients to collaboratively train a global model via stage-wise local training processes on the heterogeneous dataset. Previous works have implicitly studied that FL suffers from the ``client-drift'' problem, which is caused by the inconsistent optimum across local clients. However, till now it still lacks solid theoretical analysis to explain the impact of this local inconsistency. To alleviate the negative impact of ``client drift'' and explore its substance in FL, in this paper, we first propose an efficient FL algorithm FedInit, which allows employing the personalized relaxed initialization state at the beginning of each local training stage. Specifically, FedInit initializes the local state by moving away from the current global state towards the reverse direction of the latest local state. Moreover, to further understand how inconsistency disrupts performance in FL, we introduce the excess risk analysis and study the divergence term to investigate the test error in FL. Our studies show that optimization error is not sensitive to this local inconsistency, while it mainly affects the generalization error bound. Extensive experiments are conducted to validate its efficiency. The proposed FedInit method could achieve comparable results compared to several advanced benchmarks without any additional training or communication costs. Meanwhile, the stage-wise personalized relaxed initialization could also be incorporated into several current advanced algorithms to achieve higher generalization performance in the FL paradigm.

---


### 162. [A Multi-Agent Feedback System for Detecting and Describing News Events in Satellite Imagery](https://arxiv.org/abs/2604.12772)

**<font color=#1a73e8>作者：</font>** Madeline Anderson, Mikhail Klassen, Ash Hoover 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Changes in satellite imagery often occur over multiple time steps. Despite the emergence of bi-temporal change captioning datasets, there is a lack of multi-temporal event captioning datasets (at least two images per sequence) in remote sensing. This gap exists because (1) searching for visible events in satellite imagery and (2) labeling multi-temporal sequences require significant time and labor. To address these challenges, we present SkyScraper, an iterative multi-agent workflow that geocodes news articles and synthesizes captions for corresponding satellite image sequences. Our experiments show that SkyScraper successfully finds 5x more events than traditional geocoding methods, demonstrating that agentic feedback is an effective strategy for surfacing new multi-temporal events in satellite imagery. We apply our framework to a large database of global news articles, curating a new multi-temporal captioning dataset with 5,000 sequences. By automatically identifying imagery related to news events, our work also supports journalism and reporting efforts.

---


### 163. [EvoSpark: Endogenous Interactive Agent Societies for Unified Long-Horizon Narrative Evolution](https://arxiv.org/abs/2604.12776)

**<font color=#1a73e8>作者：</font>** Shiyu He, Minchi Kuang, Mengxian Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Realizing endogenous narrative evolution in LLM-based multi-agent systems is hindered by the inherent stochasticity of generative emergence. In particular, long-horizon simulations suffer from social memory stacking, where conflicting relational states accumulate without resolution, and narrative-spatial dissonance, where spatial logic detaches from the evolving plot. To bridge this gap, we propose EvoSpark, a framework specifically designed to sustain logically coherent long-horizon narratives within Endogenous Interactive Agent Societies. To ensure consistency, the Stratified Narrative Memory employs a Role Socio-Evolutionary Base as living cognition, dynamically metabolizing experiences to resolve historical conflicts. Complementarily, Generative Mise-en-Scène mechanism enforces Role-Location-Plot alignment, synchronizing character presence with the narrative flow. Underpinning these is the Unified Narrative Operation Engine, which integrates an Emergent Character Grounding Protocol to transform stochastic sparking into persistent characters. This engine establishes a substrate that expands a minimal premise into an open-ended, evolving story world. Experiments demonstrate that EvoSpark significantly outperforms baselines across diverse paradigms, enabling the sustained generation of expressive and coherent narrative experiences.

---


### 164. [Cognition-Inspired Dual-Stream Semantic Enhancement for Vision-Based Dynamic Emotion Modeling](https://arxiv.org/abs/2604.12777)

**<font color=#1a73e8>作者：</font>** Huanzhen Wang, Ziheng Zhou, Zeng Tao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The human brain constructs emotional percepts not by processing facial expressions in isolation, but through a dynamic, hierarchical integration of sensory input with semantic and contextual knowledge. However, existing vision-based dynamic emotion modeling approaches often neglect emotion perception and cognitive theories. To bridge this gap between machine and human emotion perception, we propose cognition-inspired Dual-stream Semantic Enhancement (DuSE). Our model instantiates a dual-stream cognitive architecture. The first stream, a Hierarchical Temporal Prompt Cluster (HTPC), operationalizes the cognitive priming effect. It simulates how linguistic cues pre-sensitize neural pathways, modulating the processing of incoming visual stimuli by aligning textual semantics with fine-grained temporal features of facial dynamics. The second stream, a Latent Semantic Emotion Aggregator (LSEA), computationally models the knowledge integration process, akin to the mechanism described by the Conceptual Act Theory. It aggregates sensory inputs and synthesizes them with learned conceptual knowledge, reflecting the role of the hippocampus and default mode network in constructing a coherent emotional experience. By explicitly modeling these neuro-cognitive mechanisms, DuSE provides a more neurally plausible and robust framework for dynamic facial expression recognition (DFER). Extensive experiments on challenging in-the-wild benchmarks validate our cognition-centric approach, demonstrating that emulating the brain's strategies for emotion processing yields state-of-the-art performance and enhances model interpretability.

---


### 165. [A sequential explanatory mixed-methods study on the acceptance of a social robot for EFL speaking practice among Chinese primary school students: Insights from the Computers Are Social Actors (CASA) paradigm](https://arxiv.org/abs/2604.12789)

**<font color=#1a73e8>作者：</font>** Yiran Du, Jinlong Li, Huimin He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study investigates Chinese primary school students' acceptance of a social robot for English-as-a-foreign-language (EFL) speaking practice through a sequential explanatory mixed-methods design. Integrating the Technology Acceptance Model (TAM) and the Computers Are Social Actors (CASA) paradigm, the research explores both functional and social factors influencing learners' behavioural intention to use the robot. Quantitative data from 436 students were analysed using structural equation modelling, followed by qualitative interviews with twelve students to interpret the findings. Results show that perceived enjoyment and ease of use are the strongest predictors of acceptance, while social attributes such as warmth, anthropomorphism, and social presence significantly enhance enjoyment. Perceived intelligence affects usefulness but not ease of use. The findings suggest that emotional and social engagement are central to young learners' acceptance of educational robots, highlighting the importance of designing socially intelligent technologies that promote motivation and speaking confidence in EFL learning contexts.

---


### 166. [Human Agency, Causality, and the Human Computer Interface in High-Stakes Artificial Intelligence](https://arxiv.org/abs/2604.12793)

**<font color=#1a73e8>作者：</font>** Georges Hattab  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current discourse on Artificial Intelligence (AI) ethics, dominated by "trustworthy" and "responsible" AI, overlooks a more fundamental human-computer interaction (HCI) crisis: the erosion of human agency. This paper argues that the primary challenge of high-stakes AI systems is not trust, but the preservation of human causal control. We posit that "bad AI" will function as "bad UI," a metaphor for catastrophic interface failures that misrepresent system state and lead to human error. Applying Marshall McLuhan's media theory, AI can be framed as a technology of "augmentation" that simultaneously "amputates" the user's direct perception of causality. This places the interface as the critical locus where a "double uncertainty"--that of the human user and that of the probabilistic model--must be mediated. We critique current Explainable AI (XAI) for its correlational focus and failure to represent uncertainty. We conclude by proposing a rigorous, nested Causal-Agency Framework (CAF) that integrates causal models, uncertainty quantification, and human-centered evaluation to restore agency at the interface.

---


### 167. [VFA: Relieving Vector Operations in Flash Attention with Global Maximum Pre-computation](https://arxiv.org/abs/2604.12798)

**<font color=#1a73e8>作者：</font>** Yupeng Sun, Yanzhao Li, Zhiqiang Zou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> FlashAttention-style online softmax enables exact attention computation with linear memory by streaming score tiles through on-chip memory and maintaining a running maximum and normalizer. However, as attention kernels approach peak tensor-core/cube-core throughput on modern accelerators, non-matmul components of online softmax -- especially per-tile rowmax and rowsum reductions and rescale chains -- can become vector or SIMD limited and dominate latency. This paper revisits FlashAttention and proposes Vector Relieved Flash Attention (VFA), a hardware-friendly method that reduces rowmax-driven updates of the running maximum while retaining the online-softmax structure. VFA initializes the running maximum via a cheap approximation from key-block representations, reorders key-block traversal to prioritize high-impact sink and local blocks, and freezes the maximum for remaining blocks to avoid repeated reductions and rescaling. We further integrate VFA with block-sparse skipping methods such as BLASST to form Vector Relieved Sparse Attention (VSA), which reduces both block count and per-block overhead. Notably, VFA and VSA completely avoid the conditional rescale operation in the update stage used in FA4.0. Extensive evaluations on benchmarks including MMLU and MATH500, together with attention statistics, verify our design: (i) sink and local reordering stabilizes the running maximum early; (ii) simple Q and K block summaries fail due to intra-block heterogeneity; (iii) m-initialization is required when maxima appear in middle blocks. Overall, VFA and VSA efficiently alleviate online-softmax reduction bottlenecks without performance loss. Compared to the C16V32 baseline, C8V32, C4V32 and C4V16 achieve nearly two times speedup on modern hardware while hitting the vector bottleneck. With upcoming architecture improvements, C4V16 will deliver six times speedup by enhancing exponent capacity.

---


### 168. [Generative Anonymization in Event Streams](https://arxiv.org/abs/2604.12803)

**<font color=#1a73e8>作者：</font>** Adam T. Müller, Mihai Kocsis, Nicolaj C. Stache  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neuromorphic vision sensors offer low latency and high dynamic range, but their deployment in public spaces raises severe data protection concerns. Recent Event-to-Video (E2V) models can reconstruct high-fidelity intensity images from sparse event streams, inadvertently exposing human identities. Current obfuscation methods, such as masking or scrambling, corrupt the spatio-temporal structure, severely degrading data utility for downstream perception tasks. In this paper, to the best of our knowledge, we present the first generative anonymization framework for event streams to resolve this utility-privacy trade-off. By bridging the modality gap between asynchronous events and standard spatial generative models, our pipeline projects events into an intermediate intensity representation, leverages pretrained models to synthesize realistic, non-existent identities, and re-encodes the features back into the neuromorphic domain. Experiments demonstrate that our method reliably prevents identity recovery from E2V reconstructions while preserving the structural data integrity required for downstream vision tasks. Finally, to facilitate rigorous evaluation, we introduce a novel, synchronized real-world event and RGB dataset captured via precise robotic trajectories, providing a robust benchmark for future research in privacy-preserving neuromorphic vision.

---


### 169. [Image-to-Image Translation Framework Embedded with Rotation Symmetry Priors](https://arxiv.org/abs/2604.12805)

**<font color=#1a73e8>作者：</font>** Feiyu Tan, Heran Yang, Qihong Duan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-image translation (I2I) is a fundamental task in computer vision, focused on mapping an input image from a source domain to a corresponding image in a target domain while preserving domain-invariant features and adapting domain-specific attributes. Despite the remarkable success of deep learning-based I2I approaches, the lack of paired data and unsupervised learning framework still hinder their effectiveness. In this work, we address the challenge by incorporating transformation symmetry priors into image-to-image translation networks. Specifically, we introduce rotation group equivariant convolutions to achieve rotation equivariant I2I framework, a novel contribution, to the best of our knowledge, along this research direction. This design ensures the preservation of rotation symmetry, one of the most intrinsic and domain-invariant properties of natural and scientific images, throughout the network. Furthermore, we conduct a systematic study on image symmetry priors on real dataset and propose a novel transformation learnable equivariant convolutions (TL-Conv) that adaptively learns transformation groups, enhancing symmetry preservation across diverse datasets. We also provide a theoretical analysis of the equivariance error of TL-Conv, proving that it maintains exact equivariance in continuous domains and provide a bound for the error in discrete cases. Through extensive experiments across a range of I2I tasks, we validate the effectiveness and superior performance of our approach, highlighting the potential of equivariant networks in enhancing generation quality and its broad applicability. Our code is available at this https URL

---


### 170. [Rethinking Satellite Image Restoration for Onboard AI: A Lightweight Learning-Based Approach](https://arxiv.org/abs/2604.12807)

**<font color=#1a73e8>作者：</font>** Adrien Dorise, Marjorie Bellizzi, Omar Hlimi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite image restoration aims to improve image quality by compensating for degradations (e.g., noise and blur) introduced by the imaging system and acquisition conditions. As a fundamental preprocessing step, restoration directly impacts both ground-based product generation and emerging onboard AI applications. Traditional restoration pipelines based on sequential physical models are computationally intensive and slow, making them unsuitable for onboard environments. In this paper, we introduce ConvBEERS: a Convolutional Board-ready Embedded and Efficient Restoration model for Space to investigate whether a light and non-generative residual convolutional network, trained on simulated satellite data, can match or surpass a traditional ground-processing restoration pipeline across multiple operating conditions.
Experiments conducted on simulated datasets and real Pleiades-HR imagery demonstrate that the proposed approach achieves competitive image quality, with a +6.9dB PSNR improvement. Evaluation on a downstream object detection task demonstrates that restoration significantly improves performance, with up to +5.1% mAP@50. In addition, successful deployment on a Xilinx Versal VCK190 FPGA validates its practical feasibility for satellite onboard processing, with a ~41x reduction in latency compared to the traditional pipeline. These results demonstrate the relevance of using lightweight CNNs to achieve competitive restoration quality while addressing real-world constraints in spaceborne systems.

---


### 171. [Algorithmic Analysis of Dense Associative Memory: Finite-Size Guarantees and Adversarial Robustness](https://arxiv.org/abs/2604.12811)

**<font color=#1a73e8>作者：</font>** Madhava Gaikwad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dense Associative Memory (DAM) generalizes Hopfield networks through higher-order interactions and achieves storage capacity that scales as $O(N^{n-1})$ under suitable pattern separation conditions. Existing dynamical analyses primarily study the thermodynamic limit $N\to\infty$ with randomly sampled patterns and therefore do not provide finite-size guarantees or explicit convergence rates.
We develop an algorithmic analysis of DAM retrieval dynamics that yields finite-$N$ guarantees under explicit, verifiable pattern conditions. Under a separation assumption and a bounded-interference condition at high loading, we prove geometric convergence of asynchronous retrieval dynamics, which implies $O(\log N)$ convergence time once the trajectory enters the basin of attraction. We further establish adversarial robustness bounds expressed through an explicit margin condition that quantifies the number of corrupted bits tolerable per sweep, and derive capacity guarantees that scale as $\Theta(N^{n-1})$ up to polylogarithmic factors in the worst case, while recovering the classical $\Theta(N^{n-1})$ scaling for random pattern ensembles. Finally, we show that DAM retrieval dynamics admit a potential-game interpretation that ensures convergence to pure Nash equilibria under asynchronous updates.
Complete proofs are provided in the appendices, together with preliminary experiments that illustrate the predicted convergence, robustness, and capacity scaling behavior.

---


### 172. [Loop Corrections to the Training and Generalization Errors of Random Feature Models](https://arxiv.org/abs/2604.12827)

**<font color=#1a73e8>作者：</font>** Taeyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate random feature models in which neural networks sampled from a prescribed initialization ensemble are frozen and used as random features, with only the readout weights optimized. Adopting a statistical-physics viewpoint, we study the training, test, and generalization errors beyond the mean-kernel approximation. Since the predictor is a nonlinear functional of the induced random kernel, the ensemble-averaged errors depend not only on the mean kernel but also on higher-order fluctuation statistics. Within an effective field-theoretic framework, these finite-width contributions naturally appear as loop corrections. We derive the loop corrections to the training, test, and generalization errors, obtain their scaling laws, and support the theory with experimental verification.

---


### 173. [Detecting and refurbishing ground truth errors during training of deep learning-based echocardiography segmentation models](https://arxiv.org/abs/2604.12832)

**<font color=#1a73e8>作者：</font>** Iman Islam, Bram Ruijsink, Andrew J. Reader 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based medical image segmentation typically relies on ground truth (GT) labels obtained through manual annotation, but these can be prone to random errors or systematic biases. This study examines the robustness of deep learning models to such errors in echocardiography (echo) segmentation and evaluates a novel strategy for detecting and refurbishing erroneous labels during model training. Using the CAMUS dataset, we simulate three error types, then compare a loss-based GT label error detection method with one based on Variance of Gradients (VOG). We also propose a pseudo-labelling approach to refurbish suspected erroneous GT labels. We assess the performance of our proposed approach under varying error levels. Results show that VOG proved highly effective in flagging erroneous GT labels during training. However, a standard U-Net maintained strong performance under random label errors and moderate levels of systematic errors (up to 50%). The detection and refurbishment approach improved performance, particularly under high-error conditions.

---


### 174. [EXTree: Towards Supporting Explainability in Attribute-based Access Control](https://arxiv.org/abs/2604.12850)

**<font color=#1a73e8>作者：</font>** Shanampudi Pranaya Chowdary, Shamik Sural  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With increasing emphasis on transparency in digital governance, users expect more than silence when their access requests are denied by a system. However, authorization methods are notorious for their inability to provide any form of meaningful feedback under such situations. This paper shows a direction towards how the problem of explainability can be mitigated in the context of Attribute-based Access Control (ABAC), arguably the most researched topic in access control in recent years. We introduce EXTree, which represents ABAC policies optimized for both fast evaluation (Efficiency) and human-centric feedback (Explainability) in the form of a tree. Two strategic dimensions are investigated, namely, Feedback Evaluation Strategies - how to craft actionable explanations when access is denied, and Tree Construction Strategies - how the policy trees should be structured for efficient yet interpretable decisions. Through extensive experiments, we compare entropy-based, changeability-based, and randomly generated trees across multiple configurations. Our results demonstrate that EXTree, built for efficiency and interpretability, can bridge the gap between complex authorization logic and human understanding.

---


### 175. [PianoFlow: Music-Aware Streaming Piano Motion Generation with Bimanual Coordination](https://arxiv.org/abs/2604.12856)

**<font color=#1a73e8>作者：</font>** Xuan Wang, Kai Ruan, Jiayi Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-driven bimanual piano motion generation requires precise modeling of complex musical structures and dynamic cross-hand coordination. However, existing methods often rely on acoustic-only representations lacking symbolic priors, employ inflexible interaction mechanisms, and are limited to computationally expensive short-sequence generation. To address these limitations, we propose PianoFlow, a flow-matching framework for precise and coordinated bimanual piano motion synthesis. Our approach strategically leverages MIDI as a privileged modality during training, distilling these structured musical priors to achieve deep semantic understanding while maintaining audio-only inference. Furthermore, we introduce an asymmetric role-gated interaction module to explicitly capture dynamic cross-hand coordination through role-aware attention and temporal gating. To enable real-time streaming generation for arbitrarily long sequences, we design an autoregressive flow continuation scheme that ensures seamless cross-chunk temporal coherence. Extensive experiments on the PianoMotion10M dataset demonstrate that PianoFlow achieves superior quantitative and qualitative performance, while accelerating inference by over 9\times compared to previous methods.

---


### 176. [Artificial Intelligence for Modeling and Simulation of Mixed Automated and Human Traffic](https://arxiv.org/abs/2604.12857)

**<font color=#1a73e8>作者：</font>** Saeed Rahmani, Shiva Rasouli, Daphne Cornelisse 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles (AVs) are now operating on public roads, which makes their testing and validation more critical than ever. Simulation offers a safe and controlled environment for evaluating AV performance in varied conditions. However, existing simulation tools mainly focus on graphical realism and rely on simple rule-based models and therefore fail to accurately represent the complexity of driving behaviors and interactions. Artificial intelligence (AI) has shown strong potential to address these limitations; however, despite the rapid progress across AI methodologies, a comprehensive survey of their application to mixed autonomy traffic simulation remains lacking. Existing surveys either focus on simulation tools without examining the AI methods behind them, or cover ego-centric decision-making without addressing the broader challenge of modeling surrounding traffic. Moreover, they do not offer a unified taxonomy of AI methods covering individual behavior modeling to full scene simulation. To address these gaps, this survey provides a structured review and synthesis of AI methods for modeling AV and human driving behavior in mixed autonomy traffic simulation. We introduce a taxonomy that organizes methods into three families: agent-level behavior models, environment-level simulation methods, and cognitive and physics-informed methods. The survey analyzes how existing simulation platforms fall short of the needs of mixed autonomy research and outlines directions to narrow this gap. It also provides a chronological overview of AI methods and reviews evaluation protocols and metrics, simulation tools, and datasets. By covering both traffic engineering and computer science perspectives, we aim to bridge the gap between these two communities.

---


### 177. [From edges to meaning: Semantic line sketches as a cognitive scaffold for ancient pictograph invention](https://arxiv.org/abs/2604.12865)

**<font color=#1a73e8>作者：</font>** Seowung Leem, Lin Gu, Ruogu Fang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans readily recognize objects from sparse line drawings, a capacity that appears early in development and persists across cultures, suggesting neural rather than purely learned origins. Yet the computational mechanism by which the brain transforms high-level semantic knowledge into low-level visual symbols remains poorly understood. Here we propose that ancient pictographic writing emerged from the brain's intrinsic tendency to compress visual input into stable, boundary-based abstractions. We construct a biologically inspired digital twin of the visual hierarchy that encodes an image into low-level features, generates a contour sketch, and iteratively refines it through top-down feedback guided by semantic representations, mirroring the feedforward and recurrent architecture of the human visual cortex. The resulting symbols bear striking structural resemblance to early pictographs across culturally distant writing systems, including Egyptian hieroglyphs, Chinese oracle bone characters, and proto-cuneiform, and offer candidate interpretations for undeciphered scripts. Our findings support a neuro-computational origin of pictographic writing and establish a framework in which AI can recapitulate the cognitive processes by which humans first externalized perception into symbols.

---


### 178. [VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization](https://arxiv.org/abs/2604.12887)

**<font color=#1a73e8>作者：</font>** Andrei Atanov, Jesse Allardice, Roman Bachmann 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual tokenizers map high-dimensional raw pixels into a compressed representation for downstream modeling. Beyond compression, tokenizers dictate what information is preserved and how it is organized. A de facto standard approach to video tokenization is to represent a video as a spatiotemporal 3D grid of tokens, each capturing the corresponding local information in the original signal. This requires the downstream model that consumes the tokens, e.g., a text-to-video model, to learn to predict all low-level details "pixel-by-pixel" irrespective of the video's inherent complexity, leading to high learning complexity.
We present VideoFlexTok, which represents videos with a variable-length sequence of tokens structured in a coarse-to-fine manner -- where the first tokens (emergently) capture abstract information, such as semantics and motion, and later tokens add fine-grained details. The generative flow decoder enables realistic video reconstructions from any token count. This representation structure allows adapting the token count according to downstream needs and encoding videos longer than the baselines with the same budget.
We evaluate VideoFlexTok on class- and text-to-video generative tasks and show that it leads to more efficient training compared to 3D grid tokens, e.g., achieving comparable generation quality (gFVD and ViCLIP Score) with a 5x smaller model (1.1B vs 5.2B). Finally, we demonstrate how VideoFlexTok can enable long video generation without prohibitive computational cost by training a text-to-video model on 10-second 81-frame videos with only 672 tokens, 8x fewer than a comparable 3D grid tokenizer.

---


### 179. [TCL: Enabling Fast and Efficient Cross-Hardware Tensor Program Optimization via Continual Learning](https://arxiv.org/abs/2604.12891)

**<font color=#1a73e8>作者：</font>** Chaoyao Shen, Linfeng Jiang, Yixian Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning (DL) compilers rely on cost models and auto-tuning to optimize tensor programs for target hardware. However, existing approaches depend on large offline datasets, incurring high collection costs and offering suboptimal transferability across platforms. In this paper, we introduce TCL, a novel efficient and transferable compiler framework for fast tensor program optimization across diverse hardware platforms to address these challenges. Specifically, TCL is built on three core enablers: (1) the RDU Sampler, a data-efficient active learning strategy that selects only 10% of tensor programs by jointly optimizing Representativeness, Diversity, and Uncertainty, substantially reducing data collection costs while maintaining near-original model accuracy; (2) a new Mamba-based cost model that efficiently captures long-range schedule dependencies while achieving a favorable trade-off between prediction accuracy and computational cost through reduced parameterization and lightweight sequence modeling; and (3) a continuous knowledge distillation framework that effectively and progressively transfers knowledge across multiple hardware platforms while avoiding the parameter explosion and data dependency issues typically caused by traditional multi-task learning. Extensive experiments validate the effectiveness of each individual enabler and the holistic TCL framework. When optimizing a range of mainstream DL models on both CPU and GPU platforms, TCL achieves, on average, 16.8x and 12.48x faster tuning time, and 1.20x and 1.13x lower inference latency, respectively, compared to Tenset-MLP.

---


### 180. [Representing 3D Faces with Learnable B-Spline Volumes](https://arxiv.org/abs/2604.12894)

**<font color=#1a73e8>作者：</font>** Prashanth Chandran, Daoye Wang, Timo Bolkart  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present CUBE (Control-based Unified B-spline Encoding), a new geometric representation for human faces that combines B-spline volumes with learned features, and demonstrate its use as a decoder for 3D scan registration and monocular 3D face reconstruction. Unlike existing B-spline representations with 3D control points, CUBE is parametrized by a lattice (e.g., 8 x 8 x 8) of high-dimensional control features, increasing the model's expressivity. These features define a continuous, two-stage mapping from a 3D parametric domain to 3D Euclidean space via an intermediate feature space. First, high-dimensional control features are locally blended using the B-spline bases, yielding a high-dimensional feature vector whose first three values define a 3D base mesh. A small MLP then processes this feature vector to predict a residual displacement from the base shape, yielding the final refined 3D coordinates. To reconstruct 3D surfaces in dense semantic correspondence, CUBE is queried at 3D coordinates sampled from a fixed template mesh. Crucially, CUBE retains the local support property of traditional B-spline representations, enabling local surface editing by updating individual control features. We demonstrate the strengths of this representation by training transformer-based encoders to predict CUBE's control features from unstructured point clouds and monocular images, achieving state-of-the-art scan registration results compared to recent baselines.

---


### 181. [A Sanity Check on Composed Image Retrieval](https://arxiv.org/abs/2604.12904)

**<font color=#1a73e8>作者：</font>** Yikun Liu, Jiangchao Yao, Weidi Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) aims to retrieve a target image based on a query composed of a reference image, and a relative caption that specifies the desired modification. Despite the rapid development of CIR models, their performance is not well characterized by existing benchmarks, which inherently contain indeterminate queries degrading the evaluation (i.e., multiple candidate images, rather than solely the target image, meet the query criteria), and have not considered their effectiveness in the context of the multi-round system. Motivated by this, we consider improving the evaluation procedure from two aspects: 1) we introduce FISD, a Fully-Informed Semantically-Diverse benchmark, which employs generative models to precisely control the variables of reference-target image pairs, enabling a more accurate evaluation of CIR methods across six dimensions, without query ambiguity; 2) we propose an automatic multi-round agentic evaluation framework to probe the potential of the existing models in the interactive scenarios. By observing how models adapt and refine their choices over successive rounds of queries, this framework provides a more realistic appraisal of their efficacy in practical applications. Extensive experiments and comparisons prove the value of our novel evaluation on typical CIR methods.

---


### 182. [Round-Trip Translation Reveals What Frontier Multilingual Benchmarks Miss](https://arxiv.org/abs/2604.12911)

**<font color=#1a73e8>作者：</font>** Ronald Skorobogat, Ameya Prabhu, Matthias Bethge  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual benchmarks guide the development of frontier models. Yet multilingual evaluations reported by frontier models are structured similar to popular reasoning and knowledge benchmarks, but across many languages. We show such benchmarks, and consequently multilingual evaluations, measure mathematical reasoning and factual recall, not multilingual proficiency. For example, thinking variants dramatically outperform instruct variants on these benchmarks, yet often perform worse on real-world multilingual tasks, such as LMArena. We propose a simple alternative: evaluate multilingual capability via round-trip translation. Given text in a source language, translate it to a target language and back; semantic gaps between the original and result expose failures in multilingual generation capabilities. Round-trip translation correlates almost perfectly (\r{ho} = 0.94) with user ratings on LMArena with our benchmark, requires no human reference translations, and does not require a more capable multilingual judge than tested models. Lastly, we introduce Lost in Translation (LiT), a challenging round-trip translation benchmark spanning widely spoken languages worldwide, for realistic evaluation of multilingual frontier models.

---


### 183. [M3D-Stereo: A Multiple-Medium and Multiple-Degradation Dataset for Stereo Image Restoration](https://arxiv.org/abs/2604.12917)

**<font color=#1a73e8>作者：</font>** Deqing Yang, Yingying Liu, Qicong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration under adverse conditions, such as underwater, haze or fog, and low-light environments, remains a highly challenging problem due to complex physical degradations and severe information loss. Existing datasets are predominantly limited to a single degradation type or heavily rely on synthetic data without stereo consistency, inherently restricting their applicability in real-world scenarios. To address this, we introduce M3D-Stereo, a stereo dataset with 7904 high-resolution image pairs for image restoration research acquired in multiple media with multiple controlled degradation levels. It encompasses four degradation scenarios: underwater scatter, haze/fog, underwater low-light, and haze low-light. Each scenario forms a subset, and is divided into six levels of progressive degradation, allowing fine-grained evaluations of restoration methods with increasing severity of degradation. Collected via a laboratory setup, the dataset provides aligned stereo image pairs along with their pixel-wise consistent clear ground truths. Two restoration tasks, single-level and mixed-level degradation, were performed to verify its validity. M3D-Stereo establishes a better controlled and more realistic benchmark to evaluate image restoration and stereo matching methods in complex degradation environments. It is made public under LGPLv3 license.

---


### 184. [Radar-Camera BEV Multi-Task Learning with Cross-Task Attention Bridge for Joint 3D Detection and Segmentation](https://arxiv.org/abs/2604.12918)

**<font color=#1a73e8>作者：</font>** Ahmet İnanç, Özgür Erkent  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bird's-eye-view (BEV) representations are the dominant paradigm for 3D perception in autonomous driving, providing a unified spatial canvas where detection and segmentation features are geometrically registered to the same physical coordinate system. However, existing radar-camera fusion methods treat these tasks in isolation, missing the opportunity to share complementary information between them: detection features encode object-level geometry that can sharpen segmentation boundaries, while segmentation features provide dense semantic context that can anchor detection. We propose \textbf{CTAB} (Cross-Task Attention Bridge), a bidirectional module that exchanges features between detection and segmentation branches via multi-scale deformable attention in shared BEV space. CTAB is integrated into a multi-task framework with an Instance Normalization-based segmentation decoder and learnable BEV upsampling to provide a more detailed BEV representation. On nuScenes, CTAB improves segmentation on 7 classes over the joint multi-task baseline at essentially neutral detection. On a 4-class subset (drivable area, pedestrian crossing, walkway, vehicle), our joint multi-task model reaches comparable mIoU on 4 classes while simultaneously providing 3D detection.

---


### 185. [MetFuse: Figurative Fusion between Metonymy and Metaphor](https://arxiv.org/abs/2604.12919)

**<font color=#1a73e8>作者：</font>** Saptarshi Ghosh, Tianyu Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metonymy and metaphor often co-occur in natural language, yet computational work has studied them largely in isolation. We introduce a framework that transforms a literal sentence into three figurative variants: metonymic, metaphoric, and hybrid. Using this framework, we construct MetFuse, the first dedicated dataset of figurative fusion between metonymy and metaphor, containing 1,000 human-verified meaning-aligned quadruplets totaling 4,000 sentences. Extrinsic experiments on eight existing benchmarks show that augmenting training data with MetFuse consistently improves both metonymy and metaphor classification, with hybrid examples yielding the largest gains on metonymy tasks. Using this dataset, we also analyze how the presence of one figurative type impacts another. Our findings show that both human annotators and large language models better identify metonymy in hybrid sentences than in metonymy-only sentences, demonstrating that the presence of a metaphor makes a metonymic noun more explicit. Our dataset is publicly available at: this https URL.

---


### 186. [Pi-HOC: Pairwise 3D Human-Object Contact Estimation](https://arxiv.org/abs/2604.12923)

**<font color=#1a73e8>作者：</font>** Sravan Chittupalli, Ayush Jain, Dong Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Resolving real-world human-object interactions in images is a many-to-many challenge, in which disentangling fine-grained concurrent physical contact is particularly difficult. Existing semantic contact estimation methods are either limited to single-human settings or require object geometries (e.g., meshes) in addition to the input image. Current state-of-the-art leverages powerful VLM for category-level semantics but struggles with multi-human scenarios and scales poorly in inference. We introduce Pi-HOC, a single-pass, instance-aware framework for dense 3D semantic contact prediction of all human-object pairs. Pi-HOC detects instances, creates dedicated human-object (HO) tokens for each pair, and refines them using an InteractionFormer. A SAM-based decoder then predicts dense contact on SMPL human meshes for each human-object pair. On the MMHOI and DAMON datasets, Pi-HOC significantly improves accuracy and localization over state-of-the-art methods while achieving 20x higher throughput. We further demonstrate that predicted contacts improve SAM-3D image-to-mesh reconstruction via a test-time optimization algorithm and enable referential contact prediction from language queries without additional training.

---


### 187. [Grasp in Gaussians: Fast Monocular Reconstruction of Dynamic Hand-Object Interactions](https://arxiv.org/abs/2604.12929)

**<font color=#1a73e8>作者：</font>** Ayce Idil Aytekin, Xu Chen, Zhengyang Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Grasp in Gaussians (GraG), a fast and robust method for reconstructing dynamic 3D hand-object interactions from a single monocular video. Unlike recent approaches that optimize heavy neural representations, our method focuses on tracking the hand and the object efficiently, once initialized from pretrained large models. Our key insight is that accurate and temporally stable hand-object motion can be recovered using a compact Sum-of-Gaussians (SoG) representation, revived from classical tracking literature and integrated with generative Gaussian-based initializations. We initialize object pose and geometry using a video-adapted SAM3D pipeline, then convert the resulting dense Gaussian representation into a lightweight SoG via subsampling. This compact representation enables efficient and fast tracking while preserving geometric fidelity. For the hand, we adopt a complementary strategy: starting from off-the-shelf monocular hand pose initialization, we refine hand motion using simple yet effective 2D joint and depth alignment losses, avoiding per-frame refinement of a detailed 3D hand appearance model while maintaining stable articulation. Extensive experiments on public benchmarks demonstrate that GraG reconstructs temporally coherent hand-object interactions on long sequences 6.4x faster than prior work while improving object reconstruction by 13.4% and reducing hand's per-joint position error by over 65%.

---


### 188. [Direct Discrepancy Replay: Distribution-Discrepancy Condensation and Manifold-Consistent Replay for Continual Face Forgery Detection](https://arxiv.org/abs/2604.12941)

**<font color=#1a73e8>作者：</font>** Tianshuo Zhang, Haoyuan Zhang, Siran Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual face forgery detection (CFFD) requires detectors to learn emerging forgery paradigms without forgetting previously seen manipulations. Existing CFFD methods commonly rely on replaying a small amount of past data to mitigate forgetting. Such replay is typically implemented either by storing a few historical samples or by synthesizing pseudo-forgeries from detector-dependent perturbations. Under strict memory budgets, the former cannot adequately cover diverse forgery cues and may expose facial identities, while the latter remains strongly tied to past decision boundaries. We argue that the core role of replay in CFFD is to reinstate the distributions of previous forgery tasks during subsequent training. To this end, we directly condense the discrepancy between real and fake distributions and leverage real faces from the current stage to perform distribution-level replay. Specifically, we introduce Distribution-Discrepancy Condensation (DDC), which models the real-to-fake discrepancy via a surrogate factorization in characteristic-function space and condenses it into a tiny bank of distribution discrepancy maps. We further propose Manifold-Consistent Replay (MCR), which synthesizes replay samples through variance-preserving composition of these maps with current-stage real faces, yielding samples that reflect previous-task forgery cues while remaining compatible with current real-face statistics. Operating under an extremely small memory budget and without directly storing raw historical face images, our framework consistently outperforms prior CFFD baselines and significantly mitigates catastrophic forgetting. Replay-level privacy analysis further suggests reduced identity leakage risk relative to selection-based replay.

---


### 189. [Adaptive Data Dropout: Towards Self-Regulated Learning in Deep Neural Networks](https://arxiv.org/abs/2604.12945)

**<font color=#1a73e8>作者：</font>** Amar Gahir, Varshil Patel, Shreyank N Gowda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are typically trained by uniformly sampling large datasets across epochs, despite evidence that not all samples contribute equally throughout learning. Recent work shows that progressively reducing the amount of training data can improve efficiency and generalization, but existing methods rely on fixed schedules that do not adapt during training. In this work, we propose Adaptive Data Dropout, a simple framework that dynamically adjusts the subset of training data based on performance feedback. Inspired by self-regulated learning, our approach treats data selection as an adaptive process, increasing or decreasing data exposure in response to changes in training accuracy. We introduce a lightweight stochastic update mechanism that modulates the dropout schedule online, allowing the model to balance exploration and consolidation over time. Experiments on standard image classification benchmarks show that our method reduces effective training steps while maintaining competitive accuracy compared to static data dropout strategies. These results highlight adaptive data selection as a promising direction for efficient and robust training. Code will be released.

---


### 190. [GlintMarkers: Spatial Perception on XR Eyewear using Corneal Reflections](https://arxiv.org/abs/2604.12949)

**<font color=#1a73e8>作者：</font>** Seungjoo Lee, Vimal Mollyn, Chris Harrison 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present GlintMarkers, the first system to perform gaze-driven spatial perception using the inward-facing cameras on XR eyewear. Our key observation is that the cornea acts as a mirror that encodes both gaze direction and visual information about the environment in a small, low-contrast reflection. To extract spatial and semantic information from this reflection despite the camera's limited pixel budget, we present a passive retroreflective marker design that concentrates reflected near-infrared light onto the cornea, producing bright glint patterns. We develop a custom Perspective-n-Point (PnP) estimation framework adapted to corneal imaging and perform orientation and distance estimation of tagged objects, as well as unique object identification.

---


### 191. [The Verification Tax: Fundamental Limits of AI Auditing in the Rare-Error Regime](https://arxiv.org/abs/2604.12951)

**<font color=#1a73e8>作者：</font>** Jason Z Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The most cited calibration result in deep learning -- post-temperature-scaling ECE of 0.012 on CIFAR-100 (Guo et al., 2017) -- is below the statistical noise floor. We prove this is not a failure of the experiment but a law: the minimax rate for estimating calibration error with model error rate epsilon is Theta((Lepsilon/m)^{1/3}), and no estimator can beat it. This "verification tax" implies that as AI models improve, verifying their calibration becomes fundamentally harder -- with the same exponent in opposite directions. We establish four results that contradict standard evaluation practice: (1) self-evaluation without labels provides exactly zero information about calibration, bounded by a constant independent of compute; (2) a sharp phase transition at mepsilon approx 1 below which miscalibration is undetectable; (3) active querying eliminates the Lipschitz constant, collapsing estimation to detection; (4) verification cost grows exponentially with pipeline depth at rate L^K. We validate across five benchmarks (MMLU, TruthfulQA, ARC-Challenge, HellaSwag, WinoGrande; ~27,000 items) with 6 LLMs from 5 families (8B-405B parameters, 27 benchmark-model pairs with logprob-based confidence), 95% bootstrap CIs, and permutation tests. Self-evaluation non-significance holds in 80% of pairs. Across frontier models, 23% of pairwise comparisons are indistinguishable from noise, implying that credible calibration claims must report verification floors and prioritize active querying once gains approach benchmark resolution.

---


### 192. [An Optimal Sauer Lemma Over $k$-ary Alphabets](https://arxiv.org/abs/2604.12952)

**<font color=#1a73e8>作者：</font>** Steve Hanneke, Qinglin Meng, Shay Moran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Sauer-Shelah-Perles Lemma is a cornerstone of combinatorics and learning theory, bounding the size of a binary hypothesis class in terms of its Vapnik-Chervonenkis (VC) dimension. For classes of functions over a $k$-ary alphabet, namely the multiclass setting, the Natarajan dimension has long served as an analogue of VC dimension, yet the corresponding Sauer-type bounds are suboptimal for alphabet sizes $k>2$.
In this work, we establish a sharp Sauer inequality for multiclass and list prediction. Our bound is expressed in terms of the Daniely--Shalev-Shwartz (DS) dimension, and more generally with its extension, the list-DS dimension -- the combinatorial parameters that characterize multiclass and list PAC learnability. Our bound is tight for every alphabet size $k$, list size $\ell$, and dimension value, replacing the exponential dependence on $\ell$ in the Natarajan-based bound by the optimal polynomial dependence, and improving the dependence on $k$ as well. Our proof uses the polynomial method. In contrast to the classical VC case, where several direct combinatorial proofs are known, we are not aware of any purely combinatorial proof in the DS setting. This motivates several directions for future research, which are discussed in the paper.
As consequences, we obtain improved sample complexity upper bounds for list PAC learning and for uniform convergence of list predictors, sharpening the recent results of Charikar et al.~(STOC~2023), Hanneke et al.~(COLT~2024), and Brukhim et al.~(NeurIPS~2024).

---


### 193. [Distinguishers for Skew and Linearized Reed-Solomon Codes](https://arxiv.org/abs/2604.12954)

**<font color=#1a73e8>作者：</font>** Felicitas Hörmann, Anna-Lena Horlemann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generalized Reed-Solomon (GRS) and Gabidulin codes have been proposed for various code-based cryptosystems, though most such schemes without elaborate disguising techniques have been successfully attacked. Both code classes are prominent examples of the isometric families of (generalized) skew and linearized Reed-Solomon ((G)SRS and (G)LRS) codes which are obtained as evaluation codes from skew polynomials. Both GSRS and GLRS codes share the advantage of achieving the maximum possible error-decoding radius and thus promise smaller key sizes than e.g. Classic McEliece.
We investigate whether these generalizations can avoid the known structural attacks on GRS and Gabidulin codes. In particular, we prove that both GSRS and GLRS codes decompose into GRS subcodes and are thus efficiently distinguishable from random codes with a square code method. This applies to all parameters for which the code length $n$ and its dimension $k$ over the field $\mathbb{F}_{q^m}$ satisfy $m + 1 < k < n - \tfrac{1}{2} (m^2 + 3m)$. The distinguishability extends to GSRS and GLRS codes with Hamming-isometric disguising.
We further relate these findings to existing distinguishers for GRS, Gabidulin, and LRS codes, and extend known results on duals of SRS and LRS codes to the generalized setting allowing nonzero column multipliers. Finally, we provide explicit transformations between GSRS and GLRS codes, clarifying the algebraic relationship between the skew and linearized frameworks.

---


### 194. [Cycle-Consistent Search: Question Reconstructability as a Proxy Reward for Search Agent Training](https://arxiv.org/abs/2604.12967)

**<font color=#1a73e8>作者：</font>** Sohyun An, Shuibenyang Yuan, Hayeon Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has shown strong potential for optimizing search agents in complex information retrieval tasks. However, existing approaches predominantly rely on gold supervision, such as ground-truth answers, which is difficult to scale. To address this limitation, we propose Cycle-Consistent Search (CCS), a gold-supervision-free framework for training search agents, inspired by cycle-consistency techniques from unsupervised machine translation and image-to-image translation. Our key hypothesis is that an optimal search trajectory, unlike insufficient or irrelevant ones, serves as a lossless encoding of the question's intent. Consequently, a high-quality trajectory should preserve the information required to accurately reconstruct the original question, thereby inducing a reward signal for policy optimization. However, naive cycle-consistency objectives are vulnerable to information leakage, as reconstruction may rely on superficial lexical cues rather than the underlying search process. To reduce this effect, we apply information bottlenecks, including exclusion of the final response and named entity recognition (NER) masking of search queries. These constraints force reconstruction to rely on retrieved observations together with the structural scaffold, ensuring that the resulting reward signal reflects informational adequacy rather than linguistic redundancy. Experiments on question-answering benchmarks show that CCS achieves performance comparable to supervised baselines while outperforming prior methods that do not rely on gold supervision. These results suggest that CCS provides a scalable training paradigm for training search agents in settings where gold supervision is unavailable.

---


### 195. [Evolution of Optimization Methods: Algorithms, Scenarios, and Evaluations](https://arxiv.org/abs/2604.12968)

**<font color=#1a73e8>作者：</font>** Tong Zhang, Jiangning Zhang, Zhucun Xue 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Balancing convergence speed, generalization capability, and computational efficiency remains a core challenge in deep learning optimization. First-order gradient descent methods, epitomized by stochastic gradient descent (SGD) and Adam, serve as the cornerstone of modern training pipelines. However, large-scale model training, stringent differential privacy requirements, and distributed learning paradigms expose critical limitations in these conventional approaches regarding privacy protection and memory efficiency. To mitigate these bottlenecks, researchers explore second-order optimization techniques to surpass first-order performance ceilings, while zeroth-order methods reemerge to alleviate memory constraints inherent to large-scale training. Despite this proliferation of methodologies, the field lacks a cohesive framework that unifies underlying principles and delineates application scenarios for these disparate approaches. In this work, we retrospectively analyze the evolutionary trajectory of deep learning optimization algorithms and present a comprehensive empirical evaluation of mainstream optimizers across diverse model architectures and training scenarios. We distill key emerging trends and fundamental design trade-offs, pinpointing promising directions for future research. By synthesizing theoretical insights with extensive empirical evidence, we provide actionable guidance for designing next-generation highly efficient, robust, and trustworthy optimization methods. The code is available at this https URL.

---


### 196. [AbdomenGen: Sequential Volume-Conditioned Diffusion Framework for Abdominal Anatomy Generation](https://arxiv.org/abs/2604.12969)

**<font color=#1a73e8>作者：</font>** Yubraj Bhandari, Lavsen Dahal, Paul Segars 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computational phantoms are widely used in medical imaging research, yet current systems to generate controlled, clinically meaningful anatomical variations remain limited. We present AbdomenGen, a sequential volume-conditioned diffusion framework for controllable abdominal anatomy generation. We introduce the \textbf{Volume Control Scalar (VCS)}, a standardized residual that decouples organ size from body habitus, enabling interpretable volume modulation. Organ masks are synthesized sequentially, conditioning on the body mask and previously generated structures to preserve global anatomical coherence while supporting independent, multi-organ control. Across 11 abdominal organs, the proposed framework achieves strong geometric fidelity (e.g., liver dice $0.83 \pm 0.05$), stable single-organ calibration over $[-3,+3]$ VCS, and disentangled multi-organ modulation. To showcase clinical utility with a hepatomegaly cohort selected from MERLIN, Wasserstein-based VCS selection reduces distributional distance of training data by 73.6\% . These results demonstrate calibrated, distribution-aware anatomical generation suitable for controllable abdominal phantom construction and simulation studies.

---


### 197. [GlotOCR Bench: OCR Models Still Struggle Beyond a Handful of Unicode Scripts](https://arxiv.org/abs/2604.12978)

**<font color=#1a73e8>作者：</font>** Amir Hossein Kargaran, Nafiseh Nikeghbal, Jana Diesner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Optical character recognition (OCR) has advanced rapidly with the rise of vision-language models, yet evaluation has remained concentrated on a small cluster of high- and mid-resource scripts. We introduce GlotOCR Bench, a comprehensive benchmark evaluating OCR generalization across 100+ Unicode scripts. Our benchmark comprises clean and degraded image variants rendered from real multilingual texts. Images are rendered using fonts from the Google Fonts repository, shaped with HarfBuzz and rasterized with FreeType, supporting both LTR and RTL scripts. Samples of rendered images were manually reviewed to verify correct rendering across all scripts. We evaluate a broad suite of open-weight and proprietary vision-language models and find that most perform well on fewer than ten scripts, and even the strongest frontier models fail to generalize beyond thirty scripts. Performance broadly tracks script-level pretraining coverage, suggesting that current OCR systems rely on language model pretraining as much as on visual recognition. Models confronted with unfamiliar scripts either produce random noise or hallucinate characters from similar scripts they already know. We release the benchmark and pipeline for reproducibility. Pipeline Code: this https URL, Benchmark: this https URL.

---


### 198. [Parallax: Why AI Agents That Think Must Never Act](https://arxiv.org/abs/2604.12986)

**<font color=#1a73e8>作者：</font>** Joel Fokou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents are rapidly transitioning from experimental tools to operational infrastructure, with projections that 80% of enterprise applications will embed AI copilots by the end of 2026. As agents gain the ability to execute real-world actions (reading files, running commands, making network requests, modifying databases), a fundamental security gap has emerged. The dominant approach to agent safety relies on prompt-level guardrails: natural language instructions that operate at the same abstraction level as the threats they attempt to mitigate. This paper argues that prompt-based safety is architecturally insufficient for agents with execution capability and introduces Parallax, a paradigm for safe autonomous AI execution grounded in four principles: Cognitive-Executive Separation, which structurally prevents the reasoning system from executing actions; Adversarial Validation with Graduated Determinism, which interposes an independent, multi-tiered validator between reasoning and execution; Information Flow Control, which propagates data sensitivity labels through agent workflows to detect context-dependent threats; and Reversible Execution, which captures pre-destructive state to enable rollback when validation fails. We present OpenParallax, an open-source reference implementation in Go, and evaluate it using Assume-Compromise Evaluation, a methodology that bypasses the reasoning system entirely to test the architectural boundary under full agent compromise. Across 280 adversarial test cases in nine attack categories, Parallax blocks 98.9% of attacks with zero false positives under its default configuration, and 100% of attacks under its maximum-security configuration. When the reasoning system is compromised, prompt-level guardrails provide zero protection because they exist only within the compromised system; Parallax's architectural boundary holds regardless.

---


### 199. [Accelerating Speculative Decoding with Block Diffusion Draft Trees](https://arxiv.org/abs/2604.12989)

**<font color=#1a73e8>作者：</font>** Liran Ringel, Yaniv Romano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive language models by using a lightweight drafter to propose multiple future tokens, which the target model then verifies in parallel. DFlash shows that a block diffusion drafter can generate an entire draft block in a single forward pass and achieve state-of-the-art speculative decoding performance, outperforming strong autoregressive drafters such as EAGLE-3. Vanilla DFlash, however, still verifies only a single drafted trajectory per round, potentially limiting its acceptance length. We introduce DDTree (Diffusion Draft Tree), a method that constructs a draft tree directly from the per-position distributions of a block diffusion drafter. Under a fixed node budget, DDTree uses a simple best-first heap algorithm to select the continuations that are most likely to match the target model according to a surrogate defined by the draft model's output. The resulting tree is verified efficiently in a single target model forward pass using an ancestor-only attention mask. Because DDTree builds on DFlash, a leading draft model for speculative decoding, these gains place DDTree among the leading approaches to speculative decoding.

---


### 200. [LogicEval: A Systematic Framework for Evaluating Automated Repair Techniques for Logical Vulnerabilities in Real-World Software](https://arxiv.org/abs/2604.12994)

**<font color=#1a73e8>作者：</font>** Syed Md Mukit Rashid, Abdullah Al Ishtiaq, Kai Tu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Logical vulnerabilities in software stem from flaws in program logic rather than memory safety, which can lead to critical security failures. Although existing automated program repair techniques primarily focus on repairing memory corruption vulnerabilities, they struggle with logical vulnerabilities because of their limited semantic understanding of the vulnerable code and its expected behavior. On the other hand, recent successes of large language models (LLMs) in understanding and repairing code are promising. However, no framework currently exists to analyze the capabilities and limitations of such techniques for logical vulnerabilities. This paper aims to systematically evaluate both traditional and LLM-based repair approaches for addressing real-world logical vulnerabilities. To facilitate our assessment, we created the first ever dataset, LogicDS, of 86 logical vulnerabilities with assigned CVEs reflecting tangible security impact. We also developed a systematic framework, LogicEval, to evaluate patches for logical vulnerabilities. Evaluations suggest that compilation and testing failures are primarily driven by prompt sensitivity, loss of code context, and difficulty in patch localization.

---


### 201. [Bilevel Late Acceptance Hill Climbing for the Electric Capacitated Vehicle Routing Problem](https://arxiv.org/abs/2604.13013)

**<font color=#1a73e8>作者：</font>** Yinghao Qin, Mosab Bazargani, Edmund K. Burke 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper tackles the Electric Capacitated Vehicle Routing Problem (E-CVRP) through a bilevel optimization framework that handles routing and charging decisions separately or jointly depending on the search stage. By analyzing their interaction, we introduce a surrogate objective at the upper level to guide the search and accelerate convergence. A bilevel Late Acceptance Hill Climbing algorithm (b-LAHC) is introduced that operates through three phases: greedy descent, neighborhood exploration, and final solution refinement. b-LAHC operates with fixed parameters, eliminating the need for complex adaptation while remaining lightweight and effective. Extensive experiments on the IEEE WCCI-2020 benchmark show that b-LAHC achieves superior or competitive performance against eight state-of-the-art algorithms. Under a fixed evaluation budget, it attains near-optimal solutions on small-scale instances and sets 9/10 new best-known results on large-scale benchmarks, improving existing records by an average of 1.07%. Moreover, the strong correlation (though not universal) observed between the surrogate objective and the complete cost justifies the use of the surrogate objective while still necessitating a joint solution of both levels, thereby validating the effectiveness of the proposed bilevel framework and highlighting its potential for efficiently solving large-scale routing problems with a hierarchical structure.

---


### 202. [PAL: Personal Adaptive Learner](https://arxiv.org/abs/2604.13017)

**<font color=#1a73e8>作者：</font>** Megha Chakraborty, Darssan L. Eswaramoorthi, Madhur Thareja 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-driven education platforms have made some progress in personalisation, yet most remain constrained to static adaptation--predefined quizzes, uniform pacing, or generic feedback--limiting their ability to respond to learners' evolving understanding. This shortfall highlights the need for systems that are both context-aware and adaptive in real time. We introduce PAL (Personal Adaptive Learner), an AI-powered platform that transforms lecture videos into interactive learning experiences. PAL continuously analyzes multimodal lecture content and dynamically engages learners through questions of varying difficulty, adjusting to their responses as the lesson unfolds. At the end of a session, PAL generates a personalized summary that reinforces key concepts while tailoring examples to the learner's interests. By uniting multimodal content analysis with adaptive decision-making, PAL contributes a novel framework for responsive digital learning. Our work demonstrates how AI can move beyond static personalization toward real-time, individualized support, addressing a core challenge in AI-enabled education.

---


### 203. [Toward Autonomous Long-Horizon Engineering for ML Research](https://arxiv.org/abs/2604.13018)

**<font color=#1a73e8>作者：</font>** Guoxin Chen, Jie Chen, Lei Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous AI research has advanced rapidly, but long-horizon ML research engineering remains difficult: agents must sustain coherent progress across task comprehension, environment setup, implementation, experimentation, and debugging over hours or days. We introduce AiScientist, a system for autonomous long-horizon engineering for ML research built on a simple principle: strong long-horizon performance requires both structured orchestration and durable state continuity. To this end, AiScientist combines hierarchical orchestration with a permission-scoped File-as-Bus workspace: a top-level Orchestrator maintains stage-level control through concise summaries and a workspace map, while specialized agents repeatedly re-ground on durable artifacts such as analyses, plans, code, and experimental evidence rather than relying primarily on conversational handoffs, yielding thin control over thick state. Across two complementary benchmarks, AiScientist improves PaperBench score by 10.54 points on average over the best matched baseline and achieves 81.82 Any Medal% on MLE-Bench Lite. Ablation studies further show that File-as-Bus protocol is a key driver of performance, reducing PaperBench by 6.41 points and MLE-Bench Lite by 31.82 points when removed. These results suggest that long-horizon ML research engineering is a systems problem of coordinating specialized work over durable project state, rather than a purely local reasoning problem.

---


### 204. [See, Point, Refine: Multi-Turn Approach to GUI Grounding with Visual Feedback](https://arxiv.org/abs/2604.13019)

**<font color=#1a73e8>作者：</font>** Himangi Mittal, Gaurav Mittal, Nelson Daniel Troncoso 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer Use Agents (CUAs) fundamentally rely on graphical user interface (GUI) grounding to translate language instructions into executable screen actions, but editing-level grounding in dense coding interfaces, where sub-pixel accuracy is required to interact with dense IDE elements, remains underexplored. Existing approaches typically rely on single-shot coordinate prediction, which lacks a mechanism for error correction and often fails in high-density interfaces. In this technical report, we conduct an empirical study of pixel-precise cursor localization in coding environments. Instead of a single-step execution, our agent engages in an iterative refinement process, utilizing visual feedback from previous attempts to reach the target element. This closed-loop grounding mechanism allows the agent to self-correct displacement errors and adapt to dynamic UI changes. We evaluate our approach across GPT-5.4, Claude, and Qwen on a suite of complex coding benchmarks, demonstrating that multi-turn refinement significantly outperforms state-of-the-art single-shot models in both click precision and overall task success rate. Our results suggest that iterative visual reasoning is a critical component for the next generation of reliable software engineering agents. Code: this https URL.

---


### 205. [CLAD: Efficient Log Anomaly Detection Directly on Compressed Representations](https://arxiv.org/abs/2604.13024)

**<font color=#1a73e8>作者：</font>** Benzhao Tang, Shiyu Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The explosive growth of system logs makes streaming compression essential, yet existing log anomaly detection (LAD) methods incur severe pre-processing overhead by requiring full decompression and parsing. We introduce CLAD, the first deep learning framework to perform LAD directly on compressed byte streams. CLAD bypasses these bottlenecks by exploiting a key insight: normal logs compress into regular byte patterns, while anomalies systematically disrupt them. To extract these multi-scale deviations from opaque bytes, we propose a purpose-built architecture integrating a dilated convolutional byte encoder, a hybrid Transformer--mLSTM, and four-way aggregation pooling. This is coupled with a two-stage training strategy of masked pre-training and focal-contrastive fine-tuning to effectively handle severe class imbalance. Evaluated across five datasets, CLAD achieves a state-of-the-art average F1-score of 0.9909 and outperforms the best baseline by 2.72 percentage points. It delivers superior accuracy while completely eliminating decompression and parsing overheads, offering a robust solution that generalizes to structured streaming compressors.

---


### 206. [Conflated Inverse Modeling to Generate Diverse and Temperature-Change Inducing Urban Vegetation Patterns](https://arxiv.org/abs/2604.13028)

**<font color=#1a73e8>作者：</font>** Baris Sarper Tezcan, Hrishikesh Viswanath, Rubab Saher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban areas are increasingly vulnerable to thermal extremes driven by rapid urbanization and climate change. Traditionally, thermal extremes have been monitored using Earth-observing satellites and numerical modeling frameworks. For example, land surface temperature derived from Landsat or Sentinel imagery is commonly used to characterize surface heating patterns. These approaches operate as forward models, translating radiative observations or modeled boundary conditions into estimates of surface thermal states. While forward models can predict land surface temperature from vegetation and urban form, the inverse problem of determining spatial vegetation configurations that achieve a desired regional temperature shift remains largely unexplored. This task is inherently underdetermined, as multiple spatial vegetation patterns can yield similar aggregated temperature responses. Conventional regression and deterministic neural networks fail to capture this ambiguity and often produce averaged solutions, particularly under data-scarce conditions. We propose a conflated inverse modeling framework that combines a predictive forward model with a diffusion-based generative inverse model to produce diverse, physically plausible image-based vegetation patterns conditioned on specific temperature goals. Our framework maintains control over thermal outcomes while enabling diverse spatial vegetation configurations, even when such combinations are absent from training data. Altogether, this work introduces a controllable inverse modeling approach for urban climate adaptation that accounts for the inherent diversity of the problem. Code is available at the GitHub repository.

---


### 207. [Visual Preference Optimization with Rubric Rewards](https://arxiv.org/abs/2604.13029)

**<font color=#1a73e8>作者：</font>** Ya-Qi Yu, Fangyu Hong, Xiangyang Qu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The effectiveness of Direct Preference Optimization (DPO) depends on preference data that reflect the quality differences that matter in multimodal tasks. Existing pipelines often rely on off-policy perturbations or coarse outcome-based signals, which are not well suited to fine-grained visual reasoning. We propose rDPO, a preference optimization framework based on instance-specific rubrics. For each image-instruction pair, we create a checklist-style rubric of essential and additional criteria to score responses from any possible policies. The instruction-rubric pool is built offline and reused during the construction of on-policy data. On public reward modeling benchmarks, rubric-based prompting massively improves a 30B-A3B judge and brings it close to GPT-5.4. On public downstream benchmarks, rubric-based filtering raises the macro average to 82.69, whereas outcome-based filtering drops it to 75.82 from 81.14. When evaluating scalability on a comprehensive benchmark, rDPO achieves 61.01, markedly outperforming the style-constrained baseline (52.36) and surpassing the 59.48 base model. Together, these results show that visual preference optimization benefits from combining on-policy data construction with instance-specific criterion-level feedback.

---


### 208. [Generative Refinement Networks for Visual Synthesis](https://arxiv.org/abs/2604.13030)

**<font color=#1a73e8>作者：</font>** Jian Han, Jinlai Liu, Jiahuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While diffusion models dominate the field of visual generation, they are computationally inefficient, applying a uniform computational effort regardless of different complexity. In contrast, autoregressive (AR) models are inherently complexity-aware, as evidenced by their variable likelihoods, but are often hindered by lossy discrete tokenization and error accumulation. In this work, we introduce Generative Refinement Networks (GRN), a next-generation visual synthesis paradigm to address these issues. At its core, GRN addresses the discrete tokenization bottleneck through a theoretically near-lossless Hierarchical Binary Quantization (HBQ), achieving a reconstruction quality comparable to continuous counterparts. Built upon HBQ's latent space, GRN fundamentally upgrades AR generation with a global refinement mechanism that progressively perfects and corrects artworks -- like a human artist painting. Besides, GRN integrates an entropy-guided sampling strategy, enabling complexity-aware, adaptive-step generation without compromising visual quality. On the ImageNet benchmark, GRN establishes new records in image reconstruction (0.56 rFID) and class-conditional image generation (1.81 gFID). We also scale GRN to more challenging text-to-image and text-to-video generation, delivering superior performance on an equivalent scale. We release all models and code to foster further research on GRN.

---


### 209. [Lyra 2.0: Explorable Generative 3D Worlds](https://arxiv.org/abs/2604.13036)

**<font color=#1a73e8>作者：</font>** Tianchang Shen, Sherwin Bahmani, Kai He 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generation enable a new paradigm for 3D scene creation: generating camera-controlled videos that simulate scene walkthroughs, then lifting them to 3D via feed-forward reconstruction techniques. This generative reconstruction approach combines the visual fidelity and creative capacity of video models with 3D outputs ready for real-time rendering and simulation. Scaling to large, complex environments requires 3D-consistent video generation over long camera trajectories with large viewpoint changes and location revisits, a setting where current video models degrade quickly. Existing methods for long-horizon generation are fundamentally limited by two forms of degradation: spatial forgetting and temporal drifting. As exploration proceeds, previously observed regions fall outside the model's temporal context, forcing the model to hallucinate structures when revisited. Meanwhile, autoregressive generation accumulates small synthesis errors over time, gradually distorting scene appearance and geometry. We present Lyra 2.0, a framework for generating persistent, explorable 3D worlds at scale. To address spatial forgetting, we maintain per-frame 3D geometry and use it solely for information routing -- retrieving relevant past frames and establishing dense correspondences with the target viewpoints -- while relying on the generative prior for appearance synthesis. To address temporal drifting, we train with self-augmented histories that expose the model to its own degraded outputs, teaching it to correct drift rather than propagate it. Together, these enable substantially longer and 3D-consistent video trajectories, which we leverage to fine-tune feed-forward reconstruction models that reliably recover high-quality 3D scenes.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
