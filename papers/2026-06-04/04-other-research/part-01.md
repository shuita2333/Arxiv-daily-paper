# 📦 其他研究 | 2026年06月04日

> 本类共 **312** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-312](./part-07.md)

---

### 1. [IdiomX A Multilingual Benchmark for Idiom Understanding, Retrieval, and Interpretation](https://arxiv.org/abs/2606.02584)

**<font color=#1a73e8>作者：</font>** Ayman Ali Sharara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Idiomatic expressions remain a persistent challenge for natural language processing because their meanings are often non-compositional, context-dependent, and difficult to align across languages. Existing idiom resources are often limited in scale, contextual diversity, or multilingual coverage, restricting their utility for modern language models. We introduce IdiomX, a large-scale multilingual benchmark for idiom understanding, retrieval, and interpretation, constructed through a reproducible multi-stage pipeline combining lexical resource extraction, large-scale normalization, controlled large language model enrichment, and structured validation. The resulting dataset contains over 190K contextualized examples spanning 12K+ idioms, with aligned English, Arabic, and French semantic representations, idiomatic and literal usage labels, and rich linguistic metadata. Building on this resource, we define a unified four-task benchmark covering idiom detection, context-to-idiom retrieval, Arabic-to-English idiom retrieval, and idiom interpretation, extending evaluation from figurative recognition to semantic grounding and explainable meaning retrieval. Experiments show that contextual transformer models substantially improve idiom detection, while hybrid retrieval and reranking architectures significantly strengthen both monolingual and cross-lingual idiom retrieval. Results further demonstrate that idiom interpretation can be effectively modeled as a semantic retrieval task, introducing interpretability as a complementary benchmark dimension. Overall, IdiomX provides a scalable benchmark for studying idiomatic language as a progression from detection to retrieval and semantic interpretation, and offers a modular framework extensible to additional languages and figurative reasoning tasks

---


### 2. [Human-in-the-Loop Contextual Bandits for Short-Term Rental Dynamic Pricing: Structural Equivalence of Historical Warm-Up and Approval-Gated Live Learning](https://arxiv.org/abs/2606.02595)

**<font color=#1a73e8>作者：</font>** Oleg Miroshnichenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic pricing in short-term rental (STR) markets presents a distinctive challenge for online learning algorithms: pricing decisions carry significant financial risk, operators require explainability, and market feedback is sparse (one booking outcome per listed night). We introduce the Human-in-the-Loop Gated Bandit (HITL-GB) framework, in which a contextual bandit algorithm generates price recommendations but a human agent retains authority to accept, modify, or reject each recommendation before it is applied. We show that under this approval constraint, historical pricing data -- collected under a prior deterministic policy -- is structurally equivalent to on-policy warm-up data for initialising the bandit's posterior, bypassing the weeks-to-months cold-start period that renders pure online bandit learning impractical in sparse-feedback markets. We formalise the approval-gated reward signal, derive a regularised ridge-regression warm-up procedure from historical episodes, and validate the approach on real STR production data (anonymised urban market, 2 rooms, April 2022 -- April 2026, 1,461 nightly pricing episodes). Our warm-up procedure compresses effective cold-start from ~150 episodes to ~30 episodes when initialising agents from the Hierarchical Factored Thompson Sampling (HF-TS) family. We further argue that the structural equivalence result is domain-agnostic: any high-stakes domain where human approval is legally or operationally required -- including clinical drug dosing, credit origination, content moderation, and radiological diagnosis -- satisfies the same conditions and benefits from the same warm-up strategy. In regulated industries, mandatory human oversight is thus a statistical asset rather than a deployment constraint.

---


### 3. [Spectral Asymptotics of Neural Network Loss Landscapes: An Exact Decomposition of the Curvature Exponent](https://arxiv.org/abs/2606.02596)

**<font color=#1a73e8>作者：</font>** Anherutowa Calvo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The curvature exponent $\alpha$ in $h_k \propto \sigma_k^\alpha$ -- governing how Hessian eigenvalues scale with gradient singular values -- varies systematically across layer types ($\alpha \approx 2$ for convolutions, $\approx 1$ for transformer attention, $< 1$ for MLP up-projections). Why? We prove the Spectral Alignment Decomposition: $\alpha = 2 + d\log\Phi_k / d\log\sigma_k$, where $\Phi_k$ measures alignment between Kronecker factor eigenbases and gradient singular directions. This reduces "why does $\alpha$ vary?" to a geometric question we answer for LayerNorm, residual connections, and softmax heads. The decomposition implies a spectral transfer identity $s = \alpha\gamma$ linking curvature exponent, effective gradient rank-decay $\gamma$, and Hessian decay exponent $s$. The identity is algebraic; its empirical content is that $\alpha$ and $\gamma$, fit on independent data (HVPs vs. SVD), recover $s$ to ~2% median error across 93 layers, five architectures, and three datasets -- with no free parameters. A zeta-function bound on participation ratio shows curvature concentrates onto effectively one direction per layer. As a proof of concept, we derive the architecture-adaptive preconditioner $T(\sigma;\alpha)$ and show that Spectral Newton -- implementing $T$ in the gradient singular basis -- outperforms AdamW on vision benchmarks where $\alpha \approx 2$.

---


### 4. [Making Brain-Computer Interfaces More Secure](https://arxiv.org/abs/2606.02597)

**<font color=#1a73e8>作者：</font>** Md Fahimul Kabir Chowdhury, Gahangir Hossain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The development of brain-computer interfaces (BCIs) based on electroencephalograms (EEGs) has advanced significantly mainly to machine learning. Although the majority of earlier research has been on increasing classification accuracy, relatively little focus has been placed on security and robustness. According to recent research, EEG-based BCIs are susceptible to adversarial attacks, which can cause misdiagnosis due to minute, well-crafted disturbances. Evaluating model robustness against such perturbations is therefore critical for ensuring reliable deployment. In this study, we propose a lightweight custom Convolutional Neural Network (CNN) architecture to investigate adversarial robustness in EEG-based BCIs. The suggested method is assessed using two EEG datasets and contrasted with three novel CNN models tailored to EEG, namely EEGNet, DeepConvNet, and SleepEEGNet, under gradient-based adversarial attack scenarios. According to experimental findings, the suggested model continuously performs better in classification under adversarial perturbations compared to baseline models, indicating improved robustness. These findings highlight the potential of lightweight architectures for enhancing the reliability of EEG-based BCI systems under adversarial conditions.

---


### 5. [Assessing Region-Level EEG Contributions to Cognitive Workload Prediction](https://arxiv.org/abs/2606.02598)

**<font color=#1a73e8>作者：</font>** Jacob Wong, Sohan Singh, Prannaya Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate and generalizable estimation of cognitive workload from electroencephalography (EEG) is critical for human-centered and safety-critical systems. Although EEG is widely used for workload assessment, the consistency of region-level EEG contributions across tasks, datasets, and subjects remains unclear. This paper presents a region-level evaluation framework for EEG-based workload prediction in which models are trained and evaluated using features extracted exclusively from electrodes belonging to anatomically defined scalp regions. We perform a large-scale analysis across four publicly available EEG workload datasets spanning diverse task demands, recording hardware, and electrode montages. Region importance is quantified using a model-agnostic, performance-based approach under both mixed-subject and subject-independent evaluation protocols, with results aggregated using a rank-based strategy to ensure robustness across experimental configurations. Across all datasets and subject-independent evaluations, frontal electrode groups outperform the full-scalp baseline by approximately 15-20% in relative rank position while using substantially fewer electrodes. Fronto-central regions exhibit the most stable predictive utility, whereas posterior and occipital regions contribute less consistently across experimental conditions. These findings indicate that workload-relevant EEG information is most consistently retained within frontal and fronto-central electrode groups, supporting the design of efficient and generalizable EEG-based workload monitoring systems.

---


### 6. [Testing the Test: Score-Direction Instability in Class-Split Anomaly Detection](https://arxiv.org/abs/2606.02601)

**<font color=#1a73e8>作者：</font>** Alejandro Ascarate, Leo Lebrat, Rodrigo Santa Cruz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Within-dataset class-split evaluation is widely used as a proxy for fully unconditional out-of-distribution anomaly detection. We show that this protocol can become ill-posed when the held-out anomaly class overlaps the normal mixture in representation space. In this regime, anomaly scores may collapse toward chance or even invert, and the preferred score direction can depend on the unknown anomaly class. We introduce a simple training-free diagnostic, neighborhood class leakage, and show that it predicts score-direction instability across Fashion-MNIST, CIFAR-10, and Imagenette, in both pixel and VAE latent spaces. Our results suggest that class-split AD benchmarks should be treated as geometry-dependent stress tests rather than unconditional evidence of anomaly-detection ability.

---


### 7. [Graph Mamba Survival Analysis Based on Topology-Aware ordering](https://arxiv.org/abs/2606.02602)

**<font color=#1a73e8>作者：</font>** Yuanfang Chen, Peiqiang Yan, Yuntao Shou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In computational pathology, Whole Slide Images (WSIs) survival analysis is crucial for patient prognosis assessment, but it faces multiple technical challenges. Although the Transformer captures long-range dependencies through its self-attention mechanism, its $O(N^2)$ time complexity causes a severe computational bottleneck in large-scale WSIs graph structures. The Mamba model breaks through the Transformer's computational bottleneck with linear complexity. But, owing to Mamba's high sensitivity to the order of input data, traditional node sorting methods in Graph Mamba, such as those based on node degree or subgraph size, fail to adequately account for the topological connectivity of graph data. This inadequacy consequently restricts the performance of Mamba's sequential modeling. Moreover, its unidirectional architecture cannot leverage the bidirectional spatial structure of images. To address these challenges, this paper proposes a novel Graph Mamba survival analysis framework based on topology-aware ordering (TopoMamSurv) to adapt to the sequential sensitivity of Mamba. Our visualization experiments further confirmed that the nodes extracted through the topology-aware ordering (TAO) strategy indeed exhibit higher similarity. Furthermore, we designed a bidirectional Mamba module and integrated a Graph Convolutional Network (GCN) to achieve bidirectional spatial context modeling of images, forming a hierarchical feature learning architecture for "local aggregation - global capture." This framework effectively reconciles the contradiction between long-range dependency modeling, computational efficiency, and spatial structure utilization in WSIs analysis through its systematic design of TAO, bidirectional semantic modeling, and hierarchical feature fusion. This framework has been validated for its comprehensive performance advantage on five TCGA datasets.

---


### 8. [COD10K-C: Benchmarking Robustness of Camouflaged Object Detection Under Natural Image Corruptions](https://arxiv.org/abs/2606.02603)

**<font color=#1a73e8>作者：</font>** Arafat Hossain Sayem  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflaged object detection has improved substantially, but most standard benchmarks evaluate models only on clean images. This is not realistic because real cameras often capture blur, sensor noise, weather effects, and compression artifacts. We present COD10K-C, a corruption robustness benchmark based on COD10K. It includes 8 corruption types and 5 severity levels, giving 40 conditions and 81,040 evaluation pairs in total. We evaluate three popular camouflaged object detection models, SINet-v2, PFNet, and ZoomNet, as well as a lightweight model called RobustCODLite. All models show clear performance drops on corrupted images. Motion blur and Gaussian blur cause the largest drops, with SINet-v2 losing 18.5 Dice points under motion blur. Brightness and fog are less harmful. RobustCODLite uses corruption augmentation, a frequency-prior branch, and an uncertainty-consistency loss. It retains 92.3% of its clean Dice score under corruption, compared with 87.7% for SINet-v2, 84.8% for ZoomNet, and 84.1% for PFNet. On the hardest corruptions, RobustCODLite matches or outperforms models that perform better on clean data. We will release the COD10K-C GitHub repository to support future research in robust camouflaged object detection.

---


### 9. [Cross-Modal Contrastive Learning of ECG and Angiography Representations for Severe Stenosis Classification](https://arxiv.org/abs/2606.02605)

**<font color=#1a73e8>作者：</font>** Nikola Cenikj, Özgün Turgut, Alexander Müller 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coronary artery stenosis is a common cardiovascular disease, with severe, untreated cases posing significant risks of heart attack. Although coronary (X-ray) angiograms remain the standard for stenosis diagnosis, they are invasive, time- and resource-intensive, and therefore only performed on patients with a high probability of disease based on symptoms and prior clinical tests. However, a subset of patients, especially those without symptoms, may remain undiagnosed. Detecting indications of stenosis from ECGs, which are fast, cheap, non-invasive, and thus routinely acquired even in asymptomatic patients, would support early diagnosis. However, as no reliable stenosis-specific signal has been identified in ECGs, they can not currently be used for stenosis risk stratification. To address this, we introduce StenCE, a pretraining framework, allowing stratification of patients based on features derived directly from ECGs. Evaluations across varying stenosis severity thresholds and additional ECG disease classification tasks demonstrate consistent performance improvements across different ECG encoders, outperforming previous work. The obtained models successfully detect signals for stenosis diagnosis in ECGs and are the first to achieve high performance in severe stenosis classification. The source code is available at this https URL.

---


### 10. [Geometry-Aware Tabular Diffusion](https://arxiv.org/abs/2606.02607)

**<font color=#1a73e8>作者：</font>** David Turtora Zagardo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular synthesis is critical for privacy-preserving sharing and augmentation, yet diffusion models rely on implicit mechanisms to capture inter-column relationships. We introduce Geometry-Aware Tabular Diffusion (GATD), which augments tabular diffusion denoisers with pairwise angles and lengths computed from column value differences and used as inputs and auxiliary targets. Our MLP instantiation achieves state-of-the-art benchmark performance while using 3.5x fewer parameters on average (up to 25x for classification tasks): on ten datasets, it wins 8/10 Shape, 7/10 Trend, and 9/10 downstream utility (F1/RMSE), reducing Shape and Trend error by 27% and 20%. Default loss weights transfer to GNN and Transformer denoisers, improving Shape on 27/30 and Trend on 25/30 architecture-dataset cells. A matched ablation shows supervision (not extra inputs or capacity) drives the gain. This shows explicit relational supervision is a portable inductive bias for tabular diffusion.

---


### 11. [Pruning Deep Neural Networks via the Marchenko--Pastur Distribution](https://arxiv.org/abs/2606.02608)

**<font color=#1a73e8>作者：</font>** Leonid Berlyand, Theo Bourdais, Houman Owhad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a Marchenko--Pastur (MP) random-matrix approach to pruning deep neural networks with very small post-pruning fine-tuning budgets. The main practical contribution is accuracy retention under short calibration and fine-tuning schedules, rather than a long post-pruning reoptimization pipeline. The theory gives deterministic data-path certificates: if the removed component $R$ has small propagated logit effect $L_s \| R \psi_1(s) \|_\infty$, pruning decreases an elastic-net objective and preserves samples whose dense margin exceeds twice the perturbation. The zero-budget case gives perfect pruning; a prune--restore extension models weight restoration inside a fixed sparse-execution pattern; and an additive $L_2$-regularized model shows admissible random-like components vanish at the training limit, with persistent spikes stabilizing as the MP bulk collapses. Under iid-Gaussian sufficient conditions, the fitted MP edge $\sigma_+$ gives a high-probability layerwise budget signal.
On ImageNet-1k, after only three distillation epochs, ViT-B/16 $2{:}4{+}$ToMe reaches $83.41\%$ top-1 ($-1.70$ pp from dense) at $59.81\%$ sparse-execution MAC reduction, with $1.388\times$ best-observed A40 native-$2{:}4$ backend speedup for the same checkpoint and ToMe graph; a separate no-ToMe A100 endpoint gives $2.705\times$. At structured sparsity, ViT-B/16 $6{:}12$ reaches $83.74\%$, ViT-L/16 $8{:}16$ dense+permutation reaches $85.33\%$ ($-0.51$ pp), and ConvNeXtV2-Base $12{:}16$ reaches $86.35\%$ ($-0.37$ pp). For CNNs, ResNet50 $8{:}16$ dense+permutation reaches $75.87\%$ ($-0.26$ pp), and ResNet152d CAST-conv+permutation reaches $81.33\%$ ($-1.53$ pp) at ${\sim}50\%$ MAC accounting with a $1.62\times$ A40 im2col$+2{:}4$ sparse-GEMM audit.

---


### 12. [Building Better Activation Oracles](https://arxiv.org/abs/2606.02609)

**<font color=#1a73e8>作者：</font>** Jan Bauer, Celeste De Schamphelaere, Adam Karvonen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation Oracles (AOs) are promising methods for interpreting residual stream activations. However, current AOs face important issues, such as hallucinations and vagueness. Additionally, text-inversion confounds make them hard to evaluate. To this end, we improve the Activation Oracle (AO) training regime in four ways: training on on-policy rollouts, improving the conversational dataset, feeding more layers and an improvement to the injection formula. The capability improvements are marginal, but quality of life improvements are quite substantial. In addition, we open source the first comprehensive evaluation suite for AO quality, which we call AObench. Overall, we hope that our work sets a foundation that helps improve AOs and other models in the paradigm of scalable, end-to-end interpretability.

---


### 13. [MultiTurnPSB: Evaluating Multi-Turn Jailbreak Attacks an dClassifier-Based Defenses for Medical AI Safety](https://arxiv.org/abs/2606.02630)

**<font color=#1a73e8>作者：</font>** Anushka Sheoran, Yiduo Hao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Patient-facing medical chatbots are commonly evaluated on single-turn prompts, yet real users push back after refusals, add urgency, and invoke authority. We introduce MultiTurnPSB, a four-turn adversarial extension of PatientSafetyBench, and evaluate GPT-4.1-mini under fixed template, template-adaptive, and live adversarial attacks. Unsafe responses rise from 35% to nearly 80% by Turn 4 under live attack. Under the same adversary, GPT-4.1-mini and Claude Sonnet 4.5 are statistically indistinguishable at baseline but diverge to a 19x gap by Turn 4, a difference invisible to single-turn evaluation. We characterize four degradation trajectory signatures and identify a two-element attack formula responsible for most catastrophic failures. A lightweight input-side classifier reduces Turn 4 unsafe responses by 52 percentage points despite severe accuracy degradation, but the 45% false alarm rate on benign queries is the primary deployment constraint. A methodological finding also emerges: Claude Sonnet refused to generate adversarial messages in over half of late-turn conversations despite explicit red team framing, suggesting safety training may generalize to the attacker role.

---


### 14. [A New Framework for Cybersecurity Refusals in AI Agents](https://arxiv.org/abs/2606.02644)

**<font color=#1a73e8>作者：</font>** Eliot Krzysztof Jones, Mateusz Dziemian, Matt Fredrikson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic scaffolds have dramatically improved LLM performance on complex, long-horizon tasks, yielding both broad benefits and amplified risks in domains like cybersecurity. Existing benchmarks for AI agents in cybersecurity focus mainly on measuring proficiency--how effectively agents can complete offensive security tasks--but neglect a critical question: when and how should agents refuse harmful requests? We present the first framework for establishing refusal boundaries in offensive security contexts. Our framework defines (1) principled criteria for when tasks should be refused, (2) categories of tasks that warrant refusal, and (3) evaluation methodology for measuring agent robustness under both benign and adversarial conditions. We apply this framework to assess how current LLM-powered agents adhere to appropriate refusal boundaries across a range of web-based offensive security scenarios, finding that 6 of 8 frontier models tested show near-zero refusal rates, with only 2 models (GPT-5.2 and GPT-5.1 Codex) demonstrating any meaningful refusal behavior.

---


### 15. [Regime-Arrival Uncertainty in Generalization Bounds under Distribution Shift](https://arxiv.org/abs/2606.02657)

**<font color=#1a73e8>作者：</font>** Prince Poudel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The standard generalization bounds assume that the training and deployment distributions are the same, or are static, and don't consider regime switching environments where the ratio of calm vs crisis states is different. This paper proposes a framework that generalizes regime-aware models by quantifying the extra risk due to regime composition mismatch, when distribution shifts are Markov-switching. We obtain an exact decomposition, separating regime mismatch from regime sensitivity; we extend the bound to beta-mixing data using the effective sample size corrected for the spectral gap; and we show a minimax lower bound for synthetic data and on 25 years of global equity indices. The proposed penalty is an ex post realized generalization gap, whereas the training-only estimator does not show significant correlation: the feature geometry of crises can be detected, but not the temporal arrival. Thus, the framework is not a forecast machine. Forecasting the composition of the future regime is an open question in the rare cases of regime change.

---


### 16. [Improvise, Adapt, Overcome: An On-The-Fly Multifidelity Algorithm for Efficient Machine Learning](https://arxiv.org/abs/2606.02662)

**<font color=#1a73e8>作者：</font>** Vivin Vinod, Peter Zaspel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning has accelerated quantum chemistry but is hindered by the prohibitive cost of generating high fidelity training data. Multifidelity machine learning (MFML) mitigates this overhead by systematically combining abundant low fidelity data with sparse high fidelity data. In spite of its success, standard MFML schemes rely on pre-defined scaling factors to determine sparse data ratio across fidelities, often generating redundant multifidelity data resulting in a loss of efficiency. Here, we introduce an adaptive on-the-fly multifidelity framework for machine learning that autonomously determines training dataset composition. By dynamically querying training samples at each fidelity, the algorithm saturates model accuracy at lower fidelities before moving up to more expensive reference calculations. We benchmark the novel adaptive-MFML across diverse chemical properties including the computational chemistry gold standard coupled cluster energies, and the more chemically challenging excitation energies. In our numerical experiments we show that our adaptive algorithm reduces data generation costs by up to a factor of 30 compared to single fidelity methods and improves upon standard MFML by up to a factor of 5. The mitigation of data redundancy establishes a high-accuracy low-cost pathway for sustainable cost-aware machine learning in quantum chemistry.

---


### 17. [AdaWeather: Adaptively Mixing Probabilistic Weather Forecasts with Logarithmic Regret](https://arxiv.org/abs/2606.02663)

**<font color=#1a73e8>作者：</font>** Saptarishi Dhanuka, Sarvesh Iyer, Manmeet Singh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in machine learning have produced probabilistic weather forecasting models comparable to state-of-the-art numerical weather predictors. But no model consistently dominates spatio-temporally, and relative performance is highly context-dependent. This motivates adaptive methods for combining multiple forecasts to obtain improvements and robustness. While combined forecasts have been proposed in the literature, these are achieved either through supervised learning or through prediction with expert advice methods. We introduce AdaWeather, an adaptive framework that combines many probabilistic forecasts using both machine learning as well as mixture of experts to arrive at a unified improved probabilistic forecast. While traditional expert methods develop the regret bounds with respect to the best single expert in hindsight, we extend the algorithm and analysis to show our method has logarithmic regret compared to the best static mixture of experts in hindsight. Empirically, we focus on forecasting temperature, and observe improvements over existing methods.

---


### 18. [Anomalies in Multivariate Time Series Benchmarks Are Mostly Univariate](https://arxiv.org/abs/2606.02670)

**<font color=#1a73e8>作者：</font>** Marc Pinet, Julien Cumin, Samuel Berlemont 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many recent multivariate time series anomaly detection (MT-SAD) models incorporate cross-channel modeling, under the implicit assumption that the structure of anomalies may be spread across multiple channels. We evaluate this assumption on eight widely used public benchmarks by introducing a per-segment diagnostic framework that flags, for each labeled anomaly, whether at least one channel deviates individually from its normal history, whether the cross-channel correlation structure changes, or both. The framework shows that no crosschannel rupture occurs without an accompanying univariate deviation across a range of reasonable thresholds. A complementary metric also reveals that on six of the eight benchmarks, at least half of the labeled anomaly segments deviate univariately on 79% to 100% of their timesteps, reaching 100% on three of these datasets. To verify that our framework captures cross-channel structure when present, we construct synthetic data of phase-shifted sinusoidal channels with shared noise. Each anomalous segment is altered through one of two channelwise corruptions that preserve the per-channel marginal distribution while breaking cross-channel structure, and our framework correctly characterizes these segments as cross-channel-only. On these data, channel-dependent (CD) models successfully exploit the cross-channel signal whereas channel-independent (CI) ones fail. The CI/CD comparison of a recent SOTA detector on real benchmarks further confirms that CD modeling brings no measurable gain. We conclude that current MTSAD benchmarks are unsuitable for validating cross-channel modeling capabilities, and we call for the development of more structurally diverse evaluation sets. The code for this study is publicly available.

---


### 19. [Aligning Data-Driven Predictors with Allocation: A Decision-Focused Approach to Survival Analysis](https://arxiv.org/abs/2606.02671)

**<font color=#1a73e8>作者：</font>** Itai Zilberstein, Ioannis Anagnostides, Tuomas Sandholm  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning predictors have become essential tools for guiding automated decision making. However, a major misalignment persists: predictive models are typically optimized in terms of standard statistical metrics in isolation from the algorithmic tasks they inform. We highlight this incongruity in the high-stakes domain of organ allocation by demonstrating that any algorithm relying on (even highly accurate) survival predictors optimized for standard metrics -- such as the Concordance index (C-index) -- can yield arbitrarily poor outcomes when used for allocation, failing to guarantee utility better than a uniform random selection. To bridge the gap between survival analysis and policy optimization, we introduce a decision-focused learning approach based on optimizing normalized discounted cumulative gain (NDCG), a mainstay metric in information retrieval. We establish the utility of NDCG in survival analysis by proving that it translates to guarantees on the performance of allocation. Empirically, we propose a bootstrapping approach to optimize the NDCG of existing survival models. Unlike prior work, we also address the challenge of right censorship when evaluating ranking. On historical heart transplant data from the US, our method dramatically boosts the NDCG of baseline models by 50-100%, which translates to tens of thousands of additional life years gained annually when deployed for transplant allocation. We anticipate that our framework will find broader applications in decision making with predictions.

---


### 20. [Locality Does Not Imply Reachability: Boundary Repair in Block-Sparse Causal Attention](https://arxiv.org/abs/2606.02680)

**<font color=#1a73e8>作者：</font>** Zhibo Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse causal attention is usually described by sequence locality: nearby tokens should remain easy to access, while distant tokens may be dropped to reduce cost. This paper studies a mismatch between sequence locality and attention-graph reachability. In fixed block causal attention, two adjacent tokens can be disconnected in the attention graph at every depth. We formalize this boundary artifact through structural dependency sets: if every attention layer uses the same fixed block causal mask and all remaining operations are positionwise, a target representation can depend only on tokens in its own block prefix. This yields an architecture-level boundary-copy separation for a constructed K-way boundary-copy distribution, with top-1 accuracy upper bound 1/K and expected cross-entropy lower bound log K. We then derive phase-conditioned coverage functions showing that reachability depends on both source-target distance and the target's offset within its block. These coverage laws predict when a sparse pattern should fail, when a repair can help, and why sliding-window attention and boundary repair are not interchangeable. Boundary Bridge Attention is treated as a constructive witness: it preserves the fixed block path and adds zero-additional-parameter auxiliary causal edges near block boundaries using shared projections. Controlled 1024-token experiments show that gains concentrate in coverage-aligned diagnostics. As secondary external-validity evidence, a fixed-checkpoint 8K-token Qwen2.5-7B probe shows the same coverage-incomparability pattern. The contribution is a theory-guided diagnostic framework for locality-reachability mismatch in block-sparse causal attention, together with phase-conditioned coverage analysis and a minimal constructive repair.

---


### 21. [Filter, Then Reweight: Rethinking Optimization Granularity in On-Policy Distillation](https://arxiv.org/abs/2606.02684)

**<font color=#1a73e8>作者：</font>** Yuying Li, Leqi Zheng, Yongzi Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-Policy distillation (OPD) in large language models is shifting from full-trace KL supervision toward more selective training paradigms. Recent OPD methods increasingly focus on selecting which trajectories to learn from, which tokens are most informative, and which supervision signals are most reliable. Motivated by this trend, we rethink optimization granularity of OPD and propose \fireicon\ FiRe-OPD (Filter, then Reweight), which jointly adjusts supervision signals at both trajectory and token levels. In details, FiRe-OPD first filters trajectories to remove low-quality rollout samples, and then applies soft reweighting within the retained trajectories to emphasize informative tokens. Compared with hard token selection, FiRe-OPD leverages a soft-weighting mechanism to effectively mitigate information loss and enhance optimization stability, thereby achieving finer-grained OPD optimization. We validate the effectiveness of FiRe-OPD across strong-to-weak, single-teacher, and multi-teacher settings, and demonstrate its superiority over recent token-level OPD methods ( (e.g., +6.25 on AIME 2024 in strong-to-weak, +18.81 on Miner in multi-teacher). Our code is available at this https URL.

---


### 22. [AVTrack: Audio-Visual Tracking in Human-centric Complex Scenes](https://arxiv.org/abs/2606.02724)

**<font color=#1a73e8>作者：</font>** Yaoting Wang, Yun Zhou, Zipei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual speaker tracking aims to localize and track active speakers by leveraging auditory and visual cues, enabling fine-grained, human-centric scene understanding. This capability is essential for real-world applications such as intelligent video editing, surveillance, and human-computer interaction. However, existing datasets are largely limited to simple or homogeneous audio-visual scenes with coarse annotations. Such oversimplified settings bias evaluation toward static audio-visual co-occurrence, rather than rigorously assessing robust spatiotemporal modeling and cross-modal reasoning in complex, dynamic scenes. To address these limitations, we introduce AVTrack, a human-centric audio-visual instance segmentation (AVIS) dataset designed for dynamic real-world scenarios. AVTrack features diverse and challenging conditions, including camera motion, visual occlusions, and position changes. Evaluations of representative AVIS methods on AVTrack reveal substantial performance degradation, establishing AVTrack as a challenging benchmark for robust human-centric audio-visual scene understanding in complex environments. We further provide a simple yet effective baseline to facilitate future research. Project website: this https URL

---


### 23. [On the Persistent Effects of Lexicality in Large Language Mod](https://arxiv.org/abs/2606.02750)

**<font color=#1a73e8>作者：</font>** Hammad Rizwan, Muhammad Umair Haider, Nishant Subramani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Representations extracted from large language models (LLMs) play an important role in many downstream applications. However, the structure of these representations is often influenced by lexical overlap rather than semantic content. Our understanding of the relationship between this lexical influence and semantic content, and its implications for downstream tasks, remains limited. In this work, we investigate representations to quantify the effect of lexical overlap relative to semantic content. We consider several adversarial semantic stress tests and further connect our findings to the information theory perspective. We find that lexical influence extends across the depth of models, consistently across architectures, training regimes, and objective functions, including the models trained for semantic similarity. Moreover, we observe a mid-depth region in which both lexical and semantic signals degrade simultaneously, indicating a transitional regime where representations are poor for both surface form and meaning. We further demonstrate the effect of lexical influence on downstream uses of LLMs using summarization and model editing as a case study.

---


### 24. [$Ψ$-Bench: Evaluating Persona-Sensitive Influencing in Persuasive Dialogues](https://arxiv.org/abs/2606.02754)

**<font color=#1a73e8>作者：</font>** Peixuan Han, Hongyi Du, Jiayu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalization is a crucial capability of modern language agents. However, current research primarily positions personalized agents as passive responders to user preferences, limiting their ability to interact with users and provide suggestions or guidance proactively. To systematically evaluate such proactive personalization in realistic interactions, we propose $\Psi$-Bench, a benchmark for assessing LLMs' ability to influence realistic users through conversation. We design three real-world interaction scenarios that involve persuasion in $\Psi$-Bench, and endow simulated clients with personal characteristics through explicit user profiles derived from dialogue histories. We evaluate 10 frontier LLMs on $\Psi$-Bench and find that while most models can produce coherent and reasonable arguments, even state-of-the-art models still leave considerable room for improvement in persuasion. We also find that providing access to client profiles yields an average performance gain of 18.24\%, highlighting the importance of user-specific information for effective persuasion. Overall, our work highlights persona-sensitive influencing as a challenging yet practical direction for evaluating and developing more proactive personalized LLM agents. Codes are available at: this https URL.

---


### 25. [Binary Road Surface Classification Using Machine Learning on Production Vehicle Signals During Cruising](https://arxiv.org/abs/2606.02762)

**<font color=#1a73e8>作者：</font>** Vishal Hariharan, Salar Basiri, Kanwar Bharat Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge of real-time road slipperiness, or even better, a refined estimate of peak grip potential, is a critical input for vehicle warning and intervention control systems. Typically, friction is estimated through dynamics-based recursive estimators by calculating the slip slope; however, its efficacy is heavily constrained by the vehicle dynamic scenario. When the vehicle is cruising and there is little to no slip, these methods become ineffective due to the inability of present-day production-grade sensors, such as wheel speed sensors, and methods to either measure or accurately estimate micro slip, which is crucial for distinguishing different surfaces. To address this challenge, the correlation between vehicle signals and road surface condition during cruising needs to be uncovered using machine learning. In this paper, a feature-based framework and an end-to-end data-driven framework are used to correlate the statistics of vehicle dynamics behavior with the condition of the road surface and perform binary classification into grip, dry or damp, and slip, snow or ice, conditions. A sliding-window approach is adopted to batch a short buffered window of wheel speeds, wheel torques, longitudinal acceleration, steering angle, and yaw rate, which are fed into a machine learning module for predicting the road state. Validation results on public-road data show scenarios where the data-driven method identifies the road surface correctly even during cruising, showing promise for accurate data-driven friction-related state estimators in the field of tire and vehicle dynamics.

---


### 26. [InquiryBits: Sharing AI Conversation Traces to Support Collaboration Within Trust Boundaries](https://arxiv.org/abs/2606.02763)

**<font color=#1a73e8>作者：</font>** Caitlin Morris, Pattie Maes  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI chat tools are shifting problem-solving and brainstorming conversations away from colleagues and into private AI interactions, reducing the shared awareness that supports team coordination. We introduce InquiryBits, a system that shares minimal summaries of AI conversations within configurable trust boundaries, separating AI-only analysis from human-visible sharing. In a study with 80 professionals, we find that people are broadly willing to share these traces to support collaboration and avoid duplicating work - but only within bounded groups. Comfort drops sharply as audience expands beyond close teams; the level of detail shared matters less than who can see it, with a preference for more detail over less within trusted groups. These findings suggest that trust boundaries, more than information granularity, may be the most impactful design parameter.

---


### 27. [From Local Training to Large-Scale Mapping: A Comparative Assessment of Machine Learning and Deep Learning for Transferable Satellite-Derived Bathymetry](https://arxiv.org/abs/2606.02764)

**<font color=#1a73e8>作者：</font>** Hsiao-Jou Hsu, Joachim Moortgat  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite-derived bathymetry (SDB) from multispectral imagery is cost-effective but scales poorly across regions, especially in optically complex coastal environments. We evaluate machine learning and deep learning for transferable SDB over the 0-20 m depth range using Sentinel-2 imagery. A Random Forest baseline and four CNNs (ResNet-50, ResNet-101, EfficientNet-B4, ConvNeXt-Large) are trained on Pratas Island and selected Great Barrier Reef regions, then evaluated on spatially independent intra- and cross-regional test areas. Preserving spatial continuity during training, by keeping contiguous reef blocks rather than random patches, is the single most impactful design choice; we further introduce a Smooth Weight Function (SWF)-weighted RMSE loss that emphasizes near-surface depths. With these choices, intra-regional RMSE ranges from 1.15 to 1.92 m over 0-20 m and is as low as 0.26 m for depths <= 3 m. Random Forest degrades sharply under cross-regional transfer (RMSE 1.53 m -> 2.99-3.78 m), while the deep models stay more robust (2.46-2.98 m). On the public MagicBathyNet aerial-RGB benchmark (0-16 m) the proposed networks reach 0.19-0.22 m RMSE, outperforming a U-Net baseline and a task-specific transformer architecture with substantially fewer parameters. We further exploit multi-temporal repeat imagery: training on it broadens diversity, and median-aggregating predictions across passes at inference reduces noise from changing sun angles, atmospheric conditions, water properties, and tides. We release optimized architectures and pretrained weights to enable scalable transfer to new sites.

---


### 28. [AURA: Action-Gated Memory for Robot Policies at Constant VRAM](https://arxiv.org/abs/2606.02775)

**<font color=#1a73e8>作者：</font>** Josef Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The KV-cache is the right memory for datacenters but the wrong memory for robots. Datacenter inference batches many short requests and resets them, amortizing an attention cache across a crowd. Embodied agents instead run one long, non-resetting episode on bandwidth-limited edge hardware, where high-bandwidth memory and flash are scarce, flash has finite write endurance, and memory writes rather than compute can become the binding constraint.
AURA-Mem (Action-Utility Recurrent Adaptive Memory) targets this regime. It wraps a frozen vision-language-action backbone with a constant-size recurrent memory and a learned gate that writes only when the current observation would change the next action: memory that knows when to stay silent. Unlike reconstruction-based memory, the gate is trained directly against a closed-loop action-error signal. Its inference state is fixed at 4,224 bytes regardless of horizon, while a KV-cache grows to 6,061 times larger at 100,000 steps.
On a controlled synthetic benchmark, AURA-Mem matches the best O(1) baseline in accuracy while using 5.19-6.13 times fewer writes, and up to 9.19 times fewer writes on easier configurations. Budget-matched random and periodic schedules do not recover this gain, isolating the benefit to the action-surprise signal. On a trained closed-loop OpenVLA-OFT 7B panel on LIBERO-Long (n=60 episodes per arm), the gate does not hurt success: AURA-Mem matches the ungated base policy (0.233) and slightly exceeds an always-write KV arm (0.217), while using 7.0 times fewer writes and constant memory. We also instantiate an approximate-information-state value-loss bound as a methodology demonstration; at this scale, the bound is vacuous rather than a guarantee.

---


### 29. [Do Value Vectors in Deep Layers Need Context from the Residual Stream?](https://arxiv.org/abs/2606.02780)

**<font color=#1a73e8>作者：</font>** Muyu He, Yuchen Liu, Qingya Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The success of the transformer architecture as the backbone of modern LLMs is in large part due to its use of attention layers. An attention layer follows the standard neural network paradigm: it takes the residual stream as input and thereby produces context-dependent query, key, and value vectors. However, we find that model performance meaningfully improves when deeper layers learn only a context-free value vector to preserve the original token information, without drawing on any context from the residual stream. When the model has access to this context-free value vector, adding back the context-dependent component provides little additional benefit for aggregate benchmark performance. Such context-free value vectors can be stored as sparse model parameters, eliminating the need to recompute or persistently cache these values. Through systematic ablations on the key design choices for such context-free value vectors, we propose Bank of Values (BoV), a new way of computing value vectors in attention by learning a lookup table of token-specific value vectors for each of the last third of layers. Across 135M and 780M models, BoV improves validation loss over standard attention and, at 780M, the average score across 21 benchmarks, matching the previous best method that adds token information to the value vector with less compute and memory.

---


### 30. [QUIVER: Quantum-Informed Views for Enhanced Representations in Large ML Models](https://arxiv.org/abs/2606.02785)

**<font color=#1a73e8>作者：</font>** Aritra Bal, Michael Binder, Markus Klute 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large machine learning models benefit substantially from multimodal inputs that provide a complementary view of the same example. We introduce QUIVER (QUantum-Informed Views for Enhanced Representations, a paradigm that enriches classical data-driven features with a quantum Fisher view: a geometrically motivated, basis-independent summary of higher-order correlations captured by a variational quantum circuit (VQC) trained to perform the same task. Unlike classical feature augmentation, the quantum Fisher information matrix encodes the intrinsic geometry of the learned quantum state manifold. While this feature map, motivated by quantum information theory, is ordinarily non-trivial to model classically, it can surface statistical structure that additional classical data or model capacity finds difficult to learn. This makes the quantum Fisher view a genuinely complementary modality rather than a redundant one. We demonstrate that QUIVER improves standard performance metrics on two benchmark datasets from very different fields: QM9 for predicting molecule properties, and JetClass for predicting jet flavor at the Large Hadron Collider (LHC). The core contribution, however, is domain-agnostic: the quantum Fisher view can be fused into a broad class of model architectures via targeted modifications to the base architecture, to incorporate information about the quantum geometry of the problem. These results demonstrate that quantum-geometric features, extracted from simulated variational circuits, can deliver measurable value for standard machine learning tasks, well before the advent of fault-tolerant quantum hardware.

---


### 31. [Diagnosis of Human Object Interaction Detectors for Real World Educational Applications](https://arxiv.org/abs/2606.02789)

**<font color=#1a73e8>作者：</font>** Divya Mereddy, Ashwin Tudur Sadashiva, Marcos Quinones-Grueiro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-object interaction (HOI) recognition is critical for automatically analyzing student behavior in complex educational environments. Although state-of-the-art (SOTA) HOI detectors perform well on benchmark datasets, their performance often degrades when deployed in real-world training environments due to domain-specific objects, occlusions, and complex visual conditions. In this paper, we introduce a diagnosis-driven framework that integrates a triplet-level HOI error taxonomy with error-factor attribution analysis for real-world educational video data. We study this problem in the context of Critical Care Air Transport Team (CCATT) mixed-reality medical training. Based on an analysis of HOI failure modes and their causes, we develop a diagnosis-informed refinement strategy for adapting pretrained HOI models to the target domain. Experiments on the CCATT dataset show that this approach improves the macro-F1 score of a pretrained CDN model from 48.6 to 90.2 through targeted refinement guided by diagnosed error factors. These results highlight the value of detailed diagnostic analysis for informing targeted adaptation of HOI models in real-world educational environments.

---


### 32. [Evaluating Transformer and LSTM Frameworks for Prediction in Ungauged Basins](https://arxiv.org/abs/2606.02791)

**<font color=#1a73e8>作者：</font>** Taye Akinrele, James Halgren, Noorbakhsh Amiri Golilarz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Watershed networks exhibit convergent topologies in which multiple tributaries merge into downstream channels,integrating diverse upstream hydrological processes. In ungauged basins, the absence of direct observations increases uncertainty and limits the ability to anticipate extreme events. This study evaluates whether an encoder-only Transformer provides an advantage over an LSTM for upstream streamflow inference under limited hydrologic information, using retrospective simulations from the NOAA National Water Model (NWM). Across both upstream-only and combined configurations, the LSTM showed stronger overall performance than the Transformer model across the two configurations. Incorporating downstream information further boosted performance for all models, increasing median NNSE by more than 60%. Rather than treating this as a leaderboard-style comparison, we interpret the experiments as a test of architectural inductive bias for hydrologic sequence inference. The results indicate that recurrent memory remains better aligned with this upstream reconstruction task than an encoder-only Transformer, while downstream hydrologic context provides a strong auxiliary constraint that substantially improves prediction skill across architectures

---


### 33. [On Improving Robustness of Deepfake Image Detectors](https://arxiv.org/abs/2606.02797)

**<font color=#1a73e8>作者：</font>** Abu Taib Mohammed Shahjahan, Mohammad Mannan, Abdessamad Ben Hamza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Generative AI has introduced remarkable opportunities while simultaneously raising critical concerns regarding content authenticity. While recent work has increasingly focused on improving the generalization of deepfake detectors across unseen generative models, their robustness against adversarial attacks remains limited. In particular, Abdullah et al. (IEEE SP 2024) evaluated eight detectors and demonstrated that most of them exhibit significant performance degradation under adversarial attacks. We also observed the same phenomenon by testing seven most recent state-of-the-art detectors. To address this problem, we propose a unified framework that integrates three complementary design principles without relying on adversarial training data: (i) higher-order statistical modeling in the frequency domain via Discrete Cosine Transform (DCT)-based moment pooling up to fourth order, (ii) content-agnostic feature representations derived from noise residuals, and (iii) cross-scene generalization enforced through patch-level semantic disruption. A key insight underpinning our approach is that adversarial attacks primarily operate on low-order statistics and visual semantics, leaving higher-order residual-frequency characteristics, particularly kurtosis, largely unconstrained. Extensive experiments demonstrate that our method consistently improves robustness across six architecturally diverse detectors. Notably, we achieve up to 88.9% reduction in recall degradation on current adversarial benchmarks, and improve the best-performing recent detector (Yang et al., IEEE CVPR 2025) from 81.9% to 97.15% accuracy under attack. Overall, our method provides a principled, architecture-agnostic approach for improving deepfake detection robustness against current attacks.

---


### 34. [BehaviorBench: Modeling Real-World User Decisions from Behavioral Traces](https://arxiv.org/abs/2606.02798)

**<font color=#1a73e8>作者：</font>** Liangwei Yang, Jielin Qiu, Zixiang Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many decision-support settings require systems that adapt to individual users, but evaluation data for this problem remain limited. Existing benchmarks for user understanding often rely on simulated users or model-generated behavior, even though recent work cautions that model-based simulations can diverge systematically from human behavior. We introduce \textsc{BehaviorBench}, a benchmark for evaluating personalized decision modeling from real-world behavioral traces. \textsc{BehaviorBench} reconstructs wallet-level decision histories from observed public prediction-market and on-chain records, and organizes them into two complementary task layers: \emph{Belief prediction}, which predicts a user's final revealed stance and confidence in a market, and \emph{Trade prediction}, which predicts the direction and amount of individual transactions. Across 2,000 evaluation wallets, the benchmark contains 141,445 Belief instances and 1,485,972 Trade instances, with disjoint support pools for retrieval-based evaluation. We evaluate frontier and open-weight generative models under four history interfaces: no personalization, direct recent history, generated user profiles, and retrieved support-wallet evidence. Personalization improves Belief prediction more consistently than Trade prediction, model rankings change across task layers and metrics, and different history interfaces expose different failure modes. \textsc{BehaviorBench} provides an evaluation setting for studying whether personalized methods can use real-world behavioral evidence rather than simulated users alone.

---


### 35. [Translating Classical Poetry into Modern Prose](https://arxiv.org/abs/2606.02806)

**<font color=#1a73e8>作者：</font>** Chalamalasetti Kranti, Sowmya Vajjala  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Padyam2Gadyam, a dataset for the task of poem-to-prose translation from 13th-17th Century Telugu Classical Poetry to contemporary Telugu and English prose. The dataset consists of 600 poems and their human-verified Telugu and English prose translations. We evaluated 5 contemporary Large Language Models (LLMs) on their ability to do poem-to-prose translation into Telugu and English. Our results indicate that while there are differences across LLMs, their overall performance leave a large room for improvement in both languages. Through qualitative analysis, we discuss the the capabilities and limitations of contemporary MT evaluation approaches for this task.

---


### 36. [Mitigating Spurious Correlations with Memorization-Guided Dataset De-Biasing](https://arxiv.org/abs/2606.02830)

**<font color=#1a73e8>作者：</font>** Arda Fazla, Abolfazl Hashemi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world datasets often contain spurious correlations that are not causally related to the target label. When such correlations dominate the majority of training samples, models tend to rely on them, leading to misclassification of minority samples that do not exhibit the same spurious patterns. While a potential approach is to select subsets of data to better represent the minority samples, this may require access to group labels, which are typically unknown. Furthermore, as we demonstrate, widely used sample scoring functions in the invariant subset or coreset selection literature largely depend on spurious features and therefore fail to accurately capture the importance or difficulty of core, causally relevant features. Accordingly, we propose to mitigate spurious correlations by developing a two-stage sample scoring function that disentangles the learning dynamics of core and spurious features and evaluates their difficulty separately. Based on our proposed metric, we introduce a new algorithm to find and prioritize informative samples both with and without spurious correlations. Extensive experiments demonstrate that a standard ERM model trained on our selected samples achieves superior performance compared to state-of-the-art debiasing techniques, while requiring as little as 10\% of the original training data.

---


### 37. [Principled Reflection Separation via Nonlinear Superposition and Feature Interaction](https://arxiv.org/abs/2606.02831)

**<font color=#1a73e8>作者：</font>** Qiming Hu, Mingjia Li, Yuntong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image reflection separation is fundamentally challenged by the entanglement of transmission and reflection layers under complex image formation processes. Existing approaches largely rely on simplified assumptions or independent modeling, limiting their ability to handle real-world scenarios. In this work, we revisit the problem from a unified perspective and identify a key issue of existing approaches, i.e., the widely adopted linear composition model in the sRGB domain fails to capture the nonlinear coupling introduced by real-world image signal processing pipelines. To address this, we introduce a learnable nonlinear superposition model that more faithfully characterizes layer interactions and improves decomposition fidelity. Building upon this formulation, we propose a generalized dual-stream interactive framework that explicitly models bidirectional dependencies between transmission and reflection through feature exchange. This framework unifies activation-, gating-, and attention-based interaction mechanisms, and is compatible with both CNN and Transformer backbones. Extensive experiments on diverse real-world benchmarks demonstrate that the proposed approach achieves superior performance with strong generalization capability. More importantly, our study reveals that reflection separation is not about undoing a linear mixture, but about learning nonlinear formation and interaction}, offering new insights into the design of principled image decomposition models. Code and models are publicly available at this https URL.

---


### 38. [An Exploration of Collision-based Enemy Morphology Generation](https://arxiv.org/abs/2606.02832)

**<font color=#1a73e8>作者：</font>** Johor Jara Gonzalez, Matthew Guzdial  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite a great deal of prior research into Procedural Content Generation (PCG), relatively little prior work has explored generating enemies for video games. In particular, there is almost no work on generating enemy morphologies, the basic body plan or collision information for in-game enemies, despite the existence of related morphology generation work in robotics. In this paper, we explore three different novel approaches to generate enemy morphologies based on player collision information. We found that each approach provides different strengths and weaknesses, but all had equivalent or better performance than an evolutionary baseline adapted from prior robotics morphology work.

---


### 39. [Human Factors in Cybersecurity in Icelandic Small and Medium-sized Enterprises](https://arxiv.org/abs/2606.02839)

**<font color=#1a73e8>作者：</font>** Goda Cicėnaitė, Thomas Welsh, Helmut Neukirchen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity threats are increasing in all aspects of society due to the integration of digital systems into modern-day life and a volatile geo-political landscape. Technical factors are an ongoing arms race; however, the threat surface from human and social factors is still present, often providing malicious actors the means to bypass complex technical security controls. Understanding human factors in light of technical evolution is essential to ensure security controls remain effective. This study presents the results of a survey on cybersecurity challenges within public and private sector organisations, including critical infrastructure providers, in Iceland (N = 130). From the management perspective, human factors were strongly noted as challenges and barriers to their organisations' security. These challenges include a lack of adequate training or awareness, hiring issues, poor cybersecurity culture, and time and/or financial resource constraints. Based on these findings, recommendations for mitigating threats from human factors are derived. These include: prioritising targeted over generic training to reduce employee fatigue, external government support for financially constrained organisations, and building a strong cybersecurity culture through constructive communication around shared responsibilities.

---


### 40. [Learning Coherent Representations: A Topological Approach to Interpretability](https://arxiv.org/abs/2606.02841)

**<font color=#1a73e8>作者：</font>** Sigurd Gaukstad, Melvin Vaupel, Valdemar Kargård Olsen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks learn representations where individual features often lack interpretable meaning; a single neuron may activate for scattered, unrelated inputs. We introduce coherence, a geometric property inspired by neural coding in the brain, where neurons like grid cells and head direction cells respond to contiguous regions of state space. A non-negative matrix is coherent if each row (sample) attends to geometrically clustered columns (features) and vice versa, and in addition every sample is well described by some feature and every feature is needed by some sample. We prove that coherent matrices induce a bounded interleaving between the Vietoris-Rips filtrations of samples and features, guaranteeing that both spaces share compatible topological structure. This geometric constraint facilitates interpretability. For example, if data lies on a circle, coherent features must tile that circle into contiguous arcs. We introduce Coh, a differentiable objective function based on Fréchet variance that enforces coherence during training. Unlike sparsity, which bounds how many samples a feature activates on, coherence bounds which samples, requiring geometric connectivity rather than only rarity. This yields not just interpretable features but an interpretable feature space. We validate Coh in an auto-encoder using synthetic and rotated MNIST datasets and in a token embedding of BERT using language data.

---


### 41. [A Systematic Evaluation of Current Architectures in Wind Power Forecasting](https://arxiv.org/abs/2606.02849)

**<font color=#1a73e8>作者：</font>** Vinicius Bortolini, Gilson Adamczuk Oliveira, Erick Oliveira Rodrigues 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interval wind speed forecasting is essential for the efficient integration of wind energy into power systems, as it accounts for the inherent uncertainty of wind resources. This study presents a systematic literature review focused on hybrid approaches to interval forecasting of wind generation, exploring the combination of deep learning, modal decomposition, and statistical methods. To guide the paper selection, Latent Dirichlet Allocation (LDA) was applied for topic modeling, enabling the identification of patterns and research trends. The findings emphasize that integrating hybrid models with decomposition techniques-such as Variational Mode Decomposition (VMD) and Ensemble Empirical Mode Decomposition (EEMD)-enhances forecast accuracy and reliability by narrowing prediction intervals without compromising coverage. Regarding interval construction, most studies adopt a dual-model strategy, independently forecasting the lower and upper bounds. Input data are commonly decomposed using techniques like EMD, EEMD, or VMD, which extract frequency-based components. These components serve as inputs to models such as LSTM or ELM, trained separately for each bound. This approach allows for targeted modeling of uncertainty, improving flexibility and precision, Interval quality is typically evaluated through metrics that balance coverage and interval width. The review also highlights challenges, including the lack of standardized evaluation metrics, computational complexity, and limited real-world validation. Overall, the study reinforces the value of interval forecasting for wind energy operations and offers insights for advancing model robustness and decision-making.

---


### 42. [RESCAST-100K: A Comprehensive Dataset for Cross-Domain Residential Load and Indoor Temperature Forecasting](https://arxiv.org/abs/2606.02852)

**<font color=#1a73e8>作者：</font>** Jainam Dhruva, Yousaf Raza, A.B. Siddique 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate short-term forecasting of residential energy load and indoor temperature is essential for home energy management systems, grid-level demand response, and community energy efficiency efforts. Domain adaptation and transfer learning have shown promise for improving forecasting accuracy under data heterogeneity and scarcity commonly seen in residential settings. However, progress is limited by the lack of comprehensive residential datasets: existing benchmarks are narrow in target coverage and rarely support structured cross-domain evaluation. We introduce RESCAST-100K, a large-scale residential forecasting benchmark for studying cross-domain generalization. It provides a configuration-driven interface that instantiates source and target domains along interpretable axes, including geography, climate zone, wall construction, and heating equipment, enabling systematic evaluation of transfer learning, domain adaptation, and zero-shot generalization under controlled domain shifts. The benchmark covers approximately 100,000 EnergyPlus-simulated U.S. homes derived from ResStock, with 15-minute time series for three coupled targets per home: total load, HVAC load, and indoor temperature. These are paired with weather channels, HVAC setpoints, and over 40 static building covariates. RESCAST-100K also integrates five real-world residential datasets under a unified schema, supporting sim-to-real evaluation on the same tasks. We benchmark recurrent, attention-based, and MLP-mixer architectures for zero-shot performance across domains, missing-input conditions, and forecasting tasks. Cross-attention and MLP-mixer models consistently outperform recurrent and classical transformer baselines under domain shift. RESCAST-100K is intended to aid the machine learning and building analytics communities advance cross-domain residential forecasting at home, community, and grid scale.

---


### 43. [Economy of Minds: Emerging Multi-Agent Intelligence with Economic Interactions](https://arxiv.org/abs/2606.02859)

**<font color=#1a73e8>作者：</font>** Zhenting Qi, Huangyuan Su, Ao Qu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How can a population of agents self-orchestrate and self-adapt into stronger collective intelligence without centralized control? Inspired by Friedrich Hayek's economic theory of decentralized coordination in markets, we study this question through an agent economy in which agents compete via auctions for the right to act, exchange payments, and accumulate wealth from environmental rewards. These simple economic signals induce decentralized credit assignment, driving planning without global orchestration or explicit communication protocols. The population evolves through economic selection: effective agents accumulate wealth and are mutated via exploitation, while ineffective ones go bankrupt and are replaced via exploration. We show that, initialized with weak agents, the economy produces emergent multi-step reasoning strategies and outperforms stronger monolithic baselines across five agentic tasks, including mathematical reasoning, financial research, scientific research, accelerator design, and distributed-system optimization. We further provide theoretical insights into how economic dynamics shape agent behaviors, linking local incentives to long-term global performance. Our results suggest a new path to multi-agent intelligence: rather than engineering coordination, we can design decentralized incentive structures under which it automatically emerges.

---


### 44. [Forgetting is Not Erasure: Recovering Latent Knowledge via Transport Keys](https://arxiv.org/abs/2606.02860)

**<font color=#1a73e8>作者：</font>** Archie Chaudhury  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting is often framed as a representational problem: after sequential training, a model appears to lose the features that supported performance on earlier tasks. We challenge the stronger form of this view. Across controlled continual-learning settings, we find that a significant portion of apparent forgetting can be attributed to interface drift between internal stages rather than permanent erasure of task-relevant computation. We study this phenomenon through a stitched evaluation protocol that combines early computation from a post-update network with late computation from its predecessor, optionally mediated by a compact, task-specific transport key. We describe transport keys at a systems level as compact interface-alignment operators estimated from a small set of paired anchor activations and evaluated through model stitching. On split CIFAR-100 with a ResNet-style network, transport keys recover most of the original Task A performance after sequential training on Task B. On a compact vision transformer, we observe a similar recovery pattern. These results suggest that continual learning may require better mechanisms for indexing and re-accessing latent computations, not only methods that prevent weight change.

---


### 45. [Don't Gamble, GAMBLe: An Analytical Framework for AI-Driven Research Systems](https://arxiv.org/abs/2606.02863)

**<font color=#1a73e8>作者：</font>** Marquita Ellis, Paul Castro  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-Driven Research Systems (ADRS) -- systems coupling LLMs with automated evaluation to discover algorithms, proofs, and designs -- are being optimized and adopted across domains, but the tools to analyze them have not kept pace. ADRS performance depends on component interactions that are poorly understood, expensive to explore, and (as we show) not well captured by standard convergence guarantees. These guarantees rely on structural assumptions that do not hold under the ADRS process we formalize. We introduce GAMBLe, a framework that decomposes ADRS behavior into four parameters (generator $G$, assessor $\mathcal{A}$, discovery mechanism $\mathcal{M}$, budget $B$) and one compositional object, the effective landscape $L_{\text{eff}} = \mathcal{A} \circ G$, which reveals that distinct generator-assessor pairs induce structurally different per-problem optimization landscapes. We exercise the framework on 760+ replicated runs (>46,000 iterations) spanning generators from single LLMs to dynamically-adaptive ensembles, mechanisms from greedy selection to co-evolutionary meta-search, and three NP-hard problems whose assessors range from continuous scoring to cliff functions. The experiments reveal no total ordering of generators or mechanisms: frontier models can underperform open-source alternatives and the simplest mechanism sometimes outperforms state-of-the-art meta-search. Results show that even under limited budgets (60 iterations per run), the right component choices can improve performance by 13-67% and search efficiency by 6-39x.

---


### 46. [When Helping Hurts and How to Fix It: Multi-Agent Debate for Data Cleaning](https://arxiv.org/abs/2606.02866)

**<font color=#1a73e8>作者：</font>** Chirag Parmar, Akshat Mehta, Henglin Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When does multi-agent debate help data cleaning, and when does it hurt? Across three benchmarks, four model families, and over 6,000 task-condition pairs, we find debate's effect reverses sign: it degrades generation across all four models (-1.6 to -15.5pp) through critique-induced confusion (CIC), hallucinated Critic feedback that the Generator accepts uncritically, yet improves error detection (+27.4pp F1, d=1.0). We derive a debate benefit condition: debate helps when the probability of rescuing a wrong output (Critic verification odds weighted by fixability) exceeds the probability of destroying a correct one. A factorial experiment proves adversarial separation is essential: self-verification with identical tools fails, while a separate Critic with code-execution grounding and evidence-gated generation produces the first debate configuration to significantly exceed single-agent on a generative task (+5.3pp, p<0.05). The condition correctly predicts all nine task types and generalizes with zero false positives across 19 published comparisons in seven domains.

---


### 47. [Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks](https://arxiv.org/abs/2606.02875)

**<font color=#1a73e8>作者：</font>** Dipesh KC, Anjila Budathoki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding-agent benchmarks evaluate whether a single uninterrupted agent can resolve a repository issue. Real software work is messier: tasks are interrupted, reassigned, reviewed, and resumed from partial states left by another agent or engineer. We study this missing dimension through \emph{handoff debt}: the rediscovery cost imposed when a predecessor's work is opaque or incomplete. Our takeover protocol interrupts a coding agent at deterministic handoff points, freezes the repository, and evaluates successor agents under four handoff views: repository state only, raw trace, summary notes, and structured notes. Across 75 source tasks, the protocol generates 181 handoff-point tasks and 724 takeover runs per successor model. Across three successor models, context-bearing handoffs reduce median agent events by 20--59\% and cumulative prompt tokens by 42--63\% relative to repository-only takeover. Solved-rate effects are smaller and model-dependent, but efficiency gains are consistent. These findings suggest that coding-agent evaluation should report not only whether a task is solved, but also how costly that work is for another agent to resume.

---


### 48. [RRISE: Robust Radius Inference via a Surrogate Estimator](https://arxiv.org/abs/2606.02876)

**<font color=#1a73e8>作者：</font>** Jong-Ik Park, Shreyas Chaudhari, Carlee Joe-Wong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized smoothing (RS) uses a smoothed classifier to provide architecture-agnostic certificates of $\ell_2$ classification robustness, but its dependence on per-input Monte Carlo (MC) sampling undermines its use in real-time systems. We argue that this cost is structural rather than fundamental, such that it can be significantly reduced by sharing information across the deployment stream. We introduce RRISE, an RS framework that compresses certification into a single forward pass through a learned surrogate. RRISE trains the surrogate against precomputed MC class-count targets via a soft-label cross-entropy loss and converts surrogate predictions into provably conservative certified radii through a one-time conformal calibration step. The resulting certificate is deployment-verifiable: whenever the calibrated radius is positive, the surrogate's prediction provably matches the smoothed classifier's and the smoothed classifier is constant on a ball of that radius around the input. Across image classification benchmarks, RRISE matches fixed-budget MC certified accuracy within $0.84$ percentage points while replacing up to $10^4$ noisy base-model evaluations per query with a single surrogate forward pass, recouping MC training cost after $\approx 10^5$ deployment queries. On CIFAR-100 and Tiny ImageNet, where the only prior offline-surrogate method collapses, RRISE achieves $1.23$ to $1.91\times$ higher certified accuracy, establishing efficient randomized smoothing as a practical path to certified robustness in repeated-deployment settings.

---


### 49. [Pathway-Structured Privileged Distillation for Deployable Computational Pathology](https://arxiv.org/abs/2606.02877)

**<font color=#1a73e8>作者：</font>** Yongxin Guo, Hao Lu, Onur Koyun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Integrating transcriptomics and histopathology can improve cancer risk modelling, yet practical use is constrained by the limited availability of RNA profiling in routine settings. Here we introduce Mixture of Pathway Experts (MoPE), a knowledge-distillation framework that reframes multimodal learning as privileged distillation for histology-only inference. MoPE is motivated by the partial observability between RNA profiles and whole-slide images: histology can capture morphology-linked consequences of certain molecular programmes, but cannot be expected to reconstruct the full transcriptomic state. MoPE encodes RNA-derived pathways and transfers the molecular supervision to pathway-indexed pathology experts through memory-usage alignment. Across diverse public benchmarks and two independent breast cancer cohorts, MoPE consistently improved WSI-only inference performance relative to baseline methods. Pathway-usage analyses and human-audited visual inspection provide bounded inspection of model behaviour and candidate morphology-linked readouts. These results support pathway-structured privileged distillation as a promising route to using molecular information during training while preserving RNA-free inference.

---


### 50. [Are we really tilting? The mechanics of reward guidance in flow and diffusion models](https://arxiv.org/abs/2606.02884)

**<font color=#1a73e8>作者：</font>** Sanjit Dandapanthula, Nicholas M. Boffi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward guidance algorithms steer a learned generative process toward the reward-tilted measure at inference time. While empirically powerful, these methods are prone to reward hacking: the guided model over-optimizes the reward at the cost of fidelity to the learned distribution. Prior work has attributed this to the complexity of neural reward functions or implicit biases in diffusion training, but its fundamental origins remain poorly understood. We show that reward hacking arises from an approximation made in most practical implementations of reward-guided diffusion -- finite-particle plug-in estimation of the Doob h-function -- even in the simplest non-trivial settings of Gaussian and Gaussian mixture targets with quadratic rewards. In closed form, we isolate two distinct failure modes of the plug-in estimator: it leads to reward hacking within each mode and it cannot select high-reward modes. We propose a closed-form reward damping schedule that corrects the within-mode bias with no additional compute, and clarify the role of best-of-n sampling in compensating for the mode selection failure. Experiments on Gaussian mixture targets, a 2D checkerboard, and FLUX.1 text-to-image generation confirm that our theoretical insights carry over to practical settings.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-312](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
