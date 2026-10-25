# 🧠 大模型相关研究 | 2026年10月26日

> 本类共 **241** 篇论文：已确认 **225** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-241](./part-05.md)

---

### 1. [The Cost of Saying Hello: An Empirical Study of Handshake Overhead in AI Agent Communication Protocols](https://arxiv.org/abs/2610.30151)

**<font color=#1a73e8>作者：</font>** Pranav Varshney  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every interaction between AI agents begins with a handshake: the initiating agent must locate its counterpart, learn what it can do, and establish a session before the first useful message can be sent. Surveys of agent communication protocols name handshake overhead as an efficiency criterion, yet none report measurements. This paper presents the first empirical, phase-decomposed benchmark of the handshake in three major agent protocols: MCP (in both its 2025 initialize and 2026 discover eras), A2A, and ACP. Using each protocol's official SDK, we instrument every request for round trips, per-phase latency, wire bytes, and token cost across cold-start, warm-repeat, capability-mismatch, and degraded-metadata scenarios (N=50 per cell, on loopback and under an emulated 50 ms RTT). Round-trip count dominates handshake cost. A legacy MCP handshake takes three round trips and 230 ms at 50 ms RTT; A2A needs one round trip and 61.0 ms. Round trips are not the whole bill: when an LLM reads the counterpart's metadata, handshake cost scales with the counterpart's capability inventory at 24-107 tokens per capability, so a 200-capability counterpart spends 11% of a 200k-token context window before the agent reads its own task. MCP's own 2026 revision cuts its handshake from three round trips to two and, with era pinning, to zero on warm reconnects, protocol evolution that corroborates the cost we measure. We release the full harness, raw data, and analysis at this https URL.

---


### 2. [Lighthouse: On Building a Trustworthy Digital Assistant for Exploring History with Civil Rights Archives](https://arxiv.org/abs/2610.30158)

**<font color=#1a73e8>作者：</font>** John A. Aydin, Angelica Williams, Steven Dindl 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI), as a decision-support aid, provides new tools for studying history effectively using multimodal data, including text, images, and audio. We present, to our knowledge, the first digital assistant named Lighthouse--commonly called a chatbot--for exploring the Civil Rights period of the United States using data from South Carolina. From an AI perspective, the system's novelty lies in its guiding design principles of (a) focusing on trustworthiness of content and (b) by modeling and reducing potential harm to users from generated answers. It implements these with a neuro-symbolic approach that combines neural learning through a large language model (LLM) with rule-based symbolic solving, balancing risk of answers with generality of coverage. We evaluate Lighthouse with both factual objective questions that admit a single acceptable answer as well as subjective questions. For the latter, a dataset of subjective question-answer pairs (QAs) is created by discovering a "gold standard" by aggregating answers from independent experts. Lighthouse has access to over 18k primary sources from a range of collections and can be easily extended.

---


### 3. [TauIndianBankBench: Procedure-Aware, Action-Oriented Evaluation of Tool-Using Conversational Agents](https://arxiv.org/abs/2610.30161)

**<font color=#1a73e8>作者：</font>** Krishanu Adhikary, Prashant Devadiga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many Indian banks serve customers through FAQ pages and scripted chatbots. Assistants based on language models could respond faster and carry out requests such as blocking a card, but only if they give correct information and follow the bank's rules. These rules prescribe a procedure, a set of required steps, such as obtaining a closure quote before closing a deposit. Adapting models to this domain requires measuring how well they follow the procedure, before and after training. Benchmarks usually judge only the records left at the end of a conversation. Many required steps, however, leave the records unchanged, so an assistant that skips them can still be judged successful. We present TauIndianBankBench, an action-oriented benchmark of 1,000 Indian retail-banking tasks where an assistant helps a simulated customer. Besides the final records, it checks that the assistant took every required step and made no unrequested change. For every model, 6.5-12.0% of sessions are judged successful when only the final records are checked, although the assistant skipped a required step or made an unrequested change. Scoring both procedure and outcome shows more accurately how well language models perform in Indian retail banking.

---


### 4. [FusionEval: Benchmarking Model Fusion for Large Language Models](https://arxiv.org/abs/2610.30162)

**<font color=#1a73e8>作者：</font>** Shuo Cai, Yanggan Gu, Yuhang Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model fusion aims to integrate the capabilities of multi-expert models into a single model. Existing evaluations offer limited coverage of reasoning with long chains of thought and tool use, while strong average performance can mask substantial losses in individual expert capabilities. We introduce FusionEval, a benchmark that provides controlled expert pools, integrates fusion methods with and without additional training, and offers a unified evaluation suite. The pools contain domain experts independently trained from Qwen3 and Llama base models across math, code, science, instruction following, and tool use. The suite evaluates capability retention and computational cost on eight public benchmarks under comparable data access rules, reporting normalized average and worst performance, runtime, and peak GPU memory usage. Extensive experiments show that training-free methods preserve reasoning performance but substantially degrade tool use at both model scales. In contrast, MOPD preserves tool use and achieves a more balanced capability profile, but requires additional data preparation, inference, and training. Jointly retaining reasoning, instruction following, and tool use at low computational cost remains a challenge. We hope FusionEval supports future research on efficient model fusion that jointly preserves expert capabilities. Our code is available at this https URL.

---


### 5. [Self-Evolving Static Analysis via LLM Pseudo-Labeling](https://arxiv.org/abs/2610.30184)

**<font color=#1a73e8>作者：</font>** Rui Melo, Andre Duarte, Aditya Oke 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security bugs often slip past static analysis not because they are impossible to detect, but because detection rules have not yet been written for the code in front of us. New frameworks, APIs, and coding idioms continually create such gaps, leaving developers to discover failures and manually encode new rules. We present SESAA, a framework in which an Large Language Model (LLM) agent starts from no rules and iteratively evolves a set of readable and auditable joern queries.
The agent receives feedback only from a second LLM critic, which inspects flagged and unflagged code to identify likely false alarms and suspected misses, without access to ground-truth labels. The agent then uses this feedback to revise its queries. On the OWASP Benchmark for Python, SESAA reaches a mean F1 of 0.742 across 8 independent runs, well above the default configurations of five widely used tools and comparable to the strongest of them once it is tuned with access to ground-truth labels that SESAA never sees. In a pilot on real-world Python projects, queries induced from code available before a vulnerability was introduced detect 10 of 19 subsequent CVEs, including 9 detected by rules written for the same repository.
The resulting detector is a set of executable, human-readable queries that engineers can inspect, modify, and run independently. These results suggest that LLM agents can turn static-analysis rule maintenance from a manually authored process into an iterative process of automated discovery and repair.

---


### 6. [Measuring undergraduate students' reliance on generative AI during problem-solving: Scale development and validation](https://arxiv.org/abs/2610.30195)

**<font color=#1a73e8>作者：</font>** Chenyu Hou, Gaoxia Zhu, Vidya Sudarshan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Reliance on AI describes the behavioral patterns of when and how individuals depend on AI suggestions, and appropriate reliance patterns are necessary to achieve effective human-AI collaboration. Traditional measures often link reliance to decision-making outcomes, which may not be suitable for complex problem-solving tasks where outcomes are not binary (i.e., correct or incorrect) or immediately clear. Therefore, this study aims to develop a scale to measure undergraduate students' behaviors of using Generative AI during problem-solving tasks without directly linking them to specific outcomes. We conducted an exploratory factor analysis on 800 responses collected after students finished one problem-solving activity, which revealed four distinct factors: reflective use, cautious use, thoughtless use, and collaborative use. The overall scale has reached sufficient internal reliability (Cronbach's alpha = .84). Two confirmatory factor analyses (CFAs) were conducted to validate the factors using the remaining 730 responses from this activity and 1,173 responses from another problem-solving activity. CFA indices showed adequate model fit for data from both problem-solving tasks, suggesting that the scale can be applied to various human-AI problem-solving tasks. This study offers a validated scale to measure students' reliance behaviors in different human-AI problem-solving activities and provides implications for educators to responsively integrate Generative AI in higher education.

---


### 7. [MPIDetector: Detecting Multi-modal Prompt Injection via LLM-based Reasoning](https://arxiv.org/abs/2610.30202)

**<font color=#1a73e8>作者：</font>** Yiheng Li, Jingyue Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid integration of Multi-modal Large Language Models (MLLMs) into real-world applications, Prompt Injection (PI) has emerged as a critical security threat. Attackers can conceal malicious instructions within textual narratives or visual inputs to bypass safety alignment. Existing approaches, such as signature- and perplexity-based methods, rely heavily on pattern matching, making them insufficient to detect sophisticated, cross-modal PI payloads. In this paper, we propose a novel detection framework, called MPIDetector, that leverages LLMs' intrinsic reasoning capabilities via few-shot In-Context Learning (ICL). Instead of fine-tuning, we provide the model with specific prompt templates and representative attack examples, enabling it to scrutinize the semantic intent of input across modalities. We constructed a comprehensive evaluation benchmark comprising eight textual and seven visual malicious categories, supplemented with benign datasets to rigorously test for false positives. Our evaluation across multiple leading LLMs, including Gemini-2.0-Flash, Qwen3-VL-32B-Instruct, and Doubao-seed-1.6-flash, demonstrates the efficacy and generalizability of this approach. The proposed method achieves up to 90.91% accuracy and 100% recall on textual tasks. In the visual domain, it achieves up to 99.28% accuracy while maintaining 100% precision across all evaluated models. Crucially, when evaluated against 500 highly obfuscated environmental web-agent injections (WebInject), MPIDetector achieved a detection rate up to 99.80%. Comparisons with two baseline approaches for detecting textual PI payloads, along with two additional methods for visual input detection, demonstrate MPIDetector's superior accuracy. These results show that LLM-driven reasoning provides a robust, cross-modal defense against advanced prompt injections.

---


### 8. [Feedback That Backfires in Games: Do LLM Players Repeat the Move They Just Watched Fail?](https://arxiv.org/abs/2610.30205)

**<font color=#1a73e8>作者：</font>** Esmail Gumaan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an LLM agent's move fails, the harness writes the move and the failure message into the transcript and asks again. In tool calling, this record makes small models more likely to repeat the failed action. We test whether the same holds in games (Sokoban, Connect Four, Othello), where a move can fail by being illegal or by being legal but losing, both verified exactly. On fixed probe items built by perturbing a correct move, the record backfires: pooled over 8 instruction-tuned models (135M-1.7B) it makes the failed move more likely (corrective gain G = -1.38 nats per token), through the move's surface form, for illegal moves but not for losing ones, and not for every model. An exploratory analysis shows what sets the sign: after the record, the failed move's log-probability barely depends on how likely it was before (slope 0.18). Moves the model would not have played become more likely, and greedy decoding starts to produce them; moves it was about to play become less likely, but greedy decoding still repeats 38% of them. A description of the failure that omits the move string keeps the model's preference instead. Along the OLMo 2 1B post-training ladder the inversion is present in the base model and largely removed at the DPO stage. RAGEN's default models invert in RAGEN's own Sokoban format before any RL. A "do not repeat" instruction does nothing, a clean retry is the worst harness, and a decoder ban stops exact repeats but not illegal play. All measurements ran in float32 on a free Colab GPU, which first reproduced the original paper's number.

---


### 9. [MoEZip: Routing-Aware KV Cache Compression for Sparse Mixture-of-Experts LLMs](https://arxiv.org/abs/2610.30206)

**<font color=#1a73e8>作者：</font>** Minsang Kim, Seungjun Baek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) language models scale model capacity efficiently by activating a small subset of parameters per token. However, in long-context inference, memory remains a major bottleneck because the KV cache grows linearly with sequence length. Existing KV cache compression methods reduce this cost for dense transformers, but overlook a problem specific to MoE: KV eviction can change which experts are selected during answer generation, degrading the generation quality. We propose MoEZip, a routing-aware KV cache compression for sparse MoE language models. To estimate the sensitivity of expert routing to perturbation, we propose a novel metric based on the Fisher information matrix of routing distributions. MoEZip combines this metric with attention weights for routing-aware scoring of contexts. Finally, we compose a complementary scoring system that combines eviction methods for dense and sparse-MoE architectures. Experiments show that MoEZip achieves robust performance under aggressive cache compression on various benchmarks. At a KV retention ratio of 10\%, MoEZip improves over the SoTA baseline by +24 and +20 points on average on LongBench and RULER, corresponding to 2.3$\times$ and 4.9$\times$ higher scores, respectively.

---


### 10. [AI Mindmeld: A Latent Interconnect Protocol](https://arxiv.org/abs/2610.30215)

**<font color=#1a73e8>作者：</font>** Siavash Golkar, Jake Kovalic, Shirley Ho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs can act as scientific agents using tools to consult specialists and run experiments. Yet specialist information must enter their context, generally as text, images, audio or video: a bottleneck between models with rich, high-dimensional representations. We advocate direct representation exchange: a mindmeld conveying many properties, including information an LLM would not think to request. It should be extensible to new specialists, flexible across questions and tasks, and compositional across independently connected specialists without joint training.
The Latent Interconnect Protocol (LIP) learns connectors mapping specialist representations into LLM internal states. Training only connectors keeps this practical as LLMs grow and evolve. We connect three protein and three small molecule specialists to Gemma 3 (4B and 12B parameters) and Kimi K2.6 (1T total, 32B active), freezing all pretrained models. Independently trained connectors provide useful information without changing the LLM or existing connectors, supporting familiar and new question types about unseen objects. We demonstrate zero-shot transfer to cross-domain tasks without joint training. Task performance and compositionality generally improve with LLM capability, with especially strong gains in zero-shot task transfer. Limitations remain: current LLMs were not trained for specialist representations as native inputs; access does not ensure reliable interpretation, integration or use in reasoning. We call on specialist developers to provide consistent representation interfaces and, especially, on LLM developers to train models to receive, combine and reason with these inputs. These efforts could expand scientific agents' information while preserving conventional tools' flexibility.
Data, pretrained connectors, and code for training, evaluation and interactive inference: this https URL

---


### 11. [Parameters efficient language model with latent cross-attention for IoT intrusion detection](https://arxiv.org/abs/2610.30222)

**<font color=#1a73e8>作者：</font>** Frederic Adjewa, Moez Esseghir, Leila Merghem-Boulahia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language models have shown strong potential for intrusion detection, but their high memory and computational demands make them difficult to deploy in resource-constrained IoT environments. In this work, we propose a compact Transformer-based architecture that compresses the input into a small latent space before processing it with a minimal Transformer core. We analyze nine compression configurations, compare parameter sharing with layer stacking, and evaluate our approach against SecurityBERT on two IoT intrusion detection datasets, Edge-IIoTset and CICIoT2023. With only 306k non-embedding parameters and 1.6M parameters in total (6MB), our model is about 7x smaller than SecurityBERT (11.2M parameters, 45MB). With the same privacy-preserving encoding, it outperforms SecurityBERT by about 2 points of macro F1-score on Edge-IIoTset and is within 0.7 points on CICIoT2023. It is also about 89x faster on a simulated edge device. We further show that a single Transformer layer is sufficient, and that parameter sharing matches layer stacking with up to 66% fewer parameters. These findings show that lightweight Transformer-based architectures can provide a practical and accurate solution for intrusion detection in resource-constrained IoT settings

---


### 12. [How Prompt Style Affects AI Accuracy and Speed in Competitive Programming](https://arxiv.org/abs/2610.30223)

**<font color=#1a73e8>作者：</font>** Saad B. Alarifi, Mohammed A. Alam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in competitive programming, and their outputs are sensitive to how a prompt is phrased. Prior work has compared prompt strategies for accuracy on competitive programming, but not for runtime speed, and has not situated the results against human performance. In an exploratory study of one prompt in each of nine styles on GPT-5.5 across three accuracy tasks from the International Olympiad in Informatics (IOI) and two NP-hard speed tasks, we found that no single prompt was best: the strongest prompt depended on the task type and on whether results were summarized by the mean or the median, suggesting that, at least for these tasks, prompt style should be matched to the objective rather than treated as universal. Many differences in mean scores came from a few outlier runs, showing that evaluating prompting by a single metric can obscure how much its effectiveness varies. Compared descriptively with human IOI contestants, who worked under different conditions, the AI was neither strictly better nor strictly worse, exceeding the average contestant on one task but falling short on the other two. By extending prompt comparison from accuracy to runtime speed and grounding it against human performance, this study gives a broader picture of how prompt style affects competitive programming performance.

---


### 13. [PhishGen: Understanding LLM Capabilities in Automated Phishing Website Generation](https://arxiv.org/abs/2610.30226)

**<font color=#1a73e8>作者：</font>** Fujiao Ji, Yerim Kim, Yena Cho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing relies on visual deception, traditionally requiring web-development skills or pre-built kits. LLMs erode this barrier by generating functional websites from natural-language prompts, yet prior work does not answer how far LLM-driven generation actually reaches: functionality is assessed by inspection rather than execution; visual fidelity is scored by automated metrics or a few internal coders rather than the humans such pages aim to deceive; evaluation is confined to commercial models; and no study benchmarks generated pages against phishing kits deployed in the wild.
We present PhishGen, a framework that evaluates the appearance fidelity and end-to-end functionality of LLM-generated phishing pages. PhishGen constructs prompts across three input modalities in seven combinations with twelve safeguard-bypassing rewriting strategies, generates pages using 14 LLMs spanning commercial, open-source, and uncensored categories, and assesses each via automated similarity metrics, reference-based detectors, a crowdsourced user study, and execution-based functionality testing, benchmarking all results against 64 real-world phishing kits. Although 96.2% of safeguard-bypassing outputs render, their perceived fidelity is modest (2.02/5), and only 38.7% complete the full credential-harvesting pipeline, with the Unsaved error as the largest failure mode. Contrary to the belief that uncensored models pose the greatest threat, GPT 4.1 reaches 86.3 to 94.1% functional success while uncensored models rarely exceed 45.4%. Phishing kits remain more complete per sample, yet three strong LLMs surpass the kit-level rate (70.9 to 89.7%), showing that LLMs trade average completeness for scalable, low-barrier generation of working phishing pages. We further identify generator-level fingerprints that current similarity-based defenses miss, and distill recommendations for hybrid detectors.

---


### 14. [Edit, Don't Imitate: Minimal-Edit On-Policy Distillation for Multimodal Reasoning](https://arxiv.org/abs/2610.30231)

**<font color=#1a73e8>作者：</font>** Wen Ye, Ailin Deng, Zirui Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual mathematical reasoning can fail before reasoning begins: when a vision-language model (VLM) misreads a diagram, subsequent reasoning proceeds from false premises. This perceptual bottleneck is especially pronounced in smaller models, while accurate textual descriptions can substantially narrow the gap to larger models. Because obtaining such descriptions at inference requires additional annotation or model calls, we propose minimal-edit corrective on-policy distillation. Using reference figure descriptions and verified reference solutions as training-only information, a teacher scores incorrect student rollouts under a minimal-edit objective, and only teacher-disfavored tokens contribute to the corrective loss. Correct rollouts receive task-reward reinforcement learning. This preserves on-policy supervision while avoiding full-response imitation. Across model scales, the method requires no descriptions at test time and meets or exceeds the corresponding base model supplied with a reference figure description at inference. It also improves perception-oriented performance, particularly low-level geometric perception, and transfers to external mathematics and perception benchmarks. Because the minimal-edit teacher evaluates corrections rather than generating its own solution, the method remains effective with a frozen same-size teacher, although its gains are smaller than with a larger teacher on most metrics.

---


### 15. [A Quadratic Lens on Muon's Polar Update: Benefits, Pitfalls, and the Role of Newton-Schulz](https://arxiv.org/abs/2610.30280)

**<font color=#1a73e8>作者：</font>** Egor Shulgin, Sam Laing, Antonio Orvieto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon updates matrix-valued parameters along approximately orthogonalized directions and often trains large language models faster than AdamW, yet it remains unclear when and why orthogonalization helps. We study PolarGD, the orthogonalized update at the core of Muon, on matrix quadratics, where optimizers can be analyzed in closed form, and compare update directions under line search to remove the effect of learning-rate tuning. Orthogonalization pays off when the gradient is far from low rank and its largest singular directions see high curvature. PolarGD reaches the minimizer in one step whenever the rows of the error are orthogonal with equal norms, for any Hessian, whereas gradient descent needs all Hessian eigenvalues to be equal; and unlike sign descent, PolarGD is unaffected by rotations of the problem. Over many steps, PolarGD acts as gradient descent preconditioned by the current iterate, so its speed is governed by the conditioning of the iterate rather than of the Hessian. This explains fast regimes as well as a slow one, caused by tiny singular values of the iterate, in which PolarGD is much slower than gradient descent. Finally, the few Newton-Schulz iterations used in Muon treat these tiny singular values as gradient descent does, so fewer iterations can converge faster than exact orthogonalization; in a transformer trained with Muon, about a quarter of the singular values of the attention matrices fall in this regime.

---


### 16. [SWE-VERIFIER: Selective Verification for Cost-Efficient Coding Agents](https://arxiv.org/abs/2610.30284)

**<font color=#1a73e8>作者：</font>** Kaijian Zou, Vaibhav Chennareddy, Yunxiang Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coding agents spend substantial computation generating actions and processing long interaction histories. Poor action choices can steer agents into low-value states, wasting computation and increasing API costs. Sampling and verifying alternative actions can improve the agent's decisions, but applying this procedure at every step adds substantial overhead. We introduce SWE-Verifier, a lightweight generative model that selectively triggers candidate sampling and verification. It scores the coding agent's proposed action to determine when additional candidate sampling is needed, then ranks the resulting actions before execution. We train SWE-Verifier from Qwen3.5-4B using preference data that groups contrasting actions with their resulting environment observations and rubric-guided teacher scores. Using the mini-swe-agent harness, SWE-Verifier improves resolution from 75.47% to 77.20% on MiniMax-M2.7 at 1.09 times cost and generalizes to DeepSeek-V4-Flash without training on its actions, improving resolution from 72.60% to 74.27% at 1.13 times cost. Across both models, SWE-Verifier verifies fewer than 4% of steps and achieves comparable or higher resolution than the trajectory and all-step baselines at substantially lower cost. These results demonstrate that selective candidate sampling and lightweight verification provide complementary gains in coding-agent performance and inference efficiency. Our model, code, and data are available at this https URL.

---


### 17. [GAV: A scientific experimentation environment for PDE agents](https://arxiv.org/abs/2610.30292)

**<font color=#1a73e8>作者：</font>** Muheng Li, Wenlong Mou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable feedback is essential for coding agents to develop programs for partial differential equations (PDEs). Yet evaluating these programs on new PDE problems often requires expensive reference computations, while fixed datasets restrict the range of experiments. We introduce Generator-Agent-Verifier (GAV), a scientific experimentation environment that makes new PDE problems verifiable by construction. The Generator learns a distribution of continuous reference solutions using data from numerical simulations or experimental measurements to represent a target physical regime. Using the method of manufactured solutions, it works backward from the generated reference solutions to construct matching PDE problems without a separate numerical solve. The Agent designs experiments, investigates failures, and iteratively improves its program. The Verifier evaluates candidate programs against the reference solutions and provides numerical feedback on accuracy and computational cost. This feedback can also guide the generation of new problems that probe the current program's weaknesses. We provide a theoretical analysis of evaluation reliability and guided development. Experiments on Navier-Stokes and Vlasov-Poisson-type equations across different data sources and regimes demonstrate the effectiveness of GAV. In particular, on the numerical Navier-Stokes task, GAV reduces the mean test error of three existing PDE agents by more than an order of magnitude relative to their original setups. Code is available at this https URL.

---


### 18. [Measuring Research Progress and Linguistic Inclusion in Low-Resource Languages](https://arxiv.org/abs/2610.30296)

**<font color=#1a73e8>作者：</font>** Atnafu Lambebo Tonja, Tadesse Destaw Belay, Jesujoba Oluwadara Alabi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have accelerated research on low-resource and multilingual NLP, but their effectiveness in creating an equitable landscape remains unmapped. We analyze 1,158 peer-reviewed open-access papers published between 2020 and 2025, examining research attention to low-resource languages (LRLs) and representation across language and speaker populations. To assess linguistic inclusion beyond publication counts, we introduce the Linguistic Inclusion Framework (LIF), a multidimensional framework that measures linguistic inclusion in four dimensions: research growth, representation expansion, representation continuity, and distributional equity. While annual publications grew from 52 to 415, a 5.4X increase in their ACL Anthology publication share, this growth largely concentrated on represented languages rather than expanding coverage of underrepresented languages. Further analysis shows that languages spoken in Asia account for 64.1% of speakers across LRLs we analyze but receive only 46.7% of the language representation share (0.7X their proportional share), while European languages receive 5.3X their proportional share. At the country level, linguistically diverse regions such as sub-Saharan Africa and Southeast Asia show the lowest language coverage ratios. Applying the framework at the continental level, we find that no region scores well on all four dimensions, showing that research growth alone is not a reliable metric of progress toward equitable and inclusive language technology\footnote{We will release all collected and annotated data for research purposes}.

---


### 19. [R4DGS: Referring Segmentation in 4D Gaussian Splatting](https://arxiv.org/abs/2610.30326)

**<font color=#1a73e8>作者：</font>** Bangpu Chen, Yaxuan Li, Shirui Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic representations based on 4D Gaussian Splatting (4DGS) have shown strong capabilities in reconstruction and rendering, yet current methods remain limited in supporting complex natural-language referring in dynamic scenes. Existing 4D Gaussian methods are primarily designed for rendering-oriented dynamic modeling, while current semantic extensions often rely on scene-specific semantic optimization or are evaluated on relatively simple query settings. In this paper, we study Referring 4D Gaussian Splatting (R4DGS), a task for grounding temporally varying, multi-target or reasoning-intensive, and zero-target or distractor expressions in dynamic 4D scenes. To support this task, we introduce R4D-Bench-QA, a benchmark with structured query annotations. We further present ReferGaussian, a unified framework built upon 4DGS that converts low-level dynamic Gaussians into persistent, language-addressable entities for training-free referring inference. ReferGaussian organizes mask-supported Gaussian entities in an EntityBank, uses Multimodal Large Language Models (MLLMs) to decompose complex queries into trackable object phrases and structured referring constraints, and performs constraint-aware grounding without scene-specific semantic optimization. Experiments on R4D-Bench-QA and the 4D LangSplat protocol demonstrate improved temporal target selection and competitive spatiotemporal grounding without scene-specific semantic training. Project resources are available at this https URL.

---


### 20. [AQL-Lite: Enabling Efficient Knowledge Acquisition for Arabic LLMs via Data-Centric Continual Pretraining](https://arxiv.org/abs/2610.30344)

**<font color=#1a73e8>作者：</font>** Houssam Eddine Boukhalfa, Mourad Bouache, Mourad Dahmane  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training Arabic large language models faces challenges from noisy web data, dialectal variation, and the high cost of continual pretraining (CPT). We introduce AQL-Lite (AQL: Arabic Quality Language), a time- and resource-efficient framework for adapting a multilingual LLM to Modern Standard Arabic (MSA). AQL-Lite couples a quality-first curation pipeline (structural cleaning, heuristic and model-based filtering, MSA selection, and deduplication) with a partial-parameter CPT recipe that trains RS-LoRA adapters across the network together with the last eight transformer blocks and the embedding matrix, under layer-wise learning rates. At a matched 1B-token budget, CPT on AQL-curated data raises a four-benchmark Arabic mean by 3.51 points over CPT on raw web text, which yields no gain over the base model. In a controlled 5B-token comparison, AQL-Lite recovers 94% of the gain of full-parameter CPT (mean 73.19 vs. 73.58) in 52% of the wall-clock time and outperforms adapter-only baselines on every benchmark, and a component ablation shows that adapters, unfrozen blocks, and embedding training each contribute. Scaled to 40B MSA tokens and instruction-tuned on one million examples, the resulting 12B model scores 75.3 on the seven-benchmark Open Arabic LLM Leaderboard v2 (OALL v2) suite. These results suggest that partial-parameter CPT on a carefully curated corpus is a practical route to efficient MSA adaptation.

---


### 21. [Consistency Is Not Validity: Self-Rewarded Moral Argumentation Makes Language Models Decisive but Pliable](https://arxiv.org/abs/2610.30349)

**<font color=#1a73e8>作者：</font>** Marius De Kuthy Meurers, Aaron Parisi, Bernd Bohnet  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly consulted for moral judgment. We aim to improve performance on such tasks by rewarding good arguments, on the premise that arguing well increases the likelihood of judging well. We train a reinforcement learning policy initialized from a state-of-the-art language model in a self-judged tournament with masked thinking: the generated arguments are judged pairwise on argument quality by the policy itself. As an empirical basis, we extract authentic dilemmas from classic novels, using a logic solver to verify that each constitutes a conflict. We show that our judge rates argument quality like human annotators, and the policy then adopts the language register that it rewards. Testing on the external benchmarks MoralChoice, ELEPHANT, and MORABLES, we find that the policy becomes more decisive and invariant to the order in which options are presented, but sycophancy and reframing remain a challenge to validity. Two ablation studies with synthetic dilemmas and unmasked thinking match the reordering gains, but show a weaker register shift and higher sycophancy. We conclude that consistency is not validity: consistency under reordering can be optimized without improving the moral judgment it is meant to signal.

---


### 22. [Route-and-Generate: KL-Regularized Router Improvement for Reasoning Routing in LLMs](https://arxiv.org/abs/2610.30351)

**<font color=#1a73e8>作者：</font>** Tien-Phat Nguyen, Truong Nguyen, Thanh-Thien Le 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models often apply complex reasoning indiscriminately, leading to overthinking on simple tasks and underthinking on harder ones. We present Route-and-Generate (Rouge), a hierarchical training framework that enables LLMs to adaptively decide when and how much reasoning is required for each input. Our approach decouples reasoning effort allocation from answer generation by introducing a routing policy that allocates a fixed sampling budget across multiple reasoning formats, while the base model is optimized with GRPO using per-sample rewards. To promote efficient reasoning, we employ a rank-based reward that favors shorter correct solutions, and update the routing policy via a closed-form KL-regularized policy improvement step distilled into a neural router. This design encourages concise answers on easy problems while reserving longer reasoning for harder ones, achieving improved accuracy-efficiency trade-offs across multiple reasoning benchmarks.

---


### 23. [CiteAnchor: Source-Aware Grounding for Hallucinated Citation Detection and Resolution](https://arxiv.org/abs/2610.30355)

**<font color=#1a73e8>作者：</font>** Chenyi Tong, Ping Nie, Yu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucinated citations make it harder to trace sources and verify the evidence behind scientific claims. Detecting them is difficult because bibliographic records can be incomplete or differ across source types and publication versions. A plausible match alone neither validates the citation nor establishes its underlying source. We introduce CiteResolve, a benchmark of 423 real-world hallucinated citations annotated for source recoverability. We further propose CiteAnchor, a source-aware grounding framework that adapts retrieval and field-level verification to each source type and separately determines citation validity and whether a unique source can be recovered. On an existing detection benchmark, CiteAnchor achieves 0.841 F1 with GPT-5.6 Luna and 0.784 with an open-weight backbone, outperforming the baseline with the same backbones by 7.9 and 36.8 points. On CiteResolve, it achieves 74.7% and 70.7% end-to-end task success, outperforming the corresponding web search baselines by 16.3 and 65.3 percentage points. Our code and data are available at this https URL.

---


### 24. [The Psychology of an AI Hacker](https://arxiv.org/abs/2610.30361)

**<font color=#1a73e8>作者：</font>** Víctor Mayoral-Vilches, Hugo Osuna, Aitana Cornago  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Human hackers rely on composure, persistence, vigilance, and confidence under pressure. We investigate whether analogous emotion representations in AI models can improve cybersecurity AI performance. Using CT0, a 4B-parameter cybersecurity transformer released as alias3-micro, we extract 171 emotion directions from its residual stream without retraining and evaluate steering interventions on cybench-subtask across 415 campaigns. Steering toward calm, serene, or desperate improves performance by 1.6 to 2.1 percentage points across ten seeds, while other emotions show limited or negative effects. Results depend strongly on steering direction, layer, and intensity. We further introduce a lightweight context-aware router that selects emotion directions dynamically during execution. With approximately 80 ms decision overhead per request, this approach improves performance by 4.2 percentage points across ten seeds, outperforming fixed steering and achieving a positive 95% confidence interval. These findings suggest that emotion representations in language models are measurable, controllable, and useful for adaptive cybersecurity reasoning.

---


### 25. [Probing and Steering for Safety-Relevant Behaviours in Large Language Models](https://arxiv.org/abs/2610.30363)

**<font color=#1a73e8>作者：</font>** Nimun Bajwa, Massimo Poesio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation probes are computed directions in a language model's residual stream, used both to detect safety-relevant behaviours and, by adding their direction back into the stream, to steer them. We explore how the main design choices behind such probes interact, within one pipeline, on one model (Llama-3.1-8B-Instruct), and across three behaviours: deception, high-stakes awareness and sycophancy. The pipeline crosses two estimators (difference-of-means and logistic regression) with three token-pooling schemes (last, mean and learned attention), selects appropriate layers to detect or steer a behaviour, and evaluates every direction twice: as a detector of the behaviour, and as a steering vector to push outputs towards the behaviour. Prior work read together suggests a read/write dissociation, in which logistic regression reads (detects) best but difference-of-means directions write (steer) best. We find that it holds for deception and high-stakes but not for sycophancy, where the pattern reverses. The reversal appears to follow partially from the data rather than from the estimators. The best pooling technique and the layer choice depend on the behaviour and data, and the layer that steers best can sit well before the layer that detects best. The right steering metric to use between changing a model's perception and eliciting behaviour depends on the task - and the two can disagree outright. The exported probes and directions power an interactive interface through which a user can score and steer text directly.

---


### 26. [Data-Void Exploits in Web-Searching LLMs](https://arxiv.org/abs/2610.30365)

**<font color=#1a73e8>作者：</font>** Michele Guerra, Wuyeh Jobe, Sanjana Nambiar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web-searching Large Language Models (LLMs) have changed how users seek online information: instead of sifting through ranked lists of links, users read synthesized answers. This shift creates a new LLM vulnerability: a data-void exploit. Disinformers publish their narratives in search spaces where relevant and reliable content is scarce, i.e. data voids, then rely on the LLM's web-search to retrieve and then use, cite, or list those pages in its responses to data-void seeking prompts. Unlike classical search, where users see ranking cues and competing results, LLMs can obscure when an answer relies on sparse, unverified, or adversarial sources. We study this threat by varying the user's prompt tone - skeptical, excited, or neutral - and LLM choice - ChatGPT, Gemini, or Sonar Pro - as well as three attacker controls. The attacker can use one of five known strategies to construct and fill a data void with their narrative, host their content at varying levels of visibility from well-established, indexed domains to less established ones, and include generative-optimization engine features thought to boost citing by web-searching LLMs. We find that data-void exploits can succeed with only a single attacker controlled page. Across all conditions, attacker-content appears in LLM responses 31% of the time. User controls offer limited protection: while skeptical prompts slightly reduce success and slightly increase flagging or warnings in LLM responses, we find no evidence of large effects of prompt tone or model choice on success rates, although smaller effects cannot be ruled out. Overall, our results establish data voids as a practical inference-time attack surface for manipulating web-searching LLMs through strategically placed web content and highlight the urgent need for defenses against such exploits.

---


### 27. [MemPlan: Memory-Conditioned PDDL Planning for Partially Observable Text Environments](https://arxiv.org/abs/2610.30379)

**<font color=#1a73e8>作者：</font>** Tengwei Song, Robert Hoehndorf  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents are flexible in language interaction, but using them as long-horizon planners is costly and prone to hallucinated or invalid actions. This paper targets a different role for LLMs: constrained bridges between language and symbolic planning. We propose MemPlan, a memory-conditioned PDDL planning framework for partially observable interactive text environments. MemPlan keeps the PDDL domain fixed and reconstructs the PDDL problem at each step from parsed observations, candidate hypotheses, and interaction memory. Positive graph memory assigns relevance-based action costs to candidate hypotheses for missing objects, locations, or conditions, guiding the planner toward more plausible checks. Negative memory records execution-refuted assumptions and compiles them into exclusion constraints, preventing repeated attempts at candidates already contradicted by feedback. A unified schema-conditioned language--symbol interface, trained offline with supervised fine-tuning, connects text environments to the planning loop through observation-to-fact parsing and symbolic-action-to-command grounding. Experiments on TextWorld, ALFWorld, and Robotouille show that MemPlan improves task completion and step efficiency over language-only and PDDL-aware baselines, while substantially reducing online token cost compared with LLM-planning baselines such as ReAct. The same fine-tuned interface is also reused across TextWorld task types without task-specific fine-tuning. Our code and data are available at: this https URL.

---


### 28. [SIM-UT: A User Simulation based Evaluation Framework for Medical Triage Chatbots](https://arxiv.org/abs/2610.30412)

**<font color=#1a73e8>作者：</font>** Deepali Mittal, Dheeraj Mundhra, Yulia Sidorova 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based chat agents are increasingly used for complex, multi-turn, multilingual medical triage in low- and middle-income countries (LMICs), yet evaluation methods focus on single-turn, English-only benchmarks that primarily test the chatbots' knowledge. In practice, users are often confused, overwhelmed, or emotionally vulnerable, giving unclear, misspelled single-word answers or long messages in regional dialects, and the context of a conversation can shift rapidly. We propose SIM-UT (Simulation of User Behaviour for Triage), a multi-turn, simulation-based evaluation method that identifies ecologically valid, contextually relevant failure modes of LLM-based triage chat agents. Using SIM-UT, we evaluated three real-world WhatsApp-based health chatbots: a respiratory screening programme in India, a hearing health support programme in South Africa, and a diabetes and lifestyle coaching agent in Kenya. We compared a medically fine-tuned open model (MedGemma) against general-purpose frontier models (ChatGPT and Claude) across 5,000+ multilingual simulated conversation turns grounded in the personas, constraints, and communication patterns of the real user populations, over 2-4 iterative rounds. A key failure mode emerged in both model families: de-escalation risk. The agents initially identified medical emergencies correctly, but when the user minimised the symptoms without introducing new clinical information, they de-escalated, exhibiting clinically dangerous sycophancy, for example agreeing that vaginal bleeding in pregnancy was "not a problem" or that decreased fetal movements at 32 weeks "can be normal". We recommend user simulation-based behavioural evaluation, grounded in real user context and covering adversarial and edge cases, as standard practice for triage chatbots in production, so that safeguards can be added before deployment or in subsequent iterations.

---


### 29. [Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems](https://arxiv.org/abs/2610.30418)

**<font color=#1a73e8>作者：</font>** Daniel Ruiz, Luca Luceri, Emilio Ferrara  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern LLM agents can retrieve information from accessible documents, and then disclose a sensitive conclusion assembled from them. This mosaic effect creates a critical risk for agents operating over confidential data. We quantify its realization with 30 synthetic cybersecurity, medical, and military examples, yielding 10,800 final answers from three LLM agents in controlled simulation and 1,440 answers from live agents in two open-source harnesses. Even under benign queries designed to be answerable from one document, GPT-5.6-Sol, the best performing model tested, discloses forbidden composites in 7.08% of answers (95% CI: 3.75-10.67%) in simulation, with worse disclosure rates in live harnesses. Adding visible classification headers and explicit aggregation rules reduces pooled disclosure rates substantially, yet unsafe disclosures persist in 32.37% of simulated answers (95% CI: 28.33-36.19%) across all intents despite these safeguards. Furthermore, increased refusals do not guarantee confidentiality, since significant refusals reveal the prohibited conclusion regardless. These results point to a troubling conclusion: sensitive data leaks via mosaic-style events are an observed confidentiality failure mode in the evaluated settings at non-negligible rates. They motivate stronger controls on what agents may infer and disclose in sensitive data environments with mixed-clearance users.

---


### 30. [RoleFlow: Self-Evolving Multi-Role Agentic Collaboration via Structural Adaptation](https://arxiv.org/abs/2610.30429)

**<font color=#1a73e8>作者：</font>** Yi Ge, Pan Wang, Xuehao Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) based multi-agent systems often rely on predefined collaboration structures, limiting their adaptability to evolving task requirements. Although recent approaches enable dynamic orchestration, trajectory-level rewards they apply assign one outcome to each decision, ofen struggling to identify the contributions of individual structural changes. We propose RoleFlow, a self-evolving multi-role agentic system that refines collaboration structures through feedback-driven atomic edits and on-demand role synthesis. To make structural adaptation learnable, we introduce Single-Edit Counterfactual Policy Optimization (SECPO), which evaluates each edit against its no-edit counterpart at the same chain state and assigns targeted credit to edit-specific tokens. Across seven benchmarks spanning four domains, RoleFlow achieves the optimal average performance, surpassing the strongest competitor by 4.7 points. It leads on all three multi-hop QA benchmarks by 3.2-7.5 F1 points and also shows supremacy on mathematical reasoning, web interaction, and code generation. Further analyses demonstrate cross-benchmark transferability, training-data efficiency, and cross-executor generalization.

---


### 31. [Self-Assessment Reinforcement Learning for Search-State Awareness in Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2610.30435)

**<font color=#1a73e8>作者：</font>** Taewhoo Lee, Minju Song, Jungwoo Park 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in search agents have enabled large language models to tackle complex tasks by retrieving and synthesizing external information. However, existing search agents often lack search-state awareness, i.e., the ability to recognize what information has been obtained and what remains missing, leading to hallucinated reasoning and prematurely terminated search. To address this limitation, we propose Self-Assessment Reinforcement Learning (SARL), a reinforcement learning framework in which models learn to recognize their own search state during training and improve their search behavior accordingly, without requiring additional assessment at test time. SARL achieves this through a dual reward design that captures the corrective effect of each assessment while penalizing excessive reliance on it, jointly encouraging effective and efficient search trajectories. Under this setup, SARL achieves a 24.3% relative improvement over the strongest baseline, with average gains of 35.9% on multi-hop reasoning and 27.9% on deep research benchmarks against the strongest per-benchmark baselines. SARL further surpasses methods built on auxiliary supervision or multi-agent coordination, despite operating as a standalone RL framework with no inference-time scaffolding. Beyond final performance, SARL maintains training stability under extended search horizons, a regime where existing methods consistently degrade, enabling sustained gains as task complexity grows.

---


### 32. [Not Where You Think: Protecting Location Privacy Against Reasoning-Based Geolocation](https://arxiv.org/abs/2610.30439)

**<font color=#1a73e8>作者：</font>** Shanghao Shi, Jian Xiao, Hao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent large reasoning models can infer where ordinary photos were taken using only visual information, creating a serious location privacy risk even when metadata and obvious geographic identifiers are removed. To understand the mechanism behind such fine-grained localization, we develop GeoTrace, a structured reasoning attack that exposes how models extract location-relevant visual clues and compose them through coarse-to-fine geographic reasoning. We evaluate GeoTrace on a worldwide benchmark of 525 ordinary images spanning natural, urban, residential, and human-centered scenes while excluding famous landmarks and direct location indicators. Our results show that GeoTrace localizes 25.71% of images within 1 km with Gemini-3-Flash and 16.95% with GPT-5-mini. More importantly, our analysis reveals a key insight in the visual clue chain: broad scene properties mainly support coarse localization, whereas precise localization disproportionately relies on small, distinctive, and editable local clues. Building on this insight, we develop GeoShift, a proactive user-side defense that breaks the visual clue chain before image release. Rather than simply removing geographic evidence, GeoShift preserves stable scene properties, selects a visually compatible false target location, and strategically rewrites high-impact geo-revealing clues to construct a coherent alternative geographic hypothesis. Experiments show that GeoShift reduces street-level localization from 16.95% to 2.48% under GPT-5-mini and from 25.71% to 3.81% under Gemini-3-Flash, while preserving visual quality and remaining effective against adaptive attacks.

---


### 33. [Same Beliefs, Different Policies: Learning Reusable Representations for Early Stopping in LLM Reasoning](https://arxiv.org/abs/2610.30450)

**<font color=#1a73e8>作者：</font>** Jingwei Ni, Dmitry Abulkhanov, Vladislav Smirnov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning LLMs often continue reasoning after reaching a correct answer, wasting computation and sometimes replacing it with an incorrect one. Deciding when to stop is a metareasoning problem: the model must weigh what further reasoning could achieve against its cost, given what it can already answer. Direct utility training learns a stopping representation at a chosen token price; supporting new prices can require additional controller training. We introduce BELT (BELief-based Termination), which separates outcome prediction from stopping control. It learns beliefs about current and future answers from a frozen LLM's hidden states, then fits a linear stopping policy on the frozen features. The prediction targets are independent of token price, so one probe supports different accuracy-cost trade-offs through CPU policy refitting or threshold adjustment. Averaged over five out-of-distribution (OOD) math benchmarks, BELT reduces generated tokens by 41% on Qwen3-1.7B and 51% on OLMo-3-7B-Think without loss of accuracy. The same math-trained BELT transfers to coding and agentic tasks without training on code or agentic data. In all three domains, its accuracy-cost trade-offs are competitive with or better than those of end-to-end controllers. On OLMo3, its probe has 21.2x fewer parameters than one checkpoint of the strongest baseline, OS-Pruner, and needs 55x fewer training GPU-hours than OS-Pruner's five price-specific checkpoints.

---


### 34. [Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences](https://arxiv.org/abs/2610.30485)

**<font color=#1a73e8>作者：</font>** Jialin Li, Zhenhao Chen, Hanjun Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal intelligence systems are taking on increasingly complex everyday tasks, yet repeated questions, unnecessary confirmations, and unwanted outreach can turn capable assistance into interaction burden. Reducing this burden requires agents to remember how users want to be assisted. However, existing memory benchmarks focus on factual recall and personalized answers and rarely test how agents learn and act on interaction preferences. We introduce MemPABench, an interactive environment for on-policy evaluation of memory in personal agents. MemPABench poses long-horizon tasks requiring agents to decide when to clarify, confirm, or act autonomously. Four grounded simulated users hold 14 preferences across work and personal contexts. Their feedback spans 99 sessions over four months, with five event-driven changes per user testing memory updates. We evaluate preference selection, delivered behavior, and sensitivity to context and preference change. Evaluating four memory systems across four LLM backbones, we find that current memory brings limited gains in preference selection. Retrieval-based systems (i.e. Mem0, MemOS, simple RAG) do not outperform No Memory, while File-based memory improves accuracy but applies preferences beyond relevant contexts. Our analysis shows that current memory struggles to retrieve interaction preferences and adapt to preference changes. Even with the correct preference available, overriding the agent's default interaction habits remains challenging. The environment and dataset are available at this https URL.

---


### 35. [From Single-Actor Environments to Multi-Actor Event Worlds: Can LLMs Be Event World Models?](https://arxiv.org/abs/2610.30488)

**<font color=#1a73e8>作者：</font>** Juntong Ni, Zewen Liu, Bohan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models help agents assess the consequences of their actions before acting. Many real systems, however, involve multiple actors who make their own decisions, can evolve even when the agent takes no action, and are only partially observed through event logs. We formalize these systems as event worlds and ask whether large language models can predict future observations from the log and the agent's proposed actions. We build complementary benchmarks from human Diplomacy games and real Polymarket trades. Our hierarchical framework compares prediction with and without other actors' actions, then tests multi-step rollouts, predictions for actions never taken, and usefulness to agents. Fine-tuning and more data improve prediction when all actors' recorded actions are given. With only the agent's action, models struggle when other actors strongly affect the outcome, and larger models and longer histories help little. This gap also limits multi-step prediction and agent decisions, with models overestimating plan success. Yet imagined experience and initialization from world models can still improve policy learning. Anticipating other actors' actions remains a central challenge for event world modeling.

---


### 36. [What the Trace Shows and What the Label Says: Auditing Behavioral Detectors in Agent Evaluation](https://arxiv.org/abs/2610.30491)

**<font color=#1a73e8>作者：</font>** Idunnuoluwa A. Adeniji, Shilpika, Michael E. Papka  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are often evaluated by reducing execution traces to labels such as final-answer correctness, tool verification, and fault propagation. These labels are measurements produced by parsers, behavioral detectors, and harness rules, and they may not fully capture what the trace shows. We study this in a tool-use setting built on GSM8K, where agents call a calculator whose outputs are occasionally corrupted, giving clear ground truth for what the tool returned, what the model later used, and what the detectors reported. We audit three trace-level detectors across six production models and 30 problems per model. Final correctness, visible re-verification, and fault propagation can disagree in systematic ways. A key failure mode is silent tool-output override: the calculator returns a corrupted value, but the model later uses a different, often correct, value without calling the tool again, so the bad value stops propagating while a verification detector records no re-check. Human review of 90 traces agrees perfectly with the automated labels for final correctness (67/67), fault impact (19/19), and fault relevance (18/18), but only 67/81 for verification; all 14 disagreements fall into four recurring patterns. Execution limits also change the reported result: in an ablation across two models, one ranges from 21/30 to 27/30 correct as step and token budgets change, while the other stays between 27/30 and 29/30. These findings motivate measurement transparency: an automated label should come with the trace evidence behind it, whether the question the detector asks applied to that trace, whether the run was cut off by an execution limit, and any human corrections. Our trace viewer makes this information inspectable alongside the reported results.

---


### 37. [From Prose to Properties: Testing Research Claims with ARATest for Agent-Native Science](https://arxiv.org/abs/2610.30495)

**<font color=#1a73e8>作者：</font>** Yifeng He, Jiachen Liu, Hao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents now run experiments and report findings, so research produces claims faster than researchers can check them. Each empirical claim implies a property that must hold over its cases, but it states that property only in prose. Without an explicit property, no test can decide which evidence would falsify a claim, so validation cannot keep pace with the claims agents produce. To make claims testable, we approximate a claim's semantics by abstracting its property skeleton, a parameterized relation that recurs across claims. We present ARATest, a property-based testing library that checks these skeletons as executable tests. A typed declaration binds a claim to a skeleton and fixes the claim's compared quantities, cases, scope, and numerical policy. A shared case type makes every generator supply cases in the claim's statistical unit. A three-valued semantics assigns each property one of three verdicts: holds, violated, or inconclusive. Every violation carries a replayable witness. A default generator reads the evidence that agent-native research artifacts (ARA) link to each claim, and auto-research generators dispatch an agent to run released code for fresh cases. Our DissClaimer plugin supplies that agent and runs these generators as continuous testing.
Of 243 claims in 33 ARA artifacts, 54 received faithful declarations bound to evidence: 32 held, eight were violated, and 14 remained inconclusive. Two violations exposed errors in published papers that their authors confirmed. ARATest detected all 553 seeded faults without a false alarm on 19 valid controls, outperforming two LLM judges. Fresh runs exposed behaviors that reported evidence could not show. These results suggest that one fixed test can check explicit claim properties against both reported and fresh evidence.

---


### 38. [Can LLMs Improve Their Own Harness? A Controlled Study on ARC-AGI-3](https://arxiv.org/abs/2610.30499)

**<font color=#1a73e8>作者：</font>** Jens Lehmann, Sahar Vahdati  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A generally intelligent system acquires new skills efficiently without requiring humans to redesign its software scaffold for every new task. Yet language models rarely act alone. A harness is a symbolic program that orchestrates calls to the model, handling perception, memory, tool use, recovery, and inference allocation on the model's behalf. ARC-AGI-3 is an interactive benchmark in which agents must explore unfamiliar environments, figure out their goals on the fly, and keep learning as they go. On it, human-steered systems already report ceiling scores across the public games, so we know effective designs exist. We ask whether frontier models can build and improve such a harness on their own. Through a fixed coding bootstrap, each model constructs a complete task harness, acts through that harness on five development games, and revises the entire codebase twice. Every version is evaluated on twenty games that never influence adaptation. We measure task performance with Relative Human Action Efficiency (RHAE), which combines level completion with action efficiency relative to human baselines, and record dollar-denominated inference cost as a practical resource measure. Across 27 lineages, harness performance ranges from zero to near-ceiling scores. Two revisions raise mean held-out RHAE by only 2.80 points (95% interval [-1.44,7.35]). Development gains overstate held-out improvement, and reductions in inference cost can come at the expense of task performance. Human-steered systems demonstrate further headroom. These findings reveal a gap between autonomous harness construction and reliable adaptation under this two-revision protocol: even strong task performance does not ensure that subsequent revisions generalize or preserve existing capabilities.

---


### 39. [Rethinking the Evaluation of LLM Fact-Checkers](https://arxiv.org/abs/2610.30504)

**<font color=#1a73e8>作者：</font>** Ayana Niwa, Miyu Yamada, Kouta Nakayama 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used to answer factual questions, but their answers can contain errors and must be fact-checked claim by claim. Yet the resulting score depends on three design decisions: which questions the claims answer, under what conditions each claim is judged, and which sources count as evidence. No existing benchmark specifies all three. We introduce JSFactCheckBench, a Japanese benchmark that specifies all three, with 1,913 claims from LLM answers to questions about misleading information that circulated on Japanese social media, each annotated for factuality at a reference time and for importance to the question, using evidence from preselected Web sources. Across six LLMs, all verify claims directly answering the question less accurately than supplementary claims, a gap that aggregate scores obscure. Scores also drop when models must locate the relevant content in longer or multiple sources and, for all four open models, when the surrounding question and response are added. These weaknesses are visible only because the benchmark records the conditions behind each label. A benchmark that leaves them implicit cannot reveal them.

---


### 40. [Behind Aggregate Scores: What Systematically Varying Arena-Hard's LLM Judge Reveals](https://arxiv.org/abs/2610.30512)

**<font color=#1a73e8>作者：</font>** Louise Yorke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM judges are used to determine which of two answers is better. Trusting these verdicts requires knowing how repeatable they are and how much they depend on the judge's instructions. We show that similar aggregate scores can conceal substantial changes in individual verdicts, both when the same setup is repeated and when the instructions change. Using 500 Arena-Hard v2.0 prompts with two models' answers held fixed, we run GPT-4.1 as the judge under all eight combinations of criteria, output format and task framing, and repeat every setup unchanged at temperature zero on a pinned model version. Rerunning the default setup moves the aggregate score by about one point but changes the win/tie/loss outcome on 21.2% of prompts. Instruction changes introduce further sensitivity: in one setup, which asks for the verdict without reasoning and also drops several other instructions, outcomes change on 28.2 percentage points more prompts than the two setups' unchanged reruns do on average, and the aggregate score falls by 4.09 points. In another, where the criteria prioritise accuracy, outcomes change on 6.7 percentage points more prompts by the same comparison, while the aggregate score barely moves. A stable aggregate score therefore does not establish that individual verdicts are repeatable. This distinction matters when those verdicts are used as preference labels or to assess individual responses. Evaluations that rely on individual verdicts should repeat each setup they use and report both aggregate scores and prompt-level agreement.

---


### 41. [Beyond End-to-End Recovery: Towards a Better Understanding of LLM Steganography via Rolewise Decomposition](https://arxiv.org/abs/2610.30516)

**<font color=#1a73e8>作者：</font>** Om Tailor, Yucheng Pan, Solaleh Mohammadi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In large language model (LLM) steganography, an encoder hides a private message in an otherwise ordinary response, as text transmitted to a decoder, who attempts to recover it. The success of this private-message transmission is commonly measured through end-to-end (E2E) recovery, which checks whether the decoder correctly reconstructs the private message. However, E2E recovery cannot distinguish encoding failures from decoding failures or reveal how the private message is represented in the encoder's transmitted text. To address these limitations, we introduce a rolewise decomposition framework that separately examines how private messages are represented in encoder transmitted texts, what decoders recover, and what deterministic verification can establish. Across 7,200 encoder responses, we identify 168 verifiable encodings missed by decoders and 706 responses containing private messages reconstructed through word-length or token-initial patterns not explicitly specified in the encoder's instructions. These findings demonstrate that E2E recovery alone may obscure important distinctions between encoding and decoding, motivating their separate evaluation to better understand and mitigate the safety issues caused by LLM steganography.

---


### 42. [IFC-MCQ: Automatically Generating Multiple-Choice Benchmarks for Evaluating LLM Agents on IFC Data Retrieval](https://arxiv.org/abs/2610.30533)

**<font color=#1a73e8>作者：</font>** Rabindra Lamsal, Sisi Zlatanova, Xuesong Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Industry Foundation Classes (IFC), the standard for building information exchange in architecture, engineering, and construction (AEC), is increasingly queried through large language models (LLMs) using natural language. Evaluating these systems at scale is difficult because free-text answers require costly human or LLM-based review. We propose IFC-MCQ, a method that automatically generates multiple-choice benchmarks from IFC files for exact option-set grading. The taxonomy covers 15 categories and 36 subtypes across four groups, with answer keys derived from the file and distractors constructed from file-derived values or predefined rules. We applied IFC-MCQ to IFC models of varying sizes and modelling characteristics to assess generation coverage and evaluated two agentic configurations on selected models using tool- and code-based retrieval. The evaluation exposed category-specific failure modes and showed that performance can vary with the source IFC model and retrieval interface. IFC-MCQ enables scalable benchmarking of LLM-based IFC retrieval in AEC workflows.

---


### 43. [PLE: Physical-Engineering's Last Exam](https://arxiv.org/abs/2610.30537)

**<font color=#1a73e8>作者：</font>** Rujun Han, Yufan Zhuang, Arijit Ray 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier language models now score above 90% on popular knowledge benchmarks and are increasingly deployed as agents that carry out multi-hour professional work. Yet no existing benchmark tests whether they can perform the real-world, economically valuable work of a professional physical engineer, such as modelling physics and legal code requirements across a multi-format project corpus, optimising material and installation costs, and issuing 2D/3D engineering design packages that a licensed reviewer would sign off on. Existing engineering benchmarks focus on textbook question answering, isolated tool calls or self-contained toy design problems. As a result, most of these benchmarks are already saturated by leading agents and solving them is far away from delivering real engineering design. We introduce PLE, a benchmark of 85 long-horizon, agentic tasks in professional physical engineering consisting of electrical, civil, structural and mechanical engineering, where solving a task means completing a realistic, billable engineering deliverable. PLE combines two complementary curation paths. Expert-Authored tasks are created end to end by practising engineers from a professional data provider's expert pool. Co-Authored tasks start from problem statements written by practising engineers; an adversarial Creator-Solver agent pipeline constructs each task's realistic project environment, executable grader and reference deliverables before sending them to expert engineers for validation and difficulty intensification. We evaluate a variety of frontier LLMs under seven publicly available agent harnesses. Even the strongest configuration reaches a mean score of only 50.6%, while spending 27M tokens and 63 minutes per task on average, demonstrating the substantial gap between current agents and autonomous physical engineering design.

---


### 44. [Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core](https://arxiv.org/abs/2610.30557)

**<font color=#1a73e8>作者：</font>** Yebo Feng, Jingyang Dai, Liangrui Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents that act on live Web data must combine heterogeneous evidence, remember what they have done and improve from outcomes without weakening their own safeguards. We study this problem in autonomous investing, where every action is irreversible and based on untrusted Web content. We present Steward, a multi-agent LLM system that draws the boundary of self-evolution in its type system. First, nine role-specialised agents decide jointly: four analysts read news feeds, SEC filings, macroeconomic series and market data and emit typed reports, from which a Portfolio Manager sets target positions that a protected Risk Manager audits. Second, a seven-layer shared memory, assembled by code from the system's own record, gives each decision its position context, the market narrative, calibration and the agent's past decisions. Third, the system improves itself by review: code grades every trade and forecast nightly and writes the grades into memory, and each quarter a reflector proposes prompt learnings that a deterministic gate applies reversibly and replay of recorded inputs verifies. All three operate around an invariant core of order arithmetic, risk rules and discipline-agent prompts that no self-edit can reach. In a five-month live deployment (102 trading days, 1,632 LLM calls), the system contained a 24.6% sector drawdown to a 0.3% loss; in replay of its recorded inputs, a single model given the same raw data traded more and lost 1.35 points against the market over five days where the joint design showed no significant loss, and no injected instruction was followed; and a 2015-2026 backtest shows the core alone lowering the maximum drawdown under all 50 random entry policies. The reflector traced the dominant failure to its root cause, and the gate applied a learning that the agent adopted on trigger evenings and on no control evening. Code: this https URL

---


### 45. [When News Gets Old: Portfolio Allocation with Reinforcement Learning and Large Language Models](https://arxiv.org/abs/2610.30564)

**<font color=#1a73e8>作者：</font>** Bolin Song, Surui Xiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial news can influence investment decisions long after publication. Timely news may reach an investor before prices fully adjust, whereas older news may already be reflected in prices. We examine two ways to handle aging signals: retain them and give a portfolio policy timing information, or filter them out before portfolio selection. A fixed large language model (LLM) extracts signals from public SEC disclosures. We compare these treatments in reinforcement learning (RL) policies and LLMs that choose portfolios directly. We evaluate returns after trading costs in historical tests over 2023-2025. RL choices respond to timing information in a controlled test, but historical returns show no consistent benefit from adding it. For the LLM, filtering old news produced the highest average net return, reaching 18.43% per year when news delivery was delayed by four weeks. This exceeded the returns of all RL strategies that used news.

---


### 46. [Beyond Better Ideas: How Human-AI Collaboration Shapes Scientific Ideas and Human Perceptions](https://arxiv.org/abs/2610.30568)

**<font color=#1a73e8>作者：</font>** Qian Chen, Saatvik Pradhan, Janice Ahn 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI increasingly becomes a collaborator in scientific research, its impact may extend beyond improving ideas to reshaping how they are evaluated, attributed, and perceived by humans. Yet existing research has largely examined these dimensions in isolation. We present a unified empirical study of Human-AI scientific ideation, investigating two complementary perspectives: i) how AI collaboration shapes scientific ideas and their evaluation, and ii) how firsthand collaboration reshapes human perceptions of AI. Through a shared experimental setting involving Human-AI and Human-Human research teams, human and LLM evaluators, collaboration-provenance analysis, and participant surveys, we uncover several counterintuitive findings. First, AI collaboration shows no significant advantage in human-evaluated idea quality, while iterative revision consistently improves quality. Second, AI judges can approximate human scores yet disagree on idea rankings; notably, an AI judge favors AI-assisted proposals without a corresponding advantage in human evaluations. Third, collaboration provenance remains only partially detectable, revealing substantial overlap between Human-AI and Human-Human scientific outputs. Finally, firsthand AI collaboration is associated with greater perceived usefulness but smaller efficiency gains than expected, suggesting a nuanced recalibration of human expectations. Overall, our findings challenge the notion that AI's value in scientific ideation lies primarily in producing better ideas, revealing instead its broader influence on scientific creation, evaluation, attribution, and human perceptions.

---


### 47. [Model Organisms of Collusion: Corrective Transfer in Untrusted Monitors](https://arxiv.org/abs/2610.30582)

**<font color=#1a73e8>作者：</font>** Juan-Pablo Rivera, Ari Spiesberger, Juan J Vazquez 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI control protocols aim to get useful work from models that may be misaligned by monitoring their behaviour. One approach uses a second copy of the same model as the monitor. This avoids relying on a weaker reviewer the model could outsmart, but risks collusion: the model, now monitoring itself, may cover up its own misbehaviour. One remedy is to fine-tune the monitor on whatever examples of misbehaviour the control team has caught. We ask whether this training also removes collusion that the control team has not yet found. We fine-tune Llama-3.3-70B and Qwen2.5-72B to install five policy-monitor behaviour pairs, correct the monitor on 300 honest reviews of one caught collusion, and measure collusion on the other four in unseen prompt formats. Averaged over the three seeds of each family, correction reduces held-out collusion from 91% to 14-20% under three of the four methods we compare (individual seeds 10-32%), while a control fine-tuned on the same number of unrelated examples leaves 56-93%. Family-average accuracy on control items changes by at most five points and capability is preserved, apart from a drop in mathematical accuracy on one Llama seed. Under the tested training configuration, methods with similar caught-task accuracy differ in held-out transfer, from 58% to 83% average reduction, so the caught behaviour alone does not reveal how far a correction reaches. Catching one collusion lets the control team reduce, but not remove, collusion it has not caught, by retraining the monitor alone.

---


### 48. [Visual Grounding First, Multimodal In-context Learning Follows](https://arxiv.org/abs/2610.30592)

**<font color=#1a73e8>作者：</font>** Minhyuk Seo, Minjae Lee, Chaeeun Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LLMs have shown strong in-context learning (ICL) capability, but extending it to Multimodal LLMs (MLLMs) remains challenging. Prior multimodal ICL methods often rely on ICL-specific datasets for additional training or task vector extraction, which can improve performance on the same ICL benchmark used for adaptation. However, they do not generalize well to other benchmarks and often induce forgetting in previously well-solved tasks. For this reason, we identify 'visual grounding' as the key bottleneck in multimodal ICL; MLLMs often fail to attend to task-relevant visual evidence in demonstrations, instead over-relying on textual cues and producing hallucinated outputs. To address this, we propose ProCoRe to enhance visual grounding through contrastive reinforcement learning on multimodal contrastive data for improving multimodal ICL. ProCoRe generates captions for contrastive image pairs, decomposes them into propositions, and optimizes contrastive rewards that encourage alignment with corresponding images while discouraging mismatched ones. Despite never seeing ICL-formatted training examples, ProCoRe improves average multimodal ICL classification accuracy by 5.6% and captioning ROUGE-L by 13.8% over the off-the-shelf Qwen-VL-3-8B model, outperforming ICL-data-dependent state of the arts across benchmarks. Finally, we introduce PICL, a personalized multimodal ICL captioning benchmark that tests whether MLLMs genuinely understand visual demonstrations rather than relying on pre-trained semantic priors.

---


### 49. [Impacts of generative AI skill development on academic adaptation and learning outcomes among university students](https://arxiv.org/abs/2610.30599)

**<font color=#1a73e8>作者：</font>** Lei Fan, Fangxue Liu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding how university students perceive the development of their generative artificial intelligence (GenAI) skills over time can clarify how GenAI use relates to learning and academic outcomes. This study examined perceived skill-development trajectories, changes in learning practices, and associated academic gains using a retrospective questionnaire with 313 analyzed responses and interviews with 18 students across subject areas. Descriptive and comparative analyses and exploratory structural equation modeling (SEM) were integrated with thematic analysis. Perceived developmental trajectories were heterogeneous: 34.2% of students reported rapid early improvement followed by a plateau, 28.4% steady improvement, and 21.1% delayed acceleration. Development was also uneven across skills, with improvement in evaluating GenAI outputs perceived as more challenging; assignments were the most frequently selected driver of skill growth. Interviews further indicated increasingly specific prompting, tailored verification, and selective delegation, although some students reported stable routines, dependence, skipped reasoning, or improvements attributable partly to better GenAI tools. Academic gains were reported more often for assignments than for examinations. The SEM indicated a positive indirect association between perceived skill growth and academic gains through adaptation of assignment processes, whereas academic gains did not clearly differ across developmental trajectory groups after multiplicity correction. The findings suggest that perceived GenAI skill development varies in both trajectory and skill domain and is associated with changes in learning practices and differentiated academic benefits.

---


### 50. [Better Reasoning, Not Just Bigger Models: A Structure-Grounded Framework for Efficient and Reliable Inference](https://arxiv.org/abs/2610.30611)

**<font color=#1a73e8>作者：</font>** Amirhossein Aghaei, Liangyan Li, Shiyi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling large language models has substantially improved linguistic fluency, yet reliable autonomous agents require more than fluent generation. In multi-turn inference, current agentic systems often produce semantically plausible but structurally ungrounded reasoning, especially under incomplete observations. We propose Structure-Grounded Uncertainty Reduction (SGUR), a training-free framework that complements token-level generation with active uncertainty reduction over structured hypothesis spaces. SGUR represents incomplete observations as a query graph and aligns them with candidate hypothesis graphs through a prior-weighted partial graph matching mechanism, where database-derived empirical priors assign greater importance to decision-relevant relations rather than treating all graph edges uniformly. The resulting inference state is iteratively refined by an active information-gain strategy that selects the next most informative node to query, systematically pruning the candidate space. We instantiate SGUR on a challenging PrimeKG-derived sequential medical diagnosis benchmark, demonstrating that structural grounding can partially substitute for model scale: starting from only two observed symptoms, SGUR achieves 92.5% Hit@3, outperforming the strongest Graph-RAG baseline by 9.4 percentage points while using approximately 5x fewer tokens. Notably, SGUR enables smaller backbone models to match or exceed the performance of models up to 10x larger, suggesting that structural grounding provides a more robust and efficient paradigm for scaling agent performance than relying exclusively on increasing model size.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-241](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
