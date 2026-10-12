# 📦 其他研究 | 2026年10月13日

> 本类共 **244** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-244**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-244**

---

### 201. [Variance-Reduced Policy Gradient is Nearly Minimax-Optimal](https://arxiv.org/abs/2610.13692)

**<font color=#1a73e8>作者：</font>** Leonardo Cesani, Matteo Papini, Marcello Restelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard Policy Gradient (PG) algorithms suffer from high estimation variance because they rely on Monte Carlo updates. While off-policy variance reduction mitigates this problem, establishing optimal sample complexity currently requires either restrictive assumptions, such as uniformly bounded importance weights, or impractical second-order operations. In this work, we introduce Loopless Variance-Reduced PG (LVR-PG), a unified theoretical framework that abstracts a class of first-order estimators that integrate recursive updates with defensive importance sampling, including known estimators such as PAGE-PG and STORM-PG. We prove that this algorithmic class achieves $\tilde{\mathcal{O}}(\epsilon^{-2})$ last-iterate global convergence under weak gradient domination for general parametric policies. We establish this guarantee using purely first-order updates, with minimal assumptions and without gradient preconditioners. By extending state-of-the-art lower bounds to continuous parametric policies, we establish an $\Omega(\epsilon^{-2})$ sample complexity limit, confirming our framework is minimax-optimal up to logarithmic factors and horizon terms.

---


### 202. [Calibration in One Go: Jointly Learning Accurate and Calibrated Neural Networks](https://arxiv.org/abs/2610.13693)

**<font color=#1a73e8>作者：</font>** Nektarios Kalampalikis, Pablo M. Olmos, Isabel Valera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks (NNs), while highly flexible and versatile, are often poorly calibrated. Post-hoc calibration methods adjust the outputs of an already trained model using a separate calibration dataset and additional calibration parameters. This process adds overhead that requires separate optimization of the calibrator and subsequent model selection. In this paper, we show that standard (post-hoc) calibrators can be trained end-to-end with the backbone via a bilevel Stackelberg formulation. This formulation eliminates the need for a separate calibration set or a dedicated calibration loss by jointly optimizing accuracy and calibration using cross-entropy, introducing only one additional hyperparameter: the calibrator learning rate. Although our framework supports calibrators ranging from temperature and matrix scaling to NN layers, our results show that using the final classification layer itself as the calibrator yields accurate, well-calibrated models with no additional parameters. Our approach outperforms SOTA calibrators with minimal added complexity, while also avoiding the multiplicative overhead of separate calibration components in settings such as multi-task learning.

---


### 203. [GLIMPSE: Global-Local Indexing with Multi-Precision Spectral Encoding for Explorable Video World Models](https://arxiv.org/abs/2610.13706)

**<font color=#1a73e8>作者：</font>** Zhufeng Xu, Henglei Lv, Bailin Deng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A camera-controlled video world model must keep a scene consistent when the camera returns to it. Memories that render stored features into the target frame can turn depth and pose errors into ghosting or duplicated structure. Positional transport avoids that resampling by relocating a historical patch's address rather than its content, but assigns full positional precision even to inaccurate projections. We present GLIMPSE, a global-local memory interface with band-wise multi-precision coordinates and geometry-conditioned spectral attenuation to reduce sensitivity to inaccurate projected addresses. Local patch memory supplies view-specific appearance, while recurrent global memory provides scene context. Footprint-guided retrieval selects historical patches under a fixed local read budget. Under matched retrieval and read budgets, GLIMPSE improves geometric correspondence and photometric consistency over deterministic positional transport.

---


### 204. [Towards Understanding the Training of GFlowNets: A Theoretical Perspective](https://arxiv.org/abs/2610.13711)

**<font color=#1a73e8>作者：</font>** Rui Hu, Yu Chen, Zhuoran Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative Flow Networks (GFlowNets) learn policies that sample discrete objects in proportion to a positive reward. They are trained by minimizing balance objectives, whose exact satisfaction guarantees correct sampling. However, a comprehensive theory linking nonzero balance loss and approximate stationarity to sampling accuracy, especially under evolving sampling distributions and backward policies, is still lacking. To bridge this gap, we develop a unified theory for Flow Matching, Detailed Balance, and Trajectory Balance in this regime. We first bound terminal symmetric KL by the square root of the expected balance loss. Then, we show that approximate stationarity controls this distribution error up to a tangent-space residual measuring parameterization incompleteness. Finally, we establish finite-time convergence under fixed or controlled sampling and fixed, balance-trained, or separately updated backward policies. Under standard smoothness assumptions, with fixed or controlled sampling and a fixed or balance-trained backward policy, the expected loss is $O(\bar\epsilon^2+T^{-1})$ and expected terminal symmetric KL is $O(\bar\epsilon+T^{-1/2})$ under uniform coverage. For a separately updated backward policy, we characterize the sufficient update decay to approach the residual neighborhood and preserve these rates. These results connect balance objectives to sampling accuracy and clarify how parameterization, coverage, and moving components govern GFlowNet training.

---


### 205. [Machine Unlearning for Federated Socially Fair k-Means Clustering](https://arxiv.org/abs/2610.13717)

**<font color=#1a73e8>作者：</font>** Aravind Reddy, Deeraj S K, Mohd Wasif Raza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated clustering can support applications such as patient stratification across hospitals and customer segmentation across distributed financial datasets. Responsible AI calls for fair representation of demographic groups and support for data deletion, motivated in part by rights such as the GDPR's right to erasure. These goals interact: deleting records can change the balance between groups and alter the clustering of the remaining population. We study exact machine unlearning for federated socially fair $k$-means, whose objective is to minimize the largest group-average squared distance to the nearest center. Our approach keeps separate local summaries for each group, so summaries at unaffected institutions remain valid as global fairness weights change. For two groups, we prove an initialization approximation guarantee independent of client group proportions under ideal sampling, and we show that same-seed replay reproduces retraining exactly. Reuse pays off most when a whole client withdraws: across three datasets, replay is $35.8\times$ faster than retraining for the initialization-only model and remains $2.4\times$ and $1.7\times$ faster with one and two fair-refinement rounds, which improve worst-group cost. For individual record deletions, gains are modest (about $1.06\times$), and certifying cached assignments can cost more than it saves. These results map where exact unlearning can profitably reuse computation. Code and reproducibility materials are available at this https URL.

---


### 206. [State-Isolated Vision Mamba via Update-Tendency Routing for Underwater Image Enhancement](https://arxiv.org/abs/2610.13720)

**<font color=#1a73e8>作者：</font>** Yan Luo, Laibin Chang, Zefan Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Mamba has recently emerged as an efficient alternative to convolutional and Transformer-based architectures by modeling long-range spatial dependencies through recurrent state evolution. Existing studies primarily improve token serialization, scanning strategies, or expert routing, yet largely overlook a state level question question: how should recurrent states be organized for spatially heterogeneous visual restoration? In this paper, we show that forcing tokens with heterogeneous update behaviors to recurrently modify a shared hidden state leads to persistent cross-content interference, which we term \textbf{State Contention}. We further argue that effective recurrent modeling should organize state evolution according to token compatibility rather than token ordering. Based on this observation, we introduce \textbf{State Isolation}, a new recurrent state organization principle for Vision Mamba,tokens with compatible state-update tendencies evolve within independent recurrent state streams. To instantiate this principle, we propose \textbf{IsoMamba}, a $\Delta$-guided architecture that constructs model-intrinsic update representations, discovers update-compatible token groups through label-free clustering, and routes them to isolated Mamba experts following a \textbf{cluster--route--isolate} paradigm. In addition, we develop a dynamic channel-wise reweighting objective to compensate for wavelength-dependent reconstruction difficulty in underwater images. Extensive experiments demonstrate that IsoMamba consistently achieves state-of-the-art performance on multiple underwater image enhancement benchmarks while providing cleaner hidden state responses, validating the effectiveness of state isolated recurrent modeling.

---


### 207. [Amortized Counterfactual Prediction with Graph Neural Networks](https://arxiv.org/abs/2610.13724)

**<font color=#1a73e8>作者：</font>** Hendrik Stumpf, Francesco Quinzan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual inference asks how an observed outcome might have differed under different circumstances, such as whether a patient would have recovered had they received a different treatment. Such questions arise whenever decisions depend on the outcomes of alternatives that were not observed. Answering counterfactual queries generally requires knowledge of the underlying causal structure, which is often unavailable in practice. A common approach is therefore to first estimate the causal graph from observational data and then perform counterfactual inference. However, errors in the estimated causal graph can propagate to downstream counterfactual predictions. To address this challenge, we introduce the Counterfactual Graph Neural Process (CFGNP), an end-to-end approach that answers counterfactual queries directly from observational data without first estimating a causal graph. CFGNP uses Graph Neural Networks (GNNs) to exploit the dual-graph structure by restricting cross-world message passing to corresponding factual--counterfactual variables. Across synthetic and image-based benchmarks, CFGNP achieves stronger predictive performance than existing approaches, including on the German Loan benchmark, where it reduces MSE from $4.51 \times 10^{-2}$ to $0.19 \times 10^{-2}$. Furthermore, on synthetic causal graphs, a model trained only on 10-node graphs maintains strong predictive performance on graphs with up to 30 nodes, without retraining.

---


### 208. [SeoulMMOD: A Large-Scale Multimodal Origin-Destination Flow Benchmark](https://arxiv.org/abs/2610.13730)

**<font color=#1a73e8>作者：</font>** Taeyoung Yu, Seonbin Jo, Jiwon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Origin-destination (OD) flow forecasting supports urban mobility decisions by predicting the volume and patterns of human movement across a city. Most existing public OD benchmarks provide only a partial view of citywide mobility, covering a single transport service or at most two modes. With partial mode coverage, observed demand changes are difficult to separate into shifts across transport modes and changes in total travel. We introduce SeoulMMOD, a large-scale public benchmark for citywide multimodal mobility in Seoul. SeoulMMOD provides three years of hourly OD flows estimating total mobility for 6 urban travel modes across 25 districts and 426 sub-districts, together with travel-time, travel-distance, calendar, rainfall, and point-of-interest (POI) signals. Using SeoulMMOD, we benchmark 14 forecasting baselines under a common protocol and analyse the effects of spatial scaling, joint versus mode-separate training, and cross-year generalization. Results show that several spatio-temporal models that work at district level do not scale to sub-district OD forecasting, and that naive joint multi-mode training does not consistently improve accuracy. Together, the dataset and benchmark establish a reproducible testbed for multi-mode, multi-year OD forecasting at the city scale.

---


### 209. [KVeil: First-Place Solution to ECCV 2026 LifeGenIP Challenge on Unlearnable Videos](https://arxiv.org/abs/2610.13733)

**<font color=#1a73e8>作者：</font>** Boheng Li, Yueming Xing, Yiming Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid development of personalized video generation has raised serious concerns over identity privacy, as a few facial videos of a person now suffice to reproduce their identity in synthetic videos. This report presents the first-place solutions to both phases of the ECCV 2026 LifeGenIP Challenge on Unlearnable Videos, which aims to protect facial videos from unauthorized customization under a limited and imperceptible perturbation budget. For Phase 1, we introduce Reference Capacity Collapse, a pair of complementary losses that degrade the information carried by the reference condition while keeping subsequent video representations dependent on it, together with a Motion-Guided EOT mechanism that improves robustness across unknown inference conditions. Phase 2 further considers tuning-based customization and unseen generative models. To address both threats within a single perturbation, we design a two-layer framework that protects the facial and background regions separately, constructing structure-aligned perturbations from a synthetic target identity in the former and strengthening the white-box disruption of Phase 1 in the latter. Our method achieves nearly perfect protection under white-box reference-based customization, and remains effective under other customization paradigms, various models, and temporal attacks. Both solutions are built upon our recent work LETHE. We hope our solutions can inspire future work on protecting facial videos against unauthorized customization. Our code is available at this https URL.

---


### 210. [Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers](https://arxiv.org/abs/2610.13735)

**<font color=#1a73e8>作者：</font>** Yuhong Chou, Zehao Liu, Yuqi Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient attention mechanisms, such as linear and sliding window attention, aim to reduce the computational complexity of Transformers from quadratic to linear. However, their degraded in-context recall often necessitates interleaving full attention layers, leaving the quadratic bottleneck unresolved in long-context processing. To address this, we introduce Orthros attention, which shifts the efficiency paradigm from structural allocation to phase-aware decoupling. As a unified module, it dynamically switches its computation pattern across different phases of sequence processing, enabling linear complexity prefilling and full attention decoding. Our design grants Orthros attention a lower asymptotic complexity compared to vanilla Transformers in prevalent long-context scenarios characterized by heavy prefilling and light decoding. Beyond theoretical formulation and complexity analysis, extensive empirical evaluations demonstrate Orthros's superiority across multiple dimensions. First, we validate its fundamental language modeling capabilities, demonstrating scalability across varying model sizes and strong competitiveness in comprehensive architectural comparisons. Second, Orthros exhibits exceptional conversion feasibility via a data-efficient Transformer-to-Orthros conversion, yielding performance that even surpasses the original Transformer. Finally, Orthros achieves a $21.9\times$ prefilling speedup over Transformers with end-to-end inference gains, while preserving long-context capabilities, as demonstrated by near-perfect 128K needle-in-a-haystack results and Transformer-level performance on real-world in-context recall tasks. Overall, these advantages in high performance, flexibility, and efficiency position Orthros as a promising candidate to succeed the Transformer in industrial applications.

---


### 211. [SafeDiSTL: Decomposing Joint Constraints for Safe Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.13737)

**<font color=#1a73e8>作者：</font>** Hongrui Zheng, Aditya Singh, Rahul Mangharam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-agent tasks often impose constraints on a shared objective or collective safety. A team level violation cost function can measure this constraint outcome, but does not distinguish which agents' actions most strongly influence that violation. We present SafeDiSTL, a constrained multi-agent reinforcement learning framework that allows for credit assignment even with joint constraint measurements. We use Signal Temporal Logic (STL) robustness to measure episode-level violation through running-maximum cost increments. Smooth full-episode robustness and differentiable dynamics provide action sensitivities, which allocate each cost increment across agents at the same decision time. These sensitivities account for delayed effects when weighting agents' shares of each cost increment. We study the framework in cooperative payload transport, connected navigation, and networked traffic control tasks. SafeDiSTL achieves 1.6-5.1x the safe-success rate in transport, improves navigation safe-success by 11.1%, and delivers 50-68% more throughput in traffic when compared to constrained baselines. Results demonstrate a strong improvement of the learned policy in dealing with shared constraint while retaining the performance of unconstrained policies.

---


### 212. [Gaussian Splatting with Reflections Guided by What is Seen](https://arxiv.org/abs/2610.13757)

**<font color=#1a73e8>作者：</font>** Yiming Liang, Tianyu Xiao, Hiroshi Ishikawa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While novel view synthesis methods like Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have shown impressive performance on common scenes, they often struggle with capturing view-dependent specular effects, particularly near-field reflections. Existing methods utilize environment maps, which only represent lights from infinity, or environment Gaussians, which rely solely on indirect supervision from reflections, are insufficient for accurately modeling such effects. Here, we propose a framework based on 2D Gaussian Splatting (2DGS) that leverages directly observable environment information in input images. Our approach also integrates a hybrid reflection appearance representation and view-dependent specular modeling. Experiments on public benchmarks and a newly curated near-field reflection dataset demonstrate that our method achieves superior rendering quality and geometric accuracy.

---


### 213. [Neurons++: A Unified Visual-Stream Framework for Image and Video Reconstruction from fMRI with Neural-to-Visual Interpretability](https://arxiv.org/abs/2610.13763)

**<font color=#1a73e8>作者：</font>** Haonan Wang, Yuchen Wang, Jingyu Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Decoding visual experience from fMRI is important for understanding human perception and developing brain-computer interfaces. Recent generative decoding methods can reconstruct plausible images and videos, but visual plausibility alone does not ensure that the output is faithfully grounded in brain activity. In this work, we propose Neurons++, a visual-stream fMRI reconstruction framework for both static image and dynamic video reconstruction. Compared with our conference version Neurons, Neurons++ extends the paradigm from video-only reconstruction to visual-stream reconstruction for both images and videos, and replaces parallel task conditioning with serial cortex-inspired decoding. The model first uses image-fMRI pretraining to obtain a stable spatial-semantic initialization, and then performs subject-specific fine-tuning for image and video reconstruction separately. The serial design organizes fMRI-derived representations into explicit spatial, semantic, language-level, and temporal cues. Extensive experiments show that Neurons++ achieves state-of-the-art video reconstruction and competitive image reconstruction across standard benchmarks. Beyond reconstruction fidelity, neural-to-visual analyses indicate that Neurons++ exhibits qualitative directional controllability under neural perturbation, that its fMRI encoder read-out is sensitive to stimulus-relevant cortical features, and that it supports ROI-guided semantic modulation. Code and model weights are available at: this https URL.

---


### 214. [When Edge Independence Fails: Joint Graph Diffusion with Latent Sociability Priors](https://arxiv.org/abs/2610.13765)

**<font color=#1a73e8>作者：</font>** Adarsh Jamadandi, Nicolas Keriven, Aline Roumy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete graph diffusion models corrupt graph structure through independent edge updates with a Markovian noise model. Combined with the exchangeability requirement on the output distribution, the terminal prior is necessarily an Erdős--Rényi (E-R) random graph. This has a fundamental consequence for unconditional graph generation without node features: in the large graph limit, any GNN denoiser applied to an E-R graph approximately outputs an E-R graph, making effective denoising difficult. In practice, generated graphs fail to recover meaningful node heterogeneity and higher-order structure. Previous models introduced specialized node features to compensate, framing this as an expressivity problem, while the role of the prior remained unexamined. We instead address the root cause by introducing the Latent Sociability Prior (LSP) and a join} diffusion process that co-evolves latent node sociability variables and graph structure, removing edge independence while preserving exchangeability. Unlike existing latent graph diffusion methods, the sociability mechanism requires no complex encoder: its sole role is to guide edge updates and preserve node heterogeneity throughout the trajectory. We validate our approach on multiple graph generation datasets and show that the proposed framework more accurately captures graph distributions than baseline methods without node features.

---


### 215. [READ: Reading the Selective Scan for Faithful Video Attribution](https://arxiv.org/abs/2610.13776)

**<font color=#1a73e8>作者：</font>** Magdalena Trędowicz, Piotr Kubaty, Arkadiusz Lewicki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Selective state-space models are an efficient approach to long-sequence video modeling. However, their recurrent computation makes it difficult to determine which video tokens drive a prediction. Existing attribution methods often require additional backward passes or repeated model evaluations, making them substantially more expensive than the forward inference they aim to explain. In this work, we introduce READ, a parameter-free attribution method for selective state-space models that unrolls the recurrence at the position read by the classifier. READ traces the contribution accumulated in the recurrent state back to the video tokens that contribute to the final prediction. By anchoring attribution at the classifier's readout, it produces a single spatiotemporal relevance map from which frame- and region-level relevance can be obtained directly. Despite requiring only one forward pass, READ achieves competitive faithfulness and localisation compared with substantially more expensive attribution methods. Experimental results show that READ avoids the systematic relevance biases of existing methods while recovering meaningful temporal and class-specific structure across datasets and backbones. More broadly, our results show that the recurrence underlying selective state-space models is not only an efficient mechanism for inference, but also a direct source of interpretable evidence for their predictions.

---


### 216. [Detection of extremely rare dead cells in fluorescence microscopy images](https://arxiv.org/abs/2610.13780)

**<font color=#1a73e8>作者：</font>** Prateek Verma, Benjamin Butter, Jian Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dead cell detection in fluorescence microscopy is essential for phenotypic screening and drug efficacy assessment. However, automated identification remains challenging due to signal variability, optical artifacts, and colocalization ambiguities across multiple channels. Markers that define nuclear boundaries do not neatly coincide spatially or temporally with apoptotic markers. Furthermore, marker accumulation kinetics vary across individual cells and apoptosis stages, making universal thresholds unreliable. We present a systematic comparison of several computational approaches for detecting apoptotic cells in nucleus-stained specimens: (1) heuristic methods using intensity thresholds, distributions, correlations, and domain guidance; (2) classification using numerical features (Logistic Regression, Random Forest, XGBoost and LightGBM) and image features (ResNet-18 and EfficientNet-B0); and (3) anomaly detection, also using numerical features (Isolation Forest, one-class SVM and PCA reconstruction) and image features (convolutional autoencoders and Deep SVDD). Using a dataset of 258 images containing 65,527 cells/nuclei across multiple scenes with 243 manually annotated ground truth dead cells, we evaluate each method on metrics such as PR-AUC, Precision, Recall, F1-score, and macro-F1. Our results indicate that classification using image features (deep learning) and numerical features (traditional) achieved the best performance, with ResNet-18 and XGBoost significantly outperforming manually designed heuristics and anomaly detection methods. Our findings demonstrate that such biomedical problems remain highly challenging to solve even with the state-of-the-art computational and learning techniques. We aim to provide an effective decision-support tool to researchers while tackling such problems either fully-automatically or in a human-in-the-loop setting as an aide to domain scientists.

---


### 217. [Your Discrete Graph Diffusion Model is Secretly Memorizing](https://arxiv.org/abs/2610.13786)

**<font color=#1a73e8>作者：</font>** Adarsh Jamadandi, Nicolas Keriven  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete graph diffusion models (GDMs) corrupt the graph structure by adding noise independently to nodes and edges under a Markovian noise model. In the unconditional setting without node features, an equivariant denoiser trained on a single graph is able to generate novel graphs and sample-level metrics such as edge overlap and WL kernel similarity find no evidence of memorization. In this work, we challenge this view and show for the first time that graph diffusion models indeed exhibit memorization. Analyzing the reverse diffusion trajectories of GDMs trained on two-block stochastic block models (SBMs), we find a strong train-data bias: the model recovers a corrupted training graph almost perfectly compared to a held-out test graph. We term this conditional memorization, as it surfaces only when the reverse trajectory is conditioned on a corrupted training graph and is not apparent during inference. It coincides with a growing generalization gap, where the training loss improves as the loss on held-out graphs degrades, and it cannot be mitigated by early stopping. The onset of memorization always precedes the emergence of community structure in the generated graphs, thus every checkpoint earlier produces structureless graphs. This behavior holds across all node sizes we test.

---


### 218. [Randomized Momentum Transport with Cheap Predictors](https://arxiv.org/abs/2610.13789)

**<font color=#1a73e8>作者：</font>** El Mahdi Chayti, Martin Jaggi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Momentum methods such as STORM and second-order momentum track the gradient by adding a transport correction to momentum, at the cost of an extra oracle call per iteration. We introduce randomized momentum transport, which evaluates the correction with probability $q$ and otherwise uses a cheap prediction, with importance weighting that preserves the conditional mean and adds $(q^{-1}-1)$ times the prediction loss to the variance. Under transport-bias, second-moment, and residual-control assumptions, linear minimization oracle (LMO) updates, including normalized, sign, and exact spectral (Muon) directions, retain an $O(T^{-1/3})$ stationarity bound for each fixed $q>0$ with a single-gradient initialization. For unnormalized STORM, some $q<1$ lowers the leading coefficient of our sufficient gradient budget if and only if the gradient-difference noise modulus exceeds the smoothness constant, by at most about $10\%$. An online diagonal predictor admits a regret-to-convergence guarantee. At approximately equal oracle cost, querying a quarter of the corrections lowers the final training loss by $18$ to $43\%$ on MNIST1D and raises the test accuracy of Hessian-vector transport on CIFAR-10 by $1.5$ points.

---


### 219. [REFLECT: Role-Aware Detection of Sentiment, Emotion, Politeness, and Formality](https://arxiv.org/abs/2610.13797)

**<font color=#1a73e8>作者：</font>** Sangpil Youm, Annabel Stocks Natalias, Hayden Heninger 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting communicative meaning in dialogue requires modeling not only lexical content but also the participant-role structures through which sentiment, emotion, politeness, and formality (SEPF) are expressed. Existing approaches rely on contextual language representations while leaving semantic roles implicit. We introduce a role-aware transformer architecture that maps the four SEPF dimensions to theory-grounded Semantic Role Labeling (SRL) configurations, incorporating these configurations directly into the transformer's self-attention mechanism. Role-aware attention models non-directional internal states (sentiment and emotion), while directional role-aware attention captures initiator-to-recipient relations for external cues (politeness and formality). The resulting role-aware representations are fused with contextual embeddings through a learned gate that adaptively weights how much role information each input contributes, rather than appending semantic roles as an auxiliary feature vector. Across four benchmark datasets, the framework yields statistically reliable gains over strong BERT-based baselines for emotion, politeness, and formality, with gains concentrated in theoretically predicted cases such as low-frequency, complex emotions and highly polite expressions; sentiment improvements are marginal and non-significant, suggesting that sentiment is conveyed more through lexical choice than participant-role structure. Additional evaluation on real-world data demonstrates that the framework improves both predictive performance and model traceability. These results demonstrate that linguistically grounded modifications to transformer self-attention improve the detection of communicative meaning, generalize beyond benchmark datasets to real-world mental-health data, and yield traceable, role-grounded explanations that extend beyond predictive performance to interpretability.

---


### 220. [FORTE: A Production Framework for Feature Evaluation and Deprecation in Industrial Recommender Systems](https://arxiv.org/abs/2610.13806)

**<font color=#1a73e8>作者：</font>** Vishnu Arun, Adam Obeng, Tianyou Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production recommender systems have feature-lifecycle asymmetry: adding new features must produce gains on some metric, while feature removal must not regress any metric. In practice, feature deprecation is hard to prioritize as a feature can fail to be removed if it interacts with other features, its importance changes daily, it cannot be evaluated before production models change or data drift occurs, it is in contention for A/B test space with other launches, it causes regressions in an online A/B test, or it is consumed by multiple models that need to coordinate its deprecation. We present FORTE, a model-agnostic production framework for discovering, validating, and removing features. Its efficient perturbation implementation allows daily feature evaluation. To account for interactions, it evaluates candidate feature sets constructed from all the low-rank features through grouped ablation and its offline results are sufficiently predictive of online A/B tests to allow deprecations to proceed to online testing with confidence. Lineage tracing identifies all downstream consumer models to realize the full savings of removing a feature from the training set. We validate FORTE over 2 large-scale recommender systems and find that it identifies deprecable feature sets which do not cause online regressions, while the impact on efficiency depends on model characteristics. On a search-relevance model, FORTE resulted in 3 nested candidate sets of 32, 48, and 59 features. Online guardrails rejected the largest treatment. The 48-feature set was selected for deprecation, removing 43.3% of the model's features. On a large ranking model, FORTE identified 8 candidates for removal. Retraining and A/B testing confirmed no regression. Its launch reduced the trainable parameters by 29.9%, improved serving throughput by 19.8-25.5%, and reduced annual training costs by hundreds of thousands of dollars.

---


### 221. [Error Rate is Not Enough: Costs of Augmentation in Low-Resource ASR](https://arxiv.org/abs/2610.13807)

**<font color=#1a73e8>作者：</font>** Katsumi Ibaraki, David Chiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data augmentation is standard practice for low-resource automatic speech recognition (ASR), but its benefits are almost always reported as aggregate error rates, leaving open why and when a method helps. On four low-resource languages and English at five data sizes, we cross two augmentations that modify existing audio (speed perturbation and SpecAugment) with two that modify text transcriptions and synthesize audio from it. We analyze errors at the phoneme level and find that they help for complementary reasons. SpecAugment has the most reliable aggregate improvements, but increases tone and palatalization errors, whereas text-based methods introduce consonant insertions; in combination, each reduces the errors the other introduces. This complementarity is predictable. Tone and palatalization are each signaled by a single acoustic property and occur least frequently in training (lowest training exposure), and text-based methods that flatten word frequency raise their frequency by 37--38%, reversing those errors while further improving aggregate error. The improvement from combining the methods exceeds the sum of their individual improvements; the superadditivity vanishes by 100 hours, limiting the complementarity to the low-resource regime. Where specific error types matter, we recommend selecting augmentation by training exposure and acoustic properties, both measurable before any training.

---


### 222. [Spanning Diffusion and Flow-based Posterior Sampling via Exact Gaussian Conditioning](https://arxiv.org/abs/2610.13812)

**<font color=#1a73e8>作者：</font>** Teo Deveney, Lea Bogensperger, Hok Shing Wong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-matching and diffusion models are increasingly used as priors for linear inverse problems, however, most methods are bespoke to one class of trajectory prior. Plug-and-play methods have been proposed, however these implicitly decorrelate the guided trajectory, resulting in broad priors that can struggle when data is sparse. This work proposes $\beta$-Flow: a general plug-and-play method indexed by a correlation parameter $\beta$ that generalises over flow, diffusion, and decorrelated priors, and a confidence parameter $\kappa$ that controls how strongly the path distribution is enforced. Each step requires only one forward evaluation of a denoising network, followed by a Gaussian conditioning step. This step is an exact Kalman update that is not dependent on network gradients. We show that many existing guided samplers can be interpreted as instances or approximations of our method, each implicitly using a different trajectory prior and operator in place of the Kalman gain. From this viewpoint, we provide a qualitative comparison of methods in terms of their implicit biases and assumptions. We demonstrate consistently state-of-the-art level performance across 7 inverse problems over 4 datasets in terms of PSNR and SSIM. Moreover, we demonstrate the utility of this prior control, by showing that confident high correlations (strict priors) work best when observations are less informative, while low correlation is preferred when observations are more informative, reflecting the complementary roles of the prior and likelihood in Bayesian inference.

---


### 223. [Shared Canonical Component Removal Beyond Expert Views](https://arxiv.org/abs/2610.13819)

**<font color=#1a73e8>作者：</font>** Jose Roberto Tello Ayala, Akl C. Fahed, Roy Perlis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In clinical practice, experts often begin by converting raw inputs into a set of expert features before making a decision. While black-box models trained on raw input can outperform models trained on expert views, it remains unclear what predictive signal the raw model exploits beyond what the expert view captures. We introduce an audit framework to quantify this gap using Shared Canonical Component Removal (SCCR). Unlike standard residualization or concept erasure, SCCR selectively removes only those directions strongly shared between learned raw and expert embeddings.
Evaluations on synthetic data, coronary artery disease (CAD) detection, antidepressant treatment dropout prediction, and skin lesion classification using SkinCon annotations show that SCCR identifies the ways in which expert views are insufficient and recovers residual predictive signal while minimizing redundancy with the expert view.

---


### 224. [Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge Update Efficiency](https://arxiv.org/abs/2610.13835)

**<font color=#1a73e8>作者：</font>** Sheng Zhao, Yuhao Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An ideal (language) model must continually update its knowledge. Existing work largely focuses on making these updates efficient after training. We investigate how the organization of time-varying knowledge during pre-training shapes the efficiency of subsequent updates. Models trained on chronologically ordered knowledge specialize in the most recently encountered knowledge; we call them specialists. In contrast, models trained on the same knowledge in randomly shuffled order perform well across all represented time periods; we call them generalists. Surprisingly, specialists require far fewer update steps than generalists to acquire new knowledge. To explain this advantage, we derive a law from first principles that relates update cost to the model's optimization dynamics and that closely predicts empirical results. Guided by these findings, we design a strategy for organizing pre-training data that preserves stable historical knowledge while enabling efficient updates to current knowledge. We also show that the benefits of temporal knowledge organization extend to real-world pre-trained models and existing knowledge update tools, and generalize to other knowledge orderings. Project page: this https URL

---


### 225. [Inference-Time Steering Across Scaffolds and Epitopes for Sample-Efficient De Novo Nanobody Design](https://arxiv.org/abs/2610.13844)

**<font color=#1a73e8>作者：</font>** Mason Minot, Simon Friedensohn, Cédric R. Weber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative molecular design typically relies on over-generation and post-hoc filtering. Inference-time steering methods like Feynman-Kac (FK) steering improve efficiency by biasing trajectories toward high-reward candidates, yet they optimize within a single fixed configuration. In de novo nanobody design, upfront commitment to conditioning choices like scaffold identity or target epitope creates a bottleneck. Since yield varies across these conditions, steering unpromising setups wastes compute. We recast generative condition selection as an inference-time resource-allocation problem. We propose two dynamic budget allocators: a joint Global Sequential Monte Carlo (SMC) formulation that steers and allocates compute across configurations concurrently, and a decoupled approach adapting Batched Successive Elimination (BaSE). Empirically, these dynamic allocators increase the yield of designable candidates per GPU-hour nearly 5$\times$ without sacrificing diversity across distinct therapeutic targets and generative configurations.

---


### 226. [Decision-Focused Learning for Cyber-Physical Risk-Aware Power Grid Operations](https://arxiv.org/abs/2610.13853)

**<font color=#1a73e8>作者：</font>** Ayesha Siddiqua Dina, Ebisa D.Wollega, Afzal Hossain Sohag  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Power grid cyber-physical security requires intrusion detection methods that account for the operational consequences of detection errors. However, the existing intrusion detection approaches primarily focus on the predictive performance of learning algorithms, while downstream operational costs are often optimized independently, which can lead to inferior operational performance. To help alleviate this problem, we propose a novel optimization-learning cyber-physical-risk-informed framework that communicates iteratively to minimize power grid operational costs. This framework translates machine learning prediction errors into power grid operational cyber-physical-risk costs. Experimental results on two power grid operation datasets, Industrial Control System (ICS) Cyber Attack and Sherlock, show that the proposed approach improves power grid operation costs compared with the traditional approach.

---


### 227. [Event-based Action Recognition by Pre-Training on Multi-Frame Representations](https://arxiv.org/abs/2610.13856)

**<font color=#1a73e8>作者：</font>** Emma Norrby, Tomas Wilkinson, Per Nyblom 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action recognition is a crucial task in domains like robotics, patient monitoring, or surveillance. Recently, event-based action recognition has attracted much attention due to the event camera's ability to capture fast motions and its improved privacy over conventional vision cameras. While frame-based event representations work well for short event sequences, their discriminative ability declines sharply with longer and more complex event sequences. In this work, we introduce a multi-frame representation that greatly improves recognition performance over its single-frame counterpart. We adopt a masked auto-encoding framework to pre-train a Vision Transformer using a sparsity-aware masking algorithm and token selection mechanism to improve downstream performance and control computational complexity. We also introduce multiple mask tokens for the decoder with a position-aware attention mechanism, leading to further improved performance. Our proposed method shows impressive performance for challenging long-duration and complex event sequences, yielding state-of-the-art performance on THU-EACT-50 CHL and DailyDVS-200.

---


### 228. [Revisiting the Task of Building Damage Assessment by Satellite Imaging](https://arxiv.org/abs/2610.13857)

**<font color=#1a73e8>作者：</font>** Anthony Cioppa, Virgile Blua, Sébastien Piérard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural disasters such as earthquakes, tropical storms, and floods cause extensive damage to buildings, and rapid, reliable damage maps are essential to guide emergency response. Automating this task, referred to as building damage assessment (BDA), from satellite imagery, has become an active research topic at the intersection of remote sensing, computer vision, and machine learning, particularly since supervised deep learning methods were shown to outperform earlier handcrafted approaches. Yet, despite a decade of intense activity and the release of several large-scale datasets, the field lacks a shared foundation. This chapter revisits the task of BDA from first principles, organized around three pillars: data, evaluation, and methods. We first clarify the candidate task for- mulations and argue for a sensor-agnostic, instance-based definition that tolerates missing pre-event imagery. We then review existing datasets along the axes of sensing modality, temporal configuration, and geographic coverage. On the evaluation side, we show that prevailing practices, largely based on a single aggregate score, are theoretically fragile, and we lay the foundations of a more informative, ranking-based, multi-score protocol. We further review methods ranging from task-specific deep networks to recent Earth observation foundation models, noticing that generalization to unseen events and regions remains an open difficulty. Finally, we discuss how these elements can inform the organization of a BDA challenge, including cross-validation, challenge, and private data-sharing setups designed to build trust between developers and users.

---


### 229. [Make It Flow: Animating Water in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2610.13860)

**<font color=#1a73e8>作者：</font>** Kjell Keune, Florian Hahlbohm, Jannis Möller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explicit 3D scene representations such as 3D Gaussian Splatting (3DGS) have recently enabled high-quality, real-time novel view synthesis. However, these methods assume static scenes, limiting realism in the presence of dynamic phenomena ubiquitous in real-world environments. While coherent motion (e.g., humans or vehicles) can be captured and reconstructed, high-frequency effects such as flowing water remain intractable under casual capture conditions, where dense multi-view, high-speed acquisition is not feasible. We present a method to animate water in static 3DGS scenes, enabling visually plausible motion without requiring dynamic capture or physical simulation. Our approach estimates 2D optical flow from reference images or model renderings and lifts it into a consistent 3D Eulerian motion field. We propose a cinemagraph-inspired algorithm that applies this motion field to deform Gaussian primitives, producing temporally seamless looping animations. The resulting representation retains real-time rendering performance, significantly enhances perceptual realism, and preserves free-viewpoint navigation within the scene. We evaluate our method on a newly captured dataset of in-the-wild waterfall scenes and demonstrate clear improvements over prior work in dynamic Gaussian splatting and 3D cinemagraph generation in visual quality and computational efficiency.

---


### 230. [Partially Informed Stochastic Optimization via Zeroth-Order Residual Tracking](https://arxiv.org/abs/2610.13871)

**<font color=#1a73e8>作者：</font>** El Mahdi Chayti, Alireza Mirrokni, Martin Jaggi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many optimization problems provide direct access to only part of the gradient, while the remaining component must be inferred from function evaluations. This structure arises in performative prediction, performative reinforcement learning, and bilevel optimization with a black-box lower level. We introduce Partially Informed Stochastic Optimization (PISO), which combines the available gradient component with a running estimate of the residual. By centring each zeroth-order observation on this estimate, PISO makes the variance due to random probing depend on the tracking error rather than the residual's magnitude. This yields a randomized sketch iteration with an explicit contraction mechanism and a principled interpretation of momentum. For smooth nonconvex objectives, we establish convergence guarantees that depend on the residual's variation and initial magnitude, without requiring a uniform bound on the unavailable gradient component. With independently sampled function evaluations and Gaussian or spherical probes, PISO attains leading function-evaluation complexities of \(O(d^{2}\varepsilon^{-6})\) under Lipschitz gradients and \(O(d^{2}\varepsilon^{-5})\) under an additional Lipschitz-Hessian assumption. These rates require only one probe direction, two function samples, and one known-component sample per update. The analysis also quantifies how batching trades observations for fewer deployments. Across five settings, PISO variants improve on the tested baselines with comparable oracle access in three, reach a comparable solution faster in bilevel routing, and perform best among methods without response-model derivatives in performative reinforcement learning.

---


### 231. [Tracking the Invisible: Self-Supervised Wheel Track Detection with Thermal-RGB Fusion](https://arxiv.org/abs/2610.13872)

**<font color=#1a73e8>作者：</font>** Yiming Yang, Jeremy P. Bos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate detection of drivable area is essential for autonomous driving and advanced driver assistance systems. While state-of-the-art methods focus on general traversability estimation, they prove inadequate for snow-covered roads where following existing wheel tracks offers crucial advantages: improved traction, predictable vehicle dynamics, and verified path stability. To address this, we propose a low-cost, self-supervised approach detecting safety-critical wheel tracks using synchronized RGB-I (RGB + Long-Wave Infrared) imagery. Our method automatically generates training labels by projecting future wheel trajectories from recorded GNSS data. A neural network is designed to identify wheel tracks with the 4-channel RGB-I images from challenging, white-out road surfaces. Experimental results demonstrate the effectiveness of our approach in visually monotonous and featureless adverse environment, offering a robust and cost-effective alternative for winter autonomy. The newly introduced ThermalTrack dataset is available at: this https URL.

---


### 232. [Prediction Is Not a Sufficient Memory State](https://arxiv.org/abs/2610.13881)

**<font color=#1a73e8>作者：</font>** Robert Jenkinson Alvarez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A memory that reproduces every current prediction may still have forgotten how to learn from the next observation. We characterize this distinction for exact cumulative learning and attention. For smooth convex residual losses with unrestricted real features and labels, a continuous recurrent state of fixed dimension exists exactly when the loss is polynomial. With ordinary, unweighted observations, degree $D$ requires precisely $r=\binom{d+D}{D}-1$ coordinates; even among histories with one fixed current predictor, exactly $r-d$ coordinates can remain necessary for continuation. Nonpolynomial losses have unbounded requirements on such equal-prediction histories. Bounded scalar logistic examples retain this obstruction after fixing any finite derivative jet. For ridge regression, the hidden evidence is the design matrix: the exact state costs $dp+d(d+1)/2$, versus $dp$ for the predictor. On a well-conditioned zero-prediction family, optimal $B$-bit compression has average one-update error of order $d^{-1}2^{-2B/s_d}$, $s_d=d(d+1)/2$, even with arbitrary randomized codes. Kernel attention gives a second exact closure classification. The results identify what future updates reveal, rather than proposing a new regression algorithm or asserting trained-model gains.

---


### 233. [RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics](https://arxiv.org/abs/2610.13889)

**<font color=#1a73e8>作者：</font>** Weiliang Chen, Song Liao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via Execution Dynamics), a retrieval framework that combines robust semantic matching with dynamic reliability adaptation. RATED employs a frozen dual-encoder with contrastive fine-tuning for semantic matching, and a lightweight contextual bandit module that re-ranks candidates based on real-time execution feedback. This design enables rapid adaptation to runtime tool failures without expensive model retraining. We introduce EcoAgent, a benchmark of 5,172 real-world tools and over 210,000 query-tool pairs for offline retrieval and dynamic reliability evaluation. Experimental results demonstrate that RATED achieves a 52.2% relative MRR improvement over the ToolLLM API retriever on real-world queries, and reduces fault selection rate from 86.2% to 2.9% under severe API outage scenarios with a 30% failure rate, while incurring negligible latency overhead of less than 1 ms over encode-only inference. The code and dataset are available at this https URL.

---


### 234. [Beyond the Snowflakes: Disentangling Weather Effects from Confounding Meta-Factors in LiDAR Object Detection](https://arxiv.org/abs/2610.13891)

**<font color=#1a73e8>作者：</font>** Yiming Yang, Jeremy P. Bos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Light Detection and Ranging (LiDAR) is critical for autonomous perception, yet its performance is known to degrade in adverse weather. While existing literature models snow as atmospheric noise that degrades performance, our granular evaluation on the WADS-3D and CADC datasets reveals a counter-intuitive phenomenon: detection accuracy consistently improves as snow intensity increases. Through ablation study and meta-information analysis, we reconcile this by confirming that while falling snow acts as noise, its negative impact is outweighed by a dominant, concurrent factor: significantly increased object point count. We hypothesize that this object point count boost acts as a geometric enhancement, driven by snow accumulation increasing vehicle surface area and a shift from specular to diffuse reflectance. Our findings demonstrate that evaluating perception systems using broad weather-severity bins without accounting for correlated object-level data can lead to misleading conclusions about detector robustness. We conclude that accurate evaluation requires decoupling atmospheric noise from surface accumulation effects and outline future research to validate these physical models. The WADS-3D dataset is available at: this https URL.

---


### 235. [Nimbus Studio reproduces reference BCI decoding pipelines: a validation study on public benchmarks across protocols and paradigms](https://arxiv.org/abs/2610.13894)

**<font color=#1a73e8>作者：</font>** Sergey Musienko  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Nimbus Studio is a visual pipeline platform for brain-computer interface (BCI) experiments: researchers assemble preprocessing, feature extraction, decoding, and evaluation over public benchmark datasets or their own recordings, with cross-validated evaluation protocols (including leave-one-subject-out), BIDS export, and bring-your-own Python model classes. Whether its numbers can be trusted is a fair question for any such platform. We answer it with a parity study: six standard BCI decoding pipelines (CSP+LDA, Riemannian MDM, tangent-space logistic regression through the platform's bring-your-own-code node, P300 xDAWN+LDA, and the deep ShallowConvNet and EEGNet) were evaluated on three public datasets (motor-imagery BNCI-2014-001/004; P300 BNCI-2014-009) under two protocols (per-subject session holdout and pooled leave-one-subject-out cross-validation via the platform's planned-CV driver), once through Nimbus Studio's execution engine and once through independent, hand-written reference implementations built directly on MNE-Python, scikit-learn, pyriemann, and braindecode. Every deterministic pipeline matched the reference exactly (0.00 points maximum difference across all 54 session-holdout subject-runs and all CSP/MDM grouped-CV folds), including pipelines through the bring-your-own-code node and the CV orchestration; the remaining grouped-CV cells agree to floating-point precision (worst case 0.06 points, about one trial per fold). The stochastic deep models agreed within seed-to-seed training variability, estimated with multi-seed reruns on each side. The platform's execution engine therefore computes the same science as the reference stack across protocols, paradigms, and extensibility surfaces. The platform is available at this https URL, and the complete harness and per-subject results accompany this paper for independent verification.

---


### 236. [Structural Automata for Neural Semantic Parsing](https://arxiv.org/abs/2610.13896)

**<font color=#1a73e8>作者：</font>** Xiao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural semantic parsers generate meaning representations token by token, yet well-formedness depends on references, scope, and graph relations that unfold during generation. Constrained decoding prevents locally invalid tokens but does not guarantee that a valid prefix can be completed within a fixed output-length limit. We investigate structural automata at three stages of DRS parsing (decoding, post hoc processing, and training) and additionally evaluate decoding on AMR. For decoding, we introduce accepting-path decoding (APD), which maintains a verified completion within the remaining length limit and follows the model's preferred token whenever that token can also be completed. APD guarantees an accepted output without retracting tokens. Under tight length limits, it improves Smatch++ over local masking by 5.1 and 2.4 points on DRS and by 6.4 and 3.2 points on AMR, comparable to rollback under the same limit, which retracts tokens. For post hoc processing, invalid outputs concentrate on the same inputs: eight unconstrained samples yield no valid output for 10.2% of inputs with limited training data, compared with 0.4% with full data, where filtering comes within 0.2 Smatch++ points of APD. For training, penalizing automaton-rejected tokens improves development Smatch++ by 3.6-11.0 points after 10% of training, but this advantage diminishes as cross-entropy alone reduces the probability assigned to rejected tokens from 14% to below 2% within the first sixth of training with limited data.

---


### 237. [Revisiting Tabular Deep Regression: Objectives and the Limits of Global Early Stopping](https://arxiv.org/abs/2610.13909)

**<font color=#1a73e8>作者：</font>** Danil Rudenko, Georgii Bulgakov, Nikolay Kartashev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While deep learning models for tabular data have recently received significant research attention, the choice of objective functions for regression tasks remains an understudied degree of freedom. Several lines of research offer alternatives to the standard Mean Squared Error (MSE), but differences in datasets, backbones, and evaluation protocols make their practical benefits difficult to compare. In this work, we address this gap by performing a systematic re-evaluation of regression objectives across a broad collection of established tabular datasets and multiple neural backbones. Our comparison reveals that many proposed objectives provide limited or inconsistent gains over a properly tuned MSE baseline, while quantile loss yields consistent aggregate improvements over MSE across the tested backbones. We then identify a limitation that remains even with this strong objective: regions with different levels of target noise can reach their best predictive performance at different training epochs. Consequently, a single global early-stopping checkpoint can impose a compromise between uncertainty regions, even when the objective can represent heteroskedastic target distributions. Motivated by this limitation, we introduce a heteroskedasticity-aware extension of quantile loss that uses input-dependent label smoothing as a potential remedy and improves over quantile loss on several backbones. Overall, our results provide a modern empirical picture of regression objectives for tabular deep learning and highlight how differences in optimal stopping times across uncertainty regions can limit the effectiveness of global early stopping. The code is available at this https URL.

---


### 238. [RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://arxiv.org/abs/2610.13912)

**<font color=#1a73e8>作者：</font>** Taoyong Cui, Pinxian Zeng, Wanghan Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predictive world models to guide action and learning-data selection. Observed feedback drives policy or workflow improvement and conditional world-model adaptation, while component and compatibility checks govern the retention of updated policy-model pairs. Across diverse computational and scientific domains, RSI-Anything demonstrates substantial gains. In code repair, with the coder fixed, success increases from 26.3% with a static verifier to 29.2% through predictive selection and 31.2% after world-model adaptation, at comparable test usage. Graphical user interface (GUI) evaluations showed higher task completion, while average actions decrease by 39.4%. Across five successive policy versions, laboratory-planning scores more than double from 21.80% to 46.01%. In reaction optimization, RSI-Anything achieves 96.15% mean best observed yield versus 82.16% for Bayesian optimization under the same 40-experiment budget. An end-to-end immune-science application further connects workflow evolution and predictive modeling with therapeutic hypothesis generation. These results demonstrate how predictive world models and retained system updates enable recursive improvement across diverse environments.

---


### 239. [Where to Look Matters: Rethinking Sub-Volume Sampling in 3D Medical Self-supervised Learning](https://arxiv.org/abs/2610.13915)

**<font color=#1a73e8>作者：</font>** Junkai Liu, Le Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning on 3D medical images commonly relies on random sub-volume sampling during pretraining. However, random cropping implicitly treats all spatial regions as equally worth observing, despite anatomical priors and spatial redundancy that make regions inherently unequal in their value for representation learning. To this end, we first show through controlled crop-quality manipulations that better sub-volumes lead to better downstream transfer, revealing the observation policy as an overlooked bottleneck in 3D medical SSL. Motivated by this finding, we revisit sub-volume sampling as a \emph{where-to-look} problem. We propose \textbf{\method}, a plug-and-play framework that replaces random cropping with an offline coarse-to-fine probe bank guided by \textit{anatomy-awareness}, \textit{informativeness}, and \textit{diversity}. We instantiate \method as a lightweight \lite variant using geometric and image-statistical cues, and a diagnostic \feat variant using frozen visual features, to examine whether lightweight volume-intrinsic priors suffice or richer semantic cues reliably provide additional value. Extensive experiments across multiple 3D medical SSL backbones and downstream tasks demonstrate that \method-\lite consistently improves transfer performance over random sampling. Mechanistic analyses further attribute these gains to more anatomically plausible and informative observations, reduced spatial redundancy, more efficient learning dynamics, and more structured representations.

---


### 240. [Designing Protein Structures from Natural Language](https://arxiv.org/abs/2610.13917)

**<font color=#1a73e8>作者：</font>** Joseph Lee, Yanjing Li, Bo Qiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central challenge in de novo protein design is generating proteins with desired structural and functional properties. Existing design models typically require a dedicated input representation for each property, limiting the design objectives they support. We develop Prompteina, the first all-atom structure generation model that supports new and broader design objectives specified in natural language, analogous to text-to-image generation. To train Prompteina, we construct Prompteina-Data, a paired text--protein structure dataset of 1.8M structures and 50M+ captions describing global and residue-specific structural and functional properties. We adapt Proteina-Complexa, a pretrained structure generation model, through text-conditioned pretraining and finetuning that aligns residues with their corresponding text. Prompteina outperforms baselines on 15 of 18 structural properties and generates proteins that more closely match descriptions of their intended functions. In binder design, it leads baselines on at least 13 of 20 targets and improves interface confidence by 14\% over the strongest baseline. With iterative in silico feedback, Prompteina's gain over non-iterative generation is 57\% larger than the next-best baseline on the hardest targets. Finally, we experimentally validate Prompteina designs against GM2A, a target with no reported de novo binders. We identify nine binders, with the strongest at an apparent $K_{\mathrm{D}}$ of 107 nM. These results establish natural language as an effective and powerful conditioning interface for protein structure generation.

---


### 241. [KL Before and After Mixing: A Round-Complexity Separation in Parallel Sampling](https://arxiv.org/abs/2610.13924)

**<font color=#1a73e8>作者：</font>** Tianyi Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A parallel sampler can choose at random which coordinates to generate together. For a target $p$ and the output law $q_U$ of a schedule $U$ drawn afresh for each output, we compare the schedule-averaged divergence $\mathbb{E}_U D_{\mathrm{KL}}(p\|q_U)$ with the output-law divergence $D_{\mathrm{KL}}(p\|\mathbb{E}_U q_U)$, in nats. Rounds commit independent draws from exact conditional marginals frozen at the round's start, each output's schedule is drawn before sampling from a finite mixture of schedules, and every scheduled round is charged. For the uniform distribution on binary strings of even length $n$ with $n/2$ ones, the least expected number of rounds at a fixed tolerance $\varepsilon>0$ is $\Theta_\varepsilon((\log n)^2)$ under the first criterion but $(e^{-\varepsilon}+o(1))\log_2\ln n$ under the second, and the double-logarithmic order is attainable with the same round count on every run. For this target, a count-state recursion gives the exact least output divergence at every round cap over all causal randomized policies. The separation extends to weighted fixed-count targets with bounded weight ratios and quota fractions bounded away from zero and one, without permutation symmetry, and to the full-support Beta$(1,1)$--Bernoulli target, where the sharp expected cost under the output-law criterion is $(e^{-\varepsilon}/2+o(1))\log_2\log_2n$, attained with rare $n$-round runs. Prior work implies the order of the schedule-averaged cost on the balanced target and its $O_\varepsilon((\log n)^2)$ upper bounds on both extensions.

---


### 242. [AI Models Can Provably Hide Arbitrary Capabilities](https://arxiv.org/abs/2610.13928)

**<font color=#1a73e8>作者：</font>** Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under cryptographic assumptions, even given full access to model weights, extending prior work from hiding fixed strings to arbitrary computations. We implement our proof of concept constructions in PyTorch and evaluate elicitation through fine-tuning, weight noising, gradient-based trigger search, and latent adversarial training on a small chemical reaction prediction task - a proxy for CBRN-relevant capabilities. Our results demonstrate resistance to these methods and, together with our cryptographic guarantees, reveal a limit of elicitation-based capability audits. We release our models to support the improvement of defenses.

---


### 243. [Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback](https://arxiv.org/abs/2610.13941)

**<font color=#1a73e8>作者：</font>** Yucheng Yang, Xiaoxiao Sun, Shusheng Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal diffusion transformers (MMDiTs) allow the evolving image to update internal text representations through joint attention. These representations then guide subsequent image updates, raising a question: does this feedback help correct deviations from the prompt, or preserve them? We find that image-to-text (I2T) feedback can preserve the objects and attributes already represented in the evolving image, including errors. Transplanting I2T messages can rescue failures or disrupt successes. At matched intervention strengths, suppressing the influence of I2T feedback improves generation, whereas opposite controls degrade it. These findings motivate Semantic Feedback Guidance (SFG), which suppresses the influence of I2T feedback by guiding away from an auxiliary branch that strengthens this feedback and weakens text-to-image conditioning. The in-place variant, iSFG, directly suppresses I2T feedback and strengthens text-to-image conditioning, requiring no extra model evaluations. Temporal interventions motivate running the SFG branch during the first 20% of image sampling steps, requiring about $1.2\times$ the base NFE without classifier-free guidance (CFG). Experiments across three image-generation backbones show gains in alignment and preference-model scores. On FLUX, adding SFG to CFG raises GenEval from $0.6661$ to $0.7479$; on SD3.5M, iSFG adds $+1.33$ HPSv2.1 over CFG at zero extra NFE. The control also transfers to text-to-video and image-to-video generation, improving VBench scores. Code is available at this https URL.

---


### 244. [Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark](https://arxiv.org/abs/2610.13947)

**<font color=#1a73e8>作者：</font>** Xudong Cai, Ruijie Zhu, Haoliang Shang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we study physically grounded articulated 3D asset generation---moving the goal from reproducing how objects look to capturing how they move and function. Inspired by the literature on procedural and agentic generation, we present Artisan, a system that extends the latest method Articraft by introducing a multi-agent pipeline with physical simulation feedback, enabling comprehensive attributes beyond geometry, appearance, and physically plausible articulation, such as collision-free motion, stability under gravity, and accurate mass and material properties. Furthermore, we construct a unified benchmark spanning four key aspects: spatial fidelity, physical plausibility, downstream task performance, and overall quality. The benchmark encompasses 100 reference assets from ArtVIP and LightWheel, 50 stability prompts, and 50 ABO objects with reference masses, with protocols evaluating various metrics. Through extensive evaluation of more than 10 representative models, Artisan achieves competitive spatial fidelity while attaining the lowest collision rates and highest stability rates among the evaluated methods. Together, our system and benchmark establish insights for advancing 3D generation towards physically plausible, functionally usable assets.

---


> [!TIP]
> 当前位于：**201-244**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-244**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
