# 📦 其他研究 | 2026年09月25日

> 本类共 **240** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-240](./part-05.md)

---

### 151. [CAST: Context- and Anomaly Structure-Conditioned Time Series Anomaly Generation](https://arxiv.org/abs/2609.27825)

**<font color=#1a73e8>作者：</font>** Haochen Zhang, Jie Peng, Songyuan Sui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomalous time series play a critical role in safety-critical domains, yet they are inherently scarce, heterogeneous, and costly to obtain. Existing time series generation methods predominantly focus on synthesizing normal data, providing limited value when anomalous samples are needed. We identify two fundamental challenges in anomaly generation: (i) the scarcity of anomaly data, and (ii) the heterogeneous morphological characteristics of anomalies. To address these challenges, we propose CAST, a Context- and Anomaly Structure-conditioned Time series anomaly generation framework with principled two-stage pretraining and finetuning strategy. In pretraining stage, we leverage abundant normal time series data to learn underlying system dynamics and substantially mitigate the limited availability of anomaly data. During finetuning, CAST explicitly conditions the generator on learned anomaly structure representations, enabling it to capture heterogeneous anomaly morphologies under similar contextual conditions. Extensive experiments on multiple real-world univariate and multivariate datasets demonstrate that CAST consistently outperforms state-of-the-art anomaly generation methods in terms of both generation fidelity and downstream task utility, highlighting the effectiveness of the proposed approach.

---


### 152. [A Non-Invasive Cloud-Based Migration Strategy for Post-Quantum Cybersecurity in Smart HVAC Systems: Architecture, Implementation, and Empirical Evaluation](https://arxiv.org/abs/2609.27828)

**<font color=#1a73e8>作者：</font>** Mahedee Zaman Moon, Kaysarul Anas Apurba, Md Hasibul Hasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Legacy smart HVAC controllers rely on vendor-cloud TLS secured by ECDH and RSA, both broken by Shor's algorithm, and typical 10-15 year lifespans mean today's devices remain in service through the quantum-threat era. Direct on-device post-quantum cryptography is infeasible: an ESP32-S3, representative of capable HVAC hardware, has only 339 KB free heap against the 900 KB ML-KEM-768 requires, and even classical ECDH-P256 keygen (111.93 ms) dwarfs hardware AES-128 (0.032 ms). We propose a non-invasive PQC proxy, requiring no device, firmware, or vendor-cloud changes, performing ML-KEM-768 encapsulation and ML-DSA-65 authentication (NIST FIPS 203/204) with AES-256-GCM session keys via HKDF, implemented with Open Quantum Safe liboqs on a Raspberry Pi 4B gateway. Over 500 runs, the post-quantum handshake (Steps 1-6) completes in 2.48 ms, 0.38 ms slower than classical baseline, with PQC computation around 8% of handshake time at 20 ms simulated round-trip network latency. The gateway sustains 443 sessions/second, 100% success under 32 concurrent connections, extrapolating to 3546 sessions/second on a 32-core cloud instance. Five side-channel tests, including verified in-place session-key zeroization and a fixed-vs-random TVLA timing analysis, found no exploitable timing leakage or susceptibility to man-in-the-middle attacks. The architecture is vendor-agnostic and becomes unnecessary once vendors adopt NIST PQC natively.

---


### 153. [From Reasoning Strings to Partial Orders: Verifier-Certified Rule Transport through Quotient Policy Optimization](https://arxiv.org/abs/2609.27833)

**<font color=#1a73e8>作者：</font>** Bang Xie, Hao Liu, Zhiyuan Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many computations admit several valid execution orders because independent subgoals or disjoint state updates can commute. Reinforcement learning with verifiable rewards usually treats each successful trace as a separate token sequence, so serialization choices can be mistaken for logical dependencies. We introduce Verifier-Certified Rule Transport (VCRT), which replays adjacent operation pairs with native verifiers. Pairs whose two orders are accepted and reach the same canonical state provide commutation certificates; rejected or state-changing reversals provide anti-diamonds. VCRT uses anti-diamonds to preserve genuine prerequisites and assigns policy credit to the total probability mass of each certified orbit. It also constrains post-swap consistency, source retention, and policy drift. We evaluate leave-one-environment-out transfer across ProofWriter, CLRS, and Lean through a shared anonymized relation-graph interface. All training and checkpoint decisions are frozen before held-out evaluation, which uses one greedy trajectory per item without search or verifier feedback. VCRT obtains a 77.60% macro pass rate versus 64.53% for the strongest matched baseline, a paired gain of 13.06 points (95% bootstrap CI [12.58, 13.54]). Lean accounts for most of this gain at 33.49 points, while ProofWriter and CLRS improve by 2.85 points on average. Mechanism tests consistently favor anti-diamond supervision, whereas No-Orbit is statistically indistinguishable from full VCRT. The evidence does not establish a general benefit from exact orbit aggregation.

---


### 154. [Security and Privacy in Large-Model-Driven Embodied Agents: Attacks, Defenses, and Future Directions](https://arxiv.org/abs/2609.27847)

**<font color=#1a73e8>作者：</font>** Lele Zheng, Tong Chen, Ke Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large-model-driven embodied agents integrate foundation models with perception, reasoning, planning, and physical action, extending conventional model-level risks into embodied closed loops. Existing studies on their security and privacy remain fragmented across different system components and operational stages, making it difficult to understand how risks arise, propagate, and ultimately affect physical behavior or sensitive information. This survey presents a lifecycle-based analysis of security and privacy in large-model-driven embodied agents. We organize existing research into five stages: model construction and supply chain, multimodal input and interaction, semantic reasoning and task planning, action execution and physical feedback, and long-term deployment. Within this lifecycle, we systematically review representative attacks, defenses, and evaluation methods. Our analysis shows that attack entry, consequence realization, and defense intervention often occur at different stages of the embodied closed loop. It further reveals substantial gaps in end-to-end protection, real-world evaluation, and long-term privacy governance. This survey provides a unified perspective for understanding current progress and identifying critical directions for securing large-model-driven embodied agents.

---


### 155. [Geometry-anchored PET-aware multimodal pseudo-CT synthesis for whole-body attenuation correction: the BIC-MAC Challenge](https://arxiv.org/abs/2609.27848)

**<font color=#1a73e8>作者：</font>** Xuan Loc Nguyen, Hoang-Loc Cao, Truong Thanh Hung Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The BIC-MAC challenge targets whole-body pseudo-CT synthesis from NAC-PET, Dixon MRI, and a 2D topogram for CT-less PET attenuation correction. We propose GeoPACT, a geometry-anchored multimodal framework that uses NAC-PET as the spatial reference and incorporates topogram and MRI features through gated residual fusion. Absolute coordinates and whole-body conditioning support anatomically consistent patch-based prediction. Training combines attenuation-map supervision with a differentiable PET-response surrogate to reduce errors relevant to downstream PET reconstruction. Full-resolution pseudo-CT volumes are generated using sliding-window inference without requiring CT or PET labels at test time.

---


### 156. [GaussianDS: Depth-supervised Semantic Gaussian Splatting for Scene Understanding](https://arxiv.org/abs/2609.27850)

**<font color=#1a73e8>作者：</font>** Yufei Zhang, Chenlu Zhan, Hongwei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting provides an efficient representation for 3D reconstruction, and recent extensions attach semantic attributes to Gaussians for open-vocabulary scene understanding. However, lifting view-dependent 2D foundation-model outputs into 3D space introduces cross-view inconsistencies and weak geometric grounding, leading to severe semantic drift and boundary leakage. We propose GaussianDS, a depth-supervised semantic 3DGS framework that treats semantic lifting as a supervision-alignment problem and jointly optimizes RGB appearance, rendered depth, and compact semantics from scratch. Specifically, GaussianDS organizes unordered multi-view images into a pose-aware pseudo-video trajectory to propagate view-consistent masks via SAM2. During joint optimization, scale-shift-aligned monocular depth supervision and depth total-variation regularization stabilize Gaussian geometry, while a depth-edge-aware refinement loss explicitly anchors semantic transitions onto physical geometric discontinuities. Extensive evaluations show that our end-to-end framework not only retains high-fidelity 3D reconstruction and real-time rendering, but also establishes superior semantic understanding. GaussianDS sets new state-of-the-art performance on LERF (60.5% mIoU) and 3D-OVS (97.79% mIoU, 90.28% mBIoU) by mitigating semantic leakage, while seamlessly facilitating downstream 3D object removal.

---


### 157. [Reachable Global Optimization in AI Systems: How Global Is Global?](https://arxiv.org/abs/2609.27855)

**<font color=#1a73e8>作者：</font>** Wesley Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly claim to optimize prompts, policies, architectures, plans, tool-use trajectories, reasoning traces, and test-time computation. This paper argues that such claims are underspecified unless they state the region actually reachable by the system that performed the optimization. We introduce Reachability-Induced Optimization (RIO), a model in which a generator, verifier, controller, memory, tools, and budget induce a reachable candidate region. The returned solution is therefore a best visited point, an approximate reachable optimum, or an exact global optimum only when additional certificates relate the reachable region to the full formal space. We prove reachable-optimality, false-globality, gap- decomposition, certificate, escape, pruning, and control-value results. The full benchmark record contains 66,150 executed trials over six known-optimum landscape families, seven control policies, 270 landscapes, and 35 runs per landscape-method. The online appendix includes raw trial records, aggregate tables, figures, benchmark code, validation scripts, and checksums. The results show that control can restrict, expand, or misdirect reachability, and that optimization quality, reachability quality, and control reliability must be reported separately.

---


### 158. [Agentic AI Cybersecurity Framework](https://arxiv.org/abs/2609.27856)

**<font color=#1a73e8>作者：</font>** Victor Kebande  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing scale, complexity, and dynamism of modern cyber threats have rendered traditional reactive cybersecurity mechanisms insufficient. This paper introduces an Agentic AI Cybersecurity Framework (AACF) designed to enable autonomous, goal-driven, and adaptive cyber defense operations. Unlike conventional systems that rely on predefined rules and human intervention, the proposed framework leverages agentic artificial intelligence to perceive environmental states, reason about potential threats, and execute context-aware responses with minimal supervision. The framework is structured into key functional layers, including perception, reasoning, decisionmaking, action execution, and feedback-driven learning, enabling continuous adaptation to evolving attack patterns. By integrating intelligent agents with real-time data analysis and automated response mechanisms, AACF supports proactive threat detection, dynamic risk assessment, and coordinated mitigation strategies across distributed environments. A conceptual architecture is presented, along with illustrative use cases demonstrating its applicability to intrusion detection, incident response, and autonomous security orchestration. The proposed framework contributes to the emerging paradigm of self-directed cybersecurity systems and provides a foundation for developing resilient, scalable, and intelligent defense infrastructures.

---


### 159. [Exact Minimax One-Bit Unbiased Compression: Heavy-Tail Necessity and Finite-Randomness Approximation](https://arxiv.org/abs/2609.27860)

**<font color=#1a73e8>作者：</font>** Tao Jiang, Minbo Gao, Shaowei Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A pointwise-unbiased one-bit compressor reconstructs every real input in expectation while transmitting one bit. For a scalar source $P$ with CDF $F$, mean $m$, and $\mathcal J(P)=\int_{\mathbb R}\sqrt{F(r)(1-F(r))}\,dr$, we prove that the infimum of the source-averaged reconstruction second moment over all public-coin one-bit codes unbiased on $\mathbb R$ is $m^2+\mathcal J(P)^2$. For regular full-support sources, a distribution-centered random-threshold code attains this value; a converse over arbitrary randomized binary encoders and an equality analysis characterize every attaining code up to null sets, bit relabeling, and public-seed refinement. For the Gaussian location family $\mathcal N(\mu,\sigma^2)$ with $|\mu|\le c\sigma$, the equal prior on the endpoint means is least favorable and the minimax value is $\sigma^2\Lambda_c^2$. Exact Gaussian minimax optimality forces a critical heavy tail: at the endpoint means, absolute moments are finite exactly for $p<3$, and $\Pr(W>t)=\Theta(t^{-3}/\sqrt{\log t})$. A Cauchy-mixture robustification inflates the second moment by at most $1/(1-\eta)$ while making every positive-order absolute moment finite. Finite-support public randomness with finite decoder means cannot achieve exact unbiasedness on $\mathbb R$, but a bounded-output approximation using exactly $R$ shared random bits has explicit bias and second-moment bounds converging to the minimax constant. Finally, coordinate allocation communicates exactly $B$ bits per Gaussian-gradient query. On Kim's continuous quadratic hard family, the expected optimization guarantee matches the lower bound in its dependence on $(\sigma,d,B,\varepsilon)$, and a finite-variance high-probability bound incurs only a logarithmic confidence factor.

---


### 160. [A hierarchy of faithfulness criteria for knowledge base completion](https://arxiv.org/abs/2609.27863)

**<font color=#1a73e8>作者：</font>** Olga Mashkova, Robert Hoehndorf  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graph completion is evaluated by ranking observed triples above randomly corrupted ones, which treats every unobserved fact as false. When the object being completed is a description logic knowledge base rather than a plain graph, the open world assumption and deductive closure make this inadequate: relative to the knowledge base, a candidate axiom is entailed, contradictory, or undetermined, and a model that cannot separate a logically impossible axiom from a plausible novel one is not merely less accurate but semantically incorrect. We ask what it means for a knowledge base completion model to be logically faithful, and whether current embedding models are. We define a hierarchy of four increasingly strict criteria, discrimination, logical admissibility, monotonic logical faithfulness, and probabilistic logical faithfulness, and prove that they form a strict chain of implications. We ground the strongest criterion in the relative model count $P(\alpha\mid\mathcal{O}) = \#(\mathcal{O}\cup\{\alpha\})/\#(\mathcal{O})$, which recovers the trichotomy at its endpoints and ranks undetermined axioms in between. Evaluating knowledge graph and logic-geometric embedding models on $\mathcal{EL}$ ontologies, with entailed, contradictory, and undetermined test sets generated by a reasoner, we find that ranking accuracy does not imply logical faithfulness and that none of the evaluated models is faithful across the hierarchy. The code is available at this https URL.

---


### 161. [What Changed? Drift Detection with Real, Virtual, and Incomparable Diagnosis](https://arxiv.org/abs/2609.27865)

**<font color=#1a73e8>作者：</font>** Kentaro Oda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sharing a deep encoder does not, by itself, fix the central confound of task-comparison scores. We show that cross-evaluated heads on a frozen shared representation inherit the extrapolation confound of shallow exchange scores: pure input rotations with fixed labels inflate a deep exchange score from about 0 to 0.80, while representation-novelty scores are blind in the complementary direction (flat under label permutations that change the task completely). Transplanting a conditional two-discriminator discrepancy into the embedding space resolves both blind spots: the functional axis stays within +-0.001 under rotations and tracks label-permutation drift mass monotonically. Built into a mixture-of-heads lifecycle, the two-axis gate attains better decision quality with fewer heads than exchange or novelty triggers at a matched training budget. On generalized category discovery, the same chunk-level functional axis separates semantic novelty from photometric shift with AUROC 0.98-0.99 where per-input OOD scores (MSP, Energy, Mahalanobis, KNN) sit near chance for that distinction. All findings replicate across frozen ImageNet-21k ViT-B/16 and self-supervised DINOv2 backbones on CIFAR-100, and extend to residual adapter pools with recurrence, where a null-calibrated novelty trigger never fires on mechanism changes while the two-axis gate handles them with full recurrence reuse. We state explicitly the common-factoring condition under which embedding-space conclusions transfer to the original mechanism.

---


### 162. [A Shared Encoder Is Not a Shared Task: Conditional Comparison for Deep Expert Pools](https://arxiv.org/abs/2609.27866)

**<font color=#1a73e8>作者：</font>** Kentaro Oda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sharing a deep encoder does not, by itself, fix the central confound of task-comparison scores. We show that cross-evaluated heads on a frozen shared representation inherit the extrapolation confound of shallow exchange scores: pure input rotations with fixed labels inflate a deep exchange score from about 0 to 0.80, while representation-novelty scores are blind in the complementary direction (flat under label permutations that change the task completely). Transplanting a conditional two-discriminator discrepancy into the embedding space resolves both blind spots: the functional axis stays within +-0.001 under rotations and tracks label-permutation drift mass monotonically. Built into a mixture-of-heads lifecycle, the two-axis gate attains better decision quality with fewer heads than exchange or novelty triggers at a matched training budget. On generalized category discovery, the same chunk-level functional axis separates semantic novelty from photometric shift with AUROC 0.98-0.99 where per-input OOD scores (MSP, Energy, Mahalanobis, KNN) sit near chance for that distinction. All findings replicate across frozen ImageNet-21k ViT-B/16 and self-supervised DINOv2 backbones on CIFAR-100, and extend to residual adapter pools with recurrence, where a null-calibrated novelty trigger never fires on mechanism changes while the two-axis gate handles them with full recurrence reuse. We state explicitly the common-factoring condition under which embedding-space conclusions transfer to the original mechanism.

---


### 163. [Evaluation Choices Decide the Forecasting Leaderboard: Evidence from a Production Marketplace Panel](https://arxiv.org/abs/2609.27867)

**<font color=#1a73e8>作者：</font>** Md Rezwanul Islam, Wael Mohammed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A forecasting benchmark reports which method won. We show that the answer is set by the evaluator's choices before any model is fitted. We benchmark 24 forecasting methods and one textbook reference, including six 2025-era time series foundation models, on a production marketplace panel of 1,887 business customers over 67 months. We hold the data, the horizon and the period fixed, and vary only the evaluation design. Three choices each reverse or dissolve a headline conclusion. Changing the unit of analysis from the market total to the individual customer moves our production baseline from second of nineteen, beaten by nothing, to twenty-third of twenty-five. Nineteen of its twenty-four challengers beat it there. Changing how much error is pooled decides whether a Diebold-Mariano test finds anything at all. Scoring prediction intervals rather than point forecasts reorders the field almost completely, with a rank correlation of 0.02 on intermittent demand. We then measure what the deployed system gets from this. Its selection rule captures 55% of the distance between doing nothing and choosing with hindsight. The reversal is not a quirk of our data. We ran the released protocol, unchanged, on the public M5 retail panel. The same baseline shape places first at the market total and last per series, beaten by everything, and a replayed selection rule closes 64.7% of the same floor-to-ceiling distance there. Adding five zero-shot foundation models to that roster changes who wins at the total, not the shape. The bands' blind spot travels too: conformal bands under-cover most on the spikiest items. Splitting our own panel into ever smaller groups turns the contrast into a curve: the baseline's rank worsens at every level of disaggregation. We release the evaluation protocol and report an error of our own that inverted a result before we caught it.

---


### 164. [TopoGS: Topology-Aware Anchor Feature Aggregation for Large-Scale 3D Gaussian Splatting](https://arxiv.org/abs/2609.27868)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Shiqiang Gong, Shengkai Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Octree-based 3D Gaussian Splatting organizes anchors into multi-level hierarchies for level-of-detail rendering, but features at different levels are typically optimized independently, leaving the octree topology underused during feature learning. We observe that uniform cross-level aggregation produces asymmetric effects: fine-level anchors benefit from coarse context, whereas coarse-level anchors require selective information from their descendants. We therefore propose TopoGS, a topology-aware anchor feature aggregation framework with two lightweight components. Hierarchical Anchor Coupling establishes bidirectional cross-level gradient pathways by fusing per-level context triplets with a residual MLP. Structure-Aware Containment Aggregation uses octree containment and hash-based matching to distinguish anchors with valid parent-child relations from isolated anchors, then applies soft weighting to accommodate varying topological sparsity. Experiments on ten scenes from Mill19, UrbanScene3D, Tanks & Temples, MatrixCity, and WHU show consistent improvements over state-of-the-art methods. TopoGS achieves average PSNR gains of 2.13, 1.78, and 0.29 dB over the strongest reported baseline on aerial, ground-level, and synthetic-cartographic scenes, respectively, while rendering faster and using less memory. Code is available at this https URL.

---


### 165. [False-science induction in autonomous scientific discovery](https://arxiv.org/abs/2609.27883)

**<font color=#1a73e8>作者：</font>** Hanbing Liang, Fujun Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Closed-loop discovery systems increasingly execute experiments and update decisions autonomously, turning record integrity into part of the experimental apparatus. We show that false-science induction arises when legitimate physical objects and measurements are paired incorrectly, driving neural surrogates to faithfully learn record-induced associations that do not correspond to the true object-outcome relationship while marginal data distributions remain unchanged. Across green fluorescent protein fitness and materials band-gap prediction loops, coherent paired misbinding systematically redirects experimental budgets toward low-performing basins, whereas same-volume random swaps have negligible effects. These observations identify error coherence, rather than raw error frequency, as the primary variable controlling this budget misallocation in the tested loops. The resulting binding identifiability boundary supports monitored-axis quarantines and feedback-conflict triage, which intercept over-concentrated proposals before execution and isolate the corrupted hypothesis axis.

---


### 166. [All modalities are equal, but video is more equal: Closing the Cross-Attention Gap in Joint Video Generation](https://arxiv.org/abs/2609.27901)

**<font color=#1a73e8>作者：</font>** Ohad Rahamim, Dvir Samuel, Idan Schwartz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video is a rich representation of a physical event, capturing appearance, geometry, motion, and temporal evolution. Other modalities, such as 3D body motion or audio, encode narrower aspects of the same event. We find that joint multimodal diffusion transformers exhibit a corresponding asymmetry in cross-modal correspondence: companion modalities develop strong correspondences to video, but the reciprocal correspondences through which they constrain video remain substantially weaker. We express both directions as comparable correspondence distributions over video tokens and define their disagreement as the reciprocal correspondence gap. We introduce RecCAR, standing for Reciprocal Cross-modal Attention Regularization, a KL regularizer that uses the well-established video-to-modality correspondence as a fixed reference and aligns the weaker modality-to-video correspondence toward it. Across joint video-motion and video-audio generation, RecCAR improves the Human Anatomy score from 0.69 to 0.75 and reduces audio-video desynchronization from 0.804 to 0.752, while improving overall generation

---


### 167. [A Resilience Recovery Method for Complex Traffic Network Security Based on Trend Forecasting](https://arxiv.org/abs/2609.27903)

**<font color=#1a73e8>作者：</font>** Sheng Hong, Tianyu Yue, Yang You 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Due to the rapid development of information technology, a huge and complex traffic network has been established across various sectors, including aviation, aerospace, vehicles, ships, electric power, and industry. However, because of the complexity and diversity of its structure, the complex traffic network is vulnerable to being attacked and faces serious security challenges. Therefore, this paper innovatively proposes a traffic network resilience recovery method based on resilience trend forecasting. In this paper, the risk value is introduced into the analysis of the network fault propagation process, and the Susceptible, Infectious, Recovered, Dead-Risk (SIRD-R) fault propagation model is established. The resilience model of traffic network, which encompasses real-time resilience and overall resilience, is constructed through the integration of network resilience bearing capacity and resilience recovery capacity. Ten, the resilience of complex traffic networks is forecasted by using long short-term memory networks, and the resilience recovery strategy of complex traffic networks based on forecasting is proposed. Finally, the effectiveness and scalability of the proposed method are demonstrated through experimental analysis conducted on a diverse range of complex traffic networks, affirming its applicability in real-world scenarios

---


### 168. [Spatiality-Frequency Domain Video Forgery Detection System Based on ResNet-LSTM-CBAM and DCT Hybrid Network](https://arxiv.org/abs/2609.27904)

**<font color=#1a73e8>作者：</font>** Zihao Liao, Sheng Hong, Yu Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As information technology advances, digital content has become widely adopted across diverse fields such as news broadcasting, entertainment, commerce, and forensic investiga?tion. However, the availability of sophisticated multimedia editing tools has significantly increased the risk of video and image forgery, raising serious concerns about content authenticity at both societal and individual this http URL address the growing need for robust and accurate detection methods, this study proposes a novel video forgery detection model that integrates both spatial and frequency-domain features. The model is built on a ResNet-LSTM framework enhanced by a Convolutional Block Attention Module (CBAM) for spatial feature extraction, and further incorporates Discrete Cosine Transform (DCT) to capture frequency domain information. Comprehensive experiments were conducted on several mainstream benchmark datasets, encompassing a wide range of forgery scenarios. The results demonstrate that the proposed model achieves superior performance in distinguishing between authentic and manipulated videos. Additional ablation and comparative studies confirm the contribution of each component in the architecture, offering deeper insight into the models capacity. Overall, the findings support the proposed approach as a promising solution for enhancing the reliability of video authenticity analysis under complex conditions.

---


### 169. [Global tree forecasters collapse at the hierarchical aggregate: a five-panel failure characterization](https://arxiv.org/abs/2609.27912)

**<font color=#1a73e8>作者：</font>** Md Rezwanul Islam, Wael Mohammed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global forecasting models pool many series and learn one shared function. Gradient-boosted trees are their most common form. We measure a failure of this design that has not, to our knowledge, been documented. Train a global tree on the individual series of a hierarchy, then ask it for the hierarchical aggregate. The aggregate sits far outside the model's training range, and the forecast collapses. The model under-predicts the total by 30-50x in our production deployment, and by up to 496x in a public M5 reconstruction. The mechanism is known: beyond its training range, a tree predicts a constant. It surfaces at the aggregate because the total dwarfs every training series. The cure is not new. Per-series scaling, the preprocessing step that Montero-Manso and Hyndman (2021) recommend, prevents the collapse. So do a weighted aggregate-level training row and seasonal differencing. Our contribution is the characterization. The collapse reproduces on five panels: a production business-to-business marketplace, a synthetic hierarchy, M5, Australian Tourism, and a public business-buyer panel. It holds on three tree libraries, is invariant across training seeds, and is statistically significant. Its onset is immediate and tracks a simple support bound: a scale gap of only 1.15x already costs a third of the total. No standard configuration change prevents it: pooling every hierarchy level into training fails at scale, and the one knob that fits linear models in the leaves softens it without curing it. Rolling the forecasts forward recursively separates the cures: the aggregate-row cure re-collapses, per-series scaling degrades but stays low, and only seasonal differencing keeps its one-step accuracy unchanged. We close with a three-step procedure for diagnosing and preventing the failure in deployed systems.

---


### 170. [Spread and Scale: What Determines Whether Test-Time Budget Allocation Pays](https://arxiv.org/abs/2609.27917)

**<font color=#1a73e8>作者：</font>** Jinhyung Bae  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural combinatorial optimization solvers generate many candidate solutions per instance and report the best one found, using the same sample budget for every instance regardless of difficulty. A companion study showed that reallocating a fixed budget toward harder instances can improve solution quality, but that the standard way of measuring this improvement is biased: deciding an allocation and evaluating it on the same data can manufacture an apparent gain even when none exists. This left open what property of a workload determines whether reallocation is worth doing, and whether a policy that spends part of the budget to decide how to allocate the rest still pays once that cost is counted.
This paper answers both questions through pre-registered confirmatory experiments -- analysis and verdict criteria fixed before data collection -- across three independently trained solvers and two ways of constructing harder workloads on the traveling salesman problem. Within the workloads we study, the deciding property is how varied the instances within a workload are in difficulty, not how difficult the workload is on average: a uniformly easy or uniformly hard workload offers little room for reallocation, while a mixed workload offers substantial room. A budget-aware policy that pays for its own information about instance difficulty recovers most, though not all, of the improvement available when that information is assumed free.
Every experiment was independently recomputed from its written specification, and every correction to an earlier version -- including two that weakened the paper's own claims -- is reported with the direction it moved the conclusion. The paper offers a specific empirical answer and a template for verifying that answer is not an artifact of how it was measured.

---


### 171. [Binary Quantized Neural Network Training Is W[1]-Hard Parameterized by Input and Output Dimensions](https://arxiv.org/abs/2609.27932)

**<font color=#1a73e8>作者：</font>** Tao Jiang, Minbo Gao, Shaowei Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ganian et al. (ICLR 2026) proved that quantized neural network training is fixed-parameter tractable when parameterized jointly by architecture treewidth, input dimension $\alpha$, and output dimension $\omega$, and left open whether $\alpha+\omega$ alone yields fixed-parameter tractability. We prove that 2-QNNT is W[1]-hard parameterized by $\alpha+\omega$. The hardness already holds with zero error on $D_k=\{(\xi^{(r)},\xi^{(r)}):0\le r\le k\}$, where every input equals its target, $|D_k|=\alpha=\omega=k+1$, and the examples form a coordinatewise prefix chain. It also holds when every non-source bias is fixed to zero. Under the Exponential Time Hypothesis, no algorithm runs in $f(\alpha+\omega)|I|^{o(\alpha+\omega)}$ for any computable $f$. The reduction starts from DAG edge-disjoint paths, converts edge capacity to vertex capacity with a directed line graph, and normalizes the result into a valid layered architecture. The key structural step is a one-flip routing equivalence: on the prefix-chain inputs, nonnegative binary weights make every activation monotone, and each required output transition has a weight-one predecessor making the same transition. Iterating this relation backward extracts a path from the unique changing input, while different transitions yield vertex-disjoint paths. In particular, every neuron on these inputs has only $k+1$ possible activation profiles.

---


### 172. [Shedding Light on Complex Bitcoin Mixer Transactions: 67-Fold Reduction in Unclassified Cases](https://arxiv.org/abs/2609.27933)

**<font color=#1a73e8>作者：</font>** Nikolay Larionov, Yekaterina Smolenkova, Yury Yanovich  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bitcoin's Unspent Transaction Output (UTXO) model enables public analysis of fund flows, but users often merge transactions into Shared Send Mixers (SSMs) to obscure these flows. Untangling SSMs to recover original subtransactions is an NP-complete problem. While a practical untangling algorithm exists, it fails to classify 1.4% of SSM transactions due to computational time limits. This paper introduces four novel heuristics that exploit structural weaknesses in real-world SSM transactions to resolve these timeout cases: preemptive grouping, connectable singleton, ambiguous pairing, and knapsack fallback. We provide theoretical proofs validating each heuristic and integrate them into an optimized pipeline. Applied to timeout transactions, our approach classifies 98.5% of previously unresolved cases, reducing the overall unclassified transaction rate from 1.4% to 0.021% of all SSM transactions. Our open-source implementation and comprehensive evaluation on the complete Bitcoin blockchain demonstrate that the heuristics effectively untangle previously intractable transactions, enabling more accurate flow analysis and deeper structural insights into cryptocurrency transaction patterns.

---


### 173. [Quality over Quantity: Semi-Supervised Detection of Illicit Bitcoin Flows via Feature Engineering](https://arxiv.org/abs/2609.27936)

**<font color=#1a73e8>作者：</font>** Yekaterina Smolenkova, Nickolay Larionov, Nikolay Ivanov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting illicit cryptocurrency transactions is hampered by extreme class imbalance, adversarial obfuscation, and a scarcity of reliable labels. While semi-supervised learning (SSL) offers a promising solution by leveraging unlabeled data, we show that its success is not guaranteed by data volume alone but is contingent on data quality. We introduce an SSL framework for detecting illicit Bitcoin flows in Shared Send Mixers (SSM) transactions, built on a comprehensive historical dataset comprising 163 million transactions. Our main conclusion is that the success of SSL depends on data quality rather than volume: high-fidelity features such as KeyLinker address clustering and Shared Send Untangling (SSU) complexity metrics achieve an F1 score of 0.84 on unlabeled data. Finally, we empirically show that common heuristics like One-Time Change (OTC), though abundant, introduce noise, while strategic reliance on higher-fidelity features like KeyLinker is essential. Our work establishes that in blockchain forensics, the path to better performance lies in smarter feature engineering for data quality, not just larger datasets.

---


### 174. [Enhancing Multiclass Malware Classification in Resource-Constrained Environments](https://arxiv.org/abs/2609.27950)

**<font color=#1a73e8>作者：</font>** Abdul Khalek Alve, Alif Rahman, Saadman Zaman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The emergence of multi-class malware attacks such as ransomware, spyware, trojans, etc., presents an increasing and serious threat to cybersecurity, particularly in resourceconstrained environments like IoT devices. Existing machine learning models have achieved nearly perfect accuracy in binary malware classification but fall short in terms of classifying malware families and individual malware. Additionally, the complexity of these multi-class malware attacks presents a significant challenge of detection in resource-constrained environments, as multi-class detection usually requires high computational capability. This research bridges the gap by enhancing the detection accuracy of multi-class malware classification as well as developing a lightweight model that can run efficiently on resource-constrained devices. In this paper, we propose a robust, lightweight machine learning model featuring LightGBM classifier with SMOTE oversampling and SOM-US undersampling techniques for data balancing, as well as well-engineered feature selection through Genetic Algorithm. The model performed better than the current state-of-the-art models developed on the same dataset in both malware family classification (4 classes) and individual malware type classification (16 classes) with accuracy of 89.1% and 76% respectively. Thus, maintaining a balance between classification accuracy and computational efficiency in resource-constrained environments. Furthermore, we propose another model using Random Forest classifier with an accuracy of 91.2% in malware family classification and 78.7% in individual malware classification. Demonstrating a significant enhancement in terms of accuracy from the current state-of-the-art models.

---


### 175. [ScoutNeRV: Rapid Encoding of Grid-Based Video INRs via ScoutNet](https://arxiv.org/abs/2609.27958)

**<font color=#1a73e8>作者：</font>** Naser Alizada, Farhang Baghban, Hashem Pishkar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) have emerged as a promising paradigm for video compression, providing compact neural representations with flexible spatial and temporal reconstruction. Hierarchical grid-based architectures such as HiNeRV achieve strong rate--distortion performance, but require extensive per-video optimization, resulting in high encoding costs. To address this limitation, we propose ScoutNeRV, a content-adaptive initialization framework for accelerating the optimization of hierarchical video INRs. ScoutNeRV employs a lightweight, offline-trained scout network that analyzes a small number of sampled frames and selects a suitable pre-trained expert from a memory bank through hard routing. The hierarchical grid and decoder parameters of the selected expert are then transferred to initialize the target HiNeRV model before video-specific fine-tuning. On the unseen ReadySetGo sequence, ScoutNeRV achieves an initial PSNR of $34.95$~dB, compared with $13.70$~dB for standard initialization, corresponding to a $21.25$~dB improvement before fine-tuning. After only 37 epochs, ScoutNeRV reaches $36.92$~dB and remains within $0.42$--$0.80$~dB of the 300-epoch HiNeRV baseline across the evaluated rate--distortion configurations. Furthermore, the proposed initialization achieves a $9.25\times$ wall-clock speedup in the reported runtime experiment. These results demonstrate that content-aware expert initialization can substantially reduce the optimization cost of hierarchical video INRs while retaining competitive reconstruction and compression performance. The code is available at this https URL.

---


### 176. [I-SplineFlow: Learning Monotone Spline Stochastic Interpolant Schedulers for Few-Step Generation](https://arxiv.org/abs/2609.27963)

**<font color=#1a73e8>作者：</font>** Md Sakib Hossain Shovon, Md Rifat Ur Rahman, Md Abtahi Majeed Chowdhury 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Few-step generation with pretrained diffusion and flow models can be accelerated by lightweight training that optimizes the sampling trajectory rather than the network. A recent approach parameterizes the stochastic interpolant (SI) scheduler as a smooth curve whose control points enforce the three properties an SI scheduler must satisfy: fixed boundary conditions, a monotone signal-to-noise ratio (SNR), and differentiability. Existing parameterizations use globally supported polynomial bases, where every control point moves the whole curve and higher expressiveness needs a higher degree, which couples distant regions of the schedule during optimization. We introduce \emph{I-SplineFlow}, which parameterizes the scheduler with integrated monotone splines (I-splines). I-splines decouple the polynomial degree from the number of mixture weights, so support width and smoothness can be chosen per model at a fixed weight count, and the compactly supported derivative basis makes the scheduler Jacobian orders of magnitude better conditioned than a Bézier basis. Boundary conditions and a strictly monotone SNR hold by construction, with no ordering constraint on the parameters and closed-form velocity derivatives. Across diffusion (EDM) and flow (ReFlow, Simple ReFlow) models, I-SplineFlow improves few-step FID over Bézier scheduling in most settings, most clearly at the lowest NFEs, and trains in minutes. Ablations show that both the degree freedom and the monotonicity constraint are needed. The code will be released upon acceptance.

---


### 177. [Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery](https://arxiv.org/abs/2609.27980)

**<font color=#1a73e8>作者：</font>** Rasmus Aagaard, Nicki Skafte Detlefsen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pruning large pre-trained transformer-based ASR models such as OpenAI's Whisper has seen great adoption, as pruning the decoder led to significant end-to-end transcription speedups. For instance, the {\tt whisper-large-v3-turbo} variant reduced the decoder from 32 to 4 layers, while Distill-Whisper similarly reduced the decoder to only 2 layers. Although some attention has been put towards reducing the size of the encoder, no approach has seen wide adoption. This could be due to the need for custom inference implementations to take advantage of the compressed model. We present an approach that ranks encoder layers by the leave-one-layer-out change in Word Error Rate (WER). The six layers that cause the least change are removed, corresponding to $18.5\%$ of the encoder stack. The pruned model requires no custom inference code as it is simply a more shallow encoder with fewer layers. We further distill using unlabeled monolingual speech data to recover performance degradation caused by the zero-shot layer pruning. Mean WER across four languages increases to $20.1\%$ after distillation, compared to $21.9\%$ zero-shot, going from a baseline of $18.2\%$. We release all of our code (this https URL) and the pruned model (this https URL).

---


### 178. [Relative Discharge Stage (RDS) Classification: A Practical Indicator of Battery Discharge Progress](https://arxiv.org/abs/2609.27986)

**<font color=#1a73e8>作者：</font>** Khoa Tran, Tri Le, Hung-Cuong Trinh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate remaining discharge time (RDT) prediction is challenging in real-world battery applications because future load profiles are unknown and highly dynamic. To address the uncertainty of continuous RDT regression, this paper introduces Relative Discharge Stage (RDS), a battery-management indicator that represents the remaining discharge condition using five interpretable classes: Normal, Good, Moderate, Low, and Recharge Required. Unlike state of charge (SOC), which reflects the current charge level, RDS characterizes the remaining discharge process without requiring future-current information during inference. A physics-informed RDS classification framework is proposed, combining SOC estimation with lightweight temporal learning. The SOC-estimation component includes second-order ECM state and terminal-voltage prediction, hysteresis and OCV temperature correction, core-temperature estimation, and AEKF state correction, supported by OCV evaluation, online STC-ECM parameter adaptation, and pretrained neural residual-voltage correction. The measured current, terminal voltage, surface temperature, and estimated SOC are arranged into a sliding observation window and processed by a lightweight temporal convolutional network. Experiments on two public lithium-ion battery datasets demonstrate robust RDS classification, with accuracy exceeding 80% under varying load and thermal conditions.

---


### 179. [Task-Induced Riemannian Metrics for Vision Transformer Feature Spaces](https://arxiv.org/abs/2609.27988)

**<font color=#1a73e8>作者：</font>** Andrew Bond, Ege Erdem Özlü, Tuna Çimen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Methods operating on Vision Transformer (ViT) feature spaces typically rely on Euclidean distance or cosine similarity. This assumes that every direction is equally meaningful, but there is no reason to believe the true task geometry has this property. The task-sensitive geometry of the feature space is given by the pullback metric $g(F) = J(F)^\top J(F)$, where $J$ is the Jacobian of the decoder's output fed to a task-specific distance, with respect to the features. Storing the full $g$ is infeasible at modern scales, and for dense outputs such as depth maps even forming $J$ is impractical. We show that whether a low-rank approximation of this metric can be learned depends on the model-decoder pair, and we characterize this with a matrix-free diagnostic $\kappa_{cap}(r)$ computable with a low number of Jacobian-vector products. For tractable pairs, we develop the Spectral Pullback Network (SPN), which learns a low-rank version of the metric from randomized power iteration, and we distill it into a $310$K-parameter importance head that predicts token importance directly from the features. When the Jacobian spectrum is too spread out for a low-rank approximation, passing the decoder's input features through a VAE bottleneck can restore tractability. Across DPT, DINOv2, CLIP, and VGGT backbones, $\kappa_{cap}(r)$ predicts which learned-metric architectures are viable. The importance head reaches Spearman $\rho = 0.998$ on DINOv2 CLS, and our geometric token pruning reduces the additional depth error of ToMe-based token selection by $25\%$ on DPT depth at prune ratio $0.5$, without fine-tuning the ViT. Project page: this https URL

---


### 180. [PISCES: Physics-Informed Solar-wind Convolutional autoEncoder for Space-weather Anomaly Detection and Early Warning](https://arxiv.org/abs/2609.28022)

**<font color=#1a73e8>作者：</font>** Kevin Lee, Alison J. March  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Space weather early warning depends on detecting solar wind transients in in-situ measurements at the first Sun-Earth Lagrange point (L1), before they reach Earth. Fixed thresholds can miss combined magnetic and plasma structure, and many learning methods provide a single anomaly score. We present the Physics-Informed Solar-wind Convolutional autoEncoder for Space-weather (PISCES), a convolutional autoencoder trained without catalog labels on OMNI solar wind measurements under physics constraints. Its loss includes magnetic field consistency, an empirical relation between temperature and velocity, the Parker spiral angle, and penalties on changes between consecutive one-minute samples in derived quantities calculated from the reconstruction. At inference, PISCES separates the anomaly score into magnetic and plasma reconstruction errors, physics relations, and residual corrections, and reports the magnitude of each contribution. Attenuation of the skip connections, selected on validation data, improves average precision for the trained models, while the untrained scores remain nearly the same. The trained models also give a more consistent ordering of these physical contributions. After smoothing with a trailing median, the alarms can precede independently observed sudden commencements, including positive sudden impulses.

---


### 181. [A Native-Reference Coordinate Geometry for L2 Pronunciation Deviation Using Self-Supervised Speech Models](https://arxiv.org/abs/2609.28060)

**<font color=#1a73e8>作者：</font>** Tina Raissi, Nhan Phan, Mikko Kurimo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-supervised speech models encode rich phonetic information, but it remains unclear how to transform this information into interpretable metrics for second-language (L2) pronunciation assessment in spontaneous speech. We propose a native-reference coordinate geometry in which phone-class averages from native speech define a low-dimensional reference subspace, and L2 speech is evaluated by its distance to matching native phone-class coordinates. Unlike prior distance-based approaches, our method does not require parallel recordings with matched linguistic content or dedicated pronunciation labels. Across different self-supervised encoders and modeling choices, the resulting native-reference distances show negative Spearman correlations up to -0.5 with speaking proficiency, indicating that higher-proficiency speakers tend to lie closer to the native-reference space.

---


### 182. [AstraLOD3: Zero-shot multimodal agentic reconstruction of LOD3 building models](https://arxiv.org/abs/2609.28061)

**<font color=#1a73e8>作者：</font>** Bryan G. Pantoja-Rosero  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated LOD3 building modeling typically relies on purpose-built geometric or learning-based pipelines, limiting flexibility across heterogeneous buildings and input evidence conditions. This study investigates whether Astra, a general-purpose multimodal foundation model, can address these limitations through zero-shot reconstruction of LOD3 building models within an agentic framework under bounded autonomy. AstraLOD3 combines multi-view images, calibrated cameras, and a filtered sparse SfM point cloud with a natural-language reconstruction specification, while the Astra agent dynamically selects and executes computational procedures using Python and Blender. Across 35 runs, including 24 benchmark buildings, AstraLOD3 achieved a mean FRDS of 0.9647 and geometric agreement comparable to that of previous purpose-built methods. Controlled ablations further revealed the effects of reconstruction guidance, evidence modalities, model configuration, and run-to-run variability. The results demonstrate that structured LOD3 reconstruction can be formulated as a constrained agentic process rather than as a fixed pipeline. Future work will investigate adaptive refinement, user-guided correction, task-specific specialization, and damage-aware reconstruction.

---


### 183. [SlackDrive: Reclaiming Runtime Slack for Adaptive Driving Inference](https://arxiv.org/abs/2609.28064)

**<font color=#1a73e8>作者：</font>** Xiaohuan Pei, Hengguang Zhou, Yuanhao Ban 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Driving world-action models improve planning by coupling multimodal reasoning with future prediction, but their growing inference cost increasingly conflicts with the real-time latency requirements of vehicle control. Existing acceleration methods reduce tokens, layers, or sampling steps with policies selected prior to deployment, yet leave residual runtime variation largely unexploited after offline profiling and static scheduling on shared onboard compute. We observe that the largest admissible compute budget varies systematically with the residual runtime state, while recent realized latency provides a direct signal of the available compute slack. Motivated by this observation, we propose \textbf{SlackDrive}, a pre-inference compute allocator that reuses realized latency to select the compute budget of each control step before model execution. SlackDrive profiles the latency and planning utility of a small discrete budget set once, estimates online compute state from completed forwards, and selects the highest-utility budget predicted to remain within the admissible latency envelope, complementing existing profiling and resource scheduling while preserving the driving backbone and its compute actuator. On NAVSIM v2 with DriveDreamer-Policy, SlackDrive improves latency-constrained EPDMS by $21.7\%$ over the strongest baseline under a stringent latency regime, while the full-budget model and preconfigured token-pruning baselines exceed the admissible latency envelope under runtime contention.

---


### 184. [TEEP-RCNN: Texture-Enhanced Edge-aware Perception for Steel Surface Defect Detection via Improved Convolutional Block Attention in Faster R-CNN](https://arxiv.org/abs/2609.28077)

**<font color=#1a73e8>作者：</font>** Kirtan Rajesh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Steel surface defect detection is critical for automated industrial quality control but remains challenging due to subtle inter-class texture differences and pronounced class imbalance. We introduce TEEP-RCNN (Texture-Enhanced Edge-aware Perception Region-based CNN), a two-stage detector built on Faster R-CNN with a Feature Pyramid Network backbone and an improved Convolutional Block Attention Module (CBAM). Our CBAM adds dropout regularization in the channel attention MLP and batch normalization on the spatial attention branch, reducing co-adaptation and stabilizing gating logits. Training uses a differential learning rate protocol with cosine annealing warm-up, separating update rates for the pre-trained ResNet-101 backbone and the detection head. At inference, predictions are refined via Test-Time Augmentation fused with Weighted Box Fusion (WBF), improving localization stability on elongated and boundary-adjacent defects. On the NEU-DET benchmark across six defect categories, TEEP-RCNN achieves 73.3\% mAP@50 and 37.9\% mAP@50-95 in only 10 training epochs on a single GPU, competitive with YOLOv11m (76.2\% mAP@50, 100 epochs) while outperforming it on the rolled-in-scale category under the COCO metric. Per-class analysis shows the spatial attention branch is most effective on elongated texture defects such as patches and scratches, while crazing remains an open challenge across both paradigms due to its distributed non-local texture structure.

---


### 185. [LiAM-SAM: Lifecycle-Aware Memory for Robust SAM2-Based MOT](https://arxiv.org/abs/2609.28078)

**<font color=#1a73e8>作者：</font>** Grégoire Francisco, Alessandro D'Amico, Samuele Costantini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation-based multi-object tracking (MOT) with foundation video models such as SAM2 offers strong localization quality, yet remains fragile in crowded, real-world scenes. In detector-prompted SAM2 pipelines, failures typically arise at three stages of the object lifecycle: (i) erroneous or duplicate track initiation, (ii) memory drift during close interactions, and (iii) unreliable re-identification after long occlusions or re-entry. These errors corrupt object memory and accumulate over time, making long-horizon tracking unstable. In this paper, we reframe MOT as a lifecycle memory integrity problem. We present LiAM-SAM, a Lifecycle-Aware Memory (LiAM) framework with targeted mechanisms for each of the three failure modes. At track birth, to prevent faulty or duplicate initiations, we apply contrastive track initiation, which conditions each prompt on existing nearby tracked instances. To preserve memory integrity during strong interactions, we introduce motion- and geometry-grounded memory correction that resolves interaction confusions and suppresses drift. For reliable re-identification after disappearance, we maintain an adaptive context memory that promotes diverse and trustworthy references as long-term identity anchors. Finally, similarity aware spatial pruning optionally selects the memory tokens to retain at cross-attention time, improving efficiency with minimal accuracy loss. LiAM-SAM represents a modular, detector-agnostic, SAM2-based MOT system that achieves state-of-the-art HOTA and IDF1 on the evaluated benchmarks. In association-challenging environments, our ablations show that LiAM improves a detector+SAM2 baseline by +10.5 HOTA, +17.4 AssA, and reduces identity switches by 96%.

---


### 186. [Reference-Based Analysis of Coherence and Diversity in Open-Ended Text Generation](https://arxiv.org/abs/2609.28080)

**<font color=#1a73e8>作者：</font>** Esteban Garcés Arias  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating open-ended text generation involves understanding how different properties of a continuation relate to its perceived quality. We present a reference-based framework for examining coherence and diversity through three perspectives: aligning their evolution with human trajectories, comparing their summaries with a human continuation of the same prompt, and estimating their likelihood under a human reference distribution. Experiments with human quality ratings suggest that diversity-based alignment and mean-based comparisons capture quality-related variation, although the comparisons do not establish a predictive advantage for temporal alignment over simpler baselines. Reference likelihood also shows positive associations with ratings, with results varying across reference configurations and scoring horizons. Together, these analyses provide a structured way to examine how measured coherence and diversity relate to human judgments, while distinguishing similarity to human references from quality itself. Code and analysis resources are available at this https URL.

---


### 187. [ZoomDiff: A High-Fidelity Diffusion Model for Dual-Camera Smooth Zooming](https://arxiv.org/abs/2609.28083)

**<font color=#1a73e8>作者：</font>** Jiayi Zhang, Renlong Wu, Yukang Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital zoom transitions between dual cameras often exhibit conspicuous discontinuities in geometric structure and chromatic consistency, degrading the user experience. While recent dual-camera smooth zoom (DCSZ) methods attempt to mitigate this by fine-tuning frame interpolation (FI) models on DCSZ data, they struggle with the large cross-view disparities and complex geometric transformations. Considering that the generative prior of diffusion models is suitable for addressing this problem, we explore their application to DCSZ. However, naively applying existing diffusion-based FI models still yields low-fidelity transitions due to insufficient conditional guidance, high-frequency information loss during VAE encoding, as well as inadequate temporal consistency. To address this, we propose ZoomDiff, a high-fidelity diffusion model that leverages dual-camera inputs in both latent and pixel spaces for photo-realistic transitions. Specifically, we first strengthen dual-image conditional guidance during the multi-step denoising process to improve geometric consistency. Then we inject flow-aligned multi-scale features from the VAE encoder into the VAE decoder to recover high-frequency details, where flow-guided temporal consistency supervision are introduced to produce more smooth transitions. Extensive experiments on both synthetic and real-world datasets demonstrate that ZoomDiff outperforms state-of-the-art methods quantitatively and qualitatively. Project page: this https URL.

---


### 188. [Curriculum Learning with GNN-based Reinforcement Learning for Job Shop Scheduling](https://arxiv.org/abs/2609.28085)

**<font color=#1a73e8>作者：</font>** Jayakrishnan K. Vasudevan, Jonathan Hoss, Noah Klarmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The job shop scheduling problem is a challenging combinatorial optimization problem, and recent reinforcement learning approaches using graph neural networks have shown promise for learning scheduling policies directly from problem instances. However, training on large instances remains computationally expensive, and generalization across instance sizes remains challenging. This paper studies curriculum learning for graph neural network-based reinforcement learning in the job shop scheduling problem by comparing it with single-size training across three target sizes: 20 x 20, 25 x 25, and 30 x 30. In the curriculum setting, the policy is first trained on smaller instances and then progressively adapted to larger target sizes, allowing scheduling behavior learned in earlier stages to support learning on larger instances. Models are evaluated on unseen instances from 8 x 8 to 30 x 30 using the optimality gap, considering both generalization across all evaluation sizes and specialization on the target size. Results show that curriculum learning consistently reduces wall-clock training time, with larger benefits as the target size increases. The strongest advantage is observed at 30 x 30, where curriculum learning reduces the mean optimality gap across all evaluation sizes by approximately 8.1 percentage points, reduces the target-size mean optimality gap by approximately 8.6 percentage points, and saves approximately 50 hours of training time.

---


### 189. [LAYERSCOPE: A Layerwise Characterization of Video and Multimodal Learned Representations](https://arxiv.org/abs/2609.28086)

**<font color=#1a73e8>作者：</font>** Sandra Arcos-Holzinger, Debashish Chakraborty, Rohita Mocharla 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose LAYERSCOPE, a label-free, layerwise framework that aims to characterize a model's learned representations in video and multimodal settings. Evaluating downstream performance using representations from final or intermediate layers typically requires large amounts of labeled data, repeated task-specific evaluations, and substantial computation. To address these limitations, LAYERSCOPE uses local, global, distributional, and correspondence-based geometric metrics to compare layerwise representation structure within and across models without requiring task-specific labels. We evaluate seven architecturally diverse models across video and multimodal classification, clustering, and text-to-video retrieval tasks from MVEB/MVEB+. We find that intermediate-layer representations can outperform final-layer and model-default outputs. We also find that no single geometric metric consistently predicts downstream performance, but note that distinct layerwise geometric signatures emerge across model families. LID shows task-dependent relationships with performance, while RankMe provides the strongest measure for classification and clustering, but is not a universal layer selector. We also find that pairing-aware metrics explain retrieval better than distributional distances alone. LAYERSCOPE therefore offers a framework for comparing representations across models and layers, enabling a more systematic evaluation in video and multimodal settings.

---


### 190. [Discovery of fully efficient fault indicators along a data-based diagnosis process](https://arxiv.org/abs/2609.28087)

**<font color=#1a73e8>作者：</font>** Igor Bezmaternykh, Louise Travé-Massuyès, Elodie Chanthery  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of model-based and data-driven paradigms provides a powerful framework for fault diagnosis by combining the interpretability of analytical redundancy relations, i.e., input-output relations that are used as diagnosis indicators in model-based diagnosis, with the adaptability of learning techniques. DT4X is a recent diagnosis algorithm that uses symbolic regression to generate multivariate relations leveraging some properties of analytical redundancy relations and uses them as split functions in a decision tree. However, its symbolic regression procedure optimizes only the separation between two selected classes at each node, often fragmenting the remaining classes and degrading both interpretability and diagnosis performance. This paper introduces DT4X+, an enhanced version of DT4X that modifies the construction of training sets and the symbolic-regression loss so that expressions separate the target classes while preserving the coherence of non-target classes. The resulting relations become fully consistent with ARR properties and lead to more informative splits, improved robustness, and better performance on dynamic-system datasets. Experiments conducted on several benchmark systems demonstrate the benefits of this enhanced formulation.

---


### 191. [MotionSpec: Spectral Trajectory Supervision for Motion-Consistent Video Generation](https://arxiv.org/abs/2609.28095)

**<font color=#1a73e8>作者：</font>** Ziqi Ni, Rui Li, Shiqi Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-to-video generation have enabled high-fidelity visual synthesis, yet realistic motion remains challenging. Generated videos may exhibit temporal discontinuities, inconsistent action progression, and structural distortions during complex movements. Even when individual frames appear realistic, the underlying motion may evolve in inconsistent or implausible ways. Standard generative objectives provide limited motion-specific supervision, leaving motion evolution insufficiently constrained. In this paper, we propose MotionSpec, a motion supervision framework centered on Spectral Trajectory Consistency (STC). STC constructs dense anchor-relative motion trajectories and transforms them into motion spectral volumes via a temporal Fourier transform. By aligning the spectral amplitude and phase of predicted and target trajectories, STC constrains both motion strength across temporal frequencies and the temporal organization of motion. To complement this trajectory-level supervision, we introduce Local Flow Consistency (LFC), which aligns consecutive-frame optical flow between predicted and target videos to stabilize local motion transitions. Experiments demonstrate that MotionSpec consistently improves motion consistency, temporal coherence, and plausibility while preserving visual fidelity.

---


### 192. [Visual Tripwires: Anticipating Failure in Deep Vision Systems](https://arxiv.org/abs/2609.28099)

**<font color=#1a73e8>作者：</font>** Anoushka Harit, Rehan Zuberi, William Prew 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep vision systems remain vulnerable to corruption, occlusion, and distribution shift despite strong benchmark performance. Existing reliability methods typically evaluate uncertainty at individual time steps and do not explicitly model how a system progresses toward failure. We introduce Visual Tripwires, a predictive reliability framework that uses temporal instability in model behaviour to anticipate impending failure. Our central hypothesis is that predictive degradation develops progressively through measurable changes in latent representations, prediction trajectories, and attention structure. Visual Tripwires captures these changes using representation drift, prediction oscillation, trajectory curvature, and attention entropy. A lightweight tripwire predictor aggregates these signals over a temporal window to estimate the probability of failure within a future prediction horizon. Experiments across multiple datasets, architectures, and progressive perturbation settings show that the proposed instability signals emerge before predictive degradation and provide earlier and more accurate failure warnings than conventional uncertainty estimation methods. These results demonstrate that temporal instability contains useful information about future model reliability and provides a practical basis for early warning in deep vision systems.

---


### 193. [Fed-ReMasker: Federated Tabular Imputation under Feature-Level Missingness](https://arxiv.org/abs/2609.28105)

**<font color=#1a73e8>作者：</font>** Ioannis Papathanail, Rooholla Poursoleymani, Lubnaa Abdur Rahman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-center clinical studies and biomedical research collaborations increasingly seek to utilize data across centers to build models that generalize beyond any single center. This creates two distinct challenges: data protection regulations may restrict the sharing of raw patient data across institutions, while centers may collect only partially overlapping sets of features under different protocols. Federated learning enables collaborative model training without centralizing raw data. However, existing federated imputation methods rarely evaluate feature-level missingness, in which entire features are unobserved at some centers. To address this setting, we adapt the ReMasker masked autoencoder to federated learning (Fed-ReMasker), enabling centers to impute features never observed locally by leveraging knowledge learned across collaborating centers. We evaluate Fed-ReMasker in a benchmark spanning synthetic datasets with linear and nonlinear relationships and real-world tabular datasets, including clinical data. The benchmark varies the number of centers, the missingness ratios, and client heterogeneity. Fed-ReMasker achieves the lowest imputation error in 93.2% of value-level and 96.7% of feature-level scenarios in the homogeneous benchmark. It also remains robust to client heterogeneity using simple federated averaging, outperforming all baselines in all 36 value-level scenarios and each baseline in at least 35 of 36 feature-level scenarios, and comes within 3.0% on average of a centralized model trained on the pooled data.

---


### 194. [Field-of-View Extension in Dental Cone-Beam CT via Implicit Neural Representations and Diffusion Model-Based Refinement](https://arxiv.org/abs/2609.28110)

**<font color=#1a73e8>作者：</font>** Susanne Schaub, Florentin Bieder, Matheus L. Oliveira 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dental cone-beam computed tomography (CBCT) systems often employ detector configurations that provide a truncated field of view (FOV) that only captures a small part of the patient's anatomy. In this work, we aim to reconstruct an extended FOV using projections of truncated FOV scans. To this end, we propose a three-stage framework that consists of (1) an implicit neural representation (INR) for estimating missing parts of the truncated projection data, (2) an iterative reconstruction for generating a secondary volumetric image with improved anatomical consistency and (3) a fast diffusion model for image enhancement. The proposed approach combines the strengths of continuous representations, physics-based reconstruction and generative refinement within a unified pipeline for truncated CBCT imaging. Experimental results demonstrate that the method effectively reduces truncation artifacts, improves the reconstruction of structures extending beyond the original FOV and produces images with enhanced quality. Our code is publicly available at this https URL.

---


### 195. [No Place to Hide: An Analysis on Protected Order Flow Sandwich Attacks](https://arxiv.org/abs/2609.28115)

**<font color=#1a73e8>作者：</font>** Lioba Heimbach, Ozan Solmaz, Burak Öz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Front-running has long plagued Ethereum's public mempool, earning it the nickname of a "dark forest", where predators lurk for profitable transactions. In response, Ethereum and other blockchain ecosystems increasingly rely on private RPCs and native protections to shield transactions from adversaries, which we refer to as protected order flow. Yet the effectiveness of these mechanisms in preventing front-running, and what trust assumptions they entail, remain poorly understood.
In this work, we conduct the first longitudinal, three-year measurement study of sandwich attacks against protected order flow across six blockchains: Ethereum, Solana, Tron, Base, Arbitrum, and Monad. We introduce detection heuristics that capture wide attacks, both within and across blocks, and filter on bot behavior to distinguish sandwiches from legitimate trading activity. We identify 28.0 million sandwich attacks on Solana, 38,567 on Tron, 30,607 on Ethereum, and 1,889 on Base against transactions intended to be protected from front-running. Reorged blocks expose a further 2,875 Ethereum victims. Unlike conventional public-mempool sandwiches, these attacks rarely occur tightly around their victims and, outside Solana, are carried out by a small number of entities.
Our analysis uncovers exposures at every layer: validator- and application-level exposure on Solana, order-flow auctions and reorged blocks on Ethereum, first-come-first-served ordering that fails to prevent latency-based front-running on Tron, and both an RPC bug that exposes pending transactions and predictable victim behavior on Base. These findings show that existing front-running protections can provide substantially weaker guarantees than users expect, highlighting the need for stronger end-to-end defenses against sandwich attacks.

---


### 196. [Probabilistic and Geometry Aware Neural Surrogate of Scrape Off Layer Plasma Simulations](https://arxiv.org/abs/2609.28116)

**<font color=#1a73e8>作者：</font>** Gabriele Gianuzzo, Stefan Dasbach, Fleur Hendriks 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast surrogates for tokamak boundary-plasma simulation are typically deterministic regressors mapping a global operating point to a flattened vector of cell values. Near the divertor detachment transition the steady state is not reliably single-valued. A point estimate must average over qualitatively different plasma states, and it arrives with no statement of confidence. Moreover, the flattened vector representation discards the geometric structure of the SOLPS-ITER mesh. This work addresses both problems. We unroll the curvilinear mesh into three fixed-size image tensors whose layout preserves cell adjacency and inverts exactly, letting a convolutional network act on the geometry without loss of information. A conditional flow matching model, well suited to highly sensitive systems, is then trained on this representation. The result is an efficient, scalable surrogate that captures multiple plausible outcomes even at sensitive operating points. Along a gas-puff scan, the predictive distribution splits into a hot and a cold mode across an early regime transition. A further check on synthetic data with an injected bifurcation of known size confirms the model recovers both branches rather than their average.

---


### 197. [A comparative assessment of global building and settlement datasets across geographic and settlement contexts](https://arxiv.org/abs/2609.28154)

**<font color=#1a73e8>作者：</font>** Rufai Omowunmi Balogun, Caroline Margaux Gevaert, Capucine Riom 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Global building and settlement datasets increasingly support population mapping, exposure assessment, urban monitoring, and other analyses of the built environment, yet comparative evidence remains fragmented across products, geographic regions, reference datasets, spatial scales, and evaluation methods. We benchmark seven global or near-global products, including Overture Maps, Global Building Atlas, 3D-GloBFP, Google Open Buildings 2.5D Temporal (OBT), Microsoft TEMPO, GHSL, and WSF Tracker, against harmonized reference footprints across 135 study areas. The evaluation combines complementary measures of detection, geometric agreement, and aggregate quantity accuracy, together with stratified analyses of settlement characteristics and diagnostic experiments on error size and temporal alignment. Overture achieved the highest median city-level vector F1 (0.786). Raster rankings were resolution-dependent: OBT achieved the highest median F1 at 10m (0.642), whereas WSF Tracker led at 100m (0.862). However, WSF Tracker substantially overestimated built-up area, emphasizing that when using raster products, it is important for the user to understand whether the raster identifies only buildings or includes additional impervious surfaces. Raster accuracy increased consistently with building density (Spearman \r{ho} = 0.58-0.75), while small candidate buildings were disproportionately associated with false positives in the vector products. Temporally aligning WSF Tracker with reference imagery increased mean F1 by 0.060 (median +0.037), indicating that the reported accuracies are conservative in rapidly growing areas. The study establishes a reproducible benchmark for comparing heterogeneous global urban and settlement layer datasets across geographic and settlement contexts.

---


### 198. [Depth-Guided Contrastive Learning for 2D Representations with 3D Spatial Awareness](https://arxiv.org/abs/2609.28159)

**<font color=#1a73e8>作者：</font>** Liang Zeng, Maarten Vergauwen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard contrastive learning frameworks are mainly designed from a semantic perspective, yet learning 2D visual representations that preserve 3D spatial structure is also important for scene understanding. In this work, we propose Depth-Guided Contrastive Learning (DGCL), a simple auxiliary objective that injects 3D spatial awareness into 2D contrastive representation learning. Our key idea is to use depth to convert local 3D proximity into contrastive similarity: pixels that are closer in 3D space are encouraged to have more similar representations than pixels that are farther apart. Instead of relying on absolute depth values, DGCL formulates supervision through relative 3D distance comparisons among randomly sampled pixels, making the objective invariant to depth scale, efficient to compute, and easy to integrate into existing contrastive frameworks. Experiments across different datasets and models show that DGCL consistently improves 2D representation learning and benefits semantic downstream tasks by stronger spatial and geometric understanding. The code is available on this https URL.

---


### 199. [Confidence Falls Short: Asymmetric Certainty Gains from Optimization Hinder Multimodal Classification](https://arxiv.org/abs/2609.28165)

**<font color=#1a73e8>作者：</font>** Longfei Huang, Xiangyu Wu, Yang Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal learning (MML) falls into the optimization dilemma due to the modality imbalance phenomenon, leading to suboptimal overall performance in practice. While many attempts primarily focus on balancing the optimization dynamics across modalities to address this issue, we identify a subtle yet critical flaw: optimization yields asymmetric gains in predictive certainty, with the strong modality more confident than the weak one, driving imbalanced modality contributions. In this paper, our analysis reveals that this flaw stems from unimodal characteristics rather than multimodal learning, and this confidence discrepancy can be corrected by positive cross-modal intervention. Based on this insight, we propose multimodal Max Confidence Regularization (MaxCR) to dynamically intervene in modality semantic confidence. Specifically, the semantic confidence of each modality is tracked using a nonlinear sparsity measure. We then design max suppression and max excitation based on this measure to regularize strong and weak modalities, respectively. They penalize and encourage the top-1 confidence, thereby constraining multimodal prediction. To this end, strong and weak modalities are expected to make calibrated confidence, thereby improving the overall performance. Empirical experiments on widely used datasets reveal the superiority of our method through comparison with various state-of-the-art (SOTA) multimodal learning baselines.

---


### 200. [Safety-Aware Zero Trust Enforcement for IoT and Cyber-Physical Systems](https://arxiv.org/abs/2609.28170)

**<font color=#1a73e8>作者：</font>** Alessandro Lotto, Alessandro Brighente, Mauro Conti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zero Trust (ZT) replaces the implicit trust of perimeter-based security with explicit, continuous, context-aware authorization. This shift is particularly relevant to IoT and cyber-physical systems, whose heterogeneous, long-lived, and remotely connected components make persistent trust untenable. Yet their physical coupling complicates ZT adoption: restricting a suspicious component can reduce cyber exposure while removing telemetry or control capabilities required for operation. Existing work mainly models physical harm caused by attacks, with less attention to consequences introduced by enforcement itself.
We introduce Safety-Aware Zero Trust (SA-ZT), which treats restriction-induced physical consequences as policy inputs. We map the NIST ZT tenets to nine IoT/CPS convergence strains, distinguish IoT-amplified challenges from those specific to cyber-physical coupling, and derive corresponding operational requirements. SA-ZT extends the NIST ZT Architecture with a Safety Engine and a Telemetry Broker. The Safety Engine selects among admissible responses by jointly considering residual cyber risk and restriction-induced consequences, while the Telemetry Broker mediates raw telemetry visibility and estimator influence. With command-side enforcement, these entities separate raw visibility, automated influence, and state-changing authority, preserving observations for monitoring while constraining their influence on automated control. An IEEE 30-bus case study under false-data-injection attack illustrates how SA-ZT makes cyber containment, telemetry visibility and influence, physical consequences, and authorization timing explicit, providing an implementable and inspectable representation of cyber-physical enforcement trade-offs.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-240](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
