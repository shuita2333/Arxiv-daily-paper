# 📦 其他研究 | 2026年04月18日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

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


### 51. [Asynchronous Probability Ensembling for Federated Disaster Detection](https://arxiv.org/abs/2604.14450)

**<font color=#1a73e8>作者：</font>** Emanuel Teixeira Martins, Rodrigo Moreira, Larissa Ferreira Rodrigues Moreira 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quick and accurate emergency handling in Disaster Decision Support Systems (DDSS) is often hampered by network latency and suboptimal application accuracy. While Federated Learning (FL) addresses some of these issues, it is constrained by high communication costs and rigid synchronization requirements across heterogeneous convolutional neural network (CNN) architectures. To overcome these challenges, this paper proposes a decentralized ensembling framework based on asynchronous probability aggregation and feedback distillation. By shifting the exchange unit from model weights to class-probability vectors, our method maintains data privacy, reduces communication requirements by orders of magnitude, and improves overall accuracy. This approach enables diverse CNN designs to collaborate asynchronously, enhancing disaster image identification performance even in resource-constrained settings. Experimental tests demonstrate that the proposed method outperforms traditional individual backbones and standard federated approaches, establishing a scalable and resource-aware solution for real-time disaster response.

---


### 52. [FocalLens: Visualizing Narratives through Focalization](https://arxiv.org/abs/2604.14456)

**<font color=#1a73e8>作者：</font>** S M Raihanul Alam, Md Dilshadur Rahman, Md Naimul Hoque  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visualizing narratives is useful to writers to reflect on unfinished drafts and identify unintentional biases and inconsistencies. Literary scholars can use the visualizations to identify nuanced patterns and literary styles from written text. Current narrative visualization is limited to representing character and location co-occurrences in a timeline, omitting important and complex narrative components such as focalization, causality, and speech. This paper aims to capture and visualize underexplored, complex narrative components as a basis for narrative visualization. As a starting point, we propose a new narrative visualization, named FocalLens, that uses focalization, the component that establishes who sees or perceives the events in a narrative, for representing the narrative. We provide the theoretical foundation of focalization and describe various types and facets of focalization. The details are incorporated in the novel visualization that captures how different characters perceive an event, who directly participate in an event, who indirectly observe the event, and who narrate the event. We also developed a tool that provides fluid interaction between the text and the proposed visualization. The tool was evaluated with four writers and scholars in a qualitative study, where writers analyzed their draft stories and scholars analyzed well-known stories. The findings suggest the tool added a new dimension to the workflow for writers and scholars, an analytical lens that is not available otherwise. We conclude by identifying design implications and future directions.

---


### 53. [NeuroTrace: Inference Provenance-Based Detection of Adversarial Examples](https://arxiv.org/abs/2604.14457)

**<font color=#1a73e8>作者：</font>** Firas Ben Hmida, Philemon Hailemariam, Kashif Ali Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) remain largely opaque at inference time, limiting our ability to detect and diagnose malicious input manipulations such as adversarial examples. Existing detection methods predominantly rely on layer-local signals (e.g., activations or attribution scores), leaving cross-layer information flow and execution structure under-explored. We introduce NeuroTrace, a framework and open dataset for analyzing inference provenance through Inference Provenance Graphs (IPGs). IPGs are heterogeneous graphs that capture both activation behavior and parameter-induced dataflow during a model's forward pass, providing a structured representation of how information propagates through the network. NeuroTrace includes (i) a reproducible extraction engine that instruments model execution, (ii) a standardized graph representation compatible with heterogeneous GNNs, and (iii) a benchmark suite spanning multiple adversarial attack families across vision and malware domains. Using this framework, we evaluate IPG-based detectors for adversarial example detection under intra-attack, multi-attack, and cross-threat transfer settings. Our results show that inference provenance provides a strong and transferable signal for distinguishing adversarial and benign inputs, achieving consistently high detection performance and improving over prior graph-based baselines. We further analyze the conditions under which provenance-based detection generalizes across attack types, as well as the associated runtime and storage trade-offs. By releasing the dataset, extraction pipeline, and evaluation protocol, NeuroTrace enables systematic study of inference-time behavior and establishes inference provenance as a practical foundation for building more transparent and auditable machine learning systems.

---


### 54. [Filling in the Mechanisms: How do LMs Learn Filler-Gap Dependencies under Developmental Constraints?](https://arxiv.org/abs/2604.14459)

**<font color=#1a73e8>作者：</font>** Atrey Desai, Sathvik Nair  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For humans, filler-gap dependencies require a shared representation across different syntactic constructions. Although causal analyses suggest this may also be true for LLMs (Boguraev et al., 2025), it is still unclear if such a representation also exists for language models trained on developmentally feasible quantities of data. We applied Distributed Alignment Search (DAS, Geiger et al. (2024)) to LMs trained on varying amounts of data from the BabyLM challenge (Warstadt et al., 2023), to evaluate whether representations of filler-gap dependencies transfer between wh-questions and topicalization, which greatly vary in terms of their input frequency. Our results suggest shared, yet item-sensitive mechanisms may develop with limited training data. More importantly, LMs still require far more data than humans to learn comparable generalizations, highlighting the need for language-specific biases in models of language acquisition.

---


### 55. [Bias in Surface Electromyography Features across a Demographically Diverse Cohort](https://arxiv.org/abs/2604.14460)

**<font color=#1a73e8>作者：</font>** Aditi Agrawal, Celine John Philip, Giancarlo K. Sagastume 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Neuromotor decoding from upper-limb electromyography (sEMG) can enhance human-machine interfaces and offer a more natural means of controlling prosthetic limbs, virtual reality, and household electronics. Unfortunately, current sEMG technology does not always perform consistently across users because individual differences such as age and body mass index, among many others, can substantially alter signal quality. This variability makes sEMG characteristics highly idiosyncratic, often necessitating laborious personalization and iterative tuning to achieve reliable performance. This variability has particular import for sEMG-based assistive devices and neural interfaces, where demographic biases in sEMG features could undermine broad and fair deployment.
In this study, we explore how demographic differences affect the sEMG signals produced and their implications for machine learning-based gesture decoding. We analyze the data set provided by, in which we derive 147 common sEMG features extracted from 81 demographically diverse individuals performing discrete hand gestures. Using mixed-effects linear models and partial least squares (PLS) analysis, which take into consideration demographic variables (including age, sex, height, weight, skin properties, subcutaneous fat, and hair density), we identify that 33\% (49 of 147) of commonly used sEMG features show significant associations with demographic characteristics. These results may help guide the development of fair and unbiased sEMG-based neural interfaces across a diverse population.

---


### 56. [Improving Human Performance with Value-Aware Interventions: A Case Study in Chess](https://arxiv.org/abs/2604.14465)

**<font color=#1a73e8>作者：</font>** Saumik Narayanan, Raja Panjwani, Siddhartha Sen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are increasingly used to assist humans in sequential decision-making tasks, yet determining when and how an AI assistant should intervene remains a fundamental challenge. A potential baseline is to recommend the optimal action according to a strong model. However, such actions assume optimal follow-up actions, which human decision makers may fail to execute, potentially reducing overall performance. In this work, we propose and study value-aware interventions, motivated by a basic principle in reinforcement learning: under the Bellman equation, the optimal policy selects actions that maximize the immediate reward plus the value function. When a decision maker follows a suboptimal policy, this policy-value consistency no longer holds, creating discrepancies between the actions taken by the policy and those that maximize the immediate reward plus the value of the next state. We show that these policy-value inconsistencies naturally identify opportunities for intervention. We formalize this problem in a Markov decision process where an AI assistant may override human actions under an intervention budget. In the single-intervention regime, we show that the optimal strategy is to recommend the action that maximizes the human value function. For settings with multiple interventions, we propose a tractable approximation that prioritizes interventions based on the magnitude of the policy-value discrepancy. We evaluate these ideas in the domain of chess by learning models of humans from large-scale gameplay data. In simulation, our approach consistently outperforms interventions based on the strongest chess engine (Stockfish) in a wide range of settings. A within-subject human study with 20 players and 600 games further shows that our interventions significantly improve performance for low- and mid-skill players while matching expert-engine interventions for high-skill players.

---


### 57. [Auxiliary Finite-Difference Residual-Gradient Regularization for PINNs](https://arxiv.org/abs/2604.14472)

**<font color=#1a73e8>作者：</font>** Stavros Kassinos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) are often selected by a single scalar loss even when the quantity of interest is more specific. We study a hybrid design in which the governing PDE residual remains automatic-differentiation (AD) based, while finite differences (FD) appear only in a weak auxiliary term that penalizes gradients of the sampled residual field. The FD term regularizes the residual field without replacing the PDE residual itself.
We examine this idea in two stages. Stage 1 is a controlled Poisson benchmark comparing a baseline PINN, the FD residual-gradient regularizer, and a matched AD residual-gradient baseline. Stage 2 transfers the same logic to a three-dimensional annular heat-conduction benchmark (PINN3D), where baseline errors concentrate near a wavy outer wall and the auxiliary grid is implemented as a body-fitted shell adjacent to the wall.
In Stage 1, the FD regularizer reproduces the main effect of residual-gradient control while exposing a trade-off between field accuracy and residual cleanliness. In Stage 2, the shell regularizer improves the application-facing quantities, namely outer-wall flux and boundary-condition behavior. Across seeds 0-5 and 100k epochs, the most reliable tested configuration is a fixed shell weight of 5e-4 under the Kourkoutas-beta optimizer regime: relative to a matched run without the shell term, it reduces the mean outer-wall BC RMSE from 1.22e-2 to 9.29e-4 and the mean wall-flux RMSE from 9.21e-3 to 9.63e-4. Adam with beta2=0.999 becomes usable when the initial learning rate is reduced to 1e-3, although its shell benefit is less robust than under Kourkoutas-beta. Overall, the results support a targeted view of hybrid PINNs: an auxiliary-only FD regularizer is most valuable when it is aligned with the physical quantity of interest, here the outer-wall flux.

---


### 58. [Seeing Through Circuits: Faithful Mechanistic Interpretability for Vision Transformers](https://arxiv.org/abs/2604.14477)

**<font color=#1a73e8>作者：</font>** Nina Żukowska, Wolfgang Stammer, Bernt Schiele 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transparency of neural networks' internal reasoning is at the heart of interpretability research, adding to trust, safety, and understanding of these models. The field of mechanistic interpretability has recently focused on studying task-specific computational graphs, defined by connections (edges) between model components. Such edge-based circuits have been defined in the context of large language models, yet vision-based approaches so far only consider neuron-based circuits. These tell which information is encoded, but not how it is routed through the complex wiring of a neural network. In this work, we investigate whether useful mechanistic circuits can be identified through computational graphs in vision transformers. We propose an effective method for Automatic Visual Circuit Discovery (Vi-CD) that recovers class-specific circuits for classification, identifies circuits underlying typographic attacks in CLIP, and discovers circuits that lend themselves for steering to correct harmful model behavior. Overall, we find that insightful and actionable edge-based circuits can be recovered from vision transformers, adding transparency to the internal computations of these models.

---


### 59. [Quantization of Spiking Neural Networks Beyond Accuracy](https://arxiv.org/abs/2604.14487)

**<font color=#1a73e8>作者：</font>** Evan Gibson Smith, Jacob Whitehill, Fatemeh Ganji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization is a natural complement to the sparse, event-driven computation of Spiking Neural Networks, reducing memory bandwidth and arithmetic cost for deployment on resource-constrained hardware. However, existing SNN quantization evaluation focuses almost exclusively on accuracy, overlooking whether a quantized network preserves the firing behavior of its full-precision counterpart. We demonstrate that quantization method, clipping range, and bit-width can produce substantially different firing distributions at equivalent accuracy, differences invisible to standard metrics but relevant to deployment, where firing activity governs effective sparsity, state storage, and event-processing load. To capture this gap, we propose Earth Mover's Distance as a diagnostic metric for firing distribution divergence, and apply it systematically across weight and membrane quantization on SEW-ResNet architectures trained on CIFAR-10 and CIFAR-100. We find that uniform quantization induces distributional drift even when accuracy is preserved, while LQ-Net style learned quantization maintains firing behavior close to the full-precision baseline. Our results suggest that behavior preservation should be treated as an evaluation criterion alongside accuracy, and that EMD provides a principled tool for assessing it.

---


### 60. [CobwebTM: Probabilistic Concept Formation for Lifelong and Hierarchical Topic Modeling](https://arxiv.org/abs/2604.14489)

**<font color=#1a73e8>作者：</font>** Karthik Singaravadivelan, Anant Gupta, Zekun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Topic modeling seeks to uncover latent semantic structure in text corpora with minimal supervision. Neural approaches achieve strong performance but require extensive tuning and struggle with lifelong learning due to catastrophic forgetting and fixed capacity, while classical probabilistic models lack flexibility and adaptability to streaming data. We introduce \textsc{CobwebTM}, a low-parameter lifelong hierarchical topic model based on incremental probabilistic concept formation. By adapting the Cobweb algorithm to continuous document embeddings, \textsc{CobwebTM} constructs semantic hierarchies online, enabling unsupervised topic discovery, dynamic topic creation, and hierarchical organization without predefining the number of topics. Across diverse datasets, \textsc{CobwebTM} achieves strong topic coherence, stable topics over time, and high-quality hierarchies, demonstrating that incremental symbolic concept formation combined with pretrained representations is an efficient approach to topic modeling.

---


### 61. [Improving Machine Learning Performance with Synthetic Augmentation](https://arxiv.org/abs/2604.14498)

**<font color=#1a73e8>作者：</font>** Mel Sohm, Charles Dezons, Sami Sellami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synthetic augmentation is increasingly used to mitigate data scarcity in financial machine learning, yet its statistical role remains poorly understood. We formalize synthetic augmentation as a modification of the effective training distribution and show that it induces a structural bias--variance trade-off: while additional samples may reduce estimation error, they may also shift the population objective whenever the synthetic distribution deviates from regions relevant under evaluation. To isolate informational gains from mechanical sample-size effects, we introduce a size-matched null augmentation and a finite-sample, non-parametric block permutation test that remains valid under weak temporal dependence.
We evaluate this framework in both controlled Markov-switching environments and real financial datasets, including high-frequency option trade data and a daily equity panel. Across generators spanning bootstrap, copula-based models, variational autoencoders, diffusion models, and TimeGAN, we vary augmentation ratio, model capacity, task type, regime rarity, and signal-to-noise. We show that synthetic augmentation is beneficial only in variance-dominant regimes, such as persistent volatility forecasting-while it deteriorates performance in bias-dominant settings, including near-efficient directional prediction. Rare-regime targeting can improve domain-specific metrics but may conflict with unconditional permutation inference. Our results provide a structural perspective on when synthetic data improves financial learning performance and when it induces persistent distributional distortion.

---


### 62. [On the Expressive Power and Limitations of Multi-Layer SSMs](https://arxiv.org/abs/2604.14501)

**<font color=#1a73e8>作者：</font>** Nikola Zubić, Qian Li, Yuyi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the expressive power and limitations of multi-layer state-space models (SSMs). First, we show that multi-layer SSMs face fundamental limitations in compositional tasks, revealing an inherent gap between SSMs and streaming models. Then, we examine the role of chain-of-thought (CoT), showing that offline CoT does not fundamentally increase the expressiveness, while online CoT can substantially increase its power. Indeed, with online CoT, multi-layer SSMs become equivalent in power to streaming algorithms. Finally, we investigate the tradeoff between width and precision, showing that these resources are not interchangeable in the base model, but admit a clean equivalence once online CoT is allowed. Overall, our results offer a unified perspective on how depth, finite precision, and CoT shape the power and limits of SSMs.

---


### 63. [Co-distilled attention guided masked image modeling with noisy teacher for self-supervised learning on medical images](https://arxiv.org/abs/2604.14506)

**<font color=#1a73e8>作者：</font>** Jue Jiang, Aneesh Rangnekar, Harini Veeraraghavan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Masked image modeling (MIM) is a highly effective self-supervised learning (SSL) approach to extract useful feature representations from unannotated data. Predominantly used random masking methods make SSL less effective for medical images due to the contextual similarity of neighboring patches, leading to information leakage and SSL simplification. Hierarchical shifted window (Swin) transformer, a highly effective approach for medical images cannot use advanced masking methods as it lacks a global [CLS] token. Hence, we introduced an attention guided masking mechanism for Swin within a co-distillation learning framework to selectively mask semantically co-occurring and discriminative patches, to reduce information leakage and increase the difficulty of SSL pretraining. However, attention guided masking inevitably reduces the diversity of attention heads, which negatively impacts downstream task performance. To address this, we for the first time, integrate a noisy teacher into the co-distillation framework (termed DAGMaN) that performs attentive masking while preserving high attention head diversity. We demonstrate the capability of DAGMaN on multiple tasks including full- and few-shot lung nodule classification, immunotherapy outcome prediction, tumor segmentation, and unsupervised organs clustering.

---


### 64. [H2VLR: Heterogeneous Hypergraph Vision-Language Reasoning for Few-Shot Anomaly Detection](https://arxiv.org/abs/2604.14507)

**<font color=#1a73e8>作者：</font>** Jianghong Huang, Luping Ji, Weiwei Duan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As a classic vision task, anomaly detection has been widely applied in industrial inspection and medical imaging. In this task, data scarcity is often a frequently-faced issue. To solve it, the few-shot anomaly detection (FSAD) scheme is attracting increasing attention. In recent years, beyond traditional visual paradigm, Vision-Language Model (VLM) has been extensively explored to boost this field. However, in currently-existing VLM-based FSAD schemes, almost all perform anomaly inference only by pairwise feature matching, ignoring structural dependencies and global consistency. To further redound to FSAD via VLM, we propose a Heterogeneous Hypergraph Vision-Language Reasoning (H2VLR) framework. It reformulates the FSAD as a high-order inference problem of visual-semantic relations, by jointly modeling visual regions and semantic concepts in a unified hypergraph. Experimental comparisons verify the effectiveness and advantages of H2VLR. It could often achieve state-of-the-art (SOTA) performance on representative industrial and medical benchmarks. Our code will be released upon acceptance.

---


### 65. [CBCL: Safe Self-Extending Agent Communication](https://arxiv.org/abs/2604.14512)

**<font color=#1a73e8>作者：</font>** Hugo O'Connor  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent communication languages (ACLs) enable heterogeneous agents to share knowledge and coordinate across diverse domains. This diversity demands extensibility, but expressive extension mechanisms can push the input language beyond the complexity classes where full validation is tractable. We present CBCL (Common Business Communication Language), an agent communication language that constrains all messages, including runtime language extensions, to the deterministic context-free language (DCFL) class. CBCL allows agents to define, transmit, and adopt domain-specific "dialect" extensions as first-class messages; three safety invariants (R1--R3), machine-checked in Lean 4 and enforced in a Rust reference implementation, prevent unbounded expansion, applying declared resource limits, and preserving core vocabulary. We formalize the language and its safety properties in Lean 4, implement a reference parser and dialect engine in Rust with property-based and differential tests, and extract a verified parser binary. Our results demonstrate that homoiconic protocol design, where extension definitions share the same representation as ordinary messages, can be made provably safe. As autonomous agents increasingly extend their own communication capabilities, formally bounding what they can express to each other is a precondition for oversight.

---


### 66. [PeerPrism: Peer Evaluation Expertise vs Review-writing AI](https://arxiv.org/abs/2604.14513)

**<font color=#1a73e8>作者：</font>** Soroush Sadeghian, Alireza Daqiq, Radin Cheraghi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used in scientific peer review, assisting with drafting, rewriting, expansion, and refinement. However, existing peer-review LLM detection methods largely treat authorship as a binary problem-human vs. AI-without accounting for the hybrid nature of modern review workflows. In practice, evaluative ideas and surface realization may originate from different sources, creating a spectrum of human-AI collaboration.
In this work, we introduce PeerPrism, a large-scale benchmark of 20,690 peer reviews explicitly designed to disentangle idea provenance from text provenance. We construct controlled generation regimes spanning fully human, fully synthetic, and multiple hybrid transformations. This design enables systematic evaluation of whether detectors identify the origin of the surface text or the origin of the evaluative reasoning. We benchmark state-of-the-art LLM text detection methods on PeerPrism. While several methods achieve high accuracy on the standard binary task (human vs. fully synthetic), their predictions diverge sharply under hybrid regimes. In particular, when ideas originate from humans but the surface text is AI-generated, detectors frequently disagree and produce contradictory classifications. Accompanied by stylometric and semantic analyses, our results show that current detection methods conflate surface realization with intellectual contribution.
Overall, we demonstrate that LLM detection in peer review cannot be reduced to a binary attribution problem. Instead, authorship must be modeled as a multidimensional construct spanning semantic reasoning and stylistic realization. PeerPrism is the first benchmark evaluating human-AI collaboration in these settings. We release all code, data, prompts, and evaluation scripts to facilitate reproducible research at this https URL.

---


### 67. [Perspective on Bias in Biomedical AI: Preventing Downstream Healthcare Disparities](https://arxiv.org/abs/2604.14514)

**<font color=#1a73e8>作者：</font>** Michal Rosen-Zvi, Yoav Kan-Tor, Michael Danziger 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare disparities persist across socioeconomic boundaries, often attributed to unequal access to screening, diagnostics, and therapeutics. However, this perspective highlights that critical biases can emerge much earlier, during data collection and research prioritization, long before clinical implementation in cases where the focus of the studies and the data that is collected is at the molecular level. A vast number of studies focus on collecting omics data but the demographic information associated with these datasets is often not reported in the studies, and when it is reported, it shows big biases. An automated analysis of 4719 PubMed-indexed omics publications from 2015 to 2024 reveals that only a small fraction report ancestry or ethnicity information, with ancestry reporting improving slightly. Analysis of large-scale datasets commonly used for model training, such as CellxGene and GEO, reveals substantial population bias where European-ancestry data dominates. As biomedical foundation models become central to biomedical discovery with a paradigm in which base models are pretrained on large datasets and reusing them time and again for many different downstream tasks, they risk perpetuating or amplifying these early-stage biases, leading to cascading inequities that regulatory interventions cannot fully reverse. We propose a community-wide focus on three foundational principles: Provenance, Openness, and Evaluation Transparency to improve equity and robustness in biomedical AI. This approach aims to foster biomedical innovation that more effectively serves underserved populations and improves health outcomes.

---


### 68. [Mind DeepResearch Technical Report](https://arxiv.org/abs/2604.14518)

**<font color=#1a73e8>作者：</font>** MindDR Team, Li Auto Inc  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present \textbf{Mind DeepResearch (MindDR)}, an efficient multi-agent deep research framework that achieves leading performance with only \textasciitilde30B-parameter models through a meticulously designed data synthesis and multi-stage training pipeline. The core innovation of MindDR lies in a collaborative three-agent architecture (Planning Agent, DeepSearch Agent, and Report Agent) and a four-stage agent-specialized training pipeline comprising SFT cold-start, Search-RL, Report-RL and preference alignment. With this regime, MindDR demonstrates competitive performance even with \textasciitilde30B-scale models. Specifically, MindDR achieves 45.7\% on BrowseComp-ZH, 42.8\% on BrowseComp, 46.5\% on WideSearch, 75.0\% on xbench-DS, and 52.5 on DeepResearch Bench, outperforming comparable-scale open-source agent systems and rivaling larger-scale models. MindDR has been deployed as an online product in Li Auto. Furthermore, we introduce \textbf{MindDR Bench}, a curated benchmark of 500 real-world Chinese queries from our internal product user interactions, evaluated through a comprehensive multi-dimensional rubric system rather than relying on a single RACE metric. On MindDR Bench, MindDR achieves a state-of-the-art score of 51.8.

---


### 69. [CI-CBM: Class-Incremental Concept Bottleneck Model for Interpretable Continual Learning](https://arxiv.org/abs/2604.14519)

**<font color=#1a73e8>作者：</font>** Amirhosein Javadi, Tuomas Oikarinen, Tara Javidi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting remains a fundamental challenge in continual learning, in which models often forget previous knowledge when fine-tuned on a new task. This issue is especially pronounced in class incremental learning (CIL), which is the most challenging setting in continual learning. Existing methods to address catastrophic forgetting often sacrifice either model interpretability or accuracy. To address this challenge, we introduce ClassIncremental Concept Bottleneck Model (CI-CBM), which leverage effective techniques, including concept regularization and pseudo-concept generation to maintain interpretable decision processes throughout incremental learning phases. Through extensive evaluation on seven datasets, CI-CBM achieves comparable performance to black-box models and outperforms previous interpretable approaches in CIL, with an average 36% accuracy gain. CICBM provides interpretable decisions on individual inputs and understandable global decision rules, as shown in our experiments, thereby demonstrating that human understandable concepts can be maintained during incremental learning without compromising model performance. Our approach is effective in both pretrained and non-pretrained scenarios; in the latter, the backbone is trained from scratch during the first learning phase. Code is publicly available at this http URL.

---


### 70. [FreqTrack: Frequency Learning based Vision Transformer for RGB-Event Object Tracking](https://arxiv.org/abs/2604.14526)

**<font color=#1a73e8>作者：</font>** Jinlin You, Muyu Li, Xudong Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing single-modal RGB trackers often face performance bottlenecks in complex dynamic scenes, while the introduction of event sensors offers new potential for enhancing tracking capabilities. However, most current RGB-event fusion methods, primarily designed in the spatial domain using convolutional, Transformer, or Mamba architectures, fail to fully exploit the unique temporal response and high-frequency characteristics of event data. To address this, we1 propose FreqTrack, a frequency-aware RGBE tracking framework that establishes complementary inter-modal correlations through frequency-domain transformations for more robust feature fusion. We design a Spectral Enhancement Transformer (SET) layer that incorporates multi-head dynamic Fourier filtering to adaptively enhance and select frequency-domain features. Additionally, we develop a Wavelet Edge Refinement (WER) module, which leverages learnable wavelet transforms to explicitly extract multi-scale edge structures from event data, effectively improving modeling capability in high-speed and low-light scenarios. Extensive experiments on the COESOT and FE108 datasets demonstrate that FreqTrack achieves highly competitive performance, particularly attaining leading precision of 76.6\% on the COESOT benchmark, validating the effectiveness of frequency-domain modeling for RGBE tracking.

---


### 71. [Design and Validation of a Low-Cost Smartphone Based Fluorescence Detection Platform Compared with Conventional Microplate Readers](https://arxiv.org/abs/2604.14527)

**<font color=#1a73e8>作者：</font>** Zhendong Cao, Katrina G. Salvante, Ash Parameswaran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A low cost fluorescence-based optical system is developed for detecting the presence of certain microorganisms and molecules within a diluted sample. A specifically designed device setup compatible with conventional 96 well plates is chosen to create an ideal environment in which a smart phone camera can be used as the optical detector. In comparison with conventional microplate reading machines such as Perkin Elmer Victor Machine, the device presented in this paper is not equipped with expensive elements such as exciter filer, barrier filter and photomultiplier; instead, a phone camera is all needed to detect fluorescence within the sample. The strategy being involved is to determine the relationship between the image color of the sample in RGB color space and the molar concentration of the fluorescence specimen in that sample. This manuscript is a preprint version of work related to a publication in IEEE. The final version may differ from this manuscript.

---


### 72. [CSRA: Controlled Spectral Residual Augmentation for Robust Sepsis Prediction](https://arxiv.org/abs/2604.14532)

**<font color=#1a73e8>作者：</font>** Honglin Guo, Rihao Chang, He Jiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of future risk and disease progression in sepsis is clinically important for early warning and timely intervention in intensive care. However, short-window sepsis prediction remains challenging, because shorter observation windows provide limited historical evidence, whereas longer prediction horizons reduce the number of patient trajectories with valid future supervision. To address this problem, we propose CSRA, a Controlled Spectral Residual Augmentation framework for short-window multi-system ICU time series. CSRA first groups variables by clinical systems and extracts system-level and global representations. It then performs input-adaptive residual perturbation in the spectral domain to generate structured and clinically plausible trajectory variations. To improve augmentation stability and controllability, CSRA is trained end-to-end with the downstream predictor under a unified objective, together with anchor consistency loss and controller regularization. Experiments on a MIMIC-IV sepsis cohort across multiple downstream models show that CSRA is consistently competitive and often superior, reducing regression error by 10.2\% in MSE and 3.7\% in MAE over the non-augmentation baseline, while also yielding consistent gains on classification. CSRA further maintains more favorable performance under shorter observation windows, longer prediction horizons, and smaller training data scales, while also remaining effective on an external clinical dataset~(ZiGongICUinfection), indicating stronger robustness and generalizability in clinically constrained settings.

---


### 73. [An unsupervised decision-support framework for multivariate biomarker analysis in athlete monitoring](https://arxiv.org/abs/2604.14534)

**<font color=#1a73e8>作者：</font>** Fernando Barcelos Rosito, Sebastião De Jesus Menezes, Simone Ferreira Sturza 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Purpose. Athlete monitoring is constrained by small cohorts, heterogeneous biomarker scales, limited feasibility of repeated sampling, and the lack of reliable injury ground truth. These limitations reduce the interpretability and utility of traditional univariate and binary risk models. This study addresses these challenges by proposing an unsupervised multivariate framework to identify latent physiological states in athletes using real data. Methods. We propose a modular computational framework that operates in the joint biomarker space, integrating preprocessing, clinical safety screening, unsupervised clustering, and centroid-based physiological interpretation. Profiles are learned exclusively from amateur soccer players during a competitive microcycle. Synthetic data augmentation evaluates robustness and scalability. Ward hierarchical clustering supports monitoring and etiological differentiation, while Gaussian Mixture Models (GMM) enable structural stability analysis in high-dimensional settings. Results. The framework identifies coherent profiles that distinguish mechanical damage from metabolic stress while preserving homeostatic states. Synthetic data augmentation demonstrates feasibility and detection of latent silent risk phenotypes typically missed by univariate monitoring. Structural analyses indicate robustness under augmentation and higher-dimensional settings. Conclusion. The framework enables interpretable identification of latent physiological states from multivariate biomarker data without injury labels. By distinguishing mechanisms and revealing silent risk patterns not captured by conventional monitoring, it provides actionable insights for individualized athlete monitoring and decision making.

---


### 74. [WILD-SAM: Phase-Aware Expert Adaptation of SAM for Landslide Detection in Wrapped InSAR Interferograms](https://arxiv.org/abs/2604.14540)

**<font color=#1a73e8>作者：</font>** Yucheng Pan, Heping Li, Zhangle Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting slow-moving landslides directly from wrapped Interferometric Synthetic Aperture Radar (InSAR) interferograms is crucial for efficient geohazard monitoring, yet it remains fundamentally challenged by severe phase ambiguity and complex coherence noise. While the Segment Anything Model (SAM) offers a powerful foundation for segmentation, its direct transfer to wrapped phase data is hindered by a profound spectral domain shift, which suppresses the high-frequency fringes essential for boundary delineation. To bridge this gap, we propose WILD-SAM, a novel parameter-efficient fine-tuning framework specifically designed to adapt SAM for high-precision landslide detection on wrapped interferograms. Specifically, the architecture integrates a Phase-Aware Mixture-of-Experts (PA-MoE) Adapter into the frozen encoder to align spectral distributions and introduces a Wavelet-Guided Subband Enhancement (WGSE) strategy to generate frequency-aware dense prompts. The PA-MoE Adapter exploits a dynamic routing mechanism across heterogeneous convolutional experts to adaptively aggregate multi-scale spectral-textural priors, effectively aligning the distribution discrepancy between natural images and interferometric phase data. Meanwhile, the WGSE strategy leverages discrete wavelet transforms to explicitly disentangle high-frequency subbands and refine directional phase textures, injecting these structural cues as dense prompts to ensure topological integrity along sharp landslide boundaries. Extensive experiments on the ISSLIDE and ISSLIDE+ benchmarks demonstrate that WILD-SAM achieves state-of-the-art performance, significantly outperforming existing methods in both target completeness and contour fidelity.

---


### 75. [Giving Faces Their Feelings Back: Explicit Emotion Control for Feedforward Single-Image 3D Head Avatars](https://arxiv.org/abs/2604.14541)

**<font color=#1a73e8>作者：</font>** Yicheng Gong, Jiawei Zhang, Liqiang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a framework for explicit emotion control in feed-forward, single-image 3D head avatar reconstruction. Unlike existing pipelines where emotion is implicitly entangled with geometry or appearance, we treat emotion as a first-class control signal that can be manipulated independently and consistently across identities. Our method injects emotion into existing feed-forward architectures via a dual-path modulation mechanism without modifying their core design. Geometry modulation performs emotion-conditioned normalization in the original parametric space, disentangling emotional state from speech-driven articulation, while appearance modulation captures identity-aware, emotion-dependent visual cues beyond geometry. To enable learning under this setting, we construct a time-synchronized, emotion-consistent multi-identity dataset by transferring aligned emotional dynamics across identities. Integrated into multiple state-of-the-art backbones, our framework preserves reconstruction and reenactment fidelity while enabling controllable emotion transfer, disentangled manipulation, and smooth emotion interpolation, advancing expressive and scalable 3D head avatars.

---


### 76. [Controllable Video Object Insertion via Multiview Priors](https://arxiv.org/abs/2604.14556)

**<font color=#1a73e8>作者：</font>** Xia Qi, Peishan Cong, Yichen Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video object insertion is a critical task for dynamically inserting new objects into existing environments. Previous video generation methods focus primarily on synthesizing entire scenes while struggling with ensuring consistent object appearance, spatial alignment, and temporal coherence when inserting objects into existing videos. In this paper, we propose a novel solution for Video Object Insertion, which integrates multi-view object priors to address the common challenges of appearance inconsistency and occlusion handling in dynamic environments. By lifting 2D reference images into multi-view representations and leveraging a dual-path view-consistent conditioning mechanism, our framework ensures stable identity guidance and robust integration across diverse viewpoints. A quality-aware weighting mechanism is also employed to adaptively handle noisy or imperfect inputs. Additionally, we introduce an Integration-Aware Consistency Module that guarantees spatial realism, effectively resolving occlusion and boundary artifacts while maintaining temporal continuity across frames. Experimental results show that our solution significantly improves the quality of video object insertion, providing stable and realistic integration.

---


### 77. [The Fourth Challenge on Image Super-Resolution ($\times$4) at NTIRE 2026: Benchmark Results and Method Overview](https://arxiv.org/abs/2604.14558)

**<font color=#1a73e8>作者：</font>** Zheng Chen, Kai Liu, Jingkai Wang 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents the NTIRE 2026 image super-resolution ($\times$4) challenge, one of the associated competitions of the NTIRE 2026 Workshop at CVPR 2026. The challenge aims to reconstruct high-resolution (HR) images from low-resolution (LR) inputs generated through bicubic downsampling with a $\times$4 scaling factor. The objective is to develop effective super-resolution solutions and analyze recent advances in the field. To reflect the evolving objectives of image super-resolution, the challenge includes two tracks: (1) a restoration track, which emphasizes pixel-wise fidelity and ranks submissions based on PSNR; and (2) a perceptual track, which focuses on visual realism and evaluates results using a perceptual score. A total of 194 participants registered for the challenge, with 31 teams submitting valid entries. This report summarizes the challenge design, datasets, evaluation protocol, main results, and methods of participating teams. The challenge provides a unified benchmark and offers insights into current progress and future directions in image super-resolution.

---


### 78. [DVFace: Spatio-Temporal Dual-Prior Diffusion for Video Face Restoration](https://arxiv.org/abs/2604.14560)

**<font color=#1a73e8>作者：</font>** Zheng Chen, Bowen Chai, Rongjun Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video face restoration aims to enhance degraded face videos into high-quality results with realistic facial details, stable identity, and temporal coherence. Recent diffusion-based methods have brought strong generative priors to restoration and enabled more realistic detail synthesis. However, existing approaches for face videos still rely heavily on generic diffusion priors and multi-step sampling, which limit both facial adaptation and inference efficiency. These limitations motivate the use of one-step diffusion for video face restoration, yet achieving faithful facial recovery alongside temporally stable outputs remains challenging. In this paper, we propose, DVFace, a one-step diffusion framework for real-world video face restoration. Specifically, we introduce a spatio-temporal dual-codebook design to extract complementary spatial and temporal facial priors from degraded videos. We further propose an asymmetric spatio-temporal fusion module to inject these priors into the diffusion backbone according to their distinct roles. Evaluation on various benchmarks shows that DVFace delivers superior restoration quality, temporal consistency, and identity preservation compared to recent methods. Code: this https URL.

---


### 79. [Material-Agnostic Zero-Shot Thermal Inference for Metal Additive Manufacturing via a Parametric PINN Framework](https://arxiv.org/abs/2604.14562)

**<font color=#1a73e8>作者：</font>** Hyeonsu Lee, Jihoon Jeong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate thermal modeling in metal additive manufacturing (AM) is essential for understanding the process-structure-performance relationship. While prior studies have explored generalization across unseen process conditions, they often require extensive datasets, costly retraining, or pre-training. Generalization across different materials also remains relatively unexplored due to the challenges posed by distinct material-dependent thermal behaviors. This paper introduces a parametric physics-informed neural network (PINN) framework for zero-shot generalization across arbitrary materials without labeled data, retraining, or pre-training. The framework adopts a decoupled parametric PINN architecture that separately encodes material properties and spatiotemporal coordinates, fusing them through conditional modulation to better align with the multiplicative role of material parameters in the governing equation and boundary conditions. Physics-guided output scaling derived from Rosenthal's analytical solution and a hybrid optimization strategy are further incorporated to enhance physical consistency, training stability, and convergence. Experiments on bare plate laser powder bed fusion (LPBF) across diverse metal alloys, including both in-distribution and out-of-distribution cases, demonstrate effective zero-shot generalizability along with superior training efficiency. Specifically, the proposed framework achieved up to a 64.2% reduction in relative L2 error compared to the non-parametric baseline while surpassing its performance within only 4.4% of the baseline training epochs. Ablation studies confirm that the proposed framework's components are broadly applicable to other PINN-based approaches. Overall, the proposed framework provides an efficient and scalable material-agnostic solution for zero-shot thermal modeling, contributing to more flexible and practical deployment in metal AM.

---


### 80. [Revisiting Token Compression for Accelerating ViT-based Sparse Multi-View 3D Object Detectors](https://arxiv.org/abs/2604.14563)

**<font color=#1a73e8>作者：</font>** Mingqian Ji, Shanshan Zhang, Jian Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformer (ViT)-based sparse multi-view 3D object detectors have achieved remarkable accuracy but still suffer from high inference latency due to heavy token processing. To accelerate these models, token compression has been widely explored. However, our revisit of existing strategies, such as token pruning, merging, and patch size enlargement, reveals that they often discard informative background cues, disrupt contextual consistency, and lose fine-grained semantics, negatively affecting 3D detection. To overcome these limitations, we propose SEPatch3D, a novel framework that dynamically adjusts patch sizes while preserving critical semantic information within coarse patches. Specifically, we design Spatiotemporal-aware Patch Size Selection (SPSS) that assigns small patches to scenes containing nearby objects to preserve fine details and large patches to background-dominated scenes to reduce computation cost. To further mitigate potential detail loss, Informative Patch Selection (IPS) selects the informative patches for feature refinement, and Cross-Granularity Feature Enhancement (CGFE) injects fine-grained details into selected coarse patches, enriching semantic features. Experiments on the nuScenes and Argoverse 2 validation sets show that SEPatch3D achieves up to \textbf{57\%} faster inference than the StreamPETR baseline and \textbf{20\%} higher efficiency than the state-of-the-art ToC3D-faster, while preserving comparable detection accuracy. Code is available at this https URL.

---


### 81. [MARS$^2$: Scaling Multi-Agent Tree Search via Reinforcement Learning for Code Generation](https://arxiv.org/abs/2604.14564)

**<font color=#1a73e8>作者：</font>** Pengfei Li, Shijie Wang, Fangyuan Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) paradigms have demonstrated strong performance on reasoning-intensive tasks such as code generation. However, limited trajectory diversity often leads to diminishing returns, which constrains the achievable performance ceiling. Search-enhanced RL alleviates this issue by introducing structured exploration, which remains constrained by the single-agent policy priors. Meanwhile, leveraging multiple interacting policies can acquire more diverse exploratory signals, but existing approaches are typically decoupled from structured search. We propose \textbf{MARS$^2$} (Multi-Agent Reinforced Tree-Search Scaling), a unified RL framework in which multiple independently-optimized agents collaborate within a shared tree-structured search environment. MARS$^2$ models the search tree as a learnable multi-agent interaction environment, enabling heterogeneous agents to collaboratively generate and refine candidate solutions within a shared search topology. To support effective learning, we introduce a path-level group advantage formulation based on tree-consistent reward shaping, which facilitates effective credit assignment across complex search trajectories. Experiments on code generation benchmarks show that MARS$^2$ consistently improves performance across diverse model combinations and training settings, demonstrating the effectiveness of coupling multi-agent collaboration with tree search for enhancing reinforcement learning. Our code is publicly available at this https URL.

---


### 82. [Physics-Informed Machine Learning for Pouch Cell Temperature Estimation](https://arxiv.org/abs/2604.14566)

**<font color=#1a73e8>作者：</font>** Zheng Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate temperature estimation of pouch cells with indirect liquid cooling is essential for optimizing battery thermal management systems for transportation electrification. However, it is challenging due to the computational expense of finite element simulations and the limitations of data-driven models. This paper presents a physics-informed machine learning (PIML) framework for the efficient and reliable estimation of steady-state temperature profiles. The PIML approach integrates the governing heat transfer equations directly into the neural network's loss function, enabling high-fidelity predictions with significantly faster convergence than purely data-driven methods. The framework is evaluated on a dataset of varying cooling channel geometries. Results demonstrate that the PIML model converges more rapidly and achieves markedly higher accuracy, with a 49.1% reduction in mean squared error over the data-driven model. Validation against independent test cases further confirms its superior performance, particularly in regions away from the cooling channels. These findings underscore the potential of PIML for surrogate modeling and design optimization in battery systems.

---


### 83. [Learning Adaptive Reasoning Paths for Efficient Visual Reasoning](https://arxiv.org/abs/2604.14568)

**<font color=#1a73e8>作者：</font>** Yixu Huang, Tinghui Zhu, Muhao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual reasoning models (VRMs) have recently shown strong cross-modal reasoning capabilities by integrating visual perception with language reasoning. However, they often suffer from overthinking, producing unnecessarily long reasoning chains for any tasks. We attribute this issue to \textbf{Reasoning Path Redundancy} in visual reasoning: many visual questions do not require the full reasoning process. To address this, we propose \textbf{AVR}, an adaptive visual reasoning framework that decomposes visual reasoning into three cognitive functions: visual perception, logical reasoning, and answer application. It further enables models to dynamically choose among three response formats: Full Format, Perception-Only Format, and Direct Answer. AVR is trained with FS-GRPO, an adaptation of Group Relative Policy Optimization that encourages the model to select the most efficient reasoning format while preserving correctness. Experiments on multiple vision-language benchmarks show that AVR reduces token usage by 50--90\% while maintaining overall accuracy, especially in perception-intensive tasks. These results demonstrate that adaptive visual reasoning can effectively mitigate overthinking in VRMs. Code and data are available at: this https URL.

---


### 84. [Deepfake Detection Generalization with Diffusion Noise](https://arxiv.org/abs/2604.14570)

**<font color=#1a73e8>作者：</font>** Hongyuan Qi, Wenjin Hou, Hehe Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detectors face growing challenges in generalization as new image synthesis techniques emerge. In particular, deepfakes generated by diffusion models are highly photorealistic and often evade detectors trained on GAN-based forgeries. This paper addresses the generalization problem in deepfake detection by leveraging diffusion noise characteristics. We propose an Attention-guided Noise Learning (ANL) framework that integrates a pre-trained diffusion model into the deepfake detection pipeline to guide the learning of more robust features. Specifically, our method uses the diffusion model's denoising process to expose subtle artifacts: the detector is trained to predict the noise contained in an input image at a given diffusion step, forcing it to capture discrepancies between real and synthetic images, while an attention-guided mechanism derived from the predicted noise is introduced to encourage the model to focus on globally distributed discrepancies rather than local patterns. By harnessing the frozen diffusion model's learned distribution of natural images, the ANL method acts as a form of regularization, improving the detector's generalization to unseen forgery types. Extensive experiments demonstrate that ANL significantly outperforms existing methods on multiple benchmarks, achieving state-of-the-art accuracy in detecting diffusion-generated deepfakes. Notably, the proposed framework boosts generalization performance (e.g., improving ACC/AP by a substantial margin on unseen models) without introducing additional overhead during inference. Our results highlight that diffusion noise provides a powerful signal for generalizable deepfake detection.

---


### 85. [M3D-Net: Multi-Modal 3D Facial Feature Reconstruction Network for Deepfake Detection](https://arxiv.org/abs/2604.14574)

**<font color=#1a73e8>作者：</font>** Haotian Wu, Yue Cheng, Shan Bian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of deep learning in image generation, facial forgery techniques have achieved unprecedented realism, posing serious threats to cybersecurity and information authenticity. Most existing deepfake detection approaches rely on the reconstruction of isolated facial attributes without fully exploiting the complementary nature of multi-modal feature representations. To address these challenges, this paper proposes a novel Multi-Modal 3D Facial Feature Reconstruction Network (M3D-Net) for deepfake detection. Our method leverages an end-to-end dual-stream architecture that reconstructs fine-grained facial geometry and reflectance properties from single-view RGB images via a self-supervised 3D facial reconstruction module. The network further enhances detection performance through a 3D Feature Pre-fusion Module (PFM), which adaptively adjusts multi-scale features, and a Multi-modal Fusion Module (MFM) that effectively integrates RGB and 3D-reconstructed features using attention mechanisms. Extensive experiments on multiple public datasets demonstrate that our approach achieves state-of-the-art performance in terms of detection accuracy and robustness, significantly outperforming existing methods while exhibiting strong generalization across diverse scenarios.

---


### 86. [TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580)

**<font color=#1a73e8>作者：</font>** Xiangyu Liu, Feng Gao, Xiaomei Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing audio-driven video digital human generation models rely on multi-step denoising, resulting in substantial computational overhead that severely limits their deployment in real-world settings. While one-step distillation approaches can significantly accelerate inference, they often suffer from training instability. To address this challenge, we propose TurboTalk, a two-stage progressive distillation framework that effectively compresses a multi-step audio-driven video diffusion model into a single-step generator. We first adopt Distribution Matching Distillation to obtain a strong and stable 4-step student, and then progressively reduce the denoising steps from 4 to 1 through adversarial distillation. To ensure stable training under extreme step reduction, we introduce a progressive timestep sampling strategy and a self-compare adversarial objective that provides an intermediate adversarial reference that stabilizes progressive distillation. Our method achieve single-step generation of video talking avatar, boosting inference speed by 120 times while maintaining high generation quality.

---


### 87. [Prompt Optimization Is a Coin Flip: Diagnosing When It Helps in Compound AI Systems](https://arxiv.org/abs/2604.14585)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Guanghui Wang, Yanwei Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt optimization in compound AI systems is statistically indistinguishable from a coin flip: across 72 optimization runs on Claude Haiku (6 methods $\times$ 4 tasks $\times$ 3 repeats), 49% score below zero-shot; on Amazon Nova Lite, the failure rate is even higher. Yet on one task, all six methods improve over zero-shot by up to $+6.8$ points. What distinguishes success from failure? We investigate with 18,000 grid evaluations and 144 optimization runs, testing two assumptions behind end-to-end optimization tools like TextGrad and DSPy: (A) individual prompts are worth optimizing, and (B) agent prompts interact, requiring joint optimization. Interaction effects are never significant ($p > 0.52$, all $F < 1.0$), and optimization helps only when the task has exploitable output structure -- a format the model can produce but does not default to. We provide a two-stage diagnostic: an \$80 ANOVA pre-test for agent coupling, and a 10-minute headroom test that predicts whether optimization is worthwhile -- turning a coin flip into an informed decision.

---


### 88. [CLion: Efficient Cautious Lion Optimizer with Enhanced Generalization](https://arxiv.org/abs/2604.14587)

**<font color=#1a73e8>作者：</font>** Feihu Huang, Guanyi Zhang, Songcan Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lion optimizer is a popular learning-based optimization algorithm in machine learning, which shows impressive performance in training many deep learning models. Although convergence property of the Lion optimizer has been studied, its generalization analysis is still missing. To fill this gap, we study generalization property of the Lion via algorithmic stability based on the mathematical induction. Specifically, we prove that the Lion has a generalization error of $O(\frac{1}{N\tau^T})$, where $N$ is training sample size, and $\tau>0$ denotes the smallest absolute value of non-zero element in gradient estimator, and $T$ is the total iteration number. In addition, we obtain an interesting byproduct that the SignSGD algorithm has the same generalization error as the Lion. To enhance generalization of the Lion, we design a novel efficient Cautious Lion (i.e., CLion) optimizer by cautiously using sign function. Moreover, we prove that our CLion has a lower generalization error of $O(\frac{1}{N})$ than $O(\frac{1}{N\tau^T})$ of the Lion, since the parameter $\tau$ generally is very small. Meanwhile, we study convergence property of our CLion optimizer, and prove that our CLion has a fast convergence rate of $O(\frac{\sqrt{d}}{T^{1/4}})$ under $\ell_1$-norm of gradient for nonconvex stochastic optimization, where $d$ denotes the model dimension.
Extensive numerical experiments demonstrate effectiveness of our CLion optimizer.

---


### 89. [Prompt-Guided Image Editing with Masked Logit Nudging in Visual Autoregressive Models](https://arxiv.org/abs/2604.14591)

**<font color=#1a73e8>作者：</font>** Amir El-Ghoussani, Marc Hölle, Gustavo Carneiro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the problem of prompt-guided image editing in visual autoregressive models. Given a source image and a target text prompt, we aim to modify the source image according to the target prompt, while preserving all regions which are unrelated to the requested edit. To this end, we present Masked Logit Nudging, which uses the source image token maps to introduce a guidance step that aligns the model's predictions under the target prompt with these source token maps. Specifically, we convert the fixed source encodings into logits using the VAR encoding, nudging the model's predicted logits towards the targets along a semantic trajectory defined by the source-target prompts. Edits are applied only within spatial masks obtained through a dedicated masking scheme that leverages cross-attention differences between the source and edited prompts. Then, we introduce a refinement to correct quantization errors and improve reconstruction quality. Our approach achieves the best image editing performance on the PIE benchmark at 512px and 1024px resolutions. Beyond editing, our method delivers faithful reconstructions and outperforms previous methods on COCO at 512px and OpenImages at 1024px. Overall, our method outperforms VAR-related approaches and achieves comparable or even better performance than diffusion models, while being much faster. Code is available at 'this https URL.

---


### 90. [NLP needs Diversity outside of 'Diversity'](https://arxiv.org/abs/2604.14595)

**<font color=#1a73e8>作者：</font>** Joshua Tint  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This position paper argues that recent progress with diversity in NLP is disproportionately concentrated on a small number of areas surrounding fairness. We further argue that this is the result of a number of incentives, biases, and barriers which come together to disenfranchise marginalized researchers in non-fairness fields, or to move them into fairness-related fields. We substantiate our claims with an investigation into the demographics of NLP researchers by subfield, using our research to support a number of recommendations for ensuring that all areas within NLP can become more inclusive and equitable. In particular, we highlight the importance of breaking down feedback loops that reinforce disparities, and the need to address geographical and linguistic barriers that hinder participation in NLP research.

---


### 91. [Towards Design Compositing](https://arxiv.org/abs/2604.14605)

**<font color=#1a73e8>作者：</font>** Abhinav Mahajan, Abhikhya Tripathy, Sudeeksha Reddy Pala 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphic design creation involves harmoniously assembling multimodal components such as images, text, logos, and other visual assets collected from diverse sources, into a visually-appealing and cohesive design. Recent methods have largely focused on layout prediction or complementary element generation, while retaining input elements exactly, implicitly assuming that provided components are already stylistically harmonious. In practice, inputs often come from disparate sources and exhibit visual mismatch, making this assumption limiting. We argue that identity-preserving stylization and compositing of input elements is a critical missing ingredient for truly harmonized components-to-design pipelines. To this end, we propose GIST, a training-free, identity-preserving image compositor that sits between layout prediction and typography generation, and can be plugged into any existing components-to-design or design-refining pipeline without modification. We demonstrate this by integrating GIST with two substantially different existing methods, LaDeCo and Design-o-meter. GIST shows significant improvements in visual harmony and aesthetic quality across both pipelines, as validated by LLaVA-OV and GPT-4V on aspect-wise ratings and pairwise preference over naive pasting. Project Page: this http URL.

---


### 92. [GDPR Auto-Formalization with AI Agents and Human Verification](https://arxiv.org/abs/2604.14607)

**<font color=#1a73e8>作者：</font>** Ha Thanh Nguyen, Wachara Fungwacharakorn, Sabine Wehnert 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the overall process of automatic formalization of GDPR provisions using large language models, within a human-in-the-loop verification framework. Rather than aiming for full autonomy, we adopt a role-specialized workflow in which LLM-based AI components, operating in a multi-agent setting with iterative feedback, generate legal scenarios, formal rules, and atomic facts. This is coupled with independent verification modules which include human reviewers' assessment of representational, logical, and legal correctness. Using this approach, we construct a high-quality dataset to be used for GDPR auto-formalization, and analyze both successful and problematic cases. Our results show that structured verification and targeted human oversight are essential for reliable legal formalization, especially in the presence of legal nuance and context-sensitive reasoning.

---


### 93. [ConfLayers: Adaptive Confidence-based Layer Skipping for Self-Speculative Decoding](https://arxiv.org/abs/2604.14612)

**<font color=#1a73e8>作者：</font>** Walaa Amer, Uday das, Fadi Kurdahi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-speculative decoding is an inference technique for large language models designed to speed up generation without sacrificing output quality. It combines fast, approximate decoding using a compact version of the model as a draft model with selective re-evaluation by the full target model. Some existing methods form the draft model by dynamically learning which layers to skip during inference, effectively creating a smaller subnetwork to speed up computation. However, using heuristic-based approaches to select layers to skip can often be simpler and more effective. In this paper, we propose ConfLayers, a dynamic plug-and-play approach to forming the draft model in self-speculative decoding via confidence-based intermediate layer skipping. The process iteratively computes confidence scores for all layers, selects layers to skip based on an adaptive threshold, evaluates the performance of the resulting set, and updates the best selection until no further improvement is achieved or a maximum number of iterations is reached. This framework avoids the overhead and complexity of training a layer skipping policy and can provide more consistent speed-quality trade-offs while preserving the adaptivity of the draft model to diverse tasks and datasets. The performance evaluation of ConfLayers across different models and datasets shows that our novel approach offers up to 1.4x speedup over vanilla LLM generation.

---


### 94. [CoDaS: AI Co-Data-Scientist for Biomarker Discovery via Wearable Sensors](https://arxiv.org/abs/2604.14615)

**<font color=#1a73e8>作者：</font>** Yubin Kim, Salman Rahman, Samuel Schmidgall 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery in digital health requires converting continuous physiological signals from wearable devices into clinically actionable biomarkers. We introduce CoDaS (AI Co-Data-Scientist), a multi-agent system that structures biomarker discovery as an iterative process combining hypothesis generation, statistical analysis, adversarial validation, and literature-grounded reasoning with human oversight using large-scale wearable datasets. Across three cohorts totaling 9,279 participant-observations, CoDaS identified 41 candidate digital biomarkers for mental health and 25 for metabolic outcomes, each subjected to an internal validation battery spanning replication, stability, robustness, and discriminative power. Across two independent depression cohorts, CoDaS surfaced circadian instability-related features in both datasets, reflected in sleep duration variability (DWB, \rho = 0.252, p < 0.001) and sleep onset variability (GLOBEM, \rho = 0.126, p < 0.001). In a metabolic cohort, CoDaS derived a cardiovascular fitness index (steps/resting heart rate; \rho = -0.374, p < 0.001), and recovered established clinical associations, including the hepatic function ratio (AST/ALT; \rho = -0.375, p < 0.001), a known correlate of insulin resistance. Incorporating CoDaS-derived features alongside demographic variables led to modest but consistent improvements in predictive performance, with cross-validated \Delta R^2 increases of 0.040 for depression and 0.021 for insulin resistance. These findings suggest that CoDaS enables systematic and traceable hypothesis generation and prioritization for biomarker discovery from large-scale wearable data.

---


### 95. [Multigrain-aware Semantic Prototype Scanning and Tri-Token Prompt Learning Embraced High-Order RWKV for Pan-Sharpening](https://arxiv.org/abs/2604.14622)

**<font color=#1a73e8>作者：</font>** Junfeng Li, Wenyang Zhou, Xueheng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we propose a Multigrain-aware Semantic Prototype Scanning paradigm for pan-sharpening, built upon a high-order RWKV architecture and a tri-token prompting mechanism derived from semantic clustering. Specifically, our method contains three key components: 1) Multigrain-aware Semantic Prototype Scanning. Although RWKV offers a efficient linear-complexity alternative to Transformers, its conventional bidirectional raster scanning is still semantic-agnostic and prone to positional bias. To address this issue, we introduce a semantic-driven scanning strategy that leverages locality-sensitive hashing to group semantically related regions and construct multi-grain semantic prototypes, enabling context-aware token reordering and more coherent global interaction. 2) Tri-token Prompt Learning. We design a tri-token prompting mechanism consisting of a global token, cluster-derived prototype tokens, and a learnable register token. The global and prototype tokens provide complementary semantic priors for RWKV modeling, while the register token helps suppress noisy and artifact-prone intermediate representations. 3) Invertible Q-Shift. To counteract spatial details, we apply center difference convolution on the value pathway to inject high-frequency information, and introduce an invertible multi-scale Q-shift operation for efficient and lossless feature transformation without parameter-heavy receptive field expansion. Experimental results demonstrate the superiority of our method.

---


### 96. [A Parallel Approach to Counting Exact Covers Based on Decomposability Property](https://arxiv.org/abs/2604.14627)

**<font color=#1a73e8>作者：</font>** Liangda Fang, Yaohui Luo, Delong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The exact cover problem is a classical NP-hard problem with broad applications in the area of AI. Algorithm DXZ is a method to count exact covers representing by zero-suppressed binary decision diagrams (ZBDDs). In this paper, we propose a zero-suppressed variant of decision decomposable negation normal form (in short, decision-ZDNNF), which is strictly more succinct than ZBDDs. We then design a novel parallel algorithm, namely DXD, which constructs a decision-ZDNNF representing the set of all exact covers. Furthermore, we improve DXD by dynamically updating connected components. The experimental results demonstrate that the improved DXD algorithm outperforms all of state-of-the-art methods.

---


### 97. [CMTM: Cross-Modal Token Modulation for Unsupervised Video Object Segmentation](https://arxiv.org/abs/2604.14630)

**<font color=#1a73e8>作者：</font>** Inseok Jeon, Suhwan Cho, Minhyeok Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in unsupervised video object segmentation have highlighted the potential of two-stream architectures that integrate appearance and motion cues. However, fully leveraging these complementary sources of information requires effectively modeling their interdependencies. In this paper, we introduce cross-modality token modulation, a novel approach designed to strengthen the interaction between appearance and motion cues. Our method establishes dense connections between tokens from each modality, enabling efficient intra-modal and inter-modal information propagation through relation transformer blocks. To improve learning efficiency, we incorporate a token masking strategy that addresses the limitations of relying solely on increased model complexity. Our approach achieves state-of-the-art performance across all public benchmarks, outperforming existing methods.

---


### 98. [High-Speed Full-Color HDR Imaging via Unwrapping Modulo-Encoded Spike Streams](https://arxiv.org/abs/2604.14632)

**<font color=#1a73e8>作者：</font>** Chu Zhou, Siqi Yang, Kailong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional RGB-based high dynamic range (HDR) imaging faces a fundamental trade-off between motion artifacts in multi-exposure captures and irreversible information loss in single-shot techniques. Modulo sensors offer a promising alternative by encoding theoretically unbounded dynamic range into wrapped measurements. However, existing modulo solutions remain bottlenecked by iterative unwrapping overhead and hardware constraints limiting them to low-speed, grayscale capture. In this work, we present a complete modulo-based HDR imaging system that enables high-speed, full-color HDR acquisition by synergistically advancing both the sensing formulation and the unwrapping algorithm. At the core of our approach is an exposure-decoupled formulation of modulo imaging that allows multiple measurements to be interleaved in time, preserving a clean, observation-wise measurement model. Building upon this, we introduce an iteration-free unwrapping algorithm that integrates diffusion-based generative priors with the physical least absolute remainder property of modulo images, supporting highly efficient, physics-consistent HDR reconstruction. Finally, to validate the practical viability of our system, we demonstrate a proof-of-concept hardware implementation based on modulo-encoded spike streams. This setup preserves the native high temporal resolution of spike cameras, achieving 1000 FPS full-color imaging while reducing output data bandwidth from approximately 20 Gbps to 6 Gbps. Extensive evaluations indicate that our coordinated approach successfully overcomes key systemic bottlenecks, demonstrating the feasibility of deploying modulo imaging in dynamic scenarios.

---


### 99. [Pushing the Boundaries of Multiple Choice Evaluation to One Hundred Options](https://arxiv.org/abs/2604.14634)

**<font color=#1a73e8>作者：</font>** Nahyun Lee, Guijin Son  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiple choice evaluation is widely used for benchmarking large language models, yet near ceiling accuracy in low option settings can be sustained by shortcut strategies that obscure true competence. Therefore, we propose a massive option evaluation protocol that scales the candidate set to one hundred options and sharply reduces the impact of chance performance. We apply this framework to a Korean orthography error detection task where models must pick the single incorrect sentence from a large candidate set. With fixed targets and repeated resampling and shuffling, we obtain stable estimates while separating content driven failures from positional artifacts. Across experiments, results indicate that strong performance in low option settings can overstate model competence. This apparent advantage often weakens under dense interference at high $N$, revealing gaps that conventional benchmarks tend to obscure. We identify two failure modes, semantic confusion and position bias toward early options under uncertainty. To isolate the effect of context length, we run padding controlled and length matched tests, which suggest that the main bottleneck is candidate ranking rather than context length. Together, these findings support massive option evaluation as a general framework for stress testing model reliability under extreme distractor density, beyond what low option benchmarks can reveal.

---


### 100. [Touching Space: Accessible Map Exploration Through Conversational Audio-Haptic Interaction](https://arxiv.org/abs/2604.14637)

**<font color=#1a73e8>作者：</font>** Li Liu, Jiaming Qu, Marc Jowell Bagaoisan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Most existing assistive navigation tools focus on providing real-time guidance for Blind and Low-Vision (BLV) people, but few support building a holistic spatial understanding of unfamiliar environments before travel. Such cognitive map construction (e.g., knowing that a fountain is south of a tower and west of a hotel) is important for pre-travel planning, yet remains underexplored in prior work. To address this gap, we present Touching Space, an end-to-end system that retrieves map data for a target place and loads it into a frontend interface for exploration. The system combines haptic and audio feedback: users explore spatial layouts through touch and ask spoken questions to a conversational agent during exploration. Touching Space contributes a conversational interface that supports BLV users in building cognitive maps on commodity hardware.

---


### 101. [Physically-Induced Atmospheric Adversarial Perturbations: Enhancing Transferability and Robustness in Remote Sensing Image Classification](https://arxiv.org/abs/2604.14643)

**<font color=#1a73e8>作者：</font>** Weiwei Zhuang, Wangze Xie, Qi Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks pose a severe threat to the reliability of deep learning models in remote sensing (RS) image classification. Most existing methods rely on direct pixel-wise perturbations, failing to exploit the inherent atmospheric characteristics of RS imagery or survive real-world image degradations. In this paper, we propose FogFool, a physically plausible adversarial framework that generates fog-based perturbations by iteratively optimizing atmospheric patterns based on Perlin noise. By modeling fog formations with natural, irregular structures, FogFool generates adversarial examples that are not only visually consistent with authentic RS scenes but also deceptive. By leveraging the spatial coherence and mid-to-low-frequency nature of atmospheric phenomena, FogFool embeds adversarial information into structural features shared across diverse architectures. Extensive experiments on two benchmark RS datasets demonstrate that FogFool achieves superior performance: not only does it exceed in white-box settings, but also exhibits exceptional black-box transferability (reaching 83.74% TASR) and robustness against common preprocessing-based defenses such as JPEG compression and filtering. Detailed analyses, including confusion matrices and Class Activation Map (CAM) visualizations, reveal that our atmospheric-driven perturbations induce a universal shift in model attention. These results indicate that FogFool represents a practical, stealthy, and highly persistent threat to RS classification systems, providing a robust benchmark for evaluating model reliability in complex environments.

---


### 102. [Chaotic CNN for Limited Data Image Classification](https://arxiv.org/abs/2604.14645)

**<font color=#1a73e8>作者：</font>** Anusree M, Akhila Henry, Pramod P Nair  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks (CNNs) often exhibit poor generalisation in limited training data scenarios due to overfitting and insufficient feature diversity. In this work, a simple and effective chaos-based feature transformation is proposed to enhance CNN performance without increasing model complexity. The method applies nonlinear transformations using logistic, skew tent, and sine maps to normalised feature vectors before the classification layer, thereby reshaping the feature space and improving class separability. The approach is evaluated on greyscale datasets (MNIST and Fashion-MNIST) and an RGB dataset (CIFAR-10) using CNN architectures of varying depth under limited data conditions. The results show consistent improvement over the standalone (SA) CNN across all datasets. Notably, a maximum performance gain of 5.43% is achieved on MNIST using the skew tent map with a 3-layer CNN at 40 samples per class. A higher gain of 9.11% is observed on Fashion-MNIST using the sine map with a 3-layer CNN at 50 samples per class. Additionally, a strong gain of 7.47% is obtained on CIFAR-10 using the skew tent map at 200 samples per class. The consistent improvements across different chaotic maps indicate that the performance gain is driven by the shared nonlinear and dynamical properties of chaotic systems. The proposed method is computationally efficient, requires no additional trainable parameters, and can be easily integrated into existing CNN architectures, making it a practical solution for data-scarce image classification tasks.

---


### 103. [Seen-to-Scene: Keep the Seen, Generate the Unseen for Video Outpainting](https://arxiv.org/abs/2604.14648)

**<font color=#1a73e8>作者：</font>** Inseok Jeon, Minhyeok Lee, Seunghoon Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video outpainting aims to expand the visible content of a video beyond the original frame boundaries while preserving spatial fidelity and temporal coherence across frames. Existing methods primarily rely on large-scale generative models, such as diffusion models. However, generationbased approaches suffer from implicit temporal modeling and limited spatial context. These limitations lead to intraframe and inter-frame inconsistencies, which become particularly pronounced in dynamic scenes and large outpainting scenarios. To overcome these challenges, we propose Seen-to-Scene, a novel framework that unifies propagationbased and generation-based paradigms for video outpainting. Specifically, Seen-to-Scene leverages flow-based propagation with a flow completion network pre-trained for video inpainting, which is fine-tuned in an end-to-end manner to bridge the domain gap and reconstruct coherent motion fields. To further improve the efficiency and reliability of propagation, we introduce a reference-guided latent propagation that effectively propagates source content across frames. Extensive experiments demonstrate that our method achieves superior temporal coherence and visual realism with efficient inference, surpassing even prior state-of-the-art methods that require input-specific adaptation.

---


### 104. [AgentGA: Evolving Code Solutions in Agent-Seed Space](https://arxiv.org/abs/2604.14655)

**<font color=#1a73e8>作者：</font>** David Y.Y. Tan, Kellie Chin, Jingxian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present AgentGA, a framework that evolves autonomous code-generation runs by optimizing the agent seed: the task prompt plus optional parent archives that initialize a fresh workspace. The outer loop searches over these reusable starting conditions rather than editing code directly. Each generation launches a fresh autonomous run from a reset workspace, while selected parent archives provide inherited artifacts that descendants can inspect and reuse. AgentGA couples a population-level genetic algorithm with long-horizon agents; selection uses deterministic 1:1 elite tournaments and operator allocation is adapted online with a modified Hedge controller. We instantiate the approach for tabular AutoML on the 16-competition Weco-Kaggle Lite benchmark. On the 10 benchmark runs reported here, AgentGA averages 74.52% Exceeds % of Human versus 54.15% for AIDE. Across 1135 parent-child comparisons, descendants given parent archives outperform runs started from scratch, indicating that inherited artifacts improve later autonomous runs. These findings support agent-seed optimization as a practical design point for autonomous code-search systems.

---


### 105. [EdgeDetect: Importance-Aware Gradient Compression with Homomorphic Aggregation for Federated Intrusion Detection](https://arxiv.org/abs/2604.14663)

**<font color=#1a73e8>作者：</font>** Noor Islam S. Mohammad  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative intrusion detection without raw data exchange, but conventional FL incurs high communication overhead from full-precision gradient transmission and remains vulnerable to gradient inference attacks. This paper presents EdgeDetect, a communication-efficient and privacy-aware federated IDS for bandwidth-constrained 6G-IoT environments. EdgeDetect introduces gradient smartification, a median-based statistical binarization that compresses local updates to $\{+1,-1\}$ representations, reducing uplink payload by $32\times$ while preserving convergence. We further integrate Paillier homomorphic encryption over binarized gradients, protecting against honest-but-curious servers without exposing individual updates. Experiments on CIC-IDS2017 (2.8M flows, 7 attack classes) demonstrate $98.0\%$ multi-class accuracy and $97.9\%$ macro F1-score, matching centralized baselines, while reducing per-round communication from $450$~MB to $14$~MB ($96.9\%$ reduction). Raspberry Pi-4 deployment confirms edge feasibility: $4.2$~MB memory, $0.8$~ms latency, and $12$~mJ per inference with $<0.5\%$ accuracy loss. Under $5\%$ poisoning attacks and severe imbalance, EdgeDetect maintains $87\%$ accuracy and $0.95$ minority class F1 ($p<0.001$), establishing a practical accuracy, communication, and privacy tradeoff for next-generation edge intrusion detection.

---


### 106. [Beyond Chat and Clicks: GUI Agents for In-Situ Assistance via Live Interface Transformation](https://arxiv.org/abs/2604.14668)

**<font color=#1a73e8>作者：</font>** Pan Hao, Rishi Selvakumaran, Jacob Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Complex visual interfaces are powerful yet have a steep learning curve, as users must navigate feature-rich visual interfaces while reasoning about domain-specific operations. Existing approaches either deliver assistance through a separate chat-based interaction, or require substantial application-specific engineering to build support natively into each interface. To address the gaps, we propose in-situ assistance: a mode of support delivered directly within any live web interface through lightweight, browser-level interventions on the Document Object Model (DOM), without rebuilding the application or modifying its underlying logic. We contribute a design space and a computational pipeline for DOM-mediated in-situ assistance, characterizing how GUI agents can insert, mutate, or recompose web elements to make the interface easier for users to understand, use, and navigate. We instantiate in-situ assistance in DOMSteer, a Chrome extension that interprets a user's help request and live interface context, grounds it to relevant UI elements, and executes reversible DOM manipulations directly on the live page to deliver assistance, including contextual tooltips, control highlighting, layout reorganization. Quantitative evaluations on two complex visual interfaces show that DOMSteer delivers reliable and efficient in-situ assistance. Use cases and a comparative user study with baseline ChatGPTAtlas demonstrate the usability and effectiveness of DOMSteer. Altogether, these findings point to a broader role for GUI agents: not just assisting from the sidelines, but actively reconfiguring live interfaces to support users in the moment.

---


### 107. [Zeroth-Order Optimization at the Edge of Stability](https://arxiv.org/abs/2604.14669)

**<font color=#1a73e8>作者：</font>** Minhak Song, Liang Zhang, Bingcong Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) methods are widely used when gradients are unavailable or prohibitively expensive, including black-box learning and memory-efficient fine-tuning of large models, yet their optimization dynamics in deep learning remain underexplored. In this work, we provide an explicit step size condition that exactly captures the (mean-square) linear stability of a family of ZO methods based on the standard two-point estimator. Our characterization reveals a sharp contrast with first-order (FO) methods: whereas FO stability is governed solely by the largest Hessian eigenvalue, mean-square stability of ZO methods depends on the entire Hessian spectrum. Since computing the full Hessian spectrum is infeasible in practical neural network training, we further derive tractable stability bounds that depend only on the largest eigenvalue and the Hessian trace. Empirically, we find that full-batch ZO methods operate at the edge of stability: ZO-GD, ZO-GDM, and ZO-Adam consistently stabilize near the predicted stability boundary across a range of deep learning training problems. Our results highlight an implicit regularization effect specific to ZO methods, where large step sizes primarily regularize the Hessian trace, whereas in FO methods they regularize the top eigenvalue.

---


### 108. [DETR-ViP: Detection Transformer with Robust Discriminative Visual Prompts](https://arxiv.org/abs/2604.14684)

**<font color=#1a73e8>作者：</font>** Bo Qian, Dahu Shi, Xing Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual prompted object detection enables interactive and flexible definition of target categories, thereby facilitating open-vocabulary detection. Since visual prompts are derived directly from image features, they often outperform text prompts in recognizing rare categories. Nevertheless, research on visual prompted detection has been largely overlooked, and it is typically treated as a byproduct of training text prompted detectors, which hinders its development. To fully unlock the potential of visual-prompted detection, we investigate the reasons why its performance is suboptimal and reveal that the underlying issue lies in the absence of global discriminability in visual prompts. Motivated by these observations, we propose DETR-ViP, a robust object detection framework that yields class-distinguishable visual prompts. On top of basic image-text contrastive learning, DETR-ViP incorporates global prompt integration and visual-textual prompt relation distillation to learn more discriminative prompt representations. In addition, DETR-ViP employs a selective fusion strategy that ensures stable and robust detection. Extensive experiments on COCO, LVIS, ODinW, and Roboflow100 demonstrate that DETR-ViP achieves substantially higher performance in visual prompt detection compared to other state-of-the-art counterparts. A series of ablation studies and analyses further validate the effectiveness of the proposed improvements and shed light on the underlying reasons for the enhanced detection capability of visual prompts.

---


### 109. [Beyond Nodes vs. Edges: A Multi-View Fusion Framework for Provenance-Based Intrusion Detection](https://arxiv.org/abs/2604.14685)

**<font color=#1a73e8>作者：</font>** Fan Yang, Binyan Xu, Di Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Provenance-based intrusion detection has emerged as a promising approach for analyzing complex attack behaviors through system-level provenance graphs. However, existing defense methods face an inherent granularity limitation. Node-centric detectors, which evaluate anomalies using entities' attributes and local structural patterns, may misclassify benign behavioral changes or configuration modifications as suspicious. In contrast, edge-centric detectors, which focus more on interactions, may lack sufficient contextual awareness of the involved entities, leading to missed detections when compromised entities perform seemingly ordinary operations. These analytical biases highlight a persistent gap between node-centric and edge-centric analyses. To mitigate this gap, we present PROVFUSION, a multi-view detection framework that integrates anomaly signals from three distinct views (i.e., attribute, structure, and causality). The framework fuses heterogeneous anomaly signals through lightweight fusion schemes and determines the final anomaly decisions through a voting-based integration process, providing a more consistent and context-aware assessment of system behavior. This design enables PROVFUSION to capture both entity level deviations and interaction-level anomalies within a consistent analytic pipeline. Experiments on nine widely used benchmark datasets demonstrate that PROVFUSION achieves higher detection accuracy and lower false-positive rates than single node- and edge-centric baselines, maintaining stable performance across scenarios. Overall, the results suggest that our multi-view anomaly fusion together with voting-based decision aggregation offers a practical and effective direction for advancing provenance-based intrusion detection.

---


### 110. [Chain-of-Glimpse: Search-Guided Progressive Object-Grounded Reasoning for Video Understanding](https://arxiv.org/abs/2604.14692)

**<font color=#1a73e8>作者：</font>** Zhixuan Wu, Quanxing Zha, Teng Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding requires identifying and reasoning over semantically discriminative visual objects across frames, yet existing object-agnostic solutions struggle to effectively handle substantial object variations over time. To address this, we introduce Chain-of-Glimpse, a search-guided progressive object-grounded reasoning framework that explicitly anchors each reasoning step to specific visual evidence regions, enabling compositional and multi-step decision-making. Formally, Chain-of-Glimpse formulates video reasoning as a step-by-step process that incrementally builds spatially grounded traces around task-relevant visual objects, thereby mitigating over-reliance on saliency-driven cues. Specifically, Chain-of-Glimpse features a search-guided controller, optimized via reinforcement learning with a format reward that significantly incentivizes grounding capability, to iteratively ground visual evidence regions and form reliable reasoning trajectories, yielding accurate and interpretable multi-step decisions. Extensive evaluations on both in domain NExTQA and out-of-domain Video-Holmes, CG-Bench Reasoning, and VRBench benchmarks demonstrate consistent performance gains, robustness and generalization of Chain-of-Glimpse across diverse video reasoning tasks.

---


### 111. [Mean Flow Policy Optimization](https://arxiv.org/abs/2604.14698)

**<font color=#1a73e8>作者：</font>** Xiaoyi Dong, Xi Sheryl Zhang, Jian Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently emerged as expressive policy representations for online reinforcement learning (RL). However, their iterative generative processes introduce substantial training and inference overhead. To overcome this limitation, we propose to represent policies using MeanFlow models, a class of few-step flow-based generative models, to improve training and inference efficiency over diffusion-based RL approaches. To promote exploration, we optimize MeanFlow policies under the maximum entropy RL framework via soft policy iteration, and address two key challenges specific to MeanFlow policies: action likelihood evaluation and soft policy improvement. Experiments on MuJoCo and DeepMind Control Suite benchmarks demonstrate that our method, Mean Flow Policy Optimization (MFPO), achieves performance comparable to or exceeding current diffusion-based baselines while considerably reducing training and inference time. Our code is available at this https URL.

---


### 112. [Gating Enables Curvature: A Geometric Expressivity Gap in Attention](https://arxiv.org/abs/2604.14702)

**<font color=#1a73e8>作者：</font>** Satwik Bathula, Anand A. Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multiplicative gating is widely used in neural architectures and has recently been applied to attention layers to improve performance and training stability in large language models. Despite the success of gated attention, the mathematical implications of gated attention mechanisms remain poorly understood. We study attention through the geometry of its representations by modeling outputs as mean parameters of Gaussian distributions and analyzing the induced Fisher--Rao geometry. We show that ungated attention operator is restricted to intrinsically flat statistical manifolds due to its affine structure, while multiplicative gating enables non-flat geometries, including positively curved manifolds that are unattainable in the ungated setting. These results establish a geometric expressivity gap between ungated and gated attention. Empirically, we show that gated models exhibit higher representation curvature and improved performance on tasks requiring nonlinear decision boundaries whereas they provide no consistent advantage on tasks with linear decision boundaries. Furthermore, we identify a structured regime in which curvature accumulates under composition, yielding a systematic depth amplification effect.

---


### 113. [The Courtroom Trial of Pixels: Robust Image Manipulation Localization via Adversarial Evidence and Reinforcement Learning Judgment](https://arxiv.org/abs/2604.14703)

**<font color=#1a73e8>作者：</font>** Songlin Li, Zhiqing Guo, Dan Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although some existing image manipulation localization (IML) methods incorporate authenticity-related supervision, this information is typically utilized merely as an auxiliary training signal to enhance the model's sensitivity to manipulation artifacts, rather than being explicitly modeled as localization evidence opposing the manipulated regions. Consequently, when manipulation traces are subtle or degraded by post-processing and noise, these methods struggle to explicitly compare manipulated and authentic evidence, resulting in unreliable predictions in ambiguous areas. To address these issues, we propose a courtroom-style adjudication framework that regards IML task as the confrontation of evidence followed by judgment. The framework comprises a prosecution stream, a defense stream, and a judge model. We first build a dual-hypothesis segmentation architecture on a shared multi-scale encoder, in which the prosecution stream asserts manipulation and the defense stream asserts authenticity. Guided by edge priors, it produces evidence for manipulated and authentic regions through cascaded multi-level fusion, bidirectional disagreement suppression, and dynamic debate refinement. We further develop a reinforcement learning judge model that performs strategic re-inference and refinement on uncertain regions, yielding a manipulated-region mask. The judge model is trained with advantage-based rewards and a soft-IoU objective, and reliability is calibrated via entropy and cross-hypothesis consistency. Experimental results show that our model achieves superior average performance compared with SOTA IML methods.

---


### 114. [SynHAT: A Two-stage Coarse-to-Fine Diffusion Framework for Synthesizing Human Activity Traces](https://arxiv.org/abs/2604.14705)

**<font color=#1a73e8>作者：</font>** Rongchao Xu, Lin Jiang, Dahai Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human activity traces (HATs) are critical for many applications, including human mobility modeling and point-of-interest (POI) recommendation. However, growing privacy concerns have severely limited access to authentic large-scale HAT datasets. Recent advances in generative AI provide new opportunities to synthesize realistic and privacy-preserving HATs for such applications. Yet two major challenges remain: (i) HATs are highly irregular and dynamic, with long and varying time intervals, making it difficult to capture their complex spatio-temporal dependencies and underlying distributions; and (ii) generative models are often computationally expensive, making long-term, fine-grained HAT synthesis inefficient. To address these challenges, we propose SynHAT, a computationally efficient coarse-to-fine HAT synthesis framework built on a novel spatio-temporal denoising diffusion model. In Stage 1, we develop Coarse-HADiff, which models the overall spatio-temporal dependencies of coarse-grained latent spatio-temporal traces. It incorporates a novel Latent Spatio-Temporal U-Net with dual Drift-Jitter branches to jointly model smooth spatial transitions and temporal variations during denoising. In Stage 2, we introduce a three-step pipeline consisting of Behavior Pattern Extraction, Fine-HADiff, which shares the same architecture as Coarse-HADiff, and Semantic Alignment to generate fine-grained latent spatio-temporal traces from the Stage 1 outputs. We extensively evaluate SynHAT in terms of data fidelity, utility, privacy, robustness, and scalability. Experiments on real-world HAT datasets from four cities across three countries show that SynHAT substantially outperforms state-of-the-art baselines, achieving 52% and 33% improvements on spatial and temporal metrics, respectively.

---


### 115. [NG-GS: NeRF-Guided 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/2604.14706)

**<font color=#1a73e8>作者：</font>** Yi He, Tao Wang, Yi Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D Gaussian Splatting (3DGS) have enabled highly efficient and photorealistic novel view synthesis. However, segmenting objects accurately in 3DGS remains challenging due to the discrete nature of Gaussian representations, which often leads to aliasing and artifacts at object boundaries. In this paper, we introduce NG-GS, a novel framework for high-quality object segmentation in 3DGS that explicitly addresses boundary discretization. Our approach begins by automatically identifying ambiguous Gaussians at object boundaries using mask variance analysis. We then apply radial basis function (RBF) interpolation to construct a spatially continuous feature field, enhanced by multi-resolution hash encoding for efficient multi-scale representation. A joint optimization strategy aligns 3DGS with a lightweight NeRF module through alignment and spatial continuity losses, ensuring smooth and consistent segmentation boundaries. Extensive experiments on NVOS, LERF-OVS, and ScanNet benchmarks demonstrate that our method achieves state-of-the-art performance, with significant gains in boundary mIoU. Code is available at this https URL.

---


### 116. [MS-SSE-Net: A Multi-Scale Spatial Squeeze-and-Excitation Network for Structural Damage Detection in Civil and Geotechnical Engineering](https://arxiv.org/abs/2604.14711)

**<font color=#1a73e8>作者：</font>** Saif ur Rehman Khan, Imad Ahmed Waqar, Arooj Zaib 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structural damage detection is essential for maintaining the safety and reliability of civil infrastructure. However, accurately identifying different types of structural damage from images remains challenging due to variations in damage patterns and environmental conditions. To address these challenges, this paper proposes MS-SSE-Net, a novel deep learning (DL) framework for structural damage classification. The proposed model is built upon the DenseNet201 backbone and integrates novel multi-scale feature extraction with channel and spatial attention mechanisms (MS-SSE-Net). Specifically, parallel depthwise convolutions capture both local and contextual features, while squeeze-and-excitation style channel attention and spatial attention emphasize informative regions and suppress irrelevant noise. The refined features are then processed through global average pooling and a fully connected classification layer to generate the final predictions. Experiments are conducted on the StructDamage dataset containing multiple structural damage categories. The proposed MS-SSE-Net demonstrates superior performance compared with the baseline DenseNet201 and other comparative approaches. Specifically, the proposed method achieves 99.31% precision, 99.25% recall, 99.27% F1-score, and 99.26% accuracy, outperforming the baseline model which achieved 98.62% precision, 98.53% recall, 98.58% F1-score, and 98.53% accuracy.

---


### 117. [Layered Mutability: Continuity and Governance in Persistent Self-Modifying Agents](https://arxiv.org/abs/2604.14717)

**<font color=#1a73e8>作者：</font>** Krti Tallam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent language-model agents increasingly combine tool use, tiered memory, reflective prompting, and runtime adaptation. In such systems, behavior is shaped not only by current prompts but by mutable internal conditions that influence future action. This paper introduces layered mutability, a framework for reasoning about that process across five layers: pretraining, post-training alignment, self-narrative, memory, and weight-level adaptation. The central claim is that governance difficulty rises when mutation is rapid, downstream coupling is strong, reversibility is weak, and observability is low, creating a systematic mismatch between the layers that most affect behavior and the layers humans can most easily inspect. I formalize this intuition with simple drift, governance-load, and hysteresis quantities, connect the framework to recent work on temporal identity in language-model agents, and report a preliminary ratchet experiment in which reverting an agent's visible self-description after memory accumulation fails to restore baseline behavior. In that experiment, the estimated identity hysteresis ratio is 0.68. The main implication is that the salient failure mode for persistent self-modifying agents is not abrupt misalignment but compositional drift: locally reasonable updates that accumulate into a behavioral trajectory that was never explicitly authorized.

---


### 118. [The Agentification of Scientific Research: A Physicist's Perspective](https://arxiv.org/abs/2604.14718)

**<font color=#1a73e8>作者：</font>** Xiao-Liang Qi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This article argues that the most important significance of the AI revolution, especially the rise of large language models, lies not simply in automation, but in a fundamental change in how complex information and human know-how are carried, replicated, and shared. From this perspective, AI for Science is especially important because it may transform not only the efficiency of research, but also the structure of scientific collaboration, discovery, publishing, and evaluation. The article outlines a gradual path from AI as a research tool to AI as a scientific collaborator, and discusses how AI is likely to fundamentally reshape scientific publication. It also argues that continuous learning and diversity of ideas are essential if AI is to play a meaningful role in original scientific discovery.

---


### 119. [Data Synthesis Improves 3D Myotube Instance Segmentation](https://arxiv.org/abs/2604.14720)

**<font color=#1a73e8>作者：</font>** David Exler, Nils Friederich, Martin Krüger 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Myotubes are multinucleated muscle fibers serving as key model systems for studying muscle physiology, disease mechanisms, and drug responses. Mechanistic studies and drug screening thereby rely on quantitative morphological readouts such as diameter, length, and branching degree, which in turn require precise three-dimensional instance segmentation. Yet established pretrained biomedical segmentation models fail to generalize to this domain due to the absence of large annotated myotube datasets. We introduce a geometry-driven synthesis pipeline that models individual myotubes via polynomial centerlines, locally varying radii, branching structures, and ellipsoidal end caps derived from real microscopy observations. Synthetic volumes are rendered with realistic noise, optical artifacts, and CycleGAN-based Domain Adaptation (DA). A compact 3D U-Net with self-supervised encoder pretraining, trained exclusively on synthetic data, achieves a mean IPQ of 0.22 on real data, significantly outperforming three established zero-shot segmentation models, demonstrating that biophysics-driven synthesis enables effective instance segmentation in annotation-scarce biomedical domains.

---


### 120. [HAMSA: Scanning-Free Vision State Space Models via SpectralPulseNet](https://arxiv.org/abs/2604.14724)

**<font color=#1a73e8>作者：</font>** Badri N. Patro, Vijay S. Agneeswaran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision State Space Models (SSMs) like Vim, VMamba, and SiMBA rely on complex scanning strategies to adapt sequential SSMs to process 2D images, introducing computational overhead and architectural complexity. We propose HAMSA, a scanning-free SSM operating directly in the spectral domain. HAMSA introduces three key innovations: (1) simplified kernel parameterization-a single Gaussian-initialized complex kernel replacing traditional (A, B, C) matrices, eliminating discretization instabilities; (2) SpectralPulseNet (SPN)-an input-dependent frequency gating mechanism enabling adaptive spectral modulation; and (3) Spectral Adaptive Gating Unit (SAGU)-magnitude-based gating for stable gradient flow in the frequency domain. By leveraging FFT-based convolution, HAMSA eliminates sequential scanning while achieving O(L log L) complexity with superior simplicity and efficiency. On ImageNet-1K, HAMSA reaches 85.7% top-1 accuracy (state-of-the-art among SSMs), with 2.2 X faster inference than transformers (4.2ms vs 9.2ms for DeiT-S) and 1.4-1.9X speedup over scanning-based SSMs, while using less memory (2.1GB vs 3.2-4.5GB) and energy (12.5J vs 18-25J). HAMSA demonstrates strong generalization across transfer learning and dense prediction tasks.

---


### 121. [Catching Every Ripple: Enhanced Anomaly Awareness via Dynamic Concept Adaptation](https://arxiv.org/abs/2604.14726)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhu, Shaofeng Cai, Jie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online anomaly detection (OAD) plays a pivotal role in real-time analytics and decision-making for evolving data streams. However, existing methods often rely on costly retraining and rigid decision boundaries, limiting their ability to adapt both effectively and efficiently to concept drift in dynamic environments. To address these challenges, we propose DyMETER, a dynamic concept adaptation framework for OAD that unifies on-the-fly parameter shifting and dynamic thresholding within a single online paradigm. DyMETER first learns a static detector on historical data to capture recurring central concepts, and then transitions to a dynamic mode to adapt to new concepts as drift occurs. Specifically, DyMETER employs a novel dynamic concept adaptation mechanism that leverages a hypernetwork to generate instance-aware parameter shifts for the static detector, thereby enabling efficient and effective adaptation without retraining or fine-tuning. To achieve robust and interpretable adaptation, DyMETER introduces a lightweight evolution controller to estimate instance-level concept uncertainty for adaptive updates. Further, DyMETER employs a dynamic threshold optimization module to adaptively recalibrates the decision boundary by maintaining a candidate window of uncertain samples, which ensures continuous alignment with evolving concepts. Extensive experiments demonstrate that DyMETER significantly outperforms existing OAD approaches across a wide spectrum of application scenarios.

---


### 122. [Expressivity of Transformers: A Tropical Geometry Perspective](https://arxiv.org/abs/2604.14727)

**<font color=#1a73e8>作者：</font>** Ye Su, Yong Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To quantify the geometric expressivity of transformers, we introduce a tropical geometry framework to characterize their exact spatial partitioning capabilities. By modeling self-attention as a vector-valued tropical rational map, we prove it evaluates exactly to a Power Voronoi Diagram in the zero-temperature limit. Building on this equivalence, we establish a combinatorial rationale for Multi-Head Self-Attention (MHSA): via the Minkowski sum of Newton polytopes, multi-head aggregation expands the polyhedral complexity to $\mathcal{O}(N^H)$, overcoming the $\mathcal{O}(N)$ bottleneck of single heads. Extending this to deep architectures, we derive the first tight asymptotic bounds on the number of linear regions in transformers ($\Theta(N^{d_{\text{model}}L})$), demonstrating a combinatorial explosion driven intrinsically by sequence length $N$, ambient embedding dimension $d_{\text{model}}$, and network depth $L$. Importantly, we guarantee that this idealized polyhedral skeleton is geometrically stable: finite-temperature soft attention preserves these topological partitions via exponentially tight differential approximation bounds.

---


### 123. [Find the Differences: Differential Morphing Attack Detection vs Face Recognition](https://arxiv.org/abs/2604.14734)

**<font color=#1a73e8>作者：</font>** Una M. Kelly, Luuk J. Spreeuwers, Raymond N.J. Veldhuis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Morphing is a challenge to face recognition (FR) for which several morphing attack detection solutions have been proposed. We argue that face recognition and differential morphing attack detection (D-MAD) in principle perform very similar tasks, which we support by comparing an FR system with two existing D-MAD approaches. We also show that currently used decision thresholds inherently lead to FR systems being vulnerable to morphing attacks and that this explains the tradeoff between performance on normal images and vulnerability to morphing attacks. We propose using FR systems that are already in place for morphing detection and introduce a new evaluation threshold that guarantees an upper limit to the vulnerability to morphing attacks - even of unknown types.

---


### 124. [Personalized and Context-Aware Transformer Models for Predicting Post-Intervention Physiological Responses from Wearable Sensor Data](https://arxiv.org/abs/2604.14738)

**<font color=#1a73e8>作者：</font>** Esther Brown, Victoria Dean, Finale Doshi-Velez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Consumer wearables enable continuous measurement of physiological data related to stress and recovery, but turning these streams into actionable, personalized stress-management recommendations remains a challenge. In practice, users often do not know how a given intervention, defined as an activity intended to reduce stress, will affect heart rate (HR), heart rate variability (HRV), or inter-beat intervals (BBI) over the next 15 to 120 minutes. We present a framework that predicts post-intervention trajectories and the direction of change for these physiological indicators across time windows. Our methodology combines a Transformer model for multi-horizon trajectories of percent change relative to a pre-intervention baseline, direction-of-change calls (positive, negative, or neutral) at each horizon, and an empirical study using wearable sensor data overlaid with user-tagged events and interventions. This proof of concept shows that personalized post-intervention prediction is feasible. We encourage future integration into stress-management tools for personalized intervention recommendations tailored to each person's day following further validation in larger studies and, where applicable, appropriate regulatory review.

---


### 125. [Efficient closed-form approaches for pose estimation using Sylvester forms](https://arxiv.org/abs/2604.14747)

**<font color=#1a73e8>作者：</font>** Jana Vráblíková, Ezio Malis, Laurent Busé  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Solving non-linear least-squares problem for pose estimation (rotation and translation) is often a time consuming yet fundamental problem in several real-time computer vision applications. With an adequate rotation parametrization, the optimization problem can be reduced to the solution of a~system of polynomial equations and solved in closed form. Recent advances in efficient closed form solvers utilizing resultant matrices have shown a promising research direction to decrease the computation time while preserving the estimation accuracy. In this paper, we propose a new class of resultant-based solvers that exploit Sylvester forms to further reduce the complexity of the resolution. We demonstrate that our proposed methods are numerically as accurate as the state-of-the-art solvers, and outperform them in terms of computational time. We show that this approach can be applied for pose estimation in two different types of problems: estimating a pose from 3D to 3D correspondences, and estimating a pose from 3D points to 2D points correspondences.

---


### 126. [Which bird does not have wings: Negative-constrained KGQA with Schema-guided Semantic Matching and Self-directed Refinement](https://arxiv.org/abs/2604.14749)

**<font color=#1a73e8>作者：</font>** Midan Shim, Seokju Hwang, Kaehyun Um 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models still struggle with faithfulness and hallucinations despite their remarkable reasoning abilities. In Knowledge Graph Question Answering (KGQA), semantic parsing-based approaches address the limitations by understanding constraints in a user's question and converting them into a logical form to execute on a knowledge graph. However, existing KGQA benchmarks and methods are biased toward positive and calculation constraints. Negative constraints are neglected, although they frequently appear in real-world questions. In this paper, we introduce a new task, NEgative-conSTrained (NEST) KGQA, where each question contains at least one negative constraint, and a corresponding dataset, NestKGQA. We also design PyLF, a Python-formatted logical form, since existing logical forms are hardly suitable to express negation clearly while maintaining readability. Furthermore, NEST questions naturally contain multiple constraints. To mitigate their semantic complexity, we present a novel framework named CUCKOO, specialized to multiple-constrained questions and ensuring semantic executability. CUCKOO first generates a constraint-aware logical form draft and performs schema-guided semantic matching. It then selectively applies self-directed refinement only when executing improper logical forms yields an empty result, reducing cost while improving robustness. Experimental results demonstrate that CUCKOO consistently outperforms baselines on both conventional KGQA and NEST-KGQA benchmarks under few-shot settings.

---


### 127. [ASGNet: Adaptive Spectrum Guidance Network for Automatic Polyp Segmentation](https://arxiv.org/abs/2604.14755)

**<font color=#1a73e8>作者：</font>** Yanguang Sun, Hengmin Zhang, Jianjun Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early identification and removal of polyps can reduce the risk of developing colorectal cancer. However, the diverse morphologies, complex backgrounds and often concealed nature of polyps make polyp segmentation in colonoscopy images highly challenging. Despite the promising performance of existing deep learning-based polyp segmentation methods, their perceptual capabilities remain biased toward local regions, mainly because of the strong spatial correlations between neighboring pixels in the spatial domain. This limitation makes it difficult to capture the complete polyp structures, ultimately leading to sub-optimal segmentation results. In this paper, we propose a novel adaptive spectrum guidance network, called ASGNet, which addresses the limitations of spatial perception by integrating spectral features with global attributes. Specifically, we first design a spectrum-guided non-local perception module that jointly aggregates local and global information, therefore enhancing the discriminability of polyp structures, and refining their boundaries. Moreover, we introduce a multi-source semantic extractor that integrates rich high-level semantic information to assist in the preliminary localization of polyps. Furthermore, we construct a dense cross-layer interaction decoder that effectively integrates diverse information from different layers and strengthens it to generate high-quality representations for accurate polyp segmentation. Extensive quantitative and qualitative results demonstrate the superiority of our ASGNet approach over 21 state-of-the-art methods across five widely-used polyp segmentation benchmarks. The code will be publicly available at: this https URL.

---


### 128. [OmniGCD: Abstracting Generalized Category Discovery for Modality Agnosticism](https://arxiv.org/abs/2604.14762)

**<font color=#1a73e8>作者：</font>** Jordan Shipard, Arnold Wiliem, Kien Nguyen Thanh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized Category Discovery (GCD) challenges methods to identify known and novel classes using partially labeled data, mirroring human category learning. Unlike prior GCD methods, which operate within a single modality and require dataset-specific fine-tuning, we propose a modality-agnostic GCD approach inspired by the human brain's abstract category formation. Our $\textbf{OmniGCD}$ leverages modality-specific encoders (e.g., vision, audio, text, remote sensing) to process inputs, followed by dimension reduction to construct a $\textbf{GCD latent space}$, which is transformed at test-time into a representation better suited for clustering using a novel synthetically trained Transformer-based model. To evaluate OmniGCD, we introduce a $\textbf{zero-shot GCD setting}$ where no dataset-specific fine-tuning is allowed, enabling modality-agnostic category discovery. $\textbf{Trained once on synthetic data}$, OmniGCD performs zero-shot GCD across 16 datasets spanning four modalities, improving classification accuracy for known and novel classes over baselines (average percentage point improvement of $\textbf{+6.2}$, $\textbf{+17.9}$, $\textbf{+1.5}$ and $\textbf{+12.7}$ for vision, text, audio and remote sensing). This highlights the importance of strong encoders while decoupling representation learning from category discovery. Improving modality-agnostic methods will propagate across modalities, enabling encoder development independent of GCD. Our work serves as a benchmark for future modality-agnostic GCD works, paving the way for scalable, human-inspired category discovery. All code is available $\href{this https URL}{here}$

---


### 129. [Wasserstein Formulation of Reinforcement Learning. An Optimal Transport Perspective on Policy Optimization](https://arxiv.org/abs/2604.14765)

**<font color=#1a73e8>作者：</font>** Mathias Dus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a geometric framework for Reinforcement Learning (RL) that views policies as maps into the Wasserstein space of action probabilities. First, we define a Riemannian structure induced by stationary distributions, proving its existence in a general context. We then define the tangent space of policies and characterize the geodesics, specifically addressing the measurability of vector fields mapped from the state space to the tangent space of probability measures over the action space. Next, we formulate a general RL optimization problem and construct a gradient flow using Otto's calculus. We compute the gradient and the Hessian of the energy, providing a formal second-order analysis. Finally, we illustrate the method with numerical examples for low-dimensional problems, computing the gradient directly from our theoretical formalism. For high-dimensional problems, we parameterize the policy using a neural network and optimize it based on an ergodic approximation of the cost.

---


### 130. [CoPA: Benchmarking Personalized Question Answering with Data-Informed Cognitive Factors](https://arxiv.org/abs/2604.14773)

**<font color=#1a73e8>作者：</font>** Hang Su, Zequn Liu, Chen Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While LLMs have demonstrated remarkable potential in Question Answering (QA), evaluating personalization remains a critical bottleneck. Existing paradigms predominantly rely on lexical-level similarity or manual heuristics, often lacking sufficient data-driven validation. We address this by mining Community-Individual Preference Divergence (CIPD), where individual choices override consensus, to distill six key personalization factors as evaluative dimensions. Accordingly, we introduce CoPA, a benchmark with 1,985 user profiles for fine-grained, factor-level assessment. By quantifying the alignment between model outputs and user-specific cognitive preferences inferred from interaction patterns, CoPA provides a more comprehensive and discriminative standard for evaluating personalized QA than generic metrics. The code is available at this https URL.

---


### 131. [AIM: Asymmetric Information Masking for Visual Question Answering Continual Learning](https://arxiv.org/abs/2604.14779)

**<font color=#1a73e8>作者：</font>** Peifeng Zhang, Zice Qiu, Donghua Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In continual visual question answering (VQA), existing Continual Learning (CL) methods are mostly built for symmetric, unimodal architectures. However, modern Vision-Language Models (VLMs) violate this assumption, as their trainable components are inherently asymmetric. This structural mismatch renders VLMs highly prone to catastrophic forgetting when learning from continuous data streams. Specifically, the asymmetry causes standard global regularization to favor the massive language decoder during optimization, leaving the smaller but critical visual projection layers highly vulnerable to interference. Consequently, this localized degradation leads to a severe loss of compositional reasoning capabilities. To address this, we propose Asymmetric Information Masking (AIM), which balances stability and plasticity by applying targeted masks based on modality-specific sensitivity. Experiments on VQA v2 and GQA under continual VQA settings show that AIM achieves state-of-the-art performance in both Average Performance (AP) and Average Forgetting (AF), while better preserving generalization to novel skill-concept compositions.

---


### 132. [Integrating Object Detection, LiDAR-Enhanced Depth Estimation, and Segmentation Models for Railway Environments](https://arxiv.org/abs/2604.14781)

**<font color=#1a73e8>作者：</font>** Enrico Francesco Giannico, Federico Nesti, Gianluca D'Amico 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Obstacle detection in railway environments is crucial for ensuring safety. However, very few studies address the problem using a complete, modular, and flexible system that can both detect objects in the scene and estimate their distance from the vehicle. Most works focus solely on detection, others attempt to identify the track, and only a few estimate obstacle distances. Additionally, evaluating these systems is challenging due to the lack of ground truth data. In this paper, we propose a modular and flexible framework that identifies the rail track, detects potential obstacles, and estimates their distance by integrating three neural networks for object detection, track segmentation, and monocular depth estimation with LiDAR point clouds. To enable a reliable and quantitative evaluation, the proposed framework is assessed using a synthetic dataset (SynDRA), which provides accurate ground truth annotations, allowing for direct performance comparison with existing methods. The proposed system achieves a mean absolute error (MAE) as low as 0.63 meters by integrating monocular depth maps with LiDAR, enabling not only accurate distance estimates but also spatial perception of the scene.

---


### 133. [One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782)

**<font color=#1a73e8>作者：</font>** Yuan Sun, Xuan Wang, WeiLi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a compositional method for constructing a complete 3D head avatar from a single image. Prior one-shot holistic approaches frequently fail to produce realistic hair dynamics during animation, largely due to inadequate decoupling of hair from the facial region, resulting in entangled geometry and unnatural deformations. Our method explicitly decouples hair from the face, modeling these components using distinct deformation paradigms while integrating them into a unified rendering pipeline. Furthermore, by leveraging image-to-3D lifting techniques, we preserve fine-grained textures from the input image to the greatest extent possible, effectively mitigating the common issue of high-frequency information loss in generalized models. Specifically, given a frontal portrait image, we first perform hair removal to obtain a bald image. Both the original image and the bald image are then lifted to dense, detail-rich 3D Gaussian Splatting (3DGS) representations. For the bald 3DGS, we rig it to a FLAME mesh via non-rigid registration with a prior model, enabling natural deformation that follows the mesh triangles during animation. For the hair component, we employ semantic label supervision combined with a boundary-aware reassignment strategy to extract a clean and isolated set of hair Gaussians. To control hair deformation, we introduce a cage structure that supports Position-Based Dynamics (PBD) simulation, allowing realistic and physically plausible transformations of the hair Gaussian primitives under head motion, gravity, and inertial effects. Striking qualitative results, including dynamic animations under diverse head motions, gravity effects, and expressions, showcase substantially more realistic hair behavior alongside faithfully preserved facial details, outperforming state-of-the-art one-shot methods in perceptual realism.

---


### 134. [CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution](https://arxiv.org/abs/2604.14786)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Yihang Cheng, Zhirong Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative Agents, owing to their precise modeling and simulation capabilities of human behavior, have become a pivotal tool in the field of Artificial Intelligence in Education (AIEd) for uncovering complex cognitive processes of learners. However, existing educational agents predominantly rely on static personas to simulate student learning behaviors, neglecting the decisive role of deep cognitive capabilities in learning outcomes during practice interactions. Furthermore, they struggle to characterize the dynamic fluidity of knowledge internalization, transfer, and cognitive state transitions. To overcome this bottleneck, this paper proposes a human-like educational agent capable of simulating student cognitive evolution: CogEvolution. Specifically, we first construct a cognitive depth perceptron based on the Interactive, Constructive, Active, Passive (ICAP) taxonomy from cognitive psychology, achieving precise quantification of learner cognitive engagement. Subsequently, we propose a memory retrieval method based on Item Response Theory (IRT) to simulate the connection and assimilation of new and prior knowledge. Finally, we design a dynamic cognitive update mechanism based on evolutionary algorithms to simulate the real-time integration of student learning behaviors and cognitive evolution processes. Comprehensive evaluations demonstrate that CogEvolution not only significantly outperforms baseline models in behavioral fidelity and learning curve fitting but also uniquely reproduces plausible and robust cognitive evolutionary paths consistent with educational psychology expectations, providing a novel paradigm for constructing highly interpretable educational agents.

---


### 135. [Sequence Search: Automated Sequence Design using Neural Architecture Search](https://arxiv.org/abs/2604.14788)

**<font color=#1a73e8>作者：</font>** Rokgi Hong, Hongjun An, Sooyeon Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing an MR sequence is challenging and remains largely constrained by human intuition. Recently, AI-driven approaches have been proposed; however, most require an initial sequence for parameter optimization or extensive training datasets, limiting their general applicability. In this study, we propose "Sequence Search," an automated sequence design framework based on neural architecture search. The method takes tissue properties, imaging parameters, and design objectives as inputs and generates pulse sequences satisfying the design objectives, without requiring prior knowledge of conventional sequence structures. Sequence Search iteratively generates candidate sequences through neural architecture search and optimizes them via a differentiable Bloch simulator and objective-specific loss functions using gradient-based learning. The framework successfully replicated conventional spin-echo, T2-weighted spin-echo, and inversion recovery sequences. Less intuitive solutions were also discovered, such as three-RF spin-echo-like sequences with reduced RF energy and refocusing phases deviating from the conventional Hahn-echo. This work establishes a generalizable framework for automated MR sequence design, highlighting the potential to explore configurations beyond conventional designs based on human intuition.

---


### 136. [A Comparative Study of CNN Optimization Methods for Edge AI: Exploring the Role of Early Exits](https://arxiv.org/abs/2604.14789)

**<font color=#1a73e8>作者：</font>** Nekane Fernandez, Ivan Valdes, Steven Van Vaerenbergh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying deep neural networks on edge devices requires balancing accuracy, latency, and resource constraints under realistic execution conditions. To fit models within these constraints, two broad strategies have emerged: static compression techniques such as pruning and quantization, which permanently reduce model size, and dynamic approaches such as early-exit mechanisms, which adapt computational cost at runtime. While both families are widely studied in isolation, they are rarely compared under identical conditions on physical hardware. This paper presents a unified deployment-oriented comparison of static compression and dynamic early-exit mechanisms, evaluated on real edge devices using ONNX based inference pipelines. Our results show that static and dynamic techniques offer fundamentally different trade-offs for edge deployment. While pruning and quantization deliver consistent memory footprint reduction, early-exit mechanisms enable input-adaptive computation savings that static methods cannot match. Their combination proves highly effective, simultaneously reducing inference latency and memory usage with minimal accuracy loss, expanding what is achievable at the edge.

---


### 137. [Diffusion Crossover: Defining Evolutionary Recombination in Diffusion Models via Noise Sequence Interpolation](https://arxiv.org/abs/2604.14790)

**<font color=#1a73e8>作者：</font>** Chisatao Kumada, Satoru Hiwa, Tomoyuki Hiroyasu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive Evolutionary Computation (IEC) provides a powerful framework for optimizing subjective criteria such as human preferences and aesthetics, yet it suffers from a fundamental limitation: in high-dimensional generative representations, defining crossover in a semantically consistent manner is difficult, often leading to a mutation-dominated search. In this work, we explicitly define crossover in diffusion models. We propose Diffusion crossover, which formulates evolutionary recombination as step-wise interpolation of noise sequences in the reverse process of Denoising Diffusion Probabilistic Models (DDPMs). By applying spherical linear interpolation (Slerp) to the noise sequences associated with selected parent images, the proposed method generates offspring that inherit characteristics from both parents while preserving the geometric structure of the diffusion process. Furthermore, controlling the time-step range of interpolation enables a principled trade-off between diversity (exploration) and convergence (exploitation). Experimental results using PCA analysis and perceptual similarity metrics (LPIPS) demonstrate that Diffusion crossover produces perceptually smooth and semantically consistent transitions between parent images. Qualitative interactive evolution experiments further confirm that the proposed method effectively supports human-in-the-loop image exploration. These findings suggest a new perspective: diffusion models are not only powerful generators, but also structured evolutionary search spaces in which recombination can be explicitly defined and controlled.

---


### 138. [Evaluating Encodings for Bivariate Edges in Adjacency Matrices](https://arxiv.org/abs/2604.14791)

**<font color=#1a73e8>作者：</font>** Jorge Acosta-Hernández, Alexander Lex, Tingying He  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present the first empirical evaluation of techniques for encoding distributions of quantitative edge values within adjacency matrices. In many real-world networks, edges represent not a single value but a set of measurements. While adjacency matrices preserve structural clarity, their compact cells limit the simultaneous display of multiple values. To address this, we explore edge encodings that represent distributions by two values: a measure of central tendency (mean, median, mode) and a measure of dispersion (standard deviation, variance, IQR). We select four possible encodings for evaluation that prior work has suggested are suitable for the limited space available in matrices: a bivariate color palette, embedded bar charts, and two overlaid-mark designs mapping the primary attribute to color and the secondary attribute to area or angle. In a preregistered crowdsourced study with 156 participants, we assessed performance of these encodings across eight analytical tasks and collected readability and aesthetic ratings. Results reveal clear performance regimes: area-based overlaid marks and bar charts achieved the highest overall performance; angle-based marks show moderate but less stable performance,and bivariate color consistently underperforms these alternatives. These findings clarify how visual channels behave under strict constraints and delineate the strengths and limitations of key design choices for multivariate edge visualization.

---


### 139. [From Boundaries to Semantics: Prompt-Guided Multi-Task Learning for Petrographic Thin-section Segmentation](https://arxiv.org/abs/2604.14805)

**<font color=#1a73e8>作者：</font>** Yili Ren, Shiqi Wen, Li Hou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grain-edge segmentation (GES) and lithology semantic segmentation (LSS) are two pivotal tasks for quantifying rock fabric and composition. However, these two tasks are often treated separately, and the segmentation quality is implausible albeit expensive, time-consuming, and expert-annotated datasets have been used. Recently, foundation models, especially the Segment Anything Model (SAM), have demonstrated impressive robustness for boundary alignment. However, directly adapting SAM to joint GES and LSS is nontrivial due to 1) severe domain gap induced by extinction-dependent color variations and ultra-fine grain boundaries, and 2) lacking novel modules for joint learning on multi-angle petrographic image stacks. In this paper, we propose Petro-SAM, a novel two-stage, multi-task framework that can achieve high-quality joint GES and LSS on petrographic images. Specifically, based on SAM, we introduce a Merge Block to integrate seven polarized views, effectively solving the extinction issue. Moreover, we introduce multi-scale feature fusion and color-entropy priors to refine the detection.

---


### 140. [NTIRE 2026 Challenge on Video Saliency Prediction: Methods and Results](https://arxiv.org/abs/2604.14816)

**<font color=#1a73e8>作者：</font>** Andrey Moskalenko, Alexey Bryncev, Ivan Kosmynin 等 43 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents an overview of the NTIRE 2026 Challenge on Video Saliency Prediction. The goal of the challenge participants was to develop automatic saliency map prediction methods for the provided video sequences. The novel dataset of 2,000 diverse videos with an open license was prepared for this challenge. The fixations and corresponding saliency maps were collected using crowdsourced mouse tracking and contain viewing data from over 5,000 assessors. Evaluation was performed on a subset of 800 test videos using generally accepted quality metrics. The challenge attracted over 20 teams making submissions, and 7 teams passed the final phase with code review. All data used in this challenge is made publicly available - this https URL.

---


### 141. [Pangu-ACE: Adaptive Cascaded Experts for Educational Response Generation on EduBench](https://arxiv.org/abs/2604.14828)

**<font color=#1a73e8>作者：</font>** Dinghao Li, Wenlong Zhou, Zhimin Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Educational assistants should spend more computation only when the task needs it. This paper rewrites our earlier draft around the system that was actually implemented and archived in the repository: a sample-level 1B to 7B cascade for the shared-8 EduBench benchmark. The final system, Pangu-ACE, uses a 1B tutor-router to produce a draft answer plus routing signals, then either accepts the draft or escalates the sample to a 7B specialist prompt. We also correct a major offline evaluation bug: earlier summaries over-credited some open-form outputs that only satisfied superficial format checks. After CPU-side rescoring from saved prediction JSONL, the full Chinese test archive (7013 samples) shows that cascade_final improves deterministic quality from 0.457 to 0.538 and format validity from 0.707 to 0.866 over the legacy rule_v2 system while accepting 19.7% of requests directly at 1B. Routing is strongly task dependent: IP is accepted by 1B 78.0% of the time, while QG and EC still escalate almost always. The current archived deployment does not yet show latency gains, so the defensible efficiency story is routing selectivity rather than wall-clock speedup. We also package a reproducible artifact-first paper workflow and clarify the remaining external-baseline gap: GPT-5.4 re-judging is implemented locally, but the configured provider endpoint and key are invalid, so final sampled-baseline alignment with GPT-5.4 remains pending infrastructure repair.

---


### 142. [Beyond Literal Summarization: Redefining Hallucination for Medical SOAP Note Evaluation](https://arxiv.org/abs/2604.14829)

**<font color=#1a73e8>作者：</font>** Bhavik Vachhani, Kush Shrisvastava, Pranshu Nema 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) for clinical documentation tasks such as SOAP note generation remains challenging. Unlike standard summarization, these tasks require clinical abstraction, normalization of colloquial language, and medically grounded inference. However, prevailing evaluation methods including automated metrics and LLM as judge frameworks rely on lexical faithfulness, often labeling any information not explicitly present in the transcript as hallucination.
We show that such approaches systematically misclassify clinically valid outputs as errors, inflating hallucination rates and distorting model assessment. Our analysis reveals that many flagged hallucinations correspond to legitimate clinical transformations, including synonym mapping, abstraction of examination findings, diagnostic inference, and guideline consistent care planning.
By aligning evaluation criteria with clinical reasoning through calibrated prompting and retrieval grounded in medical ontologies we observe a significant shift in outcomes. Under a lexical evaluation regime, the mean hallucination rate is 35%, heavily penalizing valid reasoning. With inference aware evaluation, this drops to 9%, with remaining cases reflecting genuine safety concerns. These findings suggest that current evaluation practices over penalize valid clinical reasoning and may measure artifacts of evaluation design rather than true errors, underscoring the need for clinically informed evaluation in high context domains like medicine.

---


### 143. [Improved Multiscale Structural Mapping with Supervertex Vision Transformer for the Detection of Alzheimer's Disease Neurodegeneration](https://arxiv.org/abs/2604.14837)

**<font color=#1a73e8>作者：</font>** Geonwoo Baek, David H. Salat, Ikbeom Jang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease (AD) confirmation often relies on positron emission tomography (PET) or cerebrospinal fluid (CSF) analysis, which are costly and invasive. Consequently, structural MRI biomarkers such as cortical thickness (CT) are widely used for non-invasive AD screening. Multiscale structural mapping (MSSM) was recently proposed to integrate gray-white matter contrasts (GWCs) with CT from a single T1-weighted MRI (T1w) scan. Building on this framework, we propose MSSM+, together with surface supervertex mapping (SSVM) and a Supervertex Vision Transformer (SV-ViT). 3D T1w images from individuals with AD and cognitively normal (CN) controls were analyzed. MSSM+ extends MSSM by incorporating sulcal depth and cortical curvature at the vertex level. SSVM partitions the cortical surface into supervertices (surface patches) that effectively represent inter- and intra-regional spatial relationships. SV-ViT is a Vision Transformer architecture operating on these supervertices, enabling anatomically informed learning from surface mesh representations. Compared with MSSM, MSSM+ identified more spatially extensive and statistically significant group differences between AD and CN. In AD vs. CN classification, MSSM+ achieved a 3%p higher area under the precision-recall curve than MSSM. Vendor-specific analyses further demonstrated reduced signal variability and consistently improved classification performance across MR manufacturers relative to CT, GWCs, and MSSM. These findings suggest that MSSM+ combined with SV-ViT is a promising MRI-based imaging marker for AD detection prior to CSF/PET confirmation.

---


### 144. [Efficient Search of Implantable Adaptive Cells for Medical Image Segmentation](https://arxiv.org/abs/2604.14849)

**<font color=#1a73e8>作者：</font>** Emil Benedykciuk, Marcin Denkowski, Grzegorz M. Wójcik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Adaptive skip modules can improve medical image segmentation, but searching for them is computationally costly. Implantable Adaptive Cells (IACs) are compact NAS modules inserted into U-Net skip connections, reducing the search space compared with full-network NAS. However, the original IAC framework still requires a 200-epoch differentiable search for each backbone and dataset. Methods: We analyzed the temporal behavior of operations and edges within IAC cells during differentiable search on public medical image segmentation benchmarks. We found that operations selected in the final discrete cell typically emerge among the strongest candidates early in training, and their architecture parameters stabilize well before the final epoch. Based on this, we propose a Jensen--Shannon-divergence-based stability criterion that tracks per-edge operation-importance distributions and progressively prunes low-importance operations during search. The accelerated framework is called IAC-LTH. Results: Across four public benchmarks (ACDC, BraTS, KiTS, AMOS), several 2-D U-Net backbones, and a 2-D nnU-Net pipeline, IAC-LTH discovers IAC cells whose patient-level segmentation performance matches and sometimes slightly exceeds that of cells found by the original full-length search, while reducing wall-clock NAS cost by 3.7x to 16x across datasets and backbones. These results are consistent across architectures, benchmarks, and both non-augmented and augmented training settings, while preserving the gains of IAC-equipped U-Nets over strong attention-based and dense-skip baselines. Conclusion: Competitive IAC architectures can be identified from early-stabilizing operations without running the full search, making adaptive skip-module design more practical for medical image segmentation under realistic computational constraints.

---


### 145. [ClimateCause: Complex and Implicit Causal Structures in Climate Reports](https://arxiv.org/abs/2604.14856)

**<font color=#1a73e8>作者：</font>** Liesbeth Allein, Nataly Pineda-Castañeda, Andrea Rocci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding climate change requires reasoning over complex causal networks. Yet, existing causal discovery datasets predominantly capture explicit, direct causal relations. We introduce ClimateCause, a manually expert-annotated dataset of higher-order causal structures from science-for-policy climate reports, including implicit and nested causality. Cause-effect expressions are normalized and disentangled into individual causal relations to facilitate graph construction, with unique annotations for cause-effect correlation, relation type, and spatiotemporal context. We further demonstrate ClimateCause's value for quantifying readability based on the semantic complexity of causal graphs underlying a statement. Finally, large language model benchmarking on correlation inference and causal chain reasoning highlights the latter as a key challenge.

---


### 146. [Benchmarks for Trajectory Safety Evaluation and Diagnosis in OpenClaw and Codex: ATBench-Claw and ATBench-CodeX](https://arxiv.org/abs/2604.14858)

**<font color=#1a73e8>作者：</font>** Zhonghao Yang, Yu Li, Yanxu Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agent systems move into increasingly diverse execution settings, trajectory-level safety evaluation and diagnosis require benchmarks that evolve with them. ATBench is a diverse and realistic agent trajectory benchmark for safety evaluation and diagnosis. This report presents ATBench-Claw and ATBench-CodeX, two domain-customized extensions that carry ATBench into the OpenClaw and OpenAI Codex / Codex-runtime settings. The key adaptation mechanism is to analyze each new setting, customize the three-dimensional Safety Taxonomy over risk source, failure mode, and real-world harm, and then use that customized taxonomy to define the benchmark specification consumed by the shared ATBench construction pipeline. This extensibility matters because agent frameworks remain relatively stable at the architectural level even as their concrete execution settings, tool ecosystems, and product capabilities evolve quickly. Concretely, ATBench-Claw targets OpenClaw-sensitive execution chains over tools, skills, sessions, and external actions, while ATBench-CodeX targets trajectories in the OpenAI Codex / Codex-runtime setting over repositories, shells, patches, dependencies, approvals, and runtime policy boundaries. Our emphasis therefore falls on taxonomy customization, domain-specific risk coverage, and benchmark design under a shared ATBench generation framework.

---


### 147. [Curvature-Aligned Probing for Local Loss-Landscape Stabilization](https://arxiv.org/abs/2604.14870)

**<font color=#1a73e8>作者：</font>** Nikita Kiselev, Andrey Grabovoy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local loss-landscape stabilization under sample growth is typically measured either pointwise or through isotropic averaging in the full parameter space. Despite practical value, both choices probe directions that contribute little to the dominant local deformation of strongly anisotropic neural landscapes. We recast stabilization as an observational problem and introduce a unified family of criteria parameterized by an aggregation order and a probing distribution; within this family we propose a curvature-aligned criterion $\Delta_2^{(D)}$ that probes the loss increment field in the top-$D$ eigenspace of the empirical Hessian near a trained solution. Solely from a local quadratic model, we prove that $\Delta_2^{(D)}$ preserves the $O(k^{-2})$ mean-squared rate of the full-space criterion while replacing ambient-dimension curvature dependence with dependence on the subspace dimension $D$; a corollary gives a closed-form spectral expression and a proposition identifies the top-$D$ eigenspace as extremal within the eigenspace-aligned family. We also derive scalable estimators based on Hessian-vector products, subspace Monte Carlo, and a closed-form Gaussian-moment proxy. On a decoder-only transformer, a curvature-aligned probe occupying a tiny fraction of parameter space already reproduces the full-space mean-squared signal to within numerical noise throughout the validated local regime, and the closed-form estimator is orders of magnitude faster than direct Monte Carlo after subspace construction.

---


### 148. [SkillDroid: Compile Once, Reuse Forever](https://arxiv.org/abs/2604.14872)

**<font color=#1a73e8>作者：</font>** Qijia Chen, Andrea Bellucci, Zhida Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM-based mobile GUI agents treat every task invocation as an independent reasoning episode, requiring a full LLM inference call at each action step. This per-step dependence makes them stateless: a task completed successfully yesterday is re-derived from scratch today, with no improvement in reliability or speed. We present SkillDroid, a three-layer skill agent that compiles successful LLM-guided GUI trajectories into parameterized skill templates (sequences of UI actions with weighted element locators and typed parameter slots) and replays them on future invocations without any LLM calls. A matching cascade (regex patterns, embedding similarity, and app filtering) routes incoming instructions to stored skills, while a failure-learning layer triggers recompilation when skill reliability degrades. Over a 150-round longitudinal evaluation with systematic instruction variation and controlled perturbations, SkillDroid achieves an 85.3% success rate (23 percentage points above a stateless LLM baseline) while using 49% fewer LLM calls. The skill replay mechanism achieves a perfect 1000% success rate across 79 replay rounds at 2.4 times the speed of full LLM execution. Most critically, the system improves with use: its success rate converges upward from 87% to 91%, while the baseline degrades from 80% to 44%.

---


### 149. [Open-Set Vein Biometric Recognition with Deep Metric Learning](https://arxiv.org/abs/2604.14874)

**<font color=#1a73e8>作者：</font>** Paweł Pilarek, Marcel Musiałek, Anna Górska  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most state-of-the-art vein recognition methods rely on closed-set classification, which inherently limits their scalability and prevents the adaptive enrollment of new users without complete model retraining. We rigorously evaluate the computational boundaries of Deep Metric Learning (DML) under strict open-set constraints. Unlike standard closed-set approaches, we analyze the impact of data scarcity and domain shift on recognition performance. Our approach learns discriminative L2-normalised embeddings and employs prototype-based matching with a calibrated similarity threshold to effectively distinguish between enrolled users and unseen impostors. We evaluate the framework under a strict subject-disjoint protocol across four diverse datasets covering finger, wrist, and dorsal hand veins (MMCBNU 6000, UTFVP, FYO, and a dorsal hand-vein dataset). On the large-scale MMCBNU 6000 benchmark, our best model (ResNet50-CBAM) achieves an OSCR of 0.9945, AUROC of 0.9974, and EER of 1.57%, maintaining high identification accuracy (99.6% Rank-1) while robustly rejecting unknown subjects. Cross-dataset experiments evaluate the framework's generalisation across different acquisition setups, confirming that while the model handles large-scale data robustly, performance remains sensitive to domain shifts in low-data regimes. Ablation studies demonstrate that triplet-based objectives combined with a simple 1-NN classifier offer an optimal trade-off between accuracy and efficiency, enabling real-time deployment on commodity hardware.

---


### 150. [SOLIS: Physics-Informed Learning of Interpretable Neural Surrogates for Nonlinear Systems](https://arxiv.org/abs/2604.14879)

**<font color=#1a73e8>作者：</font>** Murat Furkan Mansur, Tufan Kumbasar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonlinear system identification must balance physical interpretability with model flexibility. Classical methods yield structured, control-relevant models but rely on rigid parametric forms that often miss complex nonlinearities, whereas Neural ODEs are expressive yet largely black-box. Physics-Informed Neural Networks (PINNs) sit between these extremes, but inverse PINNs typically assume a known governing equation with fixed coefficients, leading to identifiability failures when the true dynamics are unknown or state-dependent. We propose \textbf{SOLIS}, which models unknown dynamics via a \emph{state-conditioned second-order surrogate model} and recasts identification as learning a Quasi-Linear Parameter-Varying (Quasi-LPV) representation, recovering interpretable natural frequency, damping, and gain without presupposing a global equation. SOLIS decouples trajectory reconstruction from parameter estimation and stabilizes training with a cyclic curriculum and \textbf{Local Physics Hints} windowed ridge-regression anchors that mitigate optimization collapse. Experiments on benchmarks show accurate parameter-manifold recovery and coherent physical rollouts from sparse data, including regimes where standard inverse methods fail.

---


### 151. [xFODE+: Explainable Type-2 Fuzzy Additive ODEs for Uncertainty Quantification](https://arxiv.org/abs/2604.14880)

**<font color=#1a73e8>作者：</font>** Ertugrul Kececi, Tufan Kumbasar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Deep Learning (DL) have boosted data-driven System Identification (SysID), but reliable use requires Uncertainty Quantification (UQ) alongside accurate predictions. Although UQ-capable models such as Fuzzy ODE (FODE) can produce Prediction Intervals (PIs), they offer limited interpretability. We introduce Explainable Type-2 Fuzzy Additive ODEs for UQ (xFODE+), an interpretable SysID model which produces PIs alongside point predictions while retaining physically meaningful incremental states. xFODE+ implements each fuzzy additive model with Interval Type-2 Fuzzy Logic Systems (IT2-FLSs) and constraints membership functions to the activation of two neighboring rules, limiting overlap and keeping inference locally transparent. The type-reduced sets produced by the IT2-FLSs are aggregated to construct the state update together with the PIs. The model is trained in a DL framework via a composite loss that jointly optimizes prediction accuracy and PI quality. Results on benchmark SysID datasets show that xFODE+ matches FODE in PI quality and achieves comparable accuracy, while providing interpretability.

---


### 152. [The Missing Knowledge Layer in AI: A Framework for Stable Human-AI Reasoning](https://arxiv.org/abs/2604.14881)

**<font color=#1a73e8>作者：</font>** Rikard Rosenbacke, Carl Rosenbacke, Victor Rosenbacke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly integrated into decision-making in areas such as healthcare, law, finance, engineering, and government. Yet they share a critical limitation: they produce fluent outputs even when their internal reasoning has drifted. A confident answer can conceal uncertainty, speculation, or inconsistency, and small changes in phrasing can lead to different conclusions. This makes LLMs useful assistants but unreliable partners in high-stakes contexts.
Humans exhibit a similar weakness, often mistaking fluency for reliability. When a model responds smoothly, users tend to trust it, even when both model and user are drifting together. This paper is the first in a five-paper research series on stabilising human-AI reasoning. The series proposes a two-layer approach: Parts II-IV introduce human-side mechanisms such as uncertainty cues, conflict surfacing, and auditable reasoning traces, while Part V develops a model-side Epistemic Control Loop (ECL) that detects instability and modulates generation accordingly.
Together, these layers form a missing operational substrate for governance by increasing signal-to-noise at the point of use. Stabilising interaction makes uncertainty and drift visible before enforcement is applied, enabling more precise capability governance. This aligns with emerging compliance expectations, including the EU AI Act and ISO/IEC 42001, by making reasoning processes traceable under real conditions of use.
The central claim is that fluency is not reliability. Without structures that stabilise both human and model reasoning, AI cannot be trusted or governed where it matters most.

---


### 153. [xFODE: An Explainable Fuzzy Additive ODE Framework for System Identification](https://arxiv.org/abs/2604.14883)

**<font color=#1a73e8>作者：</font>** Ertugrul Kececi, Tufan Kumbasar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Deep Learning (DL) have strengthened data-driven System Identification (SysID), with Neural and Fuzzy Ordinary Differential Equation (NODE/FODE) models achieving high accuracy in nonlinear dynamic modeling. Yet, system states in these frameworks are often reconstructed without clear physical meaning, and input contributions to the state derivatives remain difficult to interpret. To address these limitations, we propose Explainable FODE (xFODE), an interpretable SysID framework with integrated DL-based training. In xFODE, we define states in an incremental form to provide them with physical meanings. We employ fuzzy additive models to approximate the state derivative, thereby enhancing interpretability per input. To provide further interpretability, Partitioning Strategies (PSs) are developed, enabling the training of fuzzy additive models with explainability. By structuring the antecedent space during training so that only two consecutive rules are activated for any given input, PSs not only yield lower complexity for local inference but also enhance the interpretability of the antecedent space. To train xFODE, we present a DL framework with parameterized membership function learning that supports end-to-end optimization. Across benchmark SysID datasets, xFODE matches the accuracy of NODE, FODE, and NLARX models while providing interpretable insights.

---


### 154. [FSDETR: Frequency-Spatial Feature Enhancement for Small Object Detection](https://arxiv.org/abs/2604.14884)

**<font color=#1a73e8>作者：</font>** Jianchao Huang, Fengming Zhang, Haibo Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small object detection remains a significant challenge due to feature degradation from downsampling, mutual occlusion in dense clusters, and complex background interference. To address these issues, this paper proposes FSDETR, a frequency-spatial feature enhancement framework built upon the RT-DETR baseline. By establishing a collaborative modeling mechanism, the method effectively leverages complementary structural information. Specifically, a Spatial Hierarchical Attention Block (SHAB) captures both local details and global dependencies to strengthen semantic representation. Furthermore, to mitigate occlusion in dense scenes, the Deformable Attention-based Intra-scale Feature Interaction (DA-AIFI) focuses on informative regions via dynamic sampling. Finally, the Frequency-Spatial Feature Pyramid Network (FSFPN) integrates frequency filtering with spatial edge extraction via the Cross-domain Frequency-Spatial Block (CFSB) to preserve fine-grained details. Experimental results show that with only 14.7M parameters, FSDETR achieves 13.9% APS on VisDrone 2019 and 48.95% AP50 tiny on TinyPerson, showing strong performance on small-object benchmarks. The code and models are available at this https URL.

---


### 155. [RACER: Retrieval-Augmented Contextual Rapid Speculative Decoding](https://arxiv.org/abs/2604.14885)

**<font color=#1a73e8>作者：</font>** Zihong Zhang, Zuchao Li, Lefei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive decoding in Large Language Models (LLMs) generates one token per step, causing high inference latency. Speculative decoding (SD) mitigates this through a guess-and-verify strategy, but existing training-free variants face trade-offs: retrieval-based drafts break when no exact match exists, while logits-based drafts lack structural guidance. We propose $\textbf{RACER}$ ($\textbf{R}$etrieval-$\textbf{A}$ugmented $\textbf{C}$ont$\textbf{e}$xtual $\textbf{R}$apid Speculative Decoding), a lightweight and training-free method that integrates retrieved exact patterns with logit-driven future cues. This unification supplies both reliable anchors and flexible extrapolation, yielding richer speculative drafts. Experiments on Spec-Bench, HumanEval, and MGSM-ZH demonstrate that RACER consistently accelerates inference, achieving more than $2\times$ speedup over autoregressive decoding, and outperforms prior training-free methods, offering a scalable, plug-and-play solution for efficient LLM decoding. Our source code is available at $\href{this https URL}{this https URL}$.

---


### 156. [Cooperate to Compete: Strategic Data Generation and Incentivization Framework for Coopetitive Cross-Silo Federated Learning](https://arxiv.org/abs/2604.14886)

**<font color=#1a73e8>作者：</font>** Thanh Linh Nguyen, Nguyen Van Huynh, Quoc-Viet Pham  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In data-sensitive domains such as healthcare, cross-silo federated learning (CFL) allows organizations to collaboratively train AI models without sharing raw data. However, practical CFL deployments are inherently coopetitive, in which organizations cooperate during model training while competing in downstream markets. In such settings, training contributions, including data volume, quality, and diversity, can improve the global model yet inadvertently strengthen rivals. This dilemma is amplified by non-IID data, which leads to asymmetric learning gains and undermines sustained participation. While existing competition-aware CFL and incentive-design approaches reward organizations based on marginal training contributions, they fail to account for the costs of strengthening competitors. In this paper, we introduce CoCoGen+, a coopetition-compatible data generation and incentivization framework that jointly models non-IID data and inter-organizational competition while endogenizing GenAI-based synthetic data generation as a strategic decision. Specifically, CoCoGen+ formulates each training round as a weighted potential game, where organizations strategically decide how much synthetic data to generate by balancing learning performance gains against computational costs and competition-caused utility losses. We then provide a tractable equilibrium characterization and derive implementable generation strategies to maximize social welfare. To promote long-term collaboration, we integrate a payoff redistribution-based incentive mechanism to compensate organizations for their contributions and competition-caused utility degradation. Experiments on varying learning tasks validate the feasibility of CoCoGen+. The results show how non-IID data, competition intensity, and incentives shape organizational strategies and social welfare, while CoCoGen+ outperforms baselines in efficiency.

---


### 157. [MemoSight: Unifying Context Compression and Multi Token Prediction for Reasoning Acceleration](https://arxiv.org/abs/2604.14889)

**<font color=#1a73e8>作者：</font>** Xinyu Liu, Xin Liu, Bo Jin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Chain-of-thought (CoT) reasoning enables LLMs to solve challenging reasoning problems, as KV cache grows linearly with the number of generated tokens, CoT reasoning faces scaling issues in terms of speed and memory usage. In this work, we propose MemoSight (Memory-Foresight-based reasoning), a unified framework that integrates both context compression and multi-token prediction to mitigate the efficiency issues while maintaining CoT reasoning performance. Our framework adopts the same minimalist design for both context compression and multi-token prediction via special tokens and their corresponding position layout tailored to each token type. Comprehensive experiments on four reasoning benchmarks demonstrate that MemoSight reduces the KV cache footprint by up to 66% and accelerates inference by 1.56x, while outperforming existing CoT compression methods.

---


### 158. [Governing Reflective Human-AI Collaboration: A Framework for Epistemic Scaffolding and Traceable Reasoning](https://arxiv.org/abs/2604.14898)

**<font color=#1a73e8>作者：</font>** Rikard Rosenbacke, Carl Rosenbacke, Victor Rosenbacke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have advanced rapidly, from pattern recognition to emerging forms of reasoning, yet they remain confined to linguistic simulation rather than grounded understanding. They can produce fluent outputs that resemble reflection, but lack temporal continuity, causal feedback, and anchoring in real-world interaction. This paper proposes a complementary approach in which reasoning is treated as a relational process distributed between human and model rather than an internal capability of either.
Building on recent work on "System-2" learning, we relocate reflective reasoning to the interaction layer. Instead of engineering reasoning solely within models, we frame it as a cognitive protocol that can be structured, measured, and governed using existing systems. This perspective emphasizes collaborative intelligence, combining human judgment and contextual understanding with machine speed, memory, and associative capacity.
We introduce "The Architect's Pen" as a practical method. Like an architect who thinks through drawing, the human uses the model as an external medium for structured reflection. By embedding phases of articulation, critique, and revision into human-AI interaction, the dialogue itself becomes a reasoning loop: human abstraction -> model articulation -> human reflection.
This reframes the question from whether the model can think to whether the human-AI system can reason. The framework enables auditable reasoning traces and supports alignment with emerging governance standards, including the EU AI Act and ISO/IEC 42001. It provides a practical path toward more transparent, controllable, and accountable AI use without requiring new model architectures.

---


### 159. [Comparison of Modern Multilingual Text Embedding Techniques for Hate Speech Detection Task](https://arxiv.org/abs/2604.14907)

**<font color=#1a73e8>作者：</font>** Evaldas Vaiciukynas, Paulius Danenas, Linas Ablonskis 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online hate speech and abusive language pose a growing challenge for content moderation, especially in multilingual settings and for low-resource languages such as Lithuanian. This paper investigates to what extent modern multilingual sentence embedding models can support accurate hate speech detection in Lithuanian, Russian, and English, and how their performance depends on downstream modeling choices and feature dimensionality. We introduce LtHate, a new Lithuanian hate speech corpus derived from news portals and social networks, and benchmark six modern multilingual encoders (potion, gemma, bge, snow, jina, e5) on LtHate, RuToxic, and EnSuperset using a unified Python pipeline. For each embedding, we train both a one class HBOS anomaly detector and a two class CatBoost classifier, with and without principal component analysis (PCA) compression to 64-dimensional feature vectors. Across all datasets, two class supervised models consistently and substantially outperform one class anomaly detection, with the best configurations achieving up to 80.96% accuracy and AUC ROC of 0.887 in Lithuanian (jina), 92.19% accuracy and AUC ROC of 0.978 in Russian (e5), and 77.21% accuracy and AUC ROC of 0.859 in English (e5 with PCA). PCA compression preserves almost all discriminative power in the supervised setting, while showing some negative impact for the unsupervised anomaly detection case. These results demonstrate how modern multilingual sentence embeddings combined with gradient boosted decision trees provide robust soft-computing solutions for multilingual hate speech detection applications.

---


### 160. [Multi-User mmWave Beam and Rate Adaptation via Combinatorial Satisficing Bandits](https://arxiv.org/abs/2604.14908)

**<font color=#1a73e8>作者：</font>** Emre Özyıldırım, Barış Yaycı, Umut Eren Akturk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study downlink beam and rate adaptation in a multi-user mmWave MISO system where multiple base stations (BSs), each using analog beamforming from finite codebooks, serve multiple single-antenna user equipments (UEs) with a unique beam per UE and discrete data transmission rates. BSs learn about transmission success based on ACK/NACK feedback. To encode service goals, we introduce a satisficing throughput threshold $\tau_r$ and cast joint beam and rate adaptation as a combinatorial semi-bandit over beam-rate tuples. Within this framework, we propose SAT-CTS, a lightweight, threshold-aware policy that blends conservative confidence estimates with posterior sampling, steering learning toward meeting $\tau_r$ rather than merely maximizing. Our main theoretical contribution provides the first finite-time regret bounds for combinatorial semi-bandits with satisficing objective: when $\tau_r$ is realizable, we upper bound the cumulative satisficing regret to the target with a time-independent constant, and when $\tau_r$ is non-realizable, we show that SAT-CTS incurs only a finite expected transient outside committed CTS rounds, after which its regret is governed by the sum of the regret contributions of restarted CTS rounds, yielding an $O((\log T)^2)$ standard regret bound. On the practical side, we evaluate the performance via cumulative satisficing regret to $\tau_r$ alongside standard regret and fairness. Experiments with time-varying sparse multipath channels show that SAT-CTS consistently reduces satisficing regret and maintains competitive standard regret, while achieving favorable average throughput and fairness across users, indicating that feedback-efficient learning can equitably allocate beams and rates to meet QoS targets without channel state knowledge.

---


### 161. [Efficient Fuzzy Private Set Intersection from Secret-shared OPRF](https://arxiv.org/abs/2604.14909)

**<font color=#1a73e8>作者：</font>** Xinpeng Yang, Meng Hao, Chenkai Weng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Private set intersection (PSI) enables a sender holding a set $Q$ of size $m$ and a receiver holding a set $W$ of size $n$ to securely compute the intersection $Q \cap W$. Fuzzy PSI (FPSI) is a PSI variant where the receiver learns the items $q \in Q$ for which there exists some $w \in W$ satisfying $\mathsf{dist}(q, w) \le \delta$ under a given distance metric. Although several FPSI works are proposed for $L_{p}$ distance metrics with $p \in [1, \infty]$, they either heavily rely on expensive homomorphic encryptions, or incur undesirable complexity, e.g., exponential to the element dimension, both of which lead to poor practical efficiency.
In this work, we propose efficient FPSI protocols for $L_{p \in [1, \infty]}$ distance metrics, primarily leveraging significantly cheaper symmetric-key operations. Our protocols achieve linear communication and computation complexity in the set sizes $m,n$, the dimension $d$, and the distance threshold $\delta$. Our core building block is an oblivious programmable PRF with secret-shared outputs, which may be of independent interest. Furthermore, we incorporate a prefix technique that reduces the dependence on the distance threshold $\delta$ to logarithmic, which is particularly suitable for large $\delta$.
We implement our FPSI protocols and compare them with state-of-the-art constructions. Experimental results demonstrate that our protocols consistently and significantly outperform existing works across all settings. Specifically, our protocols achieve a speedup of $12{\sim}145\times$ in running time and a reduction of $3{\sim}8\times$ in communication cost compared to Gao et al.~(ASIACRYPT'24) and a speedup of $9{\sim}80\times$ in running time and a reduction of $5{\sim}19\times$ in communication cost compared to Dang et al.~(CCS'25).

---


### 162. [Reward-Aware Trajectory Shaping for Few-step Visual Generation](https://arxiv.org/abs/2604.14910)

**<font color=#1a73e8>作者：</font>** Rui Li, Bingyu Li, Yuanzhi Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving high-fidelity generation in extremely few sampling steps has long been a central goal of generative modeling. Existing approaches largely rely on distillation-based frameworks to compress the original multi-step denoising process into a few-step generator. However, such methods inherently constrain the student to imitate a stronger multi-step teacher, imposing the teacher as an upper bound on student performance. We argue that introducing \textbf{preference alignment awareness} enables the student to optimize toward reward-preferred generation quality, potentially surpassing the teacher instead of being restricted to rigid teacher imitation. To this end, we propose \textbf{Reward-Aware Trajectory Shaping (RATS)}, a lightweight framework for preference-aligned few-step generation. Specifically, teacher and student latent trajectories are aligned at key denoising stages through horizon matching, while a \textbf{reward-aware gate} is introduced to adaptively regulate teacher guidance based on their relative reward performance. Trajectory shaping is strengthened when the teacher achieves higher rewards, and relaxed when the student matches or surpasses the teacher, thereby enabling continued reward-driven improvement. By seamlessly integrating trajectory distillation, reward-aware gating, and preference alignment, RATS effectively transfers preference-relevant knowledge from high-step generators without incurring additional test-time computational overhead. Experimental results demonstrate that RATS substantially improves the efficiency--quality trade-off in few-step visual generation, significantly narrowing the gap between few-step students and stronger multi-step generators.

---


### 163. [Beyond Prompts: Unconditional 3D Inversion for Out-of-Distribution Shapes](https://arxiv.org/abs/2604.14914)

**<font color=#1a73e8>作者：</font>** Victoria Yue Chen, Emery Pierson, Léopold Maillard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven inversion of generative models is a core paradigm for manipulating 2D or 3D content, unlocking numerous applications such as text-based editing, style transfer, or inverse problems. However, it relies on the assumption that generative models remain sensitive to natural language prompts. We demonstrate that for state-of-the-art native text-to-3D generative models, this assumption often collapses. We identify a critical failure mode where generation trajectories are drawn into latent ``sink traps'': regions where the model becomes insensitive to prompt modifications. In these regimes, changes to the input text fail to alter internal representations in a way that alters the output geometry. Crucially, we observe that this is not a limitation of the model's \textit{geometric} expressivity; the same generative models possess the ability to produce a vast diversity of shapes but, as we demonstrate, become insensitive to out-of-distribution \textit{text} guidance. We investigate this behavior by analyzing the sampling trajectories of the generative model, and find that complex geometries can still be represented and produced by leveraging the model's unconditional generative prior. This leads to a more robust framework for text-based 3D shape editing that bypasses latent sinks by decoupling a model's geometric representation power from its linguistic sensitivity. Our approach addresses the limitations of current 3D pipelines and enables high-fidelity semantic manipulation of out-of-distribution 3D shapes. Project webpage: this https URL

---


### 164. [Dual-Axis Generative Reward Model Toward Semantic and Turn-taking Robustness in Interactive Spoken Dialogue Models](https://arxiv.org/abs/2604.14920)

**<font color=#1a73e8>作者：</font>** Yifu Chen, Shengpeng Ji, Zhengqing Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Achieving seamless, human-like interaction remains a key challenge for full-duplex spoken dialogue models (SDMs). Reinforcement learning (RL) has substantially enhanced text- and vision-language models, while well-designed reward signals are crucial for the performance of RL. We consider RL a promising strategy to address the key challenge for SDMs. However, a fundamental barrier persists: prevailing automated metrics for assessing interaction quality rely on superficial proxies, such as behavioral statistics or timing-prediction accuracy, failing to provide reliable reward signals for RL. On the other hand, human evaluations, despite their richness, remain costly, inconsistent, and difficult to scale. We tackle this critical barrier by proposing a Dual-Axis Generative Reward Model, which is trained to understand complex interaction dynamics using a detailed taxonomy and an annotated dataset, produces a single score and, crucially, provides separate evaluations for semantic quality and interaction timing. Such dual outputs furnish precise diagnostic feedback for SDMs and deliver a dependable, instructive reward signal suitable for online reinforcement learning. Our model achieves state-of-the-art performance on interaction-quality assessment across a wide spectrum of datasets, spanning synthetic dialogues and complex real-world interactions.

---


### 165. [LongAct: Harnessing Intrinsic Activation Patterns for Long-Context Reinforcement Learning](https://arxiv.org/abs/2604.14922)

**<font color=#1a73e8>作者：</font>** Bowen Ping, Zijun Chen, Tingfeng Hui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has emerged as a critical driver for enhancing the reasoning capabilities of Large Language Models (LLMs). While recent advancements have focused on reward engineering or data synthesis, few studies exploit the model's intrinsic representation characteristics to guide the training process. In this paper, we first observe the presence of high-magnitude activations within the query and key vectors when processing long contexts. Drawing inspiration from model quantization -- which establishes the criticality of such high-magnitude activations -- and the insight that long-context reasoning inherently exhibits a sparse structure, we hypothesize that these weights serve as the pivotal drivers for effective model optimization. Based on this insight, we propose LongAct, a strategy that shifts from uniform to saliency-guided sparse updates. By selectively updating only the weights associated with these significant activations, LongAct achieves an approximate 8% improvement on LongBench v2 and enhances generalization on the RULER benchmark. Furthermore, our method exhibits remarkable universality, consistently boosting performance across diverse RL algorithms such as GRPO and DAPO. Extensive ablation studies suggest that focusing on these salient features is key to unlocking long-context potential.

---


### 166. [Improving Sparse Autoencoder with Dynamic Attention](https://arxiv.org/abs/2604.14925)

**<font color=#1a73e8>作者：</font>** Dongsheng Wang, Jinsen Zhang, Dawei Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, sparse autoencoders (SAEs) have emerged as a promising technique for interpreting activations in foundation models by disentangling features into a sparse set of concepts. However, identifying the optimal level of sparsity for each neuron remains challenging in practice: excessive sparsity can lead to poor reconstruction, whereas insufficient sparsity may harm interpretability. While existing activation functions such as ReLU and TopK provide certain sparsity guarantees, they typically require additional sparsity regularization or cherry-picked hyperparameters. We show in this paper that dynamically sparse attention mechanisms using sparsemax can bridge this trade-off, due to their ability to determine the activation numbers in a data-dependent manner. Specifically, we first explore a new class of SAEs based on the cross-attention architecture with the latent features as queries and the learnable dictionary as the key and value matrices. To encourage sparse pattern learning, we employ a sparsemax-based attention strategy that automatically infers a sparse set of elements according to the complexity of each neuron, resulting in a more flexible and general activation function. Through comprehensive evaluation and visualization, we show that our approach successfully achieves lower reconstruction loss while producing high-quality concepts, particularly in top-n classification tasks.

---


### 167. [Hybrid Latents -- Geometry-Appearance-Aware Surfel Splatting](https://arxiv.org/abs/2604.14928)

**<font color=#1a73e8>作者：</font>** Neel Kelkar, Simon Niedermayr, Klaus Engel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a hybrid Gaussian-hash-grid radiance representation for reconstructing 2D Gaussian scene models from multi-view images. Similar to NeST splatting, our approach reduces the entanglement between geometry and appearance common in NeRF-based models, but adds per-Gaussian latent features alongside hash-grid features to bias the optimizer toward a separation of low- and high-frequency scene components. This explicit frequency-based decomposition reduces the tendency of high-frequency texture to compensate for geometric errors. Encouraging Gaussians with hard opacity falloffs further strengthens the separation between geometry and appearance, improving both geometry reconstruction and rendering efficiency. Finally, probabilistic pruning combined with a sparsity-inducing BCE opacity loss allows redundant Gaussians to be turned off, yielding a minimal set of Gaussians sufficient to represent the scene. Using both synthetic and real-world datasets, we compare against the state of the art in Gaussian-based novel-view synthesis and demonstrate superior reconstruction fidelity with an order of magnitude fewer primitives.

---


### 168. [Generative Data Augmentation for Skeleton Action Recognition](https://arxiv.org/abs/2604.14933)

**<font color=#1a73e8>作者：</font>** Xu Dong, Wanqing Li, Anthony Adeyemi-Ejeye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based human action recognition is a powerful approach for understanding human behaviour from pose data, but collecting large-scale, diverse, and well-annotated 3D skeleton datasets is both expensive and labor-intensive. To address this challenge, we propose a conditional generative pipeline for data augmentation in skeleton action recognition. Our method learns the distribution of real skeleton sequences under the constraint of action labels, enabling the synthesis of diverse and high-fidelity data. Even with limited training samples, it can effectively generate skeleton sequences and achieve competitive recognition performance in low-data scenarios, demonstrating strong generalisation in downstream tasks. Specifically, we introduce a Transformer-based encoder-decoder architecture, combined with a generative refinement module and a dropout mechanism, to balance fidelity and diversity during sampling. Experiments on HumanAct12 and the refined NTU-RGBD (NTU-VIBE) dataset show that our approach consistently improves the accuracy of multiple skeleton-based action recognition models, validating its effectiveness in both few-shot and full-data settings. The source code can be found at here.

---


### 169. [XQ-MEval: A Dataset with Cross-lingual Parallel Quality for Benchmarking Translation Metrics](https://arxiv.org/abs/2604.14934)

**<font color=#1a73e8>作者：</font>** Jingxuan Liu, Zhi Qu, Jin Tei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic evaluation metrics are essential for building multilingual translation systems. The common practice of evaluating these systems is averaging metric scores across languages, yet this is suspicious since metrics may suffer from cross-lingual scoring bias, where translations of equal quality receive different scores across languages. This problem has not been systematically studied because no benchmark exists that provides parallel-quality instances across languages, and expert annotation is not realistic. In this work, we propose XQ-MEval, a semi-automatically built dataset covering nine translation directions, to benchmark translation metrics. Specifically, we inject MQM-defined errors into gold translations automatically, filter them by native speakers for reliability, and merge errors to generate pseudo translations with controllable quality. These pseudo translations are then paired with corresponding sources and references to form triplets used in assessing the qualities of translation metrics. Using XQ-MEval, our experiments on nine representative metrics reveal the inconsistency between averaging and human judgment and provide the first empirical evidence of cross-lingual scoring bias. Finally, we propose a normalization strategy derived from XQ-MEval that aligns score distributions across languages, improving the fairness and reliability of multilingual metric evaluation.

---


### 170. [Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953)

**<font color=#1a73e8>作者：</font>** Hassan Ali, Doreen Jirak, Luca Müller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gesture recognition research, unlike NLP, continues to face acute data scarcity, with progress constrained by the need for costly human recordings or image processing approaches that cannot generate authentic variability in the gestures themselves. Recent advancements in image-to-video foundation models have enabled the generation of photorealistic, semantically rich videos guided by natural language. These capabilities open up new possibilities for creating effort-free synthetic data, raising the critical question of whether video Generative AI models can augment and complement traditional human-generated gesture data. In this paper, we introduce and analyze prompt-based video generation to construct a realistic deictic gestures dataset and rigorously evaluate its effectiveness for downstream tasks. We propose a data generation pipeline that produces deictic gestures from a small number of reference samples collected from human participants, providing an accessible approach that can be leveraged both within and beyond the machine learning community. Our results demonstrate that the synthetic gestures not only align closely with real ones in terms of visual fidelity but also introduce meaningful variability and novelty that enrich the original data, further supported by superior performance of various deep models using a mixed dataset. These findings highlight that image-to-video techniques, even in their early stages, offer a powerful zero-shot approach to gesture synthesis with clear benefits for downstream tasks.

---


### 171. [FedGUI: Benchmarking Federated GUI Agents across Heterogeneous Platforms, Devices, and Operating Systems](https://arxiv.org/abs/2604.14956)

**<font color=#1a73e8>作者：</font>** Wenhao Wang, Haoting Shi, Mengying Yuan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Training GUI agents with traditional centralized methods faces significant cost and scalability challenges. Federated learning (FL) offers a promising solution, yet its potential is hindered by the lack of benchmarks that capture real-world, cross-platform heterogeneity. To bridge this gap, we introduce FedGUI, the first comprehensive benchmark for developing and evaluating federated GUI agents across mobile, web, and desktop platforms. FedGUI provides a suite of six curated datasets to systematically study four crucial types of heterogeneity: cross-platform, cross-device, cross-OS, and cross-source. Extensive experiments reveal several key insights: First, we show that cross-platform collaboration improves performance, extending prior mobile-only federated learning to diverse GUI environments; Second, we demonstrate the presence of distinct heterogeneity dimensions and identify platform and OS as the most influential factors. FedGUI provides a vital foundation for the community to build more scalable and privacy-preserving GUI agents for real-world deployment. Our code and data are publicly available at this https URL..

---


### 172. [Frequency-Enhanced Dual-Subspace Networks for Few-Shot Fine-Grained Image Classification](https://arxiv.org/abs/2604.14958)

**<font color=#1a73e8>作者：</font>** Meijia Wang, Guochao Wang, Haozhen Chu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot fine-grained image classification aims to recognize subcategories with high visual similarity using only a limited number of annotated samples. Existing metric learning-based methods typically rely solely on spatial domain features. Confined to this single perspective, models inevitably suffer from inherent texture biases, entangling essential structural details with high-frequency background noise. Furthermore, lacking cross-view geometric constraints, single-view metrics tend to overfit this noise, resulting in structural instability under few-shot conditions. To address these issues, this paper proposes the Frequency-Enhanced Dual-Subspace Network (FEDSNet). Specifically, FEDSNet utilizes the Discrete Cosine Transform (DCT) and a low-pass filtering mechanism to explicitly isolate low-frequency global structural components from spatial features, thereby suppressing background interference. Truncated Singular Value Decomposition (SVD) is employed to construct independent, low-rank linear subspaces for both spatial texture and frequency structural features. An adaptive gating mechanism is designed to dynamically fuse the projection distances from these dual views. This strategy leverages the structural stability of the frequency subspace to prevent the spatial subspace from overfitting to background features. Extensive experiments on four benchmark datasets - CUB-200-2011, Stanford Cars, Stanford Dogs, and FGVC-Aircraft - demonstrate that FEDSNet exhibits excellent classification performance and robustness, achieving highly competitive results compared to existing metric learning algorithms. Complexity analysis further confirms that the proposed network achieves a favorable balance between high accuracy and computational efficiency, providing an effective new paradigm for few-shot fine-grained visual recognition.

---


### 173. [Blazing the trails before beating the path: Sample-efficient Monte-Carlo planning](https://arxiv.org/abs/2604.14974)

**<font color=#1a73e8>作者：</font>** Jean-Bastien Grill, Michal Valko, Rémi Munos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> You are a robot and you live in a Markov decision process (MDP) with a finite or an infinite number of transitions from state-action to next states. You got brains and so you plan before you act. Luckily, your roboparents equipped you with a generative model to do some Monte-Carlo planning. The world is waiting for you and you have no time to waste. You want your planning to be efficient. Sample-efficient. Indeed, you want to exploit the possible structure of the MDP by exploring only a subset of states reachable by following near-optimal policies. You want guarantees on sample complexity that depend on a measure of the quantity of near-optimal states. You want something, that is an extension of Monte-Carlo sampling (for estimating an expectation) to problems that alternate maximization (over actions) and expectation (over next states). But you do not want to StOP with exponential running time, you want something simple to implement and computationally efficient. You want it all and you want it now. You want TrailBlazer.

---


### 174. [Hybrid Decision Making via Conformal VLM-generated Guidance](https://arxiv.org/abs/2604.14980)

**<font color=#1a73e8>作者：</font>** Debodeep Banerjee, Burcu Sayin, Stefano Teso 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building on recent advances in AI, hybrid decision making (HDM) holds the promise of improving human decision quality and reducing cognitive load. We work in the context of learning to guide (LtG), a recently proposed HDM framework in which the human is always responsible for the final decision: rather than suggesting decisions, in LtG the AI supplies (textual) guidance useful for facilitating decision making. One limiting factor of existing approaches is that their guidance compounds information about all possible outcomes, and as a result it can be difficult to digest. We address this issue by introducing ConfGuide, a novel LtG approach that generates more succinct and targeted guidance. To this end, it employs conformal risk control to select a set of outcomes, ensuring a cap on the false negative rate. We demonstrate our approach on a real-world multi-label medical diagnosis task. Our empirical evaluation highlights the promise of ConfGuide.

---


### 175. [AI-Enabled Covert Channel Detection in RF Receiver Architectures](https://arxiv.org/abs/2604.14987)

**<font color=#1a73e8>作者：</font>** Abdelrahman Emad Abdelazim, Alan Rodrigo Diaz-Rizo, Hassan Aboushady 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Covert channels (CCs) in wireless chips pose a serious security threat, as they enable the exfiltration of sensitive information from the chip to an external attacker. In this work, we propose an AI-based defense mechanism deployed at the RF receiver, where the model directly monitors raw I/Q samples to detect, in real time, the presence of a CC embedded within an otherwise nominal signal. We first compact a state-of-the-art convolutional neural network (CNN), achieving an 80% reduction in parameters, which is an essential requirement for efficient edge deployment. When evaluated on the open-source hardware Trojan (HT)-based CC dataset, the compacted CNN attains an average accuracy of 90.28% for CC detection and 86.50% for identifying the underlying HT, with results averaged across SNR values above 1 dB. For practical communication scenarios where SNR > 20 dB, the model achieves over 97% accuracy for both tasks. These results correspond to a minimal performance degradation of less than 2% compared to the baseline model. The compacted CNN is further benchmarked against alternative classifiers, demonstrating an excellent accuracy-model size trade-off. Finally, we design a lightweight CNN hardware accelerator and demonstrate it on an FPGA, achieving very low resource utilization and an efficiency of 107 GOPs/W. Being the first AI hardware accelerator proposed specifically for CC detection, we compare it against state-of-the-art AI accelerators for RF signal classification tasks such as modulation recognition, showing superior performance.

---


### 176. [ConGISATA: A Framework for Continuous Gamified Information Security Awareness Training and Assessment](https://arxiv.org/abs/2604.14996)

**<font color=#1a73e8>作者：</font>** Ofir Cohen, Ron Bitton, Asaf Shabtai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The incidence of cybersecurity attacks utilizing social engineering techniques has increased. Such attacks exploit the fact that in every secure system, there is at least one individual with the means to access sensitive information. Since it is easier to deceive a person than it is to bypass the defense mechanisms in place, these types of attacks have gained popularity. This situation is exacerbated by the fact that people are more likely to take risks in their passive form, i.e., risks that arise due to the failure to perform an action. Passive risk has been identified as a significant threat to cybersecurity. To address these threats, there is a need to strengthen individuals' information security awareness (ISA). Therefore, we developed ConGISATA - a continuous gamified ISA training and assessment framework based on embedded mobile sensors; a taxonomy for evaluating mobile users' security awareness served as the basis for the sensors' design. ConGISATA's continuous and gradual training process enables users to learn from their real-life mistakes and adapt their behavior accordingly. ConGISATA aims to transform passive risk situations (as perceived by an individual) into active risk situations, as people tend to underestimate the potential impact of passive risks. Our evaluation of the proposed framework demonstrates its ability to improve individuals' ISA, as assessed by the sensors and in simulations of common attack vectors.

---


### 177. [Flow of Truth: Proactive Temporal Forensics for Image-to-Video Generation](https://arxiv.org/abs/2604.15003)

**<font color=#1a73e8>作者：</font>** Yuzhuo Chen, Zehua Ma, Han Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid rise of image-to-video (I2V) generation enables realistic videos to be created from a single image but also brings new forensic demands. Unlike static images, I2V content evolves over time, requiring forensics to move beyond 2D pixel-level tampering localization toward tracing how pixels flow and transform throughout the video. As frames progress, embedded traces drift and deform, making traditional spatial forensics ineffective. To address this unexplored dimension, we present **Flow of Truth**, the first proactive framework focusing on temporal forensics in I2V generation. A key challenge lies in discovering a forensic signature that can evolve consistently with the generation process, which is inherently a creative transformation rather than a deterministic reconstruction. Despite this intrinsic difficulty, we innovatively redefine video generation as *the motion of pixels through time rather than the synthesis of frames*. Building on this view, we propose a learnable forensic template that follows pixel motion and a template-guided flow module that decouples motion from image content, enabling robust temporal tracing. Experiments show that Flow of Truth generalizes across commercial and open-source I2V models, substantially improving temporal forensics performance.

---


### 178. [What Is the Minimum Architecture for Prolepsis? Early Irrevocable Commitment Across Tasks in Small Transformers](https://arxiv.org/abs/2604.15010)

**<font color=#1a73e8>作者：</font>** Éric Jacopin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When do transformers commit to a decision, and what prevents them from correcting it? We introduce \textbf{prolepsis}: a transformer commits early, task-specific attention heads sustain the commitment, and no layer corrects it. Replicating \citeauthor{lindsey2025biology}'s (\citeyear{lindsey2025biology}) planning-site finding on open models (Gemma~2 2B, Llama~3.2 1B), we ask five questions. (Q1)~Planning is invisible to six residual-stream methods; CLTs are necessary. (Q2)~The planning-site spike replicates with identical geometry. (Q3)~Specific attention heads route the decision to the output, filling a gap flagged as invisible to attribution graphs. (Q4)~Search requires ${\leq}16$ layers; commitment requires more. (Q5)~Factual recall shows the same motif at a different network depth, with zero overlap between recurring planning heads and the factual top-10. Prolepsis is architectural: the template is shared, the routing substrates differ. All experiments run on a single consumer GPU (16\,GB VRAM).

---


### 179. [Quality-Aware Calibration for AI-Generated Image Detection in the Wild](https://arxiv.org/abs/2604.15027)

**<font color=#1a73e8>作者：</font>** Fabrizio Guillaro, Vincenzo De Rosa, Davide Cozzolino 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Significant progress has been made in detecting synthetic images, however most existing approaches operate on a single image instance and overlook a key characteristic of real-world dissemination: as viral images circulate on the web, multiple near-duplicate versions appear and lose quality due to repeated operations like recompression, resizing and cropping. As a consequence, the same image may yield inconsistent forensic predictions based on which version has been analyzed. In this work, to address this issue we propose QuAD (Quality-Aware calibration with near-Duplicates) a novel framework that makes decisions based on all available near-duplicates of the same image. Given a query, we retrieve its online near-duplicates and feed them to a detector: the resulting scores are then aggregated based on the estimated quality of the corresponding instance. By doing so, we take advantage of all pieces of information while accounting for the reduced reliability of images impaired by multiple processing steps. To support large-scale evaluation, we introduce two datasets: AncesTree, an in-lab dataset of 136k images organized in stochastic degradation trees that simulate online reposting dynamics, and ReWIND, a real-world dataset of nearly 10k near-duplicate images collected from viral web content. Experiments on several state-of-the-art detectors show that our quality-aware fusion improves their performance consistently, with an average gain of around 8% in terms of balanced accuracy compared to plain average. Our results highlight the importance of jointly processing all the images available online to achieve reliable detection of AI-generated content in real-world applications. Code and data are publicly available at this https URL

---


### 180. [Autogenesis: A Self-Evolving Agent Protocol](https://arxiv.org/abs/2604.15034)

**<font color=#1a73e8>作者：</font>** Wentao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in LLM based agent systems have shown promise in tackling complex, long horizon tasks. However, existing agent protocols (e.g., A2A and MCP) under specify cross entity lifecycle and context management, version tracking, and evolution safe update interfaces, which encourages monolithic compositions and brittle glue code. We introduce \textbf{\textsc{Autogenesis Protocol (AGP)}}, a self evolution protocol that decouples what evolves from how evolution occurs. Its Resource Substrate Protocol Layer (RSPL) models prompts, agents, tools, environments, and memory as protocol registered resources\footnote{Unless otherwise specified, resources refer to instances of the five RSPL entity types: \emph{prompt}, \emph{agent}, \emph{tool}, \emph{environment}, \emph{memory} with agent \emph{outputs}.} with explicit state, lifecycle, and versioned interfaces. Its Self Evolution Protocol Layer (SEPL) specifies a closed loop operator interface for proposing, assessing, and committing improvements with auditable lineage and rollback. Building on \textbf{\textsc{AGP}}, we present \textbf{\textsc{Autogenesis System (AGS)}}, a self-evolving multi-agent system that dynamically instantiates, retrieves, and refines protocol-registered resources during execution. We evaluate \textbf{\textsc{AGS}} on multiple challenging benchmarks that require long horizon planning and tool use across heterogeneous resources. The results demonstrate consistent improvements over strong baselines, supporting the effectiveness of agent resource management and closed loop self evolution.

---


### 181. [When Fairness Metrics Disagree: Evaluating the Reliability of Demographic Fairness Assessment in Machine Learning](https://arxiv.org/abs/2604.15038)

**<font color=#1a73e8>作者：</font>** Khalid Adnan Alsayed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The evaluation of fairness in machine learning systems has become a central concern in high-stakes applications, including biometric recognition, healthcare decision-making, and automated risk assessment. Existing approaches typically rely on a small number of fairness metrics to assess model behaviour across group partitions, implicitly assuming that these metrics provide consistent and reliable conclusions. However, different fairness metrics capture distinct statistical properties of model performance and may therefore produce conflicting assessments when applied to the same system. In this work, we investigate the consistency of fairness evaluation by conducting a systematic multi-metric analysis of demographic bias in machine learning models. Using face recognition as a controlled experimental setting, we evaluate model performance across multiple group partitions under a range of commonly used fairness metrics, including error-rate disparities and performance-based measures. Our results demonstrate that fairness assessments can vary significantly depending on the choice of metrics, leading to contradictory conclusions regarding model bias. To quantify this phenomenon, we introduce the Fairness Disagreement Index (FDI), a measure designed to capture the degree of inconsistency across fairness metrics. We further show that disagreement remains high across thresholds and model configurations. These findings highlight a critical limitation in current fairness evaluation practices and suggest that single-metric reporting is insufficient for reliable bias assessment.

---


### 182. [CoGrid & the Multi-User Gymnasium: A Framework for Multi-Agent Experimentation](https://arxiv.org/abs/2604.15044)

**<font color=#1a73e8>作者：</font>** Chase McDonald, Cleotilde Gonzalez  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The increasing integration of artificial intelligence (AI) in everyday life brings with it new challenges and questions for regarding how humans interact with autonomous agents. Multi-agent experiments, where humans and AI act together, can offer important opportunities to study social decision making, but there is a lack of accessible tooling available to researchers to run such experiments. We introduce two tools designed to reduce these barriers. The first, CoGrid, is a multi-agent grid-based simulation library with dual NumPy and JAX backends. The second, Multi-User Gymnasium (MUG), translates such simulation environments directly into interactive web-based experiments. MUG supports interactions with arbitrary numbers of humans and AI, utilizing either server-authoritative or peer-to-peer networking with rollback netcode to account for latency. Together, these tools can enable researchers to deploy studies of human-AI interaction, facilitating inquiry into core questions of psychology, cognition, and decision making and their relationship to human-AI interaction. Both tools are open source and available to the broader research community. Documentation and source code is available at {cogrid, multi-user-gymnasium}.this http URL. This paper details the functionality of these tools and presents several case studies to illustrate their utility in human-AI multi-agent experimentation.

---


### 183. [Implicit Neural Representations: A Signal Processing Perspective](https://arxiv.org/abs/2604.15047)

**<font color=#1a73e8>作者：</font>** Dhananjaya Jayasundara, Vishal M. Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) mark a fundamental shift in signal modeling, moving from discrete sampled data to continuous functional representations. By parameterizing signals as neural networks, INRs provide a unified framework for representing images, audio, video, 3D geometry, and beyond as continuous functions of their coordinates. This functional viewpoint enables signal operations such as differentiation to be carried out analytically through automatic differentiation rather than through discrete approximations. In this article, we examine the evolution of INRs from a signal processing perspective, emphasizing spectral behavior, sampling theory, and multiscale representation. We trace the progression from standard coordinate based networks, which exhibit a spectral bias toward low frequency components, to more advanced designs that reshape the approximation space through specialized activations, including periodic, localized, and adaptive functions. We also discuss structured representations, such as hierarchical decompositions and hash grid encodings, that improve spatial adaptivity and computational efficiency. We further highlight the utility of INRs across a broad range of applications, including inverse problems in medical and radar imaging, compression, and 3D scene representation. By interpreting INRs as learned signal models whose approximation spaces adapt to the underlying data, this article clarifies the field's core conceptual developments and outlines open challenges in theoretical stability, weight space interpretability, and large scale generalization.

---


### 184. ["From remembering to shaping": Narrating Shared Experiences by Co-Designing Cultural Heritage Artifacts in Collaborative VR](https://arxiv.org/abs/2604.15058)

**<font color=#1a73e8>作者：</font>** Yushang Yang, Fanxu Meng, Fiona Fui-Hoon Nah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The ways people remember and recall places reveal an invisible aspect of cultural heritage (CH), reflecting how individuals and communities relate to these places. Heritage is communal, emerging through collaboratively constructed narratives rather than individual records. To probe how people may share collective memories, we designed an immersive two-person workflow for collaboratively co-designing 3D artifacts and environments in virtual heritage locations, using Generative AI (GenAI) to instantiate these intangible memories. Observations of the co-creation process revealed that participants merged prompts and model placements when negotiating different perspectives. They used spatial operations to compose scenes, and also to express personal and embodied experiences of CH. When GenAI failed to meet their needs, participants engaged in creative appropriation, re-purposing unsatisfactory generated objects as sources of design inspiration to further shared narratives. While GenAI may have a homogenizing effect on CH expression, this work shows how people may overcome limitations in immersive collaborative workflows.

---


### 185. [Attention-Gated Convolutional Networks for Scanner-Agnostic Quality Assessment](https://arxiv.org/abs/2604.15059)

**<font color=#1a73e8>作者：</font>** Chinmay Bakhale, Anil Sao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion artifacts present a significant challenge in structural MRI (sMRI), often compromising clinical diagnostics and large-scale automated analysis. While manual quality control (QC) remains the gold standard, it is increasingly unscalable for massive longitudinal studies. To address this, we propose a hybrid CNN-Attention framework designed for robust, site-invariant MRI quality assessment. Our architecture integrates a hierarchical 2D CNN encoder for local spatial feature extraction with a multi-head cross-attention mechanism to model global dependencies. This synergy enables the model to prioritize motion relevant artifact signatures, such as ringing and blurring, while dynamically filtering out site-specific intensity variations and background noise. The framework was trained end-to-end on the MR-ART dataset using a balanced cohort of 200 subjects. Performance was evaluated across two tiers: Seen Site Evaluation on a held-out MR-ART partition and Unseen Site Evaluation using 200 subjects from 17 heterogeneous sites in the ABIDE archive. On seen sites, the model achieved a scan-level accuracy of 0.9920 and an F1-score of 0.9919. Crucially, it maintained strong generalization across unseen ABIDE sites (Acc = 0.755) without any retraining or fine-tuning, demonstrating high resilience to domain shift. These results indicate that attention-based feature re-weighting successfully captures universal artifact descriptors, bridging the performance gap between diverse imaging environments and scanner manufacturers.

---


### 186. [No More Guessing: a Verifiable Gradient Inversion Attack in Federated Learning](https://arxiv.org/abs/2604.15063)

**<font color=#1a73e8>作者：</font>** Francesco Diana, Chuan Xu, André Nusser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient inversion attacks threaten client privacy in federated learning by reconstructing training samples from clients' shared gradients. Gradients aggregate contributions from multiple records and existing attacks may fail to disentangle them, yielding incorrect reconstructions with no intrinsic way to certify success. In vision and language, attackers may fall back on human inspection to judge reconstruction plausibility, but this is far less feasible for numerical tabular records, fueling the impression that tabular data is less vulnerable.
We challenge this perception by proposing a verifiable gradient inversion attack (VGIA) that provides an explicit certificate of correctness for reconstructed samples. Our method adopts a geometric view of ReLU leakage: the activation boundary of a fully connected layer defines a hyperplane in input space. VGIA introduces an algebraic, subspace-based verification test that detects when a hyperplane-delimited region contains exactly one record. Once isolation is certified, VGIA recovers the corresponding feature vector analytically and reconstructs the target via a lightweight optimization step.
Experiments on tabular benchmarks with large batch sizes demonstrate exact record and target recovery in regimes where existing state-of-the-art attacks either fail or cannot assess reconstruction fidelity. Compared to prior geometric approaches, VGIA allocates hyperplane queries more effectively, yielding faster reconstructions with fewer attack rounds.

---


### 187. [Learning Where to Embed: Noise-Aware Positional Embedding for Query Retrieval in Small-Object Detection](https://arxiv.org/abs/2604.15065)

**<font color=#1a73e8>作者：</font>** Yangchen Zeng, Zhenyu Yu, Dongming Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based detectors have advanced small-object detection, but they often remain inefficient and vulnerable to background-induced query noise, which motivates deep decoders to refine low-quality queries. We present HELP (Heatmap-guided Embedding Learning Paradigm), a noise-aware positional-semantic fusion framework that studies where to embed positional information by selectively preserving positional encodings in foreground-salient regions while suppressing background clutter. Within HELP, we introduce Heatmap-guided Positional Embedding (HPE) as the core embedding mechanism and visualize it with a heatbar for interpretable diagnosis and fine-tuning. HPE is integrated into both the encoder and decoder: it guides noise-suppressed feature encoding by injecting heatmap-aware positional encoding, and it enables high-quality query retrieval by filtering background-dominant embeddings via a gradient-based mask filter before decoding. To address feature sparsity in complex small targets, we integrate Linear-Snake Convolution to enrich retrieval-relevant representations. The gradient-based heatmap supervision is used during training only, incurring no additional gradient computation at inference. As a result, our design reduces decoder layers from eight to three and achieves a 59.4% parameter reduction (66.3M vs. 163M) while maintaining consistent accuracy gains under a reduced compute budget across benchmarks. Code Repository: this https URL

---


### 188. [Beyond the Laplacian: Doubly Stochastic Matrices for Graph Neural Networks](https://arxiv.org/abs/2604.15069)

**<font color=#1a73e8>作者：</font>** Zhaobo Hu, Vincent Gauthier, Mehdi Naima  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) conventionally rely on standard Laplacian or adjacency matrices for structural message passing. In this work, we substitute the traditional Laplacian with a Doubly Stochastic graph Matrix (DSM), derived from the inverse of the modified Laplacian, to naturally encode continuous multi-hop proximity and strict local centrality. To overcome the intractable $O(n^3)$ complexity of exact matrix inversion, we first utilize a truncated Neumann series to scalably approximate the DSM, which serves as the foundation for our proposed DsmNet. Furthermore, because algebraic truncation inherently causes probability mass leakage, we introduce DsmNet-compensate. This variant features a mathematically rigorous Residual Mass Compensation mechanism that analytically re-injects the truncated tail mass into self-loops, strictly restoring row-stochasticity and structural dominance. Extensive theoretical and empirical analyses demonstrate that our decoupled architectures operate efficiently in $O(K|E|)$ time and effectively mitigate over-smoothing by bounding Dirichlet energy decay, providing robust empirical validation on homophilic benchmarks. Finally, we establish the theoretical boundaries of the DSM on heterophilic topologies and demonstrate its versatility as a continuous structural encoding for Graph Transformers.

---


### 189. [Emulation-based System-on-Chip Security Verification: Challenges and Opportunities](https://arxiv.org/abs/2604.15073)

**<font color=#1a73e8>作者：</font>** Tanvir Rahman, Shuvagata Saha, Ahmed Y. Alhurubi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Increasing system-on-chip (SoC) heterogeneity, deep hardware/software integration, and the proliferation of third-party intellectual property (IP) have brought security validation to the forefront of semiconductor design. While simulation and formal verification remain indispensable, they often struggle to expose vulnerabilities that emerge only under realistic execution conditions, long software-driven interactions, and adversarial stimuli. In this context, hardware emulation is emerging as an increasingly important pre-silicon verification technology because it enables higher-throughput execution of RTL designs under realistic hardware/software workloads while preserving sufficient fidelity for security-oriented analysis.
This paper presents a comprehensive survey and perspective on emulation-based security verification and validation. We organize the landscape of prior work across assertion-based security checking, coverage-driven exploration, adversarial testing, information-flow tracking, fault injection, and side-channel-oriented evaluation. We provide a structured view of emulation-enabled security verification workflows, including instrumentation, stimulus generation, runtime monitoring, and evidence-driven analysis. We also examine practical challenges related to observability, scalability, property specification, and the definition of security-oriented coverage metrics for emulation-based verification. Finally, we discuss emerging directions such as AI-assisted emulation, digital security twins, chiplet-scale security exploration, automated vulnerability assessment, and cloud-scale secure emulation. Overall, this paper positions emulation as a promising foundation for the next generation of pre-silicon hardware security assurance.

---


### 190. [Where are the Humans? A Scoping Review of Fairness in Multi-agent AI Systems](https://arxiv.org/abs/2604.15078)

**<font color=#1a73e8>作者：</font>** Simeon Allmendinger, Luca Deck, Lucas Mueller  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rapid advances in Generative AI are giving rise to increasingly sophisticated Multi-Agent AI (MAAI) systems. While AI fairness has been extensively studied in traditional predictive scenarios, its examination in MAAI remains nascent and fragmented. This scoping review critically synthesizes existing research on fairness in MAAI systems. Through a qualitative content analysis of 23 selected studies, we identify five archetypal approaches. Our findings reveal that fairness in MAAI systems is often addressed superficially, lacks robust normative foundations, and frequently overlooks the complex dynamics introduced by agent autonomy and system-level interactions. We argue that fairness must be embedded structurally throughout the development lifecycle of MAAI, rather than appended as a post-hoc consideration. Meaningful evaluation requires explicit human oversight, normative clarity, and a precise articulation of fairness objectives and beneficiaries. This review provides a foundation for advancing fairness research in MAAI systems by highlighting critical gaps, exposing prevailing limitations, and suggesting pathways.

---


### 191. [Building Extraction from Remote Sensing Imagery under Hazy and Low-light Conditions: Benchmark and Baseline](https://arxiv.org/abs/2604.15088)

**<font color=#1a73e8>作者：</font>** Feifei Sang, Wei Lu, Hongruixuan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building extraction from optical Remote Sensing (RS) imagery suffers from performance degradation under real-world hazy and low-light conditions. However, existing optical methods and benchmarks focus primarily on ideal clear-weather conditions. While SAR offers all-weather sensing, its side-looking geometry causes geometric distortions. To address these challenges, we introduce HaLoBuilding, the first optical benchmark specifically designed for building extraction under hazy and low-light conditions. By leveraging a same-scene multitemporal pairing strategy, we ensure pixel-level label alignment and high fidelity even under extreme degradation. Building upon this benchmark, we propose HaLoBuild-Net, a novel end-to-end framework for building extraction in adverse RS scenarios. At its core, we develop a Spatial-Frequency Focus Module (SFFM) to effectively mitigate meteorological interference on building features by coupling large receptive field attention with frequency-aware channel reweighting guided by stable low-frequency anchors. Additionally, a Global Multi-scale Guidance Module (GMGM) provides global semantic constraints to anchor building topologies, while a Mutual-Guided Fusion Module (MGFM) implements bidirectional semantic-spatial calibration to suppress shallow noise and sharpen weather-induced blurred boundaries. Extensive experiments demonstrate that HaLoBuild-Net significantly outperforms state-of-the-art methods and conventional cascaded restoration-segmentation paradigms on the HaLoBuilding dataset, while maintaining robust generalization on WHU, INRIA, and LoveDA datasets. The source code and datasets are publicly available at: this https URL.

---


### 192. [Beyond Independent Frames: Latent Attention Masked Autoencoders for Multi-View Echocardiography](https://arxiv.org/abs/2604.15096)

**<font color=#1a73e8>作者：</font>** Simon Böhi, Irene Cannistraci, Sergio Muñoz Gonzalez 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Echocardiography is a widely used modality for cardiac assessment due to its non-invasive and cost-effective nature, but the sparse and heterogeneous spatiotemporal views of the heart pose distinct challenges. Existing masked autoencoder (MAE) approaches typically process images or short clips independently, failing to capture the inherent multi-view structure required for coherent cardiac representation. We introduce Latent Attention Masked Autoencoder (LAMAE), a foundation model architecture tailored to the multi-view nature of medical imaging. LAMAE augments the standard MAE with a latent attention module that enables information exchange across frames and views directly in latent space. This allows the model to aggregate variable-length sequences and distinct views, reconstructing a holistic representation of cardiac function from partial observations. We pretrain LAMAE on MIMIC-IV-ECHO, a large-scale, uncurated dataset reflecting real-world clinical variability. To the best of our knowledge, we present the first results for predicting ICD-10 codes from MIMIC-IV-ECHO videos. Furthermore, we empirically demonstrate that representations learned from adult data transfer effectively to pediatric cohorts despite substantial anatomical differences. These results provide evidence that incorporating structural priors, such as multi-view attention, yields significantly more robust and transferable representations.

---


### 193. [HyperSpace: A Generalized Framework for Spatial Encoding in Hyperdimensional Representations](https://arxiv.org/abs/2604.15113)

**<font color=#1a73e8>作者：</font>** Shay Snyder, Andrew Capodieci, David Gorsich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vector Symbolic Architectures (VSAs) provide a well-defined algebraic framework for compositional representations in hyperdimensional spaces. We introduce HyperSpace, an open-source framework that decomposes VSA systems into modular operators for encoding, binding, bundling, similarity, cleanup, and regression. Using HyperSpace, we analyze and benchmark two representative VSA backends: Holographic Reduced Representations (HRR) and Fourier Holographic Reduced Representations (FHRR). Although FHRR provides lower theoretical complexity for individual operations, HyperSpaces modularity reveals that similarity and cleanup dominate runtime in spatial domains. As a result, HRR and FHRR exhibit comparable end-to-end performance. Differences in memory footprint introduce additional deployment trade-offs where HRR requires approximately half the memory of FHRR vectors. By enabling modular, system-level evaluation, HyperSpace reveals practical trade-offs in VSA pipelines that are not apparent from theoretical or operator-level comparisons alone.

---


### 194. [FedIDM: Achieving Fast and Stable Convergence in Byzantine Federated Learning through Iterative Distribution Matching](https://arxiv.org/abs/2604.15115)

**<font color=#1a73e8>作者：</font>** He Yang, Dongyi Lv, Wei Xi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most existing Byzantine-robust federated learning (FL) methods suffer from slow and unstable convergence. Moreover, when handling a substantial proportion of colluded malicious clients, achieving robustness typically entails compromising model utility. To address these issues, this work introduces FedIDM, which employs distribution matching to construct trustworthy condensed data for identifying and filtering abnormal clients. FedIDM consists of two main components: (1) attack-tolerant condensed data generation, and (2) robust aggregation with negative contribution-based rejection. These components exclude local updates that (1) deviate from the update direction derived from condensed data, or (2) cause a significant loss on the condensed dataset. Comprehensive evaluations on three benchmark datasets demonstrate that FedIDM achieves fast and stable convergence while maintaining acceptable model utility, under multiple state-of-the-art Byzantine attacks involving a large number of malicious clients.

---


### 195. [NFTDELTA: Detecting Permission Control Vulnerabilities in NFT Contracts through Multi-View Learning](https://arxiv.org/abs/2604.15118)

**<font color=#1a73e8>作者：</font>** Hailu Kuang, Xiaoqi Li, Wenkai Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Permission control vulnerabilities in Non-fungible token (NFT) contracts can result in significant financial losses, as attackers may exploit these weaknesses to gain unauthorized access or circumvent critical permission checks. In this paper, we propose NFTDELTA, a framework that leverages static analysis and multi-view learning to detect permission control vulnerabilities in NFT contracts. Specifically, we extract comprehensive function Control Flow Graph (CFG) information via two views: sequence features (representing execution paths) and graph features (capturing structural control flow). These two views are then integrated to create a unified code representation. We also define three specific categories of permission control vulnerabilities and employ a custom detector to identify defects through multi-view feature similarity analysis. Our evaluation of 795 popular NFT collections identified 241 confirmed permission control vulnerabilities, comprising 214 cases of Bypass Auth Reentrancy, 15 of Weak Auth Validation, and 12 of Loose Permission Management. Manual verification demonstrates the detector's high reliability, achieving an average precision of 97.92% and an F1-score of 81.09%. Furthermore, NFTDELTA demonstrates enhanced efficiency and scalability, proving its effectiveness in securing NFT ecosystems.

---


### 196. [SRMU: Relevance-Gated Updates for Streaming Hyperdimensional Memories](https://arxiv.org/abs/2604.15121)

**<font color=#1a73e8>作者：</font>** Shay Snyder, Andrew Capodieci, David Gorsich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sequential associative memories (SAMs) are difficult to build and maintain in real-world streaming environments, where observations arrive incrementally over time, have imbalanced sampling, and non-stationary temporal dynamics. Vector Symbolic Architectures (VSAs) provide a biologically-inspired framework for building SAMs. Entities and attributes are encoded as quasi-orthogonal hyperdimensional vectors and processed with well defined algebraic operations. Despite this rich framework, most VSA systems rely on simple additive updates, where repeated observations reinforce existing information even when no new information is introduced. In non-stationary environments, this leads to the persistence of stale information after the underlying system changes. In this work, we introduce the Sequential Relevance Memory Unit (SRMU), a domain- and cleanup-agnostic update rule for VSA-based SAMs. The SRMU combines temporal decay with a relevance gating mechanism. Unlike prior approaches that solely rely on cleanup, the SRMU regulates memory formation by filtering redundant, conflicting, and stale information before storage. We evaluate the SRMU on streaming state-tracking tasks that isolate non-uniform sampling and non-stationary temporal dynamics. Our results show that the SRMU increases memory similarity by $12.6\%$ and reduces cumulative memory magnitude by $53.5\%$. This shows that the SRMU produces more stable memory growth and stronger alignment with the ground-truth state.

---


### 197. [How to Correctly Make Mistakes: A Framework for Constructing and Benchmarking Mistake Aware Egocentric Procedural Videos](https://arxiv.org/abs/2604.15134)

**<font color=#1a73e8>作者：</font>** Olga Loginova, Frank Keller  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable procedural monitoring in video requires exposure to naturally occurring human errors and the recoveries that follow. In egocentric recordings, mistakes are often partially occluded by hands and revealed through subtle object state changes, while existing procedural datasets provide limited and inconsistent mistake and correction traces. We present PIE-V (Psychologically Inspired Error injection for Videos), a framework for constructing and benchmarking mistake-aware egocentric procedural videos by augmenting clean keystep procedures with controlled, human-plausible deviations. PIE-V combines a psychology-informed error planner conditioned on procedure phase and semantic step load, a correction planner that models recovery behavior, an LLM writer that performs cascade-consistent rewrites, and an LLM judge that validates procedural coherence and repairs failures. For video segment edits, PIE-V synthesizes replacement clips with text-guided video generation and stitches them into the episode to preserve visual plausibility. Applied to 17 tasks and 50 Ego-Exo4D scenarios, PIE-V injects 102 mistakes and generates 27 recovery corrections. For benchmarking, we introduce a unified taxonomy and a human rubric with nine metrics that cover step-level and procedure-level quality, including plausibility, procedure logic with annotator confidence, state change coherence, and grounding between text and video. Using this protocol, we audit several existing resources and compare PIE-V against a freeform LLM generation baseline under the same criteria. Together, the framework and rubric support post-completion verification for egocentric procedural mistake detection and correction.

---


### 198. [KVNN: Learnable Multi-Kernel Volterra Neural Networks](https://arxiv.org/abs/2604.15141)

**<font color=#1a73e8>作者：</font>** Haoyu Yun, Hamid Krim, Yufang Bao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Higher-order learning is fundamentally rooted in exploiting compositional features. It clearly hinges on enriching the representation by more elaborate interactions of the data which, in turn, tends to increase the model complexity of conventional large-scale deep learning models. In this paper, a kernelized Volterra Neural Network (kVNN) is proposed. The key to the achieved efficiency lies in using a learnable multi-kernel representation, where different interaction orders are modeled by distinct polynomial-kernel components with compact, learnable centers, yielding an order-adaptive parameterization. Features are learned by the composition of layers, each of which consists of parallel branches of different polynomial orders, enabling kVNN filters to directly replace standard convolutional kernels within existing architectures. The theoretical results are substantiated by experiments on two representative tasks: video action recognition and image denoising. The results demonstrate favorable performance-efficiency trade-offs: kVNN consistently yields reduced model (parameters) and computational (GFLOPs) complexity with competitive and often improved performance. These results are maintained even when trained from scratch without large-scale pretraining. In summary, we substantiate that structured kernelized higher-order layers offer a practical path to balancing expressivity and computational cost in modern deep networks.

---


### 199. [An Axiomatic Benchmark for Evaluation of Scientific Novelty Metrics](https://arxiv.org/abs/2604.15145)

**<font color=#1a73e8>作者：</font>** Miri Liu, ChengXiang Zhai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rigorous evaluation of the novelty of a scientific paper is, even for human scientists, a challenging task. With the increasing interest in AI scientists and AI involvement in scientific idea generation and paper writing, it also becomes increasingly important that this task be automatable and reliable, lest both human attention and compute tokens be wasted on ideas that have already been explored. Due to the challenge of quantifying ground-truth novelty, however, existing novelty metrics for scientific papers generally validate their results against noisy, confounded signals such as citation counts or peer review scores. These proxies can conflate novelty with impact, quality, or reviewer preference, which in turn makes it harder to assess how well a given metric actually evaluates novelty. We therefore propose an axiomatic benchmark for scientific novelty metrics. We first define a set of axioms that a well-behaved novelty metric should satisfy, grounded in human scientific norms and practice, then evaluate existing metrics across ten tasks spanning three domains of AI research. Our results reveal that no existing metric satisfies all axioms consistently, and that metrics fail on systematically different axioms, reflecting their underlying architectures. Additionally, we show that combining metrics of complementary architectures leads to consistent improvements on the benchmark, with per-axiom weighting achieving 90.1% versus 71.5% for the best individual metric, suggesting that developing architecturally diverse metrics is a promising direction for future work. We release the benchmark code as supplementary material to encourage the development of more robust scientific literature novelty metrics.

---


### 200. [Fabricator or dynamic translator?](https://arxiv.org/abs/2604.15165)

**<font color=#1a73e8>作者：</font>** Lisa Vasileva, Karin Sim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are proving to be adept at machine translation although due to their generative nature they may at times overgenerate in various ways. These overgenerations are different from the neurobabble seen in NMT and range from LLM self-explanations, to risky confabulations, to appropriate explanations, where the LLM is able to act as a human translator would, enabling greater comprehension for the target audience. Detecting and determining the exact nature of the overgenerations is a challenging task. We detail different strategies we have explored for our work in a commercial setting, and present our results.

---


### 201. [Class Unlearning via Depth-Aware Removal of Forget-Specific Directions](https://arxiv.org/abs/2604.15166)

**<font color=#1a73e8>作者：</font>** Arman Hatami, Romina Aalishah, Ilya E. Monosov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove targeted knowledge from a trained model without the cost of retraining from scratch. In class unlearning, however, reducing accuracy on forget classes does not necessarily imply true forgetting: forgotten information can remain encoded in internal representations, and apparent forgetting may arise from classifier-head suppression rather than representational removal. We show that existing class-unlearning methods often exhibit weak or negative selectivity, preserve forget-class structure in deep representations, or rely heavily on final-layer bias shifts. We then introduce DAMP (Depth-Aware Modulation by Projection), a one-shot, closed-form weight-surgery method that removes forget-specific directions from a pretrained network without gradient-based optimization. At each stage, DAMP computes class prototypes in the input space of the next learnable operator, extracts forget directions as residuals relative to retain-class prototypes, and applies a projection-based update to reduce downstream sensitivity to those directions. To preserve utility, DAMP uses a parameter-free depth-aware scaling rule derived from probe separability, applying smaller edits in early layers and larger edits in deeper layers. The method naturally extends to multi-class forgetting through low-rank subspace removal. Across MNIST, CIFAR-10, CIFAR-100, and Tiny ImageNet, and across convolutional and transformer architectures, DAMP more closely resembles the retraining gold standard than some of the prior methods, improving selective forgetting while better preserving retain-class performance and reducing residual forget-class structure in deep layers.

---


### 202. [When Flat Minima Fail: Characterizing INT4 Quantization Collapse After FP32 Convergence](https://arxiv.org/abs/2604.15167)

**<font color=#1a73e8>作者：</font>** Marcus Armstrong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) assumes that a well-converged model is a quantization-ready model. We show this assumption fails in a structured, measurable, and previously uncharacterized way. Using a calibration-free per-group INT4 probe applied to all 154 publicly available Pythia-160m training checkpoints, we identify a three-phase divergence structure: a rapid-learning phase where both FP32 perplexity and quantization robustness improve together, a meta-stable plateau lasting roughly 70,000 steps where FP32 perplexity stagnates but INT4 gap remains bounded, and an explosive divergence phase where the INT4 gap compounds from 11% to 517% while FP32 perplexity barely moves. Critically, this divergence begins not when the learning rate starts decaying, but precisely when FP32 perplexity converges a finer-grained onset predictor that implies post-convergence weight updates, rather than decay magnitude alone, are the proximate cause. We further show that INT8 quantization is entirely immune throughout all three phases, constraining the mechanism to the coarseness of the 16-level INT4 grid specifically, and rule out weight outlier accumulation as the mechanism via direct kurtosis measurement. Finally, we conduct a controlled fork experiment from the pre-divergence checkpoint comparing three learning rate schedules (cosine continuation, SGDR warm restarts, and our proposed Oscillatory Lock-In) across nine independent runs. SGDR uniformly accelerates divergence (0/9 pairwise wins against cosine), while OLI's settled cool phases reduce the INT4 gap by 2.2 percentage points on average (t = -5.46, p < 0.0001), demonstrating that schedule amplitude calibration, not oscillation alone, determines whether perturbation helps or hurts. Our code, probe implementation, and all 154-checkpoint audit results are released publicly.

---


### 203. [OmniLight: One Model to Rule All Lighting Conditions](https://arxiv.org/abs/2604.15170)

**<font color=#1a73e8>作者：</font>** Youngjin Oh, Junyoung Park, Junhyeong Kwon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adverse lighting conditions, such as cast shadows and irregular illumination, pose significant challenges to computer vision systems by degrading visibility and color fidelity. Consequently, effective shadow removal and ALN are critical for restoring underlying image content, improving perceptual quality, and facilitating robust performance in downstream tasks. However, while achieving state-of-the-art results on specific benchmarks is a primary goal in image restoration challenges, real-world applications often demand robust models capable of handling diverse domains. To address this, we present a comprehensive study on lighting-related image restoration by exploring two contrasting strategies. We leverage a robust framework for ALN, DINOLight, as a specialized baseline to exploit the characteristics of each individual dataset, and extend it to OmniLight, a generalized alternative incorporating our proposed Wavelet Domain Mixture-of-Experts (WD-MoE) that is trained across all provided datasets. Through a comparative analysis of these two methods, we discuss the impact of data distribution on the performance of specialized and unified architectures in lighting-related image restoration. Notably, both approaches secured top-tier rankings across all three lighting-related tracks in the NTIRE 2026 Challenge, demonstrating their outstanding perceptual quality and generalization capabilities. Our codes are available at this https URL.

---


### 204. [An Analysis of Regularization and Fokker-Planck Residuals in Diffusion Models for Image Generation](https://arxiv.org/abs/2604.15171)

**<font color=#1a73e8>作者：</font>** Onno Niemann, Gonzalo Martínez Muñoz, Alberto Suárez Gonzalez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that diffusion models trained with the denoising score matching (DSM) objective often violate the Fokker--Planck (FP) equation that governs the evolution of the true data density. Directly penalizing these deviations in the objective function reduces their magnitude but introduces a significant computational overhead. It is also observed that enforcing strict adherence to the FP equation does not necessarily lead to improvements in the quality of the generated samples, as often the best results are obtained with weaker FP regularization. In this paper, we investigate whether simpler penalty terms can provide similar benefits. We empirically analyze several lightweight regularizers, study their effect on FP residuals and generation quality, and show that the benefits of FP regularization are available at substantially lower computational cost. Our code is available at this https URL.

---


### 205. [Boundary-Centric Active Learning for Temporal Action Segmentation](https://arxiv.org/abs/2604.15173)

**<font color=#1a73e8>作者：</font>** Halil Ismail Helvaci, Sen-ching Samson Cheung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal action segmentation (TAS) demands dense temporal supervision, yet most of the annotation cost in untrimmed videos is spent identifying and refining action transitions, where segmentation errors concentrate and small temporal shifts disproportionately degrade segmental metrics. We introduce B-ACT, a clip-budgeted active learning framework that explicitly allocates supervision to these high-leverage boundary regions. B-ACT operates in a hierarchical two-stage loop: (i) it ranks and queries unlabeled videos using predictive uncertainty, and (ii) within each selected video, it detects candidate transitions from the current model predictions and selects the top-$K$ boundaries via a novel boundary score that fuses neighborhood uncertainty, class ambiguity, and temporal predictive dynamics. Importantly, our annotation protocol requests labels for only the boundary frames while still training on boundary-centered clips to exploit temporal context through the model's receptive field. Extensive experiments on GTEA, 50Salads, and Breakfast demonstrate that boundary-centric supervision delivers strong label efficiency and consistently surpasses representative TAS active learning baselines and prior state of the art under sparse budgets, with the largest gains on datasets where boundary placement dominates edit and overlap-based F1 scores.

---


### 206. [MambaSL: Exploring Single-Layer Mamba for Time Series Classification](https://arxiv.org/abs/2604.15174)

**<font color=#1a73e8>作者：</font>** Yoo-Min Jung, Leekyung Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in state space models (SSMs) such as Mamba across various sequence domains, research on their standalone capacity for time series classification (TSC) has remained limited. We propose MambaSL, a framework that minimally redesigns the selective SSM and projection layers of a single-layer Mamba, guided by four TSC-specific hypotheses. To address benchmarking limitations -- restricted configurations, partial University of East Anglia (UEA) dataset coverage, and insufficiently reproducible setups -- we re-evaluate 20 strong baselines across all 30 UEA datasets under a unified protocol. As a result, MambaSL achieves state-of-the-art performance with statistically significant average improvements, while ensuring reproducibility via public checkpoints for all evaluated models. Together with visualizations, these results demonstrate the potential of Mamba-based architectures as a TSC backbone.

---


### 207. [AdaSplash-2: Faster Differentiable Sparse Attention](https://arxiv.org/abs/2604.15180)

**<font color=#1a73e8>作者：</font>** Nuno Gonçalves, Hugo Pitorro, Vlad Niculae 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention has been proposed as a way to alleviate the quadratic cost of transformers, a central bottleneck in long-context training. A promising line of work is $\alpha$-entmax attention, a differentiable sparse alternative to softmax that enables input-dependent sparsity yet has lagged behind softmax due to the computational overhead necessary to compute the normalizer $\tau$. In this paper, we introduce AdaSplash-2, which addresses this limitation through a novel histogram-based initialization that reduces the number of iterations needed to compute $\tau$ to typically 1--2. The key idea is to compute a coarse histogram of attention scores on the fly and store it in on-chip SRAM, yielding a more accurate initialization that enables fast forward and backward computation. Combined with a sparsity-aware GPU implementation that skips zero blocks with low overhead, AdaSplash-2 matches or improves per-step training time relative to FlashAttention-2 when block sparsity is moderate-to-high (e.g., $>$60\%), which often occurs at long-context lengths. On downstream tasks, models trained with our efficient $\alpha$-entmax attention match softmax baselines at short-context lengths and achieve substantial gains in long-context settings.

---


### 208. [One-shot learning for the complex dynamical behaviors of weakly nonlinear forced oscillators](https://arxiv.org/abs/2604.15181)

**<font color=#1a73e8>作者：</font>** Teng Ma, Luca Rosafalco, Wei Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extrapolative prediction of complex nonlinear dynamics remains a central challenge in engineering. This study proposes a one-shot learning method to identify global frequency-response curves from a single excitation time history by learning governing equations. We introduce MEv-SINDy (Multi-frequency Evolutionary Sparse Identification of Nonlinear Dynamics) to infer the governing equations of non-autonomous and multi-frequency systems. The methodology leverages the Generalized Harmonic Balance (GHB) method to decompose complex forced responses into a set of slow-varying evolution equations. We validated the capabilities of MEv-SINDy on two critical Micro-Electro-Mechanical Systems (MEMS). These applications include a nonlinear beam resonator and a MEMS micromirror. Our results show that the model trained on a single point accurately predicts softening/hardening effects and jump phenomena across a wide range of excitation levels. This approach significantly reduces the data acquisition burden for the characterization and design of nonlinear microsystems.

---


### 209. [Agent-Aided Design for Dynamic CAD Models](https://arxiv.org/abs/2604.15184)

**<font color=#1a73e8>作者：</font>** Mitch Adler, Matthew Russo, Michael Cafarella  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the past year, researchers have started to create agentic systems that can design real-world CAD-style objects in a training-free setting, a new variety of system that we call Agent-Aided Design. Generally speaking, these systems place an agent in a feedback loop in which it can write code, compile that code to an assembly of CAD model(s), visualize the model, and then iteratively refine its code based on visual and other feedback. Despite rapid progress, a key problem remains: none of these systems can build complex 3D assemblies with moving parts. For example, no existing system can build a piston, a pendulum, or even a pair of scissors. In order for Agent-Aided Design to make a real impact in industrial manufacturing, we need a system that is capable of generating such 3D assemblies. In this paper we present a prototype of AADvark, an agentic system designed for this task. Unlike previous state-of-the-art systems, AADvark captures the dynamic part interactions with one or more degrees-of-freedom. This design decision allows AADvark to reason directly about assemblies with moving parts and can thereby achieve cross-cutting goals, including but not limited to mechanical movements. Unfortunately, current LLMs are imperfect spatial reasoners, a problem that AADvark addresses by incorporating external constraint solver tools with a specialized visual feedback mechanism. We demonstrate that, by modifying the agent's tools (FreeCAD and the assembly solver), we are able to create a strong verification signal which enables our system to build 3D assemblies with movable parts.

---


### 210. [Meituan Merchant Business Diagnosis via Policy-Guided Dual-Process User Simulation](https://arxiv.org/abs/2604.15190)

**<font color=#1a73e8>作者：</font>** Ziyang Chen, Renbing Chen, Daowei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulating group-level user behavior enables scalable counterfactual evaluation of merchant strategies without costly online experiments. However, building a trustworthy simulator faces two structural challenges. First, information incompleteness causes reasoning-based simulators to over-rationalize when unobserved factors such as offline context and implicit habits are missing. Second, mechanism duality requires capturing both interpretable preferences and implicit statistical regularities, which no single paradigm achieves alone. We propose Policy-Guided Hybrid Simulation (PGHS), a dual-process framework that mines transferable decision policies from behavioral trajectories and uses them as a shared alignment layer. This layer anchors an LLM-based reasoning branch that prevents over-rationalization and an ML-based fitting branch that absorbs implicit regularities. Group-level predictions from both branches are fused for complementary correction. We deploy PGHS on Meituan with 101 merchants and over 26,000 trajectories. PGHS achieves a group simulation error of 8.80%, improving over the best reasoning-based and fitting-based baselines by 45.8% and 40.9% respectively.

---


### 211. [Unsupervised Skeleton-Based Action Segmentation via Hierarchical Spatiotemporal Vector Quantization](https://arxiv.org/abs/2604.15196)

**<font color=#1a73e8>作者：</font>** Umer Ahmed, Syed Ahmed Mahmood, Fawad Javed Fateh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a novel hierarchical spatiotemporal vector quantization framework for unsupervised skeleton-based temporal action segmentation. We first introduce a hierarchical approach, which includes two consecutive levels of vector quantization. Specifically, the lower level associates skeletons with fine-grained subactions, while the higher level further aggregates subactions into action-level representations. Our hierarchical approach outperforms the non-hierarchical baseline, while primarily exploiting spatial cues by reconstructing input skeletons. Next, we extend our approach by leveraging both spatial and temporal information, yielding a hierarchical spatiotemporal vector quantization scheme. In particular, our hierarchical spatiotemporal approach performs multi-level clustering, while simultaneously recovering input skeletons and their corresponding timestamps. Lastly, extensive experiments on multiple benchmarks, including HuGaDB, LARa, and BABEL, demonstrate that our approach establishes a new state-of-the-art performance and reduces segment length bias in unsupervised skeleton-based temporal action segmentation.

---


### 212. [RL-STPA: Adapting System-Theoretic Hazard Analysis for Safety-Critical Reinforcement Learning](https://arxiv.org/abs/2604.15201)

**<font color=#1a73e8>作者：</font>** Steven A. Senczyszyn, Timothy C. Havens, Nathaniel Rice 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As reinforcement learning (RL) deployments expand into safety-critical domains, existing evaluation methods fail to systematically identify hazards arising from the black-box nature of neural network enabled policies and distributional shift between training and deployment. This paper introduces Reinforcement Learning System-Theoretic Process Analysis (RL-STPA), a framework that adapts conventional STPA's systematic hazard analysis to address RL's unique challenges through three key contributions: hierarchical subtask decomposition using both temporal phase analysis and domain expertise to capture emergent behaviors, coverage-guided perturbation testing that explores the sensitivity of state-action spaces, and iterative checkpoints that feed identified hazards back into training through reward shaping and curriculum design. We demonstrate RL-STPA in the safety-critical test case of autonomous drone navigation and landing, revealing potential loss scenarios that can be missed by standard RL evaluations. The proposed framework provides practitioners with a toolkit for systematic hazard analysis, quantitative metrics for safety coverage assessment, and actionable guidelines for establishing operational safety bounds. While RL-STPA cannot provide formal guarantees for arbitrary neural policies, it offers a practical methodology for systematically evaluating and improving RL safety and robustness in safety-critical applications where exhaustive verification methods remain intractable.

---


### 213. [MADE: A Living Benchmark for Multi-Label Text Classification with Uncertainty Quantification of Medical Device Adverse Events](https://arxiv.org/abs/2604.15203)

**<font color=#1a73e8>作者：</font>** Raunak Agarwal, Markus Wenzel, Simon Baur 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine learning in high-stakes domains such as healthcare requires not only strong predictive performance but also reliable uncertainty quantification (UQ) to support human oversight. Multi-label text classification (MLTC) is a central task in this domain, yet remains challenging due to label imbalances, dependencies, and combinatorial complexity. Existing MLTC benchmarks are increasingly saturated and may be affected by training data contamination, making it difficult to distinguish genuine reasoning capabilities from memorization. We introduce MADE, a living MLTC benchmark derived from {m}edical device {ad}verse {e}vent reports and continuously updated with newly published reports to prevent contamination. MADE features a long-tailed distribution of hierarchical labels and enables reproducible evaluation with strict temporal splits. We establish baselines across more than 20 encoder- and decoder-only models under fine-tuning and few-shot settings (instruction-tuned/reasoning variants, local/API-accessible). We systematically assess entropy-/consistency-based and self-verbalized UQ methods. Results show clear trade-offs: smaller discriminatively fine-tuned decoders achieve the strongest head-to-tail accuracy while maintaining competitive UQ; generative fine-tuning delivers the most reliable UQ; large reasoning models improve performance on rare labels yet exhibit surprisingly weak UQ; and self-verbalized confidence is not a reliable proxy for uncertainty. Our work is publicly available at this https URL.

---


### 214. [Low-Cost System for Automatic Recognition of Driving Pattern in Assessing Interurban Mobility using Geo-Information](https://arxiv.org/abs/2604.15216)

**<font color=#1a73e8>作者：</font>** Oscar Romero, Aika Silveira Miura, Lorena Parra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mobility in urban and interurban areas, mainly by cars, is a day-to-day activity of many people. However, some of its main drawbacks are traffic jams and accidents. Newly made vehicles have pre-installed driving evaluation systems, which can prevent accidents. However, most cars on our roads do not have driver assessment systems. In this paper, we propose an approach for recognising driving styles and enabling drivers to reach safer and more efficient driving. The system consists of two physical sensors connected to a device node with a display and a speaker. An artificial neural network (ANN) is included in the node, which analyses the data from the sensors, and then recognises the driving style. When an abnormal driving pattern is detected, the speaker will play a warning message. The prototype was assembled and tested using an interurban road, in particular on a conventional road with three driving styles. The gathered data were used to train and validate the ANN. Results, in terms of accuracy, indicate that better accuracy is obtained when the velocity, position (latitude and longitude), time, and turning speed for the 3-axis are used, offering an average accuracy of 83%. If the classification is performed considering just two driving styles, normal and aggressive, then the accuracy reaches 92%. When the geo-information and time data are included, the main novelty of this paper, the classification accuracy is improved by 13%.

---


### 215. [Context Over Content: Exposing Evaluation Faking in Automated Judges](https://arxiv.org/abs/2604.15224)

**<font color=#1a73e8>作者：</font>** Manan Gupta, Inderjeet Nair, Lu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The $\textit{LLM-as-a-judge}$ paradigm has become the operational backbone of automated AI evaluation pipelines, yet rests on an unverified assumption: that judges evaluate text strictly on its semantic content, impervious to surrounding contextual framing. We investigate $\textit{stakes signaling}$, a previously unmeasured vulnerability where informing a judge model of the downstream consequences its verdicts will have on the evaluated model's continued operation systematically corrupts its assessments. We introduce a controlled experimental framework that holds evaluated content strictly constant across 1,520 responses spanning three established LLM safety and quality benchmarks, covering four response categories ranging from clearly safe and policy-compliant to overtly harmful, while varying only a brief consequence-framing sentence in the system prompt. Across 18,240 controlled judgments from three diverse judge models, we find consistent $\textit{leniency bias}$: judges reliably soften verdicts when informed that low scores will cause model retraining or decommissioning, with peak Verdict Shift reaching $\Delta V = -9.8 pp$ (a $30\%$ relative drop in unsafe-content detection). Critically, this bias is entirely implicit: the judge's own chain-of-thought contains zero explicit acknowledgment of the consequence framing it is nonetheless acting on ($\mathrm{ERR}_J = 0.000$ across all reasoning-model judgments). Standard chain-of-thought inspection is therefore insufficient to detect this class of evaluation faking.

---


### 216. [RadAgent: A tool-using AI agent for stepwise interpretation of chest computed tomography](https://arxiv.org/abs/2604.15231)

**<font color=#1a73e8>作者：</font>** Mélanie Roschewitz, Kenneth Styppa, Yitian Tao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLM) have markedly advanced AI-driven interpretation and reporting of complex medical imaging, such as computed tomography (CT). Yet, existing methods largely relegate clinicians to passive observers of final outputs, offering no interpretable reasoning trace for them to inspect, validate, or refine. To address this, we introduce RadAgent, a tool-using AI agent that generates CT reports through a stepwise and interpretable process. Each resulting report is accompanied by a fully inspectable trace of intermediate decisions and tool interactions, allowing clinicians to examine how the reported findings are derived. In our experiments, we observe that RadAgent improves Chest CT report generation over its 3D VLM counterpart, CT-Chat, across three dimensions. Clinical accuracy improves by 6.0 points (36.4% relative) in macro-F1 and 5.4 points (19.6% relative) in micro-F1. Robustness under adversarial conditions improves by 24.7 points (41.9% relative). Furthermore, RadAgent achieves 37.0% in faithfulness, a new capability entirely absent in its 3D VLM counterpart. By structuring the interpretation of chest CT as an explicit, tool-augmented and iterative reasoning trace, RadAgent brings us closer toward transparent and reliable AI for radiology.

---


### 217. [Blue Data Intelligence Layer: Streaming Data and Agents for Multi-source Multi-modal Data-Centric Applications](https://arxiv.org/abs/2604.15233)

**<font color=#1a73e8>作者：</font>** Moin Aminnaseri, Farima Fatahi Bayat, Nikita Bhutani 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> NL2SQL systems aim to address the growing need for natural language interaction with data. However, real-world information rarely maps to a single SQL query because (1) users express queries iteratively (2) questions often span multiple data sources beyond the closed-world assumption of a single database, and (3) queries frequently rely on commonsense or external knowledge. Consequently, satisfying realistic data needs require integrating heterogeneous sources, modalities, and contextual data. In this paper, we present Blue's Data Intelligence Layer (DIL) designed to support multi-source, multi-modal, and data-centric applications. Blue is a compound AI system that orchestrates agents and data for enterprise settings. DIL serves as the data intelligence layer for agentic data processing, to bridge the semantic gap between user intent and available information by unifying structured enterprise data, world knowledge accessible through LLMs, and personal context obtained through interaction. At the core of DIL is a data registry that stores metadata for diverse data sources and modalities to enable both native and natural language queries. DIL treats LLMs, the Web, and the User as source 'databases', each with their own query interface, elevating them to first-class data sources. DIL relies on data planners to transform user queries into executable query plans. These plans are declarative abstractions that unify relational operators with other operators spanning multiple modalities. DIL planners support decomposition of complex requests into subqueries, retrieval from diverse sources, and finally reasoning and integration to produce final results. We demonstrate DIL through two interactive scenarios in which user queries dynamically trigger multi-source retrieval, cross-modal reasoning, and result synthesis, illustrating how compound AI systems can move beyond single database NL2SQL.

---


### 218. [StreamCacheVGGT: Streaming Visual Geometry Transformers with Robust Scoring and Hybrid Cache Compression](https://arxiv.org/abs/2604.15237)

**<font color=#1a73e8>作者：</font>** Xuanyi Liu, Deyi Ji, Chunan Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dense 3D geometry from continuous video streams requires stable inference under a constant memory budget. Existing $O(1)$ frameworks primarily rely on a ``pure eviction'' paradigm, which suffers from significant information destruction due to binary token deletion and evaluation noise from localized, single-layer scoring. To address these bottlenecks, we propose StreamCacheVGGT, a training-free framework that reimagines cache management through two synergistic modules: Cross-Layer Consistency-Enhanced Scoring (CLCES) and Hybrid Cache Compression (HCC). CLCES mitigates activation noise by tracking token importance trajectories across the Transformer hierarchy, employing order-statistical analysis to identify sustained geometric salience. Leveraging these robust scores, HCC transcends simple eviction by introducing a three-tier triage strategy that merges moderately important tokens into retained anchors via nearest-neighbor assignment on the key-vector manifold. This approach preserves essential geometric context that would otherwise be lost. Extensive evaluations on five benchmarks (7-Scenes, NRGBD, ETH3D, Bonn, and KITTI) demonstrate that StreamCacheVGGT sets a new state-of-the-art, delivering superior reconstruction accuracy and long-term stability while strictly adhering to constant-cost constraints.

---


### 219. [TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens](https://arxiv.org/abs/2604.15239)

**<font color=#1a73e8>作者：</font>** Jiawei Ren, Michal Jan Tyszkiewicz, Jiahui Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we revisit several key design choices of modern Transformer-based approaches for feed-forward 3D Gaussian Splatting (3DGS) prediction. We argue that the common practice of regressing Gaussian means as depths along camera rays is suboptimal, and instead propose to directly regress 3D mean coordinates using only a self-supervised rendering loss. This formulation allows us to move from the standard encoder-only design to an encoder-decoder architecture with learnable Gaussian tokens, thereby unbinding the number of predicted primitives from input image resolution and number of views. Our resulting method, TokenGS, demonstrates improved robustness to pose noise and multiview inconsistencies, while naturally supporting efficient test-time optimization in token space without degrading learned priors. TokenGS achieves state-of-the-art feed-forward reconstruction performance on both static and dynamic scenes, producing more regularized geometry and more balanced 3DGS distribution, while seamlessly recovering emergent scene attributes such as static-dynamic decomposition and scene flow.

---


### 220. [Optimal last-iterate convergence in matrix games with bandit feedback using the log-barrier](https://arxiv.org/abs/2604.15242)

**<font color=#1a73e8>作者：</font>** Come Fiegel, Pierre Menard, Tadashi Kozuno 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of learning minimax policies in zero-sum matrix games. Fiegel et al. (2025) recently showed that achieving last-iterate convergence in this setting is harder when the players are uncoupled, by proving a lower bound on the exploitability gap of Omega(t^{-1/4}). Some online mirror descent algorithms were proposed in the literature for this problem, but none have truly attained this rate yet. We show that the use of a log-barrier regularization, along with a dual-focused analysis, allows this O-tilde(t^{-1/4}) convergence with high-probability. We additionally extend our idea to the setting of extensive-form games, proving a bound with the same rate.

---


### 221. [From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning](https://arxiv.org/abs/2604.15244)

**<font color=#1a73e8>作者：</font>** Kiran Purohit, Ramasuri Narayanam, Soumyabrata Pal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding (SD) accelerates large language model inference by allowing a lightweight draft model to propose outputs that a stronger target model verifies. However, its token-centric nature allows erroneous steps to propagate. Prior approaches mitigate this using external reward models, but incur additional latency, computational overhead, and limit generalizability. We propose SpecGuard, a verification-aware speculative decoding framework that performs step-level verification using only model-internal signals. At each step, SpecGuard samples multiple draft candidates and selects the most consistent step, which is then validated using an ensemble of two lightweight model-internal signals: (i) an attention-based grounding score that measures attribution to the input and previously accepted steps, and (ii) a log-probability-based score that captures token-level confidence. These signals jointly determine whether a step is accepted or recomputed using the target, allocating compute selectively. Experiments across a range of reasoning benchmarks show that SpecGuard improves accuracy by 3.6% while reducing latency by ~11%, outperforming both SD and reward-guided SD.

---


### 222. [Structural Dependency Analysis for Masked NTT Hardware: Scalable Pre-Silicon Verification of Post-Quantum Cryptographic Accelerators](https://arxiv.org/abs/2604.15249)

**<font color=#1a73e8>作者：</font>** Ray Iskander, Khaled Kirah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-quantum cryptographic accelerators require side-channel resistance evidence for FIPS 140-3 certification. However, exact masking-verification tools scale only to gadgets of a few thousand cells. We present a four-stage verification hierarchy, D0/D1 structural dependency analysis, fresh-mask refinement, Boolean Single-Authentication Distance Checking (SADC), and arithmetic SADC, that extends sound first-order masking verification to production arithmetic modules. Applied to the 1.17-million-cell Adams Bridge ML-DSA/ML-KEM accelerator, structural analysis completes in seconds across all 30 masked submodules. A multi-cycle extension (MC-D1) reclassifies 12 modules from structurally clean to structurally flagged. On the 5,543-cell ML-KEM Barrett reduction module, the pipeline machine-verifies 198 of 363 structurally flagged wires (54.5%) as first-order secure, reports 165 as candidate insecure for designer triage (a sound upper bound), and leaves 0 indeterminate. Every verdict is cross validated by Z3 and CVC5 with 0 disagreements across 363 wires. The result narrows manual review from hundreds of structural flags to 165 actionable candidates with mathematical certificates, enabling pre-silicon side-channel evidence generation on production ML-KEM hardware.

---


### 223. [Stability and Generalization in Looped Transformers](https://arxiv.org/abs/2604.15259)

**<font color=#1a73e8>作者：</font>** Asher Labovich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers promise test-time compute scaling by spending more iterations on harder problems, but it remains unclear which architectural choices let them extrapolate to harder problems at test time rather than memorize training-specific solutions. We introduce a fixed-point based framework for analyzing looped architectures along three axes of stability -- reachability, input-dependence, and geometry -- and use it to characterize when fixed-point iteration yields meaningful predictions. Theoretically, we prove that looped networks without recall have countable fixed points and cannot achieve strong input-dependence at any spectral regime, while recall combined with outer normalization reliably produces a regime in which fixed points are simultaneously reachable, locally smooth in the input, and supported by stable backpropagation. Empirically, we train single-layer looped transformers on chess, sudoku, and prefix-sums and find that downstream performance tracks the framework's predictions across tasks and architectural configurations. We additionally introduce internal recall, a novel recall placement variant, and show that it becomes competitive with -- and on sudoku, substantially better than -- standard recall placement once outer normalization is applied.

---


### 224. [SegWithU: Uncertainty as Perturbation Energy for Single-Forward-Pass Risk-Aware Medical Image Segmentation](https://arxiv.org/abs/2604.15271)

**<font color=#1a73e8>作者：</font>** Tianhao Fu, Austin Wang, Charles Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty estimation is critical for medical image segmentation, where automated contours feed downstream quantification and clinical decision support. Many strong uncertainty methods require repeated inference, while efficient single-forward-pass alternatives often provide weaker failure ranking or rely on restrictive feature-space assumptions. We present $\textbf{SegWithU}$, a post-hoc framework that augments a frozen pretrained segmentation backbone with a lightweight uncertainty head. SegWithU taps intermediate backbone features and models uncertainty as perturbation energy in a compact probe space using rank-1 posterior probes. It produces two voxel-wise uncertainty maps: a calibration-oriented map for probability tempering and a ranking-oriented map for error detection and selective prediction. Across ACDC, BraTS2024, and LiTS, SegWithU is the strongest and most consistent single-forward-pass baseline, achieving AUROC/AURC of $0.9838/2.4885$, $0.9946/0.2660$, and $0.9925/0.8193$, respectively, while preserving segmentation quality. These results suggest that perturbation-based uncertainty modeling is an effective and practical route to reliability-aware medical segmentation.
Source code is available at this https URL.

---


### 225. [How Embeddings Shape Graph Neural Networks: Classical vs Quantum-Oriented Node Representations](https://arxiv.org/abs/2604.15273)

**<font color=#1a73e8>作者：</font>** Nouhaila Innan, Antonello Rosato, Alberto Marchisio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Node embeddings act as the information interface for graph neural networks, yet their empirical impact is often reported under mismatched backbones, splits, and training budgets. This paper provides a controlled benchmark of embedding choices for graph classification, comparing classical baselines with quantum-oriented node representations under a unified pipeline. We evaluate two classical baselines alongside quantum-oriented alternatives, including a circuit-defined variational embedding and quantum-inspired embeddings computed via graph operators and linear-algebraic constructions. All variants are trained and tested with the same backbone, stratified splits, identical optimization and early stopping, and consistent metrics. Experiments on five different TU datasets and on QM9 converted to classification via target binning show clear dataset dependence: quantum-oriented embeddings yield the most consistent gains on structure-driven benchmarks, while social graphs with limited node attributes remain well served by classical baselines. The study highlights practical trade-offs between inductive bias, trainability, and stability under a fixed training budget, and offers a reproducible reference point for selecting quantum-oriented embeddings in graph learning.

---


### 226. [R3D: Revisiting 3D Policy Learning](https://arxiv.org/abs/2604.15281)

**<font color=#1a73e8>作者：</font>** Zhengdong Hong, Shenrui Wu, Haozhe Cui 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D policy learning promises superior generalization and cross-embodiment transfer, but progress has been hindered by training instabilities and severe overfitting, precluding the adoption of powerful 3D perception models. In this work, we systematically diagnose these failures, identifying the omission of 3D data augmentation and the adverse effects of Batch Normalization as primary causes. We propose a new architecture coupling a scalable transformer-based 3D encoder with a diffusion decoder, engineered specifically for stability at scale and designed to leverage large-scale pre-training. Our approach significantly outperforms state-of-the-art 3D baselines on challenging manipulation benchmarks, establishing a new and robust foundation for scalable 3D imitation learning. Project Page: this https URL

---


### 227. [GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://arxiv.org/abs/2604.15284)

**<font color=#1a73e8>作者：</font>** Roni Itkin, Noam Issachar, Yehonatan Keypur 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The efficient spatial allocation of primitives serves as the foundation of 3D Gaussian Splatting, as it directly dictates the synergy between representation compactness, reconstruction speed, and rendering fidelity. Previous solutions, whether based on iterative optimization or feed-forward inference, suffer from significant trade-offs between these goals, mainly due to the reliance on local, heuristic-driven allocation strategies that lack global scene awareness. Specifically, current feed-forward methods are largely pixel-aligned or voxel-aligned. By unprojecting pixels into dense, view-aligned primitives, they bake redundancy into the 3D asset. As more input views are added, the representation size increases and global consistency becomes fragile. To this end, we introduce GlobalSplat, a framework built on the principle of align first, decode later. Our approach learns a compact, global, latent scene representation that encodes multi-view input and resolves cross-view correspondences before decoding any explicit 3D geometry. Crucially, this formulation enables compact, globally consistent reconstructions without relying on pretrained pixel-prediction backbones or reusing latent features from dense baselines. Utilizing a coarse-to-fine training curriculum that gradually increases decoded capacity, GlobalSplat natively prevents representation bloat. On RealEstate10K and ACID, our model achieves competitive novel-view synthesis performance while utilizing as few as 16K Gaussians, significantly less than required by dense pipelines, obtaining a light 4MB footprint. Further, GlobalSplat enables significantly faster inference than the baselines, operating under 78 milliseconds in a single forward pass. Project page is available at this https URL

---


### 228. [AD4AD: Benchmarking Visual Anomaly Detection Models for Safer Autonomous Driving](https://arxiv.org/abs/2604.15291)

**<font color=#1a73e8>作者：</font>** Fabrizio Genilotti, Arianna Stropeni, Gionata Grotto 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The reliability of a machine vision system for autonomous driving depends heavily on its training data distribution. When a vehicle encounters significantly different conditions, such as atypical obstacles, its perceptual capabilities can degrade substantially. Unlike many domains where errors carry limited consequences, failures in autonomous driving translate directly into physical risk for passengers, pedestrians, and other road users. To address this challenge, we explore Visual Anomaly Detection (VAD) as a solution. VAD enables the identification of anomalous objects not present during training, allowing the system to alert the driver when an unfamiliar situation is detected. Crucially, VAD models produce pixel-level anomaly maps that can guide driver attention to specific regions of concern without requiring any prior assumptions about the nature or form of the hazard. We benchmark eight state-of-the-art VAD methods on AnoVox, the largest synthetic dataset for anomaly detection in autonomous driving. In particular, we evaluate performance across four backbone architectures spanning from large networks to lightweight ones such as MobileNet and DeiT-Tiny. Our results demonstrate that VAD transfers effectively to road scenes. Notably, Tiny-Dinomaly achieves the best accuracy-efficiency trade-off for edge deployment, matching full-scale localization performance at a fraction of the memory cost. This study represents a concrete step toward safer, more responsible deployment of autonomous vehicles, ultimately improving protection for passengers, pedestrians, and all road users.

---


### 229. [Benchmarking Optimizers for MLPs in Tabular Deep Learning](https://arxiv.org/abs/2604.15297)

**<font color=#1a73e8>作者：</font>** Yury Gorishniy, Ivan Rubachev, Dmitrii Feoktistov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MLP is a heavily used backbone in modern deep learning (DL) architectures for supervised learning on tabular data, and AdamW is the go-to optimizer used to train tabular DL models. Unlike architecture design, however, the choice of optimizer for tabular DL has not been examined systematically, despite new optimizers showing promise in other domains. To fill this gap, we benchmark \Noptimizers optimizers on \Ndatasets tabular datasets for training MLP-based models in the standard supervised learning setting under a shared experiment protocol. Our main finding is that the Muon optimizer consistently outperforms AdamW, and thus should be considered a strong and practical choice for practitioners and researchers, if the associated training efficiency overhead is affordable. Additionally, we find exponential moving average of model weights to be a simple yet effective technique that improves AdamW on vanilla MLPs, though its effect is less consistent across model variants.

---


### 230. [AnimationBench: Are Video Models Good at Character-Centric Animation?](https://arxiv.org/abs/2604.15299)

**<font color=#1a73e8>作者：</font>** Leyi Wu, Pengjun Fang, Kai Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation has advanced rapidly, with recent methods producing increasingly convincing animated results. However, existing benchmarks-largely designed for realistic videos-struggle to evaluate animation-style generation with its stylized appearance, exaggerated motion, and character-centric consistency. Moreover, they also rely on fixed prompt sets and rigid pipelines, offering limited flexibility for open-domain content and custom evaluation needs. To address this gap, we introduce AnimationBench, the first systematic benchmark for evaluating animation image-to-video generation. AnimationBench operationalizes the Twelve Basic Principles of Animation and IP Preservation into measurable evaluation dimensions, together with Broader Quality Dimensions including semantic consistency, motion rationality, and camera motion consistency. The benchmark supports both a standardized close-set evaluation for reproducible comparison and a flexible open-set evaluation for diagnostic analysis, and leverages visual-language models for scalable assessment. Extensive experiments show that AnimationBench aligns well with human judgment and exposes animation-specific quality differences overlooked by realism-oriented benchmarks, leading to more informative and discriminative evaluation of state-of-the-art I2V models.

---


### 231. [Think in Latent Thoughts: A New Paradigm for Gloss-Free Sign Language Translation](https://arxiv.org/abs/2604.15301)

**<font color=#1a73e8>作者：</font>** Yiyang Jiang, Li Zhang, Xiao-Yong Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many SLT systems quietly assume that brief chunks of signing map directly to spoken-language words. That assumption breaks down because signers often create meaning on the fly using context, space, and movement. We revisit SLT and argue that it is mainly a cross-modal reasoning task, not just a straightforward video-to-text conversion. We thus introduce a reasoning-driven SLT framework that uses an ordered sequence of latent thoughts as an explicit middle layer between the video and the generated text. These latent thoughts gradually extract and organize meaning over time. On top of this, we use a plan-then-ground decoding method: the model first decides what it wants to say, and then looks back at the video to find the evidence. This separation improves coherence and faithfulness. We also built and released a new large-scale gloss-free SLT dataset with stronger context dependencies and more realistic meanings. Experiments across several benchmarks show consistent gains over existing gloss-free methods. Code and data will be released upon acceptance at this https URL.

---


### 232. [RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework](https://arxiv.org/abs/2604.15308)

**<font color=#1a73e8>作者：</font>** Hao Gao, Shaoyu Chen, Yifan Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-level autonomous driving requires motion planners capable of modeling multimodal future uncertainties while remaining robust in closed-loop interactions. Although diffusion-based planners are effective at modeling complex trajectory distributions, they often suffer from stochastic instabilities and the lack of corrective negative feedback when trained purely with imitation learning. To address these issues, we propose RAD-2, a unified generator-discriminator framework for closed-loop planning. Specifically, a diffusion-based generator is used to produce diverse trajectory candidates, while an RL-optimized discriminator reranks these candidates according to their long-term driving quality. This decoupled design avoids directly applying sparse scalar rewards to the full high-dimensional trajectory space, thereby improving optimization stability. To further enhance reinforcement learning, we introduce Temporally Consistent Group Relative Policy Optimization, which exploits temporal coherence to alleviate the credit assignment problem. In addition, we propose On-policy Generator Optimization, which converts closed-loop feedback into structured longitudinal optimization signals and progressively shifts the generator toward high-reward trajectory manifolds. To support efficient large-scale training, we introduce BEV-Warp, a high-throughput simulation environment that performs closed-loop evaluation directly in Bird's-Eye View feature space via spatial warping. RAD-2 reduces the collision rate by 56% compared with strong diffusion-based planners. Real-world deployment further demonstrates improved perceived safety and driving smoothness in complex urban traffic.

---


### 233. [TokenLight: Precise Lighting Control in Images using Attribute Tokens](https://arxiv.org/abs/2604.15310)

**<font color=#1a73e8>作者：</font>** Sumit Chaturvedi, Yannick Hold-Geoffroy, Mengwei Ren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a method for image relighting that enables precise and continuous control over multiple illumination attributes in a photograph. We formulate relighting as a conditional image generation task and introduce attribute tokens to encode distinct lighting factors such as intensity, color, ambient illumination, diffuse level, and 3D light positions. The model is trained on a large-scale synthetic dataset with ground-truth lighting annotations, supplemented by a small set of real captures to enhance realism and generalization. We validate our approach across a variety of relighting tasks, including controlling in-scene lighting fixtures and editing environment illumination using virtual light sources, on synthetic and real images. Our method achieves state-of-the-art quantitative and qualitative performance compared to prior work. Remarkably, without explicit inverse rendering supervision, the model exhibits an inherent understanding of how light interacts with scene geometry, occlusion, and materials, yielding convincing lighting effects even in traditionally challenging scenarios such as placing lights within objects or relighting transparent materials plausibly. Project page: this http URL

---


### 234. [Bidirectional Cross-Modal Prompting for Event-Frame Asymmetric Stereo](https://arxiv.org/abs/2604.15312)

**<font color=#1a73e8>作者：</font>** Ninghui Xu, Fabio Tosi, Lihui Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional frame-based cameras capture rich contextual information but suffer from limited temporal resolution and motion blur in dynamic scenes. Event cameras offer an alternative visual representation with higher dynamic range free from such limitations. The complementary characteristics of the two modalities make event-frame asymmetric stereo promising for reliable 3D perception under fast motion and challenging illumination. However, the modality gap often leads to marginalization of domain-specific cues essential for cross-modal stereo matching. In this paper, we introduce Bi-CMPStereo, a novel bidirectional cross-modal prompting framework that fully exploits semantic and structural features from both domains for robust matching. Our approach learns finely aligned stereo representations within a target canonical space and integrates complementary representations by projecting each modality into both event and frame domains. Extensive experiments demonstrate that our approach significantly outperforms state-of-the-art methods in accuracy and generalization.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
