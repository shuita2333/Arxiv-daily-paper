# 📦 其他研究 | 2026年06月10日

> 本类共 **527** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

---

### 1. [Bidirectional Small-Granularity Search between Code and Text](https://arxiv.org/abs/2606.07519)

**<font color=#1a73e8>作者：</font>** Marco A. Valenzuela-Escárcega, Enrique Noriega-Atala, Gus Hahn-Powell 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce the novel task of bidirectional small-granularity search between code and text, where the queries are small snippets of text or code and the results are also small fragments of the opposite modality, i.e., code or text. This task establishes direct links between text in scientific publications and corresponding code segments, in support of better and faster understanding of scientific methods. We introduce a large dataset for the proposed task that includes a training partition with textual descriptions of code generated automatically using GPT-4, and three testing partitions, one in-domain and two out-of-domain (OOD) that contain manually-annotated data as well as material from other domains. We also propose a modular approach to address this task. Our approach shares an encoder across four different subtasks that learn start/end of answer spans in both directions. We show that our method achieves good results in-domain, and encouraging results OOD. This suggests that addressing this task with automatically-generated data is possible, but there is exciting future work to be done.

---


### 2. [Implicit Causal Graph Construction in Text via Chain Discovery](https://arxiv.org/abs/2606.07525)

**<font color=#1a73e8>作者：</font>** Liesbeth Allein, Marie-Francine Moens  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Causal graphs in text are typically populated by observable, predefined events. In contrast, we study implicit causal graph construction from text by treating each described cause-effect pair as the begin- and endpoint of an underlying latent causal graph and using large language models (LLMs) to infer intermediate causal events. We compare end-to-end graph construction with methods that frame the task as causal chain discovery. In the latter, graphs are built either by aggregating inferred chains or by progressively expanding partial chains through an iterative search process. We further explore Wisdom of the Crowd extensions that access causal knowledge from multiple LLMs in post-hoc aggregation and collaborative inference settings. We analyze trade-offs among these approaches and evaluate the validity of inferred causal relations using a manually curated database of 1,560 scientifically validated causal pairs. This database-based evaluation is proposed as reliable, resource-efficient, and transferable to settings where ground-truth graphs are unavailable.

---


### 3. [Finding New Connections between Concepts from Medline Database Incorporating Domain Knowledge](https://arxiv.org/abs/2606.07530)

**<font color=#1a73e8>作者：</font>** Yang Weikang, Chowdhury S.M. Mazharul Hoque, Jin Wei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this digital world, data is everything and significantly impacts our everyday lives. Interestingly, in this small world, everything is part of an ecosystem, where everything is connected, directly or indirectly. The same thing happens to data as well. In most cases, it may seem like a particular topic does not have any connection with another one, but in reality, they are connected through a mutually related topic. Therefore, in this research, we will discuss an adaptive model modified from the ABC model by Don R. Swanson, a Literature-Based Discovery (LBD) Model, to find the hidden connections between Concepts of Interest. The model demonstrates that two topics, A and C are different and have no relationship. But they have a common topic, B that can be used to connect topics A and C This famous model will be used in this discussion to connect Medical Concepts.

---


### 4. [Offline Reinforcement Learning for Plasma Control in Nuclear Fusion: Codebase and Benchmark](https://arxiv.org/abs/2606.07550)

**<font color=#1a73e8>作者：</font>** Yang Fu, Haomin Bao, Rohit Sonker 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) offers a promising route for developing plasma controllers from historical tokamak data, since online trial-and-error on real devices is costly and risky. However, progress in this direction remains difficult to measure due to the lack of a standardized offline RL benchmark for realistic multi-actuator, long-horizon plasma control problems in nuclear fusion. We introduce RL4F, an Offline Reinforcement Learning Benchmark for Plasma Control in Nuclear Fusion, providing closed-loop evaluation environments and baseline comparisons across four full-profile tracking tasks: rotation, density, temperature, and pressure. The dynamics function underlying the evaluation environment is built from historical discharge data from DIII-D, a real-world Tokamak. We evaluate a broad set of imitation learning and offline RL baselines under a unified protocol. We find that offline model-based RL methods obtain the best average performance on most objectives, although no single method dominates all tasks, highlighting the importance of dynamics modeling in complex, long-horizon plasma control tasks. To foster further research, we open-source the codebase, datasets, and evaluation framework, providing a benchmark not only for the fusion community but also for algorithm development in offline RL.

---


### 5. [MedicalRec: Medical recommender system for image classification without retraining](https://arxiv.org/abs/2606.07553)

**<font color=#1a73e8>作者：</font>** Roghayeh Taghavi, Aysa Hasanazde Bashkandi, Amir Ali Bengari 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The emergence of machine learning and deep learning has revolutionized the efficiency of diagnostic, therapeutic, and administrative systems in healthcare. However, this rapid adoption has come at the cost of requiring significant computing power and energy consumption, as well as e-waste disposal and carbon emissions. One of the challenges of these models is choosing the right model for classification tasks. To this end, researchers attempt to identify the optimal model using their data through trial and error, which involves energy consumption and waste. The goal of this study is to develop a model-based recommender system for medical image classification. For this purpose, a data set was collected from 3,000 articles in the field of medical image classification. This dataset, publicly available under the name MedicalRec-Bench, contains over 5,000 records of models tested in various tasks, including Skin Cancer Classification, Tumour Classification, Wound Classification, Breast Cancer, and MRI classification. The dataset was evaluated in four different modes, depending on the number of features: MedicalRec I (5 features), MedicalRec II (9 features), MedicalRec III (11 features), and MedicalRec IV (18 features). Collecting all values for the features is challenging due to non-reporting by the authors; hence, the dataset contains significant amounts of missing values. The Medical Recommender System (MedicalRec) is a transformer-based model used for item recommendations in this study. This model achieved remarkable results in the evaluation on the dataset and in the evaluation with 12 base models. This model achieved a maximum HitRate@100 of 75.5%. The dataset and implementations are available through the GitHub link: this https URL

---


### 6. [Priors Persist Through Suppression: A Stroop Paradigm for Lexical Override](https://arxiv.org/abs/2606.07555)

**<font color=#1a73e8>作者：</font>** Han-yu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Glossaries, technical specifications, and system prompts routinely ask language models to use familiar words in unfamiliar ways. When this works, the lexical prior persists through override rather than being replaced: it continues to operate after the local rule applies, with the rule lowering its logit rather than installing the new meaning on top. We test this with a Stroop-style paradigm: a remapping rule ("doctor" means "forest") pitted against the query word's lexical-prior distractor ("hospital"), with matched neutral controls. Across 11 open-weight models spanning four families and 1B--9B parameters, lexical-prior strength predicts interference even after item-level controls for answer prior, frequency, tokenization, and prompt wording. Activation patching on five aligned models locates a source-position triplet (definition subject, definition target, query word) that nearly fully recovers the conflict effect (aggregate $R \in [0.92, 1.06]$). A definition-target swap shows the triplet performs binding rather than identity matching. Dissociation experiments isolate target preservation as the binding-specific signature: distractor suppression occurs under matched, swap, and item-mismatched conditions alike, whereas target logit collapse occurs only when the definition-target position is corrupted. Behavior and mechanism converge on the same channel: the lexical prior is where both interference originates and where override leaves its mark.

---


### 7. [SPIN: Decentralized Swarm Control via Tensorized Policy Coordination](https://arxiv.org/abs/2606.07557)

**<font color=#1a73e8>作者：</font>** Zhaowen Fan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized multi-agent swarm coordination on resource-constrained edge platforms remains fundamentally bottlenecked by the exponential scaling of joint action spaces and high-latency communication overhead. This paper introduces the Swarm Policy Interference Network (SPIN) framework, an architectural paradigm that bypasses these limitations by modeling swarm topologies as a compressed tensor network. We factorize the joint policy tensors of local multi-agent cliques into Matrix Product State (MPS) chains, reducing the computational complexity of evaluation from an exponential $O(n^m)$ wall to a strictly linear $O(m \cdot n \cdot \chi^2)$ constraint. To bridge local continuous spatial geometry with this discrete algebraic backend without requiring power-intensive online training loops, we introduce a decoupled, hybrid neuro-symbolic control pipeline. Local multi-layered neural networks operate as structural coordination encoders, pre-trained offline to nonlinearly map hand-engineered geometric descriptors into abstract environmental target measures. At runtime, edge agents execute instantaneous behavioral adaptations by applying the Radon-Nikodým derivative directly as a zero-shot importance-reweighting filter. We validate the framework within a discrete-time multi-agent simulation sandbox spanning tracking, decentralized dispersion/area coverage, and multi-goal coordination regimes. Qualitative telemetry demonstrates that the integrated pipeline achieves stable target-directed motion, anti-collapse spatial spreading under decentralized constraints, and structured subgroup formation across multiple targets, providing a mathematically grounded route to tractable, low-power edge swarm intelligence.

---


### 8. [Page image classifier fine-tuned on century-spanning archives of scanned documents for further content-specific processing](https://arxiv.org/abs/2606.07558)

**<font color=#1a73e8>作者：</font>** Kateryna Lutsai, Pavel Straňák, David Novák 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Digitization projects in the humanities produce vast, heterogeneous archives of historical documents, making manual sorting impractical at scale. This work addresses the need for an automated system to classify scanned page images based on visual content type - text, tables, and graphics - enabling content-specific downstream processing such as Optical Character Recognition (OCR) or structured data extraction. Methods: An image classification system was developed and evaluated on a dataset of over 48,000 annotated historical page images from century-old Czech archaeological archives, refined through four successive annotation stages with domain-expert review. A Random Forest Classifier baseline was established using hand-crafted image features. Subsequently, deep learning architectures were fine-tuned and compared: Convolutional Neural Networks (EfficientNetV2, RegNetY), Vision and Document Image Transformers (ViT, DiT), and multimodal CLIP models. An 11-category label scheme was designed collaboratively with domain experts and evaluated via five-fold cross-validation. Results: The feature-based baseline achieved approximately 75% accuracy. Fine-tuned CNNs and Transformers substantially outperformed it, with RegNetY-16GF achieving 99.16% and ViT-large 99.12% Top-1 accuracy on the held-out test set. CLIP ViT-B/16 reached 99.14% with optimized text descriptions. Conclusion: Image-only models, particularly RegNetY-16GF, deliver near-perfect classification accuracy and produce consistent labels across 649,508 unlabeled archival pages with over 90% inter-model agreement. Fine-tuned CLIP, despite competitive test-set accuracy, showed under 65% agreement with image-only models on unlabeled data, making it less suitable for deployment. The final models, annotated dataset, and software are publicly available under open-source licenses.

---


### 9. [Boundary Variance Inflation Causes Acquisition Bias in Gaussian Processes](https://arxiv.org/abs/2606.07561)

**<font color=#1a73e8>作者：</font>** Maria Bånkestad, Sanna Jarl, Jens Sjölund  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian processes with stationary kernels on bounded domains exhibit inflated posterior variance near the boundary. Despite being a long-recognized artifact in geostatistics and a source of over-exploration in Bayesian optimization, the causes and effects of boundary-induced acquisition bias are underexplored. We trace the root cause to a simple geometric mechanism: the truncation of the kernel correlation neighborhood at the domain boundary creates an observation-independent distortion that worsens with dimensionality. We show how this distortion manifests across three acquisition classes: variance maximization concentrates selections at the corners, whereas negative integrated posterior variance and expected predictive information gain move selections inward to axis-aligned interior shells. These patterns arise without reference to any objective function, meaning that acquisition behavior can be dominated by kernel geometry rather than the desired task-specific uncertainty. To quantify this, we introduce a function-free selection-profile diagnostic for arbitrary acquisitions, kernels, and bounded-domain geometries.

---


### 10. [Emergence via Phase Transitions: Mechanism Landscapes and Universal Convergence Across Complex Systems](https://arxiv.org/abs/2606.07563)

**<font color=#1a73e8>作者：</font>** Truong Xuan Khanh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Across machine learning, biology, and physics, independently evolving systems often converge toward strikingly similar high-level structures despite radically different microscopic details. Grokking circuits converge across random seeds, evolutionary lineages rediscover similar metabolic solutions, and renormalization flows approach common fixed points. We propose the Hierarchical Emergence Framework (HEF) as a candidate universality framework for such convergence phenomena. HEF models emergence as a phase transition in a mechanism landscape constrained by thermodynamic and information-theoretic laws. The framework introduces a critical energy threshold Ec separating an exploration regime with competing mechanisms from a convergence regime governed by a unique minimum-cost mechanism. Under structural assumptions, we prove physical feasibility, derive strict metric contraction, and establish convergence toward a unique fixed-point representation independent of initial conditions. We further connect this convergence structure to causal emergence through Effective Information and mechanism competition entropy. To test the framework, we study delayed generalization ("grokking") in modular arithmetic transformers across 111 experiments. We identify a reproducible empirical fingerprint of the Ec transition: the weight norm peaks systematically before grokking in 92% of runs. Normalized accuracy curves collapse onto a tanh kink (R^2=0.93) consistent with a Landau-Ginzburg universality class, and all grokked models converge to 0.9745+/-0.014 regardless of initialization, weight decay, or training fraction (ANOVA p>0.13). HEF is not presented as a universal theory of emergence, but as a falsifiable mathematical scaffold for studying convergence phenomena across complex systems.

---


### 11. [STARIXNet: Multivariate and Multi-attribute Deep Learning Approach to Real-Time Resource Allocation in Cloud Platforms](https://arxiv.org/abs/2606.07565)

**<font color=#1a73e8>作者：</font>** Ahmed Abdulaal, Maruf Aytekin, Thilaga kumaran Srinivasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intelligent scaling of microservices in cloud platforms is crucial for mitigating escalating compute costs while avoiding service disruptions. Current solutions are limited to the univariate space, typically focusing on CPU usage alone to drive scaling decisions. Moreover, they address the problem as a purely forecasting task, focusing on prediction precision while neglecting the greater risks of underestimation and delays in system responsiveness. Alternative solutions are computationally complex, making them impractical for large-scale, real-time deployments. To address these challenges, we present STARIXNet, a lightweight neural network that guides resource allocation decisions in the multivariate space by capturing spatio-temporal relationships among multiple system metrics. STARIXNet models multiple quasi-dependent attributes, in particular the (S)easonal, (T)emporal, (A)uto-(R)egressive (I)ntegrated, and e(X)ogenous patterns, then implements an aggregation policy to finalize scaling decisions, prioritizing service stability, followed by cost-efficiency, over raw forecast accuracy. We empirically demonstrate the performance of STARIXNet by benchmarking against existing solutions in real-world settings. STARIXNet is deployed for critical production microservices at Walmart achieving tangible savings ranging from 10\% to 50\%, in addition to intangible benefits through improved service stability and customer experience.

---


### 12. [A Systematic Study of Behavioral Cloning for Scientific Data Annotation](https://arxiv.org/abs/2606.07568)

**<font color=#1a73e8>作者：</font>** Ishaan Singh Chandok, Core Francisco Park  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Scientific data annotation, such as tracking animals in video or proofreading neural reconstructions, remains bottlenecked by the "last mile" problem: even with strong automation, verification and correction consume substantial human effort. Standard approaches train models to directly predict annotations, discarding the rich supervision in how experts navigate, click, verify, and correct. We introduce a framework for studying behavioral cloning on scientific annotation: 9 synthetic tasks paired with synthetic annotations that simulate realistic human strategies including exploration, mistake correction, and strategic decision-making. Our experiments reveal several findings. First, skills emerge hierarchically: models learn GUI mechanics before task-critical decisions, and commit fewer mistakes than the training data while retaining the ability to correct errors when they occur. Second, scaling models on multi-task behavioral cloning shows that larger models are more data efficient within our scale range. Third, multi-task pretraining enables efficient fine-tuning to new tasks, while training from scratch fails entirely. Fourth, linear probes reveal that models internally represent latent variables of the annotation process such as task phase and data position; interestingly, we find a shared mistake representation that generalizes across different annotation tasks. Overall, our framework establishes systematic benchmarks and identifies key bottlenecks, providing a foundation for scaling behavioral cloning to real-world scientific data annotation.

---


### 13. [TriHead-GAN: A Generative Adversarial Network with Triple-Head Discriminator for Carbon Emission Time Series Generation](https://arxiv.org/abs/2606.07569)

**<font color=#1a73e8>作者：</font>** Zesen Wang, Lijuan Lan, Yonggang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate carbon emission monitoring is critical for climate policy and emerging regulatory mechanisms such as the EU Carbon Border Adjustment Mechanism, yet city-level high-frequency monitoring data remain extremely scarce, severely limiting data-hungry deep learning models. Time series generation is a natural remedy, but existing GAN and diffusion-based generators often provide limited explicit supervision for the domain structure of carbon emission data: they may match marginal distributional statistics while insufficiently preserving cross-variable correlations between CO$_2$ and co-emitted pollutants and meteorological factors, and tend to collapse the first-difference statistics of atmospheric measurements, producing sequences that are smooth on average but lack the realistic step-wise variability of the underlying signals. We propose TriHead-GAN, a Transformer-based adversarial framework whose triple-head discriminator jointly supervises three complementary aspects of the joint distribution: distributional authenticity via a Wasserstein critic, cross-variable dependency via leakage-free regression of the target variable, and step-wise temporal smoothness via adjacent-difference prediction. The generator combines global self-attention with local temporal convolution, per-step noise injection, and an anti-smoothing loss that matches first-difference statistics. Experiments on the self-collected Changsha Carbon dataset, two public carbon datasets (China, US), and the ETTh1 benchmark show that TriHead-GAN achieves favorable performance over mainstream baselines on the vast majority of settings, and that the resulting synthetic windows improve downstream forecasting accuracy in low-resource carbon monitoring scenarios.

---


### 14. [When Should an AI Scientist Stop? Verifiable Experiment Steering and Refusal for Autonomous Discovery](https://arxiv.org/abs/2606.07576)

**<font color=#1a73e8>作者：</font>** Neel Tushar Shah, Manglam Kartik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present CARTOGRAPH, a verification layer for AI scientists that couples unresolved-subspace experiment steering (select), explicit ambiguity closure (resolve), and residual-based library inadequacy detection (refuse). Under a local linear-Gaussian bridge, raw unresolved projection is the isotropic unresolved Fisher-information trace, while CARTOGRAPH-A is the exact unresolved A-optimal rule; closed-form EIG and Box-Hill arise as local comparators rather than global equivalents. Across five testbeds, CARTOGRAPH-A beats raw projection 129W/0T/15L at d = 8 (p < 10^-21) in a replicated structured cascade. More distinctively, the framework tentatively identifies three out-of-library pharmacokinetic mechanisms and then revokes those identifications as residuals expose structural misfit, while one perturbed in-library control stays identified throughout. In low-dimensional pharmacokinetic and filtered EPA settings, near-ties against disagreement are predicted by theory and observed. Finally, in a retrospective audit of 40 positive claims from the published A-Lab autonomous materials system, the refuse guard flags all 4 claims later marked inconclusive under manual reanalysis while passing 32/36 confirmed claims. Code is available at this https URL

---


### 15. [MST-Direct at Scale: Multivariate and Conditional Geostatistical Simulation via Sinkhorn Optimal Transport](https://arxiv.org/abs/2606.07578)

**<font color=#1a73e8>作者：</font>** Tcharlies Bachmann Schmitz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper extends MST-Direct, a Matching-via-Sinkhorn-Transport approach for multivariate geostatistical simulation, from the original bivariate, unconditional, small-grid formulation to multivariate, conditional, and large-grid settings. We address the three main limitations identified in the original work: (i) scalability beyond a few thousand nodes through a sparse, candidate-restricted Sinkhorn matcher with O(nC) memory complexity; (ii) extension to multiple variables by matching target value tuples onto an independent FFT-MA Gaussian backbone that reproduces a prescribed variogram; and (iii) hard-data conditioning by fixing observed data tuples at their spatial locations while conditioning the backbone through kriging. Because the transport plan remains a permutation of the target tuples, the multivariate joint distribution is preserved exactly.
The method is validated using the same six-variate, heteroscedastic, strongly nonlinear reference distribution employed in Direct Multivariate Simulation (DMS), under both unconditional (200x200) and conditional (100x100, 200 hard-data samples) scenarios, and is benchmarked against the Projection Pursuit Multivariate Transform (PPMT). Results show that MST-Direct reproduces the joint distribution with zero histogram error, exactly honours hard data, and accurately reproduces the prescribed spatial correlation structure, whereas PPMT remains an approximation.
Index Terms-Optimal transport, Sinkhorn algorithm, geostatistical simulation, multivariate simulation.

---


### 16. [Customer Churn Prediction on Structured Data Using FT-Transformer and Stacking Ensembles](https://arxiv.org/abs/2606.07582)

**<font color=#1a73e8>作者：</font>** Joyjit Roy, Samaresh Kumar Singh, Laxmi Shaw  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Customer churn prediction is essential across data-driven industries such as insurance, digital banking, eCommerce, and subscription platforms, where retaining existing customers is typically more cost-effective than acquiring new ones. Predicting churn on structured datasets remains challenging due to class imbalance, nonlinear feature interactions, and heterogeneous feature types. Tree-based ensemble methods consistently demonstrate strong performance in these contexts, often outperforming conventional neural networks. This study introduces a validated hybrid architecture that integrates feature-tokenized transformers (FT-Transformer) with gradient-boosted trees through calibration-aware stacking. The proposed framework addresses persistent gaps in statistical validation, probability calibration, and reproducibility found in prior research. The FT-Transformer captures higher-order feature interactions using self-attention, while XGBoost captures gradient-boosted decision boundaries with complementary inductive biases. Class imbalance is handled using class-weighted loss functions, thereby avoiding synthetic oversampling and preserving minority-class distributions. The models are ensembled using out-of-fold (OOF) stacking with a logistic regression meta-learner, which recalibrates overconfident base model outputs and learns optimal combination weights. On a public bank churn dataset, the hybrid model achieves 62.10% F1, 0.861 AUC-ROC, and 0.647 PR-AUC, outperforming the Multi-Layer Perceptron (MLP) baseline by 3.37 F1 points and 0.027 AUC under 5x5 cross-validation with 95% confidence intervals reported. Ablation studies demonstrate that both the transformer component and stacking strategy contribute materially to performance. The proposed methodology offers a reproducible and extensible reference architecture for contemporary churn prediction on structured tabular data.

---


### 17. [Outage Detection in Self-Healing Smart Grids Using Reinforcement Learning with Spectral Graph Neural Networks](https://arxiv.org/abs/2606.07583)

**<font color=#1a73e8>作者：</font>** Lihui Liu, Mucun Sun, Caisheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-healing smart grids can quickly adjust their network configuration during outages to minimize power disruptions. During an outage, several actions can be taken, such as network reconfiguration through switching operations and emergency load shedding. However, traditional machine learning methods for outage mitigation are not well suited for smart grids due to their slow response time and high computational cost. To address these challenges, recent studies have explored reinforcement learning to automatically perform network reconfiguration. In these approaches, the control policy is typically modeled using a graph neural network (GNN). However, conventional GNNs operate in the spatial domain and may fail to capture important relationships in the frequency domain. Frequency-domain information is particularly useful for modeling global structural patterns and system-wide interactions in power networks. In this paper, we propose a spectral graph reinforcement learning framework for outage management in distribution networks to enhance system resilience. Our model learns the optimal power restoration policy using a spectral graph neural network. We evaluate the proposed method on three modified IEEE test systems: the 13-bus, 34-bus, and 123-bus networks. Experimental results show that our approach achieves near-optimal performance in real time and generalizes well across a wide range of outage scenarios.

---


### 18. [Optimality of Sequential Filtering Under Independent Cost and Selectivity Models](https://arxiv.org/abs/2606.07589)

**<font color=#1a73e8>作者：</font>** Hrishikesh Paranjape, Abhishek Mandal, Xian Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential filtering pipelines are a common design pattern in large-scale systems, where a large population of items is progressively reduced by a sequence of stages that each incur cost. Despite their prevalence in ranking systems, cascaded machine learning inference, and fraud detection, filter ordering is often determined by heuristics without formal guarantees. We formalize sequential filtering under an expected-cost objective and prove that, under an independence model, ordering filters by increasing ratio of cost to rejection probability minimizes expected total cost. Extensive Monte Carlo simulations show that the optimal ordering strictly dominates common heuristics across all runs, both in expectation and across the full distribution of outcomes.

---


### 19. [UNIQ: Conformal Calibration for Adaptive Conservatism in Offline Reinforcement Learning](https://arxiv.org/abs/2606.07592)

**<font color=#1a73e8>作者：</font>** Aditya Upadhyay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning requires careful conservatism to mitigate distribution shift, yet most existing methods apply a fixed penalty uniformly across all states regardless of local data coverage. We present UNIQ (Uncertainty-Informed Quantile), an offline RL method that introduces state-adaptive conservatism through conformally calibrated uncertainty estimation. Built on the Implicit Q-Learning (IQL) backbone, UNIQ trains a multi-expectile value ensemble, computes distribution-free uncertainty estimates using split conformal prediction, and maps the resulting signal to a state-dependent expectile that relaxes conservatism in well-covered regions while strengthening it in uncertain regions near the data frontier. On D4RL MuJoCo benchmarks, UNIQ consistently improves over IQL, with the largest gains observed on Walker2d and replay-heavy tasks. At the same time, UNIQ operates at near-IQL memory cost (approximately 250 MB peak VRAM), providing roughly a 10x reduction compared to EDAC. Rather than pursuing overall state-of-the-art performance, we position UNIQ as a practical mechanism contribution that improves the performance-efficiency trade-off in offline reinforcement learning.

---


### 20. [Syll: Open-Source Personal Automation with Cross-Surface Execution](https://arxiv.org/abs/2606.07594)

**<font color=#1a73e8>作者：</font>** Bo Zhang, Borui Zhang, Chenghao Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal AI agents must increasingly operate across APIs, shells, web surfaces, and desktop GUIs, yet many systems remain tuned to a single interface and offer limited support for user teaching and auditability. We present Syll, an open-source, self-hosted multimodal agent harness that unifies MCP/API tools, CLI execution, and visual GUI control in a modular runtime, enabling agents to coordinate computer use across heterogeneous interfaces while streamlining how users and agents exchange information. At the core of Syll is a bidirectional user-agent interaction layer: users teach procedures through direct demonstration, which Syll compiles into reusable skills; agent execution is translated back into multimodal evidence -- logs, keyframes, and approval checkpoints -- for inspection and control. Syll further externalizes memory, skills, routines, and governance as editable local artifacts, supporting straightforward inspection, extension, and downstream development. Our implementation has been validated on production desktop applications including Adobe Photoshop, Adobe Audition, Stardew Valley, macOS Finder and others. We report mechanism-oriented studies that validate multimodal routing, teachable GUI replay, and persistent local artifacts. We hope Syll can serve as a practical open-source foundation for personal automation that users can teach, inspect, and continuously extend.

---


### 21. [VisualLeakBench: Reproducible Action-Boundary Propagation Failures in Vision-Language Agents](https://arxiv.org/abs/2606.07595)

**<font color=#1a73e8>作者：</font>** Youting Wang, Yuan Tang, Yitian Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language agents increasingly consume screenshots, documents, and user interfaces before writing to memory, sending messages, or invoking external tools. We study a concrete failure mode in this setting: action-boundary propagation, where sensitive or unsafe visible text is copied from an image into downstream tool arguments. We present VisualLeakBench, a diversified 500-image benchmark spanning UI, chat, document, form, and dashboard scenes, and evaluate a stratified 100-image agent subset with four production VLM systems under two workflows: note capture and external handoff. At baseline, target strings are propagated into tool arguments in 78.8% of PII cases and 85.5% of rendered unsafe-text cases. Under a defensive system prompt, rendered unsafe-text propagation remains high at 52.6%, while PII tool propagation falls to 2.0%, largely by suppressing tool use rather than preserving utility. Rates are tool-surface dependent: search-like tools suppress PII propagation, but rendered unsafe text still crosses tool boundaries. We measure visual-to-tool propagation rather than downstream instruction execution. We additionally provide a labeled-target oracle upper-bound diagnostic that localizes most failures at the tool boundary while leaving response-side leakage as residual risk.

---


### 22. [Repetition Mismatch: Why Data Mixture Experiments Don't Scale and How to Fix Them](https://arxiv.org/abs/2606.07597)

**<font color=#1a73e8>作者：</font>** Kevin Zhou, Lisa Alazraki, Kris Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-training data mixtures are commonly tuned by running small-scale experiments and extrapolating to the target training budget. When high-quality data is scarce and must be repeated, this extrapolation frequently fails, but the source of the failure has not been isolated. We show that a primary culprit is a repetition mismatch: because high-quality datasets are small, their repetition rate changes as the training budget grows, shifting the optimal mixture in ways that small-scale proxy experiments do not anticipate. A subsampling procedure that matches the target repetition rate controls for this effect. In a two-source setting combining limited high-quality data with web crawl, a single repetition-controlled experiment using only 1/16 of the target tokens recovers a mixture within 0.05 of the optimum for a 757M parameter model, compared to an error of 0.75 without repetition control. Achieving comparable accuracy without repetition control requires three to four horizons, consuming 44 to 94% of the target token budget. With three data sources, the larger mixture space requires more than a single experiment to constrain, but the approach remains effective: at the 757M scale, just two repetition-controlled horizons recover the optimal mixture, outperforming baselines that instead require the full two-source experiments to construct. Our results reveal that repetition dynamics, not scale alone, shape whether small-scale mixture experiments generalize. More broadly, they suggest that data repetition deserves treatment as a first-class variable in mixture optimization, rather than an inconvenient side effect of limited data.

---


### 23. [A Topological Characterization of Graph Neural Networks via Stochastic Block Model Embeddings on the n-Sphere](https://arxiv.org/abs/2606.07598)

**<font color=#1a73e8>作者：</font>** Gopal Anantharaman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a topological framework for comparing trained Graph Neural Networks (GNNs) by mapping the Stochastic Block Models (SBMs) induced on the graphon-signal space of a Message Passing Neural Network (MPNN) onto the unit $n$-sphere $\sphere^{n-1}\subset\R^n$. The construction rests on three classical pillars: the \emph{compactness} of the cut-distance graphon space $(\Wo,\cutdist)$ \citep{lovasz2006limits,lovasz2012large}, the Frieze--Kannan \emph{weak regularity lemma} together with its graphon-signal extension due to \citet{levie2023graphon}, and the Lipschitz continuity of MPNNs with respect to the cut-distance. We show that, for any prescribed tolerance $\varepsilon>0$, a trained MPNN $\Phi$ acting on a sufficiently large graph factors (up to $\varepsilon$) through a step-graphon-signal of bounded complexity, and we construct an explicit measure-preserving map $\Psi_n\colon[0,1]\to\sphere^{n-1}$ that places the SBM regions on disjoint spherical caps. This produces a problem-agnostic, low-dimensional ``fingerprint'' of a trained GNN that is amenable to visual inspection and to nearest-neighbour search across model zoos, enabling \emph{transfer-learning candidate retrieval} without retraining. We discuss the obstruction posed by concentration of measure in high dimension -- a phenomenon directly relevant to LLM-scale embeddings. We close with five concrete future research directions: hyperbolic and Grassmannian alternatives to the spherical model, Gromov--Wasserstein distances on graphon-signals as an isometry-free alternative to the $n$-sphere map, an information-geometric (Fisher) reformulation of the SBM manifold, persistent-homology fingerprints of layer-wise embedding clouds, and a spectral-distance baseline derived from the graphon eigendecomposition.

---


### 24. [DiffoR: A Unified Continuous Generative Framework for Universal Ordinal Regression](https://arxiv.org/abs/2606.07599)

**<font color=#1a73e8>作者：</font>** Hongxu Ma, Lin Wang, Chenghou Jin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ordinal Regression (OR) aims to predict target values with inherent order, underpinning critical applications across diverse domains, from recommender systems to computer vision. Though having evolved from naive regression to discretization-based classification and generation, existing paradigms remain fundamentally constrained by quantization artifacts and the lack of global ordinal topological perception. These methods typically enforce rigid boundary delineations, failing to capture the non-stationary semantic transitions inherent to ordinal data. In this paper, we propose a novel paradigm where OR is formulated as a Continuous Generative Ordinal Regression task. Under the novel paradigm, we introduce DiffOR, a unified framework that leverages diffusion models to recover continuous ordinal values via iterative denoising, thereby enabling the dynamic learning of soft semantic transitions. To explicitly preserve ordinal topology, we devise a Dual-Decoupling Strategy: Spatially, Multi-scale Increment Aggregation decomposes targets into hierarchical continuous increments; Temporally, Dynamic Denoising Perception synchronizes denoising steps with feature frequencies, ensuring robust coarse-to-fine refinement. Theoretically, we show that the proposed method can significantly enhance both representation capability and mechanistic interpretability. Extensive experiments on 12 benchmarks across four domains validate DiffOR's consistent superiority over state-of-the-art methods, establishing a new standard that demonstrates strong potential as a general-purpose solution for universal ordinal regression.

---


### 25. [Reachability and asymptotics of Gaussian Transformer dynamics](https://arxiv.org/abs/2606.07600)

**<font color=#1a73e8>作者：</font>** Albert Alcalde, Zhengping Ji, Enrique Zuazua  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We formulate data propagation through the Transformer, the machine learning architecture powering large language models, as a nonlinear control system on the space of probability measures. For the mean-field Transformer model with self-attention and affine feed-forward layers, we prove that Gaussian distributions remain exactly Gaussian along the induced flow. This invariance reduces the infinite-dimensional measure dynamics to a finite-dimensional bilinear control system governing the evolution of the mean and covariance, reformulates the expressive capacity of Transformers as a reachability problem for prescribed Gaussian moments, and reveals a novel connection with Riccati-type equations from classical filtering and control.
For time-varying controls, we prove exact finite-time reachability of any target Gaussian distribution whose covariance matrix has the same rank as the initial one, this rank constraint being an intrinsic invariant of the dynamics. For time-invariant parameters, we derive explicit spectral conditions leading either to asymptotic stability toward positive-definite equilibria or to finite-time blow-up of the covariance.
Numerical experiments complement the theory by showing that practical Transformers with Gaussian inputs remain close to moment-matched Gaussian distributions through early and intermediate layers, while Transformers with prescribed attention matrices reproduce the predicted covariance regimes: bounded evolution in stabilizing configurations and blow-up in destabilizing ones.

---


### 26. [LFNO: Bridging Laplace and Fourier via Transient-Steady Decomposition](https://arxiv.org/abs/2606.07601)

**<font color=#1a73e8>作者：</font>** Jeongun Ha, Sanga Yoon, Donghun Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Laplace-Fourier Neural Operator (LFNO), a unified framework for modeling dynamical systems across transient and steady-state regimes by integrating the spectral advantages of Laplace and Fourier Neural Operators. LFNO employs a dual-branch architecture that explicitly decomposes system dynamics into transient and steady-state components. We evaluate LFNO on nine benchmarks, including three ODE systems (Duffing, Lorenz, and Pendulum) and six PDE systems (Euler-Bernoulli beam, Heat, Reaction-diffusion, Brusselator, Burgers, and Navier-Stokes). LFNO significantly outperforms existing operators on ODE systems, where transient dynamics dominate, and consistently surpasses LNO while achieving performance competitive with FNO on PDE benchmarks. Furthermore, LFNO offers improved stability and physical interpretability through its component-wise decomposition. These results demonstrate that LFNO provides a robust and unified approach for learning complex dynamical systems across multiple temporal scales.

---


### 27. [MetaEvo: A Meta-Optimization Framework for Experience-Driven Agent Evolution](https://arxiv.org/abs/2606.07603)

**<font color=#1a73e8>作者：</font>** Bowen Ren, Heyan Huang, Yinghao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit strong reasoning capabilities, yet most LLM-based agents are statically deployed and unable to improve through task interactions. Existing experience-driven methods often rely on memory or heuristics without enhancing the model's ability to learn, treating it as a passive executor and leading to early performance plateaus and limited long-term improvement. To address this issue, we propose MetaEvo, a two-stage framework for continual agent evolution that focuses on improving how the model learns from tasks experience, rather than solely on what it stores. MetaEvo first applies preference-based optimization to enhance the model's ability of principle abstraction, then enables the accumulation and reuse of these principles within a modular agent architecture. Experimental results on diverse reasoning benchmarks demonstrate that MetaEvo consistently outperforms strong baselines, maintains reliable improvement across iterations. These findings validate the effectiveness of meta-optimization in enabling agents to learn from experience and continually enhance their reasoning capabilities.

---


### 28. [SRT: Super-Resolution for Time Series via Disentangled Rectified Flow](https://arxiv.org/abs/2606.07605)

**<font color=#1a73e8>作者：</font>** Jufang Duan, Shenglong Xiao, Yuren Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-grained time series data with high temporal resolution is critical for accurate analytics across a wide range of applications. However, the acquisition of such data is often limited by cost and feasibility. This problem can be tackled by reconstructing high-resolution signals from low-resolution inputs based on specific priors, known as super-resolution. While extensively studied in computer vision, directly transferring image super-resolution techniques to time series is not trivial. To address this challenge at a fundamental level, we propose Super-Resolution for Time series (SRT), a novel framework that reconstructs temporal patterns lost in low-resolution inputs via disentangled rectified flow. SRT decomposes the input into trend and seasonal components, aligns them to the target resolution using an implicit neural representation, and leverages a novel cross-resolution attention mechanism to guide the generation of high-resolution details. We further introduce SRT-large, a scaled-up version with extensive pre-training, which enables strong zero-shot super-resolution capability. Extensive experiments on nine public datasets demonstrate that SRT and SRT-large consistently outperform existing methods across multiple scale factors, showing both robust performance and the effectiveness of each component in our architecture.

---


### 29. [QDSP: An Interpretable Structured Learning Framework for Predicting Death or Cerebral Palsy in Very Low Birth Weight Infants](https://arxiv.org/abs/2606.07606)

**<font color=#1a73e8>作者：</font>** Ling Wang, Xiaolong Li, Hui Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Very low birth weight infants (VLBWI) are at high risk of mortality and severe neurodevelopmental impairment, including cerebral palsy, yet reliable discharge-time prognostic stratification remains challenging in high-dimensional and data-limited clinical settings. To address this problem, we propose QDSP, an interpretable structured learning framework that integrates Quota-guided Subspace Sampling (QSS) and Differentiable-decision-guided Structure Perception (DSP). The QSS module constructs stability-aware and low-redundancy feature subspaces through bootstrap-based feature consistency estimation, whereas the DSP module employs differentiable soft oblique decision structures to model nonlinear clinical interactions while preserving traceable decision evidence. The proposed framework was evaluated on a real-world VLBWI cohort comprising 51 infants and further validated on three public medical tabular datasets. On the primary cohort, QDSP achieved an accuracy of 0.9200 and an AUC of 0.9714, outperforming representative machine learning and deep tabular learning baselines, including XGBoost, TabNet, and TabPFN. Across external datasets, QDSP maintained competitive discrimination and calibration under varying sample sizes and clinical distributions. In addition, SHAP-based analyses and differentiable decision-path tracing identified clinically relevant predictors, including cystic periventricular leukomalacia (cPVL) and birth weight, consistent with established neonatal pathophysiological evidence. These results suggest that QDSP provides an interpretable and robust framework for discharge-time risk stratification in VLBWI and may support early individualized clinical decision-making in neonatal intensive care settings.

---


### 30. [Position: Genomic Model Research Must Move Beyond Anecdotal Evaluation of Interpretability Methods](https://arxiv.org/abs/2606.07607)

**<font color=#1a73e8>作者：</font>** Shasha Zhou, Mingyu Huang, Ke Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advances in machine learning and computational power have unlocked the predictive potential of the human genome, yet biologists now demand that these models also elucidate the underlying biological mechanisms. While interpretable machine learning (IML) techniques have been increasingly applied to bridge this gap, there has been a pervasive reliance on anecdotal validation: the vast majority of research relies on a single IML method and reports only isolated successful instances. Through a benchmarking study on transcription factor binding, we demonstrate the risks of current practices. We show that different IML methods can often (1) yield contradictory explanations for the same predictions, (2) fail to localize known regulatory motifs, and (3) fail to faithfully reflect the model's internal decision process. In light of this, we argue for a validation framework analogous to clinical trials: just as trials require rigorous design and adverse-event reporting, genomic interpretability must move beyond cherry-picked plausibility toward systematic assessment of consistency, faithfulness, and biological validity. To facilitate this, we propose a tiered framework to guide rigorous evaluation and reporting of genomic IML methods.

---


### 31. [Measuring Poverty and Inequality with Reduced Data: A Machine Learning Approach Using Nigerian Household Data](https://arxiv.org/abs/2606.07614)

**<font color=#1a73e8>作者：</font>** Vanesa Jordá, Miguel Niño-Zarazúa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable measurement of income and consumption is essential for monitoring poverty and inequality in low- and middle-income countries, yet full household surveys are costly and difficult to implement regularly. This paper examines whether reduced survey instruments can preserve key distributional information. We apply Random Forest Recursive Feature Elimination (RF-RFE) to the 2018/19 Nigeria General Household Survey-Panel to identify the income sources, consumption categories and household characteristics that best classify individuals within the welfare distribution. The analysis focuses on three outcomes: poverty status, location in the quintile distribution and position relative to the Gini-based inequality line. The survey's post-planting and post-harvest periods allow us to assess performance under different seasonal contexts. Results show that RF-RFE achieves strong classification accuracy with few predictors. For consumption, poverty status and inequality-line position are accurately predicted using a small set of expenditure categories, while quintile classification reaches about 80 percent accuracy for seasonal consumption and 60--65 percent for annual consumption predicted from a single seasonal visit. For income, poverty status reaches around 90 percent accuracy with five predictors, and inequality-line position is largely captured by labour earnings. The findings suggest that machine-learning methods can help improve survey design and reduce data requirements while retaining much of the distributional information needed to measure and monitor poverty and inequality.

---


### 32. [Structured Neuron Pruning in Deep Neural Networks Using Multi-Armed Bandits](https://arxiv.org/abs/2606.07615)

**<font color=#1a73e8>作者：</font>** Salem Ameen, Sunil Vadera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks often contain redundant hidden units. Removing individual weights can reduce parameter count, but unstructured sparsity is not always easy to exploit in standard dense implementations. This paper develops a structured pruning framework in which complete neurons are removed using multi-armed bandit (MAB) algorithms. Each candidate neuron is treated as an arm; pulling an arm temporarily masks that neuron, measures the change in loss on a sampled mini-batch, restores the neuron, and updates an estimate of its safe-removal reward. The framework supports stochastic policies, including Epsilon-Greedy, Softmax, UCB1 and Thompson Sampling, and multiplicative-weight policies, including Hedge-style multiplicative weights and EXP3. We evaluate the method on tabular classification, tabular regression and deep neural-network benchmarks covering image, text and reasoning tasks. Statistical comparisons using the Friedman test followed by the Nemenyi post-hoc test show significant differences between methods. On tabular classification tasks, UCB1 obtains the highest mean rank among pruning policies and improves on the unpruned neural network. On regression tasks, UCB1 obtains the highest mean rank and is statistically competitive with, or superior to, several standard regression models according to R^2. On deep-learning tasks, UCB1 and Thompson Sampling obtain the strongest ranks, and several MAB policies significantly outperform the unpruned model, magnitude-based neuron pruning and greedy activation-variation pruning. The results show that MAB-based neuron pruning is an effective and computationally practical approach for structured model reduction.

---


### 33. [Item Response Scaling Laws: A Measurement Theory Approach for Efficient and Generalizable Neural Scaling Estimation](https://arxiv.org/abs/2606.07616)

**<font color=#1a73e8>作者：</font>** Sang Truong, Yuheng Tu, Rylan Schaeffer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws provide a fundamental framework for understanding the performance of Language Models (LMs), yet deriving them requires prohibitively expensive evaluations across thousands of checkpoints or millions of inference samples. To address this, we introduce Item Response Scaling Laws (IRSL), a unified framework that integrates Item Response Theory (IRT) within the scaling law framework. Unlike traditional approaches that treat each model-benchmark pair in isolation, IRSL disentangles latent model ability from question characteristics, factorizing the scaling law estimation for $M$ models and $N$ questions to significantly reduce parameter complexity from $O(M \times N)$ to $O(M + N)$. We instantiate IRSL with Beta-IRT, which leverages the empirical probability responses of LMs -- such as token probabilities in pre-training and pass rates in test-time sampling -- to capture richer signals than binary responses. We validate our approach across two prevalent scaling paradigms: (1) pre-training downstream scaling, using 6,612 LM checkpoints and 37,682 questions from 10 benchmarks; and (2) test-time scaling, using 12 LMs and 120 questions from 4 benchmarks with up to 2,500 samples per question. Given a one-time calibration on existing model responses, IRSL yields more reliable scaling estimates using only 50 questions per benchmark (a 99.9\% reduction), achieving comparable or superior decision accuracy to traditional approaches. Furthermore, we show that the estimated latent model abilities are generalizable, enabling accurate performance forecasting across benchmarks that share the same measurement objective.

---


### 34. [Query Lens: Interpreting Sparse Key-Value Features with Indirect Effects](https://arxiv.org/abs/2606.07617)

**<font color=#1a73e8>作者：</font>** Hwiyeong Lee, Ingyu Bang, Uiji Hwang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While sparse autoencoders provide features more interpretable than individual neurons, reliably characterizing them remains challenging. We propose Query Lens, which extends Logit Lens to enable more comprehensive and faithful interpretations of sparse features. By jointly considering encoder-side key features and decoder-side value features, we identify both the inputs that activate a feature and the outputs it promotes. We also account for indirect, module-mediated effects that arise when the feature is processed by downstream modules, going beyond the direct effect captured by Logit Lens. In experiments, we find that Query Lens yields coherent token signatures for features that remain uninterpretable under Logit Lens. Finally, we propose the Subspace Channel Hypothesis, suggesting that downstream modules read features through layer-specific subspaces.

---


### 35. [Graph Neural Networks for Predicting Solvability of Finite Groups](https://arxiv.org/abs/2606.07619)

**<font color=#1a73e8>作者：</font>** Tal Weissblat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a Graph Neural Network (GNN) framework for the classification of finite groups according to their solvability. Using graph representations associated with finite groups, including Cayley graphs (CG), the proposed model is trained to distinguish solvable and non-solvable groups using structural graph information alone. The framework is evaluated on groups outside the training dataset in order to investigate the extent to which GNNs can learn algebraic properties arising in group theory. More broadly, the present work explores the relationship between algebraic structure and graph-based geometric representations of finite groups. The present study is intended as a proof-of-concept investigation of whether GNNs can learn algebraic properties of finite groups from graph-based representations

---


### 36. [SENTRY: Statistical Reliability Analysis of Vision Transformers Under Soft Errors](https://arxiv.org/abs/2606.07620)

**<font color=#1a73e8>作者：</font>** Pramit Kumar Bhaduri, Mahdi Taheri, Samira Nazari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the growth of Vision Transformers in safety-critical domains like autonomous systems and medical imaging, ensuring their reliability against soft errors is paramount. While ViTs offer state-of-the-art accuracy, their massive parameter counts render exhaustive fault injection campaigns infeasible. To bridge this gap, a statistical fault injection framework is presented, leveraging finite-population sampling theory to provide formal reliability guarantees. It is demonstrated that failure rates are bounded within a 1% margin at 99\% confidence using only a few thousand samples, regardless of model scale. This methodology achieves up to a 10,700 times reduction in experimental cost compared to exhaustive approaches, while preserving the ability to localize vulnerabilities across architectural components. Through extensive evaluation of different architectures like ViT-Tiny and ViT-Small, a highly non-uniform reliability landscape is uncovered. It is shown that while only 3% of FP32 bit-flips result in failure, the vast majority of these events lead to catastrophic accuracy collapse. Specific vulnerabilities are localized to normalization layers and critical exponent bits within the IEEE-754 format, providing a mathematical foundation and actionable insights for the design of hardened, edge-deployed ViT architectures.

---


### 37. [HASA: Subnet Allocation for Compute-Constrained Model-Heterogeneous Federated Learning](https://arxiv.org/abs/2606.07621)

**<font color=#1a73e8>作者：</font>** Amir Hossein Shahdadian, Ahmed M. Abdelmoniem, Mahdi Taheri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge services increasingly use federated learning to personalize on-device models while keeping sensitive data local. In practice, deployments must handle heterogeneity in both client resources and local data distributions. Model-heterogeneous federated learning lowers client cost by allowing each client to train a subnet of a shared supernet, but most subnet-allocation policies are driven by device constraints and do not explicitly account for statistical heterogeneity. This paper proposes Heterogeneity-Aware Subnet Allocation (HASA), a train-only rule that assigns subnet widths based on client heterogeneity scores computed from local training data while enforcing a fixed size-weighted compute budget. This design enables budget-matched comparisons with alternative allocation policies. On an article-title next-word prediction benchmark with seven clients, HASA improves unweighted mean client test accuracy over uniform allocation across 10 matched seeds, increasing mean client test accuracy from 13.82 percent to 14.32 percent, and improves worst-client accuracy on average. In a matched-budget comparison with representative partial-training baselines, HASA achieves the strongest worst-client and tail-client accuracy on this benchmark. A directionality ablation shows that assigning smaller subnets to more heterogeneous clients degrades both mean and tail performance. A cross-domain image-classification study further shows that the effectiveness of heterogeneity-aware allocation depends on how well the heterogeneity score reflects clients' need for additional model width.

---


### 38. [Airport Terminal Passenger Queue Forecasting for Departure Gates and Security Checkpoints](https://arxiv.org/abs/2606.07622)

**<font color=#1a73e8>作者：</font>** Juhwan Lee, Seokbin Yoon, Keumjin Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate passenger queue forecasting in airport terminals is essential for efficient departure operations, as it enables proactive congestion management. However, time-varying passenger demand and heterogeneous facility usage across multiple departure facilities make forecasting challenging. In this work, we propose a passenger queue forecasting framework that learns historical passenger flow patterns from operational data. The proposed model employs a Transformer-based architecture to capture temporal dependencies and inter-facility correlations using past queue length and waiting time at departure gates and security checkpoints, together with passenger throughput at check-in islands. The learned representations are mapped to two facility-specific MLP heads to predict queue length and waiting time at departure gates and security checkpoints. Experimental results demonstrate accurate forecasts up to two hours ahead. The proposed approach offers practical real-time decision support for proactive queue management and staff reallocation in airport terminal operations.

---


### 39. [Eyes All Around: Design and Analysis of 360-Degree LiDAR Perception Using Equivariant Feature Learning in Unstructured Traffic](https://arxiv.org/abs/2606.07626)

**<font color=#1a73e8>作者：</font>** Pranav Darshan, Raghuveer Narayanan Rajesh, M Uttara Kumari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perception in dense, unstructured urban traffic remains a major challenge for autonomous driving because of the wide variety of road users, frequent occlusions, irregular motion patterns, and the lack of standardized road layouts. Although recent LiDAR based 3D object detectors have shown strong performance in structured driving scenarios, most are developed and evaluated for limited field of view settings, and their behavior under full surround 360-degree sensing is still not well understood. This paper studies a 360-degree LiDAR perception pipeline for autonomous driving, with particular attention to panoramic sensing, azimuthal sector wise spatial processing, and transformation equivariant feature extraction in complex urban scenes. The paper presents a practical 360-degree perception framework that combines sector wise panoramic processing with rotation equivariant sparse convolutions and evaluates its behavior on a custom Ouster OS0 LiDAR dataset collected across diverse Indian urban traffic conditions. The results show generally stable detection across several object classes, with the strongest performance for cars at 92.02/90.51, buses at 80.53/76.34, and trucks at 78.59/74.16, while lower scores for pedestrians at 67.45/61.02, cyclists at 73.21/69.54, and motorcyclists at 71.20/68.13 reflect the greater difficulty of detecting smaller and more variable road users in dense urban scenes.

---


### 40. [Learning Transfers: Kan Extensions for Neural Invariants](https://arxiv.org/abs/2606.07627)

**<font color=#1a73e8>作者：</font>** Luciano Melodia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transfer learning presumes that a representation learned on source tasks carries structure that remains usable on related target tasks. Standard evaluations probe this through target accuracy or distributional discrepancy, yet leave unspecified which structural invariant is meant to transfer. We supply that invariant categorically. A source task category $\mathcal A$, a target task category $\mathcal B$, and a task-change functor $J:\mathcal A\to\mathcal B$ determine, for every invariant-valued source representation $F:\mathcal A\to\mathcal V$, the universal transferred invariant $\operatorname{Lan}J F$. Given a target invariant $G:\mathcal B\to\mathcal V$, we define the transfer discrepancy $\operatorname{Comp}J(F,G)=\sup{b\in\operatorname{Ob}(\mathcal B)} d{\mathcal V}\bigl((\operatorname{Lan}_J F)(b),G(b)\bigr)$, evaluating transfer not by an objectwise comparison of source and target, but by comparing the target invariant against the one forced by the prescribed task transformation. We prove finite cokernel formulas for $(\operatorname{Lan}_J F)(b)$ in chain complexes and persistence modules, indexed by the comma category $J\downarrow b$. For persistence-valued finite-type one-parameter invariants, the discrepancy is computed exactly by bottleneck distances between barcodes. Controlled experiments on neural latent point clouds then test whether the score recovers the correct task functor and flags representation collapses that preserve classification accuracy while destroying transfer-relevant topology.

---


### 41. [Evaluation of ML Resource Utilization Requires Model Life Cycle Assessment](https://arxiv.org/abs/2606.07632)

**<font color=#1a73e8>作者：</font>** Jared Fernandez, Clara Na, Yonatan Bisk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proper accounting of the energy requirements and environmental impact of artificial intelligence (AI) systems is necessary for researchers, developers, policy makers, and users to assess the barriers to building systems at scale. With the growing complexity of pipelines and underlying infrastructure needed to develop and deploy AI systems, previous approaches for evaluating AI efficiency which focus on the costs of a single training run or an individual inference prediction are no longer sufficient. In this position paper, we enunciate the need for applying life cycle assessment to evaluate the costs of the machine learning model development and deployment pipeline to properly account for the required resources and downstream impact. Life cycle assessments enable the incorporation of costs across the full life cycle of an AI system and its underlying infrastructure, from the embodied costs associated with the physical computing hardware through the operational costs in training and inference.

---


### 42. [AMN: An Adaptive Multi-Scale Fusion Network with Boundary and Uncertainty Modeling for Nuclei Segmentation](https://arxiv.org/abs/2606.07633)

**<font color=#1a73e8>作者：</font>** Spoorthi M, Suja Palaniswamy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate classification of nuclei subtypes in histopathology images is critical for downstream tasks including tumor grading, immune infiltrate quantification, and prognosis prediction. Existing approaches rely on either convolutional or transformer-based encoders in isolation, limiting their ability to simultaneously capture fine-grained local texture and long-range spatial context. We present AMN (Adaptive Multi-Scale Nuclei Network), a dual-encoder segmentation framework that jointly leverages a Swin Transformer and a ResNet-50 feature pyramid, fused via a learned per-channel gating mechanism that dynamically weighs each encoder's contribution at every scale. AMN is trained with a multi-objective loss combining class-weighted focal loss, boundary-aware loss with positive-pixel emphasis, and a novel uncertainty-modulated classification term that suppresses overconfident erroneous predictions. Evaluated on the CoNIC benchmark across seven nuclei classes, AMN achieves a mean Dice of 0.82 and mean F1 of 0.68, with an F1 of 0.67 on the diagnostically challenging lymphocyte class. AMN outperforms eight baseline models spanning pure-CNN, pure-transformer, and recent hybrid architectures: U-Net, ResU-Net, DeepLabV3+, SegNet, ViT-Small, HmsU-Net, ConvFormer-UNet, and BEFUnet. Cross-dataset evaluation on MoNuSeg demonstrates strong generalization without retraining and validating the domain robustness of the learned representations.

---


### 43. [Crayotter: Traceable Multi-Agent Workflows for Long-Form Video Editing](https://arxiv.org/abs/2606.07636)

**<font color=#1a73e8>作者：</font>** Lecheng Yan, Yichong Zhang, Ben Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Editing a long-form video from heterogeneous footage requires more than selecting clips: an agent must preserve narrative intent across material preparation, timeline construction, post-production, and revision while leaving enough evidence to diagnose failures. We present \textbf{Crayotter}, an open-source multimodal multi-agent system for prompt-driven video editing. Crayotter organizes production into three phases: coverage-aware material preparation, artifact-based editing research, and tool-grounded timeline execution. Each phase externalizes inspectable artifacts, including coverage reports, multimodal analyses, editing blueprints, tool calls, and intermediate renders. These artifacts make an editing run traceable and allow failed segments to be diagnosed and selectively revised instead of requiring a full restart. We evaluate Crayotter on 23 editing themes against CapCut-Mate and CutClaw. Under human evaluation, Crayotter achieves an average score of 3.40/5, compared with 2.44 and 1.70 for the two baselines, with consistent gains in theme alignment, narrative coherence, and editing smoothness. We additionally describe a replayable trajectory schema and verifiable reward design that prepare these workflows for future policy optimization. Code, traces, and examples are publicly available at this https URL.

---


### 44. [Anchor-Conditioned Compositional Control for Landscape Image Generation](https://arxiv.org/abs/2606.07638)

**<font color=#1a73e8>作者：</font>** Gadha Lekshmi P, Govind Arun, Rohith Syam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image generative models, though widely used as creative tools, offer limited support for the kind of compositional control that photographers and visual artists routinely exercise. This paper presents early results on an anchor conditioned finetuning framework for landscape image generation, in which a four dimensional compositional anchor vector is extracted from training images and injected into a diffusion model via a decoupled cross attention mechanism with Fourier encoding and three way classifier free guidance dropout. Quantitative evaluation against a baseline and three ablation variants shows that the proposed architecture achieves the highest horizon detection rate of 0.850 and the highest rule of thirds alignment of 0.817. A category specific ablation further demonstrates that training on compositionally homogeneous scene subsets reduces horizon deviation by up to 40 percent compared to mixed training. This establishes that compositional control precision is category dependent.

---


### 45. [MOSS-Video-Preview: Toward Real-Time Video Understanding via Cross-Attention](https://arxiv.org/abs/2606.07639)

**<font color=#1a73e8>作者：</font>** Pengyu Wang, Chenkun Tan, Shaojun Zhou 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding is shifting from the offline paradigm -- taking a fully recorded video as input and producing a single answer after it ends -- toward real-time interaction, in which the model perceives new frames while still replying, revises its answer as new evidence appears, and remains silent when there is nothing to say. We present MOSS-Video-Preview to validate this paradigm. Our central claim is that perception must not be blocked by generation; its natural realization is a two-channel architecture. We argue that a cross-attention backbone is better suited to real-time vision-language fusion than the prevailing decoder-only design: visual features enter through a side channel rather than joining the autoregressive sequence, so perception and generation run on separate, non-blocking pathways -- reducing the frequency of visual processing and exposing a clean channel-wise interface for independent compression. We complement this with a data synthesis pipeline that converts dense captions into real-time understanding QA whose answers are revised to match what the model has perceived so far, and we specialize an offline model on these data to elicit real-time behavior. Our model trails the strong Qwen2.5-VL-7B baseline overall -- a gap we attribute primarily to data and scale rather than the architecture -- yet attains competitive offline video and multimodal understanding, remains robust on the spatial and fine-grained temporal reasoning central to real-time use, and acquires behaviors that offline models lack: continuous perception, answer revision, and timely silence. On a single H200 with 256 frames per video, it achieves about a 5x speedup in time to first token and 2.7x higher decoding throughput, with negligible degradation in offline ability. Our study of paradigm, architecture, and data outlines a viable path toward real-time video understanding.

---


### 46. [No Free Lunch for Synthetic Images under Data Scarcity Conditions](https://arxiv.org/abs/2606.07640)

**<font color=#1a73e8>作者：</font>** Borja Arroyo Galende, Alejandro Almodóvar, Patricia A. Apellániz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study investigates the trade-offs between fidelity, privacy, and utility in synthetic data generation under conditions of data scarcity and privacy sensitivity. We propose an evaluation framework that jointly assesses these three dimensions and apply it to three widely used generative models, VAE, GAN, and DDPM. The evaluation spans three image datasets, MNIST, OCTMNIST, and OrganAMNIST, encompassing both general-purpose and medical imaging domains. Notable differences arise between the three models in their behaviour when differential privacy mechanisms are introduced during training. GAN and DDPM demonstrate greater robustness, maintaining higher fidelity and downstream utility across a range of noise levels, while VAE degrades more rapidly as privacy constraints increase. This study highlights the importance of a multidimensional evaluation of deep generative models, also noting that their behaviour significantly differs when privacy techniques are applied.

---


### 47. [Do VLMs See What Sensors Feel? A Scalable Expert-Guided Design for Wheelchair Accessibility Assessment from Street View](https://arxiv.org/abs/2606.07642)

**<font color=#1a73e8>作者：</font>** Dongdong Wang, Alina Hagen, Isabelle Gatmaitan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assessing built-environment interaction, such as wheelchair accessibility, is difficult because real-world mobility is shaped by distributed, context-dependent, and temporary barriers that are hard to capture at scale. To support scalable assessment, this paper examines whether vision-language models (VLMs) can identify accessibility barriers from Google Street View (GSV) imagery. We propose an expert-guided retrieval-augmented framework that combines GSV images, ADA-informed guidance, and expert-derived rubrics to evaluate accessibility dimensions. We collect a campus-scale dataset at the University of Florida, linking 407 unique GSV locations with GPS-derived wheelchair dwell behavior as a mobility-friction signal. Results show that VLM ratings are both negatively correlated and distributionally similar with dwell time, indicating partial but consistent alignment with a behavioral proxy for mobility friction. Visual cue analysis shows that certain environmental objects, such as curb ramps and crosswalks, are associated with higher VLM accessibility scores, while alignment remains limited for subtle surface conditions, transient obstructions, and viewpoint-dependent barriers. Overall, our findings show the potential of expert-guided VLMs for scalable accessibility assessment aligning with sensor-derived indicators of real-world wheelchair navigation.

---


### 48. [FineGen: A VLM-based Multi-Agent Framework for Fine-Grained Image-Text Dataset Construction](https://arxiv.org/abs/2606.07645)

**<font color=#1a73e8>作者：</font>** Chang Kong, Yuebing Li, Peng Mo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The scarcity of hard negative samples in current vision-language datasets significantly hinders fine-grained perception. To address this, we propose FineGen, a VLM-based Multi-Agent framework for automated dataset construction. By employing a collaborative Generation-Verification-Correction pipeline with a closed-loop feedback mechanism, FineGen ensures synthesized hard negatives are semantically valid yet strictly contradictory to visual content. Applying this to ImageNet, we construct FineGen-100K, a hierarchical dataset containing over 147,000 attribute-specific hard negatives with a rigorous 1:10 positive-to-negative ratio. Extensive evaluations confirm a 96.7% attribute validity rate. Crucially, downstream validation on the FG-OVD benchmark shows that fine-tuning on FineGen-100K yields a substantial +14.4% accuracy improvement on hard samples, significantly outperforming state-of-the-art methods.

---


### 49. [DOME: Learning Transferable Domain Variables from Sparse Supervision for Test-Time Adaptation](https://arxiv.org/abs/2606.07646)

**<font color=#1a73e8>作者：</font>** Xiaoran Xu, Yifan Xu, Yupeng Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) aims to align a model to shifting test domains using only unlabeled streaming data. Most existing methods implicitly infer a single global domain distribution, ignoring the multidimensional and sample-specific nature of real-world domain shifts, leading to fragile adaptation. We propose DOME, an effective domain encoder that explicitly models each sample's domain in a zero-shot manner. DOME leverages vision-language pretraining to extract dense, continuous representations, parameterizes domains as distributional variables, and introduces a momentum-updated sparse domain bank for disentangled supervision. By injecting these explicit domain cues into downstream models, even a basic entropy-minimization TTA strategy achieves state-of-the-art performance across ImageNet-C, ImageNet-R, and ImageNet-Sketch, outperforming complex TTA approaches. Our results demonstrate that robust adaptation stems not from intricate adaptation algorithms, but from explicit, structured domain representation.

---


### 50. [AQIFormer: A Transformer-Based Multi-View Architecture for Cross-City Air Quality Classification](https://arxiv.org/abs/2606.07648)

**<font color=#1a73e8>作者：</font>** Om Kathalkar, Nitin Nilesh, Sachin Chaudhari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Air pollution represents one of the most critical environmental and public health challenges globally, with traditional sensor-based monitoring systems facing significant scalability and economic constraints. Image-based air quality estimation has emerged as a promising alternative, leveraging the visual characteristics of atmospheric pollutants in traffic scenes. However, existing methods suffer from limited cross-city generalization and inadequate exploitation of multi-view perspectives. We present AQIFormer, a novel transformer-based ensemble architecture that addresses these fundamental limitations through innovative dual-view integration, weather-aware attention mechanisms, and comprehensive multi-task learning. Our approach uniquely combines front and rear traffic imagery with meteorological parameters to achieve robust air quality classification across diverse urban environments. Extensive evaluation on a comprehensive dataset of 26,678 synchronized front-rear image pairs demonstrates good performance with 89.96% accuracy, representing a 14.96% improvement over state-of-the-art methods. Most importantly, our model maintains exceptional cross-city generalization capabilities, achieving 81.67% accuracy on an independent dataset collected in Nagpur, India with only 8.29% performance degradation using few-shot adaptation with minimal training samples.

---


> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
