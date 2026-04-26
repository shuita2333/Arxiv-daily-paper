# 📦 其他研究 | 2026年04月27日

> 本类共 **231** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-231](./part-05.md)

---

### 151. [Finding Meaning in Embeddings: Concept Separation Curves](https://arxiv.org/abs/2604.21555)

**<font color=#1a73e8>作者：</font>** Paul Keuren, Marc Ponsen, Robert Ayoub Bagheri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentence embedding techniques aim to encode key concepts of a sentence's meaning in a vector space. However, the majority of evaluation approaches for sentence embedding quality rely on the use of additional classifiers or downstream tasks. These additional components make it unclear whether good results stem from the embedding itself or from the classifier's behaviour. In this paper, we propose a novel method for evaluating the effectiveness of sentence embedding methods in capturing sentence-level concepts. Our approach is classifier-independent, allowing for an objective assessment of the model's performance. The approach adopted in this study involves the systematic introduction of syntactic noise and semantic negations into sentences, with the subsequent quantification of their relative effects on the resulting embeddings. The visualisation of these effects is facilitated by Concept Separation Curves, which show the model's capacity to differentiate between conceptual and surface-level variations. By leveraging data from multiple domains, employing both Dutch and English languages, and examining sentence lengths, this study offers a compelling demonstration that Concept Separation Curves provide an interpretable, reproducible, and cross-model approach for evaluating the conceptual stability of sentence embeddings.

---


### 152. [Probabilistic Verification of Neural Networks via Efficient Probabilistic Hull Generation](https://arxiv.org/abs/2604.21556)

**<font color=#1a73e8>作者：</font>** Jingyang Li, Xin Chen, Hongfei Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The problem of probabilistic verification of a neural network investigates the probability of satisfying the safe constraints in the output space when the input is given by a probability distribution. It is significant to answer this problem when the input is affected by disturbances often modeled by probabilistic variables. In the paper, we propose a novel neural network probabilistic verification framework which computes a guaranteed range for the safe probability by efficiently finding safe and unsafe probabilistic hulls. Our approach consists of three main innovations: (1) a state space subdivision strategy using regression trees to produce probabilistic hulls, (2) a boundary-aware sampling method which identifies the safety boundary in the input space using samples that are later used for building regression trees, and (3) iterative refinement with probabilistic prioritization for computing a guaranteed range for the safe probability. The accuracy and efficiency of our approach are evaluated on various benchmarks including ACAS Xu and a rocket lander controller. The result shows an obvious advantage over the state of the art.

---


### 153. [Hybrid Deep Learning Approach for Coupled Demand Forecasting and Supply Chain Optimization](https://arxiv.org/abs/2604.21567)

**<font color=#1a73e8>作者：</font>** Nusrat Yasmin Nadia, Md Habibul Arif, Habibor Rahman Rabby 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supply chain resilience and efficiency are vital in industries characterized by volatile demand and uncertain supply, such as textiles and personal protective equipment (PPE). Traditional forecasting and optimization approaches often operate in isolation, limiting their real-world effectiveness. This paper proposes a Hybrid AI Framework for Demand-Supply Forecasting and Optimization (HAF-DS), which integrates a Long Short-Term Memory (LSTM)-based demand forecasting module with a mixed integer linear programming (MILP) optimization layer. The LSTM captures temporal and contextual demand dependencies, while the optimization layer prescribes cost-efficient replenishment and allocation decisions. The framework jointly minimizes forecasting error and operational cost through embedding-based feature representation and recurrent neural architectures. Experiments on textile sales and supply chain datasets show significant performance gains over statistical and deep learning baselines. On the combined dataset, HAF-DS reduced Mean Absolute Error (MAE) from 15.04 to 12.83 (14.7%), Root Mean Squared Error (RMSE) from 19.53 to 17.11 (12.4%), and Mean Absolute Percentage Error (MAPE) from 9.5% to 8.1%. Inventory cost decreased by 5.4%, stockouts by 27.5%, and service level rose from 95.5% to 97.8%. These results confirm that coupling predictive forecasting with prescriptive optimization enhances both accuracy and efficiency, providing a scalable and adaptable solution for modern textile and PPE supply chains.

---


### 154. [Deep kernel video approximation for unsupervised action segmentation](https://arxiv.org/abs/2604.21572)

**<font color=#1a73e8>作者：</font>** Silvia L. Pintea, Jouke Dijkstra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work focuses on per-video unsupervised action segmentation, which is of interest to applications where storing large datasets is either not possible, or nor permitted. We propose to segment videos by learning in deep kernel space, to approximate the underlying frame distribution, as closely as possible. To define this closeness metric between the original video distribution and its approximation, we rely on maximum mean discrepancy (MMD) which is a geometry-preserving metric in distribution space, and thus gives more reliable estimates. Moreover, unlike the commonly used optimal transport metric, MMD is both easier to optimize, and faster. We choose to use neural tangent kernels (NTKs) to define the kernel space where MMD operates, because of their improved descriptive power as opposed to fixed kernels. And, also, because NTKs sidestep the trivial solution, when jointly learning the inputs (video approximation) and the kernel function. Finally, we show competitive results when compared to state-of-the-art per-video methods, on six standard benchmarks. Additionally, our method has higher F1 scores than prior agglomerative work, when the number of segments is unknown.

---


### 155. [CHRep: Cross-modal Histology Representation and Post-hoc Calibration for Spatial Gene Expression Prediction](https://arxiv.org/abs/2604.21573)

**<font color=#1a73e8>作者：</font>** Changfan Wang, Xinran Wang, Donghai Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) enables spatially resolved gene profiling but remains expensive and low-throughput, limiting large-cohort studies and routine clinical use. Predicting spatial gene expression from routine hematoxylin and eosin (H&E) slides is a promising alternative, yet under realistic leave-one-slide-out evaluation, existing models often suffer from slide-level appearance shifts and regression-driven over-smoothing that suppress biologically meaningful variation. CHRep is a two-phase framework for robust histology-to-expression prediction. In the training phase, CHRep learns a structure-aware representation by jointly optimizing correlation-aware regression, symmetric image-expression alignment, and coordinate-induced spatial topology regularization. In the inference phase, cross-slide robustness is improved without backbone fine-tuning through a lightweight calibration module trained on the training slides, which combines a non-parametric estimate from a training gallery with a magnitude-regularized correction module. Unlike prior embedding-alignment or retrieval-based transfer methods that rely on a single prediction route, CHRep couples topology-preserving representation learning with post-hoc calibration, enabling stable neighborhood retrieval and controlled bias correction under slide-level shifts. Across the three cohorts, CHRep consistently improves gene-wise correlation under leave-one-slide-out evaluation, with the largest gains observed on Alex+10x. Relative to HAGE, the Pearson correlation coefficient on all considered genes [PCC(ACG)] increases by 4.0% on cSCC and 9.8% on HER2+. Relative to mclSTExp, PCC(ACG) further improves by 39.5% on Alex+10x, together with 9.7% and 9.0% reductions in mean squared error (MSE) and mean absolute error (MAE), respectively.

---


### 156. [OmniFit: Multi-modal 3D Body Fitting via Scale-agnostic Dense Landmark Prediction](https://arxiv.org/abs/2604.21575)

**<font color=#1a73e8>作者：</font>** Zeyu Cai, Yuliang Xiu, Renke Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fitting an underlying body model to 3D clothed human assets has been extensively studied, yet most approaches focus on either single-modal inputs such as point clouds or multi-view images alone, often requiring a known metric scale. This constraint is frequently impractical, especially for AI-generated assets where scale distortion is common. We propose OmniFit, a method that can seamlessly handle diverse multi-modal inputs, including full scans, partial depth observations, and image captures, while remaining scale-agnostic for both real and synthetic assets. Our key innovation is a simple yet effective conditional transformer decoder that directly maps surface points to dense body landmarks, which are then used for SMPL-X parameter fitting. In addition, an optional plug-and-play image adapter incorporates visual cues to compensate for missing geometric information. We further introduce a dedicated scale predictor that rescales subjects to canonical body proportions. OmniFit substantially outperforms state-of-the-art methods by 57.1 to 80.9 percent across daily and loose clothing scenarios. To the best of our knowledge, it is the first body fitting method to surpass multi-view optimization baselines and the first to achieve millimeter-level accuracy on the CAPE and 4D-DRESS benchmarks.

---


### 157. [Sculpt4D: Generating 4D Shapes via Sparse-Attention Diffusion Transformers](https://arxiv.org/abs/2604.21592)

**<font color=#1a73e8>作者：</font>** Minghao Yin, Wenbo Hu, Jiale Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent breakthroughs in 3D generative modeling have yielded remarkable progress in static shape synthesis, yet high-fidelity dynamic 4D generation remains elusive, hindered by temporal artifacts and prohibitive computational demand. We present Sculpt4D, a native 4D generative framework that seamlessly integrates efficient temporal modeling into a pretrained 3D Diffusion Transformer (Hunyuan3D 2.1), thereby mitigating the scarcity of 4D training data. At its core lies a Block Sparse Attention mechanism that preserves object identity by anchoring to the initial frame while capturing rich motion dynamics via a time-decaying sparse mask. This design faithfully models complex spatiotemporal dependencies with high fidelity, while sidestepping the quadratic overhead of full attention and reducing network total computation by 56%. Consequently, Sculpt4D establishes a new state-of-the-art in temporally coherent 4D synthesis and charts a path toward efficient and scalable 4D generation.

---


### 158. [Language as a Latent Variable for Reasoning Optimization](https://arxiv.org/abs/2604.21593)

**<font color=#1a73e8>作者：</font>** Linjuan Wu, Haoran Wei, Jialong Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs reduce English-centric bias, a surprising trend emerges: non-English responses sometimes outperform English on reasoning tasks. We hypothesize that language functions as a latent variable that structurally modulates the model's internal inference pathways, rather than merely serving as an output medium. To test this, we conducted a Polyglot Thinking Experiment, in which models were prompted to solve identical problems under language-constrained and language-unconstrained conditions. Results show that non-English responses often achieve higher accuracy, and the best performance frequently occur when language is unconstrained, suggesting that multilinguality broadens the model's latent reasoning space. Based on this insight, we propose polyGRPO (Polyglot Group Relative Policy Optimization), an RL framework that treats language variation as an implicit exploration signal. It generates polyglot preference data online under language-constrained and unconstrained conditions, optimizing the policy with respect to both answer accuracy and reasoning structure. Trained on only 18.1K multilingual math problems without chain-of-thought annotations, polyGRPO improves the base model (Qwen2.5-7B-Instruct) by 6.72% absolute accuracy on four English reasoning testset and 6.89% in their multilingual benchmark. Remarkably, it is the only method that surpasses the base LLM on English commonsense reasoning task (4.9%), despite being trained solely on math data-highlighting its strong cross-task generalization. Further analysis reveals that treating language as a latent variable expands the model's latent reasoning space, yielding consistent and generalizable improvements in reasoning performance.

---


### 159. [Mitigate or Fail: How Risk Management Shapes Cybersecurity Competency](https://arxiv.org/abs/2604.21604)

**<font color=#1a73e8>作者：</font>** Jeffrey T. Gardiner  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Contemporary cybersecurity governance assumes that professionals apply risk reasoning. Yet major organisational failures persist despite investment in tools, staffing, and credentials. This study investigates the structural source of that paradox. Cybersecurity speaks the language of risk, but its training architecture has shaped the profession to think in terms of threats. A sequential mixed-methods design integrated four analyses; NLP of the NIST NICE Framework v2.0.0 (2,111 TKS statements), SEM (n = 126 cybersecurity professionals), a control-group comparison (n = 133 general professionals), and thematic coding of seven leadership interviews. Four convergent findings emerged. First, "likelihood" and "probability" appear zero times across all TKS statements. Risk management content accounts for 4.5% of high-confidence semantic classifications, ranking 18th of 29 competency domains. NICE codifies threat-management activity while invoking risk mainly at the category level. Second, SEM showed that training exposure significantly predicts risk management competence directly and indirectly through conceptual salience, for a total effect of Beta = .629. However, the theoretically four-dimensional competence construct collapsed into a single factor, indicating epistemic compression. Third, cybersecurity professionals showed no measurable advantage over the general professional population in foundational risk reasoning; only 11.9% showed high differentiation. Fourth, all seven leaders expected Likelihood x Impact reasoning, yet five did not articulate the formula themselves. These findings support a structural conclusion: cybersecurity has taken professional form as a threat-management discipline that has borrowed risk vocabulary. Remediation requires redesign of professional formation, not marginal curriculum reform.

---


### 160. [Process-Mining of Hypertraces: Enabling Scalable Formal Security Verification of (Automotive) Network Architectures](https://arxiv.org/abs/2604.21606)

**<font color=#1a73e8>作者：</font>** Julius Figge, David Knuplesch, Andreas Maletti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The automotive domain is transitioning: vehicles act as rolling servers, persistently connected to numerous external entities. This connectivity, combined with rising on-board computing power for advanced driver assistance systems and similar use cases, creates escalating challenges for securing automotive network architectures. This work advances the security analysis of internet-connected automotive network architectures and their protocols. We introduce a strong, active adversary model tailored to the automotive domain. We substantially extend security protocol verification possible based on Attack Resilience Hyperproperties (ARHs) by introducing a verification-orchestration algorithm. Furthermore, we provide methods for comparative attribution of security property invalidations to specific, ne-grained component compromises. We present a novel integration of formal verification and process mining. By utilizing ARH counterexample traces for process mining, we systematically identify and aggregate attacker behavior that causes security property invalidations. This pipeline enables in-depth understanding of root causes and attack paths leading to protocol-security invalidations. We demonstrate real-world applicability through a prototype and case study on the secure transmission of battery management system data within an automotive network architecture.

---


### 161. [Local Neighborhood Instability in Parametric Projections: Quantitative and Visual Analysis](https://arxiv.org/abs/2604.21617)

**<font color=#1a73e8>作者：</font>** Frederik L. Dennig, Daniel A. Keim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parametric projections let analysts embed new points in real time, but input variations from measurement noise or data drift can produce unpredictable shifts in the 2D layout. Whether and where a projection is locally stable remains largely unexamined. In this paper, we present a stability evaluation framework that probes parametric projections with Gaussian perturbations around selected anchor points and assesses how neighborhoods deform in the 2D embedding. Our approach combines quantitative measures of mean displacement, bias, and nearest-anchor assignment error with per-anchor visualizations of displacement vectors, local PCA ellipsoids, and Voronoi misassignment for detailed inspection. We demonstrate the framework's effectiveness on UMAP- and t-SNE-based neural projectors of varying network sizes and study the effect of Jacobian regularization as a gradient-based robustness strategy. We apply our framework to the MNIST and Fashion-MNIST datasets. The results show that our framework identifies unstable projection regions invisible to reconstruction error or neighborhood-preservation metrics.

---


### 162. [A-THENA: Early Intrusion Detection for IoT with Time-Aware Hybrid Encoding and Network-Specific Augmentation](https://arxiv.org/abs/2604.21623)

**<font color=#1a73e8>作者：</font>** Ioannis Panopoulos, Maria Lamprini A. Bartsioka, Sokratis Nikolaidis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The proliferation of Internet of Things (IoT) devices has significantly expanded attack surfaces, making IoT ecosystems particularly susceptible to sophisticated cyber threats. To address this challenge, this work introduces A-THENA, a lightweight early intrusion detection system (EIDS) that significantly extends preliminary findings on time-aware encodings. A-THENA employs an advanced Transformer-based architecture augmented with a generalized Time-Aware Hybrid Encoding (THE), integrating packet timestamps to effectively capture temporal dynamics essential for accurate and early threat detection. The proposed system further employs a Network-Specific Augmentation (NA) pipeline, which enhances model robustness and generalization. We evaluate A-THENA on three benchmark IoT intrusion detection datasets-CICIoT23-WEB, MQTT-IoT-IDS2020, and IoTID20-where it consistently achieves strong performance. Averaged across all three datasets, it improves accuracy by 6.88 percentage points over the best-performing traditional positional encoding, 3.69 points over the strongest feature-based model, 6.17 points over the leading time-aware alternatives, and 5.11 points over related models, while achieving near-zero false alarms and false negatives. To assess real-world feasibility, we deploy A-THENA on the Raspberry Pi Zero 2 W, demonstrating its ability to perform real-time intrusion detection with minimal latency and memory usage. These results establish A-THENA as an agile, practical, and highly effective solution for securing IoT networks.

---


### 163. [On the Challenges of Holistic Intrusion Detection in ICS](https://arxiv.org/abs/2604.21626)

**<font color=#1a73e8>作者：</font>** Stefan Lenz, Julia Raab, Benedikt Holzbach 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Past attacks against industrial control systems (ICS) show that adversaries often target both the ICS network and the physical process to achieve potential catastrophic impact. To secure ICS, intrusion detection systems promise timely uncovering of such adversaries. However, as these detection mechanisms typically focus on isolated characteristics of ICS (e.g., packet timings), multiple detection systems have to be deployed in parallel, complicating their operation in practice. In this work, to spur discussion and further research, we present challenges encountered during our research towards a holistic intrusion detection system aiming to cover all dimensions of an ICS.

---


### 164. [DCMorph: Face Morphing via Dual-Stream Cross-Attention Diffusion](https://arxiv.org/abs/2604.21627)

**<font color=#1a73e8>作者：</font>** Tahar Chettaoui, Eduarda Caldeira, Guray Ozgur 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advancing face morphing attack techniques is crucial to anticipate evolving threats and develop robust defensive mechanisms for identity verification systems. This work introduces DCMorph, a dual-stream diffusion-based morphing framework that simultaneously operates at both identity conditioning and latent space levels. Unlike image-level methods suffering from blending artifacts or GAN-based approaches with limited reconstruction fidelity, DCMorph leverages identity-conditioned latent diffusion models through two mechanisms: (1) decoupled cross-attention interpolation that injects identity-specific features from both source faces into the denoising process, enabling explicit dual-identity conditioning absent in existing diffusion-based methods, and (2) DDIM inversion with spherical interpolation between inverted latent representations from both source faces, providing geometrically consistent initial latent representation that preserves structural attributes. Vulnerability analyses across four state-of-the-art face recognition systems demonstrate that DCMorph achieves the highest attack success rates compared to existing methods at both operational thresholds, while remaining challenging to detect by current morphing attack detection solutions.

---


### 165. [Promoting Simple Agents: Ensemble Methods for Event-Log Prediction](https://arxiv.org/abs/2604.21629)

**<font color=#1a73e8>作者：</font>** Benedikt Bollig, Matthias Függer, Thomas Nowak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We compare lightweight automata-based models (n-grams) with neural architectures (LSTM, Transformer) for next-activity prediction in streaming event logs. Experiments on synthetic patterns and five real-world process mining datasets show that n-grams with appropriate context windows achieve comparable accuracy to neural models while requiring substantially fewer resources. Unlike windowed neural architectures, which show unstable performance patterns, n-grams provide stable and consistent accuracy. While we demonstrate that classical ensemble methods like voting improve n-gram performance, they require running many agents in parallel during inference, increasing memory consumption and latency. We propose an ensemble method, the promotion algorithm, that dynamically selects between two active models during inference, reducing overhead compared to classical voting schemes. On real-world datasets, these ensembles match or exceed the accuracy of non-windowed neural models with lower computational cost.

---


### 166. [DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures](https://arxiv.org/abs/2604.21631)

**<font color=#1a73e8>作者：</font>** Xu Wang, Zhiru Wang, Shiyun Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Gaussian Splatting (3DGS) achieves real-time photorealistic rendering, its performance degrades significantly when training images contain transient objects that violate multi-view consistency. Existing methods face a circular dependency: accurate transient detection requires a well-reconstructed static scene, while clean reconstruction itself depends on reliable transient masks. We address this challenge with DualSplat, a Failure-to-Prior framework that converts first-pass reconstruction failures into explicit priors for a second reconstruction stage. We observe that transients, which appear in only a subset of views, often manifest as incomplete fragments during conservative initial training. We exploit these failures to construct object-level pseudo-masks by combining photometric residuals, feature mismatches, and SAM2 instance boundaries. These pseudo-masks then guide a clean second-pass 3DGS optimization, while a lightweight MLP refines them online by gradually shifting from prior supervision to self-consistency. Experiments on RobustNeRF and NeRF On-the-go show that DualSplat outperforms existing baselines, demonstrating particularly clear advantages in transient-heavy scenes and transient regions.

---


### 167. [To See the Unseen: on the Generalization Ability of Transformers in Symbolic Reasoning](https://arxiv.org/abs/2604.21632)

**<font color=#1a73e8>作者：</font>** Nevena Lazić, Liam Fowl, András György 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate the ability of decoder-only transformer models to perform abstract symbolic reasoning; specifically solving propositional logic reasoning problems given in-context. Previous work demonstrated that models fail to generalize to problems involving variable names that were not observed during training, and it was shown that one reason behind this is the difficulty of copying (or generating) unseen tokens. We show both theoretically and empirically that a particular representational collapse also has a crucial role: the unembeddings (last-layer weights) of unseen tokens collapse to nearly the same vector during training. The collapse makes distinguishing multiple unseen variables difficult for the model (especially when the embedding and unembedding parameters are shared), and provides a mechanistic explanation for the effectiveness of existing heuristic interventions like "active forgetting", which periodically reset the token (un)embeddings. Based on these observations, we devise a combination of techniques, involving a small architecture change facilitating copying, data diversity, and freezing or resetting (un)embeddings, that achieves generalization to unseen tokens. We support our claims with extensive controlled experiments on propositional logic reasoning problems. Beyond synthetic experiments, we also observe evidence of (un)embedding collapse in the open-weight models in the Gemma 3 family, which includes 99 unused tokens reserved for downstream use. Empirically we find that the correlated embeddings of these tokens are a poor initialization for finetuning applications.

---


### 168. [Geometric Characterisation and Structured Trajectory Surrogates for Clinical Dataset Condensation](https://arxiv.org/abs/2604.21638)

**<font color=#1a73e8>作者：</font>** Pafue Christy Nganjimi, Andrew Soltan, Danielle Belgrave 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dataset condensation constructs compact synthetic datasets that retain the training utility of large real-world datasets, enabling efficient model development and potentially supporting downstream research in governed domains such as healthcare. Trajectory matching (TM) is a widely used condensation approach that supervises synthetic data using changes in model parameters observed during training on real data, yet the structure of this supervision signal remains poorly understood. In this paper, we provide a geometric characterisation of trajectory matching, showing that a fixed synthetic dataset can only reproduce a limited span of such training-induced parameter changes. When the resulting supervision signal is spectrally broad, this creates a conditional representability bottleneck. Motivated by this mismatch, we propose Bezier Trajectory Matching (BTM), which replaces SGD trajectories with quadratic Bezier trajectory surrogates between initial and final model states. These surrogates are optimised to reduce average loss along the path while replacing broad SGD-derived supervision with a more structured, lower-rank signal that is better aligned with the optimisation constraints of a fixed synthetic dataset, and they substantially reduce trajectory storage. Experiments on five clinical datasets demonstrate that BTM consistently matches or improves upon standard trajectory matching, with the largest gains in low-prevalence and low-synthetic-budget settings. These results indicate that effective trajectory matching depends on structuring the supervision signal rather than reproducing stochastic optimisation paths.

---


### 169. [Task-specific Subnetwork Discovery in Reinforcement Learning for Autonomous Underwater Navigation](https://arxiv.org/abs/2604.21640)

**<font color=#1a73e8>作者：</font>** Yi-Ling Liu, Melvin Laux, Mariela De Lucas Alvarez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous underwater vehicles are required to perform multiple tasks adaptively and in an explainable manner under dynamic, uncertain conditions and limited sensing, challenges that classical controllers struggle to address. This demands robust, generalizable, and inherently interpretable control policies for reliable long-term monitoring. Reinforcement learning, particularly multi-task RL, overcomes these limitations by leveraging shared representations to enable efficient adaptation across tasks and environments. However, while such policies show promising results in simulation and controlled experiments, they yet remain opaque and offer limited insight into the agent's internal decision-making, creating gaps in transparency, trust, and safety that hinder real-world deployment. The internal policy structure and task-specific specialization remain poorly understood. To address these gaps, we analyze the internal structure of a pretrained multi-task reinforcement learning network in the HoloOcean simulator for underwater navigation by identifying and comparing task-specific subnetworks responsible for navigating toward different species. We find that in a contextual multi-task reinforcement learning setting with related tasks, the network uses only about 1.5% of its weights to differentiate between tasks. Of these, approximately 85% connect the context-variable nodes in the input layer to the next hidden layer, highlighting the importance of context variables in such settings. Our approach provides insights into shared and specialized network components, useful for efficient model editing, transfer learning, and continual learning for underwater monitoring through a contextual multi-task reinforcement learning method.

---


### 170. [Large-Scale Data Parallelization of Product Quantization and Inverted Indexing Using Dask](https://arxiv.org/abs/2604.21645)

**<font color=#1a73e8>作者：</font>** Ashley N. Abraham, Andrew Strelzoff, Haley R. Dozier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale Nearest Neighbor (NN) search, though widely utilized in the similarity search field, remains challenged by the computational limitations inherent in processing large scale data. In an effort to decrease the computational expense needed, Approximate Nearest Neighbor (ANN) search is often used in applications that do not require the exact similarity search, but instead can rely on an approximation. Product Quantization (PQ) is a memory-efficient ANN effective for clustering all sizes of datasets. Clustering large-scale, high dimensional data requires a heavy computational expense, in both memory-cost and execution time. This work focuses on a unique way to divide and conquer the large scale data in Python using PQ, Inverted Indexing and Dask, combining the results without compromising the accuracy and reducing computational requirements to the level required when using medium-scale data.

---


### 171. [GS-Quant: Granular Semantic and Generative Structural Quantization for Knowledge Graph Completion](https://arxiv.org/abs/2604.21649)

**<font color=#1a73e8>作者：</font>** Qizhuo Xie, Yunhui Liu, Yu Xing 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown immense potential in Knowledge Graph Completion (KGC), yet bridging the modality gap between continuous graph embeddings and discrete LLM tokens remains a critical challenge. While recent quantization-based approaches attempt to align these modalities, they typically treat quantization as flat numerical compression, resulting in semantically entangled codes that fail to mirror the hierarchical nature of human reasoning. In this paper, we propose GS-Quant, a novel framework that generates semantically coherent and structurally stratified discrete codes for KG entities. Unlike prior methods, GS-Quant is grounded in the insight that entity representations should follow a linguistic coarse-to-fine logic. We introduce a Granular Semantic Enhancement module that injects hierarchical knowledge into the codebook, ensuring that earlier codes capture global semantic categories while later codes refine specific attributes. Furthermore, a Generative Structural Reconstruction module imposes causal dependencies on the code sequence, transforming independent discrete units into structured semantic descriptors. By expanding the LLM vocabulary with these learned codes, we enable the model to reason over graph structures isomorphically to natural language generation. Experimental results demonstrate that GS-Quant significantly outperforms existing text-based and embedding-based baselines. Our code is publicly available at this https URL.

---


### 172. [Dilated CNNs for Periodic Signal Processing: A Low-Complexity Approach](https://arxiv.org/abs/2604.21651)

**<font color=#1a73e8>作者：</font>** Eli Gildish, Michael Grebshtein, Igor Makienko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Denoising of periodic signals and accurate waveform estimation are core tasks across many signal processing domains, including speech, music, medical diagnostics, radio, and sonar. Although deep learning methods have recently shown performance improvements over classical approaches, they require substantial computational resources and are usually trained separately for each signal observation. This study proposes a computationally efficient method based on DCNN and Re-sampling, termed R-DCNN, designed for operation under strict power and resource constraints. The approach targets signals with varying fundamental frequencies and requires only a single observation for training. It generalizes to additional signals via a lightweight resampling step that aligns time scales in signals with different frequencies to re-use the same network weights. Despite its low computational complexity, R-DCNN achieves performance comparable to state-of-the-art classical methods, such as autoregressive (AR)-based techniques, as well as conventional DCNNs trained individually for each observation. This combination of efficiency and performance makes the proposed method particularly well suited for deployment in resource-constrained environments without sacrificing denoising or estimation accuracy.

---


### 173. [Causal Disentanglement for Full-Reference Image Quality Assessment](https://arxiv.org/abs/2604.21654)

**<font color=#1a73e8>作者：</font>** Zhen Zhang, Jielei Chu, Tian Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing deep network-based full-reference image quality assessment (FR-IQA) models typically work by performing pairwise comparisons of deep features from the reference and distorted images. In this paper, we approach this problem from a different perspective and propose a novel FR-IQA paradigm based on causal inference and decoupled representation learning. Unlike typical feature comparison-based FR-IQA models, our approach formulates degradation estimation as a causal disentanglement process guided by intervention on latent representations. We first decouple degradation and content representations by exploiting the content invariance between the reference and distorted images. Second, inspired by the human visual masking effect, we design a masking module to model the causal relationship between image content and degradation features, thereby extracting content-influenced degradation features from distorted images. Finally, quality scores are predicted from these degradation features using either supervised regression or label-free dimensionality reduction. Extensive experiments demonstrate that our method achieves highly competitive performance on standard IQA benchmarks across fully supervised, few-label, and label-free settings. Furthermore, we evaluate the approach on diverse non-standard natural image domains with scarce data, including underwater, radiographic, medical, neutron, and screen-content images. Benefiting from its ability to perform scenario-specific training and prediction without labeled IQA data, our method exhibits superior cross-domain generalization compared to existing training-free FR-IQA models.

---


### 174. [Transferable SCF-Acceleration through Solver-Aligned Initialization Learning](https://arxiv.org/abs/2604.21657)

**<font color=#1a73e8>作者：</font>** Eike S. Eberhard, Viktor Kotsev, Timm Güthle 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning methods that predict initial guesses from molecular geometry can reduce this cost, but matrix-prediction models fail when extrapolating to larger molecules, degrading rather than accelerating convergence [Liu et al. 2025]. We show that this failure is a supervision problem, not an extrapolation problem: models trained on ground-state targets fit those targets well out of distribution, yet produce initial guesses that slow convergence. Solver-Aligned Initialization Learning (SAIL) resolves this for both Hamiltonian and density matrix models by differentiating through the SCF solver end-to-end. We introduce the Effective Relative Iteration Count (ERIC), a correction to the commonly used RIC that accounts for hidden Fock-build overhead. On QM40, containing molecules up to 4$\times$ larger than the training distribution, SAIL reduces ERIC by 37% (PBE), 33% (SCAN), and 27% (B3LYP), more than doubling the previous state-of-the-art reduction on B3LYP (10%). On QMugs molecules 10$\times$ the training size, SAIL delivers a 1.25$\times$ wall-time speedup at the hybrid level of theory, extending ML SCF acceleration to large drug-like molecules.

---


### 175. [Fine-Grained Perspectives: Modeling Explanations with Annotator-Specific Rationales](https://arxiv.org/abs/2604.21667)

**<font color=#1a73e8>作者：</font>** Olufunke O. Sarumi, Charles Welch, Daniel Braun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Beyond exploring disaggregated labels for modeling perspectives, annotator rationales provide fine-grained signals of individual perspectives. In this work, we propose a framework for jointly modeling annotator-specific label prediction and corresponding explanations, fine-tuned on the annotators' provided rationales. Using a dataset with disaggregated natural language inference (NLI) annotations and annotator-provided explanations, we condition predictions on both annotator identity and demographic metadata through a representation-level User Passport mechanism. We further introduce two explainer architectures: a post-hoc prompt-based explainer and a prefixed bridge explainer that transfers annotator-conditioned classifier representations directly into a generative model. This design enables explanation generation aligned with individual annotator perspectives. Our results show that incorporating explanation modeling substantially improves predictive performance over a baseline annotator-aware classifier, with the prefixed bridge approach achieving more stable label alignment and higher semantic consistency, while the post-hoc approach yields stronger lexical similarity. These findings indicate that modeling explanations as expressions of fine-grained perspective provides a richer and more faithful representation of disagreement. The proposed approaches advance perspectivist modeling by integrating annotator-specific rationales into both predictive and generative components.

---


### 176. [Geometric Monomial (GEM): a family of rational 2N-differentiable activation functions](https://arxiv.org/abs/2604.21677)

**<font color=#1a73e8>作者：</font>** Eylon E. Krause  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The choice of activation function plays a crucial role in the optimization and performance of deep neural networks. While the Rectified Linear Unit (ReLU) remains the dominant choice due to its simplicity and effectiveness, its lack of smoothness may hinder gradient-based optimization in deep architectures. In this work we propose a family of $C^{2N}$-smooth activation functions whose gate follows a log-logistic CDF, achieving ReLU-like performance with purely rational arithmetic. We introduce three variants: GEM (the base family), E-GEM (an $\epsilon$-parameterized generalization enabling arbitrary $L^p$-approximation of ReLU), and SE-GEM (a piecewise variant eliminating dead neurons with $C^{2N}$ junction smoothness). An $N$-ablation study establishes $N=1$ as optimal for standard-depth networks, reducing the GELU deficit on CIFAR-100 + ResNet-56 from 6.10% to 2.12%. The smoothness parameter $N$ further reveals a CNN-transformer tradeoff: $N=1$ is preferred for deep CNNs, while $N=2$ is preferred for transformers. On MNIST, E-GEM ties the best baseline (99.23%). On CIFAR-10 + ResNet-56, SE-GEM ($\epsilon=10^{-4}$) surpasses GELU (92.51% vs 92.44%) -- the first GEM-family activation to outperform GELU. On CIFAR-100 + ResNet-56, E-GEM reduces the GELU deficit from 6.10% (GEM $N=2$) to just 0.62%. On GPT-2 (124M), GEM achieves the lowest perplexity (72.57 vs 73.76 for GELU), with GEM $N=1$ also beating GELU (73.32). On BERT-small, E-GEM ($\epsilon=10$) achieves the best validation loss (6.656) across all activations. The $\epsilon$-parameterization reveals a scale-dependent optimum: small $\epsilon$ ($10^{-4}$--$10^{-6}$) for deep CNNs and larger transformers, with the special case of small transformers (BERT-small) benefiting from large $\epsilon$ ($\epsilon=10$) due to its limited depth and unconstrained gradients.

---


### 177. [Sapiens2](https://arxiv.org/abs/2604.21681)

**<font color=#1a73e8>作者：</font>** Rawal Khirodkar, He Wen, Julieta Martinez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Sapiens2, a model family of high-resolution transformers for human-centric vision focused on generalization, versatility, and high-fidelity outputs. Our model sizes range from 0.4 to 5 billion parameters, with native 1K resolution and hierarchical variants that support 4K. Sapiens2 substantially improves over its predecessor in both pretraining and post-training. First, to learn features that capture low-level details (for dense prediction) and high-level semantics (for zero-shot or few-label settings), we combine masked image reconstruction with self-distilled contrastive objectives. Our evaluations show that this unified pretraining objective is better suited for a wider range of downstream tasks. Second, along the data axis, we pretrain on a curated dataset of 1 billion high-quality human images and improve the quality and quantity of task annotations. Third, architecturally, we incorporate advances from frontier models that enable longer training schedules with improved stability. Our 4K models adopt windowed attention to reason over longer spatial context and are pretrained with 2K output resolution. Sapiens2 sets a new state-of-the-art and improves over the first generation on pose (+4 mAP), body-part segmentation (+24.3 mIoU), normal estimation (45.6% lower angular error) and extends to new tasks such as pointmap and albedo estimation. Code: this https URL

---


### 178. [Efficient Logic Gate Networks for Video Copy Detection](https://arxiv.org/abs/2604.21694)

**<font color=#1a73e8>作者：</font>** Katarzyna Fojcik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video copy detection requires robust similarity estimation under diverse visual distortions while operating at very large scale. Although deep neural networks achieve strong performance, their computational cost and descriptor size limit practical deployment in high-throughput systems. In this work, we propose a video copy detection framework based on differentiable Logic Gate Networks (LGNs), which replace conventional floating-point feature extractors with compact, logic-based representations. Our approach combines aggressive frame miniaturization, binary preprocessing, and a trainable LGN embedding model that learns both logical operations and interconnections. After training, the model can be discretized into a purely Boolean circuit, enabling extremely fast and memory-efficient inference. We systematically evaluate different similarity strategies, binarization schemes, and LGN architectures across multiple dataset folds and difficulty levels. Experimental results demonstrate that LGN-based models achieve competitive or superior accuracy and ranking performance compared to prior models, while producing descriptors several orders of magnitude smaller and delivering inference speeds exceeding 11k samples per second. These findings indicate that logic-based models offer a promising alternative for scalable and resource-efficient video copy detection.

---


### 179. [Towards Universal Tabular Embeddings: A Benchmark Across Data Tasks](https://arxiv.org/abs/2604.21696)

**<font color=#1a73e8>作者：</font>** Liane Vogel, Kavitha Srinivas, Niharika D'Souza 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models aim to learn universal representations of tabular data that transfer across tasks and domains, enabling applications such as table retrieval, semantic search and table-based prediction. Despite the growing number of such models, it remains unclear which approach works best in practice, as existing methods are often evaluated under task-specific settings that make direct comparison difficult. To address this, we introduce TEmBed, the Tabular Embedding Test Bed, a comprehensive benchmark for systematically evaluating tabular embeddings across four representation levels: cell, row, column, and table. Evaluating a diverse set of tabular representation learning models, we show that which model to use depends on the task and representation level. Our results offer practical guidance for selecting tabular embeddings in real-world applications and lay the groundwork for developing more general-purpose tabular representation models.

---


### 180. [Fixation Sequences as Time Series: A Topological Approach to Dyslexia Detection](https://arxiv.org/abs/2604.21698)

**<font color=#1a73e8>作者：</font>** Marius Huber, David R. Reich, Lena A. Jäger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persistent homology, a method from topological data analysis, extracts robust, multi-scale features from data. It produces stable representations of time series by applying varying thresholds to their values (a process known as a \textit{filtration}). We develop novel filtrations for time series and introduce topological methods for the analysis of eye-tracking data, by interpreting fixation sequences as time series, and constructing ``hybrid models'' that combine topological features with traditional statistical features. We empirically evaluate our method by applying it to the task of dyslexia detection from eye-tracking-while-reading data using the Copenhagen Corpus, which contains scanpaths from dyslexic and non-dyslexic L1 and L2 readers. Our hybrid models outperform existing approaches that rely solely on traditional features, showing that persistent homology captures complementary information encoded in fixation sequences. The strength of these topological features is further underscored by their achieving performance comparable to established baseline methods. Importantly, our proposed filtrations outperform existing ones.

---


### 181. [Phonological Subspace Collapse Is Aetiology-Specific and Cross-Lingually Stable: Evidence from 3,374 Speakers](https://arxiv.org/abs/2604.21706)

**<font color=#1a73e8>作者：</font>** Bernard Muller, Antonio Armando Ortiz Barrañón, LaVonne Roberts  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We previously introduced a training-free method for dysarthria severity assessment based on d-prime separability of phonological feature subspaces in frozen self-supervised speech representations, validated on 890 speakers across 5 languages with HuBERT-base. Here, we scale the analysis to 3,374 speakers from 25 datasets spanning 12 languages and 5 aetiologies (Parkinson's disease, cerebral palsy, ALS, Down syndrome, and stroke), plus healthy controls, using 6 SSL backbones. We report three findings. First, aetiology-specific degradation profiles are distinguishable at the group level: 10 of 13 features yield large effect sizes (epsilon-squared > 0.14, Holm-corrected p < 0.001), with Parkinson's disease separable from the articulatory execution group at Cohen's d = 0.83; individual-level classification remains limited (22.6% macro F1). Second, profiles show cross-lingual profile-shape stability: cosine similarity of 5-dimensional consonant d-prime profiles exceeds 0.95 across the languages available for each aetiology. Absolute d-prime magnitudes are not cross-lingually calibrated, so the method supports language-independent phenotyping of degradation patterns but requires within-corpus calibration for absolute severity interpretation. Third, the method is architecture-independent: all 6 backbones produce monotonic severity gradients with inter-model agreement exceeding rho = 0.77. Fixed-token d-prime estimation preserves the severity correlation (rho = -0.733 at 200 tokens per class), confirming that the signal is not a token-count artefact. These results support phonological subspace analysis as a robust, training-free framework for aetiology-aware dysarthria characterisation, with evidence of cross-lingual profile-shape stability and cross-backbone robustness in the represented sample.

---


### 182. [Fairness under uncertainty in sequential decisions](https://arxiv.org/abs/2604.21711)

**<font color=#1a73e8>作者：</font>** Michelle Seng Ah Lee, Kirtan Padh, David Watson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fair machine learning (ML) methods help identify and mitigate the risk that algorithms encode or automate social injustices. Algorithmic approaches alone cannot resolve structural inequalities, but they can support socio-technical decision systems by surfacing discriminatory biases, clarifying trade-offs, and enabling governance. Although fairness is well studied in supervised learning, many real ML applications are online and sequential, with prior decisions informing future ones. Each decision is taken under uncertainty due to unobserved counterfactuals and finite samples, with dire consequences for under-represented groups, systematically under-observed due to historical exclusion and selective feedback. A bank cannot know whether a denied loan would have been repaid, and may have less data on marginalized populations.
This paper introduces a taxonomy of uncertainty in sequential decision-making -- model, feedback, and prediction uncertainty -- providing shared vocabulary for assessing systems where uncertainty is unevenly distributed across groups. We formalize model and feedback uncertainty via counterfactual logic and reinforcement learning, and illustrate harms to decision makers (unrealized gains/losses) and subjects (compounding exclusion, reduced access) of policies that ignore the unobserved space. Algorithmic examples show it is possible to reduce outcome variance for disadvantaged groups while preserving institutional objectives (e.g. expected utility). Experiments on data simulated with varying bias show how unequal uncertainty and selective feedback produce disparities, and how uncertainty-aware exploration alters fairness metrics. The framework equips practitioners to diagnose, audit, and govern fairness risks. Where uncertainty drives unfairness rather than incidental noise, accounting for it is essential to fair and effective decision-making.

---


### 183. [Discriminative-Generative Synergy for Occlusion Robust 3D Human Mesh Recovery](https://arxiv.org/abs/2604.21712)

**<font color=#1a73e8>作者：</font>** Yang Liu, Zhiyong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D human mesh recovery from monocular RGB images aims to estimate anatomically plausible 3D human models for downstream applications, but remains challenging under partial or severe occlusions. Regression-based methods are efficient yet often produce implausible or inaccurate results in unconstrained scenarios, while diffusion-based methods provide strong generative priors for occluded regions but may weaken fidelity to rare poses due to over-reliance on generation. To address these limitations, we propose a brain-inspired synergistic framework that integrates the discriminative power of vision transformers with the generative capability of conditional diffusion models. Specifically, the ViT-based pathway extracts deterministic visual cues from visible regions, while the diffusion-based pathway synthesizes structurally coherent human body representations. To effectively bridge the two pathways, we design a diverse-consistent feature learning module to align discriminative features with generative priors, and a cross-attention multi-level fusion mechanism to enable bidirectional interaction across semantic levels. Experiments on standard benchmarks demonstrate that our method achieves superior performance on key metrics and shows strong robustness in complex real-world scenarios.

---


### 184. [Unlocking the Power of Critical Factors for 3D Visual Geometry Estimation](https://arxiv.org/abs/2604.21713)

**<font color=#1a73e8>作者：</font>** Guangkai Xu, Hua Geng, Huanyi Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward visual geometry estimation has recently made rapid progress. However, an important gap remains: multi-frame models usually produce better cross-frame consistency, yet they often underperform strong per-frame methods on single-frame accuracy. This observation motivates our systematic investigation into the critical factors driving model performance through rigorous ablation studies, which reveals several key insights: 1) Scaling up data diversity and quality unlocks further performance gains even in state-of-the-art visual geometry estimation methods; 2) Commonly adopted confidence-aware loss and gradient-based loss mechanisms may unintentionally hinder performance; 3) Joint supervision through both per-sequence and per-frame alignment improves results, while local region alignment surprisingly degrades performance. Furthermore, we introduce two enhancements to integrate the advantages of optimization-based methods and high-resolution inputs: a consistency loss function that enforces alignment between depth maps, camera parameters, and point maps, and an efficient architectural design that leverages high-resolution information. We integrate these designs into CARVE, a resolution-enhanced model for feed-forward visual geometry estimation. Experiments on point cloud reconstruction, video depth estimation, and camera pose/intrinsic estimation show that CARVE achieves strong and robust performance across diverse benchmarks.

---


### 185. [From If-Statements to ML Pipelines: Revisiting Bias in Code-Generation](https://arxiv.org/abs/2604.21716)

**<font color=#1a73e8>作者：</font>** Minh Duc Bui, Xenia Heilmann, Mattia Cerrato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work evaluates code generation bias primarily through simple conditional statements, which represent only a narrow slice of real-world programming and reveal solely overt, explicitly encoded bias. We demonstrate that this approach dramatically underestimates bias in practice by examining a more realistic task: generating machine learning (ML) pipelines. Testing both code-specialized and general-instruction large language models, we find that generated pipelines exhibit significant bias during feature selection. Sensitive attributes appear in 87.7% of cases on average, despite models demonstrably excluding irrelevant features (e.g., including "race" while dropping "favorite color" for credit scoring). This bias is substantially more prevalent than that captured by conditional statements, where sensitive attributes appear in only 59.2% of cases. These findings are robust across prompt mitigation strategies, varying numbers of attributes, and different pipeline difficulty levels. Our results challenge simple conditionals as valid proxies for bias evaluation and suggest current benchmarks underestimate bias risk in practical deployments.

---


### 186. [Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling](https://arxiv.org/abs/2604.21724)

**<font color=#1a73e8>作者：</font>** Yilong Chen, Yanxi Xie, Zitian Gao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large token-indexed lookup tables provide a compute-decoupled scaling path, but their practical gains are often limited by poor parameter efficiency and rapid memory growth. We attribute these limitations to Zipfian under-training of the long tail, heterogeneous demand across layers, and "slot collapse" that produces redundant embeddings. To address this, we propose X-GRAM, a frequency-aware dynamic token-injection framework. X-GRAM employs hybrid hashing and alias mixing to compress the tail while preserving head capacity, and refines retrieved vectors via normalized SwiGLU ShortConv to extract diverse local n-gram features. These signals are integrated into attention value streams and inter-layer residuals using depth-aware gating, effectively aligning static memory with dynamic context. This design introduces a memory-centric scaling axis that decouples model capacity from FLOPs. Extensive evaluations at the 0.73B and 1.15B scales show that X-GRAM improves average accuracy by as much as 4.4 points over the vanilla backbone and 3.2 points over strong retrieval baselines, while using substantially smaller tables in the 50% configuration. Overall, by decoupling capacity from compute through efficient memory management, X-GRAM offers a scalable and practical paradigm for future memory-augmented architectures. Code aviliable in this https URL.

---


### 187. [AEL: Agent Evolving Learning for Open-Ended Environments](https://arxiv.org/abs/2604.21725)

**<font color=#1a73e8>作者：</font>** Wujiang Xu, Jiaojiao Han, Minghao Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly operate in open-ended environments spanning hundreds of sequential episodes, yet they remain largely stateless: each task is solved from scratch without converting past experience into better future behavior. The central obstacle is not \emph{what} to remember but \emph{how to use} what has been remembered, including which retrieval policy to apply, how to interpret prior outcomes, and when the current strategy itself must change. We introduce \emph{Agent Evolving Learning} (\ael{}), a two-timescale framework that addresses this obstacle. At the fast timescale, a Thompson Sampling bandit learns which memory retrieval policy to apply at each episode; at the slow timescale, LLM-driven reflection diagnoses failure patterns and injects causal insights into the agent's decision prompt, giving it an interpretive frame for the evidence it retrieves. On a sequential portfolio benchmark (10 sector-diverse tickers, 208 episodes, 5 random seeds), \ael{} achieves a Sharpe ratio of 2.13$\pm$0.47, outperforming five published self-improving methods and all non-LLM baselines while maintaining the lowest variance among all LLM-based approaches. A nine-variant ablation reveals a ``less is more'' pattern: memory and reflection together produce a 58\% cumulative improvement over the stateless baseline, yet every additional mechanism we test (planner evolution, per-tool selection, cold-start initialization, skill extraction, and three credit assignment methods) \emph{degrades} performance. This demonstrates that the bottleneck in agent self-improvement is \emph{self-diagnosing how to use} experience rather than adding architectural complexity. Code and data: this https URL.

---


### 188. [Enabling and Inhibitory Pathways of University Students' Willingness to Disclose AI Use: A Cognition-Affect-Conation Perspective](https://arxiv.org/abs/2604.21733)

**<font color=#1a73e8>作者：</font>** Yiran Du, Huimin He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The increasing integration of artificial intelligence (AI) in higher education has raised important questions regarding students' transparency in reporting AI-assisted work. This study investigates the psychological mechanisms underlying university students' willingness to disclose AI use by applying the Cognition--Affect--Conation (CAC) framework. A sequential explanatory mixed-methods design was employed. In the quantitative phase, survey data were collected from 546 university students and analysed using structural equation modelling to examine the relationships among cognitive perceptions, affective responses, and disclosure intention. In the qualitative phase, semi-structured interviews with 22 students were conducted to further interpret the quantitative findings. The results indicate that psychological safety significantly increases students' willingness to disclose AI use and is positively shaped by perceived fairness, perceived teacher support, and perceived organisational support. Conversely, evaluation apprehension reduces disclosure intention and psychological safety, and is strengthened by perceived stigma, perceived uncertainty, and privacy concern. Qualitative findings further reveal that institutional clarity and supportive instructional practices encourage openness, whereas policy ambiguity and fear of negative evaluation often lead students to adopt cautious or strategic disclosure practices. Overall, the study highlights the dual role of enabling and inhibitory psychological mechanisms in shaping AI-use disclosure and underscores the importance of supportive institutional environments and clear guidance for promoting responsible AI transparency in higher education.

---


### 189. [Bridging the Training-Deployment Gap: Gated Encoding and Multi-Scale Refinement for Efficient Quantization-Aware Image Enhancement](https://arxiv.org/abs/2604.21743)

**<font color=#1a73e8>作者：</font>** Dat To-Thanh, Nghia Nguyen-Trong, Hoang Vo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Image enhancement models for mobile devices often struggle to balance high output quality with the fast processing speeds required by mobile hardware. While recent deep learning models can enhance low-quality mobile photos into high-quality images, their performance is often degraded when converted to lower-precision formats for actual use on mobile phones. To address this training-deployment mismatch, we propose an efficient image enhancement model designed specifically for mobile deployment. Our approach uses a hierarchical network architecture with gated encoder blocks and multiscale refinement to preserve fine-grained visual features. Moreover, we incorporate Quantization-Aware Training (QAT) to simulate the effects of low-precision representation during the training process. This allows the network to adapt and prevents the typical drop in quality seen with standard post-training quantization (PTQ). Experimental results demonstrate that the proposed method produces high-fidelity visual output while maintaining the low computational overhead needed for practical use on standard mobile devices. The code will be available at this https URL.

---


### 190. [Interpretable facial dynamics as behavioral and perceptual traces of deepfakes](https://arxiv.org/abs/2604.21760)

**<font color=#1a73e8>作者：</font>** Timothy Joseph Murphy, Jennifer Cook, Hélio Clemente José Cuve  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detection research has largely converged on deep learning approaches that, despite strong benchmark performance, offer limited insight into what distinguishes real from manipulated facial behavior. This study presents an interpretable alternative grounded in bio-behavioral features of facial dynamics and evaluates how computational detection strategies relate to human perceptual judgments. We identify core low-dimensional patterns of facial movement, from which temporal features characterizing spatiotemporal structure were derived. Traditional machine learning classifiers trained on these features achieved modest but significant above-chance deepfake classification, driven by higher-order temporal irregularities that were more pronounced in manipulated than real facial dynamics. Notably, detection was substantially more accurate for videos containing emotive expressions than those without. An emotional valence classification analysis further indicated that emotive signals are systematically degraded in deepfakes, explaining the differential impact of emotive dynamics on detection. Furthermore, we provide an additional and often overlooked dimension of explainability by assessing the relationship between model decisions and human perceptual detection. Model and human judgments converged for emotive but diverged for non-emotive videos, and even where outputs aligned, underlying detection strategies differed. These findings demonstrate that face-swapped deepfakes carry a measurable behavioral fingerprint, most salient during emotional expression. Additionally, model-human comparisons suggest that interpretable computational features and human perception may offer complementary rather than redundant routes to detection.

---


### 191. [Transferable Physics-Informed Representations via Closed-Form Head Adaptation](https://arxiv.org/abs/2604.21761)

**<font color=#1a73e8>作者：</font>** Jian Cheng Wong, Isaac Yin Chung Lai, Pao-Hsiung Chiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) have garnered significant interest for their potential in solving partial differential equations (PDEs) that govern a wide range of physical phenomena. By incorporating physical laws into the learning process, PINN models have demonstrated the ability to learn physical outcomes reasonably well. However, current PINN approaches struggle to predict or solve new PDEs effectively when there is a lack of training examples, indicating they do not generalize well to unseen problem instances. In this paper, we present a transferable learning approach for PINNs premised on a fast Pseudoinverse PINN framework (Pi-PINN). Pi-PINN learns a transferable physics-informed representation in a shared embedding space and enables rapid solving of both known and unknown PDE instances via closed-form head adaptation using a least-squares-optimal pseudoinverse under PDE constraints. We further investigate the synergies between data-driven multi-task learning loss and physics-informed loss, providing insights into the design of more performant PINNs. We demonstrate the effectiveness of Pi-PINN on various PDE problems, including Poisson's equation, Helmholtz equation, and Burgers' equation, achieving fast and accurate physics-informed solutions without requiring any data for unseen instances. Pi-PINN can produce predictions 100-1000 times faster than a typical PINN, while producing predictions with 10-100 times lower relative error than a typical data-driven model even with only two training samples. Overall, our findings highlight the potential of transferable representations with closed-form head adaptation to enhance the efficiency and generalization of PINNs across PDE families and scientific and engineering applications.

---


### 192. [Thinking with Reasoning Skills: Fewer Tokens, More Accuracy](https://arxiv.org/abs/2604.21764)

**<font color=#1a73e8>作者：</font>** Guangxiang Zhao, Qilong Shi, Xusen Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning LLMs often spend substantial tokens on long intermediate reasoning traces (e.g., chain-of-thought) when solving new problems. We propose to summarize and store reusable reasoning skills distilled from extensive deliberation and trial-and-error exploration, and to retrieve these skills at inference time to guide future reasoning. Unlike the prevailing \emph{reasoning from scratch} paradigm, our approach first recalls relevant skills for each query, helping the model avoid redundant detours and focus on effective solution paths. We evaluate our method on coding and mathematical reasoning tasks, and find that it significantly reduces reasoning tokens while improving overall performance. The resulting lower per-request cost indicates strong practical and economic potential for real-world deployment.

---


### 193. [PrismaDV: Automated Task-Aware Data Unit Test Generation](https://arxiv.org/abs/2604.21765)

**<font color=#1a73e8>作者：</font>** Hao Chen, Arnab Phani, Sebastian Schelter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data is a central resource for modern enterprises, and data validation is essential for ensuring the reliability of downstream applications. However, existing automated data unit testing frameworks are largely task-agnostic: they validate datasets without considering the semantics and requirements of the code that consumes the data.
We present PrismaDV, a compound AI system that analyzes downstream task code together with dataset profiles to identify data access patterns, infer implicit data assumptions, and generate task-aware executable data unit tests. To further adapt the data unit tests over time to specific datasets and downstream tasks, we propose "Selective Informative Feedback for Task Adaptation" (SIFTA), a prompt-optimization framework that leverages the scarce outcomes from the execution of data unit tests and downstream tasks. We evaluate PrismaDV on two new benchmarks spanning 60 tasks across five datasets, where it consistently outperforms both task-agnostic and task-aware baselines in generating unit tests that reflect the end-to-end impact of data errors. Furthermore, we show that with SIFTA, we can automatically learn prompts for PrismaDV's modules that outperform prompts written by hand or generated from a generic prompt optimizer. We publicly release our benchmarks and prototype implementation.

---


### 194. [AUDITA: A New Dataset to Audit Humans vs. AI Skill at Audio QA](https://arxiv.org/abs/2604.21766)

**<font color=#1a73e8>作者：</font>** Tasnim Kabir, Dmytro Kurdydyk, Aadi Palnitkar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing audio question answering benchmarks largely emphasize sound event classification or caption-grounded queries, often enabling models to succeed through shortcut strategies, short-duration cues, lexical priors, dataset-specific biases, or even bypassing audio via metadata and captions rather than genuine reasoning Thus, we present AUDITA (Audio Understanding from Diverse Internet Trivia Authors), a large-scale, real-world benchmark to rigorously evaluate audio reasoning beyond surface-level acoustic recognition. AUDITA comprises carefully curated, human-authored trivia questions grounded in real-world audio, designed to stress robust auditory reasoning through challenging distractors and long-range temporal dependencies, using probing queries that cannot be answered from isolated text or sound cues alone. Human average accuracy of 32.13% shows both the challenge of the task while demonstrating meaningful comprehension of the audio. In stark contrast, state of-the-art audio question answering models perform poorly, with average accuracy below 8.86%. Beyond raw accuracy, we apply Item Response Theory (IRT) to estimate latent proficiency, question difficulty, and expose systematic deficiencies of the models and data.

---


### 195. [Misinformation Span Detection in Videos via Audio Transcripts](https://arxiv.org/abs/2604.21767)

**<font color=#1a73e8>作者：</font>** Breno Matos, Rennan C. Lima, Savvas Zannettou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online misinformation is one of the most challenging issues lately, yielding severe consequences, including political polarization, attacks on democracy, and public health risks. Misinformation manifests in any platform with a large user base, including online social networks and messaging apps. It permeates all media and content forms, including images, text, audio, and video. Distinctly, video-based misinformation represents a multifaceted challenge for fact-checkers, given the ease with which individuals can record and upload videos on various video-sharing platforms. Previous research efforts investigated detecting video-based misinformation, focusing on whether a video shares misinformation or not on a video level. While this approach is useful, it only provides a limited and non-easily interpretable view of the problem given that it does not provide an additional context of when misinformation occurs within videos and what content (i.e., claims) are responsible for the video's misinformation nature.
In this work, we attempt to bridge this research gap by creating two novel datasets that allow us to explore misinformation detection on videos via audio transcripts, focusing on identifying the span of videos that are responsible for the video's misinformation claim (misinformation span detection). We present two new datasets for this task. We transcribe each video's audio to text, identifying the video segment in which the misinformation claims appears, resulting in two datasets of more than 500 videos with over 2,400 segments containing annotated fact-checked claims. Then, we employ classifiers built with state-of-the-art language models, and our results show that we can identify in which part of a video there is misinformation with an F1 score of 0.68. We make publicly available our annotated datasets. We also release all transcripts, audio and videos.

---


### 196. [Back to Source: Open-Set Continual Test-Time Adaptation via Domain Compensation](https://arxiv.org/abs/2604.21772)

**<font color=#1a73e8>作者：</font>** Yingkai Yang, Chaoqi Chen, Hui Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-Time Adaptation (TTA) aims to mitigate distributional shifts between training and test domains during inference time. However, existing TTA methods fall short in the realistic scenario where models face both continually changing domains and the simultaneous emergence of unknown semantic classes, a challenging setting we term Open-set Continual Test-Time Adaptation (OCTTA). The coupling of domain and semantic shifts often collapses the feature space, severely degrading both classification and out-of-distribution detection. To tackle this, we propose DOmain COmpensation (DOCO), a lightweight and effective framework that robustly performs domain adaptation and OOD detection in a synergistic, closed loop. DOCO first performs dynamic, adaptation-conditioned sample splitting to separate likely ID from OOD samples. Then, using only the ID samples, it learns a domain compensation prompt by aligning feature statistics with the source domain, guided by a structural preservation regularizer that prevents semantic distortion. This learned prompt is then propagated to the OOD samples within the same batch, effectively isolating their semantic novelty for more reliable detection. Extensive experiments on multiple challenging benchmarks demonstrate that DOCO outperforms prior CTTA and OSTTA methods, establishing a new state-of-the-art for the demanding OCTTA setting.

---


### 197. [Adversarial Robustness of Near-Field Millimeter-Wave Imaging under Waveform-Domain Attacks](https://arxiv.org/abs/2604.21774)

**<font color=#1a73e8>作者：</font>** Lhamo Dorje, Jordan Madden, Soamar Homsi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Near-field millimeter-wave (mmWave) imaging is widely deployed in safety-critical applications such as airport passenger screening, yet its own security remains largely unexplored. This paper presents a systematic study of the adversarial robustness of mmWave imaging algorithms under waveform-domain physical attacks that directly manipulate the image reconstruction process. We propose a practical white-box adversarial model and develop a differential imaging attack framework that leverages the differentiable imaging pipeline to optimize attack waveforms. We also construct a real measured dataset of clean and attack waveforms using a mmWave imaging testbed. Experiments on 10 representative imaging algorithms show that mmWave imaging is highly vulnerable to such attacks, enabling an adversary to conceal or alter targets with moderate transmission power. Surprisingly, deep-learning-based imaging algorithms demonstrate higher robustness than classical algorithms. These findings expose critical security risks and motivate the development of robust and secure mmWave imaging systems.

---


### 198. [Reshoot-Anything: A Self-Supervised Model for In-the-Wild Video Reshooting](https://arxiv.org/abs/2604.21776)

**<font color=#1a73e8>作者：</font>** Avinash Paliwal, Adithya Iyer, Shivin Yadav 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise camera control for reshooting dynamic videos is bottlenecked by the severe scarcity of paired multi-view data for non-rigid scenes. We overcome this limitation with a highly scalable self-supervised framework capable of leveraging internet-scale monocular videos. Our core contribution is the generation of pseudo multi-view training triplets, consisting of a source video, a geometric anchor, and a target video. We achieve this by extracting distinct smooth random-walk crop trajectories from a single input video to serve as the source and target views. The anchor is synthetically generated by forward-warping the first frame of the source with a dense tracking field, which effectively simulates the distorted point-cloud inputs expected at inference. Because our independent cropping strategy introduces spatial misalignment and artificial occlusions, the model cannot simply copy information from the current source frame. Instead, it is forced to implicitly learn 4D spatiotemporal structures by actively routing and re-projecting missing high-fidelity textures across distinct times and viewpoints from the source video to reconstruct the target. At inference, our minimally adapted diffusion transformer utilizes a 4D point-cloud derived anchor to achieve state-of-the-art temporal consistency, robust camera control, and high-fidelity novel view synthesis on complex dynamic scenes.

---


### 199. [SemEval-2026 Task 4: Narrative Story Similarity and Narrative Representation Learning](https://arxiv.org/abs/2604.21782)

**<font color=#1a73e8>作者：</font>** Hans Ole Hatzel, Ekaterina Artemova, Haimo Paul Stiemer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the shared task on narrative similarity and narrative representation learning - NSNRL (pronounced "nass-na-rel"). The task operationalizes narrative similarity as a binary classification problem: determining which of two stories is more similar to an anchor story. We introduce a novel definition of narrative similarity, compatible with both narrative theory and intuitive judgment. Based on the similarity judgments collected under this concept, we also evaluate narrative embedding representations. We collected at least two annotations each for more than 1,000 story summary triples, with each annotation being backed by at least two annotators in agreement. This paper describes the sampling and annotation process for the dataset; further, we give an overview of the submitted systems and the techniques they employ. We received a total of 71 final submissions from 46 teams across our two tracks. In our triple-based classification setup, LLM ensembles make up many of the top-scoring systems, while in the embedding setup, systems with pre- and post-processing on pretrained embedding models perform about on par with custom fine-tuned solutions. Our analysis identifies potential headroom for improvement of automated systems in both tracks. The task website includes visualizations of embeddings alongside instance-level classification results for all teams.

---


### 200. [From Codebooks to VLMs: Evaluating Automated Visual Discourse Analysis for Climate Change on Social Media](https://arxiv.org/abs/2604.21786)

**<font color=#1a73e8>作者：</font>** Katharina Prasse, Steffen Jung, Isaac Bravo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Social media platforms have become primary arenas for climate communication, generating millions of images and posts that - if systematically analysed - can reveal which communication strategies mobilise public concern and which fall flat. We aim to facilitate such research by analysing how computer vision methods can be used for social media discourse analysis. This analysis includes application-based taxonomy design, model selection, prompt engineering, and validation. We benchmark six promptable vision-language models and 15 zero-shot CLIP-like models on two datasets from X (formerly Twitter) - a 1,038-image expert-annotated set and a larger corpus of over 1.2 million images, with 50,000 labels manually validated - spanning five annotation dimensions: animal content, climate change consequences, climate action, image setting, and image type. Among the models benchmarked, Gemini-3.1-flash-lite outperforms all others across all super-categories and both datasets, while the gap to open-weight models of moderate size remains relatively small. Beyond instance-level metrics, we advocate for distributional evaluation: VLM predictions can reliably recover population level trends even when per-image accuracy is moderate, making them a viable starting point for discourse analysis at scale. We find that chain-of-thought reasoning reduces rather than improves performance, and that annotation dimension specific prompt design improves performance. We release tweet IDs and labels along with our code at this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-231](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
