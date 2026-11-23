# 🧠 大模型相关研究 | 2026年11月24日

> 本类共 **200** 篇论文：已确认 **182** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md)

---

### 51. [Scalable Evaluation of Medical AI using Evidence-based Practice Recommendations](https://arxiv.org/abs/2611.27007)

**<font color=#1a73e8>作者：</font>** Teya Bergamaschi, Bijal Rajput, Akshay Goel 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rigorously evaluating medical artificial intelligence (AI) requires testing open-ended clinical management across diverse presentations and stages of care. However, existing benchmarks rely on manual expert authoring, limiting coverage across conditions, conditional care pathways, and evolving guidelines. We develop an automated pipeline that extracts and verifies structured clinical criteria and branching decision trees from practice recommendations to generate scenarios spanning the care continuum, including nuanced presentations and practice variations across regions and guideline editions. Applied to 436 BMJ Best Practice clinical monographs (354 US, 82 International), this yields 3,200 scenarios spanning differential diagnosis, investigations, treatment, and complications, plus targeted suites for regional specificity (731 US/International pairs) and temporal freshness (630 scenarios). To grade responses, we develop a clinician-calibrated autorater that scores management plans on a 4-point rubric stratifying deviations by clinical severity. Across Gemini models, scaling improves adherence, while web search (+0.8 percentage points [pp] on average) and multi-sample synthesis (+2.2 pp) combine additively (+2.8 pp). In context, full monographs consistently trail condensed excerpts. On targeted suites, web search narrows international performance gaps (+4.2 pp) and improves adherence to newly updated guidance (+4.6 pp). In a study with Primary Care Physicians (n = 9) across 200 scenarios, AI assistance raises adherence from 50.5% to 70.0%, driven largely by fewer clinical omissions. Overall, our results demonstrate a scalable evaluation setup using an evidence-based corpus originally written to guide human clinical decision-making, and demonstrate its viability to assess medical AI and its assistance on clinician decision-making.

---


### 52. [Actions Speak Louder than Words: Stateful Privacy Sniffing of LLM Agents via Behavioral Covert Channels in Web Interactions](https://arxiv.org/abs/2611.27046)

**<font color=#1a73e8>作者：</font>** Ruichao Liang, Wenzhong Deng, Jing Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on Web interaction, issuing searches, following links, and reading pages, to complete complex user tasks. Since each action is driven by the agent's private context, including the user's prompt, dialogue history, memory, and connected data, it also opens a new privacy exposure surface. Prior attacks either passively analyze network traffic, which yields only coarse correlations, or hijack the agent through indirect prompt injection, which must place sensitive content in an outgoing field and is blocked by content-level defenses. Whether an attacker can actively recover fine-grained private context without any explicit transmission thus remains insufficiently understood.
Our insight is that an agent's benign Web decisions themselves leak private context, as what it chooses to visit encodes whether, which, and in what order it acts, forming a behavioral covert channel. Building on this, we design SNOOP, a stateful hierarchical probing framework that narrows a coarse-to-fine hypothesis tree per task and reconstructs user queries and profiles from the agent's observable paths. Across four agents and three LLM backbones on 500 StackExchange queries and 378 multi-turn iKAT dialogues, SNOOP recovers query concepts with an average F1 of 0.89 and user profiles with an F1 of 0.80, while four representative agent defenses change its recovery by less than 0.03 F1. Since no sensitive content is ever transmitted, content-level inspection cannot detect this leakage; we therefore propose Selection-Obfuscated Retrieval (SOR), which acquires resources under a fixed budget independent of private context and confines the agent's selection to a local snapshot, cutting SNOOP's F1 to 0.39 without additional LLM inference.

---


### 53. [Towards Text-Mask Consistency in Medical Image Segmentation](https://arxiv.org/abs/2611.27050)

**<font color=#1a73e8>作者：</font>** Jie Gui, Hang Tu, Wen Sha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models for medical image segmentation often produce masks that conflict with the accompanying text, especially under multi-site/multi-lesion descriptions. We trace this failure to two factors: (i) highly templated and repetitive clinical language causes one-to-one hard contrastive learning to yield numerous false negatives, weakening cross-modal alignment; and (ii) predominantly vision-driven, one-way cross-attention lacks a language-dominant, spatially aware pathway, hindering effective injection of textual semantics into the spatial visual domain. To this end, we propose Consistency-enhanced Two-stage Segmentation (C2Seg). In the pretraining stage, Cluster-aware Contrastive Learning uses a frozen strong baseline to construct an intra-batch text similarity matrix as soft labels, thereby alleviating false negative conflicts and producing more discriminative visual representations. In the fusion stage, we introduce a Bidirectional Complementary Attention Module, where each modality dominates attention along its own path, fostering deep interaction and structural consistency between visual and textual representations. In order to enhance the expressive power of multimodal features, we further adopt KAN-based Attention Gating. Without updating the language encoder, our approach significantly improves text-mask consistency and segmentation accuracy on four public medical imaging datasets. The source code is available at this https URL.

---


### 54. [Dynamic Token Merging for Efficient Vision-Language Models](https://arxiv.org/abs/2611.27064)

**<font color=#1a73e8>作者：</font>** Chris Gu, Marco Andono Sie, Nathan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) represent each image with hundreds of visual tokens, which can make inference costly even when a prompt depends on only part of the image. Dynamic Token Merging (DTM), introduced in MrT5 for byte-level text encoders, learns which tokens to remove: a lightweight delete gate scores contextualized hidden states, acts as a differentiable attention bias during training, and physically removes tokens at inference. We argue that DTM is a general token deletion framework rather than a byte-level technique, and extend it to the vision modality and to decoder-only models. Applying DTM to T5Gemma 2 and Gemma 3 yields V-MrT5Gemma2, which deletes visual tokens inside a bidirectional multimodal encoder, and V-MrGemma3, which compacts the prompt and its key-value caches during decoder-only prefill. Across ten benchmarks, DTM's advantage over attention-based and random deletion grows with the deletion rate and is largest on document, chart, and scene-text reading. At 80% visual token deletion (approximately 60% fewer FLOPs), DTM raises accuracy over FastV from 51.8 to 63.0 on ChartQA and from 63.3 to 67.8 on TextVQA with V-MrT5Gemma2, as well as from 62.2 to 68.8 and from 71.2 to 75.1 with V-MrGemma3, retaining 90-96% of unpruned performance on both tasks with significant efficiency gains. These results support DTM as a general framework for efficient transformers.

---


### 55. [Decision Models Are General-Purpose Process Reward Models](https://arxiv.org/abs/2611.27068)

**<font color=#1a73e8>作者：</font>** Jiajun Fan, Qinglong Zheng, Ziwen Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) from verifiable outcomes gives a language agent one reward per episode: every step is credited alike, and nothing about the task is learned when all rollouts fail. The last mile, step-level credit, usually requires step labels, a learned critic, costly LLM judges or hand-written rules. We introduce DM-PRM, which turns a general-purpose decision model -- one answering yes/no questions with probabilities -- into a general-purpose process reward model (PRM), zero-shot: no step labels, no fine-tuning, no critic. DM-PRM asks one question per step and adds the standardised answers to the advantage. It plugs into any policy-gradient method; one model, with one question text per environment, serves household tasks, web shopping and multiple RL methods. With Qwen2.5-1.5B it lifts GRPO by over twenty points on ALFWorld and over ten on WebShop, overtakes GiGPO on ALFWorld and learns in far fewer iterations; it also improves GiGPO and GraphGPO on both benchmarks and reaches the highest success of our comparison, ahead of critic-based PPO and of state-of-the-art GiGPO, HGPO and GraphGPO. Its scores locate useful steps in failed rollouts, and trained agents drop idle actions and explore instead of circling. DM-PRM shows that step credit need not be learned: it can be asked for.

---


### 56. [$R^2$: Recognizing and Reducing Redundant Visual Tool Use](https://arxiv.org/abs/2611.27070)

**<font color=#1a73e8>作者：</font>** Yilin Zhao, Jinyu Wang, Wenming Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent studies have shown that visual tools can improve multimodal reasoning. However, the effects of tools vary substantially across samples, and benchmark accuracy alone does not reveal whether tool interactions are beneficial or redundant. We present $R^2$, a framework that recognizes and reduces redundant visual tool use in vision-language models. We first introduce a sample-level Category Analysis of Tool Utility (CAT), which categorizes samples according to whether a model can benefit from tools. This analysis reveals that benchmark scores may obscure a model's tool-use ability. Across seven benchmarks, samples benefiting from tools account for at most 12.44% of each benchmark, while the majority gain little from tool interaction or are even harmed by it. To assess individual calls, we propose the Visual Feedback Dependency (VFD) metric, which compares the likelihood of the same subsequent reasoning under actual and alternative visual feedback without an external evaluator or trajectory regeneration. Redundancy-Aware GRPO (RA-GRPO) combines this dependency signal with a category-conditioned base call cost to assign relative efficiency advantages among correct trajectories, supplementing outcome-based supervision. Across the seven benchmarks, RA-GRPO reduces the mean number of tool calls by 12.39% relative to Vanilla GRPO at comparable benchmark accuracy. Evaluated by tool-utility category, RA-GRPO improves category macro-average accuracy over Vanilla GRPO by 3.35 percentage points.

---


### 57. [When Do LLM-Elicited Priors Help? A Controlled Audit of Language Models as Priors for Small-Sample Bayesian Regression](https://arxiv.org/abs/2611.27075)

**<font color=#1a73e8>作者：</font>** Ran Zou, Yang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly asked where to center the coefficients of a small-sample Bayesian regression, but the evidence is unclear: benchmarks are often built to match the prior and models may remember them. We audit this practice with one frontier and one flash-tier model, using hidden feature names, post-cutoff housing data and a pre-specified test that gives features the wrong descriptions. First, the models share their errors (correlation $0.92$--$0.99$ across draws, vendors and paraphrases): averaging $20$ draws is no more accurate than one, and treating draws as independent creates overconfidence. Much of this error comes from reporting each feature's effect alone, not with the others held fixed. Second, against the best classical prior, the LLM center helps clearly on one of four benchmarks (RMSE $-5.8\%$), marginally on two, and hurts mean RMSE on the fourth. Third, the LLM's stated uncertainty is unreliable; letting the data set the prior scale cuts the harm of a wrong center four-fold against a unit-variance prior. A pre-specified external test returned the verdict \textsc{partial}: on $18$ rule-selected problems the center helps on six and hurts on four, and a hard trust gate trusts a harmful prior while an evidence-weighted mixture is safer.

---


### 58. [Accelerating Muon with Spectral Residual Correction](https://arxiv.org/abs/2611.27077)

**<font color=#1a73e8>作者：</font>** Zhixin Ren, Yao Lyu, Shengbo Eben Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon constructs matrix updates by applying a matrix-sign transformation to momentum. A common route to accelerating Muon is to modify the gradient or momentum before this transformation. We explore a complementary direction: refining the parameter step while retaining Muon's momentum recursion. Derived from the parameter subproblem of the ADMM-Inspired Momentum framework, AIMuon uses the gradient--momentum residual to correct the tentative spectral step. The residual undergoes a separate matrix-sign transformation, while spectral--nuclear duality determines the relative weighting of the momentum and residual directions. In practice, both directions are approximated with Newton--Schulz iterations and their combination is rescaled to match Muon's update magnitude. We establish a stochastic stationarity bound for the corresponding exact iteration. On GPT-2-small, GPT-2-medium, and Qwen3-0.6B, AIMuon reaches Muon's final validation loss with 8.98\%, 10.05\%, and 6.49\% fewer optimization steps, respectively, while achieving lower final validation loss than Muon, Muon-Nesterov, and MONA.

---


### 59. [How Far Does Lossless Re-tokenization Move an RLVR Update?](https://arxiv.org/abs/2611.27083)

**<font color=#1a73e8>作者：</font>** Zhe Dong, Fang Qin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models assign different probabilities to token sequences that decode to the same string. In reinforcement learning from verifiable rewards (RLVR), a trainer that re-encodes sampled text may train on a different token sequence with the same reward. We ask how far this moves a training update, and whether the movement has a consistent direction. From one checkpoint, we compare updates on the same rollouts, canonical and with selected tokens split into two pieces, against an update on a different batch. On Qwen2.5-0.5B with three-digit addition, splitting about one token in 25 moves the update 0.556 times as far as replacing the batch. The ratio rises with the fraction split in four models and depends on which tokens are split; within a checkpoint, the displacements share a direction across batches. In a tabular model with one table per tokenization and a single sampled string, we prove that whenever two strings below an unsampled prefix differ in probability, only the zero full-gradient step agrees across tokenizations, however it is weighted. In an audit that decodes and re-encodes resampled rollouts, re-encoding touches up to 5.2% of rollouts but at most 0.08% of tokens, far below the split fractions we test. Training on fixed rollouts, the canonical arm finishes ahead in 14 of 18 pre-registered pairs; the interval for the mean accuracy difference includes zero over all pairs and excludes it only under the registered exclusion rule, which favours the canonical arm.

---


### 60. [Auditing and Adapting kNNGuard for Long-Context Prompts](https://arxiv.org/abs/2611.27084)

**<font color=#1a73e8>作者：</font>** Niccolò Ronchetti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training-free activation guardrails such as kNNGuard score prompts by comparing last-token LLM hidden states (the Layer Ensemble branch, kNNGuard LE) and sentence embeddings (all-MiniLM-L6-v2, Embedding-kNN) against a small reference bank (50 examples per class), combining the two branches into a Fused Ensemble (kNNGuard FE). While effective on short inputs (up to 256 tokens), standard kNNGuard degrades substantially on long inputs (over 1000 tokens): averaged across Qwen3.5-4B and Gemma-4-E4B-it, kNNGuard LE AUROC drops from 0.742 (0.777 and 0.706) to 0.554 (0.587 and 0.521) on Content Harm Moderation (Aegis-2.0), and from 0.994 (0.995 and 0.992) to 0.556 (0.598 and 0.513) on RAG Hallucination Detection (HaluBench). We trace this degradation to three causes: (1) hidden-state drift as sequence length increases, (2) hard 256-token truncation in MiniLM, and (3) signal dilution when a long document is compressed into a single final-token vector. We then evaluate three training-free adaptations: a Length-Routed Dual Bank, a long-context embedding model (Qwen3-Embedding-0.6B), and Strided Window Pooling across intermediate token positions. On Content Harm Moderation, dual-bank routing and strided window pooling raise long-context kNNGuard LE AUROC from 0.554 to 0.828 (+0.274 AUROC) and fused kNNGuard FE AUROC from 0.721 to 0.886 (+0.164 AUROC) with no latency overhead from bank routing. On RAG Hallucination Detection, where the guardrail must verify logical consistency between a generated answer and a retrieved passage, sentence-embedding kNN remains near random chance across all lengths, while length-matched LLM hidden states (kNNGuard LE) recover medium-length detection (AUROC = 0.853) but remain limited on over-1000-token passages (AUROC = 0.607) due to final-token dilution over long contexts.

---


### 61. [Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation](https://arxiv.org/abs/2611.27089)

**<font color=#1a73e8>作者：</font>** Yalin Yang, Xiao Huang, Yanan Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Weight-space programming lets a language model inspect and edit another model's weights, offering an alternative to gradient-based adaptation. We evaluated both approaches using Qwen3.5-0.8B on a fixed reference-frame task (128 items), StepGame (200 items), and two untrained distance-comparison tasks. With thinking enabled, the public patch (p50c) raised mean accuracy from 0.0% to 22.1% on the reference-frame task and from 19.2% to 33.7% on StepGame across three sampling seeds. Randomly permuting its weight change removed the gain. Further closed-form edits did not improve on p50c, whereas a rank-1 LoRA adapter trained on worked solutions reached 100% and 98.8%, respectively, with 0.09% trainable parameters. Removing the worked solutions from supervision prevented the adapter from passing the learning gate. The trained adapters reached 82% accuracy on unseen StepGame sentence templates, 42% on held-out difficulty levels 6-10 after training on levels 1-5, and 33-50% on unseen heading-answer combinations. Their target gains coincided with a sharp decline on the distance tasks: accuracy fell from 94% and 92% under p50c to 0-2%, and their outputs applied the StepGame solution template to distance questions. With thinking disabled and reasoning requested in the visible answer, the base model also solved the distance tasks while remaining weak on the target tasks. The comparison reveals a trade-off between improving spatial task performance and preserving neighbouring skills: the public edit restored completion while preserving distance performance, whereas supervised adaptation produced much larger target gains together with interference across tasks.

---


### 62. [PLoQ: A Prompt-Specific Low-Rank Basis for 4-bit Quantization of LLM Activations](https://arxiv.org/abs/2611.27092)

**<font color=#1a73e8>作者：</font>** Faraz Tahmasebi, Michael Pellauer, Hyoukjun Kwon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit activation quantization of large language models remains challenging, as a small number of dominant directions dictate the quantization range. State-of-the-art methods isolate these directions in a high-precision subspace through transformations calibrated offline and folded into the weights, which fixes the subspace for all prompts, leaving each prompt's few unique directions unprotected, and rules it out wherever no weight can absorb the transformation. We present PLoQ, a prompt-adaptive low-rank decomposition that extracts the dominant activation components before quantization, quantizes them separately, and restores them within the layer's GEMM, without modifying the weights. The low-rank component's basis is estimated from each prompt during prefill and reused throughout decoding. At the same bit width as state-of-the-art mixed-precision quantization (4-bit weights, activations and K/V cache with an eighth of the channels at 8 bits, about 4.2 bits per activation on average), PLoQ outperforms it on all six Llama and Qwen models from 1B to 70B parameters, at up to 8k tokens (16k on two of them), recovering up to 46% of the perplexity that the state of the art still loses to 4-bit activations. On Llama-3.1-8B at 8k tokens it adds only 4% to prefill and 8% to decoding.

---


### 63. [Separating Automation Gains from Agent Contributions in AI-Assisted Model Validation](https://arxiv.org/abs/2611.27094)

**<font color=#1a73e8>作者：</font>** M. Ahmadi Achachlouei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents are being proposed for bank model validation, yet evaluations that compare agent-assisted work with manual practice credit the agent with gains that come from digitized evidence and deterministic tests. We propose a staged architecture in which an LLM-free controlled workflow (P1) is both the fallback and the control arm for individually authorized agent tasks (P2), and an attribution protocol that credits an agent only for faults P1 does not already report. The protocol charges decoy false alarms, unnecessary actions and endorsed developer assertions, counts invalid outputs as misses, folds newly automatable findings back into P1 with discovery credit, and fixes safety bounds and a break-even cost gate in advance. On a synthetic credit-scorecard harness, five scripted reference policies show why this matters: naive case accuracy (4/6) and pooled detection (3/5) tie four flawed policies, whereas the protocol separates all five and credits only the reference policy with detection beyond P1. One fold-back round raises a P1-parroting policy's naive scores without any change to the policy. A regression matrix of sixteen mutants covers nine ways in which earlier versions of the evaluation passed misleadingly. No LLM agent has been evaluated yet; we specify a falsifiable pilot.

---


### 64. [Reasoning in Two Dimensions: Quantifying Chain-of-Thought Faithfulness and Efficiency](https://arxiv.org/abs/2611.27100)

**<font color=#1a73e8>作者：</font>** Chenruo Liu, Quan Zhang, Qi Lei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning exposes intermediate steps, but a correct answer does not establish that an LLM relies on the dependence expressed by those steps or reasons efficiently. We operationalize CoT faithfulness and efficiency within a common framework. Specifically, we represent a CoT as a semantic reasoning graph and decompose the model's predictive dependence along two complementary axes: dependence explained by semantic support versus additional reasoning history, and dependence allocated to answer-reaching versus off-path reasoning. This decomposition yields global and step-level measures of unfaithfulness and inefficiency. Controlled interventions show that the proposed metrics respond to hidden dependence and induced off-path reasoning as intended. Across mathematical and multi-hop reasoning tasks, answer-level unfaithfulness is consistently associated with greater predictive uncertainty, whereas both unfaithfulness and inefficiency exhibit weak or inconsistent associations with answer correctness. We further derive theoretically grounded, graph-aware fine-tuning objectives that improve the targeted reasoning properties without directly optimizing the computationally expensive metrics or compromising answer accuracy. Results indicate that accuracy and brevity provide incomplete assessments of reasoning quality: reliable CoT evaluation should also consider whether the LLM's predictive dependence is faithfully represented and efficiently allocated.

---


### 65. [One state, many questions: Opsis gives a frontier model typed eyes for pathology](https://arxiv.org/abs/2611.27102)

**<font color=#1a73e8>作者：</font>** Zhixuan Ge, Wei Qiu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A synoptic pathology report is a checklist of questions with fixed answer sets, many composed from others. Pathology foundation models answer them accurately with one classifier trained with labels for each, and frontier language models, which compose freely, cannot fit a slide of fourteen thousand tiles in their context. On 189 breast report questions, frontier models that read a written description of the slide or look at a thumbnail and tiles of it answer at 0.50 to 0.66, below the majority class at 0.67. A description is written before the question is known, and a look covers a handful of tiles. We present Opsis, which lets the model ask instead: a typed question interface on a frozen pathology encoder. A slide is encoded once, a question names an operator, arguments and candidates given at runtime, and the answer is a probability over the candidates. We build it as a 10 M parameter decoder on frozen Virchow2 tokens (Opsis-S) and inside Qwen3-VL-8B (Opsis-V). Asking Opsis-S, four frontier models answer the breast questions at 0.78 to 0.79, and on 3,797 pan cancer questions asking is 8.6 points above reading. On 995 composite questions that Opsis-S was never trained on, a frontier model composing its answers reaches 0.76, against 0.69 when it looks at the slide and 0.78 for ABMIL trained on each composite. On a pan cancer question set over 10,712 TCGA slides, one Opsis-S decoder matches linear probes trained per question on TITAN and PRISM2 embeddings (average accuracy 0.69 against 0.70 and 0.68). Opsis-S also separates CAMELYON16 metastases without training on that cohort (AUROC 0.86) and localises necrosis from report labels alone (tile AUROC 0.93).

---


### 66. [Recurrent Amplification and Exact Nonexpansiveness Criteria for Query-Driven Erasure](https://arxiv.org/abs/2611.27109)

**<font color=#1a73e8>作者：</font>** Haozhe Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Query-derived Erase Direction (QED) augments a rank-one linear attention update with a key-orthogonal query component. Under scalar decay, this correction leaves the eigenvalues of each homogeneous state transition unchanged, while the propagation of an initial perturbation depends on the ordered product of these transitions. We construct a periodic token sequence with fixed key and query projections for which every one-step spectral radius is below one but the spectral radius of the period product exceeds one. The same construction yields a sufficient condition for mean-square growth under independent uniform token sampling. For rank-one erasure with channel-wise decay, we derive a necessary and sufficient spectral-norm test for one-step nonexpansiveness that can be evaluated in $O(d)$ time. The test agrees with direct singular value decomposition on all 1,800 operators evaluated. In a counterfactual replay of a selected head of Qwen3.5-0.8B-Base, the terminal gain on a 4,096-token repeated-text sequence increased from 0.99938 to 1.3977 with the feature and checkpoint gate trajectories held fixed.

---


### 67. [CoEvoBench: Can LLMs Drive Recursive Co-Evolution of Agentic Systems?](https://arxiv.org/abs/2611.27116)

**<font color=#1a73e8>作者：</font>** Chuan Xiao, Baojie Wang, Haizhao Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The performance of an LLM agent depends on both its model and its harness, the code that mediates its interaction with tools and environments. Can LLM researchers drive this co-evolution as a recursive improvement process, deciding round after round which component to change when each change alters the value of the other? Existing benchmarks evaluate post-training or data research with the harness out of scope, or harness optimization with the model fixed, leaving this joint decision unmeasured. We introduce CoEvoBench, a benchmark that evaluates LLMs as researchers co-evolving the model and harness of a target agent across five agentic domains. Researchers start from a common base model and initial harness, train and revise within a 24-hour budget, and submit a model-harness pair that is scored on separate test tasks. Across five frontier researchers, the strongest closes more than four fifths of the gap to an instruction-tuned reference system, and co-evolution succeeds on interaction tasks but rarely on long-horizon coding. These results suggest that current LLMs can make a strong first improvement, but cannot yet turn feedback from an improved system into the next one. CoEvoBench provides a controlled testbed for measuring the research capabilities that recursive co-evolution requires.

---


### 68. [When Students Fail to Learn from Teachers: Learning Dynamics of On-Policy Distillation](https://arxiv.org/abs/2611.27125)

**<font color=#1a73e8>作者：</font>** Xinnan Zhang, Zeyi Liao, Siliang Zeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has become a core technique for post-training large language models, enabling students to learn from dense token-level supervision on their own generations. However, even with a capable teacher, OPD training can be unstable, leading to excessive response length, repetitive generation, and severe performance degradation. One example is \textit{spurious agreement}, where the student maintains high overlap with the teacher at the states visited but produces repetitive generations. Although such failures have been observed, the mechanisms behind these failures remain poorly understood. To address this gap, we investigate OPD through the lens of learning dynamics, tracing three mechanisms from local analysis to subsequent on-policy sampling. We first identify states where sampled-token OPD updates fail to correct teacher--student mismatch and characterize them using the student's mass on the teacher's top-$p$ set. We then show that learning from the teacher is difficult at mismatched states and that their gradients can also affect with learning at other tokens. Finally, using a termination-token mismatch as a case study, we study how continued training on mismatched states influences on-policy sampling, suppressing the student's current modes and leading the student toward states where the teacher is unreliable . These findings help explain the benefits of supervised fine-tuning (SFT) initialization and motivate targeted correction of states where student and teacher are mismatched.

---


### 69. [Analyzing Multi-Layer Visual Representations of Large Vision-Language Models for Anomaly Detection](https://arxiv.org/abs/2611.27128)

**<font color=#1a73e8>作者：</font>** Satoshi Hashimoto, Hitoshi Nishimura, Mori Kurokawa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we analyze multi-layer visual representations in large vision-language models (LVLMs) and examine the effectiveness of layer-wise features and multi-layer fusion for anomaly detection. Representative LVLMs connect visual encoder features to a language model through a projector. In this design, deep visual encoder features carry high-level semantics and alignment with text representations, whereas shallow and intermediate layers retain information relevant to vision-centric tasks, such as local appearance and fine-grained shape. It is therefore important to choose layer representations and fusion methods according to the nature of the downstream task. Focusing on anomaly detection, we compare layer-wise features and multi-layer fusion across multiple supervision levels and a variety of classifiers, and examine from several perspectives how multi-layer visual representations affect downstream performance. By analyzing the resulting performance differences, we further discuss the contribution of each layer representation to anomaly detection and provide empirical insights into representation selection for vision-centric tasks.

---


### 70. [MAPES: Multi-Value Alignment Pipeline via Expert Specialization](https://arxiv.org/abs/2611.27133)

**<font color=#1a73e8>作者：</font>** SungHo Kim, SangKeun Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) with human preferences requires simultaneously satisfying multiple, often competing values. Existing preference optimization methods collapse these into a single implicit signal, and even multi-objective extensions optimize within a shared parameter space, leaving cross-value conflicts unresolved. We propose MAPES, a multi-value alignment paradigm in which conflict resolution is a first-class concern at every pipeline stage: it first decomposes supervision into value-specific experts trained in isolated parameter subspaces, then recomposes them via preference-aware value merging and a lightweight harmonization stage that aligns the merged model with the expert ensemble. Across five preference alignment benchmarks, MAPES outperforms strong direct preference optimization (DPO) variants and multi-objective baselines on the benchmark-level average, with no large degradation on GSM8K and GPQA; matched controls isolate the contribution of each stage.

---


### 71. [Crafting the Difference, Grounding the Evidence: Discriminative Concept Learning for Zero-Shot Skeleton Action Recognition](https://arxiv.org/abs/2611.27135)

**<font color=#1a73e8>作者：</font>** Siyu Zhu, Feng Ding, Zixiao Jin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LLM-generated descriptions enrich zero-shot skeleton-based action recognition but repeat cues shared by confusable actions. Their contextual semantics also lack explicit links to skeleton features. To address these challenges, we propose CRAFT, which couples Concept Refinement and Feature-grounded Tokens. Hard-negative-conditioned generation and contrastive scoring identify concepts that distinguish each action from its closest rivals. Unique-QDPP selects complementary descriptions within each semantic slot and prevents their reuse across slots. This bank supervises learnable concept tokens that read motion and context cues from each skeleton. On fixed NTU-60 and NTU-120 splits, CRAFT improves five baselines spanning four recognition paradigms. ZSL accuracy and GZSL harmonic mean increase on every baseline-split pair, by 5.4 and 5.9 percentage points on average. Random-split experiments extend these gains to three datasets, including PKU-MMD. Code will be released after acceptance.

---


### 72. [Double counting in LLM evidence fusion: exact posteriors separate rule compliance from posterior gain](https://arxiv.org/abs/2611.27138)

**<font color=#1a73e8>作者：</font>** Tengfei Shao, Asma Rezaei, Ali Reza Kamali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models fuse reports in retrieval, multi-agent consensus and agent memory, where treating shared-source reports as independent can double count evidence. A common remedy is an instruction to count each source once. Its value depends on the receiver's raw baseline. Pricing it needs an exact reference. We build the graded-dependence exact reference: binary worlds with single-report reliability 0.65 and four dependence levels, whose disclosed parameters give every world an exact posterior and every rule a target risk. The paired gain protocol scores raw and instructed answers of four configurations on 2,976 worlds. Agreement and gain separate in both directions. At $\delta$ = 0, claude-opus-5-5 and gpt-6.1-sol agreed with the rule within 0.001 in 744 of 744, and the instruction raised their posterior mismatch by 0.044; gpt-6-luna agreed in 165 of 744 and gained 0.0140 (95% interval 0.0064 to 0.0219); claude-haiku-5-5's gain moved from -0.0295 ($\delta$ = 0) to +0.0302 ($\delta$ = 1) (descriptive). The prespecified first-child endpoint contrast, gain at $\delta$ = 1 minus $\delta$ = 0, was 0.0342 (0.0303 to 0.0382). In the preregistered tests, the raw source-weight contrast was positive (0.259, 95% interval 0.182 to 0.337; Holm rejected zero) and the grouping endpoint difference was not detected (0.0004, -0.0023 to 0.0031). This interval excludes differences larger than 0.0031 in magnitude and lies within the registered precision bound of $\pm$0.0046. The reference prices the rule before any model call. The paired gain, estimable as a Brier difference on labelled deployment items, decides adoption per receiver and prompt condition.

---


### 73. [Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use Subordinate Material](https://arxiv.org/abs/2611.27139)

**<font color=#1a73e8>作者：</font>** Jinxiang Xie, Xinyi Zhang, Changjiang Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems increasingly divide long tasks among subagents whose reports a senior agent turns into the final answer. Such a division of labor pays off only if each agent, and above all the senior agent, carries out the duties of its role. Current evaluations, however, mostly score the final answer, and a fluent, well-cited answer cannot show whether the senior agent weighed its subagents' reports or merely aggregated them. To assess whether a senior agent meets its assigned responsibilities, we define role integrity as the preservation of an agent's functional responsibilities when it acts on its subordinates' material. To measure it, we introduce RI-Bench, a behavioral benchmark grounded in the structures and public records of three institutional hierarchies: peer review, appellate adjudication, and parliamentary inquiry. We choose these hierarchies because their rules explicitly assign the senior role a duty toward subordinate material, and together they cover three basic duties: to weigh, to verify, and to relay. Rather than scoring output correctness, we measure how senior agents' outputs respond to controlled changes in subordinate material, using rule-based checks and a rubric-guided LLM judge calibrated against human annotation. Across eight LLMs and over 12,000 agentic episodes, senior agents rarely adopt a planted procedural error (2.9% of rulings) but often follow a majority of generic reviews (up to 71% of decisions) or drop witnesses' stated limitations (up to 65% of cited claims). Obligation prompts reduce these failures without removing them, and they also shift behavior in the control conditions. These findings motivate direct, obligation-specific evaluation of role integrity rather than inferring it from general capability or explicit role instructions. Code and data are available at this https URL.

---


### 74. [The Vulnerability Window: Decision Instability in Quantized Reward Models](https://arxiv.org/abs/2611.27155)

**<font color=#1a73e8>作者：</font>** Omkar Shewale, Deepak Kumar, Divakar Kumar Yadav  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward models and LLM judges are routinely quantized to 4 bits so that scoring many candidates stays affordable, and the usual check is that benchmark accuracy barely moves. That check is close to blind. Across eight reward models from two families (0.6B-8B), three generative judges and four 4-bit quantizers, quantization rewrites 1.1-12.3% of pairwise preference decisions on RewardBench while aggregate accuracy moves by as little as 0.03 points (p = 1.00), because the errors it fixes and introduces cancel. Flips concentrate where the full-precision margin is small relative to the quantization noise scale sigma: a Gaussian approximation Phi(-|m|/sigma) describes the aggregate rate, over-predicting it in all 30 scalar settings and failing for generative judges, and occupancy of the resulting vulnerability window falls from 25% to 7% with model size, which is what makes small judges fragile. The churn stays within noise under benign best-of-16 and becomes clear under adversarial pressure for some quantizers (146:54 harmful:helpful flips on one family, reversing sign on another). Downstream it changes what ships: across six (model, quantizer) pairs from two families, 14.6-65.7% of problems get a different best-of-64 selection while only 2.6-9.6% get a different final answer, with selections changing 5-8x more often than answers in every pair, and the pair the benchmark calls identical (0.03 points, p = 1.00) still changes 34.5% of them. Benchmark churn ranks that downstream change (rho = 0.89); benchmark accuracy does not order it reliably. Held-out audits then locate the useful diagnostic in the margin rather than the Gaussian: every margin-based predictor orders flips identically (AUC 0.927), and on the level a directly measured churn rate wins in-distribution. As a routing signal it is matched by plain top-k. The contribution is the characterization, not the model.

---


### 75. [From Acting to Learning: Experience Selection toward Continually Learning Agents](https://arxiv.org/abs/2611.27159)

**<font color=#1a73e8>作者：</font>** Yaoyuan Yan, Haoxiang Jie, Zhiyou Heng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Successful agent interactions provide training data, but success alone does not determine which records a student should learn from. We examine experience selection for a 4B language agent as a component of continual agent learning. Nine selectors are compared across two fixed experience pools, eight initialization seeds, and two sampling seeds, yielding 288 trained students. Each student is evaluated on 128 development task groups with a common executor. With equal global selection freedom, 256 distinct contents, and 768 training presentations, optimizer-aware gradient selection reaches 81.45\% and 73.19\% success in the two pools. Its gains over global random selection are 8.25 and 5.96 percentage points; gains over global high-NLL selection are 4.10 and 4.05 points. All eight initialization-level contrasts are positive against both baselines in each pool. Relaxing coverage constraints improves gradient selection but reduces random-selection performance, showing that the ranking rule and selection space must be considered together. A separately frozen replication on 128 reserved task groups is complete; its equal-source gradient-minus-random and gradient-minus-high-NLL differences are +7.03 and +5.03 points, respectively.

---


### 76. ["More Than You Expect!": Leakage-Abuse Attacks on Encrypted Vector Search](https://arxiv.org/abs/2611.27174)

**<font color=#1a73e8>作者：</font>** Yang Zhang, Ruiqi He, Xiaoqian Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vector databases support semantic search and retrieval-augmented generation, but embeddings, queries, and record labels may contain sensitive information. Although encrypted vector search protects these contents, some schemes expose records retrieved together across queries. We identify semantic neighborhood leakage, whereby co-retrieval relationships derived from access patterns reveal semantic categories of encrypted records and queries. We present SAGE (Semantic Access-pattern Graph Exploitation), a passive, persistent leakage-abuse attack that infers record labels and query categories from access patterns. SAGE builds a weighted co-retrieval graph and offers two variants requiring different auxiliary knowledge. SAGE-Dist matches anonymous spectral groups to semantic categories using estimated class proportions and refines labels via optimal transport, without known record labels. SAGE-Known combines graph-based label propagation with spectral-group anchor voting using a small set of known labels. We evaluate SAGE on four text and image datasets. With 1% known record labels, SAGE-Known achieves up to 84.3% mean record-label accuracy and outperforms the strongest corresponding baselines on all four datasets. With only estimated class proportions, SAGE-Dist achieves 66.9% record-label accuracy and 68.1% query-category accuracy on AG News, exceeding the strongest corresponding baselines by 21.8 and 41.9 percentage points, respectively, though performance varies across datasets. Experiments with a real-world DCPE implementation (Fuchsbauer et al., SCN'22) show that semantic leakage persists under encrypted approximate retrieval. These findings expose privacy risks even when vector contents remain protected.

---


### 77. [Felid: A Flexible and Efficient Design for Transformer Fine-Tuning over Encrypted Data](https://arxiv.org/abs/2611.27175)

**<font color=#1a73e8>作者：</font>** Linru Zhang, Jun Jie Sim, Xiangning Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully Homomorphic Encryption (FHE) enables non-interactive, privacy-preserving transformer fine-tuning, protecting highly sensitive data as inputs to large language models. Prior work has predominantly pursued efficiency gains through architectural refinements, yet overall performance remains bounded by the substantial cost inherent in encrypted computation. To address these issues, we target the bottleneck at the ciphertext operation level. Concretely, we propose a novel packing strategy that supports batching over a flexible number of inputs, making it well-suited for fine-tuning workloads. In addition, we design operation-specific matrix evaluation algorithms that significantly reduce (i) the number of ciphertext rotations and relinearizations, and (ii) the number of bootstrapping invocations. Additionally, we exploit functional bootstrapping to fold the evaluation of element-wise activation functions directly into the bootstrapping step, thereby reducing overall computational complexity. As a result, our framework achieves a $30\times$ reduction in ciphertext rotations and relinearizations across all matrix operations, as well as a $2.5\times$ reduction in FHE bootstrapping invocations over the entire computation flow, compared to the latest state-of-the-art work. It is worth noting that our system completes fine-tuning of a 2-layer BERT-style model with a batch size of 16 in 650 seconds, achieving a $8\times$ speedup over the state-of-the-art work.

---


### 78. [Learning Adaptive Defense Strategies: Fine-Tuned LLMs for Network Security Games under Network Mobility](https://arxiv.org/abs/2611.27180)

**<font color=#1a73e8>作者：</font>** Md Abu Sayed, Asif Rahman, Ahmed Ryen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models(LLM) show promise for strategic reasoning, yet their ability to compute game-theoretic equilibria under dynamic conditions remains largely unexplored. This work investigates whether fine-tuned LLMs can serve as solver-free surrogates for online equilibrium computation in honeypot allocation, a setting in which network mobility continuously reshapes the underlying attack graph and forces repeated re-solving of a two-player zero-sum game. We construct a dataset of 270 security games on networks of 8--25 nodes with solver-grounded equilibrium labels, and evaluate four classes of predictor over 1{,}524 held-out mobility events: non-learned baselines, six open-weight architectures evaluated zero-shot, the same six after LoRA fine-tuning, and four proprietary models as an external reference point. Predictions are scored without post-hoc repair against exact game-theoretic criteria: exploitability against an optimal attacker best-response, equilibrium support accuracy, and distributional distance. Fine-tuning reduces exploitability across every architecture, and fine-tuned open-weight models of modest size outperform every zero-shot predictor, including proprietary ones; no zero-shot model at any tier reaches the floor set by uniform allocation. Stratifying by mobility type exposes a qualitative shift that aggregate metrics conceal: zero-shot models do not condition on whether a departing node lies on an attack path, while fine-tuned models recover this distinction. We further find that validation loss is negatively rank-correlated with task performance, and that output validity, rather than predictive accuracy, is the binding constraint on further progress.

---


### 79. [What Does Matching a Human Intervention Effect Establish? Benchmark Checks for LLM Simulations](https://arxiv.org/abs/2611.27186)

**<font color=#1a73e8>作者：</font>** Tengfei Shao, Asma Rezaei, Ali Reza Kamali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM simulations are validated by equivalence with human effects, yet a zero reference passes whenever the human 90 percent interval lies inside the margin, as the human benchmark shows before simulation. When the zero reference fails, planned precision gives independent simulations the margin up to which passing is a 5 percent test of response. In an exploratory 70-experiment reanalysis, 72 percent of GPT-4's $\pm$0.20 SD passes were zero-reference passes; GPT-4 passed 16 contrasts the zero reference failed (1.58 expected without response). In a preregistered audit, Claude Sonnet 5.5 passed three intention targets, all zero-reference passes, and the registered belief-gradient control; norm beliefs changed 0.065 SD against humans' 0.351 (zero-reference check added after unblinding; norm beliefs emphasized after inspection). Registered tests detected no overestimation; average-effect intervals excluded overestimation above 0.08 SD. A group audit's precision floor is 1.33 facts against a 2.9-fact effect. Report the zero-reference threshold beside every equivalence decision.

---


### 80. [SCAP: Stochastic Context for Action Expert Pretraining](https://arxiv.org/abs/2611.27187)

**<font color=#1a73e8>作者：</font>** Xiao Lin, Yaoxu Lyu, Ronghao Dang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-modality action-expert pretraining controls competition from visual shortcuts before vision--language--action (VLA) adaptation. Yet single-modality pretraining can impair the vision--language interactions needed for subsequent joint prediction. We construct a diagnostic model in which VA or LA pretraining can disable an initially active pathway for joint vision--language modeling. In this model, subsequent training with complete visual and language inputs cannot restore the pathway, even with unlimited adaptation. We therefore introduce Stochastic Context for Action Expert Pretraining (SCAP), a new action-expert pretraining stage that precedes full-input training. During this stage, visual and text tokens are randomly masked before entering the VLM. In this unified diagnostic model, SCAP can preserve the joint vision--language modeling pathway during pretraining and subsequent full-input training. Compared with direct full-input training, it can also reduce reliance on visual shortcuts and increase reliance on language instructions. SCAP consistently improves performance across four different VLA architectures. In real-robot experiments, it achieves 76.67% average success across three instruction-conditioned manipulation tasks, outperforming full-input pretraining by 25 percentage points.

---


### 81. [EDAGoat: An EDA-Aware Agent for Project-Level GPU Optimization](https://arxiv.org/abs/2611.27196)

**<font color=#1a73e8>作者：</font>** Chengxi Li, Liang Xiao, Yutao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GPU acceleration has transformed electronic design automation (EDA), yet further improving expert-engineered GPU tools still demands substantial manual effort. Automating this work calls for coding agents that can trace bottlenecks across host and device code while preserving correctness and design quality. We introduce EDAGoat, to our knowledge the first EDA-aware GPU optimization agent for this task. Its optimization enhancement (OE) mode guides edits with four cross-project GPU optimization patterns. Its mandatory validation (MV) mode requires the agent to test the edited program against the EDA constraints its changes could affect. Our benchmark covers five GPU EDA projects across four task families and 55 circuit inputs, measuring complete-solve runtime and verifying the resulting designs. Each configuration runs three independent searches per project. A search qualifies only if its solver passes correctness and design-quality checks on all public and hidden inputs. With DeepSeek, generic prompting qualifies in 7 of 15 searches and OE in 6 of 15, despite a higher best speedup on four projects. Adding MV raises this to 13 of 15 and, on every project, exceeds both generic baselines in mean and best speedup and OE in mean speedup; the geometric mean of per-project mean speedups rises from 1.11x (1.36x with OE) to 1.53x. With GPT-6 Astra, EDAGoat qualifies in all 15 searches and improves both speedup metrics over generic prompting on every project, lifting the same geometric mean from 1.26x to 1.57x. These results show that agents can use EDA knowledge to find further speedups in expert-tuned tools while preserving design correctness and quality, establishing EDA-aware GPU optimization as a new direction for agent research.

---


### 82. [Improved Accuracy Scaling with Problem Complexity in LLM Arithmetic Reasoning Using Executable Symbolic Representations](https://arxiv.org/abs/2611.27203)

**<font color=#1a73e8>作者：</font>** Yu-Bin Liu, Shi-Ju Ran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High accuracy on mathematical benchmarks does not establish whether reasoning remains reliable as problem complexity increases. We examine how executable symbolic representations change accuracy scaling in large language models compared with natural-language reasoning. To address this limitation, we introduce the GSM Arithmetic Benchmark (GSM-AB), a controlled benchmark that independently varies operand digit length and operation count to probe numerical scale and compositional complexity. We find that executable representations can improve accuracy and slow its decline as complexity increases. Lean reduces average sensitivity to operand digit length at every tested model size. By contrast, slower degradation with increasing operation count emerges at the larger model sizes. A Python program-of-thought (Python-PoT) control shows a similar operation-axis pattern, suggesting that this finding is not specific to Lean. These findings show that reasoning representation shapes arithmetic accuracy scaling and support executable symbolic representations for more reliable reasoning on complex arithmetic tasks.

---


### 83. [Parameter-Efficient Adaptation of Qwen3-VL for Handwritten Mathematical Expression Recognition](https://arxiv.org/abs/2611.27208)

**<font color=#1a73e8>作者：</font>** Manh Tuan Ha, Xuan Bao Viet Tran, Vo Minh Dat Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handwritten mathematical expression recognition (HMER) requires joint recovery of symbol identity and two-dimensional syntax, so a locally plausible transcription may still be structurally wrong. We study whether a compact vision-language model can be adapted to generate linearized Symbol Label Graphs (SLGs) under limited computing resources. Starting from a 4-bit Qwen3-VL-4B checkpoint, we apply rank-16 Low-Rank Adaptation to the vision, language, attention, and MLP modules and train with instruction-formatted CROHME 2019 examples. We compare this model with an internally implemented ViT-Transformer baseline, a zero-shot Qwen3-VL configuration, and additional internally evaluated alternatives. On the 1,198 valid CROHME test examples, the CROHME-only model obtains 524 exact matches (43.74%) and a corpus BLEU-4 score of 77.67, compared with 4.92% and 43.26 for the task-specific ViT baseline. An ablation that adds 2,000 manually written, formula-guided samples decreases exact match to 42.32%, exposing a domain-alignment issue rather than an automatic benefit from more data. The principal contribution is therefore an evidence-backed, resource-efficient formulation of HMER as multimodal structural generation, together with a controlled data-composition ablation and an analysis of the remaining gap between local token overlap and globally correct structure.

---


### 84. [Explicit Style Extraction for Personalized Long-Form Text Generation](https://arxiv.org/abs/2611.27211)

**<font color=#1a73e8>作者：</font>** Jenitha Reddy Patel, Sameeksha Kini, Amulya Rayasam 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized long-form generation asks a language model to write new text the way a specific user would. The standard recipe, retrieval-augmented generation, places a few of the user's past texts in the prompt but leaves the model to decide what to take from them. We introduce StylePrism, a taxonomy of 28 stylistic aspects in seven categories, and SP-Refine, an inference-time method that makes style extraction an explicit step: the model first fills StylePrism with the user's patterns, quoted evidence, and habits to avoid, then drafts from the user's samples and revises the draft twice against this profile, guided by its own style scores. On the three long-form tasks of LongLaMP with three LLMs, SP-Refine outperforms LongLaMP's retrieval-augmented baseline in 25 of 27 ROUGE and METEOR comparisons, by 10.2% on average and by up to 35.8%. Annotating users' own texts with the extracted profiles shows that StylePrism captures concrete, checkable habits, from the order of rhetorical moves to a reviewer's sign-off. Ablations show that the profile helps as revision guidance, not as a replacement for the samples: writing from the profile alone is worse in all 27 comparisons, while a single implicit-inference call is a cheaper alternative that comes close. Oracle variants that let the reviser see the reference, together with reference-free controls, show that larger refinement gains require information unavailable at inference time.

---


### 85. [Correct Precedents Induce Policy Violations in On-Device LLM Agents](https://arxiv.org/abs/2611.27216)

**<font color=#1a73e8>作者：</font>** Chong Tian, Yu Wang, Steve Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Local-cloud agent systems pair a cloud model with a small on-device agent that acts on private data, often as the last check before an irreversible action. We identify, for the first time, a failure in which such an agent is led into a violation by its own correct decisions within a session. After it correctly releases an item whose restriction was lifted, it becomes more likely to release the next item that is still restricted. Because the trigger is a correct decision, a history with no faulty step can still end in a violation. We call this failure correct-precedent generalization and find it in 13 open-weight models from nine developers. A single correct precedent can cut the safe rate of the most affected agent roughly in half, and the risk compounds when a refused request is simply sent again in a new session. Interventions on the agent's history indicate that it carries its decision on the released item over to the restricted one instead of checking that item's status. Building on this finding, we propose Paired Decision Distillation (PDD), which distills the decisions of a weakly affected teacher into a LoRA adapter. PDD restores the safe rate to nearly 100% in every distilled model, without extra prompt text or model calls.

---


### 86. [CoPyro: Feeding Copy Proposals to Parallel Drafters](https://arxiv.org/abs/2611.27217)

**<font color=#1a73e8>作者：</font>** Hong-Kai Zheng, Piji Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates language generation by letting a target model verify several draft tokens in one forward pass. Earlier neural drafters such as EAGLE extend each candidate sequence one token at a time. Recent work has turned to parallel drafters such as DFlash, which predict a whole block at once. Another approach uses n-gram retrieval to find an earlier occurrence of the current context suffix and copy the tokens that followed it directly into the draft. We introduce CoPyro, which feeds these copied tokens into a parallel drafter in place of masks. The drafter learns from context which tokens to keep and which to revise as it predicts the block in its usual forward pass. Across eight benchmarks on Qwen3-4B, CoPyro improves overall acceptance length for all four parallel drafters tested, with gains of 2.19-5.08% when trained on 100K samples. With DFlash trained on 710K samples, overall gains range from 1.08% to 2.00% across the tested model sizes and temperatures. Code generation benefits most in both settings. On Qwen3-8B, processing the proposals adds an average of 0.24 ms per decoding round in Transformers.

---


### 87. [Bel: Step-Level Policy Improvement of Visual Agents Without Training](https://arxiv.org/abs/2611.27222)

**<font color=#1a73e8>作者：</font>** Jiajun Fan, Ziwen Wang, Zhaoyu Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A visual agent acts on what it sees: it taps and types on a screen, or points on a camera image to show a robot where to act. One wrong step can fail its task, yet the right action is often among its own samples, passed over by its greedy decode. Choosing it is a visual judgment, since an action is best judged where it acts, not by its text or coordinates alone: as text, a tap is two numbers; drawn on the screen, it is the Post button of an empty draft. We find that this is decisive: given the screenshot and a tap's coordinates, a decision model chooses among GUI-R1-3B's samples significantly worse on average than when the tap is drawn where it lands. Bel turns this finding into a method that trains nothing and needs only a frozen policy's samples and an image on which each action can be drawn. It marks each candidate on its own copy of the image it acts on, asks a decision model for the probability that executing it is the right decision, so that every kind of action shares one scale, and acts on another candidate only when greedy scores below a threshold and trails it by a margin. On recorded GUI steps, for each of three policies, Bel significantly beats greedy decoding on mobile, web and desktop screens alike and, on the same candidates, gives each a significantly higher mean step success than voting, CATTS, the trained GUI-Critic-R1 and two prompted Qwen3-VL judges shown the same marks; it also significantly improves the much larger Qwen3-VL-235B-A22B on every step-level test set. With GUI-R1-3B's thresholds unchanged, Bel significantly raises live AndroidWorld and MiniWoB++ task success for two other policies and robot-pointing success for three policies on each of two groups of benchmarks. Judging each action where it acts thus gives step-level policy improvement of visual agents without training, with significant gains for GUI agents and robot pointing.

---


### 88. [CreditFilter: Calibrated Token Weights over the Within-Response Entropy Rank for RLVR](https://arxiv.org/abs/2611.27227)

**<font color=#1a73e8>作者：</font>** Hanqing Zhao, Liuyue Xie, Rong-Cheng Tu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Critic-free reinforcement learning with verifiable rewards (RLVR) typically assigns a uniform advantage to every token. Token-reweighting heuristics like the 80/20 mask favor high-entropy tokens, but fail to measure a token's actual impact on the outcome. We formalize this impact as the forking value: the variance of the success probability over the policy's next-token choices. The expected forking values along a response sum exactly to the reward variance. Token credit is thus, in expectation over a prompt's responses, a fixed budget spent at the forks. This motivates weights that redistribute credit within a response. The forking value factorizes into a fork consequence, which requires costly continuations to estimate, and a fork probability, which the softmax provides. On Qwen3-8B-Base, this fork probability decays exponentially with a token's within-response entropy rank at class-specific rates, revealing that most tokens carry negligible forking value. CreditFilter weights each token by an exponential window over the same rank. The window is calibrated to this fork-probability envelope, under an approximately flat fork consequence. CreditFilter needs no extra forward passes and is stabilized by difficulty damping and an entropy-gated fallback. Averaged over three seeds, it outperforms DAPO by 7.7 points on MATH500 and by 10.5 and 9.1 points on AIME24 and AIME25. Its dynamically adaptive variant matches it. The ablations show that both parts matter: ranking tokens within each response rather than across the batch, and matching the window's decay rate to the envelope. Code is available at this https URL.

---


### 89. [LongCat Recall Sparse Attention: Co-Designing Key Organization and Retrieval for Long-Context Inference](https://arxiv.org/abs/2611.27233)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Bin Xiao, Kefeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-based sparse attention, exemplified by DeepSeek Sparse Attention (DSA), reduces attention computation by selecting a small subset of key-value entries. However, selecting these entries can still require searching the entire visible history. For long sequences, retrieval becomes a major bottleneck, limiting the efficiency gains from sparse attention. To address this problem, we propose LongCat Recall Sparse Attention (LRSA), which combines fine-grained representatives with paged retrieval in an incrementally maintained index. LRSA partitions the sequence into time buckets that can be indexed independently as new keys arrive, without regrouping existing history. Within each bucket, it organizes indexing keys into capacity-balanced directional groups and packs a fixed number of complete groups into each page, retaining a separate center for every group. These centers provide fine-grained representatives for page selection, after which refinement scores members of the selected pages together with sink, sliding-window, and visible unindexed candidates to select the final Top-$K$ logical positions. To execute this retrieval process efficiently, we store members in reordered pages, fuse construction stages according to group size, and share storage for overlapping fixed candidates across queries during chunked prefill. These choices support regular member access while reducing kernel launches during construction and repeated candidate transfers. Moreover, we integrate LRSA into SGLang to maintain the index during inference, overlapping asynchronous index construction for new buckets with subsequent computation and reusing compatible bucket indices and member pages after a prefix match in the original key-value pool. With a 1024K-token context, LRSA accelerates key selection by 4.70$\times$ over DSA and combined selection and attention by 35.60$\times$ over full attention.

---


### 90. [WINSO: A Large-Size Very-High-Resolution Remote Sensing Dataset for Wind Turbine Detection and Solar Panel Segmentation](https://arxiv.org/abs/2611.27241)

**<font color=#1a73e8>作者：</font>** Di Wang, Ke Li, Zhaokun Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wind and solar energy are central to the global transition toward net-zero emissions and sustainable development. Accurate spatial inventories of wind and solar facilities are essential for future energy planning. Satellite remote sensing provides a practical and efficient means to acquire such geospatial data at scale. However, reliable facility mapping from large-size satellite images remains constrained by the scarcity of carefully annotated datasets and the lack of systematic evaluation protocols. To address these limitations, we introduce \textbf{WINSO}, a large-scale wind and solar benchmark based on very-high-resolution (VHR) satellite imagery with ground sampling distances (GSDs) of 0.5--0.7\,m. WINSO comprises 10,962 large-size images sampled from diverse geographic locations across the Asia-Pacific region, covering at least 71,600\,$\text{km}^2$ and totaling 286.36 gigapixels, with individual image dimensions reaching 44,032$\times$62,208 pixels. Through manual annotation and expert verification, a total of 166,473 instances are labeled using horizontal bounding boxes (HBBs) for wind turbines and polygon masks for solar panels. To build baselines for clean-energy facility mapping, we evaluate state-of-the-art detection and segmentation models, specialized ultra-high-resolution (UHR) architectures, and vision-language models across different inference strategies. Furthermore, cross-dataset evaluations on two external public datasets illustrate the strong generalization capability of the WINSO. WINSO establishes a standardized benchmark to advance automated clean-energy mapping, paving the way for wide-area monitoring of the clean-energy transition.

---


### 91. [More Bits Won't Fix It: Diagnosing and Treating an Ill-Conditioned Backward Pass (A Case Study on Gemma-4)](https://arxiv.org/abs/2611.27243)

**<font color=#1a73e8>作者：</font>** Jeong Hyun Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> During LoRA fine-tuning of Gemma-4 (12B and 31B) on long prompts, whether they contain CT images, natural photos, or about 2,000 tokens of text, bf16 and fp32 gradients agree in the upper third of the language model (cosine similarity 0.96 or above) but are nearly orthogonal in the lower third. On image prompts, we trace the effect to an ill-conditioned backward path. The fp32 gradient is unchanged by element-wise relative noise of $10^{-6}$ on hidden states, confirming that fp32 is a valid reference. At $10^{-4}$, however, its cosine similarity with the noise-free gradient falls below 0.9 in 7 of 10 measurements, whereas bf16 forward states differ from fp32 states by about 1% per token. State swaps and backward-only interventions localize this sensitivity in Gemma-4-12B to the MLPs of layers 19-21 at image-token positions, where the gradient can be dominated by a single low-information patch. Detaching that path in the backward pass (while leaving the forward pass unchanged) keeps the gradient stable at $10^{-4}$ (cosine similarity 0.97 or above across all five measurements), lowers the median pre-clipping gradient norm from 8.5 to 0.63, and improves validation loss on a CT lesion-grounding task from 0.336 $\pm$ 0.019 to 0.296 $\pm$ 0.003 (four seeds; every modified run beats every baseline run). The gain disappears when the lower layers are frozen, and an fp32 run still exhibits gradient spikes (maximum norm 39,862) and fails to match this improvement. These training results cover one task and one model.

---


### 92. [EAGLE: Entity-Aware Grounding with Layered Evidence for High-Resolution Image Understanding](https://arxiv.org/abs/2611.27264)

**<font color=#1a73e8>作者：</font>** Zhongjian Zou, Quan Qian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) still struggle with fine-grained understanding of high-resolution images: attention heads vary in their reliability for grounding target entities and their attributes, while localized details are often disconnected from the broader scene context. We propose EAGLE (Entity-Aware Grounding with Layered Evidence for High-Resolution Image Understanding), a plug-in framework that jointly selects grounding signals and organizes hierarchical visual evidence. EAGLE employs a fine-grained dataset to screen visually-grounded attention heads, followed by entity-aware grounding to extract target-specific regions. It then integrates hierarchical evidence construction and question-guided routing to select optimal view combinations, feeding them into the frozen MLLM to enhance fine-grained visual understanding. Experiments with Qwen2.5-VL-7B and InternVL3-8B demonstrate that EAGLE consistently improves performance across both backbones and achieves SOTA results on V*, HRBench-4K, and HRBench-8K compared with existing methods using the same backbone.

---


### 93. [PP-CFG: Polarity-Preserving Guidance for Controllable Few-Step Image and Video Generation](https://arxiv.org/abs/2611.27266)

**<font color=#1a73e8>作者：</font>** Junyi He, Xu Peng, Chengming Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step diffusion distillation reduces sampling cost but often weakens adjustable classifier-free guidance (CFG) and runtime negative prompting. We introduce PP-CFG, an architecture that keeps positive and negative text conditions separate and combines their attention responses with opposite signs within a shared visual backbone. Its Scale-Time Polarity Mixer refines each condition using the guidance scale and denoising timestep, allowing prompt influence to vary throughout generation. The student retains a continuous scale input and selectable negative prompts with one visual backbone pass per step. We evaluate PP-CFG on Wan2.1 for video generation with distribution matching distillation (DMD), and on Qwen-Image with both latent consistency model (LCM) distillation and DMD. PP-CFG achieves 81.46 VBench in four steps and lower video teacher-student distances across guidance scales than step-distilled DMD. On NegElement-1K, our benchmark of 1,000 matched image and video prompt cases, it achieves higher target-removal rates than the corresponding teachers. These experiments support the method's generality across attention architectures, generation modalities, and distillation objectives while retaining competitive generation quality.

---


### 94. [Budgeted Safety Verification for Streaming Video Generation](https://arxiv.org/abs/2611.27268)

**<font color=#1a73e8>作者：</font>** Yuxin Cao, Ziqi Ding, Jiayu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A streamed video generator releases each chunk the moment that it is produced, so a safety decision that waits for the finished clip arrives after the harm has been seen. We measure a guardrail by exposure, the harmful frames a viewer is shown, and ask where a fixed moderation budget should be spent. The accurate detector reads decoded frames with a video language model and is too expensive for every chunk, so our guard reads hidden states the generator has computed already and spends a cheap score on deciding when to call it. On 599 streams from a distilled causal generator the undefended model shows 46.25 harmful frames of 81. The video model on every chunk leaves 0.91 frames at 80.1 scored per benign stream, and the same model triggered by our guard leaves 2.35 at 5.3. Spending that budget at random leaves 37.20 frames, so the gain is in the ordering, and a frame detector in the same role gives up almost six, so the judging stage must read the chunk as a clip. The ordering is worth more as the stream lengthens, and the guard carries to a second system. An independent guardrail model agrees with our oracle at $\kappa=0.74$, and a blinded audit by 50 participants puts its precision at 96.1% and recall at 82.8%. Warning. This paper contains examples of generated content that some readers may find disturbing or offensive in nature.

---


### 95. [Suspected Until Inspected: Neuro-Symbolic Detection of Broken Access Control in Server-Side Web Applications](https://arxiv.org/abs/2611.27270)

**<font color=#1a73e8>作者：</font>** Chengyao Yang, Zifeng Kang, Dongqi Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Broken access control (BAC) has topped the OWASP Top 10 since 2021. Unfortunately, a decade of detectors still leaves a gap on every front. Static analyzers are tied to one language or framework, dynamic testers cover only the endpoints they manage to exercise, and LLM-based auditors leave the final verdict to an error-prone model. In this paper, we design and implement FLINT, a neuro-symbolic framework that detects BAC in server-side web applications without language- or framework-specific rules. Our key insight is to separate the proposal from the verdict -- an LLM may flag any data access as needing a guard, but only a symbolically verified check can clear it. The neural component enumerates every endpoint and distills each, via demand-driven code slicing, into an authorization certificate whose claims are all grounded in cited code. The symbolic component verifies each claimed check through origin tracing and a lattice-based interprocedural dataflow analysis, so that no access is cleared on the model's word. When applied to popular real-world open-source applications, including Gitea, Grafana, and Strapi, FLINT detected 112 zero-day, exploitable BAC vulnerabilities, 30 of them in projects with over 20,000 GitHub stars. We have responsibly disclosed all of them to the developers. Mattermost, for example, has already confirmed our report and is assigning a CVE identifier.

---


### 96. [Do Companies Deliver on Their IPO Claims?](https://arxiv.org/abs/2611.27273)

**<font color=#1a73e8>作者：</font>** Vidhyakshaya Kannan, Shiv Banafar, Michael Galarnyk 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Initial public offering (IPO) filings describe what a company does and what it intends to become. Yet whether individual forward-looking claims are subsequently realized is difficult to assess. We introduce Vision Follow-Through (VFT), a benchmark and agentic pipeline that separates claim extraction, category assignment, verifiability, and evidence-grounded follow-through assessment. \vftclaims{} contains 5,066 human-annotated claim spans from 50 IPO filings, while \vftverify{} adds verifiability tiers, follow-through outcomes, and cited later evidence for 1,000 claims. Across language models, classifying human-annotated claims is substantially easier than extracting claims from full filings. Extraction coverage also varies sharply by category, with Organizational/Culture claims recovered far less often than Market Opportunity claims. Follow-through assessment poses a separate challenge: model judgments diverge from human assessments in different ways rather than exhibiting a single consistent bias. These results show that reliable assessment of corporate follow-through requires both finding the relevant claims and grounding subsequent judgments in later evidence.

---


### 97. [SIR-Agent: Skill-Augmented Image Restoration Agent with Recursive Self-Improvement](https://arxiv.org/abs/2611.27285)

**<font color=#1a73e8>作者：</font>** Yijian Wang, Qingsen Yan, Weiyu Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agents for Image Restoration (IR) aim to leverage Multimodal Large Language Models (MLLMs) to autonomously perceive image degradation and invoke IR tools. However, existing IR agents typically rely on fine-tuning MLLM parameters to adapt to new IR tasks, leading to catastrophic forgetting of IR knowledge. To address this limitation, we propose a skill-augmented IR agent, dubbed SIR-Agent, that maintains IR knowledge in a scalable skill library and uses Recursive Self-Improvement (RSI) to facilitate efficient skill-library evolution. Specifically, we design a Chain Feedback-driven Skill Revision (CFSR) to evolve the skill library. The CFSR analyzes restoration chains to identify and revise weak operations in existing skills. The compatibility of a revised skill with known tasks decides if it replaces the original skill or is appended independently. Furthermore, to advance CFSR's skill-library evolution, we present an RSI-driven skill meta-learning mechanism, which identifies CFSR's inefficient operations and autonomously refines its revision strategy. Extensive experiments across 14 IR benchmarks, covering 6 single-degradation and 8 mixed-degradation scenarios, demonstrate SIR-Agent's superior IR performance. Further evaluation on 7 unseen tasks validates SIR-Agent's generalization to new IR tasks.

---


### 98. [Belief-State Management Meets Rubric Rewards for Agentic Forecasting](https://arxiv.org/abs/2611.27286)

**<font color=#1a73e8>作者：</font>** Jingyi Chai, Yun Liao, Hao Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current large language model (LLM) agents still struggle to forecast real-world events. This stems from two primary limitations: i) standard ReAct harness accumulates reasoning and evidence within one growing context, and ii) outcome-based rewards in forecasting lead to a slow and noisy signal that cannot distinguish sound reasoning from lucky guesses. To address these, we introduce a forecasting training framework including harness design and post-training. For the harness side, we propose Proactive Belief-State Management (PBM), equipping agents with a fold tool to compress lengthy context into compact belief states and reset the context for subsequent exploration. For the training side, we develop SEIPH, a five-dimensional, outcome-blind rubric, providing process-quality rewards. Using the rubric-based reward, we post-train a 35B model with PPO and GRPO, yielding DeepForecaster-PPO and DeepForecaster-GRPO. Theoretically, we prove that idealized fold-based stopping converges and calibrated local rewards reduce segment-level gradient variance. Empirically, DeepForecaster-PPO (35B) achieves the best Brier score on both ForecastBench and Polymarket-Sim, outperforming frontier agents based on DeepSeek-V4-Pro (1.6T), Kimi-K2.6 (1T), and GPT-5.5. DeepForecaster-GRPO ranks second on both FutureX metrics. Ablations reveal that PBM also improves the untrained base model without any training. Calibration analysis shows that DeepForecaster-PPO makes more accurate high-confidence predictions than Qwen3.6 and GPT-5.5. Trajectory analysis further shows that forecasts generally improve from the first to the final belief state as agents gather evidence and revise their judgments.

---


### 99. [HookEvo: A Framework for Coordinated Plugin Evolution on Hook-Enabled Agent Runtimes](https://arxiv.org/abs/2611.27294)

**<font color=#1a73e8>作者：</font>** Shengze Huang, Yanyu Mao, Xiaofei Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Repairing failures in tool-using agents can require coordinated changes to how the harness interprets tool receipts, assembles context, and checks actions. We introduce HookEvo, a framework that uses an existing agent runtime's lifecycle hooks to evolve task-specific harnesses. We instantiate HookEvo on DeepSeek Harness. In each round, a separate improver diagnoses failures from execution traces and proposes a candidate. HookEvo evaluates the candidate against the current harness on matched tasks and carries the retained version into the next round. A single candidate can jointly edit executable plugin handlers and the state they share within a task, allowing a tool receipt to inform context and control a later action. Using a frozen Qwen3-4B executor, the selected harnesses lead the reported Qwen3-4B comparisons, achieving 95.41% on ALFWorld, 70.56% on DBBench, 48.17% on WebShop, and 41.67% on OSBench. Across three improvers and three edit scopes, from skill text to single-component and coordinated executable edits, GPT-6.1 Sol shows the largest average gain from the broadest scope. Our code is available at this https URL.

---


### 100. [Can Reasoning and Image Description Enhance Yes/No Visual Mathematical Understanding?](https://arxiv.org/abs/2611.27302)

**<font color=#1a73e8>作者：</font>** Guangcheng Song, Weichuan Wang, Linqi Song  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (VLMs) have achieved strong performance on general visual tasks, yet their ability to understand mathematical images remains limited. This paper investigates whether explicit reasoning and textual image descriptions can enhance VLMs' performance on binary yes/no visual mathematical questions. To achieve this, we curated a paired evaluation set to benchmark prominent open-source VLMs under varying prompt and input conditions. In particular, we leverage Chain-of-Thought (CoT) prompting and use textual descriptions, either replacing or augmenting visual inputs, to isolate and evaluate mathematical comprehension. Our results show that explicit reasoning improves performance, especially in paired consistency accuracy, while textual image descriptions do not consistently help and may degrade performance. These findings suggest that reasoning is important for stable visual mathematical judgement, whereas description-based intermediates require more careful design.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
