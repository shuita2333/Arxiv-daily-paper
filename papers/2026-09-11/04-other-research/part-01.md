# 📦 其他研究 | 2026年09月11日

> 本类共 **176** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-176](./part-04.md)

---

### 1. [Spectral origin of the topological gap exponent d + η: mechanism, kernel, decomposition, and scope](https://arxiv.org/abs/2609.09159)

**<font color=#1a73e8>作者：</font>** Matthew Loftus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The topological gap $\Delta$ -- the excess $H_1$ total persistence of a critical point cloud over a density-matched null -- scales as $\Delta \sim L^{d+\eta}$. We derive this analytically: the spectral integral $I(\alpha) = \sum_{k\neq 0} S_{\mathrm{conn}}(k)\,|k|^{\alpha}$ scales as $L^{2-\alpha-\eta}$ when IR-dominated, giving $I(-2\eta) \sim L^{d+\eta}$. The decomposition $I(-2\eta) = I_0 \cdot I_{\mathrm{shape}}$ separates volume ($I_0 \propto N(1-m^2) \sim L^d$) from anomalous dimension ($I_{\mathrm{shape}} \sim L^{\eta}$); the volume factor accounts for the magnetization-driven per-configuration variance of $\Delta$. We prove the mechanism requires $d < 2 + \eta$ (IR dominance), confining it to $d = 2$ for physical systems; in $d = 3$ the spectral integral is UV-dominated, explaining why density normalization is needed. An $\alpha$-sweep for Potts $q = 4$ at $L = 32$--$256$ finds $\alpha_{\mathrm{opt}}$ in $[-0.75, -0.5]$, consistent with $-2\eta_{\mathrm{Ising}}$ and inconsistent with $-2\eta_{q=4} = -1$; we flag this as tentative pending $L \geq 1024$ confirmation. The $\langle m^2 \cdot I(-2\eta)\rangle$ hyperscaling product is dominated by the correlation $r(m^2, I) \approx -0.98$ via the shared $I_0$ amplitude, so we report it as a covariance-correction analysis. Under a heuristic argument extending Divol--Polonik to inhomogeneous Poisson intensities, the bare PH kernel is flat; the effective kernel acquires $k$-dependence only at criticality. The per-configuration agreement between $\Delta$ and $I(-0.5)$ is primarily a magnetization correlation: $R^2 = 0.91$ at $L = 256$ collapses to $R^2 \approx 0$ once $|M|$ is partialed out. Per-configuration evidence corroborates the $I_0$ Parseval identity but not the $|k|^{-2\eta}$ shape factor; the latter is established by ensemble $L$-scaling.

---


### 2. [Physics-informed neural networks by Gradient-Guided Gaussian Adaptive Sampling (3GAS-PINNs)](https://arxiv.org/abs/2609.09162)

**<font color=#1a73e8>作者：</font>** Yousen Wang, Wei Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) provide a mesh-free framework for solving partial differential equations, yet their performance in nonlinear problems is often limited by slow convergence, gradient imbalance, and insufficient resolution to capture localized intermittent structures such as shock waves[1]. These issues arise primarily from the use of fixed weights of loss and uniform collocation point distributions, which cannot adapt to the evolving complexity of the solution field during training. To address these challenges, Gradient-Guided Gaussian Adaptive Sampling Physics-Informed Neural Networks (3GAS-PINNs) is proposed in this paper, which combines uniform probability distribution and Gaussian-smoothed probability distribution derived from the spatial gradients of solution, to maintain global constraint satisfaction as well as concentrating collocation points in regions of high gradient. Thus, intermittency structures like shock wave and solitons can be accurately captured. The method is evaluated on three benchmark nonlinear problems, including one-dimensional forced Burgers equation, Korteweg-de Vries (KdV) equation and nonlinear Schrodinger equation, all of which exhibit steep gradients or strong nonlinearity. In comparison with baseline PINNs, 3GAS-PINNs can effectively promote the physical consistency in intermittent regions. The accuracy of the numerical simulation can be improved by a factor of up to 14.

---


### 3. [Integrating Unimodal and Vision-Language Representations in Latent Space for Multi-Label Chest X-Ray Classification](https://arxiv.org/abs/2609.09185)

**<font color=#1a73e8>作者：</font>** Quang-Huy Tran, Duc-Tuan Ngo, Minh-Khoi Nguyen-Bui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-label chest X-ray classification has attracted considerable attention in recent years, with the effective use of visual representations and clinical semantic knowledge playing an important role. This study proposes a framework that combines unimodal representations from RAD-DINO with vision--language representations from BioViL-T for the classification of 14 labels in the MIMIC-CXR-JPG dataset. The RAD-DINO and BioViL-T embeddings and their combined representation are refined separately in latent space before being normalized and fused across the three branches. In addition to improving classification performance, the study aims to clarify the role of each embedding source and the degree to which they complement one another.
Experiments show that RAD-DINO outperforms BioViL-T when used independently, whereas early fusion further improves the results, indicating that the two embedding sources contain complementary information. The best-performing model achieves a mean AUROC of 0.840 and an mAP of 0.467. Ablation analysis shows that hybrid fusion provides consistent and statistically significant improvements over early fusion when each embedding source is refined in latent space, suggesting that fusion effectiveness depends on the quality of the representation supplied by each branch. However, the study has only been evaluated internally on MIMIC-CXR-JPG; its generalizability to data from other healthcare institutions therefore remains to be validated. The source code is available at: this https URL.

---


### 4. [M2LG-DG: A Multi-modal Local-Global Domain Generalization Framework for Cross-site Major Depressive Disorder Classification](https://arxiv.org/abs/2609.09186)

**<font color=#1a73e8>作者：</font>** Muhammad Asif Hasan, Yanming Zhu, Xuefei Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classification models based on resting-state functional magnetic resonance imaging (rs-fMRI) often show lower performance at imaging sites not included during model development, which can limit their use in clinical settings. Domain generalization (DG) addresses this issue by learning representations from source sites that remain effective for unseen target sites. However, existing DG approaches for psychiatric disorder classification commonly rely on a single imaging modality and may not fully account for site-specific acquisition effects on the learned representation space. Subjects scanned at the same site share scanner hardware, acquisition settings, and preprocessing characteristics, which can cause representations to reflect acquisition conditions rather than diagnostic information. In this work, we present M2LG-DG, a source-only multimodal local-global framework for cross-site major depressive disorder (MDD) classification. The framework employs a dual-stream rs-fMRI encoder, where the global pathway models inter-regional dependencies through self-attention and the local pathway performs graph-constrained aggregation over functional connectivity-derived brain graphs. Imaging and non-imaging representations are decomposed into shared and private components and integrated through bidirectional cross-attention with a learned modality gate. A cross-site supervised contrastive objective forms positive pairs from same-class subjects acquired at different source sites, encouraging the fused representation to preserve diagnostic information across acquisition domains. On four held-out REST-meta-MDD sites, M2LG-DG achieves an AUC of 69.48% and exceeds the closest comparison method by 2.18 percentage points. Experiments on the Autism Brain Imaging Data Exchange (ABIDE) dataset further support its applicability to other psychiatric neuroimaging classification tasks.

---


### 5. [Lensless Gaze Is Not Private by Default: Auditing Identity Leakage Across Disclosure Surfaces](https://arxiv.org/abs/2609.09188)

**<font color=#1a73e8>作者：</font>** Rahul Vimalkanth, Kaushik Mitra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lensless near-eye sensing is often described as privacy-friendly because its coded measurements are visually unintelligible. Yet visual unintelligibility reflects human interpretation, not what a learned adversary can recover. We therefore treat identity privacy as a systems property of disclosure surfaces: representations crossing sensing, storage, computation, and output boundaries. We audit a simulated lensless gaze pipeline under a 36-subject known-gallery closed-set identification protocol with a fixed, known PSF; privacy from an unknown or varying optical key is outside our scope. Reported accuracies are empirical attack success rates under matched linear and MLP probes and do not upper-bound stronger adversaries. Simulated lensless measurements yield 96.7% top-1 identification versus 97.7% for matched original eye crops, while an MAE embedding retains 94.3%. Compression alone offers little protection: 8-D PCA and a matched 8-D bottleneck retain 93.2% and 91.8%, whereas separately trained 8-D GSPL bottlenecks yield 77.5% mean recovery across three seeds. A released 128-way gaze token lowers single-frame recovery to 38.1%, while its residual and continuous gaze output expose 62.1% and 72.6%, respectively. Under a source-frame-disjoint tiled protocol, token summaries reach 39.9% at T=25, showing that repeated-output risk depends on representation and aggregation. These rates reflect all subject-correlated information in the evaluated dataset, including acquisition and behavioral cues, rather than isolating intrinsic ocular biometrics. Ordinary least squares residualization against a six-dimensional crop geometry and intensity summary still leaves lensless recovery at 95.1%. Our results show that privacy claims for lensless sensing must be tested at disclosure boundaries rather than inferred from appearance.

---


### 6. [Adaptive Entangled Game Modules in Artificial General Intelligence](https://arxiv.org/abs/2609.09226)

**<font color=#1a73e8>作者：</font>** Haochen Li, Xinshuai Guo, Jingdong Ouyang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce a probability-wave framework for modeling the collective behavior of interacting adaptive agents, deriving testable eigenmodes through a generalized behavioral intelligence (GBI) nonlocal probability-wave equation. This framework captures a broad range of human intelligence behaviors with analytical mechanisms and offers an indirect method to examine the Liu-Chen-Ao (LCA) hypothesis of nonlocal entangled nerve fibers in the brain through collective trader behaviors. Our empirical analysis of Chinese intraday stock market data demonstrates that adaptive entangled game modes explain 82-94% (89% overall) of observed decision patterns, a sharp contrast to the predictions of neoclassical finance based on independent rational agents. Moreover, 2-12% of behaviors show adaption to intraday news, events, and environments, characterized by dual equilibrium states and abrupt reference point shifts, while purely independent modes occur in less than 5% of cases. These findings empirically support the LCA hypothesis, as observable trading behaviors reflect underlying brain mechanisms and internal intelligence decision-making in behavioral psychology. Our results highlight the necessity of incorporating adaptive entangled game modules into artificial general intelligence (AGI) architectures, addressing the limitations of conventional artificial neural network (ANN)-based AI, which relies on trillions of opaque parameters. By integrating ANN-based AI with probability-wave-based entangled-brain simulations, machine learning can enrich AGI foundation models (FMs) and facilitate the development of human-like processing units (HPUs) that leverage brain-inspired mechanisms. Such HPUs may ultimately create more compact, efficient, and robust AGI systems, particularly for embodied intelligence and robotics.

---


### 7. [Compute-Bounded Security Assurance - Coverage, Verification, and Response under Resource Constraints](https://arxiv.org/abs/2609.09229)

**<font color=#1a73e8>作者：</font>** Jithin VG, Ditto PS  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Additional inference compute can increase the number of correctly resolved security-assurance tasks, but repeated success, unique coverage, accepted evidence, and operational protection are different quantities. We develop a resource-constrained framework that separates them. For repeated conditionally independent attempts with latent success probability $\Theta$, coverage is $C_n = 1 - E[(1-\Theta)^n]$, and its limiting value is $1 - P(\Theta = 0)$. Positive pairwise outcome correlation does not by itself imply a ceiling below one: we construct two models with the same mean success and pairwise correlation but different limiting coverage. We distinguish this result from the effective sample size used to estimate a mean, and show why finite-budget observations cannot generally identify an asymptotic support ceiling. We then connect coverage to fallible evidence checking, proper scoring of factual grounding, complete resource accounting, service capacity, and a response model that includes mitigation delay. A conceptual defensive architecture separates evidence analysis, adjudication, and operational authority. An evaluation protocol specifies held-out tasks, paired comparisons, negative cases, and uncertainty reporting. The contribution is a consistent theoretical synthesis and a set of counterexamples to invalid extrapolations, rather than an empirical scaling law. All numerical illustrations are analytic; no model-parity result, hardware benchmark, or general attacker-defender equilibrium is claimed.

---


### 8. [DiffLUT-Net: Differentiable Training of FPGA LUT Networks with Learnable Connectivity](https://arxiv.org/abs/2609.09254)

**<font color=#1a73e8>作者：</font>** Jiaqi Ye, Xinrui Gong, Jingcun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Field-programmable gate arrays (FPGAs) enable efficient neural-network inference, but most deployment flows either accelerate multiply-accumulate operations or convert pretrained quantized models into lookup tables (LUTs). We present DiffLUT-Net, an FPGA-native network connected by six-input LUTs that are trained from scratch. We jointly learn the 64 truth-table entries of a LUT and the source to each of its six input ports using a differentiable LUT function relaxation and hardware source selection. After training, the truth tables and connections are discretized, unused logic can be pruned, and the network is exported directly as synthesizable Verilog. Across five benchmarks, DiffLUT-Net achieves favorable accuracy-resource trade-offs. These results demonstrate the effectiveness of jointly learning LUT functions and sparse connectivity for compact FPGA-native inference. The code is available at this https URL.

---


### 9. [Accountable and uncertainty-aware evaluation of sensor-based AI under distribution shift: devices, subjects, and nearly three years underground](https://arxiv.org/abs/2609.09257)

**<font color=#1a73e8>作者：</font>** Benny Platte, Rico Thomanek, Christian Roschke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sensor-based AI systems are rarely operated under the conditions under which they were trained: devices, personnel and recording epochs change, and each change degrades performance in ways a random train-test split cannot reveal. We propose a staged, accountable evaluation protocol that treats the evaluation of a deployed model as a measurement with declared reference levels and a quantified uncertainty. Four cumulative generalisation stages hold out devices, subjects and time. Each stage is judged on quantiles of repeated trainings against chance references with the correct class count, an out-of-present-scope rate exposes silent misdirection towards classes that are no longer present in deployment relative to training, and an explicit decision rule ties roll-out decisions not to means but to 5% quantiles. We demonstrate the protocol on infrastructure-free geomagnetic localisation with smartphone-based recurrent classifiers in two real underground mines, including a replication of the scheme's training stages at the second site. Unchanged models are re-evaluated on data recorded 34 months after the training campaign, on a device generation unknown at training time and with a held-out surveyor. The 5% quantile of their present-conditioned precision there is 0.39 over 299 repeated trainings, 16.5 times the chance level; across the composition of the 42 reachable location classes the figure varies by +/-0.08, several times the spread between repeated runs. Repeated trainings of a single configuration show why means mislead: a bimodal configuration passes a mean-based test decisively while its 5% quantile lies more than an order of magnitude below chance.

---


### 10. [Literati: Towards Anytime Optimal Shape Generalized Trees via AO*](https://arxiv.org/abs/2609.09299)

**<font color=#1a73e8>作者：</font>** Nakul Upadhya, Eldan Cohen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision trees are prized for their interpretability and strong performance on tabular data, but popular greedy top-down induction algorithms can yield suboptimal and unnecessarily complex structures. Optimal decision tree methods address this through global optimization, yet remain restricted to axis-aligned threshold splits, which limit the expressivity of each node and often force deep, complex trees to capture non-linear feature effects. Shape Generalized Trees (SGTs) generalize threshold splits to learnable univariate shape functions, improving expressivity and enabling more compact trees. However, existing SGT induction algorithms are greedy and offer no optimality guarantees. In this work, we introduce Literati, the first algorithm for optimal SGT induction. We propose a novel AND/OR graph formulation of the problem that jointly optimizes tree structure and shape function complexity. To solve this AND/OR graph, we develop an AO*-based algorithm with two enhancements that improve anytime performance while preserving optimality: a secondary heuristic for OR-node selection and a round-robin policy for AND-node exploration. Across 24 real-world datasets, Literati achieves higher training and test accuracy than state-of-the-art tree approaches.

---


### 11. [Gradland: On Phenomenal Experience, Differentiated Across Many Dimensions](https://arxiv.org/abs/2609.09306)

**<font color=#1a73e8>作者：</font>** David Balduzzi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper investigates the hypothesis that the first-order structure of physical interactions, i.e. gradients or Jacobians, characterizes the structure of phenomenal experience. It does so in an idealized world inhabited by neural networks, Gradland, where the physics are known and the functions are (mostly) differentiable. The paper introduces two measures of Jacobian structure: effective rank and cohesion, based on Kirchhoff complexity. Applying the measures to a series of worked examples shows the hypothesis accounts for: (1) the duration of experience, that it can prolong over hundreds of milliseconds; (2) the difference between what is experienced vividly and obscurely; (3) the experience of texture; (4) the blooming buzzing confusion presumably experienced by newborns; (5) the difference between ideas that are held distinctly in mind and ideas that are confused; (6) what learning is like; and finally (7) the paper explains the function of rich, dense experience.

---


### 12. [Ephemeral Feeds and Enduring Rituals: RushTok and the Formation of Event-Based Algorithmic Communities](https://arxiv.org/abs/2609.09331)

**<font color=#1a73e8>作者：</font>** Emelia Hughes, Tim Weninger  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Each August, TikTok's For You page turns the University of Alabama's sorority recruitment into RushTok. We examine RushTok as an event-based algorithmic community: a collective assembled around a bounded offline ritual and sustained by recommendation. Using a mixed-methods survey (n=71) and a reflexive account of creator outreach, we ask who participates, how, and with what stakes. Findings show an ambiguous and entertainment based throughline; many called it a community (51/71) but few claimed membership (11/71). Affiliation centered on creators rather than shared practices, with parasocial attention clustering around a small set of potential new members (PNMs) and returning figures. Higher content exposure tracked with self-identification as a community member; those members commented, followed creators, and engaged across videos. Attempts to interview creators were met with silence or refusals, reflecting community boundary-work despite viral visibility. We outline implications for platform governance, including time-bounded context, graduated visibility, and aftercare.

---


### 13. [Cross User/App Network Attacks - Hijacking TCP Connections and DNS Cache Poisoning via a Malicious User/App (Extended Version)](https://arxiv.org/abs/2609.09345)

**<font color=#1a73e8>作者：</font>** Tamir Shahar, Amit Klein  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Off-path network attacks against TCP and DNS (over UDP) client-server connections are generally considered impractical nowadays, due to built-in security features in these protocols, e.g. randomized TCP (initial) sequence numbers and randomized UDP source ports, respectively. In this work, we refute this presumption by demonstrating that an unprivileged malicious application running on the client (but practically off-path), when combined with a remote off-path adversary, can enable powerful network attacks against such connections. We show how such a local--remote collaboration between the malicious application and a remote adversary allows inference of sensitive connection state, including TCP sequence numbers and DNS stub-resolver UDP source ports.
Our attacks exploit standard socket API calls such as bind(), protocol mechanisms such as IP options, and operating system features such as cBPF and procfs to infer the TCP initial sequence number (ISN) and the UDP source port in use by the connection of interest. Specifically, we take advantage of certain properties of the ISN generation algorithm as implemented in major operating systems.
We demonstrate TCP connection hijacking in Linux, Android, Windows, macOS and iOS, and DNS cache poisoning against Windows, Android and the popular systemd-resolved DNS stub resolver in Linux.
We evaluate our techniques across multiple operating systems and realistic deployment settings, including environments behind port-preserving NAT-integrated routers.
We disclosed our techniques to Microsoft, Apple, Linux and Google, which led to the release of several patches.

---


### 14. [Encrypt What Matters: When Selective Homomorphic Inference Is Efficient](https://arxiv.org/abs/2609.09357)

**<font color=#1a73e8>作者：</font>** Ali Backour, Juan Reyes, Jaime Punyed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) enables inference on private data without revealing it to the server, but evaluating an entire input under FHE is expensive. We study \emph{selective homomorphic inference}, where only a sensitive region of interest (ROI) is encrypted, and computations independent of that region are performed in plaintext. Selective evaluation produces the same output as full FHE on the same model, without retraining. Its efficiency depends on how quickly encrypted dependencies spread through the network. For small encrypted ROIs, locality-preserving architectures can achieve order-of-magnitude homomorphic-evaluation speedups, whereas architectures with early global mixing provide essentially no speedup. These results identify locality as the key architectural property governing the benefit of selective homomorphic inference.

---


### 15. [DensePol: Dense-Angle Polarization Dataset for Learning-Based Polarimetric Vision](https://arxiv.org/abs/2609.09359)

**<font color=#1a73e8>作者：</font>** Param Sangani, Ahmad Moori, Erik Blasch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Polarimetric vision is gaining increasing attention because it provides physical cues about scene shape, material, and reflection that are difficult to recover from RGB alone. Recent work has therefore explored predicting polarization directly from conventional RGB images; however, the fidelity of these methods strongly depends on the polarization supervision used for training. Most existing datasets rely on Division-of-Focal-Plane (DoFP) cameras with four spatially interleaved analyzer orientations, which provide limited angular redundancy and introduce interpolation and instantaneous-field-of-view errors. We introduce DensePol, a high-redundancy RGB--polarization dataset based on Division-of-Time (DoT) acquisition, capturing 180 full-resolution analyzer orientations at $1^\circ$ intervals. DensePol contains 2,018 paired RGB--polarization images with the angular measurements and fitting residuals retained. Dense angular sampling substantially improves polarization stability, reducing AoLP deviation from $13.36^\circ$ to $2.21^\circ$. We further introduce a deterministic diffusion-based RGB-to-polarization framework with cyclic AoLP representation and a local DoLP refiner. Experiments demonstrate improved polarization prediction and downstream surface-normal estimation. The dataset and code will be publicly available.

---


### 16. [Echoes in the Algorithm: Analyzing the Fidelity of User Preferences Against Realized Platform Reach](https://arxiv.org/abs/2609.09365)

**<font color=#1a73e8>作者：</font>** Emelia Hughes, Tim Weninger  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> What does popular content look like when platforms withhold the usual cues? On TikTok, users still form impressions about which videos are taking off even when likes and view counts are hidden, delayed, or pushed to the margins of the interface. We study this problem through TokOrNot, a web-based game in which participants compared pairs of TikTok videos and reported (i) which one they preferred and (ii) which one they believed had reached a larger audience. We benchmark these judgments against verified public view counts, which we use as a bounded proxy for realized platform reach. Across 3,513 judgments from 363 participants, participants identified the higher-reach video only modestly above chance (56.75%, 95% CI: 56.01-58.55). Preference aligned with the higher-view video at a similar rate, while preference and prediction matched in 83.48% of trials (95% CI: 83.12-85.95). Performance also varied across content categories. Taken together, these results do not suggest that users can reliably read platform success from content alone. Instead, they point to a looser and more uncertain interpretive process in which reach judgments often track personal taste or other weak heuristics when explicit popularity cues are absent. We discuss the implications for algorithmic literacy and for interface designs that reduce visible metrics without leaving users to infer reach from uneven or idiosyncratic cues alone.

---


### 17. [Explaining f-Divergence-Based Regularization via Local Curvature and Sharpness-Aware Minimization](https://arxiv.org/abs/2609.09367)

**<font color=#1a73e8>作者：</font>** Nour Jamoussi, Marios Kountouris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Divergence-based regularization and Sharpness-Aware Minimization (SAM) are two prominent approaches for improving generalization in deep learning, both motivated by robustness to perturbations. However, their relationship has remained largely unexplored. Building on classical second-order expansions of $f$-divergences, we show that the two methods are locally consistent under parameter-space perturbations: both induce curvature-sensitive penalties, with divergence regularization yielding a Fisher-weighted quadratic form and SAM penalizing sharpness through the dominant Hessian eigenvalue. For negative log-likelihood objectives with exponential-family output distributions, this correspondence becomes especially transparent, since the Fisher and Gauss-Newton matrices coincide. We further show that the same local geometric perspective extends to input-space perturbations, where divergence-based regularization is defined through transformations of the input. In this setting, the regularizer induces a pullback quadratic form on the input space, providing a more general perturbation framework than standard SAM while preserving the same local sensitivity interpretation. To validate the analysis empirically, we use the asymmetric $\alpha$-skew Jensen-Shannon divergence (JSD) family as a controlled testbed. Its local curvature coefficient scales as $\alpha(1-\alpha)$ and is maximized at the symmetric point $\alpha=\tfrac12$, which recovers the standard JSD. Loss-landscape visualizations in the input-perturbation regime show that stronger induced curvature penalization is associated with flatter local minima. Experiments on four benchmark datasets further demonstrate that both accuracy and negative log-likelihood are consistently best near this regime of maximal curvature penalization.

---


### 18. [The Living Library: Transforming Archival Collections into Conversational Knowledge Systems -- Lessons from the Theodore Roosevelt Presidential Library](https://arxiv.org/abs/2609.09368)

**<font color=#1a73e8>作者：</font>** Pengce Wang, Lucia Ronchi Darre, Matt Briney 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present the Living Library, an end-to-end framework for transforming fragmented digital archives into governed, conversational, in-person exhibit experiences. Developed and deployed at the Theodore Roosevelt Presidential Library, the framework comprises four layers: digitization and corpus creation, AI-powered processing, retrieval and reasoning, and an optional embodied conversational interface. The first three layers aggregate a 300,000-record collection, apply OCR and structured metadata enrichment for expert curatorial review, and publish records to a hybrid dense/semantic index. Expert review is conducted through the Archivist App, a curator-facing interface that supports correction of AI-generated transcriptions and metadata.
The governed corpus powers both a researcher-facing interface and Talk to TR, a continuously operating exhibit that embodies Theodore Roosevelt as a full-scale digital human within a museum environment. To support live, face-to-face interactions, Cross-Era Analogical Grounding reframes contemporary questions through documented historical parallels, allowing Roosevelt to address present-day topics without inventing facts. Dual-path retrieval and end-to-end streaming keep responses grounded and responsive. Layered watchdogs, visitor-session isolation, automated conversation management, and independently restartable services enable reliable unattended operation for hundreds of visitors. Avatar realism, spatial audio, lighting, staging, and conversational design are developed and evaluated as an integrated experience. Rather than report a controlled benchmark, we describe lessons from operating Talk to TR as a public exhibit and offer a transferable model for transforming archival collections into believable, in-person conversational experiences.

---


### 19. [Constraint-Aware Discrete Black-Box Optimization Using Tensor Decomposition](https://arxiv.org/abs/2609.09370)

**<font color=#1a73e8>作者：</font>** Keisuke Onoue, Ryosuke Kojima  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete black-box optimization is often addressed using approaches such as Sequential Model-Based Optimization (SMBO), which aims to improve sample efficiency by fitting surrogate models that approximate a costly objective function over a discrete search space. In many real-world problems, the set of feasible inputs is often given by logical constraints known in advance. However, existing surrogate modeling techniques generally fail to capture the symbolic rules governing feasibility in discrete input spaces. In this paper, we propose a surrogate modeling approach based on tensor decomposition that captures the structure of discrete search spaces while directly integrating feasibility information. To implement this approach, we formulate surrogate model training as a constrained polynomial optimization problem and solve a relaxed formulation using a differentiable penalty term derived from T-norms. Our experiments on both synthetic and real-world benchmarks, including a pressure vessel design task, demonstrate that the proposed method improves sample efficiency by effectively guiding the search away from infeasible regions.

---


### 20. [An Autonomous GeoAI Agent for Arctic Eco-Navigation](https://arxiv.org/abs/2609.09374)

**<font color=#1a73e8>作者：</font>** Samira Alkaee Taleghan, Younghyun Koo, Farnoush Banaei-Kashani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Arctic maritime navigation is becoming increasingly important as changing sea-ice conditions expand seasonal accessibility while simultaneously introducing substantial operational, environmental, and community risks. Arctic route planning is inherently a multi-criteria problem: routes that improve vessel safety or efficiency may increase exposure to sea ice, sensitive ecosystems, or nearby communities. Existing routing methods prioritize travel time, fuel use, and navigational risk, often overlooking ecological and community impacts. We introduce a human-in-the-loop, multi-agent GeoAI system for Arctic eco-navigation that integrates operational, physical, ecological, and community-related criteria within a unified routing framework. Multiple specialized agents coordinate geospatial data acquisition and preparation, multi-objective route generation, and skyline-based decision support. The ecological criteria explicitly account for exposure to sensitive areas, including Essential Fish Habitat and seal critical habitat. By considering these ecosystem impacts and potential community burdens while keeping consequential value judgments under human control, the framework supports safer, more transparent, and socially responsible Arctic navigation. Project page and code are publicly available. this https URL, this https URL

---


### 21. [XAI-Refine: An Automated Explanation-Knowledge Loop for Brain-Age Prediction](https://arxiv.org/abs/2609.09388)

**<font color=#1a73e8>作者：</font>** Yang Qiao, Junjie Wu, Deqiang Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain-age prediction models are commonly evaluated by predictive accuracy, yet accurate predictions alone do not establish that a model relies on reproducible or neurobiologically supported mechanisms. Post-hoc explanation methods can expose these mechanisms, but existing workflows typically stop at diagnosis or require correction targets to be specified before model analysis. We propose XAI-Refine, an automated explanation-knowledge loop for brain-age prediction from resting-state functional connectivity. At each iteration, XAI-Refine consolidates complementary post-hoc analyses across repeated training runs into reliable, structured model explanations. It converts each reliable explanation into a neutral neurobiological question, retrieves and verifies relevant literature, and compiles the verified evidence into an admissible set in the same typed explanation space. The target for refinement is defined as the minimal projection of the current model explanation onto the admissible set induced by applicable verified knowledge. This revised explanation is then translated into a differentiable constraint while preserving the originating model variable, measurement operator, and applicable scope. Candidate updates are promoted only when multi-seed validation confirms target-directed explanatory movement, predictive performance remains within a prespecified guardrail, and non-target explanatory drift remains bounded. Experiments on functional-connectivity-based brain-age prediction evaluate predictive performance, explanation reliability, literature alignment, and target-specific model revision, illustrating a structured route from post-hoc analysis to evidence-guided model refinement.

---


### 22. [OmniPoint: Universal Monocular Metric Pointcloud from Any Camera](https://arxiv.org/abs/2609.09394)

**<font color=#1a73e8>作者：</font>** Botao Ye, Marc Pollefeys, Ming-Hsuan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering metric 3D geometry from monocular images is a fundamental computer vision task, yet current methods remain heavily fragmented by fixed camera model assumptions and inflexible input schemes. We present OmniPoint, a unified framework designed to generalize metric reconstruction across diverse imaging sensors, including pinhole, fisheye, and equirectangular projections, while accommodating varying geometric priors. To overcome projection rigidity, OmniPoint abandons conventional planar depth regression. It instead adopts a decoupled ray and distance representation alongside a decoupled training objective, explicitly separating the camera projection model from the scene structure. To address the severe scarcity of training data for alternative cameras, we introduce a bidirectional augmentation strategy that explicitly bridges labeled perspective data and unlabeled omnidirectional domains in 3D space. Furthermore, to seamlessly integrate optional inputs like camera intrinsics or sparse depth without destabilizing the network through feature distribution shifts, we propose a robust information injection mechanism. This mechanism utilizes learnable input state embeddings to resolve architectural ambiguity and applies vectorized Gaussian smoothing to densify irregular measurements. Extensive experiments demonstrate that OmniPoint achieves state-of-the-art zero-shot performance across multiple benchmarks, establishing a robust new standard for unified monocular 3D reconstruction.

---


### 23. [X-amine509: Predicting the Practical Risk Level of Enterprise X.509 Certificates](https://arxiv.org/abs/2609.09402)

**<font color=#1a73e8>作者：</font>** Cameron Keith, Shubh Patel, JD Kilgallin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprises managing large X.509 certificate inventories face a prioritization problem: deterministic analysis tools that precisely identify standards violations are indispensable for remediation, but applying them exhaustively across millions of certificates is operationally impractical. We present X-amine509, a two-stage triage system that uses machine learning to rapidly rank certificates by predicted risk and route only the highest-risk items to full deterministic analysis. Certificate risk is quantified as a composite score derived from 177 defect checks grounded in CA/Browser Forum Baseline Requirements, NIST IR 8547/SP 800-57, and cryptographic strength criteria, weighted by security severity across four tiers ranging from cryptographic breaks to minor compliance deviations. We collected 1,027,714 X.509 certificates from Fortune 500, .gov, and .edu domains and scored each using this rubric. On a held-out test set of 201,976 certificates, our best model (Extra Trees) achieves $R^2$ of 0.993 with MAE of 2.26, while Decision Tree scores $R^2$ of 0.986 at 3.7 million certificates per second on a single machine. Ranking quality confirms the triage value: aggregate NDCG exceeds 0.997, and severity-tier classification reports 99.76% accuracy with 98.90% recall on critical-tier defects. Thirteen months later, we retrieved another 571,374 certificates to test our models' durability over time, and the Extra Trees and Decision Tree models maintain MAE below 6.8, $R^2$ of at least 0.915, aggregate NDCG above 0.988, severity-tier accuracy of at least 99.52%, and critical-tier recall of at least 97.03%. Feature importance analysis identifies validity period, Extended Key Usage configuration, negative serial number encoding, and self-signed status as the strongest risk predictors, providing coarse interpretability at the triage stage.

---


### 24. [Decision-Focused Active Learning for Scale-Aware Critical-Materials Recovery](https://arxiv.org/abs/2609.09413)

**<font color=#1a73e8>作者：</font>** Niranjan Srinivas, Debajyoti Ray, Elias Nakouzi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Choosing a recovery process for scale-up requires connecting laboratory results with product requirements, process costs, and scale effects. We analyze records from Pacific Northwest National Laboratory's Computer Intelligence for Critical Element Recovery and Optimization (CICERO) workflow for autonomous selective precipitation. Active learning uses prior results to choose experiments. In a conditional retrospective benchmark with fitted models and recycled neodymium-iron-boron (NdFeB) magnet records, active learning finds the best recorded result with fewer experiments than nonadaptive space filling. Enrichment is the selected rare-earth-to-iron ratio relative to that in the feed. Adaptive policies reach the recorded enrichment maximum by 16 to 24 wells (individual experiments), versus 48. Our two-stage reconstruction ties two adaptive alternatives at 16 wells. Conditional analyses of recycled samarium-cobalt (SmCo) magnets show a Round 2 tradeoff between purity and nominal yield, the recovery fraction calculated from an assumed starting amount - NdFeB Round 1 routes differ in enrichment. Rankings for produced water from oil and gas extraction depend on phase and dilution assumptions requiring confirmation.
We propose choosing batches by their expected reduction in downstream Bayes risk: the minimum expected loss among available process decisions under current beliefs. In exploratory simulations, a hybrid that filters candidates has lower estimated loss than the implemented joint search across routes and conditions. Differences involving the synthetic two-stage policy are small relative to estimation uncertainty. We outline a pre-registered prospective test under a shared loss and logging standard, requiring clarified measurements and records, a defined process decision and relevant outputs, credible economic inputs, and validation at the intended scale.

---


### 25. [Valerant: An Automatic Navigable Game Map Generator via Action-Conditioned World Model Exploration](https://arxiv.org/abs/2609.09418)

**<font color=#1a73e8>作者：</font>** Yiran Qiao, Feng Wang, Jing Ma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) couple predictive world modeling with action generation, allowing anticipated future states to guide agent behavior. Although WAMs are rapidly advancing embodied AI, general-purpose counterparts remain largely unexplored in games. Existing game-oriented approaches often combine action-conditioned world models with external policies and reward functions to realize WAM-like decision-making, yet they operate mainly in 2D visual observation space and do not instantiate persistent 3D geometry. Extending this paradigm to 3D games introduces a distinct challenge. In autonomous driving and robotics, the physical environment exists independently of the model, providing a persistent 3D world in which selected actions can be executed. Games have no such external substrate; the virtual world itself must be instantiated. Most playable games require a persistent and navigable space, while 3D games additionally require explicit geometry that supports movement and interaction. Action-conditioned video rollouts provide visual observations but not this spatial representation. We present \textsc{Valerant}, a training-free framework that transforms a pretrained action-conditioned world model into a WAM for exploring and constructing 3D game maps. By coupling predictive visual rollouts with SLAM-based spatial reconstruction and exploration-driven action selection, \textsc{Valerant} progressively transforms a single image into a persistent 3D game map. This framework extends WAM-based interaction beyond 2D visual simulation and offers a new approach to reducing manual effort in 3D game-map creation.

---


### 26. [FPGA Acceleration of Fully Homomorphic Encryption with Adaptive Key Switching](https://arxiv.org/abs/2609.09423)

**<font color=#1a73e8>作者：</font>** Zhihan Xu, Jayashree Adivarahan, Rajgopal Kannan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully Homomorphic Encryption (FHE) enables privacy-preserving cloud services but incurs substantial computation overhead, making hardware acceleration essential. Among FHE operations, key-switching is a major performance bottleneck. Recent cryptographic advances introduce a novel key-switching method (i.e., KLSS) that reduces certain operational complexity but demands higher computational precision than the traditional Hybrid Key Switching (HKS) method. This trade-off leads to distinct computation and memory requirements, making the relative latency of KLSS and HKS highly dependent on hardware parallelism, FHE security parameters, and available on-chip memory capacity, particularly on FPGA platforms, where memory resources and parallelism must be carefully balanced.
In this work, we first propose a memory-efficient KLSS datapath that eliminates off-chip ciphertext transfers. We then develop a performance model to analyze and compare the overheads of both KLSS and HKS. Our analysis reveals that an adaptive solution supporting both methods can achieve lower overall latency than a static method during FHE computation. Guided by the performance model, we design an adaptive FPGA-based FHE accelerator that dynamically selects between HKS and KLSS during computation. We implement the accelerator on an Alveo U280 and evaluate it across multiple FHE benchmarks. Experimental results demonstrate that our adaptive solution achieves a 1.84-3.31$\times$ speedup in bootstrapping latency and a 1.66-2.52$\times$ speedup in secure image classification compared to state-of-the-art FPGA accelerators.

---


### 27. [Longitudinal tracking of multiple sclerosis lesions in the spinal cord: A validation study](https://arxiv.org/abs/2609.09424)

**<font color=#1a73e8>作者：</font>** Pierre-Louis Benveniste, Julian McGinnis, Shannon Kolind 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Longitudinal characterization of multiple sclerosis (MS) lesions remains constrained by the lack of frameworks capable of establishing consistent instance-level correspondences across time. Conventional segmentation approaches produce semantic lesion masks at each visit and therefore fail to capture the complex instance temporal patterns associated with lesion appearance, disappearance, splitting, or merging. This study presents a comparative evaluation of five strategies for automated tracking of spinal cord MS lesions in longitudinal MRI data from a multi-site cohort. The investigated strategies rely either on deformable registration or on a spinal anatomical reference system, and encompass overlap-based matching, coordinate-based Hungarian algorithm, gradient-boosted classification, and Siamese model classification. Tracking accuracy is quantified using instance-level true positives, false positives, and false negatives, allowing to assess the presence of one-to-many and many-to-one associations. Results show best performance for the registration-based overlap method. This study provides the first systematic analysis of lesion-instance correspondence in the spinal cord and outlines the strengths and limitations of registration-based and registration-free paradigms for longitudinal MS assessment. The code is available at this http URL .

---


### 28. [SCCM : Stream Cruise Control Method for Automated Drift Detection and Adaptation](https://arxiv.org/abs/2609.09432)

**<font color=#1a73e8>作者：</font>** Mohammad Abu-Shaira, Weishi Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world datasets often exhibit evolving distributions, known as concept drift. Ignoring drift degrades predictive performance, while reliance on fixed hyperparameters further limits model adaptability under changing conditions. Adaptive learning addresses this challenge by continuously updating models online, allowing them to incrementally adjust and remain effective as data distributions evolve. This paper presents the Stream Cruise Control Method (SCCM), a comprehensive framework for drift detection and adaptation in online regression. SCCM enables automated adaptation through early-response, pre-update drift detection, drift magnitude quantification, KPI-window-based thresholding for local false-alarm mitigation, dynamic hyperparameter tuning, and model recalibration. SCCM also adopts an in-memory design for real-time adaptability, unlike purely reactive methods that typically activate adaptation only after performance degradation is observed. By using dynamic thresholding and remaining agnostic to data distributions, SCCM supports KPI-based monitoring across varying data streams, including high-dimensional and large-scale settings. SCCM is integrated with four online regression models and evaluated on 18 synthetic datasets covering abrupt, incremental, and alternating gradual drift, together with eight real-world datasets. The evaluation uses both R2 and MSE and compares against eight detector--adaptation baselines. Results show improved predictive performance and effective drift handling across the evaluated online regression settings.

---


### 29. [Efficient Leakage-Free Neural Architecture Search under Leave-One-Subject-Out Evaluation](https://arxiv.org/abs/2609.09433)

**<font color=#1a73e8>作者：</font>** Heinke Hihn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Leave-One-Subject-Out (LOSO) evaluation estimates generalisation performance for subject-based classification but makes Neural Architecture Search (NAS) computationally expensive because a fully nested implementation requires N independent architecture searches and, assuming approximately linear training cost, scales as O(N^2). We propose a leakage-free, block-based approach that shares NAS runs across subjects. On the BioVid Heat Pain dataset, our approach increased the mean accuracy from 82.79% to 83.39% while reducing the number of parameters by up to 99.2%.

---


### 30. [Tensor-Train Weak SINDy: Identifying High-Dimensional Nonlinear Dynamics](https://arxiv.org/abs/2609.09434)

**<font color=#1a73e8>作者：</font>** Will Houser, Vanja Dukic, David M. Bortz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, weak-form methods have made significant advances in data-driven discovery of dynamical systems. However, in high-dimensional settings, current techniques can prove expensive in both computation and memory. In this work, we introduce TT-WSINDy, which combines techniques of the Multidimensional Approximation of Nonlinear Dynamics (MANDy) and Weak Sparse Identification of Nonlinear Dynamics (WSINDy) methods, implementing requisite computations in the tensor-train (TT) format. We demonstrate that this method is able to search an exponentially-growing space of candidate functions -- performing weak-form transformation, regression, and sparsification -- without suffering from the curse of dimensionality.

---


### 31. [Concept drift mitigation through community and spectral graph analysis for the detectionof cyberattacks in network traffic](https://arxiv.org/abs/2609.09442)

**<font color=#1a73e8>作者：</font>** Julien Michel, Abdul Qadir Khan, Majed Jaber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In network traffic, legitimate behaviours and attack techniques evolve jointly - the phenomenon known as 'concept drift' [1]. Every detector is thereby left obsolete between two updates, and always one step behind adversaries. In this work, we propose to move the point of intervention from the model, repaired after the drift, to the feature space, selected before learning. We therefore introduce t-robustness, a stability score defined for each feature independently of any detection model, comparable across an entire feature space. It combines the step-by-step distance between successive statistical states of a feature, and its cumulative divergence from its initial state, so that a slow monotonic drift cannot pass for stability. The candidates are drawn from abnormal network connectivity patterns left by scans, DoS and communications between endpoints, read through graph community metrics and spectral metrics. The evaluation is performed on the UGR16 dataset, across three learning scenarios and a control scenario, as well as without model update, and demonstrate that t-robust feature spaces sustain detection where the baselines collapse: retained expectancy at the last test interval reaches 0.6025, against 0.5230 for graph community features and 0.3831 for the base NetFlow features.

---


### 32. ["It's Like Drinking from a Fire Hose": Understanding and Characterizing Video Learning Experiences for Individuals with ADHD](https://arxiv.org/abs/2609.09443)

**<font color=#1a73e8>作者：</font>** Hanxiu 'Hazel' Zhu, Weiyu Zhang, Ru Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Video lectures have become increasingly prevalent for education and professional development, yet their static visuals, dense information, and long duration pose attentional challenges for individuals with ADHD. While adaptive learning offers opportunities towards ADHD-accessible video learning, little is known about how to suitably adapt such videos: What components in multimodal video lectures are challenging for ADHD viewers? How do these experiences surface in behavioral signals to trigger an adaptation? What presentations do they prefer? To answer these questions, we conducted an eye-tracking-based retrospective think-aloud study with 16 participants with ADHD, who watched and reflected on a curated set of video lecture segments. Our study uncovered video design elements that hindered learning and revealed participants' coping strategies along with their limitations. By jointly analyzing behavioral signals and retrospective reflections, we characterized how these experiences manifested in behavioral patterns. We further surfaced participants' practices for addressing learning needs beyond the video watching process, and derived design implications for future ADHD-friendly adaptive video learning systems.

---


### 33. [Uncertainty-Aware Sea-Ice Type Mapping with Multiple Ice Charts](https://arxiv.org/abs/2609.09451)

**<font color=#1a73e8>作者：</font>** Samira Alkaee Taleghan, Younghyun Koo, Andrew P. Barrett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sea-ice stage of development (SoD) describes the age and associated thickness of sea ice and provides important information for navigation, and operational ice monitoring. SoD labels are obtained from operational ice charts, where trained analysts interpret satellite observations and assign standardized stage codes to regions with similar ice conditions. These codes often represent ranges of compatible ice thicknesses rather than exact physical values. Deep-learning methods can automate SoD mapping and commonly adopt operational ice charts as reference labels for training. These annotations are not exact, however; this is because chart interpretation relies on analyst judgement and on the observations available at the time, so different ice services may assign different SoD labels to the same conditions. We term this variation across independently produced expert annotations multi-annotator label uncertainty; collapsing the annotations into a single deterministic target discards this variation. A second source of uncertainty originates in the learned model itself. In this paper, we quantify both sources: annotation uncertainty from disagreement among independent ice-service charts and model uncertainty from the learned predictive models. We then evaluate their relationship by testing whether model uncertainty is higher where ice services disagree. We observe that supervision incorporating information from multiple annotators can improve this correspondence, with soft supervision achieving the highest overall correlation of 0.256. The relationship becomes substantially stronger near the ice edge, where model predictive uncertainty closely tracks multi-annotator disagreement, reaching a correlation of 0.704 within 0--10 km. Among the uncertainty-estimation approaches, Monte Carlo dropout provides the best-calibrated confidence estimates, with an expected calibration error of 0.050.

---


### 34. [Exact-Form Regret for Gradient Descent, Mirror Descent and Follow-the-Regularized-Leader](https://arxiv.org/abs/2609.09466)

**<font color=#1a73e8>作者：</font>** Ashkan Soleymani, Gabriele Farina, Patrick Jaillet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online gradient descent is usually studied through external regret, where the learner competes with fixed alternatives. Recent work shows that first-order methods control richer action-dependent deviations. We ask for a geometric characterization of the deviations with respect to which online gradient descent, mirror descent, and follow-the-regularized-leader (FTRL) achieve no regret. We identify exactness as the common principle. Exactness means that the relevant displacement field is generated by a scalar potential, or equivalently that the associated one-form is exact in the geometry used by the algorithm. This geometry depends on the algorithm. For gradient descent it is Euclidean geometry, for mirror descent it is the geometry induced by the regularizer, and for FTRL it is the cumulative dual state. Under mild regularity conditions, exactness yields sublinear regret, while nonzero circulation provides the complementary obstruction and leads to linear regret. This gives a unified geometric framework for understanding the deviation classes controlled by these algorithms and reveals that different first-order methods can control genuinely different classes of deviations. These deviation classes have direct consequences for learning, particularly in games. We study the equilibrium notions induced by exact-form deviations and introduce conservative correlated equilibrium, reflecting both the conservative geometry of the underlying displacement fields and the restricted family of deviations available to the players. We characterize its relation to correlated equilibrium, determine when the resulting equilibrium notions coincide and when they separate, and show how these relationships depend on the geometry and the learning algorithm. Overall, this work gives a unified geometric account of what first-order online learning algorithms are no-regret with respect to, beyond fixed comparators.

---


### 35. [Exploring 3D Glyph Physicalizations for Public Engagement through River Health](https://arxiv.org/abs/2609.09472)

**<font color=#1a73e8>作者：</font>** Maria Teresa Ortoleva, Min Chen, Rita Borgo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Introduction: In this paper, we present the preliminary design of a toolkit for making glyph-based physicalizations for public engagement. We use London river health data as a case study: a data set of significance to urban issues related to climate change and of interest to draw public attention, as part of the Greater London Authority's strategies. Design: We present the components of a 3D glyph-making toolkit, its encodings, and a step-by-step process for crafting a physicalization of a river's water quality using recycled materials. We reason about how users can use the template to learn about a data set while reflecting on the data's significance to their personal experience and self-mapping onto the physicalization. Reflection: We reflect on the opportunities that extending the design space of glyphs to 3D physicalization offers for supporting public engagement with complex, multi-dimensional data sets, scaffolding cognitive processes, and self-reflection, thereby bringing crucial environmental data to life. Conclusion: Future implementation of the 3D glyph template will enable the public of all abilities to explore river health data, physicalize complexity, and realize its relevance. We hope that its use in public engagement workshops will help raise awareness, invite care, and foster a sense of belonging.

---


### 36. [LeCor: Learning to Be Corrected by Meta-Learned Test-Time Training for Interactive 3D Lung-Tumour Segmentation](https://arxiv.org/abs/2609.09477)

**<font color=#1a73e8>作者：</font>** Yi Luo, Yike Guo, Wenxuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Delineating lung tumours on computed tomography (CT) takes a considerable share of the time spent on radiotherapy planning, and a contour proposed by a model can be refined interactively by the clinician. Promptable foundation models such as SAM 3 support this workflow by writing each correction into a session memory that conditions the remaining slices, while the model weights stay fixed. On 690 test cases from five public CT cohorts, fine-tuning SAM 3 on lung tumours raises the Dice obtained from a single point prompt from 0.298 to 0.757, and seven rounds of corrections raise it further to 0.765, but under memory conditioning alone the accuracy on slices the annotator has not touched stops improving after six rounds. We therefore treat each correction as a training signal and propose LeCor, which performs test-time training on a small set of case adapters that are reset for every case and meta-learned such that a single gradient step driven by a click improves the slices that were not clicked. On the 133 test cases that span at least eight slices, LeCor raises the Dice reached after seven correction rounds from 0.787 with the fine-tuned model to 0.827, reduces the number of cases that never reach a Dice of 0.80 from 47 to 27, and reaches in three correction rounds the accuracy that the fine-tuned model attains in seven.

---


### 37. [Unthrottling the Tanh Jacobian in SAC: A Negative Result on Bang-Bang Control and MetaDrive](https://arxiv.org/abs/2609.09478)

**<font color=#1a73e8>作者：</font>** Faiq Shamass  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Soft Actor-Critic (SAC) represents a continuous policy as an unbounded Gaussian that is squashed by tanh. The Jacobian of that map is $\partial a/\partial u = 1-a^2$, which vanishes as $|a|\to 1$. A natural concern is that this throttle starves the actor of critic signal exactly where extreme actions (full brake, full throttle) are optimal. We test a minimal intervention that restores the missing signal: one extra term in the actor loss whose gradient on the pre-tanh mean is the detached action-gradient of $Q$, with no gain parameter.
On a minimum-time double integrator whose optimum is bang-bang at the action bounds, vanilla SAC already reaches near-optimal return ($-31.6$ vs. a calibrated optimum of $-30.3$) across ten paired seeds. An ungated bypass does saturate the policy (99% of eval steps with $|a|\ge 0.9$) and collapses return to $-195.5$. A gated bypass that fires only on the flat shoulder $|a|\in[0.9,0.999]$ also fails, and does so without leaving a saturated policy. Warm-started MetaDrive fine-tuning shows the same pattern: the bypass does not improve return, and where collision rate falls it is typically traded for out-of-road departures. Auto-tuned entropy coefficient rises against the bypass, which is a push toward the tails.
The Jacobian effect is real. Treating it as a bug to be undone is not free, and on the tasks studied here it is not helpful. Saturating a bound is not the same as solving a problem whose optimum lives on that bound.

---


### 38. [Integrating Multi-Source Feedback in Computational Design](https://arxiv.org/abs/2609.09483)

**<font color=#1a73e8>作者：</font>** Francisco Erivaldo Fernandes Junior, Thomas Langerak, Mira Keränen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In real-world design practice, evaluations rarely rely on a single source of judgment. Designers routinely combine expert opinions, empirical studies, and computational models, each with distinct strengths and limitations. While machine learning offers methods to integrate multiple feedback sources, these approaches remain largely inaccessible to designers without technical expertise. In this paper, we explore how to integrate multiple feedback sources, primarily through: (1) a practical approach for multi-source integration, and (2) its implementation in MUSE, a no-code tool that allows designers to combine and balance diverse sources. Our technical findings show that independent modeling of multiple evaluation sources enables exploration across heterogeneous feedback, accommodates different evaluation speeds, surfaces disagreements between sources, and supports an adaptable evaluation setup that designers can reconfigure during their process. In a visualization design study, participants navigated their own judgments alongside simulator feedback, reporting a perception of enhanced confidence and flexibility. Our results highlight the viability of multi-source integration to support computational design, offering a step toward bridging the gap between advanced optimization methods and design practice.

---


### 39. [Efficient Fairness Auditing Across Guidance Scales in Text-to-Image Diffusion Models via Causal Abstraction](https://arxiv.org/abs/2609.09486)

**<font color=#1a73e8>作者：</font>** Nabila Tasfiha Rahman, Rajatsubhra Chakraborty, Depeng Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness auditing of text-to-image diffusion models often requires generating large numbers of images across sampling configurations, making comprehensive evaluation computationally expensive. We propose a causal-abstraction-based audit instrument for efficiently evaluating fairness under interventions on the classifier-free guidance scale. Given a fixed prompt and a target feature function, we represent the diffusion process as a low-level structural causal model and construct a corresponding high-level model over abstract denoising states. We characterize the projected causal structure, establish identifiability of the fairness-relevant interventional query, and provide sufficient conditions under which the high-level model preserves this query. A probabilistic transformer implements the high-level model as an amortized predictor of target-feature distributions across guidance scales. Experiments evaluate distributional fidelity, fairness-query accuracy, and computational efficiency. We present two auditing demonstrations: one using standard Stable Diffusion 1.5 and another using StayFair, a fairness-enhanced Stable Diffusion model, to examine their behavior across guidance scales.

---


### 40. [Audio Deepfake Detection Using Temporal Coherence Analysis](https://arxiv.org/abs/2609.09489)

**<font color=#1a73e8>作者：</font>** Justin D. Norman, Sarah Barrington  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The proliferation of AI-generated audio (so-called "deepfake" audio) poses significant threats to information integrity, from voice cloning fraud to synthetic music copyright disputes. We present a temporal coherence analysis framework built upon Contrastive Language-Audio Pretraining (CLAP) embeddings that spans speech, instrumental music, and music with vocals. By computing pairwise cosine similarities between audio segment embeddings and extracting statistical features from the resulting distributions, we train lightweight ensemble classifiers that reliably distinguish authentic from synthetic audio. Our work provides an interpretable, computationally efficient alternative to common deep learning methods while still achieving competitive performance across speech and music domains. Further, we reveal two notable empirical findings about audio deepfakes: (1) a feature-label inversion phenomenon in which 21 of 29 statistical features reverse their discriminative direction between training and in-the-wild deployment, and (2) a speech--music direction reversal in which entropy discriminates in opposite directions for speech and music deepfakes.

---


### 41. [Learning Global Camera Poses from Noisy View-Graphs for Structure from Motion](https://arxiv.org/abs/2609.09491)

**<font color=#1a73e8>作者：</font>** Fadi Khatib, Meirav Galun, Ronen Basri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera pose estimation is a key step in 3D reconstruction and view-synthesis pipelines. We present a deep, global Structure-from-Motion framework based on learned view-graph aggregation. Our method employs a permutation-equivariant, edge-conditioned graph neural network that takes noisy pairwise relative poses as input and outputs globally consistent camera extrinsics. The network is trained without ground-truth supervision, relying solely on a relative-pose consistency objective. This is followed by 3D point triangulation and robust bundle adjustment. Our approach is efficient, scalable to more than a thousand images, and robust to graph density. We evaluate our method on MegaDepth, 1DSfM, Strecha, and BlendedMVS. These experiments demonstrate that our method achieves superior rotation and translation accuracy compared to deep track-centric methods while registering more images across many scenes, and competitive results compared to state-of-the-art classical pipelines, while being much faster.

---


### 42. [The Mutations of Machine Speech](https://arxiv.org/abs/2609.09496)

**<font color=#1a73e8>作者：</font>** Mauricio Figueroa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Algorithmic outputs now populate the digital environments through which contemporary life is organized. The role of law in facilitating and constituting (rather than merely responding to) these processes is gaining increasing traction across scholarly accounts. This inquiry traces the evolution of algorithmic outputs attending to their legal underpinnings and social implications, surfacing the mutations of machine speech.
The first mutation redefined speech as data to be queried: search engines transformed the web from a space of information retrieval into an economic regime of algorithmic visibility. The second mutation reframed speech as engagement: social media platforms fused moderation with amplification, turning expression into a metric of attention, governed by corporate architectures. The third mutation emerges in conversational systems and interfaces, where generative text displaces information retrieval, bringing with it dense technolegal entanglements and profound epistemic consequences.
Scholars of freedom of expression, informational privacy, and communication studies have long grappled with these dynamics, yet their implications for broader legal thought have also become urgent. This piece seeks to organize and clarify the evolving debate around algorithmic speech, making this critical but often fragmented discourse more accessible to wider legal and interdisciplinary audiences. In doing so, it bridges the gap between observing technological transformation and critically assessing the constitutive role of law within it, offering a conceptual resource for researchers, students, policymakers, and practitioners navigating and contesting this evolving landscape.

---


### 43. [RoMa-$Ω$: What Feed-Forward 3D Models Know About Image Matching](https://arxiv.org/abs/2609.09507)

**<font color=#1a73e8>作者：</font>** David Nordström, Xinyue Zhang, Thibaut Loiseau 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned image matching has experienced significant progress in recent years, culminating in robust and accurate matchers such as RoMa, whose robustness is often attributed to its use of frozen DINO features. In a parallel development, feed-forward reconstruction models, such as VGGT, have been trained on ever-growing datasets to accurately regress dense 3D point maps and camera poses. The distinction between matchers and feed-forward reconstruction models has become increasingly blurred with the introduction of matching losses in models such as MASt3R and VGGT-$\Omega$. This raises a natural question: what do feed-forward 3D models know about image matching? In this work, we answer this question by analyzing three scenarios: (i) zero-shot matching of patch features, (ii) direct matching of 3D point predictions, and (iii) training a full matcher on top of the learned representations. We find that, despite performing poorly in zero-shot matching, especially in later layers, feed-forward reconstruction models provide strong representations for linear probing and full matching pipelines. We further show that, even without any training, their raw predictions alone enable competitive matching, albeit only under moderate viewpoint changes and modality gaps. Based on these insights, we retrain RoMa v2 by replacing its DINO backbone with VGGT-$\Omega$. Our resulting model, \ours, outperforms state-of-the-art matchers on a wide range of benchmarks, e.g. +8.1 mAA compared to RoMa v2 on WxBS.

---


### 44. [AnimalLift: Reconstructing Animatable 3D Animals from a Single Image by Learning Canonical Shape, Texture, and Fur Maps](https://arxiv.org/abs/2609.09513)

**<font color=#1a73e8>作者：</font>** Chunyi Sun, Ruyi Zha, Weijian Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing a fully animatable 3D animal from a single image remains challenging because animation-ready assets require not only plausible geometry, but also a unified topology, editable appearance, and fur representations compatible with deformation and simulation. Existing image-to-3D approaches often rely on implicit or loosely structured representations that are difficult to rig or edit, while parametric animal models support animation but cannot capture detailed texture and fur appearance. We present AnimalLift, a framework for reconstructing structured, animation-compatible 3D animal assets with explicit fur from a single image. Our method lifts an input image into a shared canonical space with a consistent topology and UV parameterization across the dataset, enabling joint prediction of canonical geometry, texture, and fur in a unified feed-forward architecture. A key component of our representation is a UV-aligned fur map that encodes strand geometry in a surface-aligned canonical domain, allowing explicit fur reconstruction compatible with mesh deformation and fur simulation. To train the model, we introduce a procedural data generation pipeline that provides large-scale supervision with aligned geometry, texture, and fur across diverse animal species and appearances. Experiments on synthetic and real-world datasets demonstrate strong reconstruction quality and generalization across animal categories. Beyond reconstruction, our structured representation directly supports downstream applications including animation, pose transfer, fur editing, and simulation-compatible rendering.

---


### 45. [A Statistical Approach to Estimating Sample Size of Machine Learning Models](https://arxiv.org/abs/2609.09547)

**<font color=#1a73e8>作者：</font>** Dat Phan-Trong, Sunil Gupta, Svetha Venkatesh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sample size determination for machine learning (ML) prediction models is challenging because conventional power analysis typically requires the predictor-outcome relationship and effect structure to be specified a priori. Nonlinear ML models learn complex prediction surfaces that do not admit straightforward analytical power calculations. We propose a framework that approximates nonlinear ML models with localized linear representations and estimates sample size requirements by evaluating statistical power across these local regions.

---


### 46. [An Efficient and Effective Agentic Group Shilling Attack on Recommender Systems](https://arxiv.org/abs/2609.09551)

**<font color=#1a73e8>作者：</font>** Quoc Viet Nguyen, Trinh Pham, Viet Huynh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recommender systems have become core infrastructure for modern online platforms, personalizing content at scale and strongly influencing what users see, click on, and purchase. However, this dependence on user interaction also exposes them to shilling attacks, where malicious actors can inject fake profiles to distort item rankings and control visibility. Existing attacks often rely on target-specific fine-tuning or fixed profile templates, making them either difficult to adapt to different victims or easier to detect. To overcome these limitations, we propose the Agentic Group Attack System (AGAS), a coordinated shilling framework where a central Coordinator directs a group of role-switching worker agents to adaptively promote a target item across different victim families. The Coordinator dynamically adjusts the strategy when progress stalls or suppression signals increase, while workers pursue a shared objective and switch between active and inactive roles to avoid repetitive patterns. Under the same attack budgets and evaluation protocols, AGAS consistently surpasses strong baselines in target promotion while better preserving benign recommendation quality, weakening representative detectors, and achieving higher efficiency than prior attacks. These findings also emphasize that defending recommender systems may require mechanisms that can handle adaptive shilling campaigns, not just isolated fake-profile injections. Our code is available at this https URL.

---


### 47. [BuzzASR: A Swarm of 100+ Monolingual Speech Recognition Models](https://arxiv.org/abs/2609.09554)

**<font color=#1a73e8>作者：</font>** Shivam Singh, Aditya Yadavalli, Catherine Arnett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce BuzzASR, a collection of language-specialized fine-tuned Whisper models adapted for automatic speech recognition (ASR) in 102 languages. Large end-to-end Transformer-based ASR models such as Whisper have revolutionized ASR, but most prominent models are highly multilingual. As a result, these models often perform poorly on languages less well-represented in their training set. While it has long been known that effective language adaptation can be achieved through simple fine-tuning on monolingual data, this strategy has only been applied to a small number of languages. We massively scale up this simple approach to 102 languages covered in the FLEURS dataset, while also implementing a more complex language adaptation strategy that integrates monolingual tokenizer replacement and data augmentation using text-only fine-tuning. BuzzASR models outperform Whisper-large-v3 on 77 out of 102 languages, reducing character error rates (CER) by a factor of over 2.8 on average. Our models achieve state-of-the-art CER among open-source systems on 27 of 102 languages on the combined FLEURS and Common Voice test set. Our tokenizer replacement strategy yields an average 3.3x improvement in compression rate (characters per token) over Whisper's multilingual BPE, with gains of up to 21.7x. We release all models, code, and detailed results: this https URL

---


### 48. [Robust Industrial Cyber Physical Classification Using Neuromorphic Temporal Embeddings and Hybrid SNN XGBoost Under Machine Unlearning Attacks](https://arxiv.org/abs/2609.09564)

**<font color=#1a73e8>作者：</font>** Ammar Kamoona, Sajad Koushkbaghi, Mahdi Jalili 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The digitalisation of electrical distribution networks has increased the exposure of power-grid infrastructure to cyber attacks. Existing intrusion detection systems (IDSs), however, often rely on computationally expensive deep learning models that are difficult to deploy at the edge. Periodic retraining also exposes these systems to machine unlearning attacks, where selective data removal can degrade detection performance. We propose a hybrid Spiking Neural Network (SNN) and XGBoost architecture that combines efficient temporal encoding with a lightweight classifier and provides structural resilience to such attacks. The SNN is trained once on clean data and used as a fixed feature extractor, while only the XGBoost classifier is retrained during model updates. Evaluated on two real-world public power-system datasets, the proposed method achieves 99.9\% accuracy (F1-macro 0.999) on the Synchrophasor dataset and 95.0\% accuracy (F1-macro 0.943) on the MSU/ORNL dataset, outperforming standalone baselines. Under selective label-flipping attacks, the hybrid model loses only 0.9\% F1-macro at 10\% poisoning and delays target-class collapse from 60\% to 70\% poisoning compared with raw models. These results demonstrate that neuromorphic temporal encoding can provide both accurate cyber-attack detection and improved resilience to data poisoning in cyber-physical systems.

---


### 49. [Beyond Top Words: MonoTM for Topic Modeling with Interpretable Monosemantic Features](https://arxiv.org/abs/2609.09575)

**<font color=#1a73e8>作者：</font>** Una Joh, Bei Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Topic models summarize large text corpora, but top-ranked words often provide only a limited representation of topic semantics. Sparse autoencoders (SAEs) offer a way to move beyond word-level descriptors by extracting interpretable features from dense representations, yet how feature interpretability relates to topic-inference quality remains unclear. We introduce \textbf{MonoTM}, an interpretable topic modeling framework that decouples these roles. Across three benchmark corpora, we show that document--topic mixture estimation and semantic interpretation favor different SAE configurations and feature subsets. MonoTM estimates mixtures from the full SAE bag-of-features representation and, with them fixed, learns topic descriptors over a separate vocabulary of corpus-grounded semantic features. This design preserves global topic structure while representing topics with semantic units more meaningful than individual words, making them more useful for downstream corpus analysis.

---


### 50. [A Function-Space Approach to the Statistical Mechanics of Learning Dynamics](https://arxiv.org/abs/2609.09589)

**<font color=#1a73e8>作者：</font>** Yizhou Zhang, Weichen Wu, Lun Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep neural networks exhibit regular macroscopic behavior despite highly nonlinear dynamics in vast parameter spaces. We develop a statistical-mechanical description of learning directly in function space, treating parameter configurations as microscopic realizations and functions with their dynamical operators as macroscopic variables. For mean-squared loss, the exact error dynamics are governed by the learning operator \(M=JJ^\ast\). Combining the dynamical Boltzmann weight of the conditional stochastic dynamics with the parameter-space density of states, whose local curvature defines a statistical operator \(B\), and integrating over local fluctuations yields
$$ \Phi_{\mathrm{fluc}}(M;B)=\frac{\sigma_\xi^2}{2}\log\det(M^{-1}+B)+\mathrm{const}. $$
At fixed spectrum, this term is rotationally stationary when \([M,B]=0\), is minimized by pairing large eigenvalues of \(M\) with small eigenvalues of \(B\), and generates a local restoring contribution against rotational mismatch. For ReLU-type function spaces under mild stable statistical conditions, \(B=\sigma_\xi^2L^\ast\mathcal K L\), where \(L\) measures coarse-grained second-order structure. Thus the low-\(B\) sector corresponds, up to bounded anisotropy of \(\mathcal K\), to low structural curvature, implying a preference for faster relaxation along smooth, data-adaptive directions. These results identify function space as a natural macroscopic level for studying stable collective organization in learning.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-176](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
