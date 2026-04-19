# 📦 其他研究 | 2026年04月20日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

---

### 1. [NuHF Claw: A Risk Constrained Cognitive Agent Framework for Human Centered Procedure Support in Digital Nuclear Control Rooms](https://arxiv.org/abs/2604.14160)

**<font color=#1a73e8>作者：</font>** Xingyu Xiao, Jiejuan Tong, Jun Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid digitization of nuclear power plant main control rooms has fundamentally reshaped operator interaction patterns, introducing complex soft-control behaviors and elevated cognitive risks that are not adequately addressed by existing human reliability analysis approaches. Although recent advances in large language models and autonomous agents offer new opportunities for intelligent decision support, their deployment in safety critical environments remains constrained by risks of hallucinated reasoning and weakened human authority. This study proposes NuHF Claw, a persistent cognitive-risk agent framework that enables risk governed human centered autonomy for digital nuclear operations. The core methodological innovation lies in the introduction of a risk constrained agent runtime, which tightly couples cognitive state inference with probabilistic safety assessment to regulate autonomous system behavior in real time. By integrating cognitively grounded workload and situational awareness estimation with dynamic human error probability prediction, the framework transforms conventional offline reliability analysis into a proactive intervention mechanism embedded directly within operational workflows. Experimental validation on a high-fidelity digital control room simulator demonstrates that NuHF Claw can anticipate interface induced cognitive degradation, dynamically constrain unsafe autonomous recommendations, and provide risk-aware navigational guidance while preserving human decision authority. The results highlight a fundamental shift from automation-driven operation toward cognition-aware autonomy, offering a principled pathway for the safe integration of intelligent agents into next-generation nuclear control environments.

---


### 2. [Decoupling Scores and Text: The Politeness Principle in Peer Review](https://arxiv.org/abs/2604.14162)

**<font color=#1a73e8>作者：</font>** Yingxuan Wen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Authors often struggle to interpret peer review feedback, deriving false hope from polite comments or feeling confused by specific low scores. To investigate this, we construct a dataset of over 30,000 ICLR 2021-2025 submissions and compare acceptance prediction performance using numerical scores versus text reviews. Our experiments reveal a significant performance gap: score-based models achieve 91% accuracy, while text-based models reach only 81% even with large language models, indicating that textual information is considerably less reliable. To explain this phenomenon, we first analyze the 9% of samples that score-based models fail to predict, finding their score distributions exhibit high kurtosis and negative skewness, which suggests that individual low scores play a decisive role in rejection even when the average score falls near the borderline. We then examine why text-based accuracy significantly lags behind scores from a review sentiment perspective, revealing the prevalence of the Politeness Principle: reviews of rejected papers still contain more positive than negative sentiment words, masking the true rejection signal and making it difficult for authors to judge outcomes from text alone.

---


### 3. [EviSearch: A Human in the Loop System for Extracting and Auditing Clinical Evidence for Systematic Reviews](https://arxiv.org/abs/2604.14165)

**<font color=#1a73e8>作者：</font>** Naman Ahuja, Saniya Mulla, Muhammad Ali Khan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present EviSearch, a multi-agent extraction system that automates the creation of ontology-aligned clinical evidence tables directly from native trial PDFs while guaranteeing per-cell provenance for audit and human verification. EviSearch pairs a PDF-query agent (which preserves rendered layout and figures) with a retrieval-guided search agent and a reconciliation module that forces page-level verification when agents disagree. The pipeline is designed for high-precision extraction across multimodal evidence sources (text, tables, figures) and for generating reviewer-actionable provenance that clinicians can inspect and correct. On a clinician-curated benchmark of oncology trial papers, EviSearch substantially improves extraction accuracy relative to strong parsed-text baselines while providing comprehensive attribution coverage. By logging reconciler decisions and reviewer edits, the system produces structured preference and supervision signals that bootstrap iterative model improvement. EviSearch is intended to accelerate living systematic review workflows, reduce manual curation burden, and provide a safe, auditable path for integrating LLM-based extraction into evidence synthesis pipelines.

---


### 4. [SAGE Celer 2.6 Technical Card](https://arxiv.org/abs/2604.14168)

**<font color=#1a73e8>作者：</font>** SAGEA Research Team, Basab Jha, Firoj Paudel 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce SAGE Celer 2.6, the latest in our line of general-purpose Celer models from SAGEA. Celer 2.6 is available in 5B, 10B, and 27B parameter sizes and benefits from extensive architectural modifications and further pre-training on an undisclosed model. Using our Inverse Reasoning (IR) pipeline, SAGEA natively trains Celer 2.6 to validate its own logic paths, minimizing cascading error and hallucination in complex reasoning tasks. Celer 2.6 also boasts natively integrated multimodal functionality with an end-to-end vision encoder to avoid common pitfalls in adapter-based approaches. Celer 2.6 provides highly competitive results on mathematics, coding, and general intelligence benchmarks (ACUMEN), along with low latency. Most importantly, Celer 2.6 is specifically optimized for South Asian language support, with a custom tokenizer for the Devanagari script and strong performance in both Nepali and Hindi without sacrificing English reasoning ability.

---


### 5. [The Devil Is in Gradient Entanglement: Energy-Aware Gradient Coordinator for Robust Generalized Category Discovery](https://arxiv.org/abs/2604.14176)

**<font color=#1a73e8>作者：</font>** Haiyang Zheng, Nan Pu, Yaqi Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalized Category Discovery (GCD) leverages labeled data to categorize unlabeled samples from known or unknown classes. Most previous methods jointly optimize supervised and unsupervised objectives and achieve promising results. However, inherent optimization interference still limits their ability to improve further. Through quantitative analysis, we identify a key issue, i.e., gradient entanglement, which 1) distorts supervised gradients and weakens discrimination among known classes, and 2) induces representation-subspace overlap between known and novel classes, reducing the separability of novel categories. To address this issue, we propose the Energy-Aware Gradient Coordinator (EAGC), a plug-and-play gradient-level module that explicitly regulates the optimization process. EAGC comprises two components: Anchor-based Gradient Alignment (AGA) and Energy-aware Elastic Projection (EEP). AGA introduces a reference model to anchor the gradient directions of labeled samples, preserving the discriminative structure of known classes against the interference of unlabeled gradients. EEP softly projects unlabeled gradients onto the complement of the known-class subspace and derives an energy-based coefficient to adaptively scale the projection for each unlabeled sample according to its degree of alignment with the known subspace, thereby reducing subspace overlap without suppressing unlabeled samples that likely belong to known classes. Experiments show that EAGC consistently boosts existing methods and establishes new state-of-the-art results. Code is available at this https URL.

---


### 6. [Attention to Mamba: A Recipe for Cross-Architecture Distillation](https://arxiv.org/abs/2604.14191)

**<font color=#1a73e8>作者：</font>** Abhinav Moudgil, Ningyuan Huang, Eeshan Gunesh Dhekane 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs) such as Mamba have become a popular alternative to Transformer models, due to their reduced memory consumption and higher throughput at generation compared to their Attention-based counterparts. On the other hand, the community has built up a considerable body of knowledge on how to train Transformers, and many pretrained Transformer models are readily available. To facilitate the adoption of SSMs while leveraging existing pretrained Transformers, we aim to identify an effective recipe to distill an Attention-based model into a Mamba-like architecture. In prior work on cross-architecture distillation, however, it has been shown that a naïve distillation procedure from Transformers to Mamba fails to preserve the original teacher performance, a limitation often overcome with hybrid solutions combining Attention and SSM blocks. The key argument from our work is that, by equipping Mamba with a principled initialization, we can recover an overall better recipe for cross-architectural distillation. To this end, we propose a principled two-stage approach: first, we distill knowledge from a traditional Transformer into a linearized version of Attention, using an adaptation of the kernel trick. Then, we distill the linearized version into an adapted Mamba model that does not use any Attention block. Overall, the distilled Mamba model is able to preserve the original Pythia-1B Transformer performance in downstream tasks, maintaining a perplexity of 14.11 close to the teacher's 13.86. To show the efficacy of our recipe, we conduct thorough ablations at 1B scale with 10B tokens varying sequence mixer architecture, scaling analysis on model sizes and total distillation tokens, and a sensitivity analysis on tokens allocation between stages.

---


### 7. [QualiaNet: An Experience-Before-Inference Network](https://arxiv.org/abs/2604.14193)

**<font color=#1a73e8>作者：</font>** Paul Linton  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human 3D vision involves two distinct stages: an Experience Module, where stereo depth is extracted relative to fixation, and an Inference Module, where this experience is interpreted to estimate 3D scene properties. Paradoxically, although our experience of stereo vision does not provide us with distance information, it does affect our inferences about visual scale. We propose the Inference Module exploits a natural scene statistic: near scenes produce vivid disparity gradients, while far scenes appear comparatively flat. QualiaNet implements this two-stage architecture computationally: disparity maps simulating human stereo experience are passed to a CNN trained to estimate distance. The network can recover distance from disparity gradients alone, validating this approach.

---


### 8. [Portfolio Optimization Proxies under Label Scarcity and Regime Shifts via Bayesian and Deterministic Students under Semi-Supervised Sandwich Training](https://arxiv.org/abs/2604.14206)

**<font color=#1a73e8>作者：</font>** Adhiraj Chattopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a machine learning assisted portfolio optimization framework designed for low data environments and regime uncertainty. We construct a teacher student learning pipeline in which a Conditional Value at Risk (CVaR) optimizer generates supervisory labels, and neural models (Bayesian and deterministic) are trained using both real and synthetically augmented data. The synthetic data is generated using a factor based model with t copula residuals, enabling training beyond the limited real sample of 104 labeled observations. We evaluate four student models under a structured experimental framework comprising (i) controlled synthetic experiments (3 x 5 seed grid), (ii) in-distribution real market evaluation (C2A) and (iii) cross-universe generalization (D2A). In real-market settings, models are deployed using a rolling evaluation protocol where a frozen pretrained model is periodically fine tuned on recent observations and reset to its base state, ensuring stability while allowing limited adaptation. Results show that student models can match or outperform the CVaR teacher in several settings, while achieving improved robustness under regime shifts and reduced turnover. These findings suggest that hybrid optimization learning approaches can enhance portfolio construction in data constrained environments

---


### 9. [Towards Verified and Targeted Explanations through Formal Methods](https://arxiv.org/abs/2604.14209)

**<font color=#1a73e8>作者：</font>** Hanchen David Wang, Diego Manzanas Lopez, Preston K. Robinette 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As deep neural networks are deployed in safety-critical domains such as autonomous driving and medical diagnosis, stakeholders need explanations that are interpretable but also trustworthy with formal guarantees. Existing XAI methods fall short: heuristic attribution techniques (e.g., LIME, Integrated Gradients) highlight influential features but offer no mathematical guarantees about decision boundaries, while formal methods verify robustness yet remain untargeted, analyzing the nearest boundary regardless of whether it represents a critical risk. In safety-critical systems, not all misclassifications carry equal consequences; confusing a "Stop" sign for a "60 kph" sign is far more dangerous than confusing it with a "No Passing" sign. We introduce ViTaX (Verified and Targeted Explanations), a formal XAI framework that generates targeted semifactual explanations with mathematical guarantees. For a given input (class y) and a user-specified critical alternative (class t), ViTaX: (1) identifies the minimal feature subset most sensitive to the y->t transition, and (2) applies formal reachability analysis to guarantee that perturbing these features by epsilon cannot flip the classification to t. We formalize this through Targeted epsilon-Robustness, certifying whether a feature subset remains robust under perturbation toward a specific target class. ViTaX is the first method to provide formally guaranteed explanations of a model's resilience against user-identified alternatives. Evaluations on MNIST, GTSRB, EMNIST, and TaxiNet demonstrate over 30% fidelity improvement with minimal explanation cardinality.

---


### 10. [Chinese Language Is Not More Efficient Than English in Vibe Coding: A Preliminary Study on Token Cost and Problem-Solving Rate](https://arxiv.org/abs/2604.14210)

**<font color=#1a73e8>作者：</font>** Simiao Ren, Xingyu Shen, Yuchen Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A claim has been circulating on social media and practitioner forums that Chinese prompts are more token-efficient than English for LLM coding tasks, potentially reducing costs by up to 40\%. This claim has influenced developers to consider switching to Chinese for ``vibe coding'' to save on API costs. In this paper, we conduct a rigorous empirical study using SWE-bench Lite, a benchmark of software engineering tasks, to evaluate whether this claim of Chinese token efficiency holds up to scrutiny. Our results reveal three key findings: First, the efficiency advantage of Chinese is not observed. Second, token cost varies by model architecture in ways that defy simple assumptions: while MiniMax-2.7 shows 1.28x higher token costs for Chinese, GLM-5 actually consumes fewer tokens with Chinese prompts. Third, and most importantly, we found that the success rate when prompting in Chinese is generally lower than in English across all models we tested. We also measure cost efficiency as expected cost per successful task -- jointly accounting for token consumption and task resolution rate. These findings should be interpreted as preliminary evidence rather than a definitive conclusion, given the limited number of models evaluated and the narrow set of benchmarks tested due to resource constraints; they indicate that language effects on token cost are model-dependent, and that practitioners should not expect cost savings or performance gains just by switching their prompt language to Chinese.

---


### 11. [Fun-TSG: A Function-Driven Multivariate Time Series Generator with Variable-Level Anomaly Labeling](https://arxiv.org/abs/2604.14221)

**<font color=#1a73e8>作者：</font>** Pierre Lotte, André Péninou, Olivier Teste  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of anomaly detection methods in multivariate time series remains an open challenge, largely due to the limitations of existing benchmark datasets. Current resources often lack fine-grained anomaly annotations, do not provide explicit intervariable and temporal dependencies, and offer little insight into the underlying generative mechanisms. These shortcomings hinder the development and rigorous comparison of detection models, especially those targeting interpretable and variable-specific outputs. To address this gap, we introduce Fun-TSG, a fully customizable time series generator designed to support high-quality evaluation of anomaly detection systems. Our tool enables both fully automated generation, based on randomly sampled dependency structures and anomaly types, and manual generation through user-defined equations and anomaly configurations. In both cases, it provides full transparency over the data generation process, including access to ground-truth anomaly labels at the variable and timestamp levels. Fun-TSG supports the creation of diverse, interpretable, and reproducible benchmarking scenarios, enabling fine-grained performance analysis for both classical and modern anomaly detection models.

---


### 12. [Shapley Value-Guided Adaptive Ensemble Learning for Explainable Financial Fraud Detection with U.S. Regulatory Compliance Validation](https://arxiv.org/abs/2604.14231)

**<font color=#1a73e8>作者：</font>** Mohammad Nasir Uddin, Md Munna Aziz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial crime costs U.S. institutions over $32 billion each year. Although AI tools for fraud detection have become more advanced, their use in real-world systems still faces a major obstacle: many of these models operate as black boxes that cannot provide the transparent, auditable explanations required by regulations such as OCC Bulletin 2011-12 and Federal Reserve SR 11-7. This study makes three main contributions. First, it offers a thorough evaluation of explanation quality across faithfulness (sufficiency and comprehensiveness at k=5, 10, and 15) and stability (Kendall's W across 30 bootstrap samples). XGBoost paired with TreeExplainer achieves near-perfect stability (W=0.9912), while LSTM with DeepExplainer shows weak results (W=0.4962). Second, the paper introduces the SHAP-Guided Adaptive Ensemble (SGAE), which dynamically adjusts per-transaction ensemble weights based on SHAP attribution agreement, achieving the highest AUC-ROC among all tested models (0.8837 held-out; 0.9245 cross-validation). Third, a complete three-architecture evaluation of LSTM, Transformer, and GNN-GraphSAGE on the full 590,540-transaction IEEE-CIS dataset is provided, with GNN-GraphSAGE achieving AUC-ROC 0.9248 and F1=0.6013. All results are mapped directly to OCC, SR 11-7, and BSA-AML regulatory compliance requirements.

---


### 13. [Explainable Graph Neural Networks for Interbank Contagion Surveillance: A Regulatory-Aligned Framework for the U.S. Banking Sector](https://arxiv.org/abs/2604.14232)

**<font color=#1a73e8>作者：</font>** Mohammad Nasir Uddin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Spatial-Temporal Graph Attention Network (ST-GAT) framework was created to serve as an explainable GNN-based solution for detecting bank distress early warning signs and for conducting macro-prudential surveillance of the interbank system in the United States. The ST-GAT framework models 8,103 FDIC insured institutions across 58 quarterly snapshots (2010Q1-2024Q2). Bilateral exposures were reconstructed from publicly available FDIC Call Reports using maximum entropy estimation to produce a dynamic directed weighted graph. The framework achieves the highest AUPRC among all GNN architectures (0.939 +/- 0.010), trailing only XGBoost (0.944). Ablation analysis confirms the BiLSTM temporal component contributes +0.020 AUPRC; temporal attention weights exhibit a monotonically decreasing pattern consistent with long-run structural vulnerability weighting. Permutation importance identifies ROA (0.309) and NPL Ratio (0.252) as dominant predictors, consistent with post-mortem analyses of the 2023 regional banking crisis. All data are publicly available FDIC Call Reports and FRED series; all code and results are released.

---


### 14. [Anomaly Detection in IEC-61850 GOOSE Networks: Evaluating Unsupervised and Temporal Learning for Real-Time Intrusion Detection](https://arxiv.org/abs/2604.14233)

**<font color=#1a73e8>作者：</font>** Joseph Moore  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The IEC-61850 GOOSE protocol underpins time-critical communication in modern digital substations but lacks native security mechanisms, leaving it vulnerable to replay, masquerade, and data injection attacks. Intrusion detection in this setting is challenging due to strict latency constraints (sub-4ms) and limited availability of labeled attack data. This paper evaluates whether unsupervised temporal modeling can provide effective and deployable anomaly detection for GOOSE networks. Five models are compared on the ERENO IEC-61850 dataset: a supervised Random Forest baseline, a feedforward Autoencoder, and three recurrent sequence autoencoders (RNN, LSTM, and GRU). The supervised Random Forest achieves the highest detection performance (F1=0.9516) but fails to meet real-time constraints at 21.8ms per prediction. All four unsupervised models satisfy the 4ms requirement, with the GRU achieving the best accuracy to latency tradeoff among them (F1=0.8737 at 1.118ms). A cross-environment evaluation on an independent dataset shows that all models degrade under distribution shift. However, recurrent models retain substantially higher relative performance than the supervised baseline, suggesting that temporal sequence modeling generalizes better than fitting labeled attack distributions. Anomaly thresholds for the unsupervised models are selected on a held out validation partition to avoid test set leakage. These results support unsupervised temporal models as a practical choice for real-time GOOSE intrusion detection, particularly in environments where labeled training data may be unavailable or where large-scale deployment across diverse substations is required.

---


### 15. [Graph-Based Fraud Detection with Dual-Path Graph Filtering](https://arxiv.org/abs/2604.14235)

**<font color=#1a73e8>作者：</font>** Wei He, Wensheng Gan, Philip S. Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fraud detection on graph data can be viewed as a demanding task that requires distinguishing between different types of nodes. Because graph neural networks (GNNs) are naturally suited for processing information encoded in graph form through their message-passing operations, methods based on GNN models have increasingly attracted attention in the fraud detection domain. However, fraud graphs inherently exhibit relation camouflage, high heterophily, and class imbalance, causing most GNNs to underperform in fraud detection tasks. To address these challenges, this paper proposes a Graph-Based Fraud Detection Model with Dual-Path Graph Filtering (DPF-GFD). DPF-GFD first applies a beta wavelet-based operator to the original graph to capture key structural patterns. It then constructs a similarity graph from distance-based node representations and applies an improved low-pass filter. The embeddings from the original and similarity graphs are fused through supervised representation learning to obtain node features, which are finally used by an ensemble tree model to assess the fraud risk of unlabeled nodes. Unlike existing single-graph smoothing approaches, DPF-GFD introduces a frequency-complementary dual-path filtering paradigm tailored for fraud detection, explicitly decoupling structural anomaly modeling and feature similarity modeling. This design enables more discriminative and stable node representations in highly heterophilous and imbalanced fraud graphs. Comprehensive experiments on four real-world financial fraud detection datasets demonstrate the effectiveness of our proposed method.

---


### 16. [Interpretable and Explainable Surrogate Modeling for Simulations: A State-of-the-Art Survey and Perspectives on Explainable AI for Decision-Making](https://arxiv.org/abs/2604.14240)

**<font color=#1a73e8>作者：</font>** Pramudita Satria Palar, Paul Saves, Muhammad Daffa Robani 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The simulation of complex systems increasingly relies on sophisticated but fundamentally opaque computational black-box simulators. Surrogate models play a central role in reducing the computational cost of complex systems simulations across a wide range of scientific and engineering domains. Notwithstanding, they inevitably inherit and often exacerbate this black-box nature, obscuring how input variables drive physical responses. Conversely, Explainable Artificial Intelligence (XAI) offers powerful tools to unpack these models. Yet, XAI methods struggle with engineering-specific constraints, such as highly correlated inputs, dynamical systems, and rigorous reliability requirements. Consequently, surrogate modeling and XAI have largely evolved as distinct fields of research, despite their strong complementarity. To reconnect these approaches, this state-of-the-art survey provides a structured perspective that maps existing XAI techniques onto the various stages of surrogate modeling workflows for design and exploration. To ground this synthesis, we draw upon illustrative applications across both equation-based simulations and agent-based modeling. We survey a broad spectrum of techniques, highlighting their strengths for revealing interactions and supporting human comprehension. Finally, we identify pressing open challenges, including the explainability of dynamical systems and the handling of mixed-variable systems, and propose a research agenda to make explainability a core, embedded element of simulation-driven workflows from model construction through decision-making. By transforming opaque emulators into explainable tools, this agenda empowers practitioners to move beyond accelerating simulations to extracting actionable insights from complex system behaviors.

---


### 17. [Sovereign 2.0: Control-Plane Sovereignty for Cloud Systems Under Disruption](https://arxiv.org/abs/2604.14242)

**<font color=#1a73e8>作者：</font>** Justin Stark, Scott Wilkie  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud sovereignty can no longer be defined by data residency or infrastructure location alone. Under conditions of geopolitical disruption, legal exposure, and expanding service boundaries, sovereignty must be understood as enforceable control over how digital services are governed, operated, and recovered.
This paper introduces Sovereign 2.0, a control-plane-centric model that extends sovereignty beyond localisation to include governance authority, privileged access, cryptographic trust, data lifecycle control, observability, and incident response across federated environments. We define management sovereignty as the sovereign ability to govern, operate, evidence, and recover services regardless of underlying infrastructure dependencies.
To operationalise this model, we propose a three-layer risk-assurance framework spanning governance, operational, and technical controls, enabling sovereign outcomes to be specified and continuously evidenced under both steady-state and crisis conditions. We further position post-quantum-ready cryptographic control, particularly TLS and key custody, as foundational to long-term sovereign trust.
These contributions reframe sovereignty as an evidence-backed control system rather than a property of location, with implications for cloud architecture, procurement, and resilience design.

---


### 18. [Optimistic Policy Learning under Pessimistic Adversaries with Regret and Violation Guarantees](https://arxiv.org/abs/2604.14243)

**<font color=#1a73e8>作者：</font>** Sourav Ganguly, Kartik Pandit, Arnob Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world decision-making systems operate in environments where state transitions depend not only on the agent's actions, but also on \textbf{exogenous factors outside its control}--competing agents, environmental disturbances, or strategic adversaries--formally, $s_{h+1} = f(s_h, a_h, \bar{a}_h)+\omega_h$ where $\bar{a}_h$ is the adversary/external action, $a_h$ is the agent's action, and $\omega_h$ is an additive noise. Ignoring such factors can yield policies that are optimal in isolation but \textbf{fail catastrophically in deployment}, particularly when safety constraints must be satisfied.
Standard Constrained MDP formulations assume the agent is the sole driver of state evolution, an assumption that breaks down in safety-critical settings. Existing robust RL approaches address this via distributional robustness over transition kernels, but do not explicitly model the \textbf{strategic interaction} between agent and exogenous factor, and rely on strong assumptions about divergence from a known nominal model.
We model the exogenous factor as an \textbf{adversarial policy} $\bar{\pi}$ that co-determines state transitions, and ask how an agent can remain both optimal and safe against such an adversary. \emph{To the best of our knowledge, this is the first work to study safety-constrained RL under explicit adversarial dynamics}. We propose \textbf{Robust Hallucinated Constrained Upper-Confidence RL} (\texttt{RHC-UCRL}), a model-based algorithm that maintains optimism over both agent and adversary policies, explicitly separating epistemic from aleatoric uncertainty. \texttt{RHC-UCRL} achieves sub-linear regret and constraint violation guarantees.

---


### 19. [Metric-Aware Principal Component Analysis (MAPCA):A Unified Framework for Scale-Invariant Representation Learning](https://arxiv.org/abs/2604.14249)

**<font color=#1a73e8>作者：</font>** Michael Leznik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Metric-Aware Principal Component Analysis (MAPCA), a unified framework for scale-invariant representation learning based on the generalised eigenproblem max Tr(W^T Sigma W) subject to W^T M W = I, where M is a symmetric positive definite metric matrix. The choice of M determines the representation geometry. The canonical beta-family M(beta) = Sigma^beta, beta in [0,1], provides continuous spectral bias control between standard PCA (beta=0) and output whitening (beta=1), with condition number kappa(beta) = (lambda_1/lambda_p)^(1-beta) decreasing monotonically to isotropy. The diagonal metric M = D = diag(Sigma) recovers Invariant PCA (IPCA), a method rooted in Frisch (1928) diagonal regression, as a distinct member of the broader framework. We prove that scale invariance holds if and only if the metric transforms as M_tilde = CMC under rescaling C, a condition satisfied exactly by IPCA but not by the general beta-family at intermediate values.
Beyond its classical interpretation, MAPCA provides a geometric language that unifies several self-supervised learning objectives. Barlow Twins and ZCA whitening correspond to beta=1 (output whitening); VICReg's variance term corresponds to the diagonal metric. A key finding is that W-MSE, despite being described as a whitening-based method, corresponds to M = Sigma^{-1} (beta = -1), outside the spectral compression range entirely and in the opposite spectral direction to Barlow Twins. This distinction between input and output whitening is invisible at the level of loss functions and becomes precise only within the MAPCA framework.

---


### 20. [Head Count: Privacy-Preserving Face-Based Crowd Monitoring](https://arxiv.org/abs/2604.14250)

**<font color=#1a73e8>作者：</font>** Fatemeh Marzani, Thijs van Ede, Geert Heijenk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An important aspect of crowd monitoring is knowing how many people we are dealing with. Sometimes, knowing the size of a crowd in a single location and at a specific moment is enough. Matters become problematic when counting the same people across dif ferent locations or counting them over longer periods of time. In those cases, we need to identify and later reidentify a person, which immediately leads to privacy concerns. Until recently, solutions have been based on unique identification of carry-on devices, yet privacy improvements have caused transmitted information to be randomized, rendering this technique mostly useless. We propose to use biometric data instead. We introduce a pipeline that counts people based on face recognition, yet without ever being able to reveal the identity of individuals. To count, a camera initially detects a face, extracts its features, and derives an identifier using a fuzzy extractor. The original facial image is then deleted. Identifiers are inserted into homomorphically encrypted Bloom filters. This allows oblivious set membership testing directly on encrypted data, enabling the system to count across locations or across different moments, without revealing any identities. We provide an initial evaluation of our method that shows promising results.

---


### 21. [Calibrate-Then-Delegate: Safety Monitoring with Risk and Budget Guarantees via Model Cascades](https://arxiv.org/abs/2604.14251)

**<font color=#1a73e8>作者：</font>** Edoardo Pona, Milad Kazemi, Mehran Hosseini 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monitoring LLM safety at scale requires balancing cost and accuracy: a cheap latent-space probe can screen every input, but hard cases should be escalated to a more expensive expert. Existing cascades delegate based on probe uncertainty, but uncertainty is a poor proxy for delegation benefit, as it ignores whether the expert would actually correct the error. To address this problem, we introduce Calibrate-Then-Delegate (CTD), a model-cascade approach that provides probabilistic guarantees on the computation cost while enabling instance-level (streaming) decisions. CTD builds on a novel delegation value (DV) probe, a lightweight model operating on the same internal representations as the safety probe that directly predicts the benefit of escalation. To enforce budget constraints, CTD calibrates a threshold on the DV signal using held-out data via multiple hypothesis testing, yielding finite-sample guarantees on the delegation rate. Evaluated on four safety datasets, CTD consistently outperforms uncertainty-based delegation at every budget level, avoids harmful over-delegation, and adapts budget allocation to input difficulty without requiring group labels.

---


### 22. [Formalizing Kantian Ethics: Formula of the Universal Law Logic (FULL)](https://arxiv.org/abs/2604.14254)

**<font color=#1a73e8>作者：</font>** Taylor Olson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The field of machine ethics aims to build Artificial Moral Agents (AMAs) to better understand morality and make AI agents safer. To do so, many approaches encode human moral intuition as a set of axioms on actions e.g., do not harm, you must help others. However, this introduces (at least) two limitations for future AMAs. First, it does not consider the agent's purposes in performing the action. Second, it assumes that we humans can enumerate our moral intuition. This paper explores formalizing a moral procedure that alleviates these two limitations. We specifically consider Kantian ethics and present a multi-sorted quantified modal logic we call the Formula of the Universal Law Logic (FULL). The FULL formalizes Kant's first formulation of the categorical imperative, the Formula of the Universal Law (FUL), and concepts such as causality and agency. We demonstrate on three cases from Kantian ethics that the FULL can reason to evaluate agents' actions for certain purposes without built-in moral intuition, given that it has sufficient (non-normative) background knowledge. Therefore, the FULL is a contribution towards more robust and autonomous AMAs, and a more formal understanding of Kantian ethics.

---


### 23. [GUI-Perturbed: Domain Randomization Reveals Systematic Brittleness in GUI Grounding Models](https://arxiv.org/abs/2604.14262)

**<font color=#1a73e8>作者：</font>** Yangyue Wang, Harshvardhan Sikka, Yash Mathur 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GUI grounding models report over 85% accuracy on standard benchmarks, yet drop 27-56 percentage points when instructions require spatial reasoning rather than direct element naming. Current benchmarks miss this because they evaluate each screenshot once with a single fixed instruction. We introduce GUI-Perturbed, a controlled perturbation framework that independently varies visual scenes and instructions to measure grounding robustness. Evaluating three 7B models from the same architecture lineage, we find that relational instructions cause systematic accuracy collapse across all models, a 70% browser zoom produces statistically significant degradation, and rank-8 LoRA fine-tuning with augmented data degrades performance rather than improving it. By perturbing along independent axes, GUI-Perturbed isolates which specific capability axes are affected-spatial reasoning, visual robustness, reasoning calibration-providing diagnostic signal that aggregate benchmarks cannot. We release the dataset, augmentation pipeline, and a fine-tuned model.

---


### 24. [Reinforcement Learning via Value Gradient Flow](https://arxiv.org/abs/2604.14265)

**<font color=#1a73e8>作者：</font>** Haoran Xu, Kaiwen Hu, Somayeh Sojoudi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study behavior-regularized reinforcement learning (RL), where regularization toward a reference distribution (the dataset in offline RL or the base model in LLM RL finetuning) is essential to prevent value over-optimization caused by erroneous out-of-distribution extrapolation. Existing methods either rely on reparameterized policy gradient, which are difficult to scale to large generative models, or on reject sampling, which can be overly conservative when attempting to move beyond the behavior support. In this paper, we propose Value Gradient Flow (VGF), a scalable new paradigm for behavior-regularized RL. VGF casts behavior-regularized RL as an optimal transport problem that maps the reference distribution to the value-induced optimal policy distribution. We solve this transport problem via discrete gradient flow, where value gradients guide particles initialized from the reference distribution. Our analysis shows that VGF imposes regularization implicitly by controlling the transport budget. VGF eliminates explicit policy parameterization while remaining expressive and flexible, this enables adaptive test-time scaling by adjusting the transport budget. Extensive experiments demonstrate that VGF significantly outperforms prior methods, achieving state-of-the-art results on offline RL benchmarks (D4RL, OGBench) and LLM RL tasks. Code and runs can be found at this https URL.

---


### 25. ["I Just Don't Want My Work Being Fed Into The AI Blender": Queer Artists on Refusing and Resisting Generative AI](https://arxiv.org/abs/2604.14266)

**<font color=#1a73e8>作者：</font>** Jordan Taylor, Joel Mire, Alicia DeVrio 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Art-making is a collective social activity through which queer people engage in political resistance, develop identities, archive queer memory, and form community. However, in recent years, generative AI has disrupted queer artistic communities. Through 15 semi-structured interviews, we examine how queer artists are making sense of the encroachment of GenAI into their art worlds. Our findings surface significant tensions between the relationality of our participants' queer art practices and the perceived anti-relationality of GenAI development and use. We detail how our participants refuse and resist GenAI use and development in response and highlight the limited role our participants saw for GenAI within art-making, such as the queer aesthetic potential of surreal image models. Drawing on queer theory, we discuss how CSCW researchers might support queer artists by refusing dominant AI imaginaries and supporting queer world-building.

---


### 26. [Quantum-inspired tensor networks in machine learning models](https://arxiv.org/abs/2604.14287)

**<font color=#1a73e8>作者：</font>** Guillermo Valverde, Igor García-Olaizola, Giannicola Scarpa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensor networks were developed in the context of many-body physics as compressed representations of multiparticle quantum states. These representations mitigate the exponential complexity of many-body systems by capturing only the most relevant dependencies. Due to the formal similarity between quantum entanglement and statistical correlations, tensor networks have recently been integrated in machine learning, operating both as alternative learning architectures and as decompositions of components of neural networks. The expectation is that the theoretical understanding of tensor networks developed within quantum many-body physics leads to novel methods that offer advantages in terms of computational efficiency, explainability, or privacy. Here we review the use of tensor networks in the context of machine learning, providing a critical assessment of the state of the art, the potential advantages, and the challenges that must be overcome.

---


### 27. [Geometrically Consistent Multi-View Scene Generation from Freehand Sketches](https://arxiv.org/abs/2604.14302)

**<font color=#1a73e8>作者：</font>** Ahmed Bourouis, Savas Ozkan, Andrea Maracani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We tackle a new problem: generating geometrically consistent multi-view scenes from a single freehand sketch. Freehand sketches are the most geometrically impoverished input one could offer a multi-view generator. They convey scene intent through abstract strokes while introducing spatial distortions that actively conflict with any consistent 3D interpretation. No prior method attempts this; existing multi-view approaches require photographs or text, while sketch-to-3D methods need multiple views or costly per-scene optimisation.
We address three compounding challenges; absent training data, the need for geometric reasoning from distorted 2D input, and cross-view consistency, through three mutually reinforcing contributions: (i) a curated dataset of $\sim$9k sketch-to-multiview samples, constructed via an automated generation and filtering pipeline; (ii) Parallel Camera-Aware Attention Adapters (CA3) that inject geometric inductive biases into the video transformer; and (iii) a Sparse Correspondence Supervision Loss (CSL) derived from Structure-from-Motion reconstructions.
Our framework synthesizes all views in a single denoising process without requiring reference images, iterative refinement, or per-scene optimization. Our approach significantly outperforms state-of-the-art two-stage baselines, improving realism (FID) by over 60% and geometric consistency (Corr-Acc) by 23%, while providing up to a 3.7$\times$ inference speedup.

---


### 28. [Interpretable Human Activity Recognition for Subtle Robbery Detection in Surveillance Videos](https://arxiv.org/abs/2604.14329)

**<font color=#1a73e8>作者：</font>** Bryan Jhoan Cazáres Leyva, Ulises Gachuz Davila, José Juan González Fonseca 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-violent street robberies (snatch-and-run) are difficult to detect automatically because they are brief, subtle, and often indistinguishable from benign human interactions in unconstrained surveillance footage. This paper presents a hybrid, pose-driven approach for detecting snatch-and-run events that combines real-time perception with an interpretable classification stage suitable for edge deployment. The system uses a YOLO-based pose estimator to extract body keypoints for each tracked person and computes kinematic and interaction features describing hand speed, arm extension, proximity, and relative motion between an aggressor-victim pair. A Random Forest classifier is trained on these descriptors, and a temporal hysteresis filter is applied to stabilize frame-level predictions and reduce spurious alarms. We evaluate the method on a staged dataset and on a disjoint test set collected from internet videos, demonstrating promising generalization across different scenes and camera viewpoints. Finally, we implement the complete pipeline on an NVIDIA Jetson Nano and report real-time performance, supporting the feasibility of proactive, on-device robbery detection.

---


### 29. [Understanding Student Experiences with TLS Client Authentication](https://arxiv.org/abs/2604.14330)

**<font color=#1a73e8>作者：</font>** Abubakar Sadiq Shittu, Clay Shubert, John Sadik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mutual TLS (mTLS) provides strong, certificate-based authentication for both clients and servers, yet its adoption for user-facing websites remains rare. This paper presents a longitudinal study of mTLS usability, tracking 46 senior and graduate computer science students who configured client certificates from scratch, used them for routine authentication over a semester-long course, and managed credentials across multiple devices. The results reveal that initial setup is a major bottleneck; while daily use was considered smooth, it did not improve long-term usability perceptions. Most concerningly, only 9% of participants fully understood the security implications of certificate-based authentication. We conclude that in a realistic, tooling-heavy deployment utilizing OpenSSL, a custom CA, and a 3072-bit minimum key requirement, even highly technical students struggled significantly. We argue this provides empirical evidence that today mTLS user experience is fundamentally misaligned with non-PKI specialists, and it is difficult to see a path toward mainstream adoption without substantial platform-level changes.

---


### 30. [Heat and Matérn Kernels on Matchings](https://arxiv.org/abs/2604.14331)

**<font color=#1a73e8>作者：</font>** Dmitry Eremeev, Salem Said, Viacheslav Borovitskiy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Applying kernel methods to matchings is challenging due to their discrete, non-Euclidean nature. In this paper, we develop a principled framework for constructing geometric kernels that respect the natural geometry of the space of matchings. To this end, we first provide a complete characterization of stationary kernels, i.e. kernels that respect the inherent symmetries of this space. Because the class of stationary kernels is too broad, we specifically focus on the heat and Matérn kernel families, adding an appropriate inductive bias of smoothness to stationarity. While these families successfully extend widely popular Euclidean kernels to matchings, evaluating them naively incurs a prohibitive super-exponential computational cost. To overcome this difficulty, we introduce and analyze a novel, sub-exponential algorithm leveraging zonal polynomials for efficient kernel evaluation. Finally, motivated by the known bijective correspondence between matchings and phylogenetic trees-a crucial data modality in biology-we explore whether our framework can be seamlessly transferred to the space of trees, establishing novel negative results and identifying a significant open problem.

---


### 31. [Thermodynamic Diffusion Inference with Minimal Digital Conditioning](https://arxiv.org/abs/2604.14332)

**<font color=#1a73e8>作者：</font>** Aditi De  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-model inference and overdamped Langevin dynamics are formally identical. A physical substrate that encodes the score function therefore equilibrates to the correct output by thermodynamics alone, requiring no digital arithmetic during inference and potentially achieving a $10{,}000\times$ reduction in energy relative to a GPU. Two fundamental barriers have until now prevented this equivalence from being realized at production scale: non-local skip connections, which locally coupled analog substrates cannot represent, and input conditioning, in which the coupling constants carry roughly $2{,}600\times$ too little signal to anchor the system to a specific input.
We resolve both obstacles. \emph{Hierarchical bilinear coupling} encodes U-Net skip connections as rank-$k$ inter-module interactions derived directly from the singular structure of the encoder and decoder Gram matrices, requiring only $O(Dk)$ physical connections instead of $O(D^2)$. A \emph{minimal digital interface} -- a 4-dimensional bottleneck encoder together with a 16-unit transfer network, totalling \textbf{2,560 parameters} -- overcomes the conditioning barrier. When evaluated on activations drawn from a trained denoising U-Net, the complete system attains a decoder cosine similarity of \textbf{0.9906} against an oracle upper bound of 1.0000, while preserving theoretical net energy savings of approximately $10^7\times$ over GPU inference. These results constitute the first demonstration of trained-weight, production-scale thermodynamic diffusion inference.

---


### 32. [When Missing Becomes Structure: Intent-Preserving Policy Completion from Financial KOL Discourse](https://arxiv.org/abs/2604.14333)

**<font color=#1a73e8>作者：</font>** Yuncong Liu, Yuan Wan, Zhou Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Key Opinion Leader (KOL) discourse on social media is widely consumed as investment guidance, yet turning it into executable trading strategies without injecting assumptions about unspecified execution decisions remains an open problem. We observe that the gaps in KOL statements are not random deficiencies but a structured separation: KOLs express directional intent (what to buy or sell and why) while leaving execution decisions (when, how much, how long) systematically unspecified. Building on this observation, we propose an intent-preserving policy completion framework that treats KOL discourse as a partial trading policy and uses offline reinforcement learning to complete the missing execution decisions around the KOL-expressed intent. Experiments on multimodal KOL discourse from YouTube and X (2022-2025) show that KICL achieves the best return and Sharpe ratio on both platforms while maintaining zero unsupported entries and zero directional reversals, and ablations confirm that the full framework yields an 18.9% return improvement over the KOL-aligned baseline.

---


### 33. [Mistake gating leads to energy and memory efficient continual learning](https://arxiv.org/abs/2604.14336)

**<font color=#1a73e8>作者：</font>** Aaron Pache, Mark CW van Rossum  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synaptic plasticity is metabolically expensive, yet animals continuously update their internal models without exhausting energy reserves. However, when artificial neural networks are trained, the network parameters are typically updated on every sample that is presented, even if the sample was classified correctly. Inspired by the human negativity bias and error-related negativity, we propose 'memorized mistake-gated learning' -- a biologically plausible plasticity rule where synaptic updates are strictly gated by current and past classification errors. This reduces the number of updates the network needs to make by $50\%\sim80\%$. Mistake gating is particularly well suited in two cases: 1) For incremental learning where new knowledge is acquired on a background of pre-existing knowledge, 2) For online learning scenarios when data needs to be stored for later replay, as mistake-gating reduces storage buffer requirements. The algorithm can be implemented in a few lines of code, adds no hyper-parameters, and comes at negligible computational overhead. Learning on mistakes is an energy efficient and biologically relevant modification to commonly used learning rules that is well suited for continual learning.

---


### 34. [Path-Sampled Integrated Gradients](https://arxiv.org/abs/2604.14338)

**<font color=#1a73e8>作者：</font>** Firuz Kamalov, Fadi Thabtah, R. Sivaraj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce path-sampled integrated gradients (PS-IG), a framework that generalizes feature attribution by computing the expected value over baselines sampled along the linear interpolation path. We prove that PS-IG is mathematically equivalent to path-weighted integrated gradients, provided the weighting function matches the cumulative distribution function of the sampling density. This equivalence allows the stochastic expectation to be evaluated via a deterministic Riemann sum, improving the error convergence rate from $O(m^{-1/2})$ to $O(m^{-1})$ for smooth models. Furthermore, we demonstrate analytically that PS-IG functions as a variance-reducing filter against gradient noise - strictly lowering attribution variance by a factor of 1/3 under uniform sampling - while preserving key axiomatic properties such as linearity and implementation invariance.

---


### 35. [Tight Sample Complexity Bounds for Best-Arm Identification Under Bounded Systematic Bias](https://arxiv.org/abs/2604.14345)

**<font color=#1a73e8>作者：</font>** Tianhao Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As search depth increases in autonomous reasoning and embodied planning, the candidate action space expands exponentially, heavily taxing computational budgets. While heuristic pruning is a common countermeasure, it operates without formal safety guarantees when surrogate models (like LLMs) exhibit systematic evaluation biases. This paper frames the node expansion process as a localized Best-Arm Identification (BAI) problem over dynamic frontiers, subject to a bounded systematic bias $L$. By inverting the Lambert W function, we establish an additive sample complexity of $\mathcal{O}((\Delta-4L)^{-2})$, which indicates that safe node elimination is only feasible when the empirical reward gap exceeds $4L$. We complement this with an information-theoretic lower bound of $\Omega((\Delta-2L)^{-2})$ to confirm the structural limits of biased search. Subsequent evaluations on both synthetic trees and complex reasoning tasks demonstrate that adhering to this local safety boundary successfully preserves optimal trajectories while maximizing sample allocation efficiency.

---


### 36. [When PCOS Meets Eating Disorders: An Explainable AI Approach to Detecting the Hidden Triple Burden](https://arxiv.org/abs/2604.14356)

**<font color=#1a73e8>作者：</font>** Apoorv Prasad, Susan McRoy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Women with polycystic ovary syndrome (PCOS) face substantially elevated risks of body image distress, disordered eating, and metabolic challenges, yet existing natural language processing approaches for detecting these conditions lack transparency and cannot identify co-occurring presentations. We developed small, open-source language models to automatically detect this triple burden in social media posts with grounded explainability. We collected 1,000 PCOS-related posts from six subreddits, with two trained annotators labeling posts using guidelines operationalizing Lee et al. (2017) clinical framework. Three models (Gemma-2-2B, Qwen3-1.7B, DeepSeek-R1-Distill-Qwen-1.5B) were fine-tuned using Low-Rank Adaptation to generate structured explanations with textual evidence. The best model achieved 75.3 percent exact match accuracy on 150 held-out posts, with robust comorbidity detection and strong explainability. Performance declined with diagnostic complexity, indicating their best use is for screening rather than autonomous diagnosis.

---


### 37. [Digital Guardians: The Past and The Future of Cyber-Physical Resilience](https://arxiv.org/abs/2604.14360)

**<font color=#1a73e8>作者：</font>** Saurabh Bagchi, Hyunseung Kim, Tarek Abdelzaher 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Resilience in cyber-physical systems (CPS) is the fundamental ability to maintain safety and critical functionality despite adverse "perturbations," which includes security attacks, environmental disruptions, and hardware or software failures. This survey provides a comprehensive review of CPS resilience, framing the field through five interconnected themes that are required in an integrated whole to achieve real-world resilience.
The article first posits that resilience is a system-wide property emerging from interactions between hardware, software, and human users. Second, it addresses the challenges of learning-enabled CPS, which often operate in data-scarce environments characterized by imbalanced or noisy data, requiring innovative solutions like synthetic data generation and foundation model adaptation. Third, the survey examines proactive measures for resilience, which include distinctive aspects of verification, testing, and redundancy. Fourth, it explores recovery mechanisms, moving beyond traditional fault models to design "just good enough" recovery strategies that prioritize safety-critical functions during perturbations. Finally, it highlights the central role of the human, focusing on the different levels of human intervention, the necessity of trust calibration, and the requirement for explainable AI to support human-CPS teaming.
These themes are illustrated through representative application domains, primarily Connected and Autonomous Transportation Systems (CATS) and Medical CPS (MCPS). By integrating the five interconnected themes, this survey provides a systematic roadmap for achieving the resilient CPS in increasingly complex and adversarial environments.

---


### 38. [SatBLIP: Context Understanding and Feature Identification from Satellite Imagery with Vision-Language Learning](https://arxiv.org/abs/2604.14373)

**<font color=#1a73e8>作者：</font>** Xue Wu, Shengting Cao, Jiaqi Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rural environmental risks are shaped by place-based conditions (e.g., housing quality, road access, land-surface patterns), yet standard vulnerability indices are coarse and provide limited insight into risk contexts. We propose SatBLIP, a satellite-specific vision-language framework for rural context understanding and feature identification that predicts county-level Social Vulnerability Index (SVI). SatBLIP addresses limitations of prior remote sensing pipelines-handcrafted features, manual virtual audits, and natural-image-trained VLMs-by coupling contrastive image-text alignment with bootstrapped captioning tailored to satellite semantics. We use GPT-4o to generate structured descriptions of satellite tiles (roof type/condition, house size, yard attributes, greenery, and road context), then fine-tune a satellite-adapted BLIP model to generate captions for unseen images. Captions are encoded with CLIP and fused with LLM-derived embeddings via attention for SVI estimation under spatial aggregation. Using SHAP, we identify salient attributes (e.g., roof form/condition, street width, vegetation, cars/open space) that consistently drive robust predictions, enabling interpretable mapping of rural risk environments.

---


### 39. [Modular Continual Learning via Zero-Leakage Reconstruction Routing and Autonomous Task Discovery](https://arxiv.org/abs/2604.14375)

**<font color=#1a73e8>作者：</font>** Noureddine Kermiche  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting remains a primary hurdle in sequential task learning for artificial neural networks. We propose a silicon-native modular architecture that achieves structural parameter isolation using Task-Specific Experts and a distributed, outlier-based Gatekeeper. Moving beyond traditional sequential consolidation, our framework utilizes a Simultaneous Pipeline where Teacher learning, Student distillation, and Router manifold acquisition occur in parallel while raw data is present in a localized training session. This approach ensures computational efficiency and complies with privacy mandates like GDPR by deleting raw data as soon as a task is learned. We demonstrate that a Tight-Bottleneck Autoencoder (TB-AE) can effectively distinguish semantically crowded manifolds in high-dimensional latent spaces, overcoming the posterior collapse inherent to standard variational methods. By establishing strict topological boundaries, our TB-AE resolves latent space crowding in 4096-D LLM embeddings to provide a robust, unsupervised novelty signal. Furthermore, we validate an Autonomous Retrieval mechanism that confidently identifies returning manifolds, enabling stable lifelong learning without redundant module instantiation. Empirical results demonstrate that our ``Live Distillation'' approach acts as a natural regularizer, achieving strong retention across computer vision and natural language processing domains without suffering a student fidelity gap.

---


### 40. [BiCon-Gate: Consistency-Gated De-colloquialisation for Dialogue Fact-Checking](https://arxiv.org/abs/2604.14389)

**<font color=#1a73e8>作者：</font>** Hyunkyung Park, Arkaitz Zubiaga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated fact-checking in dialogue involves multi-turn conversations where colloquial language is frequent yet understudied. To address this gap, we propose a conservative rewrite candidate for each response claim via staged de-colloquialisation, combining lightweight surface normalisation with scoped in-claim coreference resolution. We then introduce BiCon-Gate, a semantics-aware consistency gate that selects the rewrite candidate only when it is semantically supported by the dialogue context, otherwise falling back to the original claim. This gated selection stabilises downstream fact-checking and yields gains in both evidence retrieval and fact verification. On the DialFact benchmark, our approach improves retrieval and verification, with particularly strong gains on SUPPORTS, and outperforms competitive baselines, including a decoder-based one-shot LLM rewrite that attempts to perform all de-colloquialisation steps in a single pass.

---


### 41. [Generating Concept Lexicalizations via Dictionary-Based Cross-Lingual Sense Projection](https://arxiv.org/abs/2604.14397)

**<font color=#1a73e8>作者：</font>** David Basil, Chirooth Girigowda, Bradley Hauer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study the task of automatically expanding WordNet-style lexical resources to new languages through sense generation. We generate senses by associating target-language lemmas with existing lexical concepts via semantic projection. Given a sense-tagged English corpus and its translation, our method projects English synsets onto aligned target-language tokens and assigns the corresponding lemmas to those synsets. To generate these alignments and ensure their quality, we augment a pre-trained base aligner with a bilingual dictionary, which is also used to filter out incorrect sense projections. We evaluate the method on multiple languages, comparing it to prior methods, as well as dictionary-based and large language model baselines. Results show that the proposed project-and-filter strategy improves precision while remaining interpretable and requiring few external resources. We plan to make our code, documentation, and generated sense inventories accessible.

---


### 42. [Reflections on Traceability for Visualization Research](https://arxiv.org/abs/2604.14417)

**<font color=#1a73e8>作者：</font>** Jen Rogers, Derya Akbaba, James Scott-Brown 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Decades of advocacy for reproducibility and replication have advanced open, transparent practices in the sciences. However, traditional notions of reproducibility fit poorly with design-oriented visualization research, where insights emerge through subjective, situated, and iterative work. So how can we ensure rigor and transparency in processes that are inherently unreproducible? To introduce transparency in design-oriented research, we propose to focus on traceability: surfacing the origin and development of research contributions based on rich sets of artifacts documenting the design process. We investigated traceability through a collaborative autoethnographic reflection that builds on several years of work exploring ways to make design-oriented research transparent. This exploration includes an experiment to build a tool to support traceability, which we called tRRRacer. The tRRRacer tool provided a testbed for us to operationalize the three tenets of a traceable process: (1) Record abundant, annotated artifacts representative of research activities; (2) Report curated research threads that articulate rationale and evolution of the process, allowing others to (3) Read via interfaces that help retrace claims and assess plausibility. Reflecting on our experiences, we contribute a theorization of traceability and reflections on how we might support it.

---


### 43. [Non-intrusive Learning of Physics-Informed Spatio-temporal Surrogate for Accelerating Design](https://arxiv.org/abs/2604.14424)

**<font color=#1a73e8>作者：</font>** Sudeepta Mondal, Soumalya Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most practical engineering design problems involve nonlinear spatio-temporal dynamical systems. Multi-physics simulations are often performed to capture the fine spatio-temporal scales which govern the evolution of these systems. However, these simulations are often high-fidelity in nature, and can be computationally very expensive. Hence, generating data from these expensive simulations becomes a bottleneck in an end-to-end engineering design process. Spatio-temporal surrogate modeling of these dynamical systems has been a popular data-driven solution to tackle this computational bottleneck. This is because accurate machine learning models emulating the dynamical systems can be orders of magnitude faster than the actual simulations. However, one key limitation of purely data-driven approaches is their lack of generalizability to inputs outside the training distribution. In this paper, we propose a physics-informed spatio-temporal surrogate modeling (PISTM) framework constrained by the physics of the underlying dynamical system. The framework leverages state-of-the-art advancements in the field of Koopman autoencoders to learn the underlying spatio-temporal dynamics in a non-intrusive manner, coupled with a spatio-temporal surrogate model which predicts the behavior of the Koopman operator in a specified time window for unknown operating conditions. We evaluate our framework on a prototypical fluid flow problem of interest: two-dimensional incompressible flow around a cylinder.

---


### 44. [Three-Phase Transformer](https://arxiv.org/abs/2604.14430)

**<font color=#1a73e8>作者：</font>** Mohammad R. Abu Ayyash  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Three-Phase Transformer (3PT), a residual-stream structural prior for decoder-only Transformers on a standard SwiGLU + RMSNorm + RoPE + GQA backbone. The hidden vector is partitioned into N equally-sized cyclic channels, each maintained by phase-respecting ops: a per-channel RMSNorm, a 2D Givens rotation between attention and FFN that rotates each channel by theta + i*(2*pi/N), and a head-count constraint aligning GQA heads with the partition. The architecture is a self-stabilizing equilibrium between scrambling and re-imposition, not a bolted-on module. The partition carves out a one-dimensional DC subspace orthogonal to the channels, into which we inject a fixed Gabriel's horn profile r(p) = 1/(p+1) as an absolute-position side-channel composing orthogonally with RoPE's relative-position rotation. The canonical N=3 borrows its metaphor from balanced three-phase AC, where three sinusoids 120 degrees apart sum to zero with no anti-correlated pair. At 123M parameters on WikiText-103, 3PT achieves -7.20% perplexity (-2.62% bits-per-byte) over a matched RoPE-Only baseline at +1,536 parameters (0.00124% of total), with 1.93x step-count convergence speedup (1.64x wall-clock). N behaves as a parameter-sharing knob rather than a unique optimum: at 5.5M an N-sweep over {1,2,3,4,6,8,12} is near-monotone with N=1 winning; at 123M a three-seed sweep finds N=3 and N=1 statistically indistinguishable. The load-bearing mechanism is the channel-partitioned residual stream, per-block rotation, per-phase normalization, and horn DC injection. We characterize (a) self-stabilization of the geometry without explicit enforcement, a novel instance of the conservation-law framework for neural networks; (b) a U-shaped depth profile of rotation-angle drift at 12 layers; (c) orthogonal composition with RoPE, attention, and FFN.

---


### 45. [AndroScanner: Automated Backend Vulnerability Detection for Android Applications](https://arxiv.org/abs/2604.14431)

**<font color=#1a73e8>作者：</font>** Harini Dandu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile applications rely on complex backends that introduce significant security risks, yet developers often lack the tools to assess these risks effectively. This paper presents AndroScanner, an automated pipeline for detecting vulnerabilities in Android application backends through combined static and dynamic analysis. AndroScanner extracts backend API calls from APK files using apktool, Androguard, and Frida-based dynamic instrumentation, then vets them against the OWASP API Security Top 10 using APIFuzzer. We evaluate AndroScanner on two Android applications: a purposely vulnerable bank application and a production recruitment application with over 50,000 downloads on Google Play Store. Across both applications, AndroScanner extracted 24 APIs and identified 5 vulnerabilities, including a previously unreported zero-day Excessive Data Exposure vulnerability (ranked 3rd in the OWASP API Security Top 10) in the production application. The vulnerability was responsibly disclosed to the development team prior to publication. AndroScanner is available upon request to assist developers in identifying and remediating backend security risks before deployment.

---


### 46. [Zero-Ablation Overstates Register Content Dependence in DINO Vision Transformers](https://arxiv.org/abs/2604.14433)

**<font color=#1a73e8>作者：</font>** Felipe Parodi, Jordan Matelsky, Melanie Segado  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-ablation -- replacing token activations with zero vectors -- is widely used to probe token function in vision transformers. Register zeroing in DINOv2+registers and DINOv3 produces large drops (up to $-36.6$\,pp classification, $-30.9$\,pp segmentation), suggesting registers are functionally indispensable. However, three replacement controls -- mean-substitution, noise-substitution, and cross-image register-shuffling -- preserve performance across classification, correspondence, and segmentation, remaining within ${\sim}1$\,pp of the unmodified baseline. Per-patch cosine similarity shows these replacements genuinely perturb internal representations, while zeroing causes disproportionately large perturbations, consistent with why it alone degrades tasks. We conclude that zero-ablation overstates dependence on exact register content. In the frozen-feature evaluations we test, performance depends on plausible register-like activations rather than on exact image-specific values. Registers nevertheless buffer dense features from \texttt{[CLS]} dependence and are associated with compressed patch geometry. These findings, including the replacement-control results, replicate at ViT-B scale.

---


### 47. [On Tackling Complex Tasks with Reward Machines and Signal Temporal Logics](https://arxiv.org/abs/2604.14440)

**<font color=#1a73e8>作者：</font>** Ana María Gómez Ruiz, Thao Dang, Alexandre Donzé  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a Reinforcement Learning (RL) based control design framework for handling complex tasks. The approach extends the concept of Reward Machines (RM) with Signal Temporal Logic (STL) formulas that can be used for event generation. The use of STL allows not only a more efficient representation of rewards for complex tasks but also guiding the training process to converge towards behaviors satisfying specified requirements. We also propose an implementation of the framework that leverages the STL online monitoring algorithms. We illustrate the framework with three case studies (minigrid, cart-pole and high-way environments) with non-trivial tasks.

---


### 48. [Hierarchical vs. Flat Iteration in Shared-Weight Transformers](https://arxiv.org/abs/2604.14442)

**<font color=#1a73e8>作者：</font>** Sang-Il Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present an empirical study of whether hierarchically structured, shared-weight recurrence can match the representational quality of independent-layer stacking in a Transformer-based language model. HRM-LM replaces L independent Transformer layers with a two-speed recurrent pair: a Fast module operating at every step for local refinement, and a Slow module operating every T steps for global compression. This recurrent hierarchy is unrolled for M = N x T steps with shared parameters. The central and most robust finding, supported by a parameter-matched Universal Transformer ablation (UniTF, 1.2B) across five independent runs, is a sharp empirical gap between the two approaches.

---


### 49. [Robustness Analysis of Machine Learning Models for IoT Intrusion Detection Under Data Poisoning Attacks](https://arxiv.org/abs/2604.14444)

**<font color=#1a73e8>作者：</font>** Fortunatus Aabangbio Wulnye, Justice Owusu Agyemang, Kwame Opuni-Boachie Obour Agyekum 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ensuring the reliability of machine learning-based intrusion detection systems remains a critical challenge in Internet of Things (IoT) environments, particularly as data poisoning attacks increasingly threaten the integrity of model training pipelines. This study evaluates the susceptibility of four widely used classifiers, Random Forest, Gradient Boosting Machine, Logistic Regression, and Deep Neural Network models, against multiple poisoning strategies using three real-world IoT datasets. Results show that while ensemble-based models exhibit comparatively stable performance, Logistic Regression and Deep Neural Networks suffer degradation of up to 40% under label manipulation and outlier-based attacks. Such disruptions significantly distort decision boundaries, reduce detection fidelity, and undermine deployment readiness. The findings highlight the need for adversarially robust training, continuous anomaly monitoring, and feature-level validation within operational Network Intrusion Detection Systems. The study also emphasizes the importance of integrating resilience testing into regulatory and compliance frameworks for AI-driven IoT security. Overall, this work provides an empirical foundation for developing more resilient intrusion detection pipelines and informs future research on adaptive, attack-aware models capable of maintaining reliability under adversarial IoT conditions.

---


### 50. [Crowdsourcing of Real-world Image Annotation via Visual Properties](https://arxiv.org/abs/2604.14449)

**<font color=#1a73e8>作者：</font>** Xiaolei Diao, Fausto Giunchiglia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in data-centric artificial intelligence highlight inherent limitations in object recognition datasets. One of the primary issues stems from the semantic gap problem, which results in complex many-to-many mappings between visual data and linguistic descriptions. This bias adversely affects performance in computer vision tasks. This paper proposes an image annotation methodology that integrates knowledge representation, natural language processing, and computer vision techniques, aiming to reduce annotator subjectivity by applying visual property constraints. We introduce an interactive crowdsourcing framework that dynamically asks questions based on a predefined object category hierarchy and annotator feedback, guiding image annotation by visual properties. Experiments demonstrate the effectiveness of this methodology, and annotator feedback is discussed to optimize the crowdsourcing setup.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
