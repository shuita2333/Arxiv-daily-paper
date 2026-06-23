# 📦 其他研究 | 2026年06月23日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

---

### 51. [When Web Agents Finish but Still Fail: Reproducible Triggers and Trace Diagnostics for Parallel Web Exploration](https://arxiv.org/abs/2606.20724)

**<font color=#1a73e8>作者：</font>** Aagam Sogani, Botao Rui, Swetha Vaidyanathan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon web agents often fail in ways hidden by final-answer evaluation: they may visit useful pages, produce a well-formed answer, and terminate confidently while still missing fields, over-including unsupported items, or relying on stale evidence. We study these failures with Parallel WebBench, a parallel web-exploration benchmark containing 1,679 verified records: 350 manually curated parallel tasks and 1,329 reconstructed records with verified URL-based trajectories. We train WebExplorer-style agents with GRPO under human-only, balanced human-synthetic, and synthetic-heavy data mixtures. At 16k context and 16 interaction rounds, the best GRPO model improves completion over WebExplorer-8B from 50.7% to 96.0% and GPT-4.1-mini-judged element-wise F1 from 0.2489 to 0.4529, but binary accuracy remains far below completion. Trace-level analysis identifies three persistent failure modes: context-bound search loops, premature termination on partial answers, and synthesis collapse after relevant evidence has already been retrieved. These results show that synthetic-data GRPO reduces abstention and improves partial correctness, but leaves a completion-correctness gap that requires evidence-grounded coverage and synthesis diagnostics.

---


### 52. [D2HDMap: Non-visible Driveline Map Prior for Online Vectorized HD Map Prediction](https://arxiv.org/abs/2606.20725)

**<font color=#1a73e8>作者：</font>** Seojun Shon, Chikao Tsuchiya, Dhaval Bhanderi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate, up-to-date representations of road structures are critical for the safe operation of autonomous vehicles. Existing systems rely either on costly, maintenance-heavy high-definition (HD) maps which compromise safety when outdated, or purely sensor-based online mapping which struggles with long-range reliability and occlusion. Systems incorporating map prior information into online mapping seek to overcome drawbacks of both approaches by combining them in some way. We propose 'Driveline To HD Map' (D2HDMap), an online mapping system that injects a lightweight, non-visible driveline prior to guide the estimation of visible road structures such as lane dividers, road boundaries and crosswalks. This prior incurs less effort to create and update compared to full HD map priors used in other approaches. We also show that training with such a prior can improve generalization at inference time when no prior is available. Ablation studies conducted on the nuScenes and Argoverse 2 dataset demonstrate that models trained using a driveline prior largely retain performance even when priors are not available. On a geographically disjoint split, D2HDMap achieves 44.8 mAP, surpassing recent state-of-the-art. Additionally, noise-aware training substantially increases robustness to realistic localization error.

---


### 53. [How Well Can Your Video Model Remember? Measuring Memory-Budget Trade-offs in Long Video Understanding](https://arxiv.org/abs/2606.20726)

**<font color=#1a73e8>作者：</font>** Yixian Tian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a compact empirical model that quantifies how answer accuracy degrades as a function of frame budget B and temporal distance D in long video understanding -- analyzing performance when recalling content from D seconds in the past using a fraction B of total frames. Long-form models operate under strict budgets, yet no prior framework predicts how accuracy degrades as B shrinks and events recede. We fit a weighted least-squares model on ~155,000 binary predictions across ten models and three sampling strategies, deriving a law where logit-accuracy scales linearly in log-budget with a distance-dependent exponent that decays log-linearly with distance. This budget exponent \alpha(D) captures the marginal value of extra frames at distance D. The law achieves cell-level weighted R^2 = 0.05-0.75 across models. Notably, budget effectiveness at D = 1000 s differs by \approx 7.4\times between the best streaming and base models. STREAMINGVLM achieves \alpha(1000) = 1.26 (95% CI: [1.06, 1.58]), meaning a tenfold budget increase substantially improves long-distance accuracy, while the best Qwen3-VL base model reaches only \alpha(1000) = 0.17 (CI: [0.04, 0.34]). In accuracy space, a 10\times budget increase at D = 1000 s yields +29 percentage points for STREAMINGVLM versus +4 pp for the base model. Sampling strategies show model-dependent trade-offs: random sampling yields higher base sensitivity but steeper distance decay. We demonstrate how \alpha(D) enables principled budget allocation, including a model-ranking reversal at long distance, and propose it as a diagnostic metric for streaming video models.

---


### 54. [VTOS: Learning to Orchestrate Vision Tools by Co-Searching Solutions and Observers](https://arxiv.org/abs/2606.20728)

**<font color=#1a73e8>作者：</font>** Jinchao Ge, Lingqiao Liu, Shuwen Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation tools such as open-vocabulary detectors, segmentation models, and post-processing operators are powerful building blocks for computer vision, but their effectiveness depends heavily on how they are orchestrated: which tools are used, in what order, with what parameters, and under what visual conditions. Existing visual-programming agents typically generate a fixed solution pipeline, making them brittle under dense objects, occlusion, small targets, and domain shift. We introduce VTOS (Vision Tools Orchestration Search), a framework for adaptive visual tool orchestration through joint solution--observer search. VTOS co-searches executable solution programs that compose vision tools such as Grounding DINO, SAM, NMS, and slice-and-detect, together with observer programs that diagnose candidate solutions, identify failure modes, and generate actionable feedback. These observations are accumulated in a shared VisionThoughts knowledge base to guide subsequent search. We evaluate VTOS through two case studies: dense object counting on LVIS-Count and zero-shot plant-disease segmentation on PlantSeg-OOD, which stress different orchestration challenges including threshold calibration, NMS, slicing, mask refinement, and domain generalization. Across both tasks, VTOS outperforms static tool pipelines and agentic visual-programming baselines, showing that co-searching solutions and observers is an effective strategy for adapting vision tools to challenging computer vision tasks.

---


### 55. [XmoPipe: A Pipeline for Large-Scale In-the-Wild Human Motion Dataset Construction](https://arxiv.org/abs/2606.20731)

**<font color=#1a73e8>作者：</font>** Nathan Salazar, Emmanuel Dellandréa, Mathieu Lefort 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale human motion datasets are essential for training robust motion models for analysis, synthesis, and understanding. While marker-based motion capture provides precise data, it is costly and limited in scale and diversity. Recent advances in monocular motion capture and video-language understanding open the way to extract plausible motion from unconstrained online videos. We present a scalable pipeline for constructing in-the-wild human motion datasets. From a few keywords, the system retrieves videos, extracts 3D body and facial motion, and generates high-level textual descriptions. The pipeline is flexible, enabling targeted collection of various motions, multi-person interactions, or expressive behaviors. We demonstrate its quality by training motion reconstruction and motion generation models, showing performance comparable to models trained on traditional motion capture datasets and strong cross-dataset generalization.

---


### 56. [Robust Zero-Shot Generalization for Open-Vocabulary Action Recognition via Task Arithmetic](https://arxiv.org/abs/2606.20734)

**<font color=#1a73e8>作者：</font>** Francesca Morandi, Omayma Moussadek, Federico Venturini 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open Vocabulary Action Recognition (OVAR) enables the recognition of novel actions by leveraging vision-language representations, overcoming the limitations of traditional closed-set approaches. However, achieving robust performance in real-world scenarios typically requires domain-specific fine-tuning, which is often costly and raises privacy and regulatory concerns. In this work, we propose an alternative paradigm that bypasses target-domain training and recombines knowledge from existing datasets and models. Leveraging model merging and task arithmetic, we extract and combine task vectors from models fine-tuned on diverse public OVAR datasets. We show that, in out-of-distribution settings, the resulting merged model achieves superior zero-shot generalization to the pre-trained base model. Code is available at this https URL

---


### 57. [REKEY: Metadata-Grounded Visual-Key Regeneration for Contamination-Resilient VQA Evaluation](https://arxiv.org/abs/2606.20736)

**<font color=#1a73e8>作者：</font>** Tengjie Lin, Yutao Sun, Jingwei Ni 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Static visual question answering (VQA) benchmarks age quickly: Once the items leak into training corpora, scores can reflect memorization rather than genuine visual ability, thus obscuring real progress. Rebuilding high-quality benchmarks such as V*Bench requires substantial human annotation, yet each static release can quickly become another leaked artifact. We propose ReKey, a live benchmark protocol that randomly regenerates the answer-bearing local detail, or visual key, in real images at evaluation time. Using human-validated edit slots, ReKey samples fresh instances with new answers, construction-grounded labels, and controlled visual-search difficulty. On V*Bench, the ReKey regenerated benchmark reveals a sharp score jump across eight frontier vision-language models (VLMs): The original items score 9.5--18.8 percentage points higher than the regenerated variants. By making the visual key renewable, ReKey keeps evaluation fresh as models and training data evolve.

---


### 58. [Repeated Shared Access Enables Grokking, but Edit Propagation Depends on a Fine-Grained Addressable Memory](https://arxiv.org/abs/2606.20737)

**<font color=#1a73e8>作者：</font>** Yanan Niu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study factual edit propagation in a controlled synthetic knowledge-graph QA setting, comparing four architectures that cross loop recurrence with shared memory access: dense (Dense), looped (Loop), dense with shared memory (Dense+Mem), and looped with shared memory (LMC). Dense fits in-distribution 2-hop compositions but fails OOD; both looped recomputation and memory rereading cross this OOD grokking barrier, indicating that repeated shared access -- not a specific architecture -- is the common ingredient for learning. Editing, however, separates the substrates along a different axis. On a shared pre-edit-correct ID set, a single-row factual edit propagates strongly in the two memory-bearing cells (LMC 0.78-0.92, Dense+Mem 0.71-0.96) and only weakly in the others (Loop 0.04-0.30, Dense 0.00-0.03); the separation is statistically clean (Mann-Whitney p=0.008 between memory and non-memory cells, p=0.55 between the two memory cells, though n=5 vs n=5 is underpowered to rule out a moderate gap). In LMC, atomic facts localize to dominant memory sites that composition rereads, and a one-row value edit on LMC's own pre-edit-correct probes achieves 100% direct success with mean 0.989 intended propagation while moving unrelated facts ~0.1% of the time (matched specificity across substrates pending). A coarse hold-answer-subspace (HOLDANS) interchange diagnostic is consistent with this ordering, suggesting that what separates the substrates is when an edited fact is injected and how much computation remains afterwards to reuse it. These results dissociate learning competence from editing affordance: repeated shared access suffices to grok, but edit propagation depends on whether the substrate exposes a fine-grained addressable memory the forward computation can write to and later reread -- an affordance that loop recurrence provides only partially.

---


### 59. [VeriBound: PAC-Bayesian Generalization Bounds for Process Reward Models Trained with Formal Verification Tools](https://arxiv.org/abs/2606.20740)

**<font color=#1a73e8>作者：</font>** Amirul Rahman, Mohammed Sabih Alsharari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Process Reward Models (PRMs) provide step-level verification for Large Language Model (LLM) reasoning, yet their training data acquisition remains a bottleneck: human annotation is costly and Monte Carlo roll-out estimates are noisy. A recent approach, FOVER, trains PRMs on step-level error labels automatically annotated by formal verification tools such as Z3 and Isabelle, and empirically observes cross-task generalization from symbolic tasks to diverse reasoning benchmarks. However, this generalization phenomenon lacks any theoretical explanation, and no formal bounds exist on the generalization error, sample complexity, convergence rate, or downstream Best-of-K performance of such PRMs. We propose VeriBound, a theoretical framework that provides PAC-Bayesian generalization bounds for PRMs trained with formal verification tools. We establish four main results: (i) a PAC-Bayesian generalization bound that relates the empirical verification error on formal-verification-annotated training data to the expected error on unseen reasoning tasks, with the bound depending on the formal verification accuracy and the divergence between training and test task distributions; (ii) a sample complexity result showing that $O(d \log(d/\delta) / \epsilon^2)$ formal-verification-annotated examples suffice to achieve generalization error $\epsilon$ with probability $1-\delta$, where $d$ is the complexity of the PRM hypothesis class; (iii) a convergence analysis proving that PRM training with formal verification labels converges at a linear rate under $L$-smoothness and bounded variance conditions; and (iv) an error propagation bound that relates step-level verification error to Best-of-K performance degradation.

---


### 60. [Massive Activations Are Architecturally Robust: A Controlled Scratch/Commitment Residual Stream Test](https://arxiv.org/abs/2606.20743)

**<font color=#1a73e8>作者：</font>** Maruthi Vemula  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trained transformers reliably develop massive activations, a small number of hidden dimensions whose magnitude is far above the median and which concentrate on the sequence-start token. Whether these outliers are a removable artifact of the residual stream's overloaded read and write role, or instead a functional necessity, is actively debated. We test the artifact hypothesis directly, with an architectural intervention. Our architecture, Ledger Residuals, splits the residual stream into a mutable scratch stream (Deliberation) that intermediate computation may freely overwrite and a protected, decode-only accumulator (Commitment) that holds the representation the model reads out. If massive activations exist only because one stream is forced to be both scratchpad and answer, then a dedicated answer channel should remove the need for them. We find that it does not. In matched-loss language models at the 160M and 290M scales, the model rebuilds the canonical fixed-dimension, start-token outlier inside the protected channel. The rebuilt feature is smaller in magnitude than in a standard transformer but more sharply concentrated on the start token, and a stronger sparsity penalty makes it more persistent and more concentrated still, rather than removing it. Massive activations therefore look architecturally robust: they re-emerge in whichever representation the model decodes from, which is what we would expect if they are functional rather than incidental. We release our architecture and measurement code.

---


### 61. [Amplify, Don't Create: Temporal Accumulation for Slow-Burn Prompt Injection](https://arxiv.org/abs/2606.20746)

**<font color=#1a73e8>作者：</font>** J Alex Corll  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most prompt-injection detectors score a single event or message. Control-plane attacks against tool-using agents can instead distribute weak directives across a trajectory while keeping each event below threshold. We test whether a proxy-side temporal accumulator recovers this slow-burn signal by reducing frozen per-event scores to peak and CUSUM persistence statistics. To avoid circularity, grafts are generated against a held-out autoregressive cloaking target and then re-scored under a detector of record: a frozen char-ngram SVM plus an embedding-contrastive head. Only floor-met grafts bound to executed action edges and still sub-threshold under the detector of record enter the slow-burn endpoint. This is a boundary result, not a deployable detector. On concentrated attacks, trajectory-level accumulation beats the per-event foil under a clustered bootstrap (gap +0.092, 95% CI [+0.025, +0.155]), while persistence and peak are statistically tied. On git repo-exfil, density-four floor-met sub-threshold grafts add persistence mass that matched benign shams do not (persistence-delta AUC 0.708 over four attack survivors and six benign shams), while the matched peak-delta control does not separate attack from sham (AUC 0.417), localizing the effect to accumulated persistence rather than a single hot graft. The effect fails on broader clean-path actions (persistence-delta AUC 0.167), where the detector assigns attack and benign actions indistinguishable per-event scores, leaving no margin for CUSUM to bank. Independent powering is blocked by only three to four independent tasks. Temporal accumulation is therefore a narrow-band margin amplifier: it can bank elevated sub-threshold signal but cannot create margin where the per-event detector has none. As byproducts, we contribute a pseudo-replication warning and an independence-audit standard for agent-benchmark evaluation.

---


### 62. [CIExplainer++: Generating Causal and Interpretable Explanations for Graph Neural Networks](https://arxiv.org/abs/2606.20747)

**<font color=#1a73e8>作者：</font>** Francisco Caldas, Sahil Satish Kumar, Ruben Belo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainable Artificial Intelligence aims to make black-box models more trustworthy by presenting, in a human-understandable manner, the elements that lead to the model's output. This involves both (i) identifying components and connections with genuine causal influence on outputs and (ii) translating such structures into an interpretable representation. For the former, we introduce CIExplainer, a novel perturbation-based method grounded in causal inference for explaining Graph Neural Networks (GNNs). CIExplainer identifies the subgraph with the highest causal effects on GNN predictions using the Potential Outcome Framework. We evaluate and compare CIExplainer on various GNN architectures (GCN, GraphSAGE, GAT, GIN) and datasets.
To bridge subgraph explanations with human interpretability, we further propose G2TeXplainer, a method that transforms causal subgraphs into natural language explanations that capture both feature-level and relational information.

---


### 63. [From Sentiment to Actionable Insights: A Data-Driven Public Sentiment Analysis of Advanced Air Mobility](https://arxiv.org/abs/2606.20751)

**<font color=#1a73e8>作者：</font>** Esrat Farhana Dulia, Amina Dhaher, Raiful Hasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Advanced Air Mobility (AAM) is an emerging low-altitude air transportation system whose successful deployment depends not only on technological advancement but also on public acceptance. This acceptance will drive government support, regulations, noise standards, and willingness to fly, and in turn the overall commercial viability of AAM. Understanding public sentiment toward AAM is therefore essential for identifying its societal barriers and informing its adoption strategies. This study analyzes 306,009 human-generated texts collected from Reddit and Quora to examine public discourse on AAM using AI-based models. Because multiple sentiment analysis models exist, identifying the most accurate model is critical for reliable AAM sentiment prediction and trustworthy public opinion analysis. Accordingly, seven models spanning lexicon-based, machine learning, deep learning, and transformer-based approaches are evaluated for AAM-specific sentiment classification. ModernBERT achieves the best classification performance and is used to label the full dataset. Using the resulting sentiment labels, Latent Dirichlet Allocation (LDA) is applied within each sentiment class to uncover latent topics in public opinion. The analysis identifies 20 distinct topics and traces their temporal evolution from 2008 to 2025. A cross-sentiment topic analysis further reveals six major clusters of public concern: workforce and skill development (25.29% of the dataset), regulation and compliance (24.64%), technical performance of drones (20.99%), military, geopolitics, and defense (14.58%), safety and operational risks (8.51%), and noise and disturbance (5.98%). Based on these findings, this study provides actionable strategies to address these concerns, thereby, improving public acceptance and support AAM deployment.

---


### 64. [Privacy-Preserving Compliance on Public Ledgers via Selective Disclosure Authorization Schemes](https://arxiv.org/abs/2606.20760)

**<font color=#1a73e8>作者：</font>** Supriya Khadka, Sanchari Das  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public distributed ledgers enforce integrity through radical transparency, creating tension with data minimization principles required for regulatory compliance. While Zero-Knowledge Proofs (ZKPs) offer a theoretical privacy solution, existing constructions often overlook adversarial constraints in smart contract environments. Specifically, the asynchronous decoupling of off-chain proof generation from on-chain submission introduces front-running and proof-reuse risks in public mempools. In this work, we formalize Selective Disclosure Authorization Schemes (SDAS), a cryptographic primitive for granular and revocable compliance checks on public ledgers without revealing the underlying witness. We define a security model for SDAS, introducing Ledger-Bound Attribute Unlinkability and Context-Aware Sender Binding to capture how valid proofs remain bound to their intended authorization context. To validate sender binding, we present ZK-Compliance, an Ethereum-based instantiation that operationalizes a user-controlled "Grant, Verify, Revoke" lifecycle. We implement the sender-binding component using a 14-constraint Circom circuit that anchors the zero-knowledge proof to the executing on-chain sender address. Our Sepolia evaluation confirms practical viability: browser-based proof generation executes in under 200 ms, and on-chain verification costs 240,512 gas, neutralizing proof reuse by different callers while preserving strict attribute privacy.

---


### 65. [UniSLAD: A Unified Framework for Structural and Logical Industrial Visual Anomaly Detection](https://arxiv.org/abs/2606.20768)

**<font color=#1a73e8>作者：</font>** Changyi Li, Chao Yang, Yu Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual anomaly detection is a fundamental task in industrial automation. While existing approaches have achieved notable progress in identifying structural defects, the detection of logical anomalies remains relatively underexplored. In practice, structural and logical anomalies frequently co-occur in industrial workflows. Therefore, a solution capable of detecting both structural and logical anomalies is crucial for advancing comprehensive anomaly detection research. To address this limitation, we propose a unified framework, termed UniSLAD, which jointly addresses logical and structural anomalies without additional training, enabling a practical solution for dynamic industrial environments. First, we introduce a dual-feature extractor that synergistically integrates a Convolutional Neural Network (CNN) backbone for local texture perception with a Transformer backbone for global contextual reasoning, yielding richer and more comprehensive representations. Building on this foundation, we design dual-granularity feature representation modules. At the patch level, memory banks enhanced by the Mahalanobis Transform (MT) preserve representative features and support more discriminative anomaly scoring. At the image level, distribution maps are aggregated using Lower-Upper Mean (LUM) and Power Mean Pooling (PMP), yielding a more robust global representation than conventional average pooling. Extensive experiments on the two industrial benchmarks demonstrate that UniSLAD achieves competitive performance in comprehensive anomaly detection, achieving 99.4% and 93.1%, respectively. Furthermore, ablation studies verify the individual contributions and effectiveness of each proposed component.

---


### 66. [Beyond 'One Language, One Script': Quantifying Orthographic Bias in Multilingual VLMs with PuMVR](https://arxiv.org/abs/2606.20770)

**<font color=#1a73e8>作者：</font>** Prabhjot Singh, Bhushan Pawar, Madhu Reddiboina  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current Vision-Language Models (VLMs) are celebrated for their multilingual capabilities, yet they operate under a flawed assumption: that one language corresponds to a single writing system. This overlooks billions of users of multi-script languages like Punjabi, Serbian, Hindi-Urdu, Kurdish, among many others, for whom a model's capability may be fractured by orthographic bias. We introduce PuMVR (Punjabi Multimodal Visual Reasoning), the first benchmark designed to quantify script-dependent bias through 375 culturally grounded image-reasoning tasks across Punjabi's three active scripts (Gurmukhi, Shahmukhi, Roman). Evaluating 10 state-of-the-art VLMs, we expose a substantial Script Gap: models frequently solve visual puzzles in one script while failing identical tasks in another, with accuracy deltas reaching 16% and Script Consistency Rates (SCR) as low as 24.8%. Crucially, visual input boosts absolute performance but does not close this gap, the relative bias persists. Our analysis suggests reasoning patterns show limited cross-script transferability, and Chain-of-Thought pathways diverge based on script alone. We propose SCR as a core metric for script-agnostic evaluation, challenging current multilingual assessment paradigms and providing a framework for equitable AI.

---


### 67. [ELADO: Elliptic PDE Assessment Datasets for Operator Learning](https://arxiv.org/abs/2606.20771)

**<font color=#1a73e8>作者：</font>** Frank Ehebrecht, Toni Scharle, Martin Atzmueller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce ELADO (Elliptic PDE Assessment Datasets for Operator Learning), a systematic benchmark suite constructed to show and quantify failure modes of neural operator architectures when learning solution operators of elliptic PDEs. While the benchmarks of existing datasets focus on average case performance, the ELADO datasets are constructed to highlight challenges that arise naturally in elliptic PDE problems. In particular, we construct several datasets built around Poisson's equation and the Helmholtz equation, each with non-constant coefficients. We define a controllable data-generating process to create datasets, that are designed to isolate a distinct source of difficulty. Specifically, these are (1) heavy-tailed solution distributions arising from light-tailed coefficient field distributions, (2) spectral distribution shift of the input data, (3) heavy-tailed distributions in the frequency domain of solutions, arising from light-tailed coefficient field distributions, (4) input sensitivity of learned operators, quantified by an empirical local Lipschitz analysis, and (5) the effect of input signal complexity on prediction accuracy under controlled amplitude normalization. We evaluate several neural operator architectures across all datasets and show that heavy-tailed targets, spectral shift, and input sensitivity each cause substantial degradation of the prediction accuracy that standard datasets and metrics (e.g., the mean relative $L^2$ error) may obscure.

---


### 68. [TriMotion: Modality-Agnostic Camera Control for Video Generation](https://arxiv.org/abs/2606.20774)

**<font color=#1a73e8>作者：</font>** Seunghyun Shin, Jifei Song, Wooseok Jeon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera motion control is essential for directing viewpoint changes in generative systems. However, existing methods typically condition the generation process on a single specific modality, such as explicit pose trajectories or reference videos, limiting their ability to support heterogeneous user inputs. To address this limitation, we present TriMotion, a modality-agnostic framework for camera-controlled video generation that maps video, pose, and text inputs, describing the same camera trajectory into a shared motion embedding space. Learning such a space requires synchronized supervision across modalities. Therefore, we build the Motion Triplet Dataset by extending a Multi-Cam Video Dataset with geometry-grounded motion descriptions derived from camera extrinsics. We further introduce a latent motion consistency objective that leverages the motion embedding space to encourage the generated video to follow the target camera trajectory directly in latent space, avoiding the cost of pixel-space decoding. Extensive experiments show that TriMotion generates high-quality videos that accurately follow the target camera trajectories across all three modalities. Beyond standard generation, the shared motion embedding space also enables flexible applications such as sequential motion composition and cross-modal motion interpolation.

---


### 69. [Memory-Centric Computing: Security Benefits and Challenges of Processing-in-DRAM](https://arxiv.org/abs/2606.20786)

**<font color=#1a73e8>作者：</font>** Ismail Emir Yuksel, F. Nisa Bostanci, Ataberk Olgun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Today's computing systems are processor-centric: they require frequent data movement between processing elements (e.g., CPU) and main memory (DRAM), leading to significant inefficiencies in performance and energy consumption. Memory-centric computing instead moves computation to the data, enabling computation capability in and near all places where data is generated and stored, and greatly reducing the performance and energy overheads of data access and data movement. This shift from a processor-centric to a memory-centric paradigm has important and underexplored consequences for system security. Turning memory from a dumb, inactive store into an active computing substrate introduces benefits as well as challenges for system security: it can provide new in-memory security primitives and also reduce data exposure, but it can also expose new attack surfaces. This work discusses the security benefits and challenges of memory-centric computing, specifically Processing-in-DRAM (PiD), a paradigm where the operational characteristics of a DRAM chip are exploited and enhanced to perform computation on data stored in DRAM. Specifically, we describe 1) new state-of-the-art DRAM-based true random number generators that provide up to 16.05 Gb/s throughput and physical unclonable functions with 5.75% lower evaluation latency than the prior state-of-the-art, both on real DRAM chips and 2) two key security challenges of PiD: amplified DRAM read disturbance (e.g., 158x reduction in the minimum number of DRAM accesses required to induce the first bitflip) and high throughput memory timing channels (e.g., a communication throughput of 14.8Mb/s). We believe it is time to design, use, and program DRAM, and in general memory, not as an inactive storage substrate, but as a combined computation, storage, and security substrate, where computational capability, storage density, and security are all key goals.

---


### 70. [GroundShot: Visually Consistent Multi-Shot Long Video Generation via Entity-Grounded Shot Scheduling](https://arxiv.org/abs/2606.20799)

**<font color=#1a73e8>作者：</font>** Yixuan Lai, Tianjia Shao, Kun Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating visually consistent multi-shot videos remains an open challenge. As videos span more shots, inconsistencies can accumulate across shots, causing entities that reappear across shots -- characters, objects, and locations -- to drift away from how they first appear. We observe that viewers judge consistency by comparing each later appearance of an entity with its first clear appearance; the visual quality of this initial appearance sets the consistency ceiling for all that follows. Motivated by this, we present \textbf{GroundShot}, a training-free, model-agnostic agentic framework for entity-grounded multi-shot generation. GroundShot builds an entity-level visual memory online from accepted generated shots: it schedules shots' generation order by their expected usefulness as entity references, grounds entities from generated videos, verifies their reliability before adding them to memory, and retrieves suitable entity references from memory before each shot is generated. To evaluate this entity-centered view of consistency, we further introduce \textbf{GroundBench}, a diagnostic benchmark that measures consistency at the entity level while isolating controlled challenge dimensions. Experiments show that GroundShot improves multi-shot consistency over existing methods while requiring no additional training or model modification.

---


### 71. [NeoLoc-68: End-to-end 68-point neonatal facial landmark localisation in neonatal clinical environments](https://arxiv.org/abs/2606.20823)

**<font color=#1a73e8>作者：</font>** Abdullah Bin-Obaid, Maria M. Cobo, Rebeccah Slater 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial landmark localisation is a prerequisite for developing automated, non-contact neonatal pain assessment methods. Clinicians use pain scales to judge the severity of pain, many of which rely on facial expression. However, facial landmark detectors trained on adult faces perform poorly in neonatal clinical environments due to frequent occlusions caused by medical equipment, varied head poses, and challenging imaging conditions, including motion blur triggered by sudden pain-related movements. We propose an end-to-end facial landmark detector capable of predicting 68 landmarks on neonatal faces in clinical environments. We combined 37,459 single-face images from 11 public datasets, standardised to 68-point markup, with 1,123 manually annotated frames from a neonatal research dataset (totalling over 76,000 landmarks). A YOLO-based keypoint model was adapted to regress the facial landmarks, initialised with weights from a pretrained neonatal face detector. On public datasets, our proposed model achieved state-of-the-art performance: Normalised Mean Error (NME) = 5.37, Failure Rate (FR) = 12.5%, Area Under the Cumulative Error Curve (AUC) at AUC0.08 = 38.00% and AUC0.1 = 48.70%. On the clinical neonatal test set, before fine-tuning, the model achieved the lowest Detection Failure Rate (DFR) = 5.3% among all baselines and showed strong generalisation. After fine-tuning, performance improved further to NME = 6.36, FR = 22.30%, DFR = 1.77%, AUC0.08 = 29.24% and AUC0.1 = 40.25%. To the best of our knowledge, this represents the first end-to-end 68-point neonatal facial landmark detection model. With further dataset expansion and refinement, it could support downstream tasks in neonatal health monitoring and pain-related facial analysis.

---


### 72. [PromptMark: A Prompt-Guided Iterative-Feedback Framework for Source Code Watermarking](https://arxiv.org/abs/2606.20835)

**<font color=#1a73e8>作者：</font>** Istiaq Ahmed Fahad, Mridha Md. Nafis Fuad, Kazi Sakib  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking has become a crucial technique for ensuring provenance and accountability in AI-generated source code. As large language models (LLMs) are increasingly integrated into development workflows, reliable attribution remains challenging. In practice, most developers rely on commercial LLM APIs operating under black-box constraints, making existing approaches that require access to the decoding process less feasible for real-world integration. To address this limitation, we propose PromptMark, a black-box, prompt-guided watermarking framework that embeds invisible yet statistically detectable signals into generated code via structured input instructions. The method steers models toward subtle identifier and comment naming patterns while preserving the functional correctness and structural integrity of the generated code. Detection is performed using statistical tests designed to remain reliable across varying code lengths and model outputs. The embedding is further refined through an iterative feedback loop, where prompts are updated based on watermark detection scores. Experiments on the MBPP and HumanEval benchmarks show that PromptMark consistently achieves strong watermark detectability while maintaining high code correctness, outperforming baseline approaches.

---


### 73. [Study on Quantitative Dynamic Epistemic Logic for Belief Revision](https://arxiv.org/abs/2606.20837)

**<font color=#1a73e8>作者：</font>** Felipe Nunes de Souza Camargo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Belief revision is a process in which an agent begins to believe in something she previously did not. I begin the paper by presenting, based on (Gärdenfors, 1998; Hansson, 1999), postulates for belief revision that constitute the basis of the AGM theory. I will then briefly show the semantics of a modal logic introduced in (van Ditmarsch, 2005), which I call `$P$'. This logic formalizes static epistemic states and has greater expressive power than AGM in doing so because it captures the quantitative notion of "degrees of conviction". The third step is to introduce revision operators on $P$ and, mostly following (van Ditmarsch, 2005), obtain the Dynamic Epistemic Logic (DEL) I call `$P*$'. It models processes of belief revision in several ways. Original results are presented in the following two sections. The first one of these sections revolves around a formalization of AGM postulates within $P*$ by proving some theorems related to the satisfaction of those postulates by revisions defined in $P*$. The last section features an analysis of $P*$'s revisions that go beyond the mere satisfaction of postulates. I compare their formal behavior with respect to some philosophical criteria. At last, I conclude that the functions presented in (van Ditmarsch, 2005) are not good formalizations of the philosophical intuition behind AGM. Instead, it is captured by the function $*^0$ originally defined in this paper (but highly inspired by (van Benthem, 2007)). An implementation of this function is also provided.

---


### 74. [Process-Reward Tactic Evolution for Long-Horizon Bioinformatics Workflows](https://arxiv.org/abs/2606.20839)

**<font color=#1a73e8>作者：</font>** Lingzhi Yang, Yubo Fan, Song Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents can write code and call tools, but reliable bioinformatics work requires long-horizon interaction with workflow software, typed data objects, provenance, and biological checks. We study this setting through Galaxy workflow execution. The agent must explore task data, construct or adapt an executable workflow DAG, bind inputs and dataset collections, monitor execution, debug failures, and validate biological outputs. We propose Process-Reward Tactic Evolution, a Galaxy-based training framework that turns verified workflow rollouts into reusable \tactics. During training, agents practice on curriculum-organized Galaxy tasks in Agent Gym; process verifiers score workflow construction, software interaction, execution, and biological correctness; successful and failed traces are distilled into a tactic library. At inference, the trained executor, Process-Reward Tactic Evolution, uses this library to execute held-out peer reviewed Galaxy workflow converted BioWorkflow Bench and BioAgent Bench tasks in isolated environments. The paper evaluates whether process-supervised tactic accumulation improves long-horizon bioinformatics workflow completion, biological correctness, and execution efficiency over no-memory and reflection-style baselines.

---


### 75. [From Uncertainty to Stability and Fidelity: Guiding Sparse-View 3D Gaussian Splatting with Fisher Information](https://arxiv.org/abs/2606.20842)

**<font color=#1a73e8>作者：</font>** Junbao Zhou, Qingshan Xu, Yuan Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has emerged as a promising technique for novel view synthesis. However, 3DGS requires dense input views to achieve high-quality rendering. In sparse-view scenarios, 3DGS often prones to overfitting, resulting in noticeable artifacts and degraded rendering quality. Previous methods explore to address this issue by introducing additional priors (e.g. depth priors) or integrating regularization techniques (e.g. Dropout). However, these methods are often applied without principled guidance. In particular, prior-based augmentation typically samples novel viewpoints randomly, while Dropout-based regularization randomly removes Gaussians. The compounded randomness introduces uncertainty and instability, limiting the fidelity of novel view synthesis. In this paper, we propose a novel method for sparse-view 3DGS that incorporates Fisher Information to quantitatively guide the utilization of geometric priors and regularization. Specifically, our method comprises two key components: (1) Stereo augmentation with Fisher Information. By leveraging Fisher Information, we actively select most informative supporting views and use depth priors to curate reliable pseudo ground truths, which reduces randomness in augmentation and improves stability and rendering fidelity; (2) Uncertainty-aware regularization. We reduce the instability of Dropout-based regularization by using Fisher Information to quantitatively measure the uncertainty of each 3D Gaussian, and adaptively adjust the removal probability, leading to more stable and effective regularization. With these two components, our method effectively mitigates overfitting and improves the stability of optimization in sparse-view 3DGS, resulting in superior rendering fidelity. Extensive experiments show that our method achieves state-of-the-art performance in sparse-view novel view synthesis benchmarks.

---


### 76. [Stochastic Signed Distance Processes](https://arxiv.org/abs/2606.20856)

**<font color=#1a73e8>作者：</font>** Hiroki Sakuma, Masatoshi Okutomi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view surface reconstruction is a core problem in computer vision. One prominent line of work represents the surface implicitly as a signed distance field (SDF), optimizing it based on the photometric loss between rendered and observed pixel colors. These approaches typically employ SDF-based volume rendering to obtain a differentiable relaxation of discontinuous visibility along rays, thereby reducing reliance on silhouette supervision. In this paper, we reformulate SDF-based volume rendering as probabilistic surface rendering, where each pixel color is modeled as a mixture distribution induced by the random first ray-surface intersection. To this end, we introduce Stochastic Signed Distance Processes (SSDP), which model the SDF along each ray as a stochastic process, inducing a first-passage-time distribution for each ray. We then derive the first-passage probability for each sampling interval based on Bayesian filtering, together with its practical approximation for parallel rendering. We further show that NeuS, an existing SDF-based volume rendering method, arises as a special case of our formulation. Experiments on the DTU and MobileBrick datasets demonstrate that our method outperforms baselines in both surface reconstruction and uncertainty quantification, supporting the effectiveness of our first-passage formulation. Our code is available at this https URL.

---


### 77. [SignVLA: Real-Time Sign Language-Guided Robotic Manipulation via Attention LSTM and Vision-Language-Action Models](https://arxiv.org/abs/2606.20857)

**<font color=#1a73e8>作者：</font>** Ningwei Bai, Xinyu Tan, Harry Gardner 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models enable robots to execute manipulation tasks from natural-language instructions grounded in visual observations. However, existing VLA interfaces primarily rely on speech or text input, limiting accessibility for deaf, hard-of-hearing, and speech-impaired users. We present SignVLA, a real-time sign-language-guided VLA framework for accessible human-robot interaction. The system introduces a modular sign-to-text interface that converts visual sign gestures into semantic instructions compatible with downstream VLA policies. Given video streams, SignVLA extracts hand landmark features and employs an attention-enhanced Long Short-Term Memory (LSTM) network to capture temporal gesture dynamics for alphabet- and command-level sign recognition. A temporal stabilization module further improves prediction consistency in real-time interaction this http URL generated instruction sequence is then passed to a downstream VLA policy for sign-conditioned robotic manipulation. Experimental results demonstrate stable real-time sign recognition and successful execution of manipulation tasks driven by sign-language inputs. Our findings suggest that lightweight temporal sign recognition can serve as an effective and practical accessibility layer for multimodal embodied intelligence.

---


### 78. [Evolutionary Discovery of Developmental Reward Schedules in Deep Reinforcement Learning](https://arxiv.org/abs/2606.20858)

**<font color=#1a73e8>作者：</font>** Alan Nadelsticher Ruvalcaba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The temporal structure of reward composition in reinforcement learning (RL) is typically hand-designed and held fixed throughout training, leaving the progression of motivational priorities largely unexplored. In this work, we propose an evolutionary framework for discovering developmental reward schedules, in which three distinct biologically inspired motivational components -- agency, novelty, and reactivity -- are combined through time-varying weights that dynamically shift over the course of training. Evaluated on two sparse-reward MiniGrid tasks: DoorKey-6x6 and KeyCorridorS3R1, our framework compares the generalizability of four evolutionary algorithms: CMA-ES, xNES, DE, and L-SHADE against an extrinsically motivated baseline (our main comparison point), and three additional hand-designed methods. On DoorKey-6x6, all evolved methods outperform the non-evolved baselines, with L-SHADE achieving the best performance -- an approximate relative mean improvement of 11.4% over the extrinsic only baseline. On KeyCorridorS3R1, CMA-ES achieves the best overall performance, with the remaining evolved methods showing weaker and less reliable generalization capability compared to the extrinsic only baseline. Interestingly, the discovered schedules diverge from our defined developmental ordering, with novelty consistently emerging as the dominant early signal during training, across both tasks. Collectively, our results position evolutionary optimization as a promising approach for developmental reward schedule discovery in deep reinforcement learning, and suggest that what evolution finds to be optimal in computational settings may differ from what it finds to be optimal in biology. The code for this project can be found at: this https URL.

---


### 79. [Synthetic Network Packet Generation through Statistical Learning and Genetic Algorithms](https://arxiv.org/abs/2606.20864)

**<font color=#1a73e8>作者：</font>** Mayank Raj, Nathaniel D. Bastian, Lance Fiondella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Developing robust intrusion detection systems (IDS) for IoT environments requires large, labeled datasets capturing realistic traffic distributions across both benign and malicious activity. Existing public datasets suffer from fixed activity distributions and extreme class imbalance, while deep generative models (GANs, VAEs) provide no mechanism to enforce that synthetic packets remain within physically valid feature ranges. This paper proposes and compares two constraint-enforcing approaches for synthetic IoT network packet generation: (i) a statistical learning method combining PCA-based latent space sampling with dual One-Class SVM (OCSVM) and Isolation Forest (IF) boundary enforcement, and (ii) a genetic algorithm (GA) method that treats packet generation as a multi-objective optimization problem with explicit fitness criteria for anomaly model acceptance and distributional fidelity. Both methods embed hard validity constraints -- dual anomaly-detection gating, feature-range clamping, and independent validation -- directly into the synthesis pipeline. Evaluation on the complete ACI IoT 2023 dataset (1,231,411 packets, 12 attack categories, class imbalance up to 175,805:1) demonstrates that both methods achieve PASS status across all categories under independently trained validators with a 30% anomaly rate threshold: the statistical method attains 1.20% average anomaly rate with ~1,091 packets/s throughput, while the GA attains 0.62% average anomaly rate with organic per-class variance (0.00%-2.50%) at ~5.7 packets/s. Both methods successfully amplify the 5-sample ARP Spoofing category by 200x to 1,000 validated packets. The ~190:1 throughput ratio between methods, combined with their complementary quality profiles, provides evidence-based selection criteria for deployment contexts ranging from rapid dataset augmentation to adversarial robustness testing.

---


### 80. [FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation](https://arxiv.org/abs/2606.20867)

**<font color=#1a73e8>作者：</font>** Duc Minh Nguyen, Nghiem Tuong Diep, Binh Gia Nguyen 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models enable general-purpose robotic control via large-scale multimodal pretraining, yet their effectiveness under few-shot imitation learning remains limited. We conduct a systematic stress test of state-of-the-art VLA models and show that performance degrades sharply as demonstrations are reduced, revealing a key weakness of existing adaptation strategies. To address this, we introduce FOCA, a future-oriented conditioning framework for data-efficient VLA adaptation. FOCA combines explicit prediction of task-grounded future interaction embeddings with implicit alignment to future goal observations, enabling long-horizon reasoning in latent space without pixel-level prediction. This formulation naturally supports action-free co-training with synthetic videos from video world models and can be interpreted as learning a future-conditioned value-like representation. Extensive experiments demonstrate FOCA achieves 95.7% success with 20 demonstrations on LIBERO, improves 7-12% on RoboCasa, and delivers up to 26% absolute gains on real robots, establishing a new state of the art in few-shot VLA adaptation.

---


### 81. [Machine Learning Classification of Cryopathy Syndromes: A Comprehensive Comparative Study](https://arxiv.org/abs/2606.20874)

**<font color=#1a73e8>作者：</font>** Nataliya Shakhovska, Valentyna Chopyak, Ivan Izonin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cryopathy syndromes are difficult to classify because laboratory patterns often overlap across diagnostic categories, while some diagnoses are rare. This makes routine interpretation of cryoglobulin-related tests challenging and increases dependence on expert judgment. The aim of this study was to develop and compare machine learning approaches for automated classification of cryopathy syndromes from laboratory data and to identify a practical strategy for clinical decision support. Methods: We analysed laboratory records from 2,686 patients assigned to 14 diagnostic categories. The dataset included demographic variables, cryoglobulin measurements, precipitation tests, and hemagglutinin and hemolysin titers. Data preprocessing included cleaning, encoding, imputation, normalization, and construction of clinically informed interaction features. We evaluated 12 modelling strategies, including Random Forest, Gradient Boosted Trees, Multi-Layer Perceptron, soft-voting ensembles, class balancing with Synthetic Minority Over-sampling Technique, hierarchical classification, period-aware models, targeted binary classifiers, and probability calibration. Performance was assessed using stratified train-test evaluation and stratified 5-fold cross-validation. The main metrics were macro-averaged F1 score, accuracy, Top-3 accuracy, and expected calibration error. The overall task proved difficult because of marked class imbalance and clinical overlap between diagnoses. The best multiclass performance was achieved by a soft-voting ensemble of Random Forest and Gradient Boosted Trees. Cross-validation confirmed stable performance for the balanced Random Forest model. Tree-based methods consistently outperformed the neural network model. Feature engineering improved discrimination, and the most informative predictors were derived cryoglobulin-based interaction features.

---


### 82. [Artificial collectives of specialists and generalists excel at different tasks](https://arxiv.org/abs/2606.20877)

**<font color=#1a73e8>作者：</font>** John Meluso, Laurent Hébert-Dufresne, Christoph Riedl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Collective artificial intelligence, where multiple agents work on shared tasks, holds potential to solve expansive problems in fields from medicine to collective governance. But while prescriptive engineering solutions abound, we lack descriptive scientific understanding of artificial collectives, and therefore principles for how to design resource efficient multi-agent systems. Through systematic experiments with optimizing agents, we characterize how agent interpretive abilities, rationality bounds, and task qualities interact to shape collective performance. Agents range from specialists, with narrow interpretive abilities, to generalists, with broad ones. Collectives of specialists correspond to sparse, centralized networks, while collectives of generalists correspond to dense, decentralized ones. We show that interpretive network properties have small performance effects on average (0.07 standard deviations of performance). However, for specific task qualities, these effects are 4.5 times larger (0.33 sd) and can reach much higher for certain task qualities (1.84 sd). This leads collectives of generalists to perform better on tasks that involve generating, choosing, and coordinating, while collectives of specialists with a few generalist mediators perform better on tasks that involve negotiating. Rationality bounds then moderate these relationships. At loose bounds, specialists outperform generalists through more effective sampling of high-dimensional decision spaces. At tight bounds, generalists outperform specialists through better gradient estimation. A fundamental trade-off between performance and convergence speed emerges at moderate bounds. These findings suggest that multi-agent design could benefit from matching interpretive networks to both task demands and agents' computational limits, with implications for the efficiency and energy costs of multi-agent systems.

---


### 83. [Understanding Latent Flow Models for Tabular Data Synthesis: Targets, Paths, and Sampling](https://arxiv.org/abs/2606.20878)

**<font color=#1a73e8>作者：</font>** Bahrul Ilmi Nasution  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic tabular data enables microdata sharing in regulated domains, yet deploying continuous-time generative models requires balancing analytical utility, disclosure risk, and computational cost. Latent-space flow models are flexible, but theoretical equivalences across learning targets, probability paths, and sampling dynamics can translate into different behaviour under finite-step integration and explicit compute budgets. We present an empirical study of tabular latent flow models across seven datasets, evaluating velocity, score, noise, and posterior matching objectives under optimal transport (OT) and variance-preserving (VP) paths, ODE and SDE sampling, and varying integration budgets. Our contributions are threefold: (1) we show that the learning target largely determines the utility-risk operating regime, with velocity and posterior matching tending to yield higher utility, while score and noise matching tend to achieve lower disclosure risk; (2) we demonstrate that configuration and sampling choices shift performance, with midpoint often improving distributional fidelity and OT paths often tolerating earlier stopping than VP, enabling compute savings under fixed budgets or risk thresholds; and (3) we distil these findings into actionable defaults and practical configuration guidance to support pre-release model selection under disclosure risk and resource constraints. The code implementation and supplementary materials can be accessed in this https URL.

---


### 84. [Toward Parking Spot Occupancy Recognition: A Self-Supervised Approach](https://arxiv.org/abs/2606.20886)

**<font color=#1a73e8>作者：</font>** Luan Marko Kujavski, Rayson Laroca, Paulo Lisboa de Almeida  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As urban areas expand, automatic monitoring of parking lots becomes essential for efficient and sustainable cities. This work proposes a self-supervised approach for parking spot occupancy recognition that requires no labeled samples from the target parking lot. Building upon a self-supervised transfer learning fine-tuning protocol, the proposed training strategy consists of two self-supervised stages: first on unlabeled generic data and then on unlabeled target-specific data, followed by supervised fine-tuning using only generic parking lot labels. We adopt SimCLR with a ResNet-50 encoder and evaluate the method under a leave-one-out cross-environment protocol on three public datasets: PKLot, CNRPark-EXT, and PLds. We also introduce a two-stage deployment strategy in which a Strong General Model is initially deployed, followed by a Specialized Model that incorporates unlabeled images collected during the first N days of deployment in a self-supervised manner. Experimental results show that the Strong General Model alone outperforms supervised and self-supervised baselines, achieving an average accuracy of 97.2%, which further improves to 97.8% with the proposed two-stage strategy. These results demonstrate that self-supervised learning enables a scalable and labelefficient solution for real-world parking occupancy monitoring. Our trained models and source code are publicly available at this https URL.

---


### 85. [Temporal Causal Prior-Data Fitted Networks for Panel Data with Learned Reliability Signals](https://arxiv.org/abs/2606.20889)

**<font color=#1a73e8>作者：</font>** Shravan Talupula, Saurabh Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating causal effects in industrial time series requires handling temporal dynamics, time-varying treatments, and unobserved confounders. Existing causal foundation models (CausalPFN, CausalFM) operate only on static cross-sectional data; neural temporal methods (CRN, G-Net) require per-dataset training; and concurrent temporal-PFN proposals have not been demonstrated at industrial scale. None output explicit per-pair reliability signals alongside their CATE estimates.
We introduce Temporal Causal Prior-Data Fitted Networks (TCPFN), a foundation model for zero-shot temporal causal discovery with learned reliability signals. TCPFN makes four contributions: (1) a Causal Judgment Head that jointly predicts null-effect probability, confounding strength, identifiability, mediation fraction, and causal regime; (2) a mixed training prior covering six causal regimes (independent, direct, confounded, mediated, time-varying confounded, feedback) plus CausalFM-style front-door and instrumental-variable priors; (3) a discrete-token panel-data architecture with cross-attention masking that prevents inter-horizon leakage; (4) zero-shot inference at industrial scale via FAISS-based context selection and one-step posterior correction.
On 19 benchmark datasets across five domains, TCPFN achieves competitive zero-shot causal discovery: AUROC 0.96 on Tennessee Eastman, 0.93 on SWaT, 0.98 on Causal Rivers, 0.97 on CAUSRCA. The null detector reaches NullF1 0.94, AUROC 0.99. TCPFN scales to V=1,275 on a proprietary Kraft pulp-and-paper dataset in 6 hours on a single GPU; PCMCI, a CPU-only library, on a V=666 sub-panel of the same data took 81.5 hours, extrapolating by O(V^2) to ~12.5 days at V=1,275. TCPFN's top edges identify cross-subsystem causal relationships while PCMCI's surface within-instrument controller-measurement coupling -- a scalability case study.

---


### 86. [Go-with-the-Track: Video Compositing and Motion Control with Point Tracking](https://arxiv.org/abs/2606.20891)

**<font color=#1a73e8>作者：</font>** Koichi Namekata, Yash Kant, Zhizheng Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Filmmaking demands precise motion control and reference image compositing -- capabilities that existing methods treat separately. Point-track-conditioned image-to-video models restrict content insertion to the first frame, while reference-to-video models lack fine-grained spatial-temporal control over how reference content integrates across frames.
We present Go-with-the-Track, which unifies both capabilities by jointly conditioning on multiple reference images and reference-anchored point-tracks -- extending conventional point-tracks to explicitly establish correspondences between generated frames and reference images, thus enabling precise compositing and motion control throughout the video.
To achieve this, we introduce spatially-aware point-track embeddings that encode the full sequence of point-track coordinates using a coordinate-wise MLP followed by temporal pooling. This representation captures the spatial characteristics of each point-track (serving as a unique identifier), while the embedding similarity correlates directly with spatial proximity, enhancing the model's ability to distinguish and associate point-tracks. We inject these point-track embeddings into a video diffusion transformer via a lightweight adapter, resolving the pixel-to-patch resolution mismatch while avoiding the substantial motion detail loss inherent in naive point-track subsampling.
We use a hybrid training strategy to train jointly on dynamic, static, and synthetic scene video datasets to boost motion controllability. Experiments demonstrate that Go-with-the-Track achieves superior motion and reference control in a single model and enables new capabilities: multi-reference conditioned video generation with point-track driven compositing, as well as camera control for both static and dynamic scenes. Project Page: this https URL

---


### 87. [Storyline Trees: Hierarchical Representations for Long-Form Narratives](https://arxiv.org/abs/2606.20900)

**<font color=#1a73e8>作者：</font>** Litu Ou, Mirella Lapata  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form narratives are challenging for long-context models because their structure is implicit: events, characters, and plotlines interact across hundreds of pages without the explicit cues that guide navigation in structured documents. We address this by constructing storyline trees, hierarchical representations that organize narratives from global themes and major plotlines to fine-grained events. We first segment chapters into contiguous narrative segments, or scenes, and use them as the basic units for tree construction. We then infer storyline trees through complementary top-down and bottom-up procedures that derive, refine, cluster, and summarize storylines at multiple levels of abstraction. We showcase the utility of this representation for question answering: storyline trees enable adaptive retrieval, allowing models to iteratively inspect high-level narrative structure and retrieve scene-level evidence on demand. Experiments on three long-context narrative QA benchmarks show that adaptive retrieval outperforms strong baselines, including post-trained long-context models and agentic chunk-based methods. Ablations confirm that scenes are more effective basic units than chapters or generic segmentation, and that gains persist under matched retrieval budgets

---


### 88. [MMGNN: Multi-level, multi-color graph neural networks for molecular property prediction](https://arxiv.org/abs/2606.20906)

**<font color=#1a73e8>作者：</font>** Trung Nguyen, Duc Duy Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular message-passing neural networks commonly propagate chemically diverse interactions through a single graph, which may mix interaction-specific signals and require deep propagation to capture long-range effects. We introduce the Multi-level, Multi-color Graph Neural Network (MMGNN), a hierarchical framework that decomposes a molecular graph into overlapping atom-type-pair-specific subgraphs while preserving atom-level resolution. MMGNN-2D constructs chemical-colored subgraphs from covalent connectivity, whereas MMGNN-3D constructs geometric-colored subgraphs from spatial proximity and augments their edges with distance, angular, and torsional descriptors. Both variants apply a shared communicative message-passing backbone to each subgraph and combine the resulting representations through atom-wise aggregation and molecular readout. We evaluated MMGNN on five classification and three regression benchmarks from MoleculeNet using common scaffold splits and five independent runs. MMGNN-2D achieved the highest macro-average AUC-ROC of 0.838 across the classification datasets and the lowest RMSE on ESOL (0.803). MMGNN-3D obtained the highest mean AUC-ROC on BBBP (0.956) and the lowest RMSE on FreeSolv (1.793), indicating complementary strengths of topological and geometric representations. Structural and leave-one-out analyses further illustrate how the subgraph decomposition affects learned representations and atom-type-pair sensitivities. These results support overlapping interaction-specific graph decomposition as a competitive strategy for molecular property prediction.

---


### 89. [BELDE: Building a Large-scale Earth-observation Land-cover Dataset for Europe](https://arxiv.org/abs/2606.20909)

**<font color=#1a73e8>作者：</font>** Ümit Mert Çağlar, Alptekin Temizel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth observation imagery plays a critical role in environmental monitoring, urban planning, disaster assessment, and climate analysis. While multi-spectral sensors are increasingly available, true-color (RGB) imagery remains widely used due to the power, cost, and deployment constraints of many satellite and aerial platforms. However, existing land-cover segmentation datasets are often limited in geographic coverage, scale, or public accessibility.
To bridge this gap, we introduce BELDE (Building a Large-scale Earth-observation Land-cover Dataset for Europe), a publicly available dataset tailored for RGB-based remote sensing semantic segmentation. Constructed from Sentinel-2 true-color images and ESA WorldCover data annotations, BELDE contains 1,088,385 curated image-segmentation map pairs spanning Europe with 7 land-cover classes at 10 m spatial resolution, making it one of the largest publicly available RGB land-cover segmentation datasets for Earth observation. To facilitate cross-region generalization studies, we additionally introduce BELDE-K (16,607 pairs) covering the Republic of Korea and BELDE-CA-NV (88,155 pairs) covering California and Nevada in the United States.
We establish baseline results using multiple semantic segmentation architectures and evaluate both in-domain and cross-domain performance. Models trained on BELDE achieve an F1 score of 83.0% on the European test set, while performance decreases to 66.4% on BELDE-CA-NV and 58.3% on BELDE-K, highlighting the challenges posed by out-of-distribution geographic domain shift. By providing a continental-scale RGB segmentation and evaluation benchmark, BELDE supports the development of robust and transferable Earth observation models. The dataset and benchmark resources will be publicly released.

---


### 90. [Root Cause Analysis with Latent Confounders using Partial Ancestral Graphs](https://arxiv.org/abs/2606.20912)

**<font color=#1a73e8>作者：</font>** Henrique O. Caetano, Rafael Arone, Carlos Dias Maciel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Finding the source of failures, known as Root Cause Analysis (RCA), is essential for identifying the root causes of anomalies and maintaining the reliability of complex systems. While causal theory has advanced data-driven RCA, existing frameworks assume causal sufficiency, failing to account for the unobserved latent variables prevalent in real-world environments. To address this gap, we propose PAG-RCA. This framework models system failures as parametric interventions over Partial Ancestral Graphs (PAGs) to perform RCA in the presence of latent variables. We use standard causal identification algorithms to find the source of failures by quantifying causal effects over the PAG. When an effect is identifiable, candidate root causes are ranked based on their exact intervention effects. When effects are structurally unidentifiable, our framework (for the first time in the RCA literature) integrates partial identification to evaluate and score candidates using analytical causal bounds. By integrating latent variables and partial identification at once our framework ensures robust RCA even under data scarcity and latent-variable scenarios where traditional methods degrade. Evaluations on synthetic data, microservice anomaly benchmarks and power-grid cascading failures demonstrate that PAG-RCA consistently outperforms state-of-the-art data-driven baselines. By improving data-driven RCA performance under data scarcity, this methodology advances reliable automated diagnostics in partially observable complex networks.

---


### 91. [PROTON: Prototype-Based Test-Time Online OOD Detection for Medical VLMs](https://arxiv.org/abs/2606.20913)

**<font color=#1a73e8>作者：</font>** Abhijit Das, Nichula Wasalathilaka, Yifan Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) enable zero-shot clinical image classification, yet reliably detecting out-of-distribution (OOD) inputs at deployment remains an open problem. No static scoring method works across all shift types: Maximum Concept Matching (MCM) on FLAIR achieves 76.4% AUROC for far-OOD but only 42.4% for covariate shifts such as ultra-wide-field fundus images, effectively random. We trace this to a structural mismatch: covariate-shifted inputs are indistinguishable from in-distribution samples in softmax space, yet occupy distinct regions in the VLM embedding space. To exploit this untapped signal, we propose PROTON (PROtotype-based Test-time ONline OOD detection), a lightweight post-hoc module that maintains an online prototype bank from high-confidence test predictions and adaptively fuses prototype distance with MCM scoring via stream-level variance statistics, requiring no model modification, training data, or prompt engineering. On the ophthalmology benchmark FLAIR + FIVES, PROTON improves MCM by +23.9 AUROC on covariate shift, +8.8 on semantic shift, and +8.1 on far-OOD, making it the only zero-shot method to improve all three without hierarchical prompts or labeled data. Code is available at this https URL, and the project page is available at this https URL.

---


### 92. [Physics-Guided Dual-Stream Heterogeneous Graph Neural Network for Predicting Full-Field Structural Response of Stiffened Panels](https://arxiv.org/abs/2606.20916)

**<font color=#1a73e8>作者：</font>** Yuecheng Cai, Jasmin Jelovica  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative design and optimization of large, complex structures require fast and accurate prediction of stress, displacement, and other fields. Finite element analysis (FEA) is computationally expensive for this task. Existing neural network surrogates often struggle with varying topologies and complex boundary conditions. This study proposes the novel Dual-Stream Heterogeneous Graph Neural Network (DS-HGNN) for full-field stress and displacement prediction in thin-walled structures, demonstrated on box beams made of stiffened panels. DS-HGNN operates on panel-level heterogeneous graph representations and introduces physics-guided edge states initialized from edge types, spatial information, and boundary kinematics. These states are updated through dual-stream message passing that separates longitudinal and transverse structural information while allowing cross-stream exchange. Geometry and loading effects are incorporated through Feature-wise Linear Modulation (FiLM)-conditioned 1-D spectral convolutions, and physical fields are reconstructed using a spectral-bypass low-rank readout. The model is evaluated on stiffened panel datasets with different geometries, boundary kinematics, loading conditions, and material nonlinear responses. DS-HGNN achieves the lowest stress and displacement RMSE compared with six benchmark heterogeneous graph neural network models. It also reaches comparable accuracy to the strongest benchmark models using 19%-38% fewer training samples. A targeted evaluation further shows that DS-HGNN captures yield and post-yield stress features.

---


### 93. [Short-Term Electricity Demand Forecasting for New England Using a Hybrid Transformer-XGBoost Framework with Weather, Calendar, and COVID-19 Indicators](https://arxiv.org/abs/2606.20918)

**<font color=#1a73e8>作者：</font>** Reza Ghanavati, Behrooz Mosallaei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate short-term electricity demand forecasting is critical for reliable power system operation, energy market planning, and infrastructure optimization. This paper presents a hybrid framework combining a Transformer encoder for temporal feature extraction with gradient-boosted decision trees (XGBoost) for daily electricity demand forecasting across New England. The framework integrates meteorological observations from six cities spanning all six New England states, calendar and holiday effects, autoregressive demand lags, and COVID-19 epidemiological variables. Hyperparameter optimization uses Optuna with a multivariate Tree-structured Parzen Estimator over 500 trials, with a leakage-free 70/15/15 chronological train-validation-test split. The hybrid model achieves a test RMSE of 8,876 MWh, MAPE of 2.05%, and R-squared of 0.906. A tabular-only XGBoost baseline achieves RMSE of 9,304 MWh, MAPE of 2.21%, and R-squared of 0.896. A Diebold-Mariano test (Harvey-Leybourne-Newbold correction) confirms the 427.7 MWh difference is statistically indistinguishable from noise (DM = -1.126, p = 0.262). An ablation study reveals COVID-19 features improved training accuracy but had asymmetric test effects: removal degraded hybrid RMSE by 3.2% while marginally improving XGBoost-only by 1.2%. A SHAP temporal analysis shows 5 of 8 COVID features rank higher on the post-acute test set than during pandemic-active training, indicating the model over-applies learned pandemic patterns. These findings establish temporal validity decay as a central mechanism: behavioral disruptions drove a strong COVID-demand signal during 2020-2021, but adaptation was complete by mid-2022, leaving epidemiological features as noise amplifying overfitting to stale pandemic patterns.

---


### 94. [$Ω$: Operator-based Mixture Ensemble for Generative Assimilation](https://arxiv.org/abs/2606.20920)

**<font color=#1a73e8>作者：</font>** Pouria Behnoudfar, Nan Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Characterizing non-Gaussian posterior distributions in partially observed high-dimensional nonlinear systems remains a fundamental challenge in data assimilation. Ensemble Kalman filters rely on Gaussian approximations that can be inaccurate for strongly non-Gaussian posteriors, whereas particle filters suffer from severe scalability limitations. Recent score-based generative approaches improve posterior characterization but typically require supervised training with ground-truth posterior samples, which are unavailable in most practical applications. We introduce $\Omega$ (Operator-based Mixture Ensemble for Generative Assimilation), a scalable framework that integrates conditional Gaussian surrogate modeling, unsupervised score learning, and generative sampling. The conditional Gaussian surrogate provides a nonlinear non-Gaussian baseline approximation while admitting closed-form conditional posterior distributions for the unresolved variables. First, $\Omega$ exploits these closed-form conditional distributions to analytically recover the high-dimensional unobserved component, reducing computational cost and mitigating the curse of dimensionality. Second, $\Omega$ learns only the residual discrepancy beyond an analytical baseline through denoising score matching using ensemble trajectories alone, eliminating the need for ground-truth posterior samples and substantially reducing the learning burden. Third, $\Omega$ reconstructs the full non-Gaussian posterior distribution of both observed and unobserved variables via a Gaussian mixture representation, capturing multimodal, skewed, and heavy-tailed statistics. Finally, $\Omega$ employs annealed Langevin sampling to iteratively refine ensemble members from the baseline toward the target posterior. $\Omega$ is validated on several turbulent models with intermittency and extreme events, consistently improving posterior accuracy.

---


### 95. [ELDiff: When Evidential Learning Meets Text-to-Image Diffusion](https://arxiv.org/abs/2606.20924)

**<font color=#1a73e8>作者：</font>** Qingtao Pan, Kai Ye, Zhihao Dou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In multi-object text-to-image (T2I) diffusion, ensuring semantic consistency between textual prompts and generated visual content is crucial for image synthesis. However, such consistency constraint is often underemphasized in the denoising process of diffusion models. Although token supervised diffusion models can mitigate this issue by learning object-wise consistency between the image content and object segmentation maps, it tends to suffer from the problems of segmentation map bias and semantic overlap conflict, especially when involving multiple objects. In this paper, we propose ELDiff, a new evidential learning-supervised T2I diffusion model, which leverages the advantages of uncertainty metric and conflict detection to enhance the fault tolerance of unreliable segmentation maps and suppress semantic conflicts, strengthening object-wise consistency learning. Specifically, a pixel evidence loss is proposed to restrain overconfidence in unreliable labels through evidential regularization, and a token conflict loss is designed to weaken the contradiction between semantics through optimizing a measured conflict factor. Extensive experiments show that our ELDiff outperforms existing training based and train-free based T2I diffusion models on SD v1.4, SD v2.1, SDXL, SD v3.5, and Qwen-Image, without requiring additional inference-time manipulations. Notably, ELDiff can be seamlessly extended to the existing training pipeline of T2I diffusion models. Code can be found at this https URL.

---


### 96. [Hierarchical Pooling for Sheaf Neural Networks](https://arxiv.org/abs/2606.20932)

**<font color=#1a73e8>作者：</font>** Dionisia Naddeo, Carlo Abate, Pietro Liò 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sheaf Neural Networks (SNNs) generalize Graph Neural Networks (GNNs) by replacing scalar node signals with stalk-valued signals and by using restriction maps to measure compatibility across edges. Unlike standard graph diffusion, which encourages neighboring node features to become similar, sheaf diffusion promotes consistency through the restriction maps and can therefore model more general relationships between neighboring nodes. However, existing sheaf neural architectures mainly operate at a fixed graph resolution and do not provide a principled pooling mechanism for building hierarchical representations. In this paper, we introduce Hierarchical Sheaf Pool (HiSP), a sheaf-aware pooling framework based on local spectral coarsening. Given a partition of the graph, HiSP constructs each coarse stalk by projecting fine stalk-valued features onto the low-frequency eigenmodes of the cluster-internal sheaf Laplacian. These local modes define a cochain-level prolongation map, which allows the fine sheaf energy to be represented on the coarse space through a Galerkin operator. We further analyze the approximation induced by coarsening by separating truncation loss, due to discarded local modes, from realization loss, due to representing the projected operator as a coarse sheaf. Finally, we implement HiSP as a GNN pooling layer compatible with SNNs and provide a PyG implementation supporting batching, lifted sheaf Laplacians, and hierarchical architectures.

---


### 97. [Comparing Transformers and Hybrid Models at the Token Level](https://arxiv.org/abs/2606.20936)

**<font color=#1a73e8>作者：</font>** Yanhong Li, William Merrill  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hybrid language models that mix attention and recurrent layers have shown promise: theoretically, recurrent layers ameliorate the limitations of pure transformers on state tracking, and empirically, hybrids can outperform pure transformers in loss and downstream evaluations \citep{waleffe2024empirical,merrill2026olmohybrid}. Yet it remains unclear which data or capabilities drive these gains, and to what degree they reflect the theoretical advantages motivating hybrid models. We address this question using the open weights from Olmo 3 \citep{olmo2025olmo3} and Olmo Hybrid \citep{merrill2026olmohybrid}: we compare the loss of a matched transformer and hybrid at the same target tokens under the same prefixes, stratifying the results by natural token tags, copy features, delimiter structure, and controlled synthetic probes. The hybrid has lower loss on most tag families, but the gains are not uniform: they are largest for open-class content words and smaller for many closed-class function words. Across prose, code, and markup, the hybrid's loss advantage is larger on opening delimiters than on the corresponding closing delimiters, and nearly vanishes on repeated $n$-grams. Synthetic probes show the same split: the hybrid is favored on pronoun-memory and entity-tracking tasks, whereas the transformer is favored on bracket-matching tasks that require choosing closing delimiters. These patterns suggest that the recurrent layers in hybrids improve predictions that leverage the semantic state of a document, whereas attention helps on tokens predictable by $n$-gram copying or syntactic bracket matching. We conclude with proof-of-concept filtered evaluations showing how token-level decompositions can sharpen pretraining diagnostics for hybrid architectures.

---


### 98. [Learning through Internalization](https://arxiv.org/abs/2606.20937)

**<font color=#1a73e8>作者：</font>** Nikolaos Tsilivis, Nirmit Joshi, Marko Medvedev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study internalization processes, by which neural-network-based systems absorb an explicit computational procedure into their own weights, and how they facilitate learning. We investigate how transformers internalize the simulation of semiautomata by internalizing chain-of-thought (CoT) tokens, which classes of semiautomata are harder to internalize, and expose the flip side of internalization, that is, a progressive degradation of out-of-distribution performance. We then provide the first provable analysis of successful internalization: for the task of learning parities, we show that a simplified one-layer transformer provably first learns the target with explicit CoT supervision and then internalizes the autoregressive generation as CoT tokens are progressively removed, learning to directly compute the parity. This task is computationally hard to learn from data without CoT supervision. Finally, we discuss how learning through internalization relates to the \textit{Positive Distribution Shift} phenomenon recently introduced by~\citet{Med+26}.

---


### 99. [Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention](https://arxiv.org/abs/2606.20945)

**<font color=#1a73e8>作者：</font>** Vishesh Tripathi, Abhay Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-attention is central to Transformer performance and is often the most expensive part of the Transformer at long context lengths because its pairwise token interactions scale quadratically with sequence length. Standard dense attention also applies the same set of attention heads to every token regardless of token difficulty or information content. This uniform activation can waste compute, especially as sequences grow longer and attention cost increases rapidly. We propose Grouped Query Experts (GQE), a mixture-of-experts layer on top of grouped-query attention (GQA). Within each GQA group, a router selects k query-head experts per token while all key-value (KV) heads remain dense and unchanged. Thus, GQE keeps the KV cache benefits of GQA and reduces only the active query-head computation. On a fixed 30B token budget at the 250M parameter scale, GQE matches the all-active GQA baseline in downstream accuracy while activating half the query heads per token.

---


### 100. [Scaling Diverse Language Generation for 3D Visual Grounding](https://arxiv.org/abs/2606.20946)

**<font color=#1a73e8>作者：</font>** Austin T. Wang, Dongchen Yang, Angel X. Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Developing robust models for 3D visual grounding (3DVG), the localization of entities in a 3D scene described in natural language, is important for enabling agents to correspond spatial language with objects in the physical world. However, the lack of diverse descriptions at scale prevents models from generalizing beyond simple linguistic patterns. Recent such attempts lack diversity in the constraint types and language used to ground objects. Captioning methods cannot precisely contrast objects, which is important for visual grounding. We therefore propose ViGiL3D++, a scalable, scene-agnostic method that generates diverse visual grounding queries by combining constraint sampling in scene graphs with the language generation of LLMs. We show that it has greater diversity over existing scaled datasets and improves model performance over several 3DVG benchmarks but also illuminates outstanding limitations of VLMs.

---


> [!TIP]
> 当前位于：**51-100**（第 2/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
