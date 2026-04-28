# 📦 其他研究 | 2026年04月29日

> 本类共 **437** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-437](./part-09.md)

---

### 1. [HalalBench: A Multilingual OCR Benchmark for Food Packaging Ingredient Extraction](https://arxiv.org/abs/2604.22754)

**<font color=#1a73e8>作者：</font>** Hasan Arief  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> No standardized benchmark exists for evaluating OCR on food packaging, despite its critical role in automated halal food verification. Existing benchmarks target documents or scene text, missing the unique challenges of ingredient labels: curved surfaces, dense multilingual text, and sub-8pt fonts. We present HalalBench, the first open multilingual benchmark for food packaging OCR, comprising 1,043 images (50 real, 993 synthetic) with 36,438 annotations in COCO format spanning 14 languages. We evaluate four engines: docTR achieves F1=0.193, ML Kit 0.180, EasyOCR 0.167, while all fail on Japanese (F1=0.000). A clustering ablation shows 36% F1 improvement from our post-processing algorithm. We validate findings through HalalLens (this https URL), a production halal scanner serving 20+ countries. Dataset and code are released under open licenses.

---


### 2. [The Imbalanced User-AI Relationships as an Ethical Failure of Front-End Design in Healthcare AI](https://arxiv.org/abs/2604.22767)

**<font color=#1a73e8>作者：</font>** Maureen Mghambi Mwadime  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Ethical discourse on AI in healthcare has focused predominantly on back-end concerns such as bias, fairness and explainability, while the front-end interface, where patients and clinicians actually encounter AI outputs, remains under explored. This paper identifies imbalanced user-AI relationships as a distinct class of front-end ethical failure: patients are rendered highly visible to AI systems through data inference, yet cannot understand, question or influence how they are represented. Through the concept of asymmetric legibility and a chat-based telemedicine case, we show how design choices e.g., default recommendations, restricted inputs and suppressed uncertainty, undermine agency, clinician judgment and human oversight even where systems are technically accurate. We propose reciprocity as a design orientation and offer interventions for more balanced, participatory user-AI relationships in healthcare.

---


### 3. [An Intelligent Fault Diagnosis Method for General Aviation Aircraft Based on Multi-Fidelity Digital Twin and FMEA Knowledge Enhancement](https://arxiv.org/abs/2604.22777)

**<font color=#1a73e8>作者：</font>** Zhihuan Wei, Yang Hu, Xinhang Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fault diagnosis of general aviation aircraft faces challenges including scarce real fault data, diverse fault types, and weak fault signatures. This paper proposes an intelligent fault diagnosis framework based on multi-fidelity digital twin, integrating four modules: high-fidelity flight dynamics simulation, FMEA-driven fault injection, multi-fidelity residual feature extraction, and large language model (LLM)-enhanced interpretable report generation. A digital twin is constructed using the JSBSim six-degree-of-freedom (6-DoF) flight dynamics engine, generating 23-channel engine health monitoring data via semi-empirical sensor synthesis equations. A three-layer fault injection engine based on failure mode and effects analysis (FMEA) models the physical causal propagation of 19 engine fault types. A multi-fidelity residual computation framework comprising paired-mirror residuals and GRU surrogate prediction residuals is proposed: the high-fidelity path obtains clean fault deviation signals using nominal mirror trajectories with identical initial conditions, while the low-fidelity path achieves online real-time residual computation through a multi-step prediction GRU surrogate model. A 1D-CNN classifier performs end-to-end diagnosis of 20 fault classes. An LLM diagnostic report engine enhanced with FMEA knowledge fuses classification results, residual evidence, and domain causal knowledge to generate interpretable natural language reports. Experiments show the paired-mirror residual scheme achieves a Macro-F1 of 96.2% on the 20-class task, while the GRU surrogate scheme achieves 4.3x inference acceleration at only 0.6% performance cost. Comparison across 24 schemes reveals that residual feature quality contributes approximately 5x more to diagnostic performance than classifier architecture, establishing the "residual quality first" design principle.

---


### 4. [The Spectral Lifecycle of Transformer Training: Transient Compression Waves, Persistent Spectral Gradients, and the Q/K--V Asymmetry](https://arxiv.org/abs/2604.22778)

**<font color=#1a73e8>作者：</font>** Yi Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present the first systematic study of weight matrix singular value spectra \emph{during} transformer pretraining, tracking full SVD decompositions of every weight matrix at 25-step intervals across three model scales (30M--285M parameters). We discover three phenomena: \textbf{(1)~Transient Compression Waves:} stable rank compression propagates as a traveling wave from early to late layers, creating a dramatic gradient that peaks early then \emph{reverses} -- late layers eventually over-compress past early layers. \textbf{(2)~Persistent Spectral Gradients:} the power-law exponent~$\alpha$ develops a permanent depth gradient forming a non-monotonic inverted-U in deeper models, with peaks shifting toward earlier layers as depth increases. \textbf{(3)~Q/K--V Functional Asymmetry:} value/output projections compress uniformly while query/key projections carry the full depth-dependent dynamics. The dissociation between transient compression and persistent spectral shape reveals that \emph{rank and spectral shape encode fundamentally different information about training}. We formalize this as a two-timescale dynamical model and derive scaling laws ($\Delta\alpha \propto L^{0.26}$, $R^2{=}0.99$). We validate on nine models across three families (custom, GPT-2, Pythia; 30M--1B parameters; 8--36 layers), demonstrate that $\alpha$ predicts layer importance ($\rho{=}0.69$--$0.84$, $p{<}0.02$), and show that spectral-guided pruning outperforms Last-N heuristics by $1.1{\times}$--$3.6{\times}$ across seven models in two families (GPT-2 124M--774M, Pythia 160M--1B), with worst-vs-best gaps up to $23.7{\times}$ confirming the causal role of spectral structure.

---


### 5. [BiTA: Bidirectional Gated Recurrent Unit-Transformer Aggregator in a Temporal Graph Network Framework for Alert Prediction in Computer Networks](https://arxiv.org/abs/2604.22781)

**<font color=#1a73e8>作者：</font>** Zahra Makki Nayeri, Mohsen Rezvani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proactive alert prediction in computer networks is critical for mitigating evolving cyber threats and enabling timely defensive actions. Temporal Graph Neural Networks (TGNs) provide a principled framework for modeling time-evolving interactions; however, existing TGN-based methods predominantly rely on unidirectional or single-mechanism temporal aggregation, which limits their ability to capture recursive, multi-scale temporal patterns commonly observed in real-world attack behaviors. In this paper, we propose BiTA, a Bidirectional Gated Recurrent Unit-Transformer Aggregator for temporal graph learning. Rather than introducing a deeper or higher-capacity model, BiTA redesigns the temporal aggregation function within the TGN framework by jointly encoding bidirectional sequential dependencies and long-range contextual relations over each node's temporal neighborhood. This aggregation strategy enables complementary temporal reasoning at different scales while preserving the original TGN memory and message-passing structure. We evaluate BiTA on real-world alert datasets, demonstrating significant improvements in key performance metrics such as area under the curve, average precision, mean reciprocal rank, and per-category prediction accuracy when compared to state-of-the-art temporal graph models. BiTA outperforms baseline methods under both transductive and inductive settings, highlighting its robustness and generalization capabilities in dynamic network environments. BiTA is a scalable and interpretable framework for real-time cyber threat anticipation, paving the way toward more intelligent and adaptive intrusion detection systems.

---


### 6. [Stochastic KV Routing: Enabling Adaptive Depth-Wise Cache Sharing](https://arxiv.org/abs/2604.22782)

**<font color=#1a73e8>作者：</font>** Anastasiia Filippova, David Grangier, Marco Cuturi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Serving transformer language models with high throughput requires caching Key-Values (KVs) to avoid redundant computation during autoregressive generation. The memory footprint of KV caching is significant and heavily impacts serving costs. This work proposes to lessen these memory requirements. While recent work has largely addressed KV cache reduction via compression and eviction along the temporal axis, we argue that the \emph{depth} dimension offers an orthogonal and robust avenue for optimization. Although prior research suggests that a full cache for every layer is redundant, implementing cross-layer cache sharing remains a practical challenge; existing methods typically suffer from reduced throughput or increased time-to-first-token. In this paper, we demonstrate that dropping a layer's cache offers efficient optimization without information loss. We propose a simple training approach: random cross-layer attention. During training, layers randomly choose to attend either to their own KV states or those of a preceding layer. This stochastic process adapts the model to be robust to various depth-wise cache sharing strategies, ensuring flexibility for unknown hardware constraints at deployment time. Our evaluations show that applying this scheme during pre-training or fine-tuning enables depth-wise cache sharing for various model families. Furthermore, for larger models in data-constrained settings, this approach is suggestive of a regularization-like effect, frequently preserving or improving performance while significantly reducing the cache's memory footprint.

---


### 7. [Learning Without Adversarial Training: A Physics-Informed Neural Network for Secure Power System State Estimation under False Data Injection Attacks](https://arxiv.org/abs/2604.22784)

**<font color=#1a73e8>作者：</font>** Solon Falas, Markos Asprou, Charalambos Konstantinou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State estimation is a cornerstone of power system control-center operations, and its robust operation is increasingly a cyber-physical security concern as modern grids become more digitalized and communication-intensive. Neural network-based approaches have gained attention as alternatives to conventional model-based state estimation methods. Physics-Informed Neural Networks (PINNs), which embed power-flow consistency into the learning objective, have shown improved accuracy over existing approaches. This work proposes a PINN-based model for Power System State Estimation (PSSE) that protects the estimation process against the stealth-constrained AC False Data Injection Attacks (FDIAs) considered in this study. The model is developed without adversarial training. Instead, a dynamic loss-weighting formulation based on homoscedastic uncertainty learns the relative scaling of supervised data-fit and physics-residual terms during training, reducing sensitivity to manual weight tuning. Robustness is evaluated on the IEEE 118-bus system using representative stealthy-FDIA families including state distortion, load redistribution, line overloading, and residual-constrained stealth corruption. Performance is measured using Mean Absolute Error (MAE) on voltage magnitudes and phase angles. Results demonstrate higher accuracy and stability than existing fixed-weight PINN variants.

---


### 8. [AutoCompress: Critical Layer Isolation for Efficient Transformer Compression](https://arxiv.org/abs/2604.22786)

**<font color=#1a73e8>作者：</font>** Archit Thorat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present AutoCompress, a transformer compression method motivated by an empirical finding: in small transformers, Layer 0 carries disproportionately high task-critical information, with an NTK-based importance score of 3.6 compared to a maximum of 0.054 for all other layers -- a gap of over 60x. Based on this finding, we propose Critical Layer Isolation (CLI), an architecture that protects Layer 0 at full dimensionality, compresses all intermediate layers through a learned bottleneck, and restores the full dimension at the final layer. Applied to GPT-2 Medium (354.8M parameters), CLI-GPT2 achieves 204.5 perplexity on WikiText-103 with only 143.8M parameters -- a 2.47x compression ratio and 59.5% parameter reduction. Crucially, an ablation study demonstrates that a uniform bottleneck baseline of comparable size achieves only 571.8 perplexity under identical training conditions, confirming that the architectural decision to protect Layer 0 -- rather than simply reducing model size -- is the primary driver of performance. Code and checkpoints are publicly available.

---


### 9. [Conformal PM2.5 Mapping Under Spatial Covariate Shift: Satellite-Reanalysis Fusion for Africa's Green Industrial Transition](https://arxiv.org/abs/2604.22787)

**<font color=#1a73e8>作者：</font>** Yaw Osei Adjei, Davis Opoku, Ephraim Abotsi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Africa's green industrialization imperative demands reliable infrastructure for monitoring air quality. We present a satellite-reanalysis PM2.5 fusion system trained on 2,068,901 records from 404 monitoring locations in 29 African countries (OpenAQ, 2017-2022), combining LightGBM with leakage-resistant spatial cross-validation and conformal prediction to quantify predictions and their geographic applicability limits. Under 5-fold location-grouped spatial cross-validation, LightGBM achieves RMSE = 30.83 +/- 5.07 ug/m3, MAE = 14.54 +/- 1.66 ug/m3, R2 = 0.134 +/- 0.023, and macro F1 = 0.336 +/- 0.018. This R2 is substantially below random-split benchmarks (>0.90) but reflects true geographic generalisation difficulty rather than model failure. Split conformal prediction targeting 90% marginal coverage reveals severe East Africa degradation (actual PICP = 65.3% vs. nominal 90%), consistent with medium-strength covariate shift (humidity KS = 0.2237, sat_pblh KS = 0.2558). We operationalise these findings through regional reliability flags (High/Medium/Low/Unreliable) and a monitor prioritisation score directing infrastructure expansion toward highest-burden unmonitored populations, directly supporting Africa's green industrial transition and SDGs 3.9, 7.1.2, 9, 11.6.2, and 13.

---


### 10. [Enabling users to work sustainably on shared institute computing resources](https://arxiv.org/abs/2604.22799)

**<font color=#1a73e8>作者：</font>** Niclas Eich, Johannes Erdmann, Martin Erdmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The VISPA project is a self-managed, mid-scale computing cluster that supports physics data analysis in research and teaching. Because the cluster is housed in a 1970s institute building with limited retrofit options, conventional efficiency upgrades would yield only minor energy savings. We therefore target sustainability primarily through user-centric measures. A monitoring system now records per-job energy consumption, while real-time data on the renewable share of the German power grid enable `green-window' scheduling. Users can query their individual energy consumption and carbon footprints, receive weekly reports, and tag jobs by project for aggregate accounting; memory records from previous runs help avoid oversubscription. All options are voluntary, fostering a cultural shift rather than imposing hard constraints. A simulation framework evaluates the potential impact of these measures. Together, the technological and behavioral interventions aim at medium- to long-term reductions in greenhouse-gas emissions by increasing resource awareness within the scientific community.

---


### 11. [See No Evil: Semantic Context-Aware Privacy Risk Detection for AR](https://arxiv.org/abs/2604.22805)

**<font color=#1a73e8>作者：</font>** Jialu Liu, Yao Li, Zhuoheng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Augmented reality (AR) systems pose unique privacy risks due to their continuous capture of visual data. Existing AR privacy frameworks lack semantic understanding of visual content, limiting their effectiveness in detecting context-dependent privacy risks. We propose PrivAR, which leverages vision language models (VLMs) with chain-of-thought prompting for contextual privacy risk detection in AR environments. PrivAR uses visual scene cues to infer potential sensitive information types, such as identifying password notes in office environments through contextual reasoning. PrivAR detects and obfuscates textual content, preventing exposure of sensitive information while preserving contextual cues necessary for VLM inference. Additionally, we investigate contextually-informed warning interfaces to enhance user privacy awareness. Experiments on a real-world AR dataset show that PrivAR achieves superior accuracy (81.48%) and F1-score (84.62%) compared to baselines, while reducing privacy leakage rate to 17.58%. User studies evaluating contextually-informed warning interfaces provide insights into effective privacy-aware AR design.

---


### 12. [FreqFormer: Hierarchical Frequency-Domain Attention with Adaptive Spectral Routing for Long-Sequence Video Diffusion Transformers](https://arxiv.org/abs/2604.22808)

**<font color=#1a73e8>作者：</font>** Haopeng Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-sequence video diffusion transformers hit a quadratic self-attention cost that dominates runtime and memory for very long token sequences. Most efficient attention methods use one approximation everywhere, yet video features are spectrally structured: low frequencies carry global layout and coarse motion; high frequencies carry texture and fine detail. We present FreqFormer, a frequency-aware heterogeneous attention framework. Token features are split into spectral bands with different operators: dense global attention on compressed low-frequency content, structured block-sparse attention on mid frequencies, and sliding-window local attention on high frequencies. A lightweight spectral routing network allocates heads across bands using layer statistics and the diffusion timestep, shifting compute toward global structure early in denoising and detail later. Cross-band summary tokens provide cheap residual exchange. FreqFormer is paired with a fused GPU execution plan that co-schedules dense, sparse, and local branches to cut kernel launches and memory traffic. We give a consistent complexity model, an orthonormal-decomposition view of approximation, and simulation-based systems numbers (throughput, arithmetic intensity, memory traffic, duration scaling). In simulations from 64K to 1M tokens, FreqFormer substantially reduces estimated attention FLOPs and KV-related memory traffic versus dense attention while keeping a hardware-friendly pattern, supporting spectrally structured heterogeneous attention as a practical direction for long-video diffusion transformers.

---


### 13. [WeatherSeg: Weather-Robust Image Segmentation using Teacher-Student Dual Learning and Classifier-Updating Attention](https://arxiv.org/abs/2604.22824)

**<font color=#1a73e8>作者：</font>** Zhang Zhang, Yifeng Zeng, Jinquan Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> WeatherSeg, an advanced semi-supervised segmentation framework, addresses autonomous driving's environmental perception challenges in adverse weather while reducing annotation costs. This framework integrates a Dual Teacher-Student Weight-Sharing Model (DTSWSM) that enables knowledge distillation from weather-affected images, and a Classifier Weight Updating Attention Mechanism (CWUAM) that dynamically adjusts classifier weights based on environmental attributes. Comprehensive evaluations demonstrate that WeatherSeg significantly outperforms baseline models in both accuracy and robustness across various weather conditions, including clear, rainy, cloudy, and foggy scenarios, establishing it as an effective solution for all-weather semantic segmentation in autonomous driving and related applications.

---


### 14. [SGP-SAM: Self-Gated Prompting for Transferring 3D Segment Anything Models to Lesion Segmentation](https://arxiv.org/abs/2604.22825)

**<font color=#1a73e8>作者：</font>** Zixuan Tang, Shen Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large segmentation foundation models such as the Segment Anything Model (SAM) have reshaped promptable segmentation in natural images, and recent efforts have extended these models to medical images and volumetric settings. However, directly transferring a 3D SAM-style model to lesion segmentation remains challenging due to (i) weak spatial representational capacity for small, irregular targets in intermediate features, and (ii) extreme foreground-background imbalance in 3D this http URL propose SGP-SAM, a self-gated prompting framework for efficient and effective transfer to 3D lesion segmentation. Our key component, the Self-Gated Prompting Module (SGPM), performs conditional multi-scale spatial enhancement: a lightweight multi-channel gating unit predicts whether the current features require additional multi-scale fusion, and only then activates a Multi-Scale Feature Fusion Block to enrich spatial context. To further address small-lesion learning, we design a Zoom Loss that up-weights lesion-focused supervision by combining Dice and a voxel-balanced focal this http URL on MSD Liver Tumor and MSD Brain Tumor (enhancing tumor) show consistent gains over strong transfer baselines based on SAM-Med3D. On MSD Liver Tumor, SGP-SAM improves mDice by 7.3% over fine-tuning.

---


### 15. [DGHMesh: A Large-scale Dual-radar mmWave Dataset and Generalization-focused Benchmark for Human Mesh Reconstruction](https://arxiv.org/abs/2604.22827)

**<font color=#1a73e8>作者：</font>** Rongxiao Guo, Qingchao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave (mmWave) radar has shown great potential for contactless, privacy-preserving, and robust human sensing, yet existing mmWave-based human mesh reconstruction (HMR) studies are still limited by the lack of benchmarks for generalization analysis under configuration shifts and fair comparison of different algorithms. To address the limitation, we present DGHMesh, a large-scale dual-radar mmWave dataset and generalization-focused benchmark for HMR. It contains data from 15 subjects performing 8 actions, with 360,000 synchronized frames collected from FMCW radar, SFCW radar, RGB images, and high-precision 3D HMR annotations. In addition, the dataset provides synchronized raw I/Q data from both radar modalities and accurately calibrated radar spatial positions. The benchmark is designed to evaluate HMR methods under diverse measurement configurations, including human position shifts, human orientation shifts, subarray size variations, and cross-subject settings. Based on DGHMesh, we also propose mmPTM, a query-based multi-radar fusion framework that jointly exploits point clouds and imaging tubes for HMR. Extensive experiments are conducted against representative baselines under different settings. The results demonstrate that mmPTM consistently achieves outstanding accuracy and competitive generalization capability across multiple sub-benchmarks, validating the effectiveness of multi-radar fusion and the practical value of the proposed dataset and benchmark for mmWave-based HMR research. DGHMesh and mmPTM are publicly available at this https URL complete benchmark and code will be released after paper publication)

---


### 16. [MetaEarth3D: Unlocking World-scale 3D Generation with Spatially Scalable Generative Modeling](https://arxiv.org/abs/2604.22828)

**<font color=#1a73e8>作者：</font>** Jinqi Cao, Zhiping Yu, Baihong Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent generative AI models have achieved remarkable breakthroughs in language and visual understanding. However, although these models can generate realistic visual content, their spatial scale remains confined to bounded environments, preventing them from capturing how geographic environments evolve across thousands of kilometers or from modeling the spatial structure of the large-scale physical world. This limitation poses a critical challenge for ultra-wide-area spatial intelligence in Earth observation and simulation, revealing a deeper gap in generative AI: progress has relied primarily on scaling model parameters and training data, while overlooking spatial scale as a core dimension of intelligence. Here, motivated by this missing dimension, we investigate spatial scale as a new scaling axis in foundation models and present MetaEarth3D, the first generative foundation model capable of spatially consistent generation at the planetary scale. Taking optical Earth observation simulation as a testbed, MetaEarth3D enables the generation of multi-level, unbounded, and diverse 3D scenes spanning large-scale terrains, medium-scale cities, and fine-grained street blocks. Built upon 10 million globally distributed real-world training images, MetaEarth3D demonstrates both strong visual realism and geospatial statistical realism. Beyond generation, MetaEarth3D serves as a generative data engine for diverse virtual environments in ultra-wide spatial intelligence. We argue that this study may help empower next-generation spatial intelligence for Earth observation.

---


### 17. [WebSerial Vision Training for Microcontrollers: A Browser-Based Companion to On-Device CNN Training](https://arxiv.org/abs/2604.22834)

**<font color=#1a73e8>作者：</font>** Jeremy Ellis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents webmcu-vision-web, a single-file, zero-install browser application for end-to-end TinyML vision model training and deployment on the Seeed Studio XIAO ESP32-S3 Sense (XIAO ML Kit, $15--40 USD). Acting as a browser-based companion to the on-device Arduino firmware of Paper 1 [1], it provides a private, fully local machine learning pipeline, from firmware flashing through image collection, CNN training, weight export, and live activation visualization, without any software installation beyond a Chromium-based browser. The system targets educators, small businesses, and researchers who need to train task-specific visual classifiers under their exact deployment conditions. Key capabilities include: in-browser firmware flashing via esptool-js; an SD card file browser with image preview and inline editing; this http URL live-sync for zero-recompile hyperparameter adjustment; webcam and ESP32 OV2640 camera image capture; this http URL CNN training completing a three-class run (~30 images per class, 20 epochs) in approximately 1 minute browser-side versus 9 minutes on-device, enabling a complete collect-train-deploy cycle in under 10 minutes; weight export as this http URL and myWeights.h; confusion matrix; and a live Conv2 activation heatmap streamed from the ESP32 during inference. No data leaves the local machine at any stage. A five-run consistency evaluation on the three-class reference problem (0Blank, 1Cup, 2Pen) demonstrates stable convergence with mean accuracy and standard deviation reported; all artefacts are released at the repository link below. The repository is a living template for LLM-assisted adaptation to new hardware and tasks. All source code is MIT-licensed at this https URL.

---


### 18. [ParkingScenes: A Structured Dataset for End-to-End Autonomous Parking in Simulation Scenes](https://arxiv.org/abs/2604.22835)

**<font color=#1a73e8>作者：</font>** Haonan Chen, Kaiwen Xiao, Bin Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous parking remains a critical yet challenging task in intelligent driving systems, particularly within constrained urban environments where maneuvering space is limited and precise control is essential. While recent advances in end-to-end learning have shown great promise, the lack of high-quality, structured datasets tailored for parking scenarios remains a significant this http URL address this gap, we present ParkingScenes, a comprehensive multimodal dataset specifically designed for end-to-end autonomous parking in simulated scenes. Built on the CARLA simulator, ParkingScenes features structured parking trajectories generated by a Hybrid A* planner and a Model Predictive Controller (MPC), providing accurate and reproducible supervision signals. The dataset includes 16 reverse-in and 6 parallel parking scenarios, each executed under two pedestrian conditions (present and absent), resulting in 704 structured episodes and approximately 105000 frames. Each scenario is repeated 16 times to ensure consistent coverage. Each frame contains synchronized data from four RGB cameras, four depth sensors, vehicle motion states, and Bird's-Eye View (BEV) representations, enabling rich multimodal fusion and context-aware learning. To demonstrate the utility of our dataset, we compare models trained on ParkingScenes with those trained on unstructured, manually collected simulation data under identical conditions. Results show significant improvements in performance, underscoring the effectiveness of structured supervision for robust and accurate parking policy learning. By releasing both the dataset and the collection framework, ParkingScenes establishes a scalable and reproducible benchmark for advancing learning-based autonomous parking systems. The dataset and collection framework will be released at: this https URL

---


### 19. [AgentRVOS for MeViS-Text Track of 5th PVUW Challenge: 3rd Method](https://arxiv.org/abs/2604.22836)

**<font color=#1a73e8>作者：</font>** Deshui Miao, Chao Yang, Chao Tian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report describes a Ref-VOS pipeline centered on Sa2VA and organized with explicit agent roles. The key idea is that Sa2VA should provide the first dense semantic hypothesis, while an agent loop decides whether that hypothesis should be accepted, revised, or refined. The pipeline starts with a target-presence judgment stage. If the referred object does not exist in the video, the system directly outputs zero masks. Otherwise, Sa2VA receives the video and referring prompt and produces a coarse mask trajectory over the full video. This trajectory is treated as a semantic prior rather than a final answer. A planner agent decomposes the query, temporal partition agents identify informative blocks, scout agents search for anchor frames, and refinement agents convert reliable Sa2VA masks into boxes and points for SAM3 propagation. A critic scores candidate trajectories, a reflection controller repairs weak hypotheses, and a collaboration controller reconciles multiple agent branches. The result is a Ref-VOS system in which Sa2VA is responsible for dense grounded understanding, while the agent layer handles presence verification, temporal search, confidence-aware revision, and final mask refinement.

---


### 20. [OAMVOS:2nd Report for 5th PVUW MOSE Track](https://arxiv.org/abs/2604.22837)

**<font color=#1a73e8>作者：</font>** Deshui Miao, Xingsen Huang, Yameng Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> SAM-based dense trackers provide strong short-term mask propagation but remain fragile under long occlusion, fast motion, viewpoint change, and distractors. The problem is especially severe for small objects, where a few incorrect memory updates can dominate later predictions. This report presents an occlusion- and reappearance-aware extension of DAM4SAM that improves memory control rather than changing the backbone. The method augments the original SAM3 tracker with four ingredients: a reliability-aware tracking state machine, branch-based recovery, delayed DRM promotion, and a selective policy for native SAM3 memory selection. During stable tracking, the model follows the original single-path propagation process. Once confidence drops, the tracker enters an ambiguous or recovery mode, maintains a small set of candidate branches, and commits memory only after a branch is reconfirmed. For small-object disappearance and reappearance, native memory selection is temporarily bypassed so older anchors remain accessible. In addition, the first conditioning frame is explicitly preserved, and the conditioning-memory budget is moderately enlarged to improve long-gap recovery. The resulting design keeps DAM4SAM efficient in easy cases while improving robustness in sequences dominated by occlusion and reappearance.

---


### 21. [From Skeletons to Pixels: Few-Shot Precise Event Spotting via Representation and Prediction Distillation](https://arxiv.org/abs/2604.22839)

**<font color=#1a73e8>作者：</font>** Zhong Han Ervin Yeoh, Jiang Kan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise Event Spotting (PES) is essential in fast-paced sports such as tennis, where fine-grained events occur within very short temporal windows. Accurate frame-level localization is challenging because of motion blur, subtle action differences, and limited annotated data. We study two complementary distillation strategies for few-shot PES: Adaptive Weight Distillation (AWD), a prediction-level method that adaptively weights teacher supervision on unlabeled data, and Annealed Multimodal Distillation for Few-Shot Event Detection (AMD-FED), a representation-level framework that transfers robust skeleton knowledge into visual modalities through annealed pseudo-labeling. Both methods use multimodal distillation to improve generalization under limited supervision. We evaluate them on F3Set-Tennis(sub) under few-shot k-clip settings, where they consistently outperform single-modality baselines and prior PES approaches. After observing the stronger performance of representation-level distillation on tennis, we further validate AMD-FED on a second sports dataset, Figure Skating, where it also shows robust performance in the k-clip scenario. These results highlight the effectiveness of multimodal distillation, especially representation-level transfer, for few-shot precise event spotting.

---


### 22. [ATTN-FIQA: Interpretable Attention-based Face Image Quality Assessment with Vision Transformers](https://arxiv.org/abs/2604.22841)

**<font color=#1a73e8>作者：</font>** Guray Ozgur, Tahar Chettaoui, Eduarda Caldeira 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Image Quality Assessment (FIQA) aims to assess the recognition utility of face samples and is essential for reliable face recognition (FR) systems. Existing approaches require computationally expensive procedures such as multiple forward passes, backpropagation, or additional training, and only recent work has focused on the use of Vision Transformers. Recent studies highlighted that these architectures inherently function as saliency learners with attention patterns naturally encoding spatial importance. This work proposes ATTN-FIQA, a novel training-free approach that investigates whether pre-softmax attention scores from pre-trained Vision Transformer-based face recognition models can serve as quality indicators. We hypothesize that attention magnitudes intrinsically encode quality: high-quality images with discriminative facial features enable strong query-key alignments producing focused, high-magnitude attention patterns, while degraded images generate diffuse, low-magnitude patterns. ATTN-FIQA extracts pre-softmax attention matrices from the final transformer block, aggregate multi-head attention information across all patches, and compute image-level quality scores through simple averaging, requiring only a single forward pass through pre-trained models without architectural modifications, backpropagation, or additional training. Through comprehensive evaluation across eight benchmark datasets and four FR models, this work demonstrates that attention-based quality scores effectively correlate with face image quality and provide spatial interpretability, revealing which facial regions contribute most to quality determination.

---


### 23. [Unified Multi-Foundation-Model Slide Representation for Pan-Cancer Recognition and Text-Guided Tumor Localization](https://arxiv.org/abs/2604.22846)

**<font color=#1a73e8>作者：</font>** Tianyang Wang, Ziyu Su, Abdul Rehman Akbar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The expanding ecosystem of pathology foundation models has produced powerful but fragmented tile-level representations, limiting their use in clinical tasks that require unified slide-level reasoning and interpretable linkage to clinically meaningful information. We present ASTRA, a pan-cancer framework that integrates heterogeneous foundation-model representations into a shared slide-level representation space and semantically grounds that space using structured pathology annotation fields, including classification category, cancer type, and anatomic site. ASTRA combines sparse mixture-of-experts contextualization, masked multi-model reconstruction, and contrastive alignment to structured pathology prompts to learn slide representations that support 4-category classification, 3-class solid tumor typing, 16-class cancer typing, and text-guided tumor localization without pixel-level supervision. Developed on a CHTN cohort of 10,359 whole-slide images (WSIs) spanning 16 tumor types, ASTRA consistently improves pan-cancer classification across four pathology foundation-model backbones, achieving up to 97.8% macro-AUC for 4-category classification, 99.7% for 3-class solid tumor typing, and 99.2% for 16-class cancer typing. For tumor localization, ASTRA achieves a mean Dice of 0.897 on an annotated in-domain CHTN subset (n = 380) spanning 16 cancer types and 0.738 on an external TCGA cohort (n = 1,686) spanning four cancer types. These results demonstrate that minimal structured pathology annotation fields derived from slide-level metadata can provide effective semantic supervision for unified slide representation learning, enabling both pan-cancer prediction and weakly supervised tumor localization within a single framework.

---


### 24. [Dream-Cubed: Controllable Generative Modeling in Minecraft by Training on Billions of Cubes](https://arxiv.org/abs/2604.22847)

**<font color=#1a73e8>作者：</font>** Tim Merino, Sam Earle, Ryunosuke Iwai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Dream-Cubed, a large-scale dataset of Minecraft worlds at voxel resolution, and a family of models using cubes as powerful compositional units for efficient generation of interactive 3D environments. Dream-Cubed comprises tens of billions of tokens from a carefully curated mixture of procedural biome terrain and high-quality human-authored maps. We use this dataset to conduct the first large-scale study of 3D diffusion models for voxel generation, analyzing discrete and continuous diffusion formulations, data compositions, and architectural design choices. Our models operate directly in the space of blocks, enabling efficient and semantically grounded generation while supporting interactive user workflows such as inpainting and outpainting from user-authored blocks. To quantitatively evaluate our models, we adapt the FID metric to assess semantic differences between real and generated world renderings, and validate generation quality through a human preference study. We release the full dataset, code, and all our pretrained models, which we hope will provide a foundation for future research in efficient generative modeling for structured, interactive 3D environments.

---


### 25. [LunarDepthNet: Generation of Digital Elevation Models using Deep Learning and Monocular Satellite Images](https://arxiv.org/abs/2604.22848)

**<font color=#1a73e8>作者：</font>** Aaranay Aadi, Jai Gopal Singla, Amitabh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent times have seen an increase in demand of high quality Digital Elevation Models (DEMs) for the lunar surface, because they are highly important for studying the moon and planning future missions. However, there is an evident lack of detailed elevation data on the Moon. To overcome this limitation, this study proposes a novel deep learning method that estimates and generates a surface elevation map directly from monocular images of the surface. The dataset used comprises of the Chandrayaan-2 Terrain Mapping Camera (TMC) images with their corresponding Digital Terrain Models (DTMs). The study proposes LunarDepthNet, which comprises of a UNet architecture to generate DEMS. It incorporates an EfficientNet encoder and custom layers to correctly learn how the light shadows on the surface relate to the actual elevation values. A combined loss function was also utilized to keep the terrain details accurate and smooth. During validation, the model showed a stable loss convergence of 12%. It achieved a mean nRMSE of 0.437 and an MAE of 4.5m in the testing stage. These results prove the model can generate dependable elevation maps from single orbital images, which are quite useful in regions of the moon where stereo-images are not available.

---


### 26. [Accelerating New Product Introduction for Visual Quality Inspection via Few-Shot Diffusion-Based Defect Synthesis](https://arxiv.org/abs/2604.22850)

**<font color=#1a73e8>作者：</font>** Serkan Hamdi Güğül, Kemal Levi, Burak Acar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial visual inspection systems often suffer from a severe scarcity of labeled defect data, particularly during the early stages of New Product Introduction (NPI). This limitation hinders the deployment of robust supervised detectors precisely when automated quality control is most needed. We present an end-to-end generative framework for high-fidelity, few-shot defect synthesis that enables both in-domain augmentation and cross-domain transfer. Our approach disentangles defect morphology from background appearance by combining masked textual inversion for defect representation learning, noise-blended conditioned generation for surface-aware synthesis, and gradient-aware post-processing for seamless visual integration. We evaluate the framework in two practically relevant settings: few-shot data augmentation, where synthetic samples enrich a small set of real defects, and zero-shot adaptation, where defects learned from a source domain are transferred to a novel target surface without any real target-domain defect examples. Using RF-DETR as the downstream detector, we show that the proposed pipeline substantially narrows the domain gap on a private industrial dataset. In the few-shot setting, synthetic augmentation improves mAP from 78.8% to 83.3%. In the zero-shot setting, synthetic domain adaptation improves mAP from 65.0% to 85.1%. These results demonstrate that high-fidelity defect synthesis can meaningfully accelerate NPI by enabling effective inspection models before sufficient real defect data has been collected.

---


### 27. [FastAT Benchmark: A Comprehensive Framework for Fair Evaluation of Fast Adversarial Training Methods](https://arxiv.org/abs/2604.22853)

**<font color=#1a73e8>作者：</font>** Chao Pan, Xin Yao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fast Adversarial Training (FastAT) seeks to achieve adversarial robustness at a fraction of the computational cost incurred by standard multi-step methods such as PGD-AT. Although numerous FastAT techniques have been proposed in recent years, fair comparison among them remains elusive. Existing benchmarks and public leaderboards typically permit diverse model architectures, varying training configurations, and external data sources, making it unclear whether reported improvements reflect genuine algorithmic advances or merely more favorable experimental conditions. To address this problem, we introduce the FastAT Benchmark, a controlled evaluation framework built on three core design principles: unified architecture requirements, standardized training settings, and strict prohibition of external or synthetic data. The benchmark implements over twenty representative FastAT methods within a single codebase, enabling direct and reproducible comparison. Each method is assessed through a dual-metric evaluation framework that measures both adversarial robustness (accuracy under PGD, AutoAttack, and CR Attack) and computational cost (GPU training time and peak memory footprint). Comprehensive experiments on CIFAR-10, CIFAR-100, and Tiny-ImageNet provide reliable baseline measurements and reveal that well-designed single-step methods can match or surpass PGD-AT robustness at substantially lower cost, while no single method dominates across all evaluation dimensions. The complete benchmark, including source code, configuration files, and experimental results, is publicly available to support transparent and fair evaluation of future FastAT research.

---


### 28. [MAE-Based Self-Supervised Pretraining for Data-Efficient Medical Image Segmentation Using nnFormer](https://arxiv.org/abs/2604.22854)

**<font color=#1a73e8>作者：</font>** R. M. Krishna Sureddi, T. Satyanarayana Murthy, Nomula Varsha Reddy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer architectures, including nnFormer,have demonstrated promising results in volumetric medical image segmentation by being able to capture long-range spatial interactions. Although they have high performance, these models need large quantities of labeled training data and are also likely to overfit and become training unstable. This is a serious practical problem because it is not only time-consuming but also expensive to obtain medical images that are annotated by experts. Moreover, fully supervised traditional training pipelines do not take advantage of the available large amounts of unlabeled medical imaging data that can be easily obtained in the clinics. We have solved these drawbacks by advancing the efficiency of the nnFormer with a self-supervised pretraining framework, which is based on the Masked Autoencoders (MAE). In this method, the model is pretrained on unlabeled volumetric medical images to reconstruct randomly masked parts of the input. This allows the encoder to learn meaningful anatomical and structural representations . The encoder is then further fine-tuned on a labeled dataset on the downstream segmentation task. Conducted Experiment shows that the offered method leads to a higher segmentation performance on the count of Dice score, a quicker convergence rate on the course of the fine-tuning procedure, and a superior generalization on the basis of limited labeled data . These findings validate that self-supervised learning combined with transformer-based segmentation models is an appropriate approach to the problem of data shortage in medical image analysis.

---


### 29. [Attention-Augmented YOLOv8 with Ghost Convolution for Real-Time Vehicle Detection in Intelligent Transportation Systems](https://arxiv.org/abs/2604.22856)

**<font color=#1a73e8>作者：</font>** Syed Sajid Ullah, Muhammad Zunair Zamir, Ahsan Ishfaq 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate vehicle detection is a critical component of autonomous driving, traffic surveillance, and intelligent transportation systems. This paper presents an enhanced YOLOv8n-based model that integrates the Ghost Module, Convolutional Block Attention Module (CBAM), and Deformable Convolutional Networks v2 (DCNv2) to improve detection performance. The Ghost Module reduces feature redundancy through efficient feature generation, CBAM refines feature representation via channel and spatial attention, and DCNv2 enhances adaptability to geometric variations in vehicle structures. Evaluated on the KITTI dataset, the proposed model achieves 95.4% mAP@0.5, representing an 8.97% improvement over the baseline YOLOv8n, along with 96.2% precision, 93.7% recall, and a 94.93% F1-score. Comparative analysis against seven state-of-the-art detectors demonstrates consistent superiority across key performance metrics, while ablation studies validate the individual and combined contributions of the integrated modules. By addressing feature redundancy, attention refinement, and spatial adaptability, the proposed approach offers a robust and computationally efficient solution for vehicle detection in diverse and complex traffic environments.

---


### 30. [IoT-Enhanced CNN-Based Labelled Crack Detection for Additive Manufacturing Image Annotation in Industry 4.0](https://arxiv.org/abs/2604.22857)

**<font color=#1a73e8>作者：</font>** Mohsen Asghari Ilani, Yaser Mike Banad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents an IoT-enhanced deep learning framework for automated crack detection in Additive Manufacturing (AM) surfaces using convolutional neural networks (CNNs). By integrating IoT-enabled real-time monitoring, high-resolution imaging, and edge computing, the system enables continuous in-situ defect detection and classification. Real-time data acquisition supports immediate CNN-based analysis, improving both accuracy and efficiency in AM quality control. The framework supports supervised and semi-supervised learning, enabling robust performance on large, sparsely annotated datasets. Using LabelImg for annotation and OpenCV for preprocessing, the system achieves 99.54% accuracy on 14,982 images, with 96% precision, 98% recall, and a 97% F1-score. Dataset balancing and augmentation significantly improve generalization, increasing accuracy from 32% to 99%. Beyond detection, the framework establishes a linkage between AM process parameters, defect formation, and surface topology, supporting predictive analytics and defect mitigation. Aligned with Industry 4.0, it incorporates Digital Twin (DT) technology for real-time process simulation, predictive maintenance, and adaptive control. Key contributions include an IoT-based monitoring system using edge devices (Raspberry Pi 4B), an optimized CNN with model quantization and batch processing reducing inference latency by 47%, and an MQTT-based low-latency data streaming system with 5G connectivity, lowering transmission overhead by 35%. DT integration further enables predictive defect analysis and dynamic adjustment of AM parameters. This work advances intelligent AM quality control by providing a scalable, high-accuracy, and low-latency framework. Future directions include multimodal data fusion, hybrid architectures, and enhanced Digital Twin simulations for AI-driven defect prevention.

---


### 31. [A Digital Pathology Resource for Liver Cancer Quantification with Datasets, Benchmarks, and Tools](https://arxiv.org/abs/2604.22858)

**<font color=#1a73e8>作者：</font>** Ying Xiao, Shimiao Tang, Xitong Ling 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Liver cancer, especially hepatocellular carcinoma (HCC), imposes a substantial global disease burden. Accurate diagnosis and prognostic assessment directly influence treatment selection and patient survival, and pathological examination remains the gold standard for liver cancer diagnosis. Identifying diverse tissue components and pathological subtypes on histopathology slides is crucial for estimating postoperative recurrence risk and overall prognosis. However, most publicly available resources are still provided at the whole-slide image (WSI) level, and well-annotated datasets for fine-grained tissue component identification in liver cancer are scarce, which hinders reproducible model development and the deployment of quantitative analysis tools. To address this gap, we release HepatoBench, a patch-level image database for liver cancer with annotations for seven key tissue categories. Based on HepatoBench, we train and open-source a deep learning classification model as a tissue recognition tool. Furthermore, we train a WSI-level tumor/non-tumor segmentation model to automatically localize lesion regions across entire slides. By integrating the patch-level tissue classifier with the WSI-level segmentation model, we build HepatoQuant, an end-to-end, disease-specific regional quantification tool for liver cancer, enabling a unified workflow from WSIs to tissue composition parsing and quantitative statistics. We also open-source HepatoBench, the benchmarking protocol, and supporting tools, providing a solid foundation for automated regional quantification and fair method comparison in liver cancer pathology.

---


### 32. [MeshLAM: Feed-Forward One-Shot Animatable Textured Mesh Avatar Reconstruction](https://arxiv.org/abs/2604.22865)

**<font color=#1a73e8>作者：</font>** Yisheng He, Steven Hoi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce MeshLAM, a feed-forward framework for one-shot animatable mesh head reconstruction that generates high-fidelity, animatable 3D head avatars from a single image. Unlike previous work that relies on time-consuming test-time optimization or extensive multi-view data, our method produces complete mesh representations with inherent animatability from a single image in a single forward pass. Our approach employs a dual shape and texture map architecture that simultaneously processes mesh vertices and texture map with extracted image features from a shared transformer backbone, allowing for coherent shape carving and appearance modeling. To prevent mesh collapse and ensure topological integrity during feed-forward deformation, we propose an iterative GRU-based decoding mechanism with progressive geometry deformation and texture refinement, coupled with a novel reprojection-based texture guidance mechanism that anchors appearance learning to the input image. Extensive experiments demonstrate that our method outperforms state-of-the-art approaches in reconstruction quality, animation capability, and computational efficiency. Project page at this https URL.

---


### 33. [Risk Models as Mediating Artifacts: A Postphenomenological Analysis of the CIIM Framework in Cybersecurity Practice](https://arxiv.org/abs/2604.22866)

**<font color=#1a73e8>作者：</font>** Rommel Salas-Guerra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This article applies postphenomenological theory to the field of cybersecurity risk management, arguing that formal risk models function as mediating artifacts that shape how security practitioners or analysts perceive, interpret, and act on threats. Based on Don Ihde's taxonomy on human-technology relationships and Peter-Paul Verbeek's extended mediational framework, the Contextual and Multimodal Hazard Impact Index (CIIM), an original dynamic risk model presented as an empirical case study, is analyzed. CIIM is formally defined as CIIM(t+1) = [A T(t) V(t) E(t)] / R(t) + {alpha} P(t), where the condition R(t) 0 is not treated as a computational artifact to be smoothed out, but as a genuine systemic collapse that signals singularity. This design choice constitutes a deliberate phenomenological move, allowing organizational fragility to be made visible in a way that previous CVSS-based and probabilistic models conceal. In addition, we examine how CIIM's time projection (t+1) and its hybrid machine learning architecture, combining LSTM/GRU, XGBoost, and Reinforcement Learning, produce a new form of technological intentionality that structures practitioner or analyst attention and ethical deliberation. The article concludes by establishing implications for the ethical design of cybersecurity instrumentation and for the post-phenomenological methodology itself, proposing the concept of 'phenomenology of collapse' as a contribution to the empirical philosophy of technology.

---


### 34. [Probing Visual Planning in Image Editing Models](https://arxiv.org/abs/2604.22868)

**<font color=#1a73e8>作者：</font>** Zhimu Zhou, Yanpeng Zhao, Qiuyu Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual planning represents a crucial facet of human intelligence, especially in tasks that require complex spatial reasoning and navigation. Yet, in machine learning, this inherently visual problem is often tackled through a verbal-centric lens. While recent research demonstrates the promise of fully visual approaches, they suffer from significant computational inefficiency due to the step-by-step planning-by-generation paradigm. In this work, we present EAR, an editing-as-reasoning paradigm that reformulates visual planning as a single-step image transformation. To isolate intrinsic reasoning from visual recognition, we employ abstract puzzles as probing tasks and introduce AMAZE, a procedurally generated dataset that features the classical Maze and Queen problems, covering distinct, complementary forms of visual planning. The abstract nature of AMAZE also facilitates automatic evaluation of autoregressive and diffusion-based models in terms of both pixel-wise fidelity and logical validity. We assess leading proprietary and open-source editing models. The results show that they all struggle in the zero-shot setting, finetuning on basic scales enables remarkable generalization to larger in-domain scales and out-of-domain scales and geometries. However, our best model that runs on high-end hardware fails to match the zero-shot efficiency of human solvers, highlighting a persistent gap in neural visual reasoning.

---


### 35. [Avionic Main Fuel Pump Simulation and Fault-Diagnosis Benchmark](https://arxiv.org/abs/2604.22869)

**<font color=#1a73e8>作者：</font>** Felix Leonhard Janzen, Lukas Moddemann, Alexander Diedrich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many cyber-physical systems, especially in critical applications such as aeroplanes, data to train anomaly detection and diagnosis algorithms is lacking due to data protection issues and partial observability. To combat this inherent lack of data, we introduce a high-fidelity, physics-informed co-simulation of a common aircraft main-fuel-pump system modelled in \textsc{MATLAB/Simulink Simscape Fluids}. We also describe its generated time-series data with health and fault mode annotations. To show feasibility of our benchmark, we apply an unsupervised Recurrent Variational Autoencoder (RNN-VAE) for anomaly detection and a SOM-VAE for operating mode discretization, trained to separate healthy and faulty conditions.

---


### 36. [Towards Understanding the Expressive Power of GNNs with Global Readout](https://arxiv.org/abs/2604.22870)

**<font color=#1a73e8>作者：</font>** Maurice Funk, Daumantas Kojelis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the expressive power of message-passing aggregate-combine-readout graph neural networks (ACR-GNNs). Particularly, we focus on the first-order (FO) properties expressible by this formalism. While a tight logical characterisation remains a difficult open question, we make two contributions towards answering it. First, we show that sum aggregation and readout suffice for GNNs to capture FO properties that cannot be expressed in the logic C2 on both directed and undirected graphs. This strengthens known results by Hauke and Wał{\k e}ga (2026) where aggregation and readout functions are specially crafted for the task. Second, we identify two natural ways of restoring characterisability (with regard to C2) for ACR-GNNs. One option is to limit local aggregation (without imposing restrictions on global readout), whilst the second is to run ACR-GNNs over graphs of bounded degree (but unbounded size). In both cases, the FO properties captured by GNNs are exactly those definable by a formula in graded modal logic with global counting modalities. Our results thus establish an innate lower- and upper-bound in terms of how far (fragments of) C2 can be taken to characterise GNNs, and imply that is indeed the unbounded interaction of aggregation and readout that pushes the logical expressive power of GNNs above C2.

---


### 37. [Vision-Based Lane Following and Traffic Sign Recognition for Resource-Constrained Autonomous Vehicles](https://arxiv.org/abs/2604.22872)

**<font color=#1a73e8>作者：</font>** Md Tanjemul Islam, Md Rafiul Kabir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles (AVs) rely on real-time perception systems to understand road environments and ensure safe navigation. However, implementing reliable perception algorithms on resource-constrained embedded platforms remains challenging due to limited computational resources. This paper presents a lightweight vision-based framework that integrates lane detection, lane tracking, and traffic sign recognition for embedded autonomous vehicles. A computationally efficient threshold-based lane segmentation method combined with perspective transformation and histogram-based curvature estimation is used for robust lane tracking under varying illumination conditions. A rule-based steering controller generates steering commands to maintain stable vehicle navigation. For traffic sign recognition, two lightweight convolutional neural networks (CNNs), EfficientNet-B0 and MobileNetV2, are evaluated using a custom dataset captured from the vehicle's onboard camera. Experimental results show that the system achieves real-time performance while maintaining accurate lane tracking with only 3.16% maximum offset RMSE. EfficientNet-B0 achieves a high offline classification accuracy of 98.77% on the test dataset, while achieving 90% accuracy during real-time on-device deployment, outperforming MobileNetV2 in both settings. MobileNetV2, however, offers slightly faster inference and lower computational cost. These results highlight the effectiveness of lightweight vision-based perception pipelines for resource-constrained autonomous driving applications.

---


### 38. [TexOCR: Advancing Document OCR Models for Compilable Page-to-LaTeX Reconstruction](https://arxiv.org/abs/2604.22880)

**<font color=#1a73e8>作者：</font>** Chengye Wang, Lin Fu, Zexi Kuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing document OCR largely targets plain text or Markdown, discarding the structural and executable properties that make LaTeX essential for scientific publishing. We study page-level reconstruction of scientific PDFs into compilable LaTeX and introduce TexOCR-Bench, a benchmark, and TexOCR-Train, a large-scale training corpus, for this task. TexOCR-Bench features a multi-dimensional evaluation suite that jointly assesses transcription fidelity, structural faithfulness, and end-to-end compilability. Leveraging TexOCR-Train, we train a 2B-parameter model, TexOCR, using supervised fine-tuning (SFT) and reinforcement learning (RL) with verifiable rewards derived from LaTeX unit tests that directly enforce compilability and referential integrity. Experiments across 21 frontier models on TexOCR-Bench show that existing systems frequently violate key document invariants, including consistent section structure, correct float placement, and valid label-reference links, which undermines compilation reliability and downstream usability. Our analysis further reveals that RL with verifiable rewards yields consistent improvements over SFT alone, particularly on structural and compilation metrics.

---


### 39. [MTServe: Efficient Serving for Generative Recommendation Models with Hierarchical Caches](https://arxiv.org/abs/2604.22881)

**<font color=#1a73e8>作者：</font>** Xin Wang, Chi Ma, Shaobin Chen 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative recommendation (GR) offers superior modeling capabilities but suffers from prohibitive inference costs due to the repeated encoding of long user histories. While cross-request Key-Value (KV) cache reuse presents a significant optimization opportunity, the massive scale of individual user states creates a storage explosion that far exceeds physical GPU limits. We propose MTServe, a hierarchical cache management system that virtualizes GPU memory by leveraging host RAM as a scalable backup store. To bridge the I/O gap between tiers, MTServe introduces a suite of system-level optimizations, including a hybrid storage layout, an asynchronous data transfer pipeline, and a locality-driven replacement policy. On both public and production datasets, MTServe delivers up to 3.1* speedup while maintaining near-perfect hit ratios (>98.5%).

---


### 40. [Predicting Wind Loads on Container Ships in Harbor Environments through Multi-Fidelity Modeling](https://arxiv.org/abs/2604.22882)

**<font color=#1a73e8>作者：</font>** Matilde Fiore, Andrea Bresciani, Miguel Alfonso Mendez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern container ships face higher wind loads due to increased windage areas, making accurate predictions of wind loads essential for mooring design. Existing empirical models, largely developed for container ships with smaller windage areas and simpler geometrical configurations than those of modern large-scale vessels, often lack accuracy and do not account for the influence of nearby structures. This study proposes a multi-fidelity surrogate modelling framework for the prediction of wind-load coefficients, combining empirical correlations with simplified and detailed CFD models for ships in open-sea and harbor environments. The approach relies on recursive co-kriging to consistently fuse information across fidelity levels, enabling accurate predictions at a reduced computational cost. A sensitivity analysis is used to identify the most influential geometric parameters, and the resulting reduced parameter space is explored through sequential sampling to efficiently construct the training database.
The surrogate models are validated over a wide range of loading configurations and for two distinct harbor environments. The results demonstrate that the multi-fidelity approach significantly improves prediction accuracy compared to single-fidelity models, while substantially reducing the reliance on high-fidelity simulations. In particular, the proposed framework captures the dependence of wind loads on key geometric parameters and consistently outperforms traditional empirical correlations, providing a robust and efficient tool for engineering applications.

---


### 41. [NeuroAPS-Net: Neuro-Anatomically Aware Point Cloud Representation for Efficient Alzheimer's Disease Classification](https://arxiv.org/abs/2604.22883)

**<font color=#1a73e8>作者：</font>** Towhidul Islam, Mufti Mahmud  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease (AD) is a progressive neurodegenerative disorder and a major cause of dementia. Structural MRI is widely used to analyze AD-related brain atrophy; however, most deep learning methods rely on computationally expensive 3D convolutional neural networks (CNNs), limiting deployment in resource-constrained settings. This work introduces two main contributions. First, we propose a pipeline that converts T1-weighted MRI into anatomically informed 2D point clouds using Anatomical Priority Sampling (APS), producing ADNI-2DPC, the first neuroanatomically labeled MRI-derived point cloud dataset. Second, we present NeuroAPS-Net, a lightweight geometric deep learning model that incorporates anatomical priors via region-aware feature encoding and ROI token aggregation. Experiments on ADNI-2DPC demonstrate that NeuroAPS-Net achieves competitive classification accuracy while significantly reducing inference latency and GPU memory compared to state-of-the-art point cloud methods. These results highlight the potential of anatomically guided point cloud learning as an efficient and interpretable alternative to voxel-based CNNs for AD classification.

---


### 42. [Federated Cross-Modal Retrieval with Missing Modalities via Semantic Routing and Adapter Personalization](https://arxiv.org/abs/2604.22885)

**<font color=#1a73e8>作者：</font>** Hefeng Zhou, Xuan Liu, Sicheng Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated cross-modal retrieval faces severe challenges from heterogeneous client data, particularly non-IID semantic distributions and missing modalities. Under such heterogeneity, a single global model is often insufficient to capture both shared cross-modal knowledge and client-specific characteristics. We propose RCSR, a personalization-friendly federated framework that integrates prototype anchoring, retrieval-centric semantic routing, and optional client-specific adapters. Built on a frozen CLIP backbone, RCSR leverages lightweight shared adapters for global knowledge transfer while supporting efficient local personalization. Prototype anchoring helps unimodal clients align with global cross-modal semantics, and a server-side semantic router adaptively assigns aggregation weights based on retrieval consistency to mitigate alignment drift during heterogeneous updates. Extensive experiments on MS-COCO, Flickr30K, and other benchmarks show that RCSR consistently improves global retrieval accuracy and training stability, while further enhancing client-level retrieval performance, especially for clients with incomplete modalities. Code is available at this https URL.

---


### 43. [Breaking Degradation Coupling: A Structural Entropy Guided Decoupled Framework and Benchmark for Infrared Enhancement](https://arxiv.org/abs/2604.22886)

**<font color=#1a73e8>作者：</font>** Pu Li, Huafeng Li, Yafei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal infrared image enhancement aims to restore high-quality images from complex compound degradations. Existing all-in-one approaches typically employ a single shared backbone to handle diverse degradations, which causes gradient interference and parameter competition. To address this, we propose a Structural Entropy-Guided Decoupled (SEGD) Framework. Unlike unified modeling paradigms, SEGD decomposes compound degradations into independent sub-processes and models them in a divide-and-conquer manner through Degradation-Specific Residual Modules (DRMs). Each DRM focuses on residual estimation for a specific degradation, enabling task decoupling while remaining jointly trainable, which mitigates parameter contention. A Degradation-Aware Evidential Network further estimates degradation type and intensity, providing priors that adaptively regulate DRM restoration strength. To handle compound cases, DRMs are composed in varying orders to form multiple restoration paths, from which the most informative features are aggregated under a structural-entropy criterion, yielding decoder-ready representations with structural fidelity and degradation awareness. Integrating divide-and-conquer restoration, evidential perception, and entropy-guided adaptation, SEGD achieves fine-grained and interpretable enhancement. We also construct a nighttime TIR benchmark for evaluation under real low-light conditions. Experimental results demonstrate that SEGD surpasses state-of-the-art methods while achieving higher efficiency with fewer parameters.

---


### 44. [StackFeat RL: Reinforcement Learning over Iterative Dual Criterion Feature Selection for Stable Biomarker Discovery](https://arxiv.org/abs/2604.22892)

**<font color=#1a73e8>作者：</font>** A. Yermekov, D.A. Herrera-Martí  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature selection in high-dimensional genomic data ($d \gg n$) demands methods that are simultaneously accurate, sparse, and stable. Existing approaches either require manual threshold specification (mRMR, stability selection), produce unstable selections under data perturbation (Lasso, Boruta), or ignore biological structure entirely. We introduce StackFeat-RL, a meta-learning framework that optimises the hyperparameters of an iterative dual-criterion feature selection algorithm via REINFORCE policy gradients. The dual criterion, requiring both coefficient consistency and selection frequency, guards against two failure modes missed by single-criterion methods, while iterative accumulation provides convergence guarantees via the law of large numbers.
On COVID-19 miRNA data (GSE240888, 332 features) and three Alzheimer's disease classification tasks (GSE84422, 13237 genes; Normal vs.\ Possible, Probable, and Definite AD), StackFeat-RL achieves the highest predictive accuracy among all evaluated methods, including ElasticNet, Boruta, mRMR, and stability selection, while requiring 3--4$\times$ fewer features.
Keywords: feature selection, reinforcement learning, REINFORCE, elastic net, biomarker discovery, Alzheimer's disease, dual-criterion selection, protein interaction networks

---


### 45. [Reconstructive Authority Model: Runtime Execution Validity Under Partial Observability](https://arxiv.org/abs/2604.22898)

**<font color=#1a73e8>作者：</font>** Marcelo Fernandez - TraslaIA  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous systems increasingly operate under partial observability where execution-relevant state is never fully accessible. Existing governance mechanisms -- trusted execution environments, oracle-signed state proofs, cryptographic attestation -- enforce the integrity of computation and state projections. We show this is structurally insufficient: an authenticated projection of state is necessary but never sufficient for execution validity.
We introduce the Reconstructive Authority Model (RAM), which separates integrity from coverage. RAM defines a reconstruction gate that reasons over an explicit coverage envelope -- comprising proven state, declared assumptions, and an acknowledged unobservable residual -- and permits execution only when coverage is adequate for the action class. When coverage is insufficient, RAM narrows privileges dynamically or fails closed. Attestation proves trust in measurement; RAM proves adequacy of what is measured.
We formalize RAM, prove necessity via two theorems (attestation insufficiency and RAM necessity) and three corollaries, and present a hybrid RAM+Attestation architecture with privilege-narrowing. Synthetic experiments (N=100,000, seed=42) show RAM achieves zero invalid execution rates at all coverage levels. Attestation-based systems exhibit IER=0.423 at low coverage and IER=0.233 even at full coverage, the latter arising from undefined-state handling failures undetectable by integrity checks alone.
This reframes execution validity as a coverage reconstruction problem, distinct from and complementary to integrity guarantees provided by attestation.

---


### 46. [Module Lattice Security (Part II): Module Lattice Reduction via Optimal Sign Selection](https://arxiv.org/abs/2604.22900)

**<font color=#1a73e8>作者：</font>** Ming-Xing Luo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We extend the CDPR lattice reduction algorithm from ideal to module lattices, leveraging the trace orthogonality of the power basis to decompose the module into rank-1 submodules and applying CDPR independently to each. This base module reduction achieves a Hermite factor $\exp(\tilde{O}(\sqrt{n}))$ matching the ideal case, with a module reduction factor $O(1)$ independent of the rank, under a balance hypothesis automatically satisfied for MLWE-distributed bases. To control precision, we introduce CRT-scaled rounding at totally split primes, reducing the Gram-Schmidt rounding error and yielding a bounded-precision implementation. We further reformulate the CDPR sign-selection subproblem as a mixed-integer linear program, determining the optimal balanced discrepancy to be a universal constant $\delta^*\approx 0.4407$. All results build on the class number one condition $h_k^+=1$ established in Part I of this series.

---


### 47. [Accelerating Frequency Domain Diffusion Models with Error-Feedback Event-Driven Caching](https://arxiv.org/abs/2604.22901)

**<font color=#1a73e8>作者：</font>** Dong Liu, Haisheng Wang, Yanxuan Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models achieve remarkable success in time series generation. However, slow inference limits their practical deployment. We propose E$^2$-CRF (Error-Feedback Event-Driven Cumulative Residual Feature caching) to accelerate frequency domain diffusion models. Our method exploits two structural properties: (1) spectral localization, where signal energy concentrates in low frequencies, and (2) mirror symmetry, which halves the effective frequency dimension. E$^2$-CRF uses a closed-loop error-feedback system that adaptively caches transformer KV features across diffusion steps. We trigger recomputation using event-driven residual dynamics instead of fixed schedules. Our method selectively recomputes high-energy or rapidly-changing tokens while reusing cached features for stable high-frequency components. E$^2$-CRF achieves ~2.2 speedup while maintaining sample quality. We demonstrate effectiveness on 5 datasets. Our caching strategy naturally aligns with the diffusion process's structure-to-detail progression. We include sufficient-condition error and complexity bounds under standard regularity assumptions (Appendix), alongside empirical validation. Our code is available at this https URL and is also integrated in this https URL.

---


### 48. [On the Complementarity of Quantum and Classical Features: Adaptive Hybrid Quantum-Classical Feature Fusion for Breast Cancer Classification](https://arxiv.org/abs/2604.22903)

**<font color=#1a73e8>作者：</font>** Yasmin Rodrigues Sobrinho, João Renato Ribeiro Manesco, João Paulo Papa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The integration of quantum machine learning with classical deep learning offers promising avenues for medical image analysis by mapping data into high-dimensional Hilbert spaces. However, effectively unifying these distinct paradigms remains challenging due to common optimization asymmetries. In this paper, a novel hybrid quantum-classical architecture for breast cancer diagnosis based on a dual-branch feature-extraction pipeline is proposed. Our framework extracts and unifies complementary representations from classical models and quantum circuits, exploring both trainable and deterministic (non-trainable) quantum paradigms. To integrate these embeddings, three progressive feature fusion strategies are introduced: Static Hybrid Fusion (SHF) for offline extraction, Dynamic Hybrid Fusion (DHF) for end-to-end co-adaptation, and a novel Temperature-Scaled Hybrid Fusion (TSHF). The TSHF strategy incorporates a learnable scalar, inspired by multimodal learning, that dynamically balances hybrid gradient dynamics and resolves optimization bottlenecks. Empirical validation on the BreastMNIST dataset confirms our hypothesis that unifying diverse feature representations creates a richer data context. The TSHF strategy, specifically when pairing a ResNet backbone with a trainable quantum circuit, achieved a peak accuracy of 87.82%, F1-score of 91.77%, and an AUC-ROC of 89.08%, outperforming purely classical baselines. These results demonstrate that the proposed hybrid framework improves classification accuracy and threshold reliability, providing a stable, high-performance architecture for the clinical deployment of quantum-enhanced diagnostic tools.

---


### 49. [Deep Clustering for Climate: Analyzing Teleconnections through Learned Categorical States](https://arxiv.org/abs/2604.22909)

**<font color=#1a73e8>作者：</font>** Lívia Meinhardt, Dário Oliveira  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding and representing complex climate variability is essential for both scientific analysis and predictive modeling. However, identifying meaningful climate regimes from raw variables is challenging, as they exhibit high noise and nonlinear dependencies. In this work, we explore the use of Masked Siamese Networks to discretize climate time series into semantically rich clusters. Focusing on daily minimum and maximum temperature, we show that the resulting representations: (i) yield clusters that reflect meaningful climate states under our modeling assumptions, offering a simplified representation for downstream use; (ii) enable sampling and analysis of specific climate scenarios; and (iii) exhibit statistical associations with El Niño events, underscoring their scientific relevance. Our findings highlight the potential of self-supervised discretization as a tool for climate data analysis and open avenues for incorporating richer climate indicators in future work.

---


### 50. [PExA: Parallel Exploration Agent for Complex Text-to-SQL](https://arxiv.org/abs/2604.22934)

**<font color=#1a73e8>作者：</font>** Tanmay Parekh, Ella Hofmann-Coyle, Shuyi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents for text-to-SQL often struggle with latency-performance trade-off, where performance improvements come at the cost of latency or vice versa. We reformulate text-to-SQL generation within the lens of software test coverage where the original query is prepared with a suite of test cases with simpler, atomic SQLs that are executed in parallel and together ensure semantic coverage of the original query. After iterating on test case coverage, the final SQL is generated only when enough information is gathered, leveraging the explored test case SQLs to ground the final generation. We validated our framework on a state-of-the-art benchmark for text-to-SQL, Spider 2.0, achieving a new state-of-the-art with 70.2% execution accuracy.

---


> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-437](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
